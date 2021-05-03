# -*- coding: UTF-8 -*-

'''
 Module
     write_template.py
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
     Defined class WriteTemplate with attribute(s) and method(s).
     Created API for write a template content with parameters to a file.
'''

import sys
from datetime import date
from os import getcwd, chmod
from string import Template

try:
    from gen_data_model.pro.model_selector import ModelSelector
    from ats_utilities.checker import ATSChecker
    from ats_utilities.cooperative import CooperativeMeta
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/gen_data_model'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_data_model/blob/dev/LICENSE'
__version__ = '1.6.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplate(FileChecking):
    '''
        Defined class WriteTemplate with attribute(s) and method(s).
        Created API for write a template content with parameters to a file.
        It defines:

            :attributes:
                | __metaclass__ - setting cooperative metaclasses.
                | GEN_VERBOSE - console text indicator for process-phase.
                | __check_status - check status.
            :methods:
                | __init__ - initial constructor.
                | get_check_status - get check status.
                | write - write a template content with parameters to a file.
                | __str__ - dunder method for WriteTemplate.
    '''

    __metaclass__ = CooperativeMeta
    GEN_VERBOSE = 'GEN_DATA_MODEL::PRO::WRITE_TEMPLATE'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :excptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(WriteTemplate.GEN_VERBOSE, verbose, 'init writer')
        self.__check_status = False

    def get_check_status(self):
        '''
            Get check status.

            :return: getting check status.
            :rtype: <bool>
            :excptions: None
        '''
        return self.__check_status

    def write(self, model_content, model_name, verbose=False):
        '''
            Write a template content with parameters to a file.

            :param model_content: template content for model.
            :type model_content: <str>
            :param model_name: parameter model name.
            :type model_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status True (success) | False.
            :rtype: <bool>
            :excptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:model_content', model_content),
            ('str:model_name', model_name)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        status, file_name = False, None
        verbose_message(WriteTemplate.GEN_VERBOSE, verbose, 'writer template')
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
                WriteTemplate.GEN_VERBOSE, verbose, 'write model', module_file
            )
            if template:
                with open(module_file, 'w') as model_file:
                    model_file.write(template.substitute(model_params))
                    chmod(module_file, 0o666)
                    self.check_path(module_file, verbose=verbose)
                    self.check_mode('w', verbose=verbose)
                    self.check_format(module_file, 'py', verbose=verbose)
                    if self.is_file_ok():
                        status = True
        return status

    def __str__(self):
        '''
            Dunder method for WriteTemplate.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            str(self.__check_status)
        )
