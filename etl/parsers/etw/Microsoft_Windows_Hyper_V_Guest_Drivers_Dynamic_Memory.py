# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Hyper-V-Guest-Drivers-Dynamic-Memory
GUID : ba2ffb5c-e20a-4fb9-91b4-45f61b4b66a0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ba2ffb5c-e20a-4fb9-91b4-45f61b4b66a0"), event_id=6, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_Dynamic_Memory_6_0(Etw):
    pattern = Struct(
        "OperationMessage" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("ba2ffb5c-e20a-4fb9-91b4-45f61b4b66a0"), event_id=7, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_Dynamic_Memory_7_0(Etw):
    pattern = Struct(
        "OperationMessage" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("ba2ffb5c-e20a-4fb9-91b4-45f61b4b66a0"), event_id=8, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_Dynamic_Memory_8_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("ba2ffb5c-e20a-4fb9-91b4-45f61b4b66a0"), event_id=100, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_Dynamic_Memory_100_0(Etw):
    pattern = Struct(
        "OperationMessage" / WString,
        "PageCount" / Int32ul
    )


@declare(guid=guid("ba2ffb5c-e20a-4fb9-91b4-45f61b4b66a0"), event_id=101, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_Dynamic_Memory_101_0(Etw):
    pattern = Struct(
        "HighestHotAddPage" / Int64ul,
        "MinPageCount" / Int64ul,
        "IsHighestPageDetermined" / Int8ul,
        "SupportsHotAdd" / Int8ul,
        "SupportsHotRemove" / Int8ul,
        "SupportsContiguousAllocations" / Int8ul,
        "SupportsFastContiguousAllocations" / Int8ul
    )


@declare(guid=guid("ba2ffb5c-e20a-4fb9-91b4-45f61b4b66a0"), event_id=102, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_Dynamic_Memory_102_0(Etw):
    pattern = Struct(
        "MajorVersion" / Int32ul,
        "MinorVersion" / Int32ul
    )

