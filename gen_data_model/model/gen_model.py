# -*- coding: UTF-8 -*-

"""
 Module
     gen_model.py
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
     Define class GenModel with attribute(s) and method(s).
     Generate data model by template and parameters.
"""

import sys
from inspect import stack

try:
    from gen_data_model.model.read_template import ReadTemplate
    from gen_data_model.model.write_template import WriteTemplate
    from gen_data_model.model.model_selector import ModelSelector
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2018, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"


class GenModel(object):
    """
        Define class GenModel with attribute(s) and method(s).
        Generate data model by template and parameters.
        It defines:

            :attributes:
                | __slots__ - Setting class slots
                | VERBOSE - Console text indicator for current process-phase
                | __reader - Reader API
                | __writer - Writer API
            :methods:
                | __init__ - Initial constructor
                | get_reader - Getter for reader object
                | get_writer - Getter for writer object
                | gen_model - Generate module file with data model
    """

    __slots__ = ('VERBOSE', '__reader', '__writer')
    VERBOSE = 'GEN_DATA_MODEL::MODEL::GEN_MODEL'

    def __init__(self, verbose=False):
        """
            Initial constructor.

            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(GenModel.VERBOSE, verbose, 'Initial data model')
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)

    def get_reader(self):
        """
            Getter for reader object.

            :return: Read Template object
            :rtype: <ReadTemplate>
            :exceptions: None
        """
        return self.__reader

    def get_writer(self):
        """
            Getter for writer object.

            :return: Write Template object
            :rtype: <WriteTemplate>
            :exceptions: None
        """
        return self.__writer

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
        func, status, model_type = stack()[0][3], False, None
        model_content, model_base_content = None, None
        model_txt = 'Argument: expected model_name <str> object'
        model_msg = "{0} {1} {2}".format('def', func, model_txt)
        if model_name is None or not model_name:
            raise ATSBadCallError(model_msg)
        if not isinstance(model_name, str):
            raise ATSTypeError(model_msg)
        verbose_message(
            GenModel.VERBOSE, verbose, 'Generating data model', model_name
        )
        model_type = ModelSelector.choose_model(verbose=verbose)
        if model_type == ModelSelector.Cancel:
            status = True
        else:
            model_content, model_base_content = self.__reader.read(
                model_type, verbose=verbose
            )
            if model_content and model_base_content:
                status_of_generation = [
                    self.__writer.write(
                        model_content, model_name, verbose=verbose
                    ),
                    self.__writer.write(
                        model_base_content, 'base', verbose=verbose
                    )
                ]
                if all(status_of_generation):
                    status = True
        return True if status else False
