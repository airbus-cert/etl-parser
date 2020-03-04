# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SystemEventsBroker
GUID : b6bfcc79-a3af-4089-8d4d-0eecb1b80779
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b6bfcc79-a3af-4089-8d4d-0eecb1b80779"), event_id=15, version=1)
class Microsoft_Windows_SystemEventsBroker_15_1(Etw):
    pattern = Struct(
        "BrokeredEventId" / Guid,
        "UserSID" / Sid,
        "EventType" / Int32ul
    )


@declare(guid=guid("b6bfcc79-a3af-4089-8d4d-0eecb1b80779"), event_id=16, version=1)
class Microsoft_Windows_SystemEventsBroker_16_1(Etw):
    pattern = Struct(
        "BrokeredEventId" / Guid
    )


@declare(guid=guid("b6bfcc79-a3af-4089-8d4d-0eecb1b80779"), event_id=17, version=1)
class Microsoft_Windows_SystemEventsBroker_17_1(Etw):
    pattern = Struct(
        "BrokeredEventId" / Guid
    )


@declare(guid=guid("b6bfcc79-a3af-4089-8d4d-0eecb1b80779"), event_id=18, version=1)
class Microsoft_Windows_SystemEventsBroker_18_1(Etw):
    pattern = Struct(
        "BrokeredEventId" / Guid
    )


@declare(guid=guid("b6bfcc79-a3af-4089-8d4d-0eecb1b80779"), event_id=19, version=1)
class Microsoft_Windows_SystemEventsBroker_19_1(Etw):
    pattern = Struct(
        "SessionID" / Int32ul,
        "UserSID" / Sid
    )


@declare(guid=guid("b6bfcc79-a3af-4089-8d4d-0eecb1b80779"), event_id=19, version=2)
class Microsoft_Windows_SystemEventsBroker_19_2(Etw):
    pattern = Struct(
        "SessionID" / Int32ul
    )

