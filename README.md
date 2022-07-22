# miniwdl-slurm
Extends miniwdl to run workflows on SLURM clusters in singularity containers.

This example [SLURM backend](
https://miniwdl.readthedocs.io/en/latest/runner_backends.html) plugin for 
[miniwdl](https://github.com/chanzuckerberg/miniwdl) runs WDL task containers 
by creating a job script that is submitted to a SLURM cluster. In case the job
description has a container, singularity will be used as container runtime.

To run the example, cd into a clone of this repo and:

```bash
pip3 install .
export MINIWDL__SCHEDULER__CONTAINER_BACKEND=slurm_singularity
miniwdl run_self_test
```
