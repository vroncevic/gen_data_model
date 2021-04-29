# -*- coding: UTF-8 -*-

'''
 Module
     read_template.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class ReadTemplate with attribute(s) and method(s).
     Created API for read a model template files and return a contents.
'''

import sys
from os.path import exists

try:
    from pathlib import Path
    from ats_utilities.cooperative import CooperativeMeta
    from gen_data_model.pro.model_selector import ModelSelector
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/gen_data_model'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_data_model/blob/master/LICENSE'
__version__ = '1.4.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ReadTemplate(FileChecking):
    '''
        Defined class ReadTemplate with attribute(s) and method(s).
        Created API for read a model template files and return a contents.
        It defines:

            attributes:
                | __metaclass__ - setting cooperative metaclasses.
                | GEN_VERBOSE - console text indicator for process-phase.
                | MODEL_TYPES - model types and descriptions.
                | TEMPLATE_DIR - prefix path to templates.
                | __config - cotainer object for configuration.
                | template_dir - absolute path of template dir.
            methods:
                | __init__ - initial constructor.
                | get_config - get model types, templates, configurations.
                | read - read templates and return a string representations.
                | __str__ - dunder method for ReadTemplate.
    '''

    __metaclass__ = CooperativeMeta
    GEN_VERBOSE = 'GEN_DATA_MODEL::PRO::READ_TEMPLATE'
    MODEL_TYPES = '../conf/data_model_types.yaml'
    TEMPLATE_DIR = '/../conf/template/'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :excptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(ReadTemplate.GEN_VERBOSE, verbose, 'init reader')
        models = '{0}/{1}'.format(
            Path(__file__).parent, ReadTemplate.MODEL_TYPES
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
                Path(__file__).parent, ReadTemplate.TEMPLATE_DIR
            )

    def get_config(self):
        '''
            Get model types, templates, configurations.

            :return: dictionary with configurations.
            :rtype: <dict>
            :excptions: None
        '''
        return self.__config

    def read(self, verbose=False):
        '''
            Read templates and return a string representations.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: template contents (base data model and data model) | None.
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
                    ReadTemplate.GEN_VERBOSE, verbose, 'loading base model'
                )
                with open(template_base, 'r') as model_base_file:
                    model_base_content = model_base_file.read()
                verbose_message(
                    ReadTemplate.GEN_VERBOSE, verbose, 'loading model'
                )
                with open(template, 'r') as model_file:
                    model_content = model_file.read()
        else:
            model_base_content, model_content = 'Cancel', 'Cancel'
        return model_base_content, model_content

    def __str__(self):
        '''
            Dunder method for ReadTemplate.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            str(self.__config), str(self.template_dir)
        )
