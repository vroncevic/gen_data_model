# -*- coding: UTF-8 -*-
# read_template.py
# Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# gen_data_model is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gen_data_model is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys

try:
    from pathlib import Path

    from model.model_selector import ModelSelector
    from ats_utilities.console_io.verbose import verbose_message
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ###################################


__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2018, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"


class ReadTemplate(object):
    """
        Define class ReadTemplate with attribute(s) and method(s).
        Read a model template file and return a content.
        It defines:
            attribute:
                VERBOSE - Console text indicator for current process-phase
                __TEMPLATE_DIR - Prefix path to templates
                __TEMPLATES - Models (python module templates)
                __template - Absolute file path of template
            method:
                __init__ - Initial constructor
                read - Read templates and return a string representations
    """

    VERBOSE = 'MODEL::READ_TEMPLATE'
    __TEMPLATE_DIR = "/../../conf/template"
    __TEMPLATES = {
        ModelSelector.Django: [
            'django.template', 'django_base_model.template'
        ],
        ModelSelector.Flask: [
            'flask.template', 'flask_base_model.template'
        ],
        ModelSelector.SQLAlchemy: [
            'sqlalchemy.template', 'sqlalchemy_base_model.template'
        ]
    }

    def __init__(self, verbose=False):
        """
            Loading configuration and setting argument options.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        cls, module_dir = ReadTemplate, Path(__file__).parent
        self.__template = "{0}{1}".format(module_dir, cls.__TEMPLATE_DIR)
        verbose_message(cls.VERBOSE, verbose, 'Initial template dir path')

    def read(self, model_type, verbose=False):
        """
            Read template content.
            :param model_type: Chosen type of model (Django/Flask/SQLAlchemy)
            :type: <int>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Template contents (base data model and data model)
            :rtype: <str> | <NoneType>
        """
        cls, model_content, model_base_content = ReadTemplate, None, None
        if model_type in cls.__TEMPLATES.keys():
            templates = cls.__TEMPLATES[model_type]
            template = "{0}/{1}".format(self.__template, templates[0])
            verbose_message(cls.VERBOSE, verbose, 'Loading template')
            template_base = "{0}/{1}".format(self.__template, templates[1])
            verbose_message(cls.VERBOSE, verbose, 'Loading template base')
            try:
                with open(template, 'r') as model_file:
                    model_content = model_file.read()
                verbose_message(cls.VERBOSE, verbose, 'Loading template done')
                with open(template_base, 'r') as model_base_file:
                    model_base_content = model_base_file.read()
                verbose_message(
                    cls.VERBOSE, verbose, 'Loading template base done'
                )
            except AttributeError:
                pass
        return model_content, model_base_content
