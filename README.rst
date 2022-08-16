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

.. code-block::

    pip install git+https://github.com/LUMC/miniwdl-slurm.git

Configuration
--------------
