# -*- coding: UTF-8 -*-

'''
 Module
     read_template.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
     gen_data_model is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     gen_data_model is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define class ReadTemplate with attribute(s) and method(s).
     Read a model template files and return a contents.
'''

import sys
from os.path import exists

try:
    from pathlib import Path
    from gen_data_model.pro.model_selector import ModelSelector
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################


__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.2.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ReadTemplate(FileChecking):
    '''
        Define class ReadTemplate with attribute(s) and method(s).
        Read a model template files and return a contents.
        It defines:

            attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __MODEL_TYPES - Model types and descriptions.
                | __TEMPLATE_DIR - Prefix path to templates.
                | template_dir - Absolute path of template dir.
            methods:
                | __init__ - Initial constructor.
                | get_config - Get model types, templates, configurations.
                | read - Read templates and return a string representations.
    '''

    __slots__ = ('VERBOSE', '__MODEL_TYPES', '__TEMPLATE_DIR', 'template_dir')
    VERBOSE = 'GEN_DATA_MODEL::PRO::READ_TEMPLATE'
    __MODEL_TYPES = '../conf/data_model_types.yaml'
    __TEMPLATE_DIR = '/../conf/template/'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :excptions: None
        '''
        verbose_message(ReadTemplate.VERBOSE, verbose, 'init reader')
        FileChecking.__init__(self, verbose=verbose)
        models = '{0}/{1}'.format(
            Path(__file__).parent, ReadTemplate.__MODEL_TYPES
        )
        self.check_path(file_path=models, verbose=verbose)
        self.check_mode(file_mode='r', verbose=verbose)
        self.check_format(
            file_path=models, file_format='yaml', verbose=verbose
        )
        if self.is_file_ok():
            yml2obj = Yaml2Object(models)
            self.__config = yml2obj.read_configuration()
        else:
            self.__config = None
        if bool(self.__config):
            self.template_dir = '{0}{1}'.format(
                Path(__file__).parent, ReadTemplate.__TEMPLATE_DIR
            )

    def get_config(self):
        '''
            Get model types, templates, configurations.

            :return: Dictionary with configurations.
            :rtype: <dict>
            :excptions: None
        '''
        return self.__config

    def read(self, verbose=False):
        '''
            Read templates and return a string representations.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: Template contents (base data model and data model) | None
            :rtype: <str> <str> | <NoneType> <NoneType>
            :excptions: None
        '''
        model_base_content, model_content = None, None
        model_type = ModelSelector.choose_model(self.__config, verbose=verbose)
        model = self.__config['model_types'][int(model_type) - 1]
        model_index = model.keys()[0]
        if model_index != 'Cancel':
            template_base = '{0}{1}'.format(
                self.template_dir, model[model_index]['base_template']
            )
            template = '{0}{1}'.format(
                self.template_dir, model[model_index]['model_template']
            )
            if all([exists(template_base), exists(template)]):
                verbose_message(
                    ReadTemplate.VERBOSE, verbose, 'loading base model'
                )
                with open(template_base, 'r') as model_base_file:
                    model_base_content = model_base_file.read()
                verbose_message(
                    ReadTemplate.VERBOSE, verbose, 'loading model'
                )
                with open(template, 'r') as model_file:
                    model_content = model_file.read()
        else:
            model_base_content, model_content = 'Cancel', 'Cancel'
        return model_base_content, model_content
