# Generate Data Model (Django/Flask/SQLAlchemy/Pydantic/Dataclass/SQLModel)

<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_data_model/dev/docs/gen_data_model_logo.png" width="25%">

**gen_data_model** is tool generator of data model for

* Django FWK
* Flask FWK
* SQLAlchemy FWK
* Pydantic V2
* Python Dataclass
* SQLModel FWK

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![gen_data_model python checker](https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_python_checker.yml/badge.svg)](https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_python_checker.yml) [![gen_data_model package checker](https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_package_checker.yml/badge.svg)](https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_package.yml) [![gen_data_model interface checker](https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_interface_checker.yml/badge.svg)](https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_interface_checker.yml) [![gen_data_model isp checker](https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_isp_checker.yml/badge.svg)](https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_isp_checker.yml) [![gen_data_model srp checker](https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_srp_checker.yml/badge.svg)](https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_srp_checker.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_data_model.svg)](https://github.com/vroncevic/gen_data_model/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_data_model.svg)](https://github.com/vroncevic/gen_data_model/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [🚀 Installation](#-installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [📦 Dependencies](#-dependencies)
- [📁 Tool structure](#-tool-structure)
- [📊 Code coverage](#-code-coverage)
- [📚 Docs](#-docs)
- [👥 Contributing](#-contributing)
- [📄 Copyright and licence](#-copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### 🚀 Installation
Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/gen_data_model/dev/docs/debtux.png)

[![gen_data_model python3 build](https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_python3_build.yml/badge.svg)](https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_python3_build.yml)

Currently there are three ways to install tool
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

Python is located at **[pypi.org](https://pypi.org/project/gen_data_model/)**.

You can install by using pip

```bash
#python3
pip3 install gen_data_model
```

##### Install using build

Navigate to **[release page](https://github.com/vroncevic/gen_data_model/releases)** download and extract release archive.

To install **gen_data_model** run

```bash
tar xvzf gen_data_model-x.y.z.tar.gz
cd gen_data_model-x.y.z
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build --no-isolation --wheel
pip3 install dist/gen_data_model-x.y.z-py3-none-any.whl
rm -f get-pip.py
```

##### Install using py setup

Navigate to **[release page](https://github.com/vroncevic/gen_data_model/releases)** download and extract release archive.

To install **gen_data_model** locate and run setup.py

```bash
tar xvzf gen_data_model-x.y.z.tar.gz
cd gen_data_model-x.y.z
#python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
python3 setup.py install_data
```

##### Install using docker

You can use Dockerfile to create image/container.

### 📦 Dependencies
**gen_data_model** requires next modules and libraries

* [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/gen_data_model)

### 📁 Tool structure

**gen_data_model** is based on OOP.

Tool structure

<details>
<summary><b>Click to expand framework structure</b></summary>

```bash
    gen_data_model/
         ├── core/
         │   ├── __init__.py
         │   ├── model/
         │   │   ├── __init__.py
         │   │   └── model_setup.py
         │   └── service/
         │       ├── engine.py
         │       ├── __init__.py
         │       ├── iservice.py
         │       └── isubprocessor.py
         ├── engine.py
         ├── infrastructure/
         │   ├── cli/
         │   │   ├── engine.py
         │   │   ├── icli.py
         │   │   ├── __init__.py
         │   │   └── setup/
         │   │       ├── bundle.py
         │   │       ├── dep_validator.py
         │   │       ├── dependencies.py
         │   │       ├── factory.py
         │   │       ├── __init__.py
         │   │       ├── keys.py
         │   │       ├── opt_validator.py
         │   │       ├── options.py
         │   │       ├── registry.py
         │   │       └── validator.py
         │   ├── command/
         │   │   ├── command.py
         │   │   ├── gen_model_command_definition.py
         │   │   ├── gen_model_command_executor.py
         │   │   ├── icommand_definition.py
         │   │   ├── icommand_executor.py
         │   │   └── __init__.py
         │   ├── config/
         │   │   ├── gen_data_model.cfg
         │   │   ├── gen_data_model.logo
         │   │   ├── scheme.json
         │   │   └── templates.tgz
         │   ├── __init__.py
         │   └── subprocessor.py
         ├── __init__.py
         ├── py.typed
         └── setup/
             ├── bundle.py
             ├── dep_validator.py
             ├── dependencies.py
             ├── factory.py
             ├── __init__.py
             ├── keys.py
             ├── opt_validator.py
             ├── options.py
             ├── registry.py
             └── validator.py

     10 directories, 45 files
```
</details>

### 📊 Code coverage

<details>
<summary><b>Click to expand code coverage</b></summary>

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `gen_data_model/__init__.py` | 9 | 0 | 100%|
| `gen_data_model/core/__init__.py` | 9 | 0 | 100%|
| `gen_data_model/core/model/__init__.py` | 9 | 0 | 100%|
| `gen_data_model/core/model/model_setup.py` | 14 | 0 | 100%|
| `gen_data_model/core/service/__init__.py` | 9 | 0 | 100%|
| `gen_data_model/core/service/engine.py` | 27 | 0 | 100%|
| `gen_data_model/core/service/iservice.py` | 14 | 0 | 100%|
| `gen_data_model/core/service/isubprocessor.py` | 14 | 0 | 100%|
| `gen_data_model/engine.py` | 57 | 0 | 100%|
| `gen_data_model/infrastructure/__init__.py` | 9 | 0 | 100%|
| `gen_data_model/infrastructure/cli/__init__.py` | 9 | 0 | 100%|
| `gen_data_model/infrastructure/cli/engine.py` | 39 | 0 | 100%|
| `gen_data_model/infrastructure/cli/icli.py` | 14 | 0 | 100%|
| `gen_data_model/infrastructure/cli/setup/__init__.py` | 9 | 0 | 100%|
| `gen_data_model/infrastructure/cli/setup/bundle.py` | 22 | 0 | 100%|
| `gen_data_model/infrastructure/cli/setup/dep_validator.py` | 36 | 0 | 100%|
| `gen_data_model/infrastructure/cli/setup/dependencies.py` | 18 | 0 | 100%|
| `gen_data_model/infrastructure/cli/setup/factory.py` | 35 | 0 | 100%|
| `gen_data_model/infrastructure/cli/setup/keys.py` | 26 | 0 | 100%|
| `gen_data_model/infrastructure/cli/setup/opt_validator.py` | 34 | 0 | 100%|
| `gen_data_model/infrastructure/cli/setup/options.py` | 15 | 0 | 100%|
| `gen_data_model/infrastructure/cli/setup/registry.py` | 30 | 0 | 100%|
| `gen_data_model/infrastructure/cli/setup/validator.py` | 43 | 0 | 100%|
| `gen_data_model/infrastructure/command/__init__.py` | 9 | 0 | 100%|
| `gen_data_model/infrastructure/command/command.py` | 16 | 0 | 100%|
| `gen_data_model/infrastructure/command/gen_model_command_definition.py` | 24 | 0 | 100%|
| `gen_data_model/infrastructure/command/gen_model_command_executor.py` | 23 | 0 | 100%|
| `gen_data_model/infrastructure/command/icommand_definition.py` | 14 | 0 | 100%|
| `gen_data_model/infrastructure/command/icommand_executor.py` | 14 | 0 | 100%|
| `gen_data_model/infrastructure/subprocessor.py` | 56 | 0 | 100%|
| `gen_data_model/setup/__init__.py` | 9 | 0 | 100%|
| `gen_data_model/setup/bundle.py` | 23 | 0 | 100%|
| `gen_data_model/setup/dep_validator.py` | 36 | 0 | 100%|
| `gen_data_model/setup/dependencies.py` | 19 | 0 | 100%|
| `gen_data_model/setup/factory.py` | 49 | 0 | 100%|
| `gen_data_model/setup/keys.py` | 27 | 0 | 100%|
| `gen_data_model/setup/opt_validator.py` | 34 | 0 | 100%|
| `gen_data_model/setup/options.py` | 12 | 0 | 100%|
| `gen_data_model/setup/registry.py` | 32 | 0 | 100%|
| `gen_data_model/setup/validator.py` | 48 | 0 | 100%|
| **Total** | 946 | 0 | 100% |

</details>

### 📚 Docs
[![Documentation Status](https://readthedocs.org/projects/gen-data-model/badge/?version=latest)](https://gen-data-model.readthedocs.io/projects/gen_data_model/en/latest/?badge=latest)

More documentation and info at

* [gen_data_model.readthedocs.io](https://gen-data-model.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### 👥 Contributing
[Contributing to gen_data_model](CONTRIBUTING.md)

### 📄 Copyright and licence
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 - 2026 by [vroncevic.github.io/gen_data_model](https://vroncevic.github.io/gen_data_model/)

**gen_data_model** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_data_model/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
