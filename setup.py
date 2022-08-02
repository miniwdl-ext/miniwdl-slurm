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

from setuptools import setup, find_packages

with open("README.md") as fp:
    long_description = fp.read()

setup(
    name="miniwdl-slurm",
    version="v0.1.0-dev",
    description="miniwdl slurm singularity backend",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Leiden University Medical Center",
    author_email="sasc <at> lumc.nl",
    python_requires=">=3.7",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        "miniwdl@git+https://github.com/rhpvorderman/miniwdl@singularity_cache"],
    entry_points={
        "miniwdl.plugin.container_backend": [
            "slurm_singularity=miniwdl_slurm.slurm_singularity:SlurmSingularityRun"
        ],
    },
)
