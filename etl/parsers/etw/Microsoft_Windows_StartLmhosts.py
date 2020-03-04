# -*- coding: utf-8 -*-
"""
Microsoft-Windows-StartLmhosts
GUID : 2d7904d8-5c90-4209-ba6a-4c08f409934c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("2d7904d8-5c90-4209-ba6a-4c08f409934c"), event_id=1, version=0)
class Microsoft_Windows_StartLmhosts_1_0(Etw):
    pattern = Struct(
        "StartLmHostTrigger" / Guid
    )

