# -*- coding: UTF-8 -*-

'''
 Module
     write_template.py
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
     Define class WriteTemplate with attribute(s) and method(s).
     Write a template content with parameters to a file.
'''

import sys
from datetime import date
from os import getcwd, chmod
from string import Template

try:
    from gen_data_model.pro.model_selector import ModelSelector
    from ats_utilities.console_io.verbose import verbose_message
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


class WriteTemplate(object):
    '''
        Define class WriteTemplate with attribute(s) and method(s).
        Write a template content with parameters to a file.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __check_status - Check status.
            :methods:
                | __init__ - Initial constructor.
                | get_check_status - Get check status.
                | write - Write a template content with parameters to a file.
    '''

    __slots__ = ('VERBOSE', '__check_status')
    VERBOSE = 'GEN_DATA_MODEL::PRO::WRITE_TEMPLATE'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :excptions: None
        '''
        verbose_message(WriteTemplate.VERBOSE, verbose, 'init writer')
        self.__check_status = False

    def get_check_status(self):
        '''
            Get check status.

            :return: Getting check status.
            :rtype: <bool>
            :excptions: None
        '''
        return self.__check_status

    def write(self, model_content, model_name, verbose=False):
        '''
            Write a template content with parameters to a file.

            :param model_content: Template content for model.
            :type model_content: <str>
            :param model_name: Parameter model name.
            :type model_name: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: Boolean status True (success) | False.
            :rtype: <bool>
            :excptions: ATSBadCallError | ATSTypeError
        '''
        status, file_name = False, None
        verbose_message(WriteTemplate.VERBOSE, verbose, 'writer template')
        file_name = ModelSelector.format_name(model_name)
        if file_name:
            self.__check_status, current_dir = True, getcwd()
            module_file = '{0}/{1}'.format(current_dir, file_name)
            model_params = {
                'mod': '{0}'.format(model_name),
                'modlc': '{0}'.format(model_name.lower()),
                'date': '{0}'.format(date.today()),
                'year': '{0}'.format(date.today().year)
            }
            template = Template(model_content)
            verbose_message(
                WriteTemplate.VERBOSE, verbose, 'write model', module_file
            )
            if template:
                with open(module_file, 'w') as model_file:
                    model_file.write(template.substitute(model_params))
                    chmod(module_file, 0o666)
                    status = True
        return True if status else False
