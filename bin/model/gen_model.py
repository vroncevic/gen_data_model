# -*- coding: UTF-8 -*-
# gen_model.py
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
from inspect import stack

try:
    from model.read_template import ReadTemplate
    from model.write_template import WriteTemplate
    from model.model_selector import ModelSelector
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.success import success_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
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


class GenModel(ReadTemplate, WriteTemplate):
    """
        Define class GenModel with attribute(s) and method(s).
        Generate data model by template and parameters.
        It defines:
            attribute:
                VERBOSE - Console text indicator for current process-phase
            method:
                __init__ - Initial constructor
                gen_model - Generate module file with data model
    """

    VERBOSE = 'MODEL::GEN_MODEL'

    def __init__(self, verbose=False):
        """
            Initial constructor
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        cls = GenModel
        verbose_message(cls.VERBOSE, verbose, 'Initial data model')
        ReadTemplate.__init__(self, verbose=verbose)
        WriteTemplate.__init__(self, verbose=verbose)

    def gen_model(self, model_name, verbose=False):
        """
            Generate setup.py for python package.
            :param model_name: Parameter model name
            :type model_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        cls, func, status = GenModel, stack()[0][3], False
        model_txt = 'Argument: expected model_name <str> object'
        model_msg = "{0} {1} {2}".format('def', func, model_txt)
        if model_name is None or not model_name:
            raise ATSBadCallError(model_msg)
        if not isinstance(model_name, str):
            raise ATSTypeError(model_msg)
        verbose_message(
            cls.VERBOSE, verbose, 'Generating data model', model_name
        )
        model_type = ModelSelector.choose_model()
        if model_type == ModelSelector.Cancel:
            status = True
        else:
            model_content, model_base_content = self.read(
                model_type, verbose=verbose
            )
            if model_content and model_base_content:
                status_model = self.write(model_content, model_name)
                status_base_model = self.write(model_base_content, 'base')
                if status_model and status_base_model:
                    status = True
        return True if status else False
