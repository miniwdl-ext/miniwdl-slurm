==========
Changelog
==========

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
