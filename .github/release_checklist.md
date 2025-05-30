Release checklist
- [ ] Check outstanding issues on GitHub.
- [ ] Create a release branch.
  - [ ] Change current development version in `CHANGELOG.rst` to stable version.
- [ ] Merge the release branch into `main`.
- [ ] Created an annotated tag with the stable version by using 
      `git tag -a v{VERSION}`. Include changes from `CHANGELOG.rst`.
- [ ] Install the ``build`` package and use ``python -m build .`` to create
      the source distribution and the wheel.
- [ ] Install the package on the cluster to see if it works.
- [ ] Push tag to remote.
- [ ] Push tested packages to pypi.
- [ ] merge `main` branch back into `develop`.
- [ ] Create a new release on GitHub.
- [ ] Update the package on conda-forge.
