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

from setuptools import find_packages, setup

with open("README.rst") as fp:
    long_description = fp.read()

setup(
    name="miniwdl-slurm",
    version="0.1.0",
    license="MIT",
    url="https://github.com/miniwdl-ext/miniwdl-slurm",
    description="miniwdl slurm backend using singularity",
    keywords="WDL miniwdl slurm backend singularity",
    long_description=long_description,
    zip_safe=False,
    long_description_content_type="text/x-rst",
    author="Leiden University Medical Center",
    author_email="sasc@lumc.nl",
    python_requires=">=3.6",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=["miniwdl>=1.7.0"],
    entry_points={
        "miniwdl.plugin.container_backend": [
            "slurm_singularity=miniwdl_slurm:SlurmSingularity"
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: System :: Distributed Computing",
    ]
)
