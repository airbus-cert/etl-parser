# -*- coding: utf-8 -*-
"""
Microsoft-Windows-IME-KRTIP
GUID : e013e74b-97f4-4e1c-a120-596e5629ecfe
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e013e74b-97f4-4e1c-a120-596e5629ecfe"), event_id=10, version=0)
class Microsoft_Windows_IME_KRTIP_10_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul,
        "IMEType" / Int32ul
    )

