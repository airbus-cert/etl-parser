# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WiFiHotspotService
GUID : 814182fe-58f7-11e1-853c-78e7d1ca7337
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("814182fe-58f7-11e1-853c-78e7d1ca7337"), event_id=1003, version=0)
class Microsoft_Windows_WiFiHotspotService_1003_0(Etw):
    pattern = Struct(
        "uString" / WString,
        "Dword" / Int32ul
    )


@declare(guid=guid("814182fe-58f7-11e1-853c-78e7d1ca7337"), event_id=1004, version=0)
class Microsoft_Windows_WiFiHotspotService_1004_0(Etw):
    pattern = Struct(
        "uString" / WString,
        "Dword" / Int32ul
    )


@declare(guid=guid("814182fe-58f7-11e1-853c-78e7d1ca7337"), event_id=1005, version=0)
class Microsoft_Windows_WiFiHotspotService_1005_0(Etw):
    pattern = Struct(
        "Ptr1" / Int64ul,
        "Ptr2" / Int64ul
    )


@declare(guid=guid("814182fe-58f7-11e1-853c-78e7d1ca7337"), event_id=1006, version=0)
class Microsoft_Windows_WiFiHotspotService_1006_0(Etw):
    pattern = Struct(
        "uString" / WString,
        "Dword" / Int32ul
    )


@declare(guid=guid("814182fe-58f7-11e1-853c-78e7d1ca7337"), event_id=1007, version=0)
class Microsoft_Windows_WiFiHotspotService_1007_0(Etw):
    pattern = Struct(
        "uString" / WString,
        "Dword" / Int32ul
    )


@declare(guid=guid("814182fe-58f7-11e1-853c-78e7d1ca7337"), event_id=1008, version=0)
class Microsoft_Windows_WiFiHotspotService_1008_0(Etw):
    pattern = Struct(
        "uString" / WString,
        "Dword" / Int32ul
    )


@declare(guid=guid("814182fe-58f7-11e1-853c-78e7d1ca7337"), event_id=1009, version=0)
class Microsoft_Windows_WiFiHotspotService_1009_0(Etw):
    pattern = Struct(
        "uString" / WString,
        "Dword" / Int32ul
    )


@declare(guid=guid("814182fe-58f7-11e1-853c-78e7d1ca7337"), event_id=1010, version=0)
class Microsoft_Windows_WiFiHotspotService_1010_0(Etw):
    pattern = Struct(
        "uString" / WString,
        "Dword" / Int32ul
    )


@declare(guid=guid("814182fe-58f7-11e1-853c-78e7d1ca7337"), event_id=1011, version=0)
class Microsoft_Windows_WiFiHotspotService_1011_0(Etw):
    pattern = Struct(
        "uString" / WString,
        "Dword" / Int32ul
    )


@declare(guid=guid("814182fe-58f7-11e1-853c-78e7d1ca7337"), event_id=1012, version=0)
class Microsoft_Windows_WiFiHotspotService_1012_0(Etw):
    pattern = Struct(
        "uString" / WString,
        "Dword" / Int32ul
    )


@declare(guid=guid("814182fe-58f7-11e1-853c-78e7d1ca7337"), event_id=2000, version=0)
class Microsoft_Windows_WiFiHotspotService_2000_0(Etw):
    pattern = Struct(
        "uString1" / WString,
        "uString2" / WString,
        "Dword1" / Int32ul,
        "Dword2" / Int32ul,
        "Dword3" / Int32ul
    )


@declare(guid=guid("814182fe-58f7-11e1-853c-78e7d1ca7337"), event_id=3000, version=0)
class Microsoft_Windows_WiFiHotspotService_3000_0(Etw):
    pattern = Struct(
        "Dword1" / Int32ul,
        "Dword2" / Int32ul
    )


@declare(guid=guid("814182fe-58f7-11e1-853c-78e7d1ca7337"), event_id=3001, version=0)
class Microsoft_Windows_WiFiHotspotService_3001_0(Etw):
    pattern = Struct(
        "Ptr" / Int64ul,
        "Dword" / Int32ul
    )


@declare(guid=guid("814182fe-58f7-11e1-853c-78e7d1ca7337"), event_id=3002, version=0)
class Microsoft_Windows_WiFiHotspotService_3002_0(Etw):
    pattern = Struct(
        "Ptr" / Int64ul
    )


@declare(guid=guid("814182fe-58f7-11e1-853c-78e7d1ca7337"), event_id=3003, version=0)
class Microsoft_Windows_WiFiHotspotService_3003_0(Etw):
    pattern = Struct(
        "uString" / WString,
        "Dword" / Int32ul
    )


@declare(guid=guid("814182fe-58f7-11e1-853c-78e7d1ca7337"), event_id=3004, version=0)
class Microsoft_Windows_WiFiHotspotService_3004_0(Etw):
    pattern = Struct(
        "uString" / WString,
        "Dword" / Int32ul
    )


@declare(guid=guid("814182fe-58f7-11e1-853c-78e7d1ca7337"), event_id=4000, version=0)
class Microsoft_Windows_WiFiHotspotService_4000_0(Etw):
    pattern = Struct(
        "aString" / CString
    )


@declare(guid=guid("814182fe-58f7-11e1-853c-78e7d1ca7337"), event_id=4001, version=0)
class Microsoft_Windows_WiFiHotspotService_4001_0(Etw):
    pattern = Struct(
        "uString" / WString,
        "Dword" / Int32ul
    )


@declare(guid=guid("814182fe-58f7-11e1-853c-78e7d1ca7337"), event_id=4002, version=0)
class Microsoft_Windows_WiFiHotspotService_4002_0(Etw):
    pattern = Struct(
        "uString" / WString,
        "Dword" / Int32ul
    )


@declare(guid=guid("814182fe-58f7-11e1-853c-78e7d1ca7337"), event_id=4003, version=0)
class Microsoft_Windows_WiFiHotspotService_4003_0(Etw):
    pattern = Struct(
        "Dword1" / Int32ul,
        "Dword2" / Int32ul,
        "aString1" / CString,
        "Dword3" / Int32ul,
        "Dword4" / Int32ul,
        "Dword5" / Int32ul,
        "uString1" / WString
    )


@declare(guid=guid("814182fe-58f7-11e1-853c-78e7d1ca7337"), event_id=4004, version=0)
class Microsoft_Windows_WiFiHotspotService_4004_0(Etw):
    pattern = Struct(
        "uString" / WString,
        "Dword" / Int32ul
    )

