Release checklist
- [ ] Check outstanding issues on Github.
- [ ] Create a release branch.
  - [ ] Change current development version in `CHANGELOG.rst` to stable version.
- [ ] Merge the release branch into `main`.
- [ ] Created an annotated tag with the stable version number. Include changes
from history.rst.
- [ ] Create a test pypi package from the main branch. ([Instructions.](
https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives
))
- [ ] Install the packages from the test pypi repository to see if they work.
- [ ] Push tag to remote.
- [ ] Push tested packages to pypi.
- [ ] merge `main` branch back into `develop`.
- [ ] Add updated version number to develop.
- [ ] Create a new release on github.
- [ ] Update the package on conda-forge.
