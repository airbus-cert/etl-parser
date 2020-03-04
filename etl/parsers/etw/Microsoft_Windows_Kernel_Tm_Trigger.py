# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-Tm-Trigger
GUID : ce20d1c3-a247-4c41-bcb8-3c7f52c8b805
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ce20d1c3-a247-4c41-bcb8-3c7f52c8b805"), event_id=1, version=0)
class Microsoft_Windows_Kernel_Tm_Trigger_1_0(Etw):
    pattern = Struct(
        "KtmTriggerSvcStartGuid" / Guid
    )

