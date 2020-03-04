# -*- coding: utf-8 -*-
"""
Microsoft-Windows-HotspotAuth
GUID : de095dbe-8667-4168-94c2-48ca61665aca
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("de095dbe-8667-4168-94c2-48ca61665aca"), event_id=1001, version=0)
class Microsoft_Windows_HotspotAuth_1001_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("de095dbe-8667-4168-94c2-48ca61665aca"), event_id=1002, version=0)
class Microsoft_Windows_HotspotAuth_1002_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("de095dbe-8667-4168-94c2-48ca61665aca"), event_id=1003, version=0)
class Microsoft_Windows_HotspotAuth_1003_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "Result" / Int32sl,
        "ResponseCode" / Int32ul
    )


@declare(guid=guid("de095dbe-8667-4168-94c2-48ca61665aca"), event_id=1004, version=0)
class Microsoft_Windows_HotspotAuth_1004_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("de095dbe-8667-4168-94c2-48ca61665aca"), event_id=1005, version=0)
class Microsoft_Windows_HotspotAuth_1005_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "AuthenticationScenarioType" / Int32ul,
        "Result" / Int32sl,
        "ResponseCode" / Int32ul
    )


@declare(guid=guid("de095dbe-8667-4168-94c2-48ca61665aca"), event_id=1006, version=0)
class Microsoft_Windows_HotspotAuth_1006_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("de095dbe-8667-4168-94c2-48ca61665aca"), event_id=2001, version=0)
class Microsoft_Windows_HotspotAuth_2001_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("de095dbe-8667-4168-94c2-48ca61665aca"), event_id=2002, version=0)
class Microsoft_Windows_HotspotAuth_2002_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("de095dbe-8667-4168-94c2-48ca61665aca"), event_id=2003, version=0)
class Microsoft_Windows_HotspotAuth_2003_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "Result" / Int32sl
    )


@declare(guid=guid("de095dbe-8667-4168-94c2-48ca61665aca"), event_id=2004, version=0)
class Microsoft_Windows_HotspotAuth_2004_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "WisprScenarioType" / Int32ul,
        "Result" / Int32sl
    )


@declare(guid=guid("de095dbe-8667-4168-94c2-48ca61665aca"), event_id=2005, version=0)
class Microsoft_Windows_HotspotAuth_2005_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("de095dbe-8667-4168-94c2-48ca61665aca"), event_id=2006, version=0)
class Microsoft_Windows_HotspotAuth_2006_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("de095dbe-8667-4168-94c2-48ca61665aca"), event_id=2007, version=0)
class Microsoft_Windows_HotspotAuth_2007_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("de095dbe-8667-4168-94c2-48ca61665aca"), event_id=3001, version=0)
class Microsoft_Windows_HotspotAuth_3001_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("de095dbe-8667-4168-94c2-48ca61665aca"), event_id=3002, version=0)
class Microsoft_Windows_HotspotAuth_3002_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )

