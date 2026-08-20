Generate Data Model (Django/Flask/SQLAlchemy)
-----------------------------------------------

**gen_data_model** is tool generator of form model for

* Django FWK
* Flask FWK
* SQLAlchemy

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|gen_data_model python checker| |gen_data_model python package| |gen_data_model interface checker| |gen_data_model isp checker| |gen_data_model srp checker| |github issues| |documentation status| |github contributors|

.. |gen_data_model python checker| image:: https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_python_checker.yml

.. |gen_data_model python package| image:: https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_package.yml

.. |gen_data_model interface checker| image:: https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_interface_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_interface_checker.yml

.. |gen_data_model isp checker| image:: https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_isp_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_isp_checker.yml

.. |gen_data_model srp checker| image:: https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_srp_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_data_model/actions/workflows/gen_data_model_srp_checker.yml

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

🚀 Installation
------------------

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


📦 Dependencies
------------------

**gen_data_model** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

📁 Tool structure
--------------------

**gen_data_model** is based on OOP

Generator structure

.. code-block:: bash

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

✨ Features
--------------

* Automatically generates data models skeletons (Django, Flask, SQLAlchemy).
* Provides a modular and extensible architecture based on OOP and SOLID principles.
* Includes command line interface (CLI) support via a command/executor structure.
* Robust validation of project bundles, dependencies, and options.
* Comes with configurable templates and JSON schema definitions.
* High code quality with full type checking and 100% unit test coverage.

📊 Code coverage
-------------------

.. csv-table:: Code coverage
   :file: coverage_table.csv
   :widths: 60, 10, 10, 20
   :header-rows: 1

🛠 Usage
-----------

Install package

.. code-block:: bash

    pip3 install gen_data_model

Prepare main entry point by downloading `main.py` or create your own.

.. code-block:: bash

    wget -O main.py https://raw.githubusercontent.com/vroncevic/gen_data_model/main/main.py

Running tool for creating new data model skeleton files

.. code-block:: bash

    python3 main.py create --name mytool --type django --output ./demo/

📚 Docs
----------

More documentation and info at

* `gen-data-model.readthedocs.io <https://gen-data-model.readthedocs.io>`_
* `www.python.org <https://www.python.org/>`_

👥 Contributing
-----------------

`Contributing to gen_data_model <https://github.com/vroncevic/gen_data_model/blob/dev/CONTRIBUTING.md>`_

📄 Copyright and licence
-------------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2017 - 2026 by `vroncevic.github.io/gen_data_model <https://vroncevic.github.io/gen_data_model>`_

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
