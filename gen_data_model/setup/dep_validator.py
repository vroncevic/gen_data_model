# -*- coding: UTF-8 -*-

'''
Module
    dep_validator.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Validator for the gen_data_model bundle dependencies.
'''

from __future__ import annotations

from collections.abc import Mapping
from ats_utilities.exceptions import ATSValueError, ATSTypeError

from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

from gen_data_model.setup.dependencies import GenDataModelBundleDependencies
from gen_data_model.setup.keys import GenDataModelBundleKeys

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_data_model'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_data_model/blob/dev/LICENSE'
__version__ = '2.3.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenDataModelBundleDependenciesValidator:
    '''
        Validator for the gen_data_model bundle dependencies.

        It defines:

            :methods:
                | validate - Validates the gen_data_model bundle dependencies.
                | is_valid - Checks if the gen_data_model bundle dependencies is valid.
    '''

    @classmethod
    def validate(cls, dependencies: GenDataModelBundleDependencies) -> None:
        '''
            Validates the gen_data_model bundle dependencies.

            :param dependencies: The gen_data_model bundle dependencies to be validated.
            :exceptions:
                | ATSValueError: The gen_data_model bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_data_model bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
        '''
        ctx: str = 'gen_data_model_bundle_dependencies_validator::validate(...)'
        msg_dependencies_none: str = 'the gen_data_model bundle dependencies must be provided'
        msg_dependencies_istype: str = 'the gen_data_model bundle dependencies must be a Mapping'

        not_none(dependencies, ctx, msg_dependencies_none)
        istype(dependencies, Mapping, ctx, msg_dependencies_istype)

        for attr_name, expected_type in GenDataModelBundleKeys.get_dependency_to_type().items():
            msg_attr_name_none: str = f'the {attr_name.replace("_", " ")} must be provided'
            msg_attr_name_istype: str = f'the {attr_name.replace("_", " ")} must be an instance of {expected_type.__name__}'

            attribute = dependencies.get(attr_name)

            not_none(attribute, ctx, msg_attr_name_none)
            istype(attribute, expected_type, ctx, msg_attr_name_istype)

    @classmethod
    def is_valid(cls, dependencies: GenDataModelBundleDependencies) -> bool:
        '''
            Checks if the gen_data_model bundle dependencies is valid.

            :param dependencies: The gen_data_model bundle dependencies to be checked.
            :return: True if valid, False otherwise.
        '''
        try:
            cls.validate(dependencies)
            return True

        except (ATSValueError, ATSTypeError):
            return False
