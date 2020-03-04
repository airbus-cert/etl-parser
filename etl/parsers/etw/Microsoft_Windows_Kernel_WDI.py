# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-WDI
GUID : 2ff3e6b7-cb90-4700-9621-443f389734ed
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("2ff3e6b7-cb90-4700-9621-443f389734ed"), event_id=32, version=0)
class Microsoft_Windows_Kernel_WDI_32_0(Etw):
    pattern = Struct(
        "ProviderID" / Guid,
        "EventID" / Int16ul,
        "DroppedEventCount" / Int32ul,
        "ActionCount" / Int8ul,
        "SemActions" / Int16sl
    )


@declare(guid=guid("2ff3e6b7-cb90-4700-9621-443f389734ed"), event_id=33, version=0)
class Microsoft_Windows_Kernel_WDI_33_0(Etw):
    pattern = Struct(
        "ProviderID" / Guid,
        "EventID" / Int16ul,
        "DroppedEventCount" / Int32ul,
        "ActionCount" / Int8ul,
        "SemActions" / Int16sl
    )


@declare(guid=guid("2ff3e6b7-cb90-4700-9621-443f389734ed"), event_id=34, version=0)
class Microsoft_Windows_Kernel_WDI_34_0(Etw):
    pattern = Struct(
        "ProviderID" / Guid,
        "EventID" / Int16ul
    )


@declare(guid=guid("2ff3e6b7-cb90-4700-9621-443f389734ed"), event_id=35, version=0)
class Microsoft_Windows_Kernel_WDI_35_0(Etw):
    pattern = Struct(
        "ProviderID" / Guid,
        "EventID" / Int16ul,
        "ScenarioCount" / Int8ul,
        "ScenarioInflightItems" / Int8ul
    )


@declare(guid=guid("2ff3e6b7-cb90-4700-9621-443f389734ed"), event_id=36, version=0)
class Microsoft_Windows_Kernel_WDI_36_0(Etw):
    pattern = Struct(
        "ProviderID" / Guid,
        "EventID" / Int16ul,
        "NTStatus" / Int32ul
    )


@declare(guid=guid("2ff3e6b7-cb90-4700-9621-443f389734ed"), event_id=37, version=0)
class Microsoft_Windows_Kernel_WDI_37_0(Etw):
    pattern = Struct(
        "ProviderID" / Guid,
        "EventID" / Int16ul,
        "NTStatus" / Int32ul
    )


@declare(guid=guid("2ff3e6b7-cb90-4700-9621-443f389734ed"), event_id=38, version=0)
class Microsoft_Windows_Kernel_WDI_38_0(Etw):
    pattern = Struct(
        "ProviderID" / Guid,
        "EventID" / Int16ul
    )


@declare(guid=guid("2ff3e6b7-cb90-4700-9621-443f389734ed"), event_id=39, version=0)
class Microsoft_Windows_Kernel_WDI_39_0(Etw):
    pattern = Struct(
        "ProviderID" / Guid,
        "EventID" / Int16ul
    )


@declare(guid=guid("2ff3e6b7-cb90-4700-9621-443f389734ed"), event_id=40, version=0)
class Microsoft_Windows_Kernel_WDI_40_0(Etw):
    pattern = Struct(
        "ProviderID" / Guid,
        "EventID" / Int16ul
    )


@declare(guid=guid("2ff3e6b7-cb90-4700-9621-443f389734ed"), event_id=41, version=0)
class Microsoft_Windows_Kernel_WDI_41_0(Etw):
    pattern = Struct(
        "ProviderID" / Guid
    )


@declare(guid=guid("2ff3e6b7-cb90-4700-9621-443f389734ed"), event_id=42, version=0)
class Microsoft_Windows_Kernel_WDI_42_0(Etw):
    pattern = Struct(
        "ProviderID" / Guid,
        "EventID" / Int16ul,
        "NTStatus" / Int32ul
    )


@declare(guid=guid("2ff3e6b7-cb90-4700-9621-443f389734ed"), event_id=43, version=0)
class Microsoft_Windows_Kernel_WDI_43_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSid" / Sid
    )


@declare(guid=guid("2ff3e6b7-cb90-4700-9621-443f389734ed"), event_id=44, version=0)
class Microsoft_Windows_Kernel_WDI_44_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("2ff3e6b7-cb90-4700-9621-443f389734ed"), event_id=45, version=0)
class Microsoft_Windows_Kernel_WDI_45_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )

