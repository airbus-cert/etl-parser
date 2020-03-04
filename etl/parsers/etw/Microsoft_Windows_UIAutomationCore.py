# -*- coding: utf-8 -*-
"""
Microsoft-Windows-UIAutomationCore
GUID : 820a42d8-38c4-465d-b64e-d7d56ea1d612
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=1, version=0)
class Microsoft_Windows_UIAutomationCore_1_0(Etw):
    pattern = Struct(
        "Method" / WString,
        "Hresult" / Int32ul,
        "Details" / WString,
        "SourceHwnd" / WString,
        "Provider" / WString
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=2, version=0)
class Microsoft_Windows_UIAutomationCore_2_0(Etw):
    pattern = Struct(
        "Method" / WString,
        "Hresult" / Int32ul,
        "Details" / WString,
        "SourceHwnd" / WString,
        "Provider" / WString
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=3, version=0)
class Microsoft_Windows_UIAutomationCore_3_0(Etw):
    pattern = Struct(
        "Method" / WString,
        "ErrorCode" / Int32ul,
        "Details" / WString
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=4, version=0)
class Microsoft_Windows_UIAutomationCore_4_0(Etw):
    pattern = Struct(
        "Method" / WString,
        "Parameter" / WString,
        "Details" / WString
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=5, version=0)
class Microsoft_Windows_UIAutomationCore_5_0(Etw):
    pattern = Struct(
        "Method" / WString,
        "Win32Error" / Int32ul,
        "HRESULT" / Int32ul,
        "ProcessId" / Int32ul,
        "Details" / WString
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=509, version=0)
class Microsoft_Windows_UIAutomationCore_509_0(Etw):
    pattern = Struct(
        "MethodName" / WString,
        "ProcessId" / Int32ul,
        "ObjectReference" / Int32ul,
        "Duration" / Int64ul,
        "InstanceId" / Int32ul
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=510, version=0)
class Microsoft_Windows_UIAutomationCore_510_0(Etw):
    pattern = Struct(
        "MethodName" / WString,
        "ProcessId" / Int32ul,
        "ObjectReference" / Int32ul,
        "Duration" / Int64ul,
        "InstanceId" / Int32ul
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=513, version=0)
class Microsoft_Windows_UIAutomationCore_513_0(Etw):
    pattern = Struct(
        "Method" / WString,
        "HWND" / Int32ul,
        "WindowClassName" / WString,
        "EventId" / Int32ul,
        "ObjectId" / Int32ul,
        "ChildId" / Int32ul
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=514, version=0)
class Microsoft_Windows_UIAutomationCore_514_0(Etw):
    pattern = Struct(
        "Method" / WString,
        "HWND" / Int32ul,
        "WindowClassName" / WString,
        "EventId" / Int32ul,
        "ObjectId" / Int32ul,
        "ChildId" / Int32ul
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=515, version=0)
class Microsoft_Windows_UIAutomationCore_515_0(Etw):
    pattern = Struct(
        "Method" / WString,
        "HWND" / Int32ul,
        "WindowClassName" / WString,
        "EventId" / Int32ul,
        "CoalescedEvents" / Int32ul
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=517, version=0)
class Microsoft_Windows_UIAutomationCore_517_0(Etw):
    pattern = Struct(
        "MethodName" / WString,
        "Parameter1" / Int32ul,
        "Parameter2" / Int32ul
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=518, version=0)
class Microsoft_Windows_UIAutomationCore_518_0(Etw):
    pattern = Struct(
        "MethodName" / WString,
        "Parameter1" / Int32ul,
        "Parameter2" / Int32ul
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=519, version=0)
class Microsoft_Windows_UIAutomationCore_519_0(Etw):
    pattern = Struct(
        "MethodName" / WString,
        "HWND" / Int32ul
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=520, version=0)
class Microsoft_Windows_UIAutomationCore_520_0(Etw):
    pattern = Struct(
        "MethodName" / WString,
        "HWND" / Int32ul
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=521, version=0)
class Microsoft_Windows_UIAutomationCore_521_0(Etw):
    pattern = Struct(
        "IsChannelConnection" / Int8ul,
        "InstanceId" / Int32ul
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=522, version=0)
class Microsoft_Windows_UIAutomationCore_522_0(Etw):
    pattern = Struct(
        "IsChannelConnection" / Int8ul,
        "InstanceId" / Int32ul
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=523, version=0)
class Microsoft_Windows_UIAutomationCore_523_0(Etw):
    pattern = Struct(
        "MethodName" / WString,
        "ObjectReference" / Int32ul,
        "InstanceId" / Int32ul
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=524, version=0)
class Microsoft_Windows_UIAutomationCore_524_0(Etw):
    pattern = Struct(
        "MethodName" / WString,
        "ObjectReference" / Int32ul,
        "InstanceId" / Int32ul
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=525, version=0)
class Microsoft_Windows_UIAutomationCore_525_0(Etw):
    pattern = Struct(
        "InstanceId" / Int32ul
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=526, version=0)
class Microsoft_Windows_UIAutomationCore_526_0(Etw):
    pattern = Struct(
        "InstanceId" / Int32ul
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=529, version=0)
class Microsoft_Windows_UIAutomationCore_529_0(Etw):
    pattern = Struct(
        "ObjectCount" / Int32ul,
        "IsCombinedWithOtherMethod" / Int8ul
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=531, version=0)
class Microsoft_Windows_UIAutomationCore_531_0(Etw):
    pattern = Struct(
        "NewState" / WString
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=701, version=0)
class Microsoft_Windows_UIAutomationCore_701_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "HWND" / Int32ul,
        "WindowClassName" / WString,
        "RequestedMethod" / WString,
        "RequestedTimeout" / Int32ul
    )


@declare(guid=guid("820a42d8-38c4-465d-b64e-d7d56ea1d612"), event_id=702, version=0)
class Microsoft_Windows_UIAutomationCore_702_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "HWND" / Int32ul,
        "WindowClassName" / WString,
        "TotalEvents" / Int32ul,
        "EventId" / Int32ul,
        "EventCount" / Int32ul
    )

