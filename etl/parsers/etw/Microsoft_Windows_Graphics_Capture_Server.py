# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Graphics-Capture-Server
GUID : 7d0cbd25-390e-524d-8c1e-2a8e846055c0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7d0cbd25-390e-524d-8c1e-2a8e846055c0"), event_id=1, version=0)
class Microsoft_Windows_Graphics_Capture_Server_1_0(Etw):
    pattern = Struct(
        "processId" / Int32ul
    )


@declare(guid=guid("7d0cbd25-390e-524d-8c1e-2a8e846055c0"), event_id=2, version=0)
class Microsoft_Windows_Graphics_Capture_Server_2_0(Etw):
    pattern = Struct(
        "processId" / Int32ul
    )

