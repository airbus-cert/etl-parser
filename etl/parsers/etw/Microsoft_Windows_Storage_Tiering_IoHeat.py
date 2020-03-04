# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Storage-Tiering-IoHeat
GUID : 990c55fc-2662-47f6-b7d7-eb3c027cb13f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("990c55fc-2662-47f6-b7d7-eb3c027cb13f"), event_id=1, version=0)
class Microsoft_Windows_Storage_Tiering_IoHeat_1_0(Etw):
    pattern = Struct(
        "VolumeGuid" / Guid,
        "VolumeIdHash" / Int32ul
    )


@declare(guid=guid("990c55fc-2662-47f6-b7d7-eb3c027cb13f"), event_id=2, version=0)
class Microsoft_Windows_Storage_Tiering_IoHeat_2_0(Etw):
    pattern = Struct(
        "FileIDLower" / Int64ul,
        "FileIDUpper" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul,
        "VolumeIdHash" / Int32ul
    )


@declare(guid=guid("990c55fc-2662-47f6-b7d7-eb3c027cb13f"), event_id=3, version=0)
class Microsoft_Windows_Storage_Tiering_IoHeat_3_0(Etw):
    pattern = Struct(
        "FileIDLower" / Int64ul,
        "FileIDUpper" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul,
        "VolumeIdHash" / Int32ul
    )


@declare(guid=guid("990c55fc-2662-47f6-b7d7-eb3c027cb13f"), event_id=4, version=0)
class Microsoft_Windows_Storage_Tiering_IoHeat_4_0(Etw):
    pattern = Struct(
        "FileIDLower" / Int64ul,
        "FileIDUpper" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul,
        "VolumeIdHash" / Int32ul
    )


@declare(guid=guid("990c55fc-2662-47f6-b7d7-eb3c027cb13f"), event_id=5, version=0)
class Microsoft_Windows_Storage_Tiering_IoHeat_5_0(Etw):
    pattern = Struct(
        "FileIDLower" / Int64ul,
        "FileIDUpper" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul,
        "Source" / Int32ul,
        "Destination" / Int32ul,
        "VolumeIdHash" / Int32ul
    )

