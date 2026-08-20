# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
Info
    Unit tests for GenDataModelBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest

from gen_data_model.setup.opt_validator import GenDataModelBundleOptionsValidator


class TestGenDataModelBundleOptionsValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        options = {'info_file': 'some_path'}
        GenDataModelBundleOptionsValidator.validate(options)

    def test_validate_none(self) -> None:
        with self.assertRaises(Exception):
            GenDataModelBundleOptionsValidator.validate(None)

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            GenDataModelBundleOptionsValidator.validate("not_a_mapping")

            options = {'info_file': 123}
            GenDataModelBundleOptionsValidator.validate(options)

    def test_is_valid_success(self) -> None:
        options = {'info_file': 'some_path'}
        self.assertTrue(GenDataModelBundleOptionsValidator.is_valid(options))

    def test_is_valid_failure(self) -> None:
        self.assertFalse(GenDataModelBundleOptionsValidator.is_valid(None))
        self.assertFalse(GenDataModelBundleOptionsValidator.is_valid("not_a_mapping"))
        self.assertFalse(GenDataModelBundleOptionsValidator.is_valid({'info_file': 123}))

