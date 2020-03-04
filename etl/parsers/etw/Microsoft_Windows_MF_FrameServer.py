# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MF-FrameServer
GUID : 9e22a3ed-7b32-4b99-b6c2-21dd6ace01e1
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9e22a3ed-7b32-4b99-b6c2-21dd6ace01e1"), event_id=2, version=0)
class Microsoft_Windows_MF_FrameServer_2_0(Etw):
    pattern = Struct(
        "PinId" / Int32ul,
        "MediaType" / CString
    )


@declare(guid=guid("9e22a3ed-7b32-4b99-b6c2-21dd6ace01e1"), event_id=3, version=0)
class Microsoft_Windows_MF_FrameServer_3_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("9e22a3ed-7b32-4b99-b6c2-21dd6ace01e1"), event_id=4, version=0)
class Microsoft_Windows_MF_FrameServer_4_0(Etw):
    pattern = Struct(
        "D3dDesc" / WString,
        "LUID" / Int64ul,
        "VendorId" / Int32ul,
        "DeviceId" / Int32ul,
        "SubSysId" / Int32ul
    )


@declare(guid=guid("9e22a3ed-7b32-4b99-b6c2-21dd6ace01e1"), event_id=5, version=0)
class Microsoft_Windows_MF_FrameServer_5_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("9e22a3ed-7b32-4b99-b6c2-21dd6ace01e1"), event_id=6, version=0)
class Microsoft_Windows_MF_FrameServer_6_0(Etw):
    pattern = Struct(
        "SymbolicLink" / WString,
        "Devices" / Int32ul,
        "Streams" / Int32ul,
        "StreamType" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("9e22a3ed-7b32-4b99-b6c2-21dd6ace01e1"), event_id=7, version=0)
class Microsoft_Windows_MF_FrameServer_7_0(Etw):
    pattern = Struct(
        "SymbolicLink" / WString,
        "Devices" / Int32ul,
        "Streams" / Int32ul,
        "StreamType" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("9e22a3ed-7b32-4b99-b6c2-21dd6ace01e1"), event_id=8, version=0)
class Microsoft_Windows_MF_FrameServer_8_0(Etw):
    pattern = Struct(
        "StreamId" / Int32ul,
        "TimeStamp" / Int64ul,
        "Duration" / Int32ul,
        "MemoryType" / Int32ul
    )


@declare(guid=guid("9e22a3ed-7b32-4b99-b6c2-21dd6ace01e1"), event_id=9, version=0)
class Microsoft_Windows_MF_FrameServer_9_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("9e22a3ed-7b32-4b99-b6c2-21dd6ace01e1"), event_id=10, version=0)
class Microsoft_Windows_MF_FrameServer_10_0(Etw):
    pattern = Struct(
        "StreamId" / Int32ul,
        "StatSource" / Int32ul,
        "Flags" / Int32ul,
        "Requests" / Int64ul,
        "Input" / Int64ul,
        "Output" / Int64ul,
        "Dropped" / Int64ul,
        "FrameDelayRMSAccumulator" / Double,
        "FrameDelayRMSCounter" / Int32ul,
        "ExpectedFrameDelay" / Int64ul,
        "hr" / Int32ul,
        "SymbolicLink" / WString
    )


@declare(guid=guid("9e22a3ed-7b32-4b99-b6c2-21dd6ace01e1"), event_id=11, version=0)
class Microsoft_Windows_MF_FrameServer_11_0(Etw):
    pattern = Struct(
        "TimerScope" / Int32ul,
        "TimerScopeId" / Int64ul,
        "WatchdogOperation" / Int32ul,
        "DurationToTriggerInHns" / Int64ul,
        "SymbolicLink" / WString
    )


@declare(guid=guid("9e22a3ed-7b32-4b99-b6c2-21dd6ace01e1"), event_id=12, version=0)
class Microsoft_Windows_MF_FrameServer_12_0(Etw):
    pattern = Struct(
        "TimerScope" / Int32ul,
        "TimerScopeId" / Int64ul,
        "WatchdogOperation" / Int32ul,
        "DurationToCompletionInHns" / Int64ul
    )


@declare(guid=guid("9e22a3ed-7b32-4b99-b6c2-21dd6ace01e1"), event_id=13, version=0)
class Microsoft_Windows_MF_FrameServer_13_0(Etw):
    pattern = Struct(
        "TimerScope" / Int32ul,
        "TimerScopeId" / Int64ul,
        "WatchdogOperation" / Int32ul,
        "hr" / Int32ul
    )

