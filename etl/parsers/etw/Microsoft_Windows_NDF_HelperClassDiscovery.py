# -*- coding: utf-8 -*-
"""
Microsoft-Windows-NDF-HelperClassDiscovery
GUID : fc3bc8a7-2f61-449c-a8b4-22ac22058f92
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("fc3bc8a7-2f61-449c-a8b4-22ac22058f92"), event_id=1001, version=0)
class Microsoft_Windows_NDF_HelperClassDiscovery_1001_0(Etw):
    pattern = Struct(
        "HelperClassName" / WString,
        "ComponentName" / WString
    )


@declare(guid=guid("fc3bc8a7-2f61-449c-a8b4-22ac22058f92"), event_id=1002, version=0)
class Microsoft_Windows_NDF_HelperClassDiscovery_1002_0(Etw):
    pattern = Struct(
        "HelperClassName" / WString,
        "ComponentName" / WString
    )


@declare(guid=guid("fc3bc8a7-2f61-449c-a8b4-22ac22058f92"), event_id=1003, version=0)
class Microsoft_Windows_NDF_HelperClassDiscovery_1003_0(Etw):
    pattern = Struct(
        "HelperClassName" / WString
    )


@declare(guid=guid("fc3bc8a7-2f61-449c-a8b4-22ac22058f92"), event_id=1004, version=0)
class Microsoft_Windows_NDF_HelperClassDiscovery_1004_0(Etw):
    pattern = Struct(
        "HelperClassName" / WString
    )


@declare(guid=guid("fc3bc8a7-2f61-449c-a8b4-22ac22058f92"), event_id=1005, version=0)
class Microsoft_Windows_NDF_HelperClassDiscovery_1005_0(Etw):
    pattern = Struct(
        "HelperClassName" / WString
    )


@declare(guid=guid("fc3bc8a7-2f61-449c-a8b4-22ac22058f92"), event_id=1006, version=0)
class Microsoft_Windows_NDF_HelperClassDiscovery_1006_0(Etw):
    pattern = Struct(
        "HelperClassName" / WString
    )


@declare(guid=guid("fc3bc8a7-2f61-449c-a8b4-22ac22058f92"), event_id=1007, version=0)
class Microsoft_Windows_NDF_HelperClassDiscovery_1007_0(Etw):
    pattern = Struct(
        "HelperClassName" / WString
    )


@declare(guid=guid("fc3bc8a7-2f61-449c-a8b4-22ac22058f92"), event_id=1008, version=0)
class Microsoft_Windows_NDF_HelperClassDiscovery_1008_0(Etw):
    pattern = Struct(
        "HelperClassName" / WString,
        "ComponentName" / WString
    )


@declare(guid=guid("fc3bc8a7-2f61-449c-a8b4-22ac22058f92"), event_id=1009, version=0)
class Microsoft_Windows_NDF_HelperClassDiscovery_1009_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Name" / WString
    )


@declare(guid=guid("fc3bc8a7-2f61-449c-a8b4-22ac22058f92"), event_id=1010, version=0)
class Microsoft_Windows_NDF_HelperClassDiscovery_1010_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Name" / WString
    )


@declare(guid=guid("fc3bc8a7-2f61-449c-a8b4-22ac22058f92"), event_id=1011, version=0)
class Microsoft_Windows_NDF_HelperClassDiscovery_1011_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Name" / WString
    )


@declare(guid=guid("fc3bc8a7-2f61-449c-a8b4-22ac22058f92"), event_id=1012, version=0)
class Microsoft_Windows_NDF_HelperClassDiscovery_1012_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Name" / WString
    )


@declare(guid=guid("fc3bc8a7-2f61-449c-a8b4-22ac22058f92"), event_id=1100, version=0)
class Microsoft_Windows_NDF_HelperClassDiscovery_1100_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Name" / WString,
        "KeyOrValue" / WString
    )


@declare(guid=guid("fc3bc8a7-2f61-449c-a8b4-22ac22058f92"), event_id=1101, version=0)
class Microsoft_Windows_NDF_HelperClassDiscovery_1101_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Name" / WString,
        "KeyOrValue" / WString
    )

