# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TZUtil
GUID : 2d318b91-e6e7-4c46-bd04-bfe6db412cf9
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("2d318b91-e6e7-4c46-bd04-bfe6db412cf9"), event_id=1004, version=0)
class Microsoft_Windows_TZUtil_1004_0(Etw):
    pattern = Struct(
        "TimeZone" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("2d318b91-e6e7-4c46-bd04-bfe6db412cf9"), event_id=1005, version=0)
class Microsoft_Windows_TZUtil_1005_0(Etw):
    pattern = Struct(
        "TimeZone" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("2d318b91-e6e7-4c46-bd04-bfe6db412cf9"), event_id=1006, version=0)
class Microsoft_Windows_TZUtil_1006_0(Etw):
    pattern = Struct(
        "TimeZone" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("2d318b91-e6e7-4c46-bd04-bfe6db412cf9"), event_id=1007, version=0)
class Microsoft_Windows_TZUtil_1007_0(Etw):
    pattern = Struct(
        "TimeZone" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("2d318b91-e6e7-4c46-bd04-bfe6db412cf9"), event_id=20001, version=0)
class Microsoft_Windows_TZUtil_20001_0(Etw):
    pattern = Struct(
        "TimeZone" / WString
    )

