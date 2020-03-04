# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ServiceTriggerPerfEventProvider
GUID : 6545939f-3398-411a-88b7-6a8914b8cec7
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6545939f-3398-411a-88b7-6a8914b8cec7"), event_id=1, version=0)
class Microsoft_Windows_ServiceTriggerPerfEventProvider_1_0(Etw):
    pattern = Struct(
        "TriggerSubType" / WString,
        "TriggerData" / WString
    )


@declare(guid=guid("6545939f-3398-411a-88b7-6a8914b8cec7"), event_id=2, version=0)
class Microsoft_Windows_ServiceTriggerPerfEventProvider_2_0(Etw):
    pattern = Struct(
        "TriggerSubType" / WString,
        "TriggerData" / WString
    )


@declare(guid=guid("6545939f-3398-411a-88b7-6a8914b8cec7"), event_id=3, version=0)
class Microsoft_Windows_ServiceTriggerPerfEventProvider_3_0(Etw):
    pattern = Struct(
        "TriggerSubType" / WString,
        "TriggerData" / WString
    )

