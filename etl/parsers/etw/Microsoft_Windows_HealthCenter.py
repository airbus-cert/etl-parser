# -*- coding: utf-8 -*-
"""
Microsoft-Windows-HealthCenter
GUID : 588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=1, version=0)
class Microsoft_Windows_HealthCenter_1_0(Etw):
    pattern = Struct(
        "CLSID" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=2, version=0)
class Microsoft_Windows_HealthCenter_2_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=3, version=0)
class Microsoft_Windows_HealthCenter_3_0(Etw):
    pattern = Struct(
        "CannonicalName" / WString
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=4, version=0)
class Microsoft_Windows_HealthCenter_4_0(Etw):
    pattern = Struct(
        "EventID" / Int32ul,
        "EventVeresion" / Int8ul,
        "ChannelName" / WString
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=5, version=0)
class Microsoft_Windows_HealthCenter_5_0(Etw):
    pattern = Struct(
        "StateID" / Int32ul,
        "CanonicalName" / WString
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=6, version=0)
class Microsoft_Windows_HealthCenter_6_0(Etw):
    pattern = Struct(
        "StateID" / Int32ul,
        "CanonicalName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=7, version=0)
class Microsoft_Windows_HealthCenter_7_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=8, version=0)
class Microsoft_Windows_HealthCenter_8_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=9, version=0)
class Microsoft_Windows_HealthCenter_9_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=10, version=0)
class Microsoft_Windows_HealthCenter_10_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=11, version=0)
class Microsoft_Windows_HealthCenter_11_0(Etw):
    pattern = Struct(
        "CanonicalName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=12, version=0)
class Microsoft_Windows_HealthCenter_12_0(Etw):
    pattern = Struct(
        "CanonicalName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=13, version=0)
class Microsoft_Windows_HealthCenter_13_0(Etw):
    pattern = Struct(
        "ChannelName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=14, version=0)
class Microsoft_Windows_HealthCenter_14_0(Etw):
    pattern = Struct(
        "ChannelName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=15, version=0)
class Microsoft_Windows_HealthCenter_15_0(Etw):
    pattern = Struct(
        "ChannelName" / WString
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=16, version=0)
class Microsoft_Windows_HealthCenter_16_0(Etw):
    pattern = Struct(
        "ChannelName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=17, version=0)
class Microsoft_Windows_HealthCenter_17_0(Etw):
    pattern = Struct(
        "ChannelName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=18, version=0)
class Microsoft_Windows_HealthCenter_18_0(Etw):
    pattern = Struct(
        "InputString" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=19, version=0)
class Microsoft_Windows_HealthCenter_19_0(Etw):
    pattern = Struct(
        "CanonicalName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=20, version=0)
class Microsoft_Windows_HealthCenter_20_0(Etw):
    pattern = Struct(
        "CanonicalName" / WString
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=21, version=0)
class Microsoft_Windows_HealthCenter_21_0(Etw):
    pattern = Struct(
        "CanonicalName" / WString
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=122, version=0)
class Microsoft_Windows_HealthCenter_122_0(Etw):
    pattern = Struct(
        "CLSID" / WString
    )


@declare(guid=guid("588c5c5a-ffc5-44a2-9a7f-d5e8dbe6efd7"), event_id=123, version=0)
class Microsoft_Windows_HealthCenter_123_0(Etw):
    pattern = Struct(
        "CLSID" / WString
    )

