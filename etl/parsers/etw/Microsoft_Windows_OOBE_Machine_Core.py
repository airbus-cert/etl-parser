# -*- coding: utf-8 -*-
"""
Microsoft-Windows-OOBE-Machine-Core
GUID : ec276cde-2a17-473c-a010-2ff78d5426d2
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ec276cde-2a17-473c-a010-2ff78d5426d2"), event_id=5004, version=0)
class Microsoft_Windows_OOBE_Machine_Core_5004_0(Etw):
    pattern = Struct(
        "Service" / WString,
        "DWORD" / Int32ul,
        "Started" / Int8ul
    )

