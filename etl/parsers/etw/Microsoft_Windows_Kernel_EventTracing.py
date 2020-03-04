# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-EventTracing
GUID : b675ec37-bdb6-4648-bc92-f3fdc74d3ca2
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=0, version=0)
class Microsoft_Windows_Kernel_EventTracing_0_0(Etw):
    pattern = Struct(
        "SessionName" / WString,
        "FileName" / WString,
        "ErrorCode" / Int32ul,
        "LoggingMode" / Int32ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=1, version=0)
class Microsoft_Windows_Kernel_EventTracing_1_0(Etw):
    pattern = Struct(
        "SessionName" / WString,
        "ErrorCode" / Int32ul,
        "LoggingMode" / Int32ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=2, version=0)
class Microsoft_Windows_Kernel_EventTracing_2_0(Etw):
    pattern = Struct(
        "SessionName" / WString,
        "FileName" / WString,
        "ErrorCode" / Int32ul,
        "LoggingMode" / Int32ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=3, version=0)
class Microsoft_Windows_Kernel_EventTracing_3_0(Etw):
    pattern = Struct(
        "SessionName" / WString,
        "FileName" / WString,
        "ErrorCode" / Int32ul,
        "LoggingMode" / Int32ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=3, version=1)
class Microsoft_Windows_Kernel_EventTracing_3_1(Etw):
    pattern = Struct(
        "SessionName" / WString,
        "FileName" / WString,
        "ErrorCode" / Int32ul,
        "LoggingMode" / Int32ul,
        "FailureReason" / Int32ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=4, version=0)
class Microsoft_Windows_Kernel_EventTracing_4_0(Etw):
    pattern = Struct(
        "SessionName" / WString,
        "FileName" / WString,
        "ErrorCode" / Int32ul,
        "LoggingMode" / Int32ul,
        "MaxFileSize" / Int64ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=5, version=0)
class Microsoft_Windows_Kernel_EventTracing_5_0(Etw):
    pattern = Struct(
        "SessionName" / WString,
        "FileName" / WString,
        "ErrorCode" / Int32ul,
        "LoggingMode" / Int32ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=8, version=0)
class Microsoft_Windows_Kernel_EventTracing_8_0(Etw):
    pattern = Struct(
        "ProviderName" / Guid
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=9, version=0)
class Microsoft_Windows_Kernel_EventTracing_9_0(Etw):
    pattern = Struct(
        "ProviderName" / Guid
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=10, version=0)
class Microsoft_Windows_Kernel_EventTracing_10_0(Etw):
    pattern = Struct(
        "SessionGuid" / Guid,
        "LoggerMode" / Int32ul,
        "SessionName" / WString,
        "LogFileName" / WString
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=10, version=1)
class Microsoft_Windows_Kernel_EventTracing_10_1(Etw):
    pattern = Struct(
        "SessionGuid" / Guid,
        "LoggerMode" / Int32ul,
        "SessionName" / WString,
        "LogFileName" / WString,
        "MinimumBuffers" / Int32ul,
        "MaximumBuffers" / Int32ul,
        "BufferSize" / Int32ul,
        "PeakBuffersCount" / Int32ul,
        "CurrentBuffersCount" / Int32ul,
        "FlushThreshold" / Int32ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=11, version=0)
class Microsoft_Windows_Kernel_EventTracing_11_0(Etw):
    pattern = Struct(
        "SessionGuid" / Guid,
        "LoggerMode" / Int32ul,
        "SessionName" / WString,
        "LogFileName" / WString
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=11, version=1)
class Microsoft_Windows_Kernel_EventTracing_11_1(Etw):
    pattern = Struct(
        "SessionGuid" / Guid,
        "LoggerMode" / Int32ul,
        "SessionName" / WString,
        "LogFileName" / WString,
        "MinimumBuffers" / Int32ul,
        "MaximumBuffers" / Int32ul,
        "BufferSize" / Int32ul,
        "PeakBuffersCount" / Int32ul,
        "CurrentBuffersCount" / Int32ul,
        "FlushThreshold" / Int32ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=11, version=2)
class Microsoft_Windows_Kernel_EventTracing_11_2(Etw):
    pattern = Struct(
        "SessionGuid" / Guid,
        "LoggerMode" / Int32ul,
        "SessionName" / WString,
        "LogFileName" / WString,
        "MinimumBuffers" / Int32ul,
        "MaximumBuffers" / Int32ul,
        "BufferSize" / Int32ul,
        "PeakBuffersCount" / Int32ul,
        "CurrentBuffersCount" / Int32ul,
        "FlushThreshold" / Int32ul,
        "EventsLost" / Int32ul,
        "BuffersLost" / Int32ul,
        "RealTimeBuffersLost" / Int32ul,
        "LoggerId" / Int32ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=12, version=0)
