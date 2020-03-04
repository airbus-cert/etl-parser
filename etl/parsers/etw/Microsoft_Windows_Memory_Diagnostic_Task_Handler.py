# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Memory-Diagnostic-Task-Handler
GUID : babda89a-4d5e-48eb-af3d-e0e8410207c0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("babda89a-4d5e-48eb-af3d-e0e8410207c0"), event_id=1001, version=0)
class Microsoft_Windows_Memory_Diagnostic_Task_Handler_1001_0(Etw):
    pattern = Struct(
        "RemovedMemorySize" / Int64ul
    )


@declare(guid=guid("babda89a-4d5e-48eb-af3d-e0e8410207c0"), event_id=1003, version=0)
class Microsoft_Windows_Memory_Diagnostic_Task_Handler_1003_0(Etw):
    pattern = Struct(
        "RemovedMemorySize" / Int64ul
    )

