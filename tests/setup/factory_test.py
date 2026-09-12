# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenDataModelBundleFactory class.
'''

from __future__ import annotations

import unittest

from gen_data_model.setup.bundle import GenDataModelBundle
from gen_data_model.setup.factory import GenDataModelBundleFactory


class TestGenDataModelBundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenDataModelBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenDataModelBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_data_model/infrastructure/config/gen_data_model.cfg'}
        bundle = GenDataModelBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenDataModelBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenDataModelBundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(GenDataModelBundleFactory.get_version(), '2.3.9')

