==========
Changelog
==========

version 0.3.0-dev
----------------------------
+ Use ``sbatch --wait`` instead of ``srun`` to prevent issues with batch submitted
  miniwdl runs.
+ Always set ``--ntasks 1`` to prevent multiple tasks being spawned.
+ Add support for a ``gpuType`` runtime attribute to specify the type of GPU required.
+ Add support for a ``slurm_partition_gpu`` runtime attribute.
+ Add support for ``slurm_account`` and ``slurm_account_gpu`` runtime attributes.


version 0.2.0
----------------------------
+ Add support for ``slurm_partition`` runtime attribute.
+ Adds support for ``gpu`` and ``gpuCount`` runtime attributes. The ``gpu`` runtime
  attribute is a boolean that indicates whether the task requires a GPU.  The
  ``gpuCount`` runtime attribute is an integer that indicates the number of GPUs
  required by the task.
+ Add support for ``slurm_constraint`` runtime attribute.

version 0.1.0
----------------------------
Initial release with the following features:

+ Utilize miniwdl's singularity backend to create a singularity command that
  is then submitted using srun.
+ Create a singularity image cache so singularity images are available on
  the cluster nodes.
+ Support for ``cpu``, ``memory`` and ``time_minutes`` runtime attributes.
