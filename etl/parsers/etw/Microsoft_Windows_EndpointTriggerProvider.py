# -*- coding: utf-8 -*-
"""
Microsoft-Windows-EndpointTriggerProvider
GUID : 92aab24d-d9a9-4a60-9f94-201fed3e3e88
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("92aab24d-d9a9-4a60-9f94-201fed3e3e88"), event_id=1, version=0)
class Microsoft_Windows_EndpointTriggerProvider_1_0(Etw):
    pattern = Struct(
        "TriggerSubType" / WString,
        "TriggerData" / WString
    )

