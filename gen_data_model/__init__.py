# -*- coding: utf-8 -*-

'''
Module
    gen_data_model.py
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
    Defines class GenDataModel with attribute(s) and method(s).
    Loads a base info, creates a CLI interface and runs operations.
'''

import sys
from typing import Any, List, Dict
from os.path import exists, dirname, realpath
from os import getcwd
from argparse import Namespace

try:
    from ats_utilities.splash import Splash
    from ats_utilities.logging import ATSLogger
    from ats_utilities.cli.cfg_cli import CfgCLI
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.success import success_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from gen_data_model.pro import GenModel
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


class GenDataModel(CfgCLI):
    '''
        Defines class GenDataModel with attribute(s) and method(s).
        Loads a base info, creates a CLI interface and runs operations.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
                | _CONFIG - Configuration file path.
                | _LOG - Tool log file path.
                | _LOGO - Logo for splash screen.
                | _OPS - List of tool options.
                | _logger - Logger object API.
            :methods:
                | __init__ - Initials GenDataModel constructor.
                | process - Processes and runs tool options.
    '''

    _GEN_VERBOSE: str = 'GEN_DATA_MODEL'
    _CONFIG: str = '/conf/gen_data_model.cfg'
    _LOG: str = '/log/gen_data_model.log'
    _LOGO: str = '/conf/gen_data_model.logo'
    _OPS: List[str] = ['-n', '--name', '-t', '--type', '-v', '--verbose']

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials GenDataModel constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        current_dir: str = dirname(realpath(__file__))
        gen_data_model_property: Dict[str, str | bool] = {
            'ats_organization': 'vroncevic',
            'ats_repository': f'{self._GEN_VERBOSE.lower()}',
            'ats_name': f'{self._GEN_VERBOSE.lower()}',
            'ats_logo_path': f'{current_dir}{self._LOGO}',
            'ats_use_github_infrastructure': True
        }
        Splash(gen_data_model_property, verbose)
        base_info: str = f'{current_dir}{self._CONFIG}'
        super().__init__(base_info, verbose)
        verbose_message(
            verbose, [f'{self._GEN_VERBOSE.lower()} init configuration']
        )
        self._logger: ATSLogger = ATSLogger(
            self._GEN_VERBOSE.lower(), f'{current_dir}{self._LOG}', verbose
        )
        if self.tool_operational:
            self.add_new_option(
                self._OPS[0], self._OPS[1], dest='name',
                help='generate model (provide project name)'
            )
            self.add_new_option(
                self._OPS[2], self._OPS[3], dest='type',
                help='model type (django | flask | sqlalchemy)'
            )
            self.add_new_option(
                self._OPS[4], self._OPS[5],
                action='store_true', default=False,
                help='activate verbose mode for generation'
            )

    def process(self, verbose: bool = False) -> bool:
        '''
            Process and run operation.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (success operation) | False
            :rtype: <bool>
            :exceptions: None
        '''
        status: bool = False
        if self.tool_operational:
            try:
                args: Any | Namespace = self.parse_args(sys.argv)
                if not bool(getattr(args, "name")):
                    error_message(
                        [f'{self._GEN_VERBOSE.lower()} missing name argument']
                    )
                    return status
                if not bool(getattr(args, "type")):
                    error_message(
                        [f'{self._GEN_VERBOSE.lower()} missing type argument']
                    )
                    return status
                if exists(f'{getcwd()}/{str(getattr(args, "name"))}'):
                    error_message([
                        f'{self._GEN_VERBOSE.lower()}',
                        f'project with name [{getattr(args, "name")}] exists'
                    ])
                    return status
                gen: GenModel = GenModel(getattr(args, 'verbose') or verbose)
                try:
                    print(
                        " ".join([
                            f'[{self._GEN_VERBOSE.lower()}]',
                            'generate model skeleton',
                            str(getattr(args, "name"))
                        ])
                    )
                    status = gen.gen_model(
                        f'{getattr(args, "name")}',
                        f'{getattr(args, "type")}',
                        getattr(args, 'verbose') or verbose
                    )
                except (ATSTypeError, ATSValueError) as e:
                    error_message([f'{self._GEN_VERBOSE.lower()} {str(e)}'])
                    self._logger.write_log(f'{str(e)}', self._logger.ATS_ERROR)
                if status:
                    success_message([f'{self._GEN_VERBOSE.lower()} done\n'])
                    self._logger.write_log(
                        f'generate {getattr(args, "name")} done',
                        self._logger.ATS_INFO
                    )
                else:
                    error_message([f'{self._GEN_VERBOSE.lower()} failed'])
                    self._logger.write_log(
                        'generation failed', self._logger.ATS_ERROR
                    )
            except SystemExit:
                error_message(
                    [f'{self._GEN_VERBOSE.lower()} expected argument -n']
                )
                return status
        else:
            error_message(
                [f'{self._GEN_VERBOSE.lower()} tool is not operational']
            )
            self._logger.write_log(
                'tool is not operational', self._logger.ATS_ERROR
            )
        return status
