# -*- coding: utf-8 -*-
"""
Microsoft-Windows-User-Diagnostic
GUID : 305fc87b-002a-5e26-d297-60223012ca9c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("305fc87b-002a-5e26-d297-60223012ca9c"), event_id=1, version=0)
class Microsoft_Windows_User_Diagnostic_1_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )

