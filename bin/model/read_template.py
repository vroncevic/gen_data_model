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
from inspect import stack
from os.path import isdir

try:
    from pathlib import Path

    from model.model_selector import ModelSelector
    from ats_utilities.config.file_checking import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ##################################


__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2018, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"


class ReadTemplate(FileChecking):
    """
        Define class ReadTemplate with attribute(s) and method(s).
        Read a model template file and return a content.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __TEMPLATE_DIR - Prefix path to templates
                __TEMPLATES - Models (python module templates)
                __template_dir - Absolute file path of template dir
            method:
                __init__ - Initial constructor
                read - Read templates and return a string representations
    """

    __slots__ = (
        'VERBOSE',
        '__TEMPLATE_DIR',
        '__TEMPLATES',
        '__template_dir'
    )
    VERBOSE = 'GEN_DATA_MODEL::MODEL::READ_TEMPLATE'
    __TEMPLATE_DIR = '/../../conf/template'
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
            :excptions: None
        """
        verbose_message(
            ReadTemplate.VERBOSE, verbose, 'Initial reader'
        )
        FileChecking.__init__(self, verbose=verbose)
        current_dir = Path(__file__).parent
        template_dir = "{0}{1}".format(
            current_dir, ReadTemplate.__TEMPLATE_DIR
        )
        check_template_dir = isdir(template_dir)
        if check_template_dir:
            self.__template_dir = template_dir
        else:
            self.__template_dir = None

    def read(self, model_type, verbose=False):
        """
            Read template content.
            :param model_type: Chosen type of model (Django/Flask/SQLAlchemy)
            :type: <int>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Template contents (base data model and data model) | None
            :rtype: <str> | <NoneType>
            :excptions: ATSBadCallError | ATSTypeError
        """
        func, model_content, model_base_content = stack()[0][3], None, None
        model_type_txt = 'Argument: expected model_content <str> object'
        model_type_msg = "{0} {1} {2}".format('def', func, model_type_txt)
        if model_type is None:
            raise ATSBadCallError(model_type_msg)
        if not isinstance(model_type, int):
            raise ATSTypeError(model_type_msg)
        if model_type in ReadTemplate.__TEMPLATES.keys():
            templates = ReadTemplate.__TEMPLATES[model_type]
            template = "{0}/{1}".format(self.__template_dir, templates[0])
            verbose_message(ReadTemplate.VERBOSE, verbose, 'Loading template')
            template_base = "{0}/{1}".format(self.__template_dir, templates[1])
            verbose_message(
                ReadTemplate.VERBOSE, verbose, 'Loading template base'
            )
            if template and template_base:
                with open(template, 'r') as model_file:
                    model_content = model_file.read()
                verbose_message(
                    ReadTemplate.VERBOSE, verbose, 'Loading template done'
                )
                with open(template_base, 'r') as model_base_file:
                    model_base_content = model_base_file.read()
                verbose_message(
                    ReadTemplate.VERBOSE, verbose, 'Loading template base done'
                )
        return model_content, model_base_content

