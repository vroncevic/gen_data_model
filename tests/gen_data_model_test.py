# -*- coding: UTF-8 -*-

'''
Module
    gen_data_model_test.py
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
    Defines class GenDataModelTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of GenDataModel.
Execute
    python3 -m unittest -v gen_data_model_test
'''

import sys
from typing import List
from os import makedirs, rmdir
from unittest import TestCase, main

try:
    from gen_data_model import GenDataModel
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_data_model'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_data_model/blob/dev/LICENSE'
__version__ = '2.3.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenDataModelTestCase(TestCase):
    '''
        Defines class GenDataModelTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of GenDataModel.
        GenDataModel unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_default_create - Default on create (not None).
                | test_missing_args - Test missing args.
                | test_wrong_arg - Test wrong arg.
                | test_process - Generate project structure.
                | test_tool_not_operational - Test not operational.
                | test_pro_already_exists - Test pro already exists.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_default_create(self) -> None:
        '''Default on create (not None)'''
        generator: GenDataModel = GenDataModel()
        self.assertIsNotNone(generator)

    def test_missing_args(self) -> None:
        '''Test missing args'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_gen_data_model_run.py')
        generator: GenDataModel = GenDataModel()
        self.assertFalse(generator.process())

    def test_wrong_arg(self) -> None:
        '''Test wrong arg'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_gen_data_model_run.py')
        sys.argv.insert(2, '-d')
        sys.argv.insert(3, 'wrong_pro')
        sys.argv.insert(4, '-t')
        sys.argv.insert(5, 'django')
        generator: GenDataModel = GenDataModel()
        self.assertFalse(generator.process())

    def test_process(self) -> None:
        '''Generate project structure'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_gen_data_model_run.py')
        sys.argv.insert(2, '-g')
        sys.argv.insert(3, 'latest_pro')
        sys.argv.insert(4, '-t')
        sys.argv.insert(5, 'django')
        generator: GenDataModel = GenDataModel()
        self.assertTrue(generator.process())

    def test_tool_not_operational(self) -> None:
        '''Test not operational'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_gen_data_model_run.py')
        sys.argv.insert(2, '-g')
        sys.argv.insert(3, 'fresh')
        sys.argv.insert(4, '-t')
        sys.argv.insert(5, 'django')
        generator: GenDataModel = GenDataModel()
        generator.tool_operational = False
        self.assertFalse(generator.process())

    def test_pro_already_exists(self) -> None:
        '''Test pro already exists'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_gen_data_model_run.py')
        sys.argv.insert(2, '-g')
        sys.argv.insert(3, 'fresh_new')
        sys.argv.insert(4, '-t')
        sys.argv.insert(5, 'django')
        generator: GenDataModel = GenDataModel()
        makedirs('fresh_new')
        self.assertFalse(generator.process())
        rmdir('fresh_new')


if __name__ == '__main__':
    main()
