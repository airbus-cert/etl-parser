# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DirectShow-KernelSupport
GUID : 3cc2d4af-da5e-4ed4-bcbe-3cf995940483
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3cc2d4af-da5e-4ed4-bcbe-3cf995940483"), event_id=7, version=0)
class Microsoft_Windows_DirectShow_KernelSupport_7_0(Etw):
    pattern = Struct(
        "Buffer" / Int64ul,
        "TimeStamp" / Int64sl
    )


@declare(guid=guid("3cc2d4af-da5e-4ed4-bcbe-3cf995940483"), event_id=8, version=0)
class Microsoft_Windows_DirectShow_KernelSupport_8_0(Etw):
    pattern = Struct(
        "Buffer" / Int64ul,
        "TimeStamp" / Int64sl
    )


@declare(guid=guid("3cc2d4af-da5e-4ed4-bcbe-3cf995940483"), event_id=9, version=0)
class Microsoft_Windows_DirectShow_KernelSupport_9_0(Etw):
    pattern = Struct(
        "Buffer" / Int64ul,
        "TimeStamp" / Int64sl
    )


@declare(guid=guid("3cc2d4af-da5e-4ed4-bcbe-3cf995940483"), event_id=10, version=0)
class Microsoft_Windows_DirectShow_KernelSupport_10_0(Etw):
    pattern = Struct(
        "Buffer" / Int64ul,
        "TimeStamp" / Int64sl
    )


@declare(guid=guid("3cc2d4af-da5e-4ed4-bcbe-3cf995940483"), event_id=11, version=0)
class Microsoft_Windows_DirectShow_KernelSupport_11_0(Etw):
    pattern = Struct(
        "Buffer" / Int64ul,
        "TimeStamp" / Int64sl
    )


@declare(guid=guid("3cc2d4af-da5e-4ed4-bcbe-3cf995940483"), event_id=12, version=0)
class Microsoft_Windows_DirectShow_KernelSupport_12_0(Etw):
    pattern = Struct(
        "Buffer" / Int64ul,
        "TimeStamp" / Int64sl
    )


@declare(guid=guid("3cc2d4af-da5e-4ed4-bcbe-3cf995940483"), event_id=13, version=0)
class Microsoft_Windows_DirectShow_KernelSupport_13_0(Etw):
    pattern = Struct(
        "Buffer" / Int64ul,
        "TimeStamp" / Int64sl
    )

