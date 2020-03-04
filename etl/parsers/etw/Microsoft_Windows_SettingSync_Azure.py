# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SettingSync-Azure
GUID : 9f973c1d-d056-4e38-84a5-7be81cdd6ab6
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=5001, version=0)
class Microsoft_Windows_SettingSync_Azure_5001_0(Etw):
    pattern = Struct(
        "ApiName" / WString,
        "CollectionId" / WString,
        "ProviderOp" / Int32ul,
        "Duration" / Int64ul,
        "HRESULT" / Int32ul,
        "CorrelationId" / Guid
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=5002, version=0)
class Microsoft_Windows_SettingSync_Azure_5002_0(Etw):
    pattern = Struct(
        "WebTokenRequestStatus" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=5003, version=0)
class Microsoft_Windows_SettingSync_Azure_5003_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=5004, version=0)
class Microsoft_Windows_SettingSync_Azure_5004_0(Etw):
    pattern = Struct(
        "UInt32" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=5005, version=0)
class Microsoft_Windows_SettingSync_Azure_5005_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=5006, version=0)
class Microsoft_Windows_SettingSync_Azure_5006_0(Etw):
    pattern = Struct(
        "Filename" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=5007, version=0)
class Microsoft_Windows_SettingSync_Azure_5007_0(Etw):
    pattern = Struct(
        "UnitId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=5008, version=0)
class Microsoft_Windows_SettingSync_Azure_5008_0(Etw):
    pattern = Struct(
        "UnitId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=5009, version=0)
class Microsoft_Windows_SettingSync_Azure_5009_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=5010, version=0)
class Microsoft_Windows_SettingSync_Azure_5010_0(Etw):
    pattern = Struct(
        "String" / WString,
        "UInt32" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=5011, version=0)
class Microsoft_Windows_SettingSync_Azure_5011_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=5012, version=0)
class Microsoft_Windows_SettingSync_Azure_5012_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=5013, version=0)
class Microsoft_Windows_SettingSync_Azure_5013_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=5014, version=0)
class Microsoft_Windows_SettingSync_Azure_5014_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=6001, version=0)
class Microsoft_Windows_SettingSync_Azure_6001_0(Etw):
    pattern = Struct(
        "ApiName" / WString,
        "CollectionId" / WString,
        "ProviderOp" / Int32ul,
        "Duration" / Int64ul,
        "HRESULT" / Int32ul,
        "CorrelationId" / Guid
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=6003, version=0)
class Microsoft_Windows_SettingSync_Azure_6003_0(Etw):
    pattern = Struct(
        "Name0Data0" / Int32ul,
        "Name0Data1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=6004, version=0)
class Microsoft_Windows_SettingSync_Azure_6004_0(Etw):
    pattern = Struct(
        "Name0Data0" / Int32ul,
        "Name0Data1" / Int32ul,
        "Name1Data0" / Int32ul,
        "Name1Data1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=6005, version=0)
class Microsoft_Windows_SettingSync_Azure_6005_0(Etw):
    pattern = Struct(
        "UInt32" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=6006, version=0)
class Microsoft_Windows_SettingSync_Azure_6006_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=6008, version=0)
class Microsoft_Windows_SettingSync_Azure_6008_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=6009, version=0)
class Microsoft_Windows_SettingSync_Azure_6009_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=6010, version=0)
class Microsoft_Windows_SettingSync_Azure_6010_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=6011, version=0)
class Microsoft_Windows_SettingSync_Azure_6011_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=6012, version=0)
class Microsoft_Windows_SettingSync_Azure_6012_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=6013, version=0)
class Microsoft_Windows_SettingSync_Azure_6013_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=6014, version=0)
class Microsoft_Windows_SettingSync_Azure_6014_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("9f973c1d-d056-4e38-84a5-7be81cdd6ab6"), event_id=6015, version=0)
class Microsoft_Windows_SettingSync_Azure_6015_0(Etw):
    pattern = Struct(
        "Message" / WString
    )

