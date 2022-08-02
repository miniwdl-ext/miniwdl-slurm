# Copyright (c) 2022 Leiden University Medical Center
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import logging
import shlex
import sys
from contextlib import ExitStack
from typing import Callable, Dict, List

from WDL.runtime.backend.singularity import SingularityContainer
from WDL.runtime import config
from WDL.runtime.backend.cli_subprocess import _SubprocessScheduler
from WDL._util import StructuredLogMessage


class SlurmSingularityRun(SingularityContainer):
    @classmethod
    def global_init(cls, cfg: config.Loader, logger: logging.Logger) -> None:

        # TODO: Query from cluster. This requires parsing sinfo output and
        # determining which partition etc. etc.
        cls._resource_limits = {
            "cpu": sys.maxsize,
            "mem_bytes": sys.maxsize,
            "time": sys.maxsize,
        }
        _SubprocessScheduler.global_init(cls._resource_limits)
        # Since we run on the cluster, the images need to be placed in a
        # shared directory. The singularity cache itself cannot be shared
        # across nodes, as it can become corrupted when nodes pull the same
        # image. The solution is to pull image to a shared directory on the
        # submit node. If no image_cache is given, simply place a folder in
        # the current working directory.
        if cfg.get("singularity", "image_cache") == "":
            cfg.override({"singularity":
                              {"image_cache": "miniwdl_singularity_cache"}})
        SingularityContainer.global_init(cfg, logger)

    @classmethod
    def detect_resource_limits(cls, cfg: config.Loader,
                               logger: logging.Logger) -> Dict[str, int]:
        return cls._resource_limits

    def _slurm_invocation(self):
        # We use srun as this makes the submitted job behave like a local job.
        # This also gives informative exit codes back, including 253 for out
        # of memory.
        srun_args = ["srun"]

        cpu = self.runtime_values.get("cpu", None)
        if cpu is not None:
            srun_args.extend(["--cpus-per-task", str(cpu)])

        memory = self.runtime_values.get("memory_limit", None)
        if memory is not None:
            srun_args.extend(["--mem", f"{memory / (1024 ^ 2)}M"])

        time_minutes = self.runtime_values.get("time_minutes", None)
        if time_minutes is not None:
            srun_args.extend(["--time", str(time_minutes)])

        if self.cfg.has_section("slurm"):
            partition = self.cfg.get("slurm", "partition")
            if partition is not None:
                srun_args.extend(["--partition", partition])

        return srun_args

    def _run_invocation(self, logger: logging.Logger, cleanup: ExitStack,
                        image: str) -> List[str]:
        singularity_command = super()._run_invocation(logger, cleanup, image)

        slurm_invocation = self._slurm_invocation()
        slurm_invocation.extend(["--wrap", " ".join(singularity_command)])
        slurm_invocation_string = ' '.join(shlex.quote(part)
                                           for part in slurm_invocation)
        logger.info(f"Slurm invocation: " + slurm_invocation_string)
        return slurm_invocation

