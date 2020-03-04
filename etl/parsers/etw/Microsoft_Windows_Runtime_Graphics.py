# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Runtime-Graphics
GUID : fa5cf675-72eb-49e2-b447-de5552faff1c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("fa5cf675-72eb-49e2-b447-de5552faff1c"), event_id=1, version=0)
class Microsoft_Windows_Runtime_Graphics_1_0(Etw):
    pattern = Struct(
        "WnfStateNameData0" / Int32ul,
        "WnfStateNameData1" / Int32ul
    )

