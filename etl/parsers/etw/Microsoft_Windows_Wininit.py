# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Wininit
GUID : 206f6dea-d3c5-4d10-bc72-989f03c8b84b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("206f6dea-d3c5-4d10-bc72-989f03c8b84b"), event_id=9, version=0)
class Microsoft_Windows_Wininit_9_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul
    )


@declare(guid=guid("206f6dea-d3c5-4d10-bc72-989f03c8b84b"), event_id=10, version=0)
class Microsoft_Windows_Wininit_10_0(Etw):
    pattern = Struct(
        "Win32Status" / Int32ul
    )


@declare(guid=guid("206f6dea-d3c5-4d10-bc72-989f03c8b84b"), event_id=11, version=0)
class Microsoft_Windows_Wininit_11_0(Etw):
    pattern = Struct(
        "StringCount" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("206f6dea-d3c5-4d10-bc72-989f03c8b84b"), event_id=12, version=0)
class Microsoft_Windows_Wininit_12_0(Etw):
    pattern = Struct(
        "Level" / Int32ul
    )


@declare(guid=guid("206f6dea-d3c5-4d10-bc72-989f03c8b84b"), event_id=14, version=0)
class Microsoft_Windows_Wininit_14_0(Etw):
    pattern = Struct(
        "Config" / Int32ul,
        "IsTestConfig" / Int32ul
    )


@declare(guid=guid("206f6dea-d3c5-4d10-bc72-989f03c8b84b"), event_id=16, version=0)
class Microsoft_Windows_Wininit_16_0(Etw):
    pattern = Struct(
        "Level" / Int32ul
    )


@declare(guid=guid("206f6dea-d3c5-4d10-bc72-989f03c8b84b"), event_id=17, version=0)
class Microsoft_Windows_Wininit_17_0(Etw):
    pattern = Struct(
        "Level" / Int32ul
    )


@declare(guid=guid("206f6dea-d3c5-4d10-bc72-989f03c8b84b"), event_id=53, version=0)
class Microsoft_Windows_Wininit_53_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("206f6dea-d3c5-4d10-bc72-989f03c8b84b"), event_id=55, version=0)
class Microsoft_Windows_Wininit_55_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "IsRemote" / Int32ul,
        "GracePeriod" / Int32ul,
        "Flags" / Int32ul,
        "Reason" / Int32ul,
        "Message" / WString
    )


@declare(guid=guid("206f6dea-d3c5-4d10-bc72-989f03c8b84b"), event_id=6001, version=0)
class Microsoft_Windows_Wininit_6001_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul
    )


@declare(guid=guid("206f6dea-d3c5-4d10-bc72-989f03c8b84b"), event_id=6002, version=1)
class Microsoft_Windows_Wininit_6002_1(Etw):
    pattern = Struct(
        "ShutdownFlags" / Int32ul,
        "SystemShutdownDuration" / Int64ul,
        "SkuHasLogoff" / Int32ul
    )

