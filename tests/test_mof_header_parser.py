# -*- coding: utf-8 -*-

import unittest

from etl.parsers.kernel.core import build_mof
from etl.parsers.kernel.header import Header_Extension_TypeGroup
from etl.wmi import EventTraceGroup


class TestMofHeaderParser(unittest.TestCase):
    def test_header_extension_typegroup_type32(self):
        payload = b'\x07\x03\x00\x00\x04\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00F\x00\x00\x00'
        mof = build_mof(EventTraceGroup.EVENT_TRACE_GROUP_HEADER, 2, 32, payload)
        self.assertIsInstance(mof, Header_Extension_TypeGroup)
