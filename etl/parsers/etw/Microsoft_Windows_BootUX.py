# -*- coding: utf-8 -*-
"""
Microsoft-Windows-BootUX
GUID : 67d781bd-cbd2-4bd2-ad1f-6152fb891246
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("67d781bd-cbd2-4bd2-ad1f-6152fb891246"), event_id=1004, version=0)
class Microsoft_Windows_BootUX_1004_0(Etw):
    pattern = Struct(
        "UsingUSB" / Int8ul,
        "success" / Int8ul,
        "resultCode" / Int32ul
    )


@declare(guid=guid("67d781bd-cbd2-4bd2-ad1f-6152fb891246"), event_id=1005, version=0)
class Microsoft_Windows_BootUX_1005_0(Etw):
    pattern = Struct(
        "programCounter" / Int64ul,
        "exceptionType" / Int32ul
    )

