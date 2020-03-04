# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Shell-LockScreenContent
GUID : a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2"), event_id=11, version=0)
class Microsoft_Windows_Shell_LockScreenContent_11_0(Etw):
    pattern = Struct(
        "ImageCount" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2"), event_id=13, version=0)
class Microsoft_Windows_Shell_LockScreenContent_13_0(Etw):
    pattern = Struct(
        "ImagePath" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2"), event_id=22, version=0)
class Microsoft_Windows_Shell_LockScreenContent_22_0(Etw):
    pattern = Struct(
        "OnPrimaryMonitor" / Int8ul,
        "Initialized" / Int8ul
    )


@declare(guid=guid("a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2"), event_id=23, version=0)
class Microsoft_Windows_Shell_LockScreenContent_23_0(Etw):
    pattern = Struct(
        "OnPrimaryMonitor" / Int8ul,
        "Layout" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2"), event_id=30, version=0)
class Microsoft_Windows_Shell_LockScreenContent_30_0(Etw):
    pattern = Struct(
        "OnPrimaryMonitor" / Int8ul,
        "LayoutChosen" / Int32ul
    )


@declare(guid=guid("a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2"), event_id=31, version=0)
class Microsoft_Windows_Shell_LockScreenContent_31_0(Etw):
    pattern = Struct(
        "OnPrimaryMonitor" / Int8ul,
        "LayoutChosen" / Int32ul
    )


@declare(guid=guid("a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2"), event_id=32, version=0)
class Microsoft_Windows_Shell_LockScreenContent_32_0(Etw):
    pattern = Struct(
        "OnPrimaryMonitor" / Int8ul
    )


@declare(guid=guid("a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2"), event_id=36, version=0)
class Microsoft_Windows_Shell_LockScreenContent_36_0(Etw):
    pattern = Struct(
        "Layout" / Int32ul
    )


@declare(guid=guid("a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2"), event_id=37, version=0)
class Microsoft_Windows_Shell_LockScreenContent_37_0(Etw):
    pattern = Struct(
        "EnterLayout" / Int32ul,
        "ExitLayout" / Int32ul,
        "Cookie" / Int32ul
    )


@declare(guid=guid("a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2"), event_id=38, version=0)
class Microsoft_Windows_Shell_LockScreenContent_38_0(Etw):
    pattern = Struct(
        "EnterLayout" / Int32ul,
        "ExitLayout" / Int32ul,
        "Cookie" / Int32ul
    )


@declare(guid=guid("a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2"), event_id=39, version=0)
class Microsoft_Windows_Shell_LockScreenContent_39_0(Etw):
    pattern = Struct(
        "AmbientLayout" / Int32ul,
        "Cookie" / Int32ul
    )


@declare(guid=guid("a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2"), event_id=40, version=0)
class Microsoft_Windows_Shell_LockScreenContent_40_0(Etw):
    pattern = Struct(
        "AmbientLayout" / Int32ul,
        "Cookie" / Int32ul
    )


@declare(guid=guid("a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2"), event_id=46, version=0)
class Microsoft_Windows_Shell_LockScreenContent_46_0(Etw):
    pattern = Struct(
        "DualMonitorSourcing" / Int8ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2"), event_id=47, version=0)
class Microsoft_Windows_Shell_LockScreenContent_47_0(Etw):
    pattern = Struct(
        "ImagePath" / WString,
        "PossibleLayoutRegions" / Int32ul,
        "Bucket" / Int32ul,
        "ImageWidth" / Int32ul,
        "ImageHeight" / Int32ul,
        "MonitorWidth" / Int32ul,
        "MonitorHeight" / Int32ul
    )


@declare(guid=guid("a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2"), event_id=48, version=0)
class Microsoft_Windows_Shell_LockScreenContent_48_0(Etw):
    pattern = Struct(
        "FullRefresh" / Int8ul,
        "Result" / Int32ul
    )


@declare(guid=guid("a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2"), event_id=49, version=0)
class Microsoft_Windows_Shell_LockScreenContent_49_0(Etw):
    pattern = Struct(
        "WasInitialized" / Int8ul
    )


@declare(guid=guid("a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2"), event_id=51, version=0)
class Microsoft_Windows_Shell_LockScreenContent_51_0(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2"), event_id=53, version=0)
class Microsoft_Windows_Shell_LockScreenContent_53_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2"), event_id=57, version=0)
class Microsoft_Windows_Shell_LockScreenContent_57_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2"), event_id=59, version=0)
class Microsoft_Windows_Shell_LockScreenContent_59_0(Etw):
    pattern = Struct(
        "BucketSize" / Int32ul,
        "ValidatedItems" / Int32ul
    )


@declare(guid=guid("a3c0d58a-9fe5-4f24-a2ce-e16de8baa0d2"), event_id=64, version=0)
class Microsoft_Windows_Shell_LockScreenContent_64_0(Etw):
    pattern = Struct(
        "MeetsLayoutConstraints" / Int8ul,
        "MeetsTimeConstraints" / Int8ul,
        "MeetsSlideReuseConstraints" / Int8ul
    )

