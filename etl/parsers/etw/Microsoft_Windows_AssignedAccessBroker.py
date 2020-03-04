# -*- coding: utf-8 -*-
"""
Microsoft-Windows-AssignedAccessBroker
GUID : f2311b48-32be-4902-a22a-7240371dbb2c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f2311b48-32be-4902-a22a-7240371dbb2c"), event_id=30000, version=0)
class Microsoft_Windows_AssignedAccessBroker_30000_0(Etw):
    pattern = Struct(
        "AboveLockAppAUMID" / WString,
        "InterfaceType" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("f2311b48-32be-4902-a22a-7240371dbb2c"), event_id=30003, version=0)
class Microsoft_Windows_AssignedAccessBroker_30003_0(Etw):
    pattern = Struct(
        "Result" / Int8ul
    )


@declare(guid=guid("f2311b48-32be-4902-a22a-7240371dbb2c"), event_id=30004, version=0)
class Microsoft_Windows_AssignedAccessBroker_30004_0(Etw):
    pattern = Struct(
        "CustomMessage" / WString,
        "HResult" / Int32ul,
        "Address" / Int64ul
    )


@declare(guid=guid("f2311b48-32be-4902-a22a-7240371dbb2c"), event_id=30005, version=0)
class Microsoft_Windows_AssignedAccessBroker_30005_0(Etw):
    pattern = Struct(
        "Interface" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("f2311b48-32be-4902-a22a-7240371dbb2c"), event_id=30007, version=0)
class Microsoft_Windows_AssignedAccessBroker_30007_0(Etw):
    pattern = Struct(
        "Interface" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("f2311b48-32be-4902-a22a-7240371dbb2c"), event_id=30008, version=0)
class Microsoft_Windows_AssignedAccessBroker_30008_0(Etw):
    pattern = Struct(
        "Operation" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("f2311b48-32be-4902-a22a-7240371dbb2c"), event_id=30009, version=0)
class Microsoft_Windows_AssignedAccessBroker_30009_0(Etw):
    pattern = Struct(
        "RequestAction" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("f2311b48-32be-4902-a22a-7240371dbb2c"), event_id=30010, version=0)
class Microsoft_Windows_AssignedAccessBroker_30010_0(Etw):
    pattern = Struct(
        "Result" / Int8ul
    )

