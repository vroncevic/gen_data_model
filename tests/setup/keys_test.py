# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenDataModelBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from gen_data_model.setup.keys import GenDataModelBundleKeys


class TestGenDataModelBundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenDataModelBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenDataModelBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenDataModelBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenDataModelBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenDataModelBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenDataModelBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenDataModelBundleKeys.OPTION_INFO_FILE, opts)
