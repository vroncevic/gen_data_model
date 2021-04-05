<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_data_model/dev/docs/gen_data_model_logo.png" width="25%">

# Generate Data Model (Django/Flask/SQLAlchemy)

**gen_data_model** is tool generator of data model for:

* Django FWK
* Flask FWK
* SQLAlchemy FWK

Developed in **[python](https://www.python.org/)** code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/gen_data_model/workflows/Python%20package%20gen_data_model/badge.svg?branch=master) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_data_model.svg)](https://github.com/vroncevic/gen_data_model/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_data_model.svg)](https://github.com/vroncevic/gen_data_model/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using setuptools](#install-using-setuptools)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Generation flow of data model](#generation-flow-of-data-model)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

![Install Python2 Package](https://github.com/vroncevic/gen_data_model/workflows/Install%20Python2%20Package%20gen_data_model/badge.svg?branch=master) ![Install Python3 Package](https://github.com/vroncevic/gen_data_model/workflows/Install%20Python3%20Package%20gen_data_model/badge.svg?branch=master)

Currently there are three ways to install tool:
* Install process based on pip
* Install process based on setup.py (setuptools)
* Install process based on docker mechanism

##### Install using pip

Python package is located at **[pypi.org](https://pypi.org/project/gen_data_model/)**.

You can install by using pip
```
#python2
pip install gen_data_model
#python3
pip3 install gen_data_model
```

##### Install using setuptools

Navigate to **[release page](https://github.com/vroncevic/gen_data_model/releases)** download and extract release archive.

To install modules, locate and run setup.py, type the following:
```
tar xvzf gen_data_model-x.y.z.tar.gz
cd gen_data_model-x.y.z
#python2
pip install -r requirements.txt
python setup.py install_lib
python setup.py install_egg_info
python setup.py install_data
#python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
python3 setup.py install_data
```

##### Install using docker

You can use Dockerfile to create image/container.

[![gen_data_model docker checker](https://github.com/vroncevic/gen_data_model/workflows/gen_data_model%20docker%20checker/badge.svg)](https://github.com/vroncevic/gen_data_model/actions?query=workflow%3A%22gen_data_model+docker+checker%22)

### Dependencies

**gen_data_model** requires next modules and libraries:

* [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/ats_utilities)
* [Flask-WTF - Simple integration of Flask and WTForms](https://pypi.org/project/Flask-WTF/)
* [Django - High-level Python Web framework](https://pypi.org/project/Django/)
* [SQLAlchemy -  SQL Toolkit and Object Relational Mapper](https://pypi.org/project/SQLAlchemy/)

### Generation flow of data model

Base flow of generation process:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_data_model/dev/docs/gen_data_model_flow.png)

### Tool structure

**gen_data_model** is based on OOP:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_data_model/dev/docs/gen_data_model.png)

Generator structure:

```
gen_data_model/
├── conf/
│   ├── data_model_types.yaml
│   ├── gen_data_model.cfg
│   ├── gen_data_model_util.cfg
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
│   ├── model_selector.py
│   ├── read_template.py
│   └── write_template.py
└── run/
    └── gen_data_model_run.py
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_data_model/badge/?version=latest)](https://gen_data_model.readthedocs.io/projects/gen_data_model/en/latest/?badge=latest)

More documentation and info at:
* [gen_data_model.readthedocs.io](https://gen_data_model.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 by [vroncevic.github.io/gen_data_model](https://vroncevic.github.io/gen_data_model/)

**gen_data_model** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_data_model/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
