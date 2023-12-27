Generate Data Model (Django/Flask/SQLAlchemy)
---------------------------------------------

**gen_data_model** is tool generator of form model for

* Django FWK
* Flask FWK
* SQLAlchemy

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|gen_data_model python checker| |gen_data_model python package| |github issues| |documentation status| |github contributors|

.. |gen_data_model python checker| image:: https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_python_checker.yml

.. |gen_data_model python package| image:: https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_data_model.svg
   :target: https://github.com/vroncevic/gen_data_model/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_data_model.svg
   :target: https://github.com/vroncevic/gen_data_model/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen-data-model/badge/?version=latest
   :target: https://gen-data-model.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

|gen_data_model python3 build|

.. |gen_data_model python3 build| image:: https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_data_model/releases

To install **gen_data_model** type the following

.. code-block:: bash

    tar xvzf gen_data_model-x.y.z.tar.gz
    cd gen_data_model-x.y.z
    #python3
    pip3 install -r requirements.txt
    python3 setup.py install_lib
    python3 setup.py install_egg_info
    python3 setup.py install_data

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    #python3
    pip3 install gen_data_model


Dependencies
-------------

**gen_data_model** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
---------------

**gen_data_model** is based on OOP

Generator structure

.. code-block:: bash

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
        └── run/
            └── gen_data_model_run.py
        
        6 directories, 16 files

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2017 - 2024 by `vroncevic.github.io/gen_data_model <https://vroncevic.github.io/gen_data_model>`_

**gen_data_model** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_data_model/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
