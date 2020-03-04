# -*- coding: utf-8 -*-
"""
Microsoft-Windows-UserDataAccess-UserDataApis
GUID : b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=1, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_1_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=2, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_2_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=10, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_10_0(Etw):
    pattern = Struct(
        "Prop_UnicodeString" / WString
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=102, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_102_0(Etw):
    pattern = Struct(
        "Prop_HexInt32" / Int32ul
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=103, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_103_0(Etw):
    pattern = Struct(
        "Prop_HexInt32" / Int32ul
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=104, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_104_0(Etw):
    pattern = Struct(
        "Prop_UnicodeString_1" / WString,
        "Prop_UnicodeString_2" / WString
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=105, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_105_0(Etw):
    pattern = Struct(
        "Prop_HexInt32" / Int32ul,
        "Prop_Guid" / Guid
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=106, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_106_0(Etw):
    pattern = Struct(
        "Prop_HexInt32" / Int32ul
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=120, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_120_0(Etw):
    pattern = Struct(
        "Prop_HexInt32" / Int32ul
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=121, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_121_0(Etw):
    pattern = Struct(
        "Prop_HexInt32" / Int32ul
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=122, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_122_0(Etw):
    pattern = Struct(
        "Prop_HexInt32" / Int32ul
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=123, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_123_0(Etw):
    pattern = Struct(
        "Prop_HexInt32" / Int32ul
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=124, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_124_0(Etw):
    pattern = Struct(
        "Prop_HexInt32" / Int32ul
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=145, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_145_0(Etw):
    pattern = Struct(
        "Prop_UInt_1" / Int32ul
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=401, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_401_0(Etw):
    pattern = Struct(
        "Prop_UnicodeString" / WString
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=402, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_402_0(Etw):
    pattern = Struct(
        "Prop_UnicodeString" / WString
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=403, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_403_0(Etw):
    pattern = Struct(
        "Prop_UnicodeString" / WString
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=404, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_404_0(Etw):
    pattern = Struct(
        "Prop_UInt_1" / Int32ul
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=405, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_405_0(Etw):
    pattern = Struct(
        "Prop_UInt_1" / Int32ul
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=500, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_500_0(Etw):
    pattern = Struct(
        "Prop_UnicodeString" / WString
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=501, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_501_0(Etw):
    pattern = Struct(
        "Prop_UnicodeString" / WString
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=502, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_502_0(Etw):
    pattern = Struct(
        "Prop_UnicodeString" / WString
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=600, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_600_0(Etw):
    pattern = Struct(
        "Prop_Guid" / Guid
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=1000, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_1000_0(Etw):
    pattern = Struct(
        "Prop_UInt_1" / Int32ul,
        "Prop_UInt_2" / Int32ul
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=1001, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_1001_0(Etw):
    pattern = Struct(
        "Prop_UInt_1" / Int32ul
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=1002, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_1002_0(Etw):
    pattern = Struct(
        "Prop_UInt_1" / Int32ul
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=1006, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_1006_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=1007, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_1007_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=1008, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_1008_0(Etw):
    pattern = Struct(
        "Prop_ULong" / Int64ul
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=1009, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_1009_0(Etw):
    pattern = Struct(
        "Prop_UnicodeString" / WString
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=1010, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_1010_0(Etw):
    pattern = Struct(
        "Prop_UInt_1" / Int32ul,
        "Prop_UInt_2" / Int32ul
    )


@declare(guid=guid("b9b2de3c-3fbd-4f42-8ff7-33c3bad35fd4"), event_id=1013, version=0)
class Microsoft_Windows_UserDataAccess_UserDataApis_1013_0(Etw):
    pattern = Struct(
        "Prop_BOOL" / Int8ul
    )

