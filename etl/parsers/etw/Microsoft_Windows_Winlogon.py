# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Winlogon
GUID : dbe9b383-7cf3-4331-91cc-a3cb16a3b538
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=2, version=0)
class Microsoft_Windows_Winlogon_2_0(Etw):
    pattern = Struct(
        "Win32Status" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=3, version=0)
class Microsoft_Windows_Winlogon_3_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=4, version=0)
class Microsoft_Windows_Winlogon_4_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=9, version=0)
class Microsoft_Windows_Winlogon_9_0(Etw):
    pattern = Struct(
        "CommandList" / WString
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=301, version=0)
class Microsoft_Windows_Winlogon_301_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=401, version=0)
class Microsoft_Windows_Winlogon_401_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=402, version=0)
class Microsoft_Windows_Winlogon_402_0(Etw):
    pattern = Struct(
        "Win32Status" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=403, version=0)
class Microsoft_Windows_Winlogon_403_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=404, version=0)
class Microsoft_Windows_Winlogon_404_0(Etw):
    pattern = Struct(
        "Win32Status" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=801, version=0)
class Microsoft_Windows_Winlogon_801_0(Etw):
    pattern = Struct(
        "Event" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=802, version=0)
class Microsoft_Windows_Winlogon_802_0(Etw):
    pattern = Struct(
        "Event" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=803, version=0)
class Microsoft_Windows_Winlogon_803_0(Etw):
    pattern = Struct(
        "EventCode" / Int32ul,
        "SessionId" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=804, version=0)
class Microsoft_Windows_Winlogon_804_0(Etw):
    pattern = Struct(
        "EventCode" / Int32ul,
        "SessionId" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=805, version=0)
class Microsoft_Windows_Winlogon_805_0(Etw):
    pattern = Struct(
        "Event" / Int32ul,
        "SubscriberName" / WString
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=806, version=0)
class Microsoft_Windows_Winlogon_806_0(Etw):
    pattern = Struct(
        "Event" / Int32ul,
        "SubscriberName" / WString
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=807, version=0)
class Microsoft_Windows_Winlogon_807_0(Etw):
    pattern = Struct(
        "Event" / Int32ul,
        "SubscriberName" / WString,
        "Message" / WString
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=808, version=0)
class Microsoft_Windows_Winlogon_808_0(Etw):
    pattern = Struct(
        "Event" / Int32ul,
        "SubscriberName" / WString,
        "Message" / WString
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=809, version=0)
class Microsoft_Windows_Winlogon_809_0(Etw):
    pattern = Struct(
        "SubscriberName" / WString
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=810, version=0)
class Microsoft_Windows_Winlogon_810_0(Etw):
    pattern = Struct(
        "SubscriberName" / WString
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=811, version=0)
class Microsoft_Windows_Winlogon_811_0(Etw):
    pattern = Struct(
        "Event" / Int32ul,
        "SubscriberName" / WString
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=812, version=0)
class Microsoft_Windows_Winlogon_812_0(Etw):
    pattern = Struct(
        "Event" / Int32ul,
        "SubscriberName" / WString
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=1001, version=0)
class Microsoft_Windows_Winlogon_1001_0(Etw):
    pattern = Struct(
        "ActionId" / Int32ul,
        "TimeLeft" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=1101, version=0)
class Microsoft_Windows_Winlogon_1101_0(Etw):
    pattern = Struct(
        "UserSid" / Sid,
        "UserName" / WString,
        "UserDomain" / WString
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=1102, version=0)
class Microsoft_Windows_Winlogon_1102_0(Etw):
    pattern = Struct(
        "UserSid" / Sid,
        "UserName" / WString,
        "UserDomain" / WString
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=1103, version=0)
class Microsoft_Windows_Winlogon_1103_0(Etw):
    pattern = Struct(
        "UserSid" / Sid,
        "UserName" / WString,
        "UserDomain" / WString
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=1104, version=0)
class Microsoft_Windows_Winlogon_1104_0(Etw):
    pattern = Struct(
        "Win32Status" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=5001, version=0)
class Microsoft_Windows_Winlogon_5001_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=5003, version=0)
class Microsoft_Windows_Winlogon_5003_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=5007, version=0)
class Microsoft_Windows_Winlogon_5007_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=5007, version=1)
class Microsoft_Windows_Winlogon_5007_1(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "ReadyBootTrainingCountSinceLastServicing" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=5007, version=2)
class Microsoft_Windows_Winlogon_5007_2(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "ReadyBootTrainingCountSinceLastServicing" / Int32ul,
        "SyncPrefetchErrorCode" / Int32ul,
        "SyncPrefetchDurationMs" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=6001, version=0)
class Microsoft_Windows_Winlogon_6001_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=6101, version=0)
class Microsoft_Windows_Winlogon_6101_0(Etw):
    pattern = Struct(
        "LogoffFlags" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=6102, version=0)
class Microsoft_Windows_Winlogon_6102_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=6103, version=0)
class Microsoft_Windows_Winlogon_6103_0(Etw):
    pattern = Struct(
        "LogoffFlags" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=6104, version=0)
class Microsoft_Windows_Winlogon_6104_0(Etw):
    pattern = Struct(
        "LogoffFlags" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=6107, version=0)
class Microsoft_Windows_Winlogon_6107_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=6109, version=0)
class Microsoft_Windows_Winlogon_6109_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=6116, version=0)
class Microsoft_Windows_Winlogon_6116_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul,
        "ResolverData" / Int32ul
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=7001, version=0)
class Microsoft_Windows_Winlogon_7001_0(Etw):
    pattern = Struct(
        "TSId" / Int32ul,
        "UserSid" / Sid
    )


@declare(guid=guid("dbe9b383-7cf3-4331-91cc-a3cb16a3b538"), event_id=7002, version=0)
class Microsoft_Windows_Winlogon_7002_0(Etw):
    pattern = Struct(
        "TSId" / Int32ul,
        "UserSid" / Sid
    )

