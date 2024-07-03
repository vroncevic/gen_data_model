# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
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
    Defines class GenModel with attribute(s) and method(s).
    Generates data model by templates and parameters.
'''

import sys
from typing import List, Optional
from os.path import dirname, realpath

try:
    from ats_utilities.pro_config import ProConfig
    from ats_utilities.pro_config.pro_name import ProName
    from ats_utilities.config_io.file_check import FileCheck
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from gen_data_model.pro.read_template import ReadTemplate
    from gen_data_model.pro.write_template import WriteTemplate
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


class GenModel(FileCheck, ProConfig, ProName):
    '''
        Defines class GenModel with attribute(s) and method(s).
        Generates data model by templates and parameters.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
                | _PRO_STRUCTURE - Project setup (templates, modules).
                | _reader - Reader API.
                | _writer - Writer API.
            :methods:
                | __init__ - Initials GenModel constructor.
                | get_reader - Gets template reader.
                | get_writer - Gets template writer.
                | gen_model - Generates data model.
    '''

    _GEN_VERBOSE: str = 'GEN_DATA_MODEL::PRO::GEN_MODEL'
    _PRO_STRUCTURE: str = '/../conf/model_types.yaml'

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initial constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        FileCheck.__init__(self, verbose)
        ProConfig.__init__(self, verbose)
        ProName.__init__(self, verbose)
        verbose_message(
            verbose, [f'{self._GEN_VERBOSE.lower()} init generator']
        )
        self._reader: Optional[ReadTemplate] = ReadTemplate(verbose)
        self._writer: Optional[WriteTemplate] = WriteTemplate(verbose)
        current_dir: str = dirname(realpath(__file__))
        pro_structure: str = f'{current_dir}{self._PRO_STRUCTURE}'
        self.check_path(pro_structure, verbose)
        self.check_mode('r', verbose)
        self.check_format(pro_structure, 'yaml', verbose)
        if self.is_file_ok():
            yml2obj: Optional[Yaml2Object] = Yaml2Object(pro_structure)
            self.config = yml2obj.read_configuration()

    def get_reader(self) -> Optional[ReadTemplate]:
        '''
            Gets template reader.

            :return: Template reader object | None
            :rtype: <Optional[ReadTemplate]>
            :exceptions: None
        '''
        return self._reader

    def get_writer(self) -> Optional[WriteTemplate]:
        '''
            Gets template writer.

            :return: Template writer object | none
            :rtype: <Optional[WriteTemplate]>
            :exceptions: None
        '''
        return self._writer

    def gen_model(
        self,
        model_name: Optional[str],
        model_type: Optional[str],
        verbose: bool = False
    ) -> bool:
        '''
            Generates data model.

            :param model_name: Model name
            :type model_name: <Optional[str]>
            :param model_type: Model type
            :type model_type: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (success operation) | False
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSValueError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([
            ('str:model_name', model_name), ('str:model_type', model_type)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if not bool(model_name):
            raise ATSValueError('missing model name')
        if not bool(model_type):
            raise ATSValueError('missing model type')
        status: bool = False
        verbose_message(
            verbose, [
                f'{self._GEN_VERBOSE.lower()}',
                'generate', model_type, 'model', model_name
            ]
        )
        base_content: Optional[str] = None
        model_content: Optional[str] = None
        if bool(self._reader) and bool(self._writer):
            base_content, model_content = self._reader.read(
                model_type, verbose
            )
            if bool(base_content) and bool(model_content):
                model_generated: List[bool] = [
                    self._writer.write(base_content, 'base', verbose),
                    self._writer.write(model_content, model_name, verbose)
                ]
                if all([bool(model_generated), all(model_generated)]):
                    status = True
        return status
