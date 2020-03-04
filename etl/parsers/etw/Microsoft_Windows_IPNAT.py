# -*- coding: utf-8 -*-
"""
Microsoft-Windows-IPNAT
GUID : a67075c2-3e39-4109-b6cd-6d750058a732
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a67075c2-3e39-4109-b6cd-6d750058a732"), event_id=2001, version=0)
class Microsoft_Windows_IPNAT_2001_0(Etw):
    pattern = Struct(
        "_DebugString" / CString
    )

