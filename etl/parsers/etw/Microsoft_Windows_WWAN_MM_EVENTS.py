# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WWAN-MM-EVENTS
GUID : 7839bb2a-2ea3-4eca-a00f-b558ba678bec
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7839bb2a-2ea3-4eca-a00f-b558ba678bec"), event_id=1004, version=0)
class Microsoft_Windows_WWAN_MM_EVENTS_1004_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )

