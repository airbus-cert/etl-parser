# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Subsys-Csr
GUID : e8316a2d-0d94-4f52-85dd-1e15b66c5891
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e8316a2d-0d94-4f52-85dd-1e15b66c5891"), event_id=3, version=0)
class Microsoft_Windows_Subsys_Csr_3_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "Level" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("e8316a2d-0d94-4f52-85dd-1e15b66c5891"), event_id=4, version=0)
class Microsoft_Windows_Subsys_Csr_4_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("e8316a2d-0d94-4f52-85dd-1e15b66c5891"), event_id=4, version=1)
class Microsoft_Windows_Subsys_Csr_4_1(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "ProcessId" / Int32ul
    )

