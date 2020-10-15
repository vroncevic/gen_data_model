Generate Data Model (Django/Flask/SQLAlchemy)
---------------------------------------------

**gen_data_model** is tool generator of form model for:

* Django FWK
* Flask FWK
* SQLAlchemy

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|Python package| |GitHub issues| |Documentation Status| |GitHub contributors|

.. |Python package| image:: https://github.com/vroncevic/gen_data_model/workflows/Python%20package%20gen_data_model/badge.svg
   :target: https://github.com/vroncevic/gen_data_model/workflows/Python%20package%20gen_data_model/badge.svg?branch=master

.. |GitHub issues| image:: https://img.shields.io/github/issues/vroncevic/gen_data_model.svg
   :target: https://github.com/vroncevic/gen_data_model/issues

.. |GitHub contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_data_model.svg
   :target: https://github.com/vroncevic/gen_data_model/graphs/contributors

.. |Documentation Status| image:: https://readthedocs.org/projects/gen_data_model/badge/?version=latest
   :target: https://gen_data_model.readthedocs.io/projects/gen_data_model/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   self
   modules

Installation
-------------

|Install Python2 Package| |Install Python3 Package|

.. |Install Python2 Package| image:: https://github.com/vroncevic/gen_data_model/workflows/Install%20Python2%20Package%20gen_data_model/badge.svg
   :target: https://github.com/vroncevic/gen_data_model/workflows/Install%20Python2%20Package%20gen_data_model/badge.svg?branch=master

.. |Install Python3 Package| image:: https://github.com/vroncevic/gen_data_model/workflows/Install%20Python3%20Package%20gen_data_model/badge.svg
   :target: https://github.com/vroncevic/gen_data_model/workflows/Install%20Python3%20Package%20gen_data_model/badge.svg?branch=master

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_data_model/releases

To install **gen_data_model** type the following:

.. code-block:: bash

    tar xvzf gen_data_model-x.y.z.tar.gz
    cd gen_data_model-x.y.z/
    pip install -r requirements.txt
    python setup.py install_lib
    python setup.py install_egg_info
    python setup.py install_data

You can use Docker to create image/container.

|GitHub docker checker|

.. |GitHub docker checker| image:: https://github.com/vroncevic/gen_data_model/workflows/gen_data_model%20docker%20checker/badge.svg
   :target: https://github.com/vroncevic/gen_data_model/actions?query=workflow%3A%22gen_data_model+docker+checker%22

Dependencies
-------------

**gen_data_model** requires next modules and libraries:

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_
* `Flask-WTF - Simple integration of Flask and WTForms <https://pypi.org/project/Flask-WTF/>`_
* `Django - High-level Python Web framework <https://pypi.org/project/Django/>`_
* `SQLAlchemy -  SQL Toolkit and Object Relational Mapper <https://pypi.org/project/SQLAlchemy/>`_

Generation process
-------------------

Generation flow:

.. image:: https://raw.githubusercontent.com/vroncevic/gen_data_model/dev/docs/gen_data_model_flow.png

Library structure
------------------

**gen_data_model** is based on OOP:

.. image:: https://raw.githubusercontent.com/vroncevic/gen_data_model/dev/docs/gen_data_model.png

Code structure:

.. code-block:: bash

    .
    ├── conf/
    │   ├── gen_data_model.cfg
    │   ├── gen_data_model_util.cfg
    │   └── template/
    │       ├── django_base_model.template
    │       ├── django.template
    │       ├── flask_base_model.template
    │       ├── flask.template
    │       ├── SQLAlchemy_base_model.template
    │       └── SQLAlchemy.template
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

Copyright and licence
----------------------

|License: GPL v3| |License: Apache 2.0|

.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |License: Apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2018 by `vroncevic.github.io/gen_data_model <https://vroncevic.github.io/gen_data_model>`_

**gen_data_model** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|Python Software Foundation|

.. |Python Software Foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_data_model/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|Donate|

.. |Donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