class Microsoft_Windows_Kernel_EventTracing_12_0(Etw):
    pattern = Struct(
        "SessionGuid" / Guid,
        "LoggerMode" / Int32ul,
        "SessionName" / WString,
        "LogFileName" / WString
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=13, version=0)
class Microsoft_Windows_Kernel_EventTracing_13_0(Etw):
    pattern = Struct(
        "SessionGuid" / Guid,
        "LoggerMode" / Int32ul,
        "SessionName" / WString,
        "LogFileName" / WString
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=14, version=0)
class Microsoft_Windows_Kernel_EventTracing_14_0(Etw):
    pattern = Struct(
        "ProviderName" / Guid,
        "SessionName" / WString
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=14, version=1)
class Microsoft_Windows_Kernel_EventTracing_14_1(Etw):
    pattern = Struct(
        "ProviderName" / Guid,
        "SessionName" / WString,
        "MatchAnyKeyword" / Int64ul,
        "MatchAllKeyword" / Int64ul,
        "EnableProperty" / Int32ul,
        "Level" / Int8ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=15, version=0)
class Microsoft_Windows_Kernel_EventTracing_15_0(Etw):
    pattern = Struct(
        "ProviderName" / Guid,
        "SessionName" / WString
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=17, version=0)
class Microsoft_Windows_Kernel_EventTracing_17_0(Etw):
    pattern = Struct(
        "SessionGuid" / Guid,
        "LoggerMode" / Int32ul,
        "SessionName" / WString,
        "LogFileName" / WString
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=19, version=0)
class Microsoft_Windows_Kernel_EventTracing_19_0(Etw):
    pattern = Struct(
        "ProviderId" / Guid,
        "StatusCode" / Int32ul,
        "EventId" / Int16ul,
        "SessionName" / WString
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=20, version=0)
class Microsoft_Windows_Kernel_EventTracing_20_0(Etw):
    pattern = Struct(
        "SessionGuid" / Guid,
        "LoggerMode" / Int32ul,
        "SessionName" / WString,
        "LogFileName" / WString,
        "MinimumBuffers" / Int32ul,
        "MaximumBuffers" / Int32ul,
        "BufferSize" / Int32ul,
        "PeakBuffersCount" / Int32ul,
        "CurrentBuffersCount" / Int32ul,
        "FlushThreshold" / Int32ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=20, version=1)
class Microsoft_Windows_Kernel_EventTracing_20_1(Etw):
    pattern = Struct(
        "SessionGuid" / Guid,
        "LoggerMode" / Int32ul,
        "SessionName" / WString,
        "LogFileName" / WString,
        "MinimumBuffers" / Int32ul,
        "MaximumBuffers" / Int32ul,
        "BufferSize" / Int32ul,
        "PeakBuffersCount" / Int32ul,
        "CurrentBuffersCount" / Int32ul,
        "FlushThreshold" / Int32ul,
        "EventsLost" / Int32ul,
        "BuffersLost" / Int32ul,
        "RealTimeBuffersLost" / Int32ul,
        "LoggerId" / Int32ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=22, version=0)
class Microsoft_Windows_Kernel_EventTracing_22_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "BufferSize" / Int32ul,
        "BuffersPersisted" / Int32ul,
        "BuffersWritten" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=22, version=1)
class Microsoft_Windows_Kernel_EventTracing_22_1(Etw):
    pattern = Struct(
        "FileName" / WString,
        "BufferSize" / Int32ul,
        "BuffersPersisted" / Int32ul,
        "BuffersWritten" / Int32ul,
        "Status" / Int32ul,
        "BuffersLost" / Int32ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=23, version=0)
class Microsoft_Windows_Kernel_EventTracing_23_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "BufferSize" / Int32ul,
        "BuffersPersisted" / Int32ul,
        "BuffersWritten" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=23, version=1)
class Microsoft_Windows_Kernel_EventTracing_23_1(Etw):
    pattern = Struct(
        "FileName" / WString,
        "BufferSize" / Int32ul,
        "BuffersPersisted" / Int32ul,
        "BuffersWritten" / Int32ul,
        "Status" / Int32ul,
        "BuffersLost" / Int32ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=24, version=0)
class Microsoft_Windows_Kernel_EventTracing_24_0(Etw):
    pattern = Struct(
        "GUID" / Guid,
        "FilterFlags" / Int32ul,
        "LastEnableLoggerId" / Int16ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=25, version=0)
class Microsoft_Windows_Kernel_EventTracing_25_0(Etw):
    pattern = Struct(
        "GUID" / Guid,
        "FilterFlags" / Int32ul,
        "LastEnableLoggerId" / Int16ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=26, version=0)
class Microsoft_Windows_Kernel_EventTracing_26_0(Etw):
    pattern = Struct(
        "GUID" / Guid,
        "Index" / Int8ul,
        "LoggerId" / Int16ul,
        "MatchAnyKeyword" / Int64ul,
        "MatchAllKeyword" / Int64ul,
        "Level" / Int8ul,
        "EnableProperty" / Int32ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=27, version=0)
class Microsoft_Windows_Kernel_EventTracing_27_0(Etw):
    pattern = Struct(
        "ProviderGUID" / Guid,
        "GroupGUID" / Guid,
        "Flags" / Int16ul,
        "EnableMask" / Int8ul,
        "GroupEnableMask" / Int8ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=28, version=0)
class Microsoft_Windows_Kernel_EventTracing_28_0(Etw):
    pattern = Struct(
        "ProviderGuid" / Guid,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b675ec37-bdb6-4648-bc92-f3fdc74d3ca2"), event_id=29, version=0)
class Microsoft_Windows_Kernel_EventTracing_29_0(Etw):
    pattern = Struct(
        "ProviderGuid" / Guid,
        "ProviderGroupGuid" / Guid
    )

