miniwdl-slurm
=============
Extends miniwdl to run workflows on SLURM clusters in singularity containers.

This `SLURM backend
<https://miniwdl.readthedocs.io/en/latest/runner_backends.html>`_ plugin for
`miniwdl <https://github.com/chanzuckerberg/miniwdl>`_ runs WDL task containers
by creating a job script that is submitted to a SLURM cluster. In case the job
description has a container, singularity will be used as container runtime.

Installation
------------
For the development version::

    pip install git+https://github.com/Pkoiralap/miniwdl-slurm-mem-per-cpu

Configuration
--------------
The following `miniwdl configuration
<https://miniwdl.readthedocs.io/en/latest/runner_reference.html#configuration>`_
example can be used to use miniwdl on a SLURM cluster:

.. code-block:: ini

    [scheduler]
    container_backend=slurm_singularity
    # task_concurrency defaults to the number of processors on the system.
    # since we submit the jobs to SLURM this is not necessary.
    # higher numbers means miniwdl has to monitor more processes simultaneously
    # which might impact performance.
    task_concurrency=200
    
    # This setting allows running tasks to continue, even if one other tasks fails. 
    # Useful in combination with call caching. Prevents wasting resources by
    # cancelling jobs half-way that would probably succeed.
    fail_fast = false

    [call_cache]
    # The following settings create a call cache under the current directory.
    # This prevents wasting unnecessary resources on the cluster by rerunning 
    # jobs that have already succeeded.
    put = true 
    get = true 
    dir = "$PWD/miniwdl_call_cache"

    [task_runtime]
    # Setting a 'maxRetries' default allows jobs that fail due to intermittent
    # errors on the cluster to be retried.
    defaults = {
            "maxRetries": 2,
            "docker": "ubuntu:20.04"
        }
 
    [singularity]
    # This plugin wraps the singularity backend. Make sure the settings are
    # appropriate for your cluster.
    exe = ["singularity"]

    # the miniwdl default options contain options to run as a fake root, which
    # is not available on most clusters.
    run_options = [
            "--containall"
        ]

    # Location of the singularity images (optional). The miniwdl-slurm plugin
    # will set it to a directory inside $PWD. This location must be reachable
    # for the submit nodes.
    image_cache = "$PWD/miniwdl_singularity_cache"

    [slurm]
    # extra arguments passed to the sbatch command (optional).
    extra_args="--partition heavy_users,gpu --comment 'run with miniwdl'"

    [slurm_custom]
    # do either or, don't do both
    mem_per_cpu="8G"
    #mem_per_gpu="8G"
