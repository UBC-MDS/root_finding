# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

### Unreleased
- setup workflow for code coverage with codecov and documentation preview with netlify
- Add badges for linting, MIT license, codecov, netlify python version, testpypi version
- fix documentation website link in README.md in [issue 78](https://github.com/UBC-MDS/root_finding/issues/78) mentioned in parent issues [issue 61](https://github.com/UBC-MDS/root_finding/issues/61) comment 3, [issue 76](https://github.com/UBC-MDS/root_finding/issues/76) comment 2 and [issue 74](https://github.com/UBC-MDS/root_finding/issues/61) comment 3
- add documentation to test functions in test_hybrid.py and test_plot_root.py as suggested by TA's feedback
## [0.0.4] - (2026-02-02)

### Fixed
- Fix installation instructions in README - provide working GitHub installation command instead of non-existent PyPI package 
- Fix documentation links in README - update to point to deployed documentation site instead of GitHub repository 
- Add testing dependencies installation step in README for developers 
- Simplify public API usage examples in README - use top-level imports instead of deep module paths 
- Add reminder about testing dependencies in "Running Tests" section

### Changed
- Update README to address peer review feedback

## [0.0.3] - (2026-01-24)

- Add github actions workflow to automate pytest + formatting
- Add github actions workflow to deploy package + test
- Add github actions workflow to update documnetation
- Add a few unit tests

## [0.0.2] - (2026-01-17)

- Update documentation for bisection.py
- Add tests and function body for bisection.py
- Add tests and function body for bisection_find_roots.py
- update dependencies in pyproject.toml
- add evironment.yml
- Add tests and function body for newton1d.py

## [0.0.1] - (2026-01-10)

- Update code of conduct enforcement contact
- Add documentation for bisection.py
- Add documentation for newton1d.py
- Add documentation for hybrid.py
- Add documentation for plot_root.py
- reformat .py files

- First release
