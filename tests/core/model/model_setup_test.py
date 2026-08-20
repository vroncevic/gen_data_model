# -*- coding: UTF-8 -*-

'''
Module
    model_setup_test.py
Info
    Unit tests for ModelSetup class.
'''

from __future__ import annotations

import unittest

from gen_data_model.core.model.model_setup import ModelSetup


class TestModelSetup(unittest.TestCase):
    def test_model_setup_initialization(self) -> None:
        model_config = {'key': 'value'}
        setup = ModelSetup(model_config=model_config)
        self.assertEqual(setup.model_config, model_config)
