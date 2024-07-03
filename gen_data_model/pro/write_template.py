# -*- coding: UTF-8 -*-

'''
Module
    write_template.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class WriteTemplate with attribute(s) and method(s).
    Creates an API for write a template content with parameters to a file.
'''

import sys
from typing import List, Dict, Optional
from datetime import date
from os import getcwd, chmod
from string import Template

try:
    from ats_utilities.config_io.file_check import FileCheck
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_data_model'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_data_model/blob/dev/LICENSE'
__version__ = '2.3.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplate(FileCheck):
    '''
        Defines class WriteTemplate with attribute(s) and method(s).
        Creates an API for write a template content with parameters to a file.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
            :methods:
                | __init__ - Initials WriteTemplate constructor.
                | write - write a template content with parameters to a file.
    '''

    _GEN_VERBOSE: str = 'GEN_DATA_MODEL::PRO::WRITE_TEMPLATE'

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials WriteTemplate constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :excptions: None
        '''
        super().__init__(verbose)
        verbose_message(verbose, [f'{self._GEN_VERBOSE.lower()} init writer'])

    def write(
        self,
        model_content: Optional[str],
        model_name: Optional[str],
        verbose: bool = False
    ) -> bool:
        '''
            Write a template content with parameters to a file.

            :param model_content: Content for model | None
            :type model_content: <Optional[str]>
            :param model_name: Model name | None
            :type model_name: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (success operation) | False
            :rtype: <bool>
            :excptions: ATSTypeError | ATSValueError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([
            ('str:model_content', model_content),
            ('str:model_name', model_name)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if not bool(model_content):
            raise ATSValueError('missing model content')
        if not bool(model_name):
            raise ATSValueError('missing model name')
        status = False
        verbose_message(
            verbose, [f'{self._GEN_VERBOSE.lower()} writer template']
        )
        module_file: str
        if model_name == 'base':
            module_file = f'{getcwd()}/model_{model_name}.py'
        else:
            module_file = f'{getcwd()}/{model_name}.py'
        model_params: Dict[str, str] = {
            'PRO': f'{model_name}',
            'MOD': f'{model_name}',
            'MODLC': f'{model_name.capitalize()}',
            'YEAR': f'{date.today().year}'
        }
        template: Template = Template(model_content)
        if bool(template) and bool(model_params):
            with open(module_file, 'w', encoding='utf-8') as model_file:
                verbose_message(
                    verbose, [
                        f'{self._GEN_VERBOSE} write model', module_file
                    ]
                )
                model_file.write(template.substitute(model_params))
                chmod(module_file, 0o666)
                self.check_path(module_file, verbose)
                self.check_mode('w', verbose)
                self.check_format(module_file, 'py', verbose)
                if self.is_file_ok():
                    status = True
        return status
