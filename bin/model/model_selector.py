# -*- coding: UTF-8 -*-
# model_selector.py
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
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.error import error_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ##################################

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2018, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"


class ModelSelector(object):
    """
        Define class ModelSelector with attribute(s) and method(s).
        Selecting data model type for generating process.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                Django - 0 Django type model
                Flask - 1 Flask type model
                SQLAlchemy - 2 SQLAlchemy type model
                Cancel - 3 Cancel option
                __MODELS - Dictionary with option/description
            method:
                choose_model - Selecting type of model for generating process
                format_name - Formatting name for file module
    """

    __slots__ = (
        'VERBOSE',
        'Django',
        'Flask',
        'SQLAlchemy',
        'Cancel',
        '__MODELS'
    )
    VERBOSE = 'MODEL::MODEL_SELECTOR'
    Django, Flask, SQLAlchemy, Cancel = range(4)
    __MODELS = {
        Django: "Django model",
        Flask: "Flask model",
        SQLAlchemy: "SQLAlchemy model",
        Cancel: "Cancel"
    }

    @classmethod
    def choose_model(cls, verbose=False):
        """
            Choose type of data model.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Type of data model (0, 1, 2)
            :rtype: <int>
            :exceptions: None
        """
        verbose_message(cls.VERBOSE, verbose, 'Loading options')
        print("\n {0}".format('model option list:'))
        for key in sorted(cls.__MODELS):
            print("  {0} {1}".format(key, cls.__MODELS[key]))
        while True:
            model_type = input(' Select model: ')
            if model_type not in cls.__MODELS.keys():
                error_message(cls.VERBOSE, 'Not an appropriate choice.')
            else:
                break
        verbose_message(cls.VERBOSE, verbose, 'Selected option', model_type)
        return model_type

    @classmethod
    def format_name(cls, model_name):
        """
            Format file name (Format: model_<name>.py).
            :param model_name: Postfix name for data model file
            :type: <str>
            :return: File name with extension (lower case) | None
            :rtype: <str> | <NoneType>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func, model_name_final = stack()[0][3], None
        model_name_txt = 'Argument: expected model_name <str> object'
        model_name_msg = "{0} {1} {2}".format('def', func, model_name_txt)
        if model_name is None or not model_name:
            raise ATSBadCallError(model_name_msg)
        if not isinstance(model_name, str):
            raise ATSTypeError(model_name_msg)
        if model_name:
            model_name_final = "model_{0}{1}".format(model_name.lower(), '.py')
        return model_name_final

