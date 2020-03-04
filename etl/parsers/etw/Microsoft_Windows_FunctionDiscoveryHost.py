# -*- coding: utf-8 -*-
"""
Microsoft-Windows-FunctionDiscoveryHost
GUID : 538cbbad-4877-4eb2-b26e-7caee8f0f8cb
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("538cbbad-4877-4eb2-b26e-7caee8f0f8cb"), event_id=1000, version=0)
class Microsoft_Windows_FunctionDiscoveryHost_1000_0(Etw):
    pattern = Struct(
        "String" / WString,
        "HRESULT" / Int32ul,
        "Line" / Int32ul,
        "Filename" / CString
    )

