# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Fault-Tolerant-Heap
GUID : 6b93bf66-a922-4c11-a617-cf60d95c133d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6b93bf66-a922-4c11-a617-cf60d95c133d"), event_id=1003, version=0)
class Microsoft_Windows_Fault_Tolerant_Heap_1003_0(Etw):
    pattern = Struct(
        "FthEnabledPID" / Int32ul,
        "FthEnabledProcessName" / WString,
        "FthEnabledProcessStartup" / Int64ul
    )

