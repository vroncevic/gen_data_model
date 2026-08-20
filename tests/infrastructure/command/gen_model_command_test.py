# -*- coding: UTF-8 -*-

'''
Module
    gen_model_command_test.py
Info
    Unit tests for GenModelCommandDefinition and GenModelCommandExecutor.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from gen_data_model.core.service.iservice import IService
from gen_data_model.infrastructure.command.gen_model_command_definition import GenModelCommandDefinition
from gen_data_model.infrastructure.command.gen_model_command_executor import GenModelCommandExecutor


class TestGenModelCommand(unittest.TestCase):

    def test_definition(self) -> None:
        definition = GenModelCommandDefinition()
        self.assertEqual(definition.name, 'create')
        self.assertEqual(definition.help_text, 'Generate data model skeleton files')
        self.assertEqual(len(definition.options), 3)
        self.assertTrue(isinstance(str(definition), str))

    def test_executor_execute_success(self) -> None:
        definition = GenModelCommandDefinition()
        executor = GenModelCommandExecutor(definition)
        
        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = True
        mock_service.execute.return_value = {'returncode': 0}
        
        params = {'name': 'test', 'type': 'django', 'output': '.'}
        result = executor.execute(params=params, service=mock_service)
        
        self.assertEqual(result['returncode'], 0)
        mock_service.execute.assert_called_once_with(params=params)

    def test_executor_execute_not_initialized(self) -> None:
        definition = GenModelCommandDefinition()
        executor = GenModelCommandExecutor(definition)
        
        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = False
        
        result = executor.execute(params={}, service=mock_service)
        self.assertEqual(result['returncode'], 1)
        self.assertIn('service not initialized', result['stderr'])

    def test_executor_str_representation(self) -> None:
        definition = GenModelCommandDefinition()
        executor = GenModelCommandExecutor(definition)
        self.assertTrue(isinstance(str(executor), str))

    def test_executor_get_definition(self) -> None:
        definition = GenModelCommandDefinition()
        executor = GenModelCommandExecutor(definition)
        self.assertEqual(executor.get_definition(), definition)

