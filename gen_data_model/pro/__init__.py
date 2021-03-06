# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
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
     Generate data model by templates and parameters.
'''

import sys

try:
    from pathlib import Path
    from ats_utilities.checker import ATSChecker
    from gen_data_model.pro.read_template import ReadTemplate
    from gen_data_model.pro.write_template import WriteTemplate
    from gen_data_model.pro.model_selector import ModelSelector
    from ats_utilities.console_io.success import success_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.2.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenModel(object):
    '''
        Define class GenModel with attribute(s) and method(s).
        Generate data model by templates and parameters.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __MODEL_TYPES - Data model types.
                | __config - Configuration structure.
                | __reader - Reader API.
                | __writer - Writer API.
            :methods:
                | __init__ - Initial constructor.
                | get_reader - Get reader object.
                | get_writer - Get writer object.
                | gen_model - Generate data model.
    '''

    __slots__ = ('VERBOSE', '__config', '__reader', '__writer', 'model_name')
    VERBOSE = 'GEN_DATA_MODEL::PRO::GEN_MODEL'

    def __init__(self, model_name, verbose=False):
        '''
            Initial constructor.

            :param model_name: Data model name.
            :type model_name: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params(
            [('str:model_name', model_name)]
        )
        if status == ATSChecker.TYPE_ERROR: raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR: raise ATSBadCallError(error)
        verbose_message(GenModel.VERBOSE, verbose, 'init generator')
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)
        self.model_name = model_name

    def get_reader(self):
        '''
            Get reader object.

            :return: Read template object.
            :rtype: <ReadTemplate>
            :exceptions: None
        '''
        return self.__reader

    def get_writer(self):
        '''
            Get writer object.

            :return: Write template object.
            :rtype: <WriteTemplate>
            :exceptions: None
        '''
        return self.__writer

    def gen_model(self, verbose=False):
        '''
            Generate data model.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: True (success) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        status, model_type = False, None
        verbose_message(
            GenModel.VERBOSE, verbose, 'generate model', self.model_name
        )
        base_content, model_content = None, None
        base_content, model_content = self.__reader.read(verbose=verbose)
        if all([base_content, model_content]):
            if all([base_content == 'Cancel', model_content == 'Cancel']):
                status = True
            else:
                model_generated = [
                    self.__writer.write(
                        base_content, 'base', verbose=verbose
                    ),
                    self.__writer.write(
                        model_content, self.model_name, verbose=verbose
                    )
                ]
                if all(model_generated):
                    status = True
        return True if status else False
