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
    from ats_utilities.cli.cfg_cli import CfgCLI
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
__version__ = '1.3.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenDataModel(CfgCLI):
    '''
        Defined class GenDataModel with attribute(s) and method(s).
        Load a base info, create an CLI interface and run operation(s).
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __CONFIG - Configuration file path.
                | __OPS - Tool options (list).
            :methods:
                | __init__ - Initial constructor.
                | process - Process and run tool option(s).
                | __str__ - Dunder method for GenDataModel.
    '''

    __slots__ = ('VERBOSE', '__CONFIG', '__OPS')
    VERBOSE = 'GEN_DATA_MODEL'
    __CONFIG = '/conf/gen_data_model.cfg'
    __OPS = ['-g', '--gen', '-v']

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        verbose_message(GenDataModel.VERBOSE, verbose, 'init configuration')
        current_dir = Path(__file__).resolve().parent
        base_info = '{0}{1}'.format(current_dir, GenDataModel.__CONFIG)
        CfgCLI.__init__(self, base_info, verbose=verbose)
        if self.tool_operational:
            self.add_new_option(
                GenDataModel.__OPS[0], GenDataModel.__OPS[1],
                dest='pro', help='generate data model'
            )
            self.add_new_option(
                GenDataModel.__OPS[2], action='store_true', default=False,
                help='activate verbose mode for generation'
            )

    def process(self, verbose=False):
        '''
            Process and run operation.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: True (success) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        status = False
        if self.tool_operational:
            num_of_args_sys = len(sys.argv)
            if num_of_args_sys > 1:
                option = sys.argv[1]
                if option not in GenDataModel.__OPS:
                    sys.argv = []
                    sys.argv.append('-h')
            else:
                sys.argv.append('-h')
            opts, args = self.parse_args(sys.argv)
            num_of_args, pro_exists = len(args), exists(opts.pro)
            if not pro_exists:
                if num_of_args >= 1 and bool(opts.pro):
                    print(
                        '{0} {1} [{2}]'.format(
                            '[{0}]'.format(GenDataModel.VERBOSE.lower()),
                            'generating model', opts.pro
                        )
                    )
                    generator = GenModel(opts.pro, verbose=opts.v or verbose)
                    status = generator.gen_model(verbose=opts.v or verbose)
                    if status:
                        success_message(GenDataModel.VERBOSE, 'done\n')
                    else:
                        error_message(
                            GenDataModel.VERBOSE, 'failed to generate model'
                        )
                else:
                    error_message(
                        GenDataModel.VERBOSE, 'provide model name'
                    )
            else:
                error_message(GenDataModel.VERBOSE, 'model already exist')
        else:
            error_message(GenDataModel.VERBOSE, 'tool is not operational')
        return True if status else False

    def __str__(self):
        '''
            Dunder method for GenDataModel.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(
            self.__class__.__name__, CfgCLI.__str__(self)
        )
