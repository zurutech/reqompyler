# Reqompyler

![Python - Version](https://img.shields.io/pypi/pyversions/reqompyler.svg)
[![PyPy - Version](https://badge.fury.io/py/reqompyler.svg)](https://pypi.org/project/reqompyler/)
![PyPI - License](https://img.shields.io/pypi/l/reqompyler.svg)
[![Reqompyler - Badge](https://img.shields.io/badge/package-reqompyler-brightgreen.svg)](https://pypi.org/project/reqompyler/)
[![Updates](https://pyup.io/repos/github/zurutech/reqompyler/shield.svg)](https://pyup.io/repos/github/zurutech/reqompyler/)
[![Build Status](https://travis-ci.org/zurutech/reqompyler.svg?branch=master)](https://travis-ci.org/zurutech/reqompyler)
[![Documentation Status](https://readthedocs.org/projects/reqompyler/badge/?version=latest)](https://reqompyler.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/zurutech/reqompyler/branch/master/graph/badge.svg)](https://codecov.io/gh/zurutech/reqompyler)
[![CodeFactor](https://www.codefactor.io/repository/github/zurutech/reqompyler/badge)](https://www.codefactor.io/repository/github/zurutech/reqompyler)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)
[![Black - Badge](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Description

Use [pip-tools](https://github.com/jazzband/pip-tools) to compile a requirements.in folder into proper pinned dependencies.

## Installation

```console
pip install reqompyler
```

## Usage

```console
$ reqompyler --help

Usage: reqompyler [OPTIONS]

  Console script for reqompyler.

Options:
  -i, --in PATH      Path to requirements.in folder  [default:
                     ./requirements.in]
  -o, --output PATH  Path to pinned requirements folder  [default:
                     ./requirements]
  --tld PATH         Ideally the top-level-directory of the package (ie, were
                     there is a setup.py). If not None will be used to export
                     a copy of your dev.txt as requirements.txt  [default: .]
  --ignore TEXT      Requirements.in file (without extension) to ignore,
                     if they are required by another they will be used but no dedicated
                     .txt file will be generated.  [default: linting]
  --help             Show this message and exit.

```

## Credits

This package was created with [Cookiecutter] and the [zurutech/cookie-monster] project template.

[Cookiecutter]: https://github.com/audreyr/cookiecutter
[zurutech/cookie-monster]: https://github.com/zurutech/cookie-monster
