# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TimeBroker
GUID : 0657adc1-9ae8-4e18-932d-e6079cda5ab3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("0657adc1-9ae8-4e18-932d-e6079cda5ab3"), event_id=1, version=1)
class Microsoft_Windows_TimeBroker_1_1(Etw):
    pattern = Struct(
        "BrokeredEventId" / Guid,
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("0657adc1-9ae8-4e18-932d-e6079cda5ab3"), event_id=2, version=1)
class Microsoft_Windows_TimeBroker_2_1(Etw):
    pattern = Struct(
        "BrokeredEventId" / Guid,
        "StartTime" / Int64ul,
        "EndTime" / Int64ul
    )


@declare(guid=guid("0657adc1-9ae8-4e18-932d-e6079cda5ab3"), event_id=3, version=1)
class Microsoft_Windows_TimeBroker_3_1(Etw):
    pattern = Struct(
        "BrokeredEventId" / Guid,
        "EventType" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("0657adc1-9ae8-4e18-932d-e6079cda5ab3"), event_id=4, version=1)
class Microsoft_Windows_TimeBroker_4_1(Etw):
    pattern = Struct(
        "BrokeredEventId" / Guid,
        "Status" / Int32ul
    )

