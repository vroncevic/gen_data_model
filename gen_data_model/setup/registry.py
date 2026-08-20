# -*- coding: UTF-8 -*-

'''
Module
    registry.py
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
    Encapsulates core gen_data_model components for simplification of gen_data_model bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle

from gen_data_model.core.service.iservice import IService
from gen_data_model.core.service.isubprocessor import ISubProcessor
from gen_data_model.infrastructure.cli.icli import ICLI
from gen_data_model.setup.bundle import GenDataModelBundle
from gen_data_model.setup.validator import GenDataModelBundleValidator
from gen_data_model.setup.keys import GenDataModelBundleKeys
from gen_data_model.setup.dependencies import GenDataModelBundleDependencies
from gen_data_model.setup.dep_validator import GenDataModelBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_data_model'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_data_model/blob/dev/LICENSE'
__version__ = '2.3.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenDataModelBundleRegistry:
    '''
        Encapsulates core gen_data_model components for simplification of gen_data_model bundle.

        It defines:

            :methods:
                | create_bundle - Creates the gen_data_model bundle.
                | get_version - Returns the registry version.
    '''

    @classmethod
    def create_bundle(cls, dependencies: GenDataModelBundleDependencies) -> GenDataModelBundle:
        '''
            Creates the gen_data_model bundle.

            :param dependencies: The gen_data_model bundle dependencies.
            :return: The gen_data_model bundle.
            :exceptions:
                | ATSValueError: The gen_data_model bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_data_model bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_data_model bundle must be provided and have proper values.
                | ATSTypeError:  The gen_data_model bundle must be an instance of GenDataModelBundle and
                |                its attributes must be instances of their respective types.
        '''
        GenDataModelBundleDependenciesValidator.validate(dependencies)

        base: BaseBundle | None = dependencies.get(GenDataModelBundleKeys.DEPENDENCY_BASE) if dependencies else None
        service: IService | None = dependencies.get(GenDataModelBundleKeys.DEPENDENCY_SERVICE) if dependencies else None
        subprocessor: ISubProcessor | None = dependencies.get(GenDataModelBundleKeys.DEPENDENCY_SUBPROCESSOR) if dependencies else None
        cli: ICLI | None = dependencies.get(GenDataModelBundleKeys.DEPENDENCY_CLI) if dependencies else None

        bundle: GenDataModelBundle = GenDataModelBundle(base=base, service=service, subprocessor=subprocessor, cli=cli)

        GenDataModelBundleValidator.validate(bundle)

        return bundle

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the registry version.

            :return: The registry version.
            :exceptions: None.
        '''
        return __version__
