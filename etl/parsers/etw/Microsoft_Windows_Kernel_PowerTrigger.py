# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-PowerTrigger
GUID : aa1f73e8-15fd-45d2-abfd-e7f64f78eb11
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("aa1f73e8-15fd-45d2-abfd-e7f64f78eb11"), event_id=1, version=0)
class Microsoft_Windows_Kernel_PowerTrigger_1_0(Etw):
    pattern = Struct(
        "AoAc" / Int8ul
    )

