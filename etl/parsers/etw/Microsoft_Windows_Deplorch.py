# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Deplorch
GUID : b9da9fe6-ae5f-4f3e-b2fa-8e623c11dc75
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b9da9fe6-ae5f-4f3e-b2fa-8e623c11dc75"), event_id=1002, version=0)
class Microsoft_Windows_Deplorch_1002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )

