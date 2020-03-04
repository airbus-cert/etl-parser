# -*- coding: utf-8 -*-

import unittest

from construct import ListContainer, Container

from etl.parsers.etw.core import Guid, guid
from etl.parsers.tracelogging import build_tracelogging
from etl.error import TlMetaDataNotFound, TlUnhandledTag


class TraceloggingParser(unittest.TestCase):
    def test_tracelogging_wstring(self):
        """
        Test the normal build of a trace logging
        The name of the event is AmsiScript
        This bin have three meta field to parse :
        * Engine : name of the script engine
        * Script : raw script for encoded in wide string
        * Raw Script : raw script not encode (Array of UINT16)
        """
        event = Container()
        meta = Container()
        meta.ext_type = 11
        meta.data_item = b'\x10\x00\x00Test\x00Engine\x00\x01'
        event.extended_data = ListContainer([meta])
        event.user_data = b'P\x00o\x00w\x00e\x00r\x00S\x00h\x00e\x00l\x00l\x00\x00\x00'
        tl = build_tracelogging(event)
        self.assertEqual(tl.get_name(), "Test", "Invalid Name")
        self.assertEqual(tl["Engine"], "PowerShell", "Invalid Name")

    def test_wrong_meta(self):
        """
        Test parser if have metadata with wrong flag
        """
        event = Container()
        meta = Container()
        meta.ext_type = 12 # wrong flag
        meta.data_item = b''
        event.extended_data = ListContainer([meta])
        event.user_data = b''
        self.assertRaises(TlMetaDataNotFound, build_tracelogging, event)

    def test_miss_meta(self):
        """
        Test parser if no metadata is set
        """
        event = Container()
        event.extended_data = ListContainer([])
        event.user_data = b''
        self.assertRaises(TlMetaDataNotFound, build_tracelogging, event)

    def test_invalid_tag(self):
        """
        Test parser if have metadata with wrong flag
        """
        event = Container()
        meta = Container()
        meta.ext_type = 11  # wrong flag
        meta.data_item = b'\x10\x00\x00Test\x00Engine\x00\x1f' #not existing tag
        event.extended_data = ListContainer([meta])
        event.user_data = b''
        self.assertRaises(TlUnhandledTag, build_tracelogging, event)

    def test_tracelogging_guid(self):
        """
        Test a trace named Test and log GUI
        """
        event = Container()
        meta = Container()
        meta.ext_type = 11
        meta.data_item = b'\x10\x00\x00Test\x00Engine\x00\x0F'
        event.extended_data = ListContainer([meta])
        event.user_data = b'\x00'*16
        tl = build_tracelogging(event)
        self.assertEqual(tl.get_name(), "Test", "Invalid Name")
        parsed_guid = tl["Engine"]
        self.assertEqual(Guid(parsed_guid.data1, parsed_guid.data2, parsed_guid.data3, parsed_guid.data4), guid("00000000-0000-0000-0000-000000000000"), "Invalid GUID")

    def test_array_uint8(self):
        """
        Test the deserialization of an array UINT8 element
        """
        event = Container()
        meta = Container()
        meta.ext_type = 11
        meta.data_item = b'\x10\x00\x00Test\x00Engine\x00\x23'
        event.extended_data = ListContainer([meta])
        event.user_data = b'\x10\x00' + b'\x01' * 16
        tl = build_tracelogging(event)
        self.assertEqual(tl.get_name(), "Test", "Invalid Name")
        self.assertEqual(tl["Engine"], [1] * 16)

    def test_array_uint16(self):
        """
        Test the deserialization of an array UINT16 element
        """
        event = Container()
        meta = Container()
        meta.ext_type = 11
        meta.data_item = b'\x10\x00\x00Test\x00Engine\x00\x26'
        event.extended_data = ListContainer([meta])
        event.user_data = b'\x10\x00' + b'\x00' * 32
        tl = build_tracelogging(event)
        self.assertEqual(tl.get_name(), "Test", "Invalid Name")
        self.assertEqual(tl["Engine"], [0] * 16)