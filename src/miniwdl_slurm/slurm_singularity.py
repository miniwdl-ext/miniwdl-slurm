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
import sys
from typing import Callable, Dict

import WDL.runtime.backend.singularity
from WDL.runtime import config
from WDL.runtime.backend.cli_subprocess import _SubprocessScheduler


class SlurmSingularityRun(WDL.runtime.backend.singularity.SingularityContainer):
    @classmethod
    def global_init(cls, cfg: config.Loader, logger: logging.Logger) -> None:
        super().global_init(cfg, logger)

        # TODO: Query from cluster. This requires parsing sinfo output and
        # determining which partition etc. etc.
        cls._resource_limits = {
            "cpu": sys.maxsize,
            "mem_bytes": sys.maxsize,
            "time": sys.maxsize,
        }
        _SubprocessScheduler.global_init(cls._resource_limits)

    @classmethod
    def detect_resource_limits(cls, cfg: config.Loader,
                               logger: logging.Logger) -> Dict[str, int]:
        return super().detect_resource_limits(cfg, logger)

