# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ResetEng-Trace
GUID : 7fa514b5-a023-4b62-a6ab-2946a483e065
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7fa514b5-a023-4b62-a6ab-2946a483e065"), event_id=10, version=0)
class Microsoft_Windows_ResetEng_Trace_10_0(Etw):
    pattern = Struct(
        "OnlineUi" / Int8ul,
        "PageId" / Int32ul
    )

