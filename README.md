# Generate Data Model (Django/Flask/SQLAlchemy).

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

### INSTALLATION

To install this set of modules type the following:

```
cp -R ~/gen_data_model/bin/   /root/scripts/gen_data_model/ver.1.0/
cp -R ~/gen_data_model/conf/  /root/scripts/gen_data_model/ver.1.0/
cp -R ~/gen_data_model/log/   /root/scripts/gen_data_model/ver.1.0/
```

### DEPENDENCIES

This module requires these other modules and libraries:

* ats_utilities https://vroncevic.github.io/ats_utilities

### Tool structure

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_data_model/dev/python-tool-docs/gen_data_model.png)

```
├── bin
│   ├── gen_data_model.py
│   ├── gen_data_model_run.py
│   └── model
│       ├── gen_model.py
│       ├── __init__.py
│       ├── model_selector.py
│       ├── read_template.py
│       └── write_template.py
├── conf
│   ├── gen_data_model.cfg
│   ├── gen_data_model_util.cfg
│   └── template
│       ├── django_base_model.template
│       ├── django.template
│       ├── flask_base_model.template
│       ├── flask.template
│       ├── sqlalchemy_base_model.template
│       └── sqlalchemy.template
└── log
    └── gen_data_model.log
```

### COPYRIGHT AND LICENCE

Copyright (C) 2018 by https://vroncevic.github.io/gen_data_model/

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.7/3.4 or,
at your option, any later version of Python 3 you may have available.

:sparkles:

