# -*- coding: UTF-8 -*-
# gen_data_model.py
# Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# gen_data_model is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gen_data_model is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys
from os import getcwd

try:
    from pathlib import Path

    from ats_utilities.cfg_base import CfgBase
    from model.gen_model import GenModel
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.success import success_message
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ###################################

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"


class GenDataModel(CfgBase, GenModel):
    """
        Define class GenDataModel with attribute(s) and method(s).
        Load a settings, create an interface and run operation(s).
        It defines:
            attribute:
                VERBOSE - Console text indicator for current process-phase
                __CONFIG - Configuration file path
                __OPS - Tool options (list)
            method:
                __init__ - Initial constructor
                process - Process and run tool option
    """

    VERBOSE = 'GEN_DATA_MODEL'
    __CONFIG = "/../conf/gen_data_model.cfg"
    __OPS = ["-g", "--gen", "-h", "--version"]

    def __init__(self, verbose=False):
        """
            Loading configuration and setting argument options.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        cls = GenDataModel
        verbose_message(cls.VERBOSE, verbose, 'Initial configuration')
        module_dir = Path(__file__).resolve().parent
        base_config_file = "{0}{1}".format(module_dir, cls.__CONFIG)
        CfgBase.__init__(self, base_config_file, verbose=verbose)
        tool_status = self.get_tool_status(verbose=verbose)
        if tool_status:
            self.add_new_option(
                cls.__OPS[0], cls.__OPS[1], dest="mod",
                help="generate data model"
            )
            GenModel.__init__(self, verbose=verbose)

    def process(self, verbose=False):
        """
            Process and run operation.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
        """
        cls, status = GenDataModel, False
        tool_status = self.get_tool_status(verbose=verbose)
        if tool_status:
            self.show_base_info(verbose=verbose)
            if len(sys.argv) > 1:
                op = sys.argv[1]
                if op not in cls.__OPS:
                    sys.argv = []
                    sys.argv.append("-h")
            else:
                sys.argv.append("-h")
            opts, args = self.parse_args(sys.argv)
            model = "model_{0}{1}".format(opts.mod, ".py")
            current_dir, num_of_args = getcwd(), len(args)
            model_path = "{0}/{1}".format(current_dir, model)
            model_exists = Path(model_path).exists()
            if num_of_args == 1 and opts.mod and not model_exists:
                message = "{0} {1} [{2}]".format(
                    "[{0}]".format(self.get_ats_name(verbose=verbose)),
                    'Generating data model',
                    opts.mod
                )
                print(message)
                gen_model_process = self.gen_model("{0}".format(opts.mod))
                if gen_model_process:
                    success_message(
                        self.get_ats_name(verbose=verbose), 'Done\n'
                    )
                    status = True
                else:
                    error_message(
                        self.get_ats_name(verbose=verbose),
                        'Failed to process and run option'
                    )
            else:
                error_message(
                    self.get_ats_name(verbose=verbose),
                    'model already exist in current directory'
                )
        else:
            error_message('[gen_data_model]', 'Tool is not operational')
        return True if status else False
