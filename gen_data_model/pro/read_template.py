# -*- coding: UTF-8 -*-

'''
Module
    read_template.py
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
    Defines class ReadTemplate with attribute(s) and method(s).
    Creates an API for reading a model template.
'''

import sys
from typing import Tuple, List, Optional
from os.path import dirname, realpath, exists

try:
    from ats_utilities.console_io.verbose import verbose_message
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


class ReadTemplate:
    '''
        Defines class ReadTemplate with attribute(s) and method(s).
        Creates an API for reading a model template.

        It defines:

            attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
                | _TEMPLATE_DIR - Prefix path to templates.
            methods:
                | __init__ - Initials ReadTemplate constructor.
                | read - Reads a template.
    '''

    _GEN_VERBOSE: str = 'GEN_DATA_MODEL::PRO::READ_TEMPLATE'
    _TEMPLATE_DIR: str = '/../conf/template/'

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials ReadTemplate constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :excptions: None
        '''
        verbose_message(verbose, [f'{self._GEN_VERBOSE.lower()} init reader'])

    def read(
        self,
        model_type: Optional[str],
        verbose: bool = False
    ) -> Tuple[Optional[str], Optional[str]]:
        '''
            Reads a template.

            :param model_type: Model type | None
            :type model_type: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Models (base data model | None, data model | None)
            :rtype: <str> <Optional[str]> <NoneType>
            :excptions: None
        '''
        model_base_content: Optional[str] = None
        model_content: Optional[str] = None
        current_dir: str = dirname(realpath(__file__))
        pro_structure: str = f'{current_dir}{self._TEMPLATE_DIR}'
        base_model: str = f'{pro_structure}{model_type}_base_model.template'
        model: str = f'{pro_structure}{model_type}.template'
        if all([exists(base_model), exists(model)]):
            with open(base_model, 'r', encoding='utf-8') as base_file:
                model_base_content = base_file.read()
            with open(model, 'r', encoding='utf-8') as model_file:
                model_content = model_file.read()
        verbose_message(
            verbose, [
                f'{self._GEN_VERBOSE.lower()}',
                f'{model_base_content}',
                f'{model}'
            ]
        )
        return model_base_content, model_content
