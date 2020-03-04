# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DeviceUpdateAgent
GUID : e8f9af91-afbe-5a03-dfec-5d591686326c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=100, version=0)
class Microsoft_Windows_DeviceUpdateAgent_100_0(Etw):
    pattern = Struct(
        "Prop_SessionId" / WString
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=100, version=1)
class Microsoft_Windows_DeviceUpdateAgent_100_1(Etw):
    pattern = Struct(
        "Prop_SessionId" / WString,
        "Prop_UpdateId" / WString,
        "Prop_FlightId" / WString
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=101, version=0)
class Microsoft_Windows_DeviceUpdateAgent_101_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=101, version=1)
class Microsoft_Windows_DeviceUpdateAgent_101_1(Etw):
    pattern = Struct(
        "Prop_UpdateId" / WString,
        "Prop_FlightId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=200, version=0)
class Microsoft_Windows_DeviceUpdateAgent_200_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=200, version=1)
class Microsoft_Windows_DeviceUpdateAgent_200_1(Etw):
    pattern = Struct(
        "Prop_ProductId" / WString,
        "Prop_ProductVersion" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=201, version=0)
class Microsoft_Windows_DeviceUpdateAgent_201_0(Etw):
    pattern = Struct(
        "Prop_NumFiles" / Int32ul,
        "Prop_RequestSize" / Int64ul
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=300, version=0)
class Microsoft_Windows_DeviceUpdateAgent_300_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=300, version=1)
class Microsoft_Windows_DeviceUpdateAgent_300_1(Etw):
    pattern = Struct(
        "Prop_ProductId" / WString,
        "Prop_ProductVersion" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=301, version=0)
class Microsoft_Windows_DeviceUpdateAgent_301_0(Etw):
    pattern = Struct(
        "Win32Error" / Int32ul,
        "Prop_UnicodeString" / WString
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=302, version=0)
class Microsoft_Windows_DeviceUpdateAgent_302_0(Etw):
    pattern = Struct(
        "Win32Error" / Int32ul,
        "Prop_UnicodeString" / WString
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=303, version=0)
class Microsoft_Windows_DeviceUpdateAgent_303_0(Etw):
    pattern = Struct(
        "Win32Error" / Int32ul,
        "Prop_UnicodeString" / WString
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=304, version=0)
class Microsoft_Windows_DeviceUpdateAgent_304_0(Etw):
    pattern = Struct(
        "Prop_Id" / WString
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=305, version=0)
class Microsoft_Windows_DeviceUpdateAgent_305_0(Etw):
    pattern = Struct(
        "Prop_Id" / WString
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=306, version=0)
class Microsoft_Windows_DeviceUpdateAgent_306_0(Etw):
    pattern = Struct(
        "Prop_SetId" / WString,
        "Prop_SuccessfulUpdates" / Int32ul,
        "Prop_TotalUpdates" / Int32ul,
        "Prop_ElapsedMilliseconds" / Int64ul
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=307, version=0)
class Microsoft_Windows_DeviceUpdateAgent_307_0(Etw):
    pattern = Struct(
        "Prop_ProductId" / WString,
        "Prop_ProductVersion" / WString
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=400, version=0)
class Microsoft_Windows_DeviceUpdateAgent_400_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=500, version=0)
class Microsoft_Windows_DeviceUpdateAgent_500_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=600, version=0)
class Microsoft_Windows_DeviceUpdateAgent_600_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=601, version=0)
class Microsoft_Windows_DeviceUpdateAgent_601_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=700, version=0)
class Microsoft_Windows_DeviceUpdateAgent_700_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=800, version=0)
class Microsoft_Windows_DeviceUpdateAgent_800_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=801, version=0)
class Microsoft_Windows_DeviceUpdateAgent_801_0(Etw):
    pattern = Struct(
        "Prop_ProductId" / WString,
        "Prop_ProductVersion" / WString
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=802, version=0)
class Microsoft_Windows_DeviceUpdateAgent_802_0(Etw):
    pattern = Struct(
        "Prop_ProductId" / WString,
        "Prop_ProductVersion" / WString,
        "Prop_MissingUpdates" / Int32ul,
        "Prop_MissingDrivers" / Int32ul,
        "Prop_UnpublishedDrivers" / Int32ul,
        "Prop_PublishedDrivers" / Int32ul,
        "Prop_AnalysisErrorDrivers" / Int32ul
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=900, version=0)
class Microsoft_Windows_DeviceUpdateAgent_900_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("e8f9af91-afbe-5a03-dfec-5d591686326c"), event_id=1000, version=0)
class Microsoft_Windows_DeviceUpdateAgent_1000_0(Etw):
    pattern = Struct(
        "Prop_ProductId" / WString,
        "Prop_Version1" / WString,
        "Prop_Version2" / WString
    )

