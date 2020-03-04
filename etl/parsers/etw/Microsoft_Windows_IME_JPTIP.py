# -*- coding: utf-8 -*-
"""
Microsoft-Windows-IME-JPTIP
GUID : 8c8a69ad-cc89-481f-bbad-fd95b5006256
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("8c8a69ad-cc89-481f-bbad-fd95b5006256"), event_id=30, version=0)
class Microsoft_Windows_IME_JPTIP_30_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul,
        "IMEType" / Int32ul
    )

