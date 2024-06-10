# -*- coding: utf-8 -*-

'''
Module
    latest_pro.py
Copyright
    Copyright (C) 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
    latest_pro is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    latest_pro is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines class Latest_pro with attribute(s) and method(s).
    Defines model Latest_pro.
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


class Latest_pro(Base):
    '''
        Defines class Latest_pro with attribute(s) and method(s).
        Defines model Latest_pro.

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

        db_table = 'Latest_pro'
