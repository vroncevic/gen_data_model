# -*- coding: UTF-8 -*-

'''
 Module
     model_selector.py
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
     Defined class ModelSelector with attribute(s) and method(s).
     Selecting data model type for generating process.
'''

import sys

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/gen_data_model'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_data_model/blob/dev/LICENSE'
__version__ = '2.2.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ModelSelector:
    '''
        Defined class ModelSelector with attribute(s) and method(s).
        Selecting data model type for generating process.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
            :methods:
                | choose_model - selecting type of model for generation.
                | format_name - formatting name for file module.
                | __str__ - dunder method for ModelSelector.
    '''

    GEN_VERBOSE = 'GEN_DATA_MODEL::PRO::MODEL_SELECTOR'

    @classmethod
    def choose_model(cls, data_model_types, verbose=False):
        '''
            Choose type of data model.

            :param data_model_types: data model types.
            :type data_model_types: <dict>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: type of data model (1, 2, 3, ...).
            :rtype: <int>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status, input_type = ATSChecker(), None, False, -1
        error, status = checker.check_params([
            ('dict:data_model_types', data_model_types)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        verbose_message(cls.GEN_VERBOSE, verbose, 'loading options')
        print('\n {0}'.format('model option list:'))
        for index, model_type in enumerate(data_model_types['model_types']):
            option = index + 1
            for mode_type_key, model_type_params in model_type.iteritems():
                print(
                    '{0} {1} {2}'.format(
                        option, mode_type_key, model_type_params['name']
                    )
                )
        while True:
            input_type = input(' select model: ')
            options = range(1, len(data_model_types['model_types']) + 1, 1)
            try:
                if int(input_type) in list(options):
                    break
                else:
                    raise ValueError
            except ValueError:
                error_message(cls.GEN_VERBOSE, 'not an appropriate choice.')
        verbose_message(
            cls.GEN_VERBOSE, verbose, 'selected option', input_type
        )
        return input_type

    @classmethod
    def format_name(cls, model_name):
        '''
            Format file name (Format: model_<name>.py).

            :param model_name: postfix name for data model file.
            :type model_name: <str>
            :return: file name with extension (lower case).
            :rtype: <str>
            :exceptions: ATSBadCallError | ATSTypeError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([('str:model_name', model_name)])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        return 'model_{0}.py'.format(model_name.lower())

    def __str__(self):
        '''
            Dunder method for ModelSelector.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ()'.format(self.__class__.__name__)
