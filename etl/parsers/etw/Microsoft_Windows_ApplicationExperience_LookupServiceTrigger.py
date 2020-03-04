# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ApplicationExperience-LookupServiceTrigger
GUID : 18f4a5fd-fd3b-40a5-8fc2-e5d261c5d02e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("18f4a5fd-fd3b-40a5-8fc2-e5d261c5d02e"), event_id=1, version=0)
class Microsoft_Windows_ApplicationExperience_LookupServiceTrigger_1_0(Etw):
    pattern = Struct(
        "AeLookupServieTrigger" / Guid
    )

