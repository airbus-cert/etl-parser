# -*- coding: utf-8 -*-
"""
Microsoft-Windows-UserDataAccess-UserDataUtils
GUID : d1f688bf-012f-4aec-a38c-e7d4649f8cd2
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d1f688bf-012f-4aec-a38c-e7d4649f8cd2"), event_id=1, version=0)
class Microsoft_Windows_UserDataAccess_UserDataUtils_1_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("d1f688bf-012f-4aec-a38c-e7d4649f8cd2"), event_id=2, version=0)
class Microsoft_Windows_UserDataAccess_UserDataUtils_2_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("d1f688bf-012f-4aec-a38c-e7d4649f8cd2"), event_id=3, version=0)
class Microsoft_Windows_UserDataAccess_UserDataUtils_3_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("d1f688bf-012f-4aec-a38c-e7d4649f8cd2"), event_id=101, version=0)
class Microsoft_Windows_UserDataAccess_UserDataUtils_101_0(Etw):
    pattern = Struct(
        "Prop_LINE_UInt32" / Int32ul,
        "Prop_Trace_UnicodeString" / WString
    )


@declare(guid=guid("d1f688bf-012f-4aec-a38c-e7d4649f8cd2"), event_id=102, version=0)
class Microsoft_Windows_UserDataAccess_UserDataUtils_102_0(Etw):
    pattern = Struct(
        "Prop_Trace_UnicodeString" / WString
    )


@declare(guid=guid("d1f688bf-012f-4aec-a38c-e7d4649f8cd2"), event_id=103, version=0)
class Microsoft_Windows_UserDataAccess_UserDataUtils_103_0(Etw):
    pattern = Struct(
        "Prop_Trace_UnicodeString" / WString
    )


@declare(guid=guid("d1f688bf-012f-4aec-a38c-e7d4649f8cd2"), event_id=104, version=0)
class Microsoft_Windows_UserDataAccess_UserDataUtils_104_0(Etw):
    pattern = Struct(
        "Prop_Trace_UnicodeString" / WString
    )


@declare(guid=guid("d1f688bf-012f-4aec-a38c-e7d4649f8cd2"), event_id=105, version=0)
class Microsoft_Windows_UserDataAccess_UserDataUtils_105_0(Etw):
    pattern = Struct(
        "P1_UnicodeString" / WString,
        "P1_UInt32" / Int32ul
    )


@declare(guid=guid("d1f688bf-012f-4aec-a38c-e7d4649f8cd2"), event_id=106, version=0)
class Microsoft_Windows_UserDataAccess_UserDataUtils_106_0(Etw):
    pattern = Struct(
        "P1_UnicodeString" / WString,
        "P1_UInt32" / Int32ul
    )


@declare(guid=guid("d1f688bf-012f-4aec-a38c-e7d4649f8cd2"), event_id=107, version=0)
class Microsoft_Windows_UserDataAccess_UserDataUtils_107_0(Etw):
    pattern = Struct(
        "P1_UnicodeString" / WString,
        "P1_UInt32" / Int32ul
    )


@declare(guid=guid("d1f688bf-012f-4aec-a38c-e7d4649f8cd2"), event_id=301, version=0)
class Microsoft_Windows_UserDataAccess_UserDataUtils_301_0(Etw):
    pattern = Struct(
        "P1_HexInt32" / Int32sl,
        "Prop_Handle" / Int32ul,
        "Prop_Handle2" / Int32ul
    )


@declare(guid=guid("d1f688bf-012f-4aec-a38c-e7d4649f8cd2"), event_id=401, version=0)
class Microsoft_Windows_UserDataAccess_UserDataUtils_401_0(Etw):
    pattern = Struct(
        "P1_UnicodeString" / WString
    )


@declare(guid=guid("d1f688bf-012f-4aec-a38c-e7d4649f8cd2"), event_id=402, version=0)
class Microsoft_Windows_UserDataAccess_UserDataUtils_402_0(Etw):
    pattern = Struct(
        "P1_UnicodeString" / WString
    )


@declare(guid=guid("d1f688bf-012f-4aec-a38c-e7d4649f8cd2"), event_id=501, version=0)
class Microsoft_Windows_UserDataAccess_UserDataUtils_501_0(Etw):
    pattern = Struct(
        "P1_Int32" / Int32sl
    )


@declare(guid=guid("d1f688bf-012f-4aec-a38c-e7d4649f8cd2"), event_id=502, version=0)
class Microsoft_Windows_UserDataAccess_UserDataUtils_502_0(Etw):
    pattern = Struct(
        "P1_Int32" / Int32sl
    )


@declare(guid=guid("d1f688bf-012f-4aec-a38c-e7d4649f8cd2"), event_id=600, version=0)
class Microsoft_Windows_UserDataAccess_UserDataUtils_600_0(Etw):
    pattern = Struct(
        "P1_Int32" / Int32sl
    )


@declare(guid=guid("d1f688bf-012f-4aec-a38c-e7d4649f8cd2"), event_id=601, version=0)
class Microsoft_Windows_UserDataAccess_UserDataUtils_601_0(Etw):
    pattern = Struct(
        "P1_UnicodeString" / WString,
        "P2_UnicodeString" / WString
    )


@declare(guid=guid("d1f688bf-012f-4aec-a38c-e7d4649f8cd2"), event_id=602, version=0)
class Microsoft_Windows_UserDataAccess_UserDataUtils_602_0(Etw):
    pattern = Struct(
        "P1_HexInt32" / Int32sl,
        "P2_HexInt32" / Int32sl
    )

