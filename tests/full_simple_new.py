# -*- coding: utf-8 -*-

'''
Module
    full_simple_new.py
Copyright
    Copyright (C) 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
    full_simple_new is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    full_simple_new is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines class Full_simple_new with attribute(s) and method(s).
    Defines model Full_simple_new.
'''

import sys
from typing import List

try:
    from .model_base import Base
except ImportError as error:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{error}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, Free software to use and distributed it.'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Full_simple_new(Base):
    '''
        Defines class Full_simple_new with attribute(s) and method(s).
        Defines model Full_simple_new.

        It defines:

            :attributes:
                | None
            :methods:
                | None
    '''

    class Meta:
        '''
            Define class meta with attribute(s) and method(s).
            Meta class.

            It defines:

                :attributes:
                    | db_table - database table.
                :methods:
                    | None
        '''

        db_table = 'Full_simple_new'
