# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DesktopActivityModerator
GUID : 32dd13df-9c0b-4c3b-b854-ee76c050f5f4
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("32dd13df-9c0b-4c3b-b854-ee76c050f5f4"), event_id=9, version=0)
class Microsoft_Windows_DesktopActivityModerator_9_0(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("32dd13df-9c0b-4c3b-b854-ee76c050f5f4"), event_id=21, version=0)
class Microsoft_Windows_DesktopActivityModerator_21_0(Etw):
    pattern = Struct(
        "SuspendFlag" / Int8ul
    )


@declare(guid=guid("32dd13df-9c0b-4c3b-b854-ee76c050f5f4"), event_id=22, version=0)
class Microsoft_Windows_DesktopActivityModerator_22_0(Etw):
    pattern = Struct(
        "SuspendFlag" / Int8ul
    )


@declare(guid=guid("32dd13df-9c0b-4c3b-b854-ee76c050f5f4"), event_id=23, version=0)
class Microsoft_Windows_DesktopActivityModerator_23_0(Etw):
    pattern = Struct(
        "SuspendFlag" / Int8ul
    )


@declare(guid=guid("32dd13df-9c0b-4c3b-b854-ee76c050f5f4"), event_id=24, version=0)
class Microsoft_Windows_DesktopActivityModerator_24_0(Etw):
    pattern = Struct(
        "SuspendFlag" / Int8ul
    )


@declare(guid=guid("32dd13df-9c0b-4c3b-b854-ee76c050f5f4"), event_id=25, version=0)
class Microsoft_Windows_DesktopActivityModerator_25_0(Etw):
    pattern = Struct(
        "ActiveFlag" / Int8ul
    )


@declare(guid=guid("32dd13df-9c0b-4c3b-b854-ee76c050f5f4"), event_id=26, version=0)
class Microsoft_Windows_DesktopActivityModerator_26_0(Etw):
    pattern = Struct(
        "ActiveFlag" / Int8ul
    )


@declare(guid=guid("32dd13df-9c0b-4c3b-b854-ee76c050f5f4"), event_id=31, version=0)
class Microsoft_Windows_DesktopActivityModerator_31_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "SessionId" / Int32ul,
        "ImageFileNameLength" / Int16ul,
        "ImageFileName" / Bytes(lambda this: this.ImageFileNameLength),
        "CommandLineLength" / Int16ul,
        "CommandLine" / Bytes(lambda this: this.CommandLineLength)
    )


@declare(guid=guid("32dd13df-9c0b-4c3b-b854-ee76c050f5f4"), event_id=32, version=0)
class Microsoft_Windows_DesktopActivityModerator_32_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "SessionId" / Int32ul
    )


@declare(guid=guid("32dd13df-9c0b-4c3b-b854-ee76c050f5f4"), event_id=41, version=0)
class Microsoft_Windows_DesktopActivityModerator_41_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "SessionId" / Int32ul,
        "ExemptGroup" / Int32ul,
        "Modern" / Int8ul
    )


@declare(guid=guid("32dd13df-9c0b-4c3b-b854-ee76c050f5f4"), event_id=42, version=0)
class Microsoft_Windows_DesktopActivityModerator_42_0(Etw):
    pattern = Struct(
        "PolicyRecords" / Int32ul
    )


@declare(guid=guid("32dd13df-9c0b-4c3b-b854-ee76c050f5f4"), event_id=51, version=0)
class Microsoft_Windows_DesktopActivityModerator_51_0(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "NTSTATUS" / Int32ul,
        "WorkItemQueued" / Int8ul
    )


@declare(guid=guid("32dd13df-9c0b-4c3b-b854-ee76c050f5f4"), event_id=52, version=0)
class Microsoft_Windows_DesktopActivityModerator_52_0(Etw):
    pattern = Struct(
        "ClientState" / Int32ul
    )


@declare(guid=guid("32dd13df-9c0b-4c3b-b854-ee76c050f5f4"), event_id=53, version=0)
class Microsoft_Windows_DesktopActivityModerator_53_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul
    )


@declare(guid=guid("32dd13df-9c0b-4c3b-b854-ee76c050f5f4"), event_id=60, version=0)
class Microsoft_Windows_DesktopActivityModerator_60_0(Etw):
    pattern = Struct(
        "DeviceBucket" / Int32ul,
        "ElapsedTimeMs" / Int32ul,
        "FastIoCount" / Int32ul,
        "SlowIoCount" / Int32ul
    )


@declare(guid=guid("32dd13df-9c0b-4c3b-b854-ee76c050f5f4"), event_id=61, version=0)
class Microsoft_Windows_DesktopActivityModerator_61_0(Etw):
    pattern = Struct(
        "DeviceType" / Int16ul,
        "DeviceBucket" / Int32ul,
        "ElapsedTime" / Int64ul,
        "SlowIo" / Int8ul
    )

