==========
Changelog
==========

.. Newest changes should be on top.

.. This document is user facing. Please word the changes in such a way
.. that users understand how the changes affect the new version.

version 0.1.0
----------------------------
Initial release with the following features:

+ Utilize miniwdl's singularity backend to create a singularity command that
  is then submitted using srun.
+ Create a singularity image cache so singularity images are available on
  the cluster nodes.
+ Support for ``cpu``, ``memory`` and ``time_minutes`` runtime attributes.
