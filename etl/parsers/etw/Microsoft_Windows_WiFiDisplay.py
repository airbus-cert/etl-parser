# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WiFiDisplay
GUID : 712880e9-7813-41a3-8e4c-e4e0c4f6580a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("712880e9-7813-41a3-8e4c-e4e0c4f6580a"), event_id=1, version=0)
class Microsoft_Windows_WiFiDisplay_1_0(Etw):
    pattern = Struct(
        "AssociationKey" / Int32ul,
        "LocalDeviceInformation" / WString,
        "RemoteDeviceInformation" / WString
    )


@declare(guid=guid("712880e9-7813-41a3-8e4c-e4e0c4f6580a"), event_id=2, version=0)
class Microsoft_Windows_WiFiDisplay_2_0(Etw):
    pattern = Struct(
        "AssociationKey" / Int32ul,
        "ErrorCode" / Int32ul,
        "LocalDeviceInformation" / WString,
        "RemoteDeviceInformation" / WString
    )


@declare(guid=guid("712880e9-7813-41a3-8e4c-e4e0c4f6580a"), event_id=3, version=0)
class Microsoft_Windows_WiFiDisplay_3_0(Etw):
    pattern = Struct(
        "AssociationKey" / Int32ul,
        "LocalDeviceInformation" / WString,
        "RemoteDeviceInformation" / WString
    )


@declare(guid=guid("712880e9-7813-41a3-8e4c-e4e0c4f6580a"), event_id=4, version=0)
class Microsoft_Windows_WiFiDisplay_4_0(Etw):
    pattern = Struct(
        "AssociationKey" / Int32ul,
        "ErrorCode" / Int32ul,
        "LocalDeviceInformation" / WString,
        "RemoteDeviceInformation" / WString
    )


@declare(guid=guid("712880e9-7813-41a3-8e4c-e4e0c4f6580a"), event_id=5, version=0)
class Microsoft_Windows_WiFiDisplay_5_0(Etw):
    pattern = Struct(
        "LocalDeviceInformation" / WString,
        "RemoteDeviceInformation" / WString
    )


@declare(guid=guid("712880e9-7813-41a3-8e4c-e4e0c4f6580a"), event_id=6, version=0)
class Microsoft_Windows_WiFiDisplay_6_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "LocalDeviceInformation" / WString,
        "RemoteDeviceInformation" / WString
    )


@declare(guid=guid("712880e9-7813-41a3-8e4c-e4e0c4f6580a"), event_id=7, version=0)
class Microsoft_Windows_WiFiDisplay_7_0(Etw):
    pattern = Struct(
        "LocalDeviceInformation" / WString,
        "RemoteDeviceInformation" / WString
    )


@declare(guid=guid("712880e9-7813-41a3-8e4c-e4e0c4f6580a"), event_id=8, version=0)
class Microsoft_Windows_WiFiDisplay_8_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "LocalDeviceInformation" / WString,
        "RemoteDeviceInformation" / WString
    )


@declare(guid=guid("712880e9-7813-41a3-8e4c-e4e0c4f6580a"), event_id=9, version=0)
class Microsoft_Windows_WiFiDisplay_9_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "LocalDeviceInformation" / WString,
        "RemoteDeviceInformation" / WString
    )


@declare(guid=guid("712880e9-7813-41a3-8e4c-e4e0c4f6580a"), event_id=10, version=0)
class Microsoft_Windows_WiFiDisplay_10_0(Etw):
    pattern = Struct(
        "DiscoveryTime" / Int32ul,
        "LocalDeviceInformation" / WString,
        "RemoteDeviceInformation" / WString
    )

