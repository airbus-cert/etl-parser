# -*- coding: utf-8 -*-
"""
Microsoft-Windows-EventCollector
GUID : b977cf02-76f6-df84-cc1a-6a4b232322b6
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b977cf02-76f6-df84-cc1a-6a4b232322b6"), event_id=1, version=0)
class Microsoft_Windows_EventCollector_1_0(Etw):
    pattern = Struct(
        "SubscriptionId" / WString,
        "MachineName" / WString,
        "ErrorCode" / Int32ul,
        "FaultMessage" / WString
    )


@declare(guid=guid("b977cf02-76f6-df84-cc1a-6a4b232322b6"), event_id=2, version=0)
class Microsoft_Windows_EventCollector_2_0(Etw):
    pattern = Struct(
        "SubscriptionId" / WString,
        "MachineName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b977cf02-76f6-df84-cc1a-6a4b232322b6"), event_id=3, version=0)
class Microsoft_Windows_EventCollector_3_0(Etw):
    pattern = Struct(
        "SubscriptionId" / WString
    )


@declare(guid=guid("b977cf02-76f6-df84-cc1a-6a4b232322b6"), event_id=4, version=0)
class Microsoft_Windows_EventCollector_4_0(Etw):
    pattern = Struct(
        "SubscriptionId" / WString,
        "MachineName" / WString,
        "ErrorCode" / Int32ul,
        "FaultMessage" / WString
    )


@declare(guid=guid("b977cf02-76f6-df84-cc1a-6a4b232322b6"), event_id=5, version=0)
class Microsoft_Windows_EventCollector_5_0(Etw):
    pattern = Struct(
        "SubscriptionId" / WString,
        "MachineName" / WString
    )


@declare(guid=guid("b977cf02-76f6-df84-cc1a-6a4b232322b6"), event_id=6, version=0)
class Microsoft_Windows_EventCollector_6_0(Etw):
    pattern = Struct(
        "SubscriptionId" / WString,
        "MachineName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b977cf02-76f6-df84-cc1a-6a4b232322b6"), event_id=501, version=0)
class Microsoft_Windows_EventCollector_501_0(Etw):
    pattern = Struct(
        "SubscriptionId" / WString,
        "MachineName" / WString,
        "ErrorCode" / Int32ul,
        "EventData" / WString
    )


@declare(guid=guid("b977cf02-76f6-df84-cc1a-6a4b232322b6"), event_id=502, version=0)
class Microsoft_Windows_EventCollector_502_0(Etw):
    pattern = Struct(
        "SubscriptionId" / WString,
        "MachineName" / WString,
        "EventCount" / Int32ul
    )

