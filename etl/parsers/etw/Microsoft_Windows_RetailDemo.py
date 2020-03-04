# -*- coding: utf-8 -*-
"""
Microsoft-Windows-RetailDemo
GUID : d3f29eda-805d-428a-9902-b259b937f84b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d3f29eda-805d-428a-9902-b259b937f84b"), event_id=200, version=0)
class Microsoft_Windows_RetailDemo_200_0(Etw):
    pattern = Struct(
        "ErrorState" / CString,
        "ErrorPhase" / CString,
        "HRESULT" / Int32ul
    )

