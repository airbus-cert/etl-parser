# -*- coding: utf-8 -*-
"""
Microsoft-Windows-IME-TCTIP
GUID : d5268c02-6f51-436f-983b-74f2efbfaf3a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d5268c02-6f51-436f-983b-74f2efbfaf3a"), event_id=30, version=0)
class Microsoft_Windows_IME_TCTIP_30_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul,
        "IMEType" / Int32ul
    )

