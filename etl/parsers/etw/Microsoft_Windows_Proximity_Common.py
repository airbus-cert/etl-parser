# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Proximity-Common
GUID : 28058203-d394-4afc-b2a6-2f9155a3bb95
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("28058203-d394-4afc-b2a6-2f9155a3bb95"), event_id=5, version=0)
class Microsoft_Windows_Proximity_Common_5_0(Etw):
    pattern = Struct(
        "Pointer1" / Int64ul
    )


@declare(guid=guid("28058203-d394-4afc-b2a6-2f9155a3bb95"), event_id=10, version=0)
class Microsoft_Windows_Proximity_Common_10_0(Etw):
    pattern = Struct(
        "Pointer1" / Int64ul
    )


@declare(guid=guid("28058203-d394-4afc-b2a6-2f9155a3bb95"), event_id=11, version=0)
class Microsoft_Windows_Proximity_Common_11_0(Etw):
    pattern = Struct(
        "Pointer1" / Int64ul,
        "String2" / WString,
        "String3" / WString
    )


@declare(guid=guid("28058203-d394-4afc-b2a6-2f9155a3bb95"), event_id=12, version=0)
class Microsoft_Windows_Proximity_Common_12_0(Etw):
    pattern = Struct(
        "Pointer1" / Int64ul,
        "String2" / WString,
        "String3" / WString
    )


@declare(guid=guid("28058203-d394-4afc-b2a6-2f9155a3bb95"), event_id=13, version=0)
class Microsoft_Windows_Proximity_Common_13_0(Etw):
    pattern = Struct(
        "Pointer1" / Int64ul,
        "String2" / WString,
        "String3" / WString
    )


@declare(guid=guid("28058203-d394-4afc-b2a6-2f9155a3bb95"), event_id=14, version=0)
class Microsoft_Windows_Proximity_Common_14_0(Etw):
    pattern = Struct(
        "HrResult" / Int32ul,
        "DeviceCategory" / WString
    )


@declare(guid=guid("28058203-d394-4afc-b2a6-2f9155a3bb95"), event_id=15, version=0)
class Microsoft_Windows_Proximity_Common_15_0(Etw):
    pattern = Struct(
        "HrResult" / Int32ul,
        "DeviceCategory" / WString
    )


@declare(guid=guid("28058203-d394-4afc-b2a6-2f9155a3bb95"), event_id=16, version=0)
class Microsoft_Windows_Proximity_Common_16_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("28058203-d394-4afc-b2a6-2f9155a3bb95"), event_id=17, version=0)
class Microsoft_Windows_Proximity_Common_17_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("28058203-d394-4afc-b2a6-2f9155a3bb95"), event_id=18, version=0)
class Microsoft_Windows_Proximity_Common_18_0(Etw):
    pattern = Struct(
        "Pointer1" / Int64ul
    )


@declare(guid=guid("28058203-d394-4afc-b2a6-2f9155a3bb95"), event_id=19, version=0)
class Microsoft_Windows_Proximity_Common_19_0(Etw):
    pattern = Struct(
        "Pointer1" / Int64ul
    )


@declare(guid=guid("28058203-d394-4afc-b2a6-2f9155a3bb95"), event_id=20, version=0)
class Microsoft_Windows_Proximity_Common_20_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("28058203-d394-4afc-b2a6-2f9155a3bb95"), event_id=21, version=0)
class Microsoft_Windows_Proximity_Common_21_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("28058203-d394-4afc-b2a6-2f9155a3bb95"), event_id=22, version=0)
class Microsoft_Windows_Proximity_Common_22_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("28058203-d394-4afc-b2a6-2f9155a3bb95"), event_id=23, version=0)
class Microsoft_Windows_Proximity_Common_23_0(Etw):
    pattern = Struct(
        "Integer4" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("28058203-d394-4afc-b2a6-2f9155a3bb95"), event_id=24, version=0)
class Microsoft_Windows_Proximity_Common_24_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "String2" / WString
    )


@declare(guid=guid("28058203-d394-4afc-b2a6-2f9155a3bb95"), event_id=30, version=0)
class Microsoft_Windows_Proximity_Common_30_0(Etw):
    pattern = Struct(
        "Pointer1" / Int64ul
    )


@declare(guid=guid("28058203-d394-4afc-b2a6-2f9155a3bb95"), event_id=31, version=0)
class Microsoft_Windows_Proximity_Common_31_0(Etw):
    pattern = Struct(
        "Pointer1" / Int64ul
    )


@declare(guid=guid("28058203-d394-4afc-b2a6-2f9155a3bb95"), event_id=41, version=0)
class Microsoft_Windows_Proximity_Common_41_0(Etw):
    pattern = Struct(
        "TransportType" / Int32ul,
        "HrConnectResult" / Int32ul
    )

