# -*- coding: utf-8 -*-
"""
Microsoft-Windows-RasServer
GUID : 29d13147-1c2e-48ec-9994-e29dfe496eb3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("29d13147-1c2e-48ec-9994-e29dfe496eb3"), event_id=50010, version=0)
class Microsoft_Windows_RasServer_50010_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )

