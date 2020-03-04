# -*- coding: utf-8 -*-
"""
Microsoft-Windows-COM
GUID : d4263c98-310c-4d97-ba39-b55354f08584
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d4263c98-310c-4d97-ba39-b55354f08584"), event_id=1, version=0)
class Microsoft_Windows_COM_1_0(Etw):
    pattern = Struct(
        "CLSID" / Guid
    )

