# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Security-Adminless
GUID : ea216962-877b-5b73-f7c5-8aef5375959e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ea216962-877b-5b73-f7c5-8aef5375959e"), event_id=1, version=0)
class Microsoft_Windows_Security_Adminless_1_0(Etw):
    pattern = Struct(
        "FailureTime" / Int64ul,
        "StackHash" / Int32ul
    )

