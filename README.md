# Generate Data Model (Django/Flask/SQLAlchemy)

<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_data_model/dev/docs/gen_data_model_logo.png" width="25%">

**gen_data_model** is tool generator of data model for

* Django FWK
* Flask FWK
* SQLAlchemy FWK

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![gen_data_model python checker](https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_python_checker.yml/badge.svg)](https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_python_checker.yml) [![gen_data_model package checker](https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_package_checker.yml/badge.svg)](https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_data_model.svg)](https://github.com/vroncevic/gen_data_model/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_data_model.svg)](https://github.com/vroncevic/gen_data_model/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

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

### Dependencies

**gen_data_model** requires next modules and libraries

* [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/gen_data_model)

### Tool structure

**gen_data_model** is based on OOP

Generator structure

```bash
    gen_data_model/
          ├── conf/
          │   ├── gen_data_model.cfg
          │   ├── gen_data_model.logo
          │   ├── gen_data_model_util.cfg
          │   ├── model_types.yaml
          │   └── template/
          │       ├── django_base_model.template
          │       ├── django.template
          │       ├── flask_base_model.template
          │       ├── flask.template
          │       ├── sqlalchemy_base_model.template
          │       └── sqlalchemy.template
          ├── __init__.py
          ├── log/
          │   └── gen_data_model.log
          ├── pro/
          │   ├── __init__.py
          │   ├── read_template.py
          │   └── write_template.py
          ├── py.typed
          └── run/
              └── gen_data_model_run.py
    
    6 directories, 17 files
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_data_model/badge/?version=latest)](https://gen-data-model.readthedocs.io/projects/gen_data_model/en/latest/?badge=latest)

More documentation and info at

* [gen_data_model.readthedocs.io](https://gen-data-model.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Contributing

[Contributing to gen_data_model](CONTRIBUTING.md)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 - 2024 by [vroncevic.github.io/gen_data_model](https://vroncevic.github.io/gen_data_model/)

**gen_data_model** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_data_model/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
