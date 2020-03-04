# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DiskDiagnosticResolver
GUID : 6b1ffe48-5b1e-4793-9f7f-ae926454499d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6b1ffe48-5b1e-4793-9f7f-ae926454499d"), event_id=7, version=0)
class Microsoft_Windows_DiskDiagnosticResolver_7_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )

