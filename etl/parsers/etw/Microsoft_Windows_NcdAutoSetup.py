# -*- coding: utf-8 -*-
"""
Microsoft-Windows-NcdAutoSetup
GUID : ec23f986-ae2d-4269-b52f-4e20765c1a94
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ec23f986-ae2d-4269-b52f-4e20765c1a94"), event_id=4001, version=0)
class Microsoft_Windows_NcdAutoSetup_4001_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "String2" / WString
    )


@declare(guid=guid("ec23f986-ae2d-4269-b52f-4e20765c1a94"), event_id=4002, version=0)
class Microsoft_Windows_NcdAutoSetup_4002_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "String2" / WString
    )


@declare(guid=guid("ec23f986-ae2d-4269-b52f-4e20765c1a94"), event_id=4003, version=0)
class Microsoft_Windows_NcdAutoSetup_4003_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "String2" / WString
    )


@declare(guid=guid("ec23f986-ae2d-4269-b52f-4e20765c1a94"), event_id=4004, version=0)
class Microsoft_Windows_NcdAutoSetup_4004_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "String2" / WString,
        "Integer1" / Int32ul
    )


@declare(guid=guid("ec23f986-ae2d-4269-b52f-4e20765c1a94"), event_id=4005, version=0)
class Microsoft_Windows_NcdAutoSetup_4005_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "String2" / WString
    )


@declare(guid=guid("ec23f986-ae2d-4269-b52f-4e20765c1a94"), event_id=4006, version=0)
class Microsoft_Windows_NcdAutoSetup_4006_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "String2" / WString
    )


@declare(guid=guid("ec23f986-ae2d-4269-b52f-4e20765c1a94"), event_id=4007, version=0)
class Microsoft_Windows_NcdAutoSetup_4007_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "String2" / WString
    )


@declare(guid=guid("ec23f986-ae2d-4269-b52f-4e20765c1a94"), event_id=4008, version=0)
class Microsoft_Windows_NcdAutoSetup_4008_0(Etw):
    pattern = Struct(
        "String1" / WString
    )


@declare(guid=guid("ec23f986-ae2d-4269-b52f-4e20765c1a94"), event_id=5001, version=0)
class Microsoft_Windows_NcdAutoSetup_5001_0(Etw):
    pattern = Struct(
        "String1" / WString
    )


@declare(guid=guid("ec23f986-ae2d-4269-b52f-4e20765c1a94"), event_id=5002, version=0)
class Microsoft_Windows_NcdAutoSetup_5002_0(Etw):
    pattern = Struct(
        "String1" / WString
    )


@declare(guid=guid("ec23f986-ae2d-4269-b52f-4e20765c1a94"), event_id=5003, version=0)
class Microsoft_Windows_NcdAutoSetup_5003_0(Etw):
    pattern = Struct(
        "String1" / WString
    )


@declare(guid=guid("ec23f986-ae2d-4269-b52f-4e20765c1a94"), event_id=5004, version=0)
class Microsoft_Windows_NcdAutoSetup_5004_0(Etw):
    pattern = Struct(
        "String1" / WString
    )


@declare(guid=guid("ec23f986-ae2d-4269-b52f-4e20765c1a94"), event_id=5005, version=0)
class Microsoft_Windows_NcdAutoSetup_5005_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "Integer1" / Int32ul
    )

