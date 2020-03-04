# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Volume
GUID : 9f7b5df4-b902-48bc-bc94-95068c6c7d26
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9f7b5df4-b902-48bc-bc94-95068c6c7d26"), event_id=1001, version=0)
class Microsoft_Windows_Volume_1001_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "DiskNumber" / Int32ul,
        "DiskOffset" / Int64ul,
        "ControlCode" / Int32ul
    )


@declare(guid=guid("9f7b5df4-b902-48bc-bc94-95068c6c7d26"), event_id=1002, version=0)
class Microsoft_Windows_Volume_1002_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "DiskNumber" / Int32ul,
        "DiskOffset" / Int64ul,
        "ControlCode" / Int32ul,
        "Status" / Int32ul
    )

