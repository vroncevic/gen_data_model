# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
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
     Defined class GenModel with attribute(s) and method(s).
     Generate data model by templates and parameters.
'''

import sys

try:
    from pathlib import Path
    from gen_data_model.pro.read_template import ReadTemplate
    from gen_data_model.pro.write_template import WriteTemplate
    from gen_data_model.pro.model_selector import ModelSelector
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.success import success_message
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
__version__ = '1.5.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenModel:
    '''
        Defined class GenModel with attribute(s) and method(s).
        Generate data model by templates and parameters.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | __reader - reader API.
                | __writer - writer API.
            :methods:
                | __init__ - initial constructor.
                | get_reader - get reader object.
                | get_writer - get writer object.
                | gen_model - generate data model.
                | __str__ - dunder method for GenModel.
    '''

    GEN_VERBOSE = 'GEN_DATA_MODEL::PRO::GEN_MODEL'

    def __init__(self, model_name, verbose=False):
        '''
            Initial constructor.

            :param model_name: data model name.
            :type model_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([('str:model_name', model_name)])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        verbose_message(GenModel.GEN_VERBOSE, verbose, 'init generator')
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)
        self.model_name = model_name

    def get_reader(self):
        '''
            Get reader object.

            :return: read template object.
            :rtype: <ReadTemplate>
            :exceptions: None
        '''
        return self.__reader

    def get_writer(self):
        '''
            Get writer object.

            :return: write template object.
            :rtype: <WriteTemplate>
            :exceptions: None
        '''
        return self.__writer

    def gen_model(self, verbose=False):
        '''
            Generate data model.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: True (success) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        status = False
        verbose_message(
            GenModel.GEN_VERBOSE, verbose, 'generate model', self.model_name
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

    def __str__(self):
        '''
            Dunder method for GenModel.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3})'.format(
            self.__class__.__name__, str(self.__reader),
            str(self.__writer), str(self.model_name)
        )
