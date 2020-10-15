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
- [Dependencies](#dependencies)
- [Generation flow of data model](#generation-flow-of-data-model)
- [Tool structure](#tool-structure)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Navigate to release **[page](https://github.com/vroncevic/gen_data_model/releases/tag/v1.0)** download and extract release archive.

To install **gen_data_model** type the following:

```
tar xvzf gen_data_model-x.y.z.tar.gz
cd gen_data_model-x.y.z
pip install -r requirements.txt
```

Install lib process
```
python setup.py install_lib
running install_lib
running build_py
creating build
creating build/lib.linux-x86_64-2.7
creating build/lib.linux-x86_64-2.7/gen_data_model
copying gen_data_model/__init__.py -> build/lib.linux-x86_64-2.7/gen_data_model
creating build/lib.linux-x86_64-2.7/gen_data_model/model
copying gen_data_model/model/__init__.py -> build/lib.linux-x86_64-2.7/gen_data_model/model
copying gen_data_model/model/write_template.py -> build/lib.linux-x86_64-2.7/gen_data_model/model
copying gen_data_model/model/gen_model.py -> build/lib.linux-x86_64-2.7/gen_data_model/model
copying gen_data_model/model/read_template.py -> build/lib.linux-x86_64-2.7/gen_data_model/model
copying gen_data_model/model/model_selector.py -> build/lib.linux-x86_64-2.7/gen_data_model/model
creating /usr/local/lib/python2.7/dist-packages/gen_data_model
creating /usr/local/lib/python2.7/dist-packages/gen_data_model/model
copying build/lib.linux-x86_64-2.7/gen_data_model/model/__init__.py -> /usr/local/lib/python2.7/dist-packages/gen_data_model/model
copying build/lib.linux-x86_64-2.7/gen_data_model/model/write_template.py -> /usr/local/lib/python2.7/dist-packages/gen_data_model/model
copying build/lib.linux-x86_64-2.7/gen_data_model/model/gen_model.py -> /usr/local/lib/python2.7/dist-packages/gen_data_model/model
copying build/lib.linux-x86_64-2.7/gen_data_model/model/read_template.py -> /usr/local/lib/python2.7/dist-packages/gen_data_model/model
copying build/lib.linux-x86_64-2.7/gen_data_model/model/model_selector.py -> /usr/local/lib/python2.7/dist-packages/gen_data_model/model
copying build/lib.linux-x86_64-2.7/gen_data_model/__init__.py -> /usr/local/lib/python2.7/dist-packages/gen_data_model
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_data_model/model/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_data_model/model/write_template.py to write_template.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_data_model/model/gen_model.py to gen_model.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_data_model/model/read_template.py to read_template.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_data_model/model/model_selector.py to model_selector.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_data_model/__init__.py to __init__.pyc
```

Install lib egg info
```
python setup.py install_egg_info
running install_egg_info
running egg_info
creating gen_data_model.egg-info
writing requirements to gen_data_model.egg-info/requires.txt
writing gen_data_model.egg-info/PKG-INFO
writing top-level names to gen_data_model.egg-info/top_level.txt
writing dependency_links to gen_data_model.egg-info/dependency_links.txt
writing manifest file 'gen_data_model.egg-info/SOURCES.txt'
reading manifest file 'gen_data_model.egg-info/SOURCES.txt'
writing manifest file 'gen_data_model.egg-info/SOURCES.txt'
Copying gen_data_model.egg-info to /usr/local/lib/python2.7/dist-packages/gen_data_model-1.0.0-py2.7.egg-info
```

Install lib data
```
python setup.py install_data
running install_data
copying gen_data_model/run/gen_data_model_run.py -> /usr/local/bin/
creating /usr/local/lib/python2.7/dist-packages/gen_data_model/conf
copying gen_data_model/conf/gen_data_model.cfg -> /usr/local/lib/python2.7/dist-packages/gen_data_model/conf/
copying gen_data_model/conf/gen_data_model_util.cfg -> /usr/local/lib/python2.7/dist-packages/gen_data_model/conf/
creating /usr/local/lib/python2.7/dist-packages/gen_data_model/conf/template
copying gen_data_model/conf/template/django.template -> /usr/local/lib/python2.7/dist-packages/gen_data_model/conf/template/
copying gen_data_model/conf/template/flask.template -> /usr/local/lib/python2.7/dist-packages/gen_data_model/conf/template/
copying gen_data_model/conf/template/sqlalchemy.template -> /usr/local/lib/python2.7/dist-packages/gen_data_model/conf/template/
copying gen_data_model/conf/template/django_base_model.template -> /usr/local/lib/python2.7/dist-packages/gen_data_model/conf/template/
copying gen_data_model/conf/template/flask_base_model.template -> /usr/local/lib/python2.7/dist-packages/gen_data_model/conf/template/
copying gen_data_model/conf/template/sqlalchemy_base_model.template -> /usr/local/lib/python2.7/dist-packages/gen_data_model/conf/template/
creating /usr/local/lib/python2.7/dist-packages/gen_data_model/log
copying gen_data_model/log/gen_data_model.log -> /usr/local/lib/python2.7/dist-packages/gen_data_model/log/
```

Or You can use docker to create image/container.

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

**gen_data_model** is based on Template mechanism:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_data_model/dev/docs/gen_data_model.png)

Generator structure:

```
.
├── conf/
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
├── model/
│   ├── gen_model.py
│   ├── __init__.py
│   ├── model_selector.py
│   ├── read_template.py
│   └── write_template.py
└── run/
    └── gen_data_model_run.py
```

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2018 by [vroncevic.github.io/gen_data_model](https://vroncevic.github.io/gen_data_model/)

**gen_data_model** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.7/3.4 or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_data_model/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
