# -*- coding: utf-8 -*-

'''
Module
    base_model.py
Copyright
    Copyright (C) 2023 Vladimir Roncevic <elektron.ronca@gmail.com>
    base is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    base is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines class Base with attribute(s) and method(s).
    Abstract data model.
'''

import sys
from typing import List

try:
    from django.db import models
except ImportError as error:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{error}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2023, Free software to use and distributed it.'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Base(models.Model):
    '''
        Define class Base with attribute(s) and method(s).
        Abstract data model.

        It defines:

            :attributes:
                | created - date of creation.
                | modified - date of modification.
            :methods:
                | None
    '''

    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
