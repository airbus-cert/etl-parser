# -*- coding: utf-8 -*-

import unittest
from construct import Enum, Int8ul, CheckError
from etl.utils import check_enum


class TestUtilsModule(unittest.TestCase):
    """
    Test all functions presents in the utils module
    """
    def test_check_enum_ok(self):
        """
        Test check enum function with valid value
        """
        enum = Enum(
            Int8ul,
            VAL_1=0x01,
            VAL_2=0x02
        )
        check_enum(enum).parse(b"\x01")

    def test_check_enum_ko(self):
        """
        Test check enum with invalid value
        """
        enum = Enum(
            Int8ul,
            VAL_1=0x01,
            VAL_2=0x02
        )
        self.assertRaises(CheckError,  check_enum(enum).parse, b"\x03")
