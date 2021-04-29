# -*- coding: utf-8 -*-

'''
 Module
     gen_data_model.py
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
     Defined class GenDataModel with attribute(s) and method(s).
     Load a base info, create an CLI interface and run operation(s).
'''

import sys
from os.path import exists

try:
    from pathlib import Path
    from gen_data_model.pro import GenModel
    from ats_utilities.logging import ATSLogger
    from ats_utilities.cli.cfg_cli import CfgCLI
    from ats_utilities.cooperative import CooperativeMeta
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.success import success_message
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/gen_data_model'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_data_model/blob/master/LICENSE'
__version__ = '1.5.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenDataModel(CfgCLI):
    '''
        Defined class GenDataModel with attribute(s) and method(s).
        Load a base info, create an CLI interface and run operation(s).
        It defines:

            :attributes:
                | __metaclass__ - setting cooperative metaclasses.
                | GEN_VERBOSE - console text indicator for process-phase.
                | CONFIG - configuration file path.
                | LOG - tool log file path.
                | OPS - tool options (list).
                | logger - logger object API.
            :methods:
                | __init__ - initial constructor.
                | process - process and run tool option(s).
                | __str__ - dunder method for GenDataModel.
    '''

    __metaclass__ = CooperativeMeta
    GEN_VERBOSE = 'GEN_DATA_MODEL'
    CONFIG = '/conf/gen_data_model.cfg'
    LOG = '/log/gen_data_model.log'
    OPS = ['-g', '--gen', '-v', '--verbose', '--version']

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        current_dir = Path(__file__).resolve().parent
        base_info = '{0}{1}'.format(current_dir, GenDataModel.CONFIG)
        CfgCLI.__init__(self, base_info, verbose=verbose)
        verbose_message(
            GenDataModel.GEN_VERBOSE, verbose, 'init configuration'
        )
        self.logger = ATSLogger(
            GenDataModel.GEN_VERBOSE.lower(),
            '{0}{1}'.format(current_dir, GenDataModel.LOG),
            verbose=verbose
        )
        if self.tool_operational:
            self.add_new_option(
                GenDataModel.OPS[0], GenDataModel.OPS[1],
                dest='pro', help='generate data model'
            )
            self.add_new_option(
                GenDataModel.OPS[2], GenDataModel.OPS[3],
                action='store_true', default=False,
                help='activate verbose mode for generation'
            )
            self.add_new_option(
                GenDataModel.OPS[4], action='version', version=__version__
            )

    def process(self, verbose=False):
        '''
            Process and run operation.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: True (success) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        status = False
        if self.tool_operational:
            num_of_args_sys = len(sys.argv)
            if num_of_args_sys > 1:
                operation = sys.argv[1]
                if operation not in GenDataModel.OPS:
                    sys.argv.append('-h')
            else:
                sys.argv.append('-h')
            args = self.parse_args(sys.argv[1:])
            pro_exists = exists(args.pro)
            if not pro_exists:
                if bool(args.pro):
                    print(
                        '{0} {1} [{2}]'.format(
                            '[{0}]'.format(GenDataModel.GEN_VERBOSE.lower()),
                            'generating model', args.pro
                        )
                    )
                    generator = GenModel(
                        args.pro, verbose=args.verbose or verbose
                    )
                    status = generator.gen_model(
                        verbose=args.verbose or verbose
                    )
                    if status:
                        success_message(GenDataModel.GEN_VERBOSE, 'done\n')
                        self.logger.write_log(
                            '{0} {1} done'.format(
                                'generating data model', args.pro
                            ), ATSLogger.ATS_INFO
                        )
                    else:
                        error_message(
                            GenDataModel.GEN_VERBOSE, 'generation failed'
                        )
                        self.logger.write_log(
                            'generation failed', ATSLogger.ATS_ERROR
                        )
                else:
                    error_message(
                        GenDataModel.GEN_VERBOSE, 'provide model name'
                    )
                    self.logger.write_log(
                        'provide model name', ATSLogger.ATS_ERROR
                    )
            else:
                error_message(GenDataModel.GEN_VERBOSE, 'model already exist')
                self.logger.write_log(
                    'model already exist', ATSLogger.ATS_ERROR
                )
        else:
            error_message(GenDataModel.GEN_VERBOSE, 'tool is not operational')
            self.logger.write_log(
                'tool is not operational', ATSLogger.ATS_ERROR
            )
        return status

    def __str__(self):
        '''
            Dunder method for GenDataModel.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, CfgCLI.__str__(self), str(self.logger)
        )
