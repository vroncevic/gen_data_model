# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating the gen_data_model bundle.
'''

from __future__ import annotations

from os.path import abspath, dirname, join

from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextBundleFactory

from gen_data_model.setup.bundle import GenDataModelBundle
from gen_data_model.setup.options import GenDataModelBundleOptions
from gen_data_model.setup.registry import GenDataModelBundleRegistry
from gen_data_model.setup.dependencies import GenDataModelBundleDependencies
from gen_data_model.setup.opt_validator import GenDataModelBundleOptionsValidator
from gen_data_model.setup.keys import GenDataModelBundleKeys
from gen_data_model.core.service.engine import Service
from gen_data_model.infrastructure.subprocessor import SubProcessor
from gen_data_model.infrastructure.cli.engine import CLI
from gen_data_model.infrastructure.cli.setup.bundle import CLIBundle
from gen_data_model.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from gen_data_model.infrastructure.cli.setup.registry import CLIBundleRegistry
from gen_data_model.infrastructure.command.command import CommandBundle
from gen_data_model.infrastructure.command.gen_model_command_definition import GenModelCommandDefinition
from gen_data_model.infrastructure.command.gen_model_command_executor import GenModelCommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_data_model'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_data_model/blob/dev/LICENSE'
__version__ = '2.3.9'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenDataModelBundleFactory:
    '''
        Factory for creating the gen_data_model bundle.

        It defines:

            :attributes:
                | _info_file - Path to the gen_data_model info file.
            :methods:
                | create_bundle - Creates the gen_data_model bundle with optional pre-configured options.
                | get_version - Returns the factory version.
    '''

    _info_file: str = join(
        dirname(dirname(abspath(__file__))), 'infrastructure', 'config', 'gen_data_model.cfg'
    )

    @classmethod
    def create_bundle(cls, options: GenDataModelBundleOptions | None = None) -> GenDataModelBundle:
        '''
            Creates the gen_data_model bundle with optional pre-configured options.

            :param options: The pre-configured options for the gen_data_model bundle.
            :return: The gen_data_model bundle.
            :exceptions:
                | ATSValueError: The gen_data_model bundle options must be provided and have proper values.
                | ATSTypeError:  The gen_data_model bundle options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_data_model bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_data_model bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_data_model bundle must be provided and have proper values.
                | ATSTypeError:  The gen_data_model bundle must be an instance of GenDataModelBundle and
                |                its attributes must be instances of their respective types.
        '''
        if options is not None:
            GenDataModelBundleOptionsValidator.validate(options)

        info_file = options.get(GenDataModelBundleKeys.OPTION_INFO_FILE) if options else cls._info_file

        context_bundle: ContextBundle = ContextBundleFactory.create_bundle()

        base_bundle: BaseBundle = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file=info_file,
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        subprocessor: SubProcessor = SubProcessor(generator=base_bundle.generation_manager)

        service: Service = Service(subprocessor=subprocessor)

        gen_model_definition: GenModelCommandDefinition = GenModelCommandDefinition()

        gen_model_bundle: CommandBundle = CommandBundle(
            definition=gen_model_definition,
            executor=GenModelCommandExecutor(gen_model_definition)
        )

        cli_bundle: CLIBundle = CLIBundleRegistry.create_bundle(
            dependencies=CLIBundleDependencies(
                service=service,
                parser=base_bundle.option_manager,
                commands=[gen_model_bundle]
            )
        )

        cli: CLI = CLI(cli_bundle)

        return GenDataModelBundleRegistry.create_bundle(
            dependencies=GenDataModelBundleDependencies(
                base=base_bundle,
                service=service,
                subprocessor=subprocessor,
                cli=cli
            )
        )

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the factory version.

            :return: The factory version.
            :exceptions: None.
        '''
        return __version__
