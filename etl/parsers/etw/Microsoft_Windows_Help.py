# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Help
GUID : de513a55-c345-438b-9a74-e18cac5c5cc5
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=52, version=0)
class Microsoft_Windows_Help_52_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=53, version=0)
class Microsoft_Windows_Help_53_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=54, version=0)
class Microsoft_Windows_Help_54_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=55, version=0)
class Microsoft_Windows_Help_55_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=56, version=0)
class Microsoft_Windows_Help_56_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=57, version=0)
class Microsoft_Windows_Help_57_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=62, version=0)
class Microsoft_Windows_Help_62_0(Etw):
    pattern = Struct(
        "sessionid" / Int32ul
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=63, version=0)
class Microsoft_Windows_Help_63_0(Etw):
    pattern = Struct(
        "sessionid" / Int32ul
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=100, version=0)
class Microsoft_Windows_Help_100_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=101, version=0)
class Microsoft_Windows_Help_101_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=102, version=0)
class Microsoft_Windows_Help_102_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=103, version=0)
class Microsoft_Windows_Help_103_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=104, version=0)
class Microsoft_Windows_Help_104_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=105, version=0)
class Microsoft_Windows_Help_105_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=106, version=0)
class Microsoft_Windows_Help_106_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=107, version=0)
class Microsoft_Windows_Help_107_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=134, version=0)
class Microsoft_Windows_Help_134_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=135, version=0)
class Microsoft_Windows_Help_135_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=144, version=0)
class Microsoft_Windows_Help_144_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=145, version=0)
class Microsoft_Windows_Help_145_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=146, version=0)
class Microsoft_Windows_Help_146_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=147, version=0)
class Microsoft_Windows_Help_147_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=148, version=0)
class Microsoft_Windows_Help_148_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=149, version=0)
class Microsoft_Windows_Help_149_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=1001, version=0)
class Microsoft_Windows_Help_1001_0(Etw):
    pattern = Struct(
        "cause" / WString,
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=1002, version=0)
class Microsoft_Windows_Help_1002_0(Etw):
    pattern = Struct(
        "url" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=1003, version=0)
class Microsoft_Windows_Help_1003_0(Etw):
    pattern = Struct(
        "Win32LastError" / Int32ul
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=1004, version=0)
class Microsoft_Windows_Help_1004_0(Etw):
    pattern = Struct(
        "Win32LastError" / Int32ul
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=1005, version=0)
class Microsoft_Windows_Help_1005_0(Etw):
    pattern = Struct(
        "Win32LastError" / Int32ul
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=1010, version=0)
class Microsoft_Windows_Help_1010_0(Etw):
    pattern = Struct(
        "Win32LastError" / Int32ul
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=1011, version=0)
class Microsoft_Windows_Help_1011_0(Etw):
    pattern = Struct(
        "Win32LastError" / Int32ul
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=1012, version=0)
class Microsoft_Windows_Help_1012_0(Etw):
    pattern = Struct(
        "Win32LastError" / Int32ul
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=1013, version=0)
class Microsoft_Windows_Help_1013_0(Etw):
    pattern = Struct(
        "Win32LastError" / Int32ul
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=1020, version=0)
class Microsoft_Windows_Help_1020_0(Etw):
    pattern = Struct(
        "ApplicationErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=1021, version=0)
class Microsoft_Windows_Help_1021_0(Etw):
    pattern = Struct(
        "ApplicationErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=1022, version=0)
class Microsoft_Windows_Help_1022_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=1023, version=0)
class Microsoft_Windows_Help_1023_0(Etw):
    pattern = Struct(
        "Win32LastError" / Int32ul
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=1024, version=0)
class Microsoft_Windows_Help_1024_0(Etw):
    pattern = Struct(
        "ApplicationErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=1025, version=0)
class Microsoft_Windows_Help_1025_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=1030, version=0)
class Microsoft_Windows_Help_1030_0(Etw):
    pattern = Struct(
        "ApplicationErrorCode" / Int32ul,
        "Win32LastError" / Int32ul
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=1040, version=0)
class Microsoft_Windows_Help_1040_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Url" / WString,
        "SrcText" / WString,
        "Reason" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=1041, version=0)
class Microsoft_Windows_Help_1041_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "SrcText" / WString,
        "Description" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=2000, version=0)
class Microsoft_Windows_Help_2000_0(Etw):
    pattern = Struct(
        "policy" / WString
    )


@declare(guid=guid("de513a55-c345-438b-9a74-e18cac5c5cc5"), event_id=2005, version=0)
class Microsoft_Windows_Help_2005_0(Etw):
    pattern = Struct(
        "ApplicationErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )

