# -*- coding: utf-8 -*-
"""
Microsoft-Windows-KernelStreaming
GUID : 548c4417-ce45-41ff-99dd-528f01ce0fe1
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("548c4417-ce45-41ff-99dd-528f01ce0fe1"), event_id=202, version=0)
class Microsoft_Windows_KernelStreaming_202_0(Etw):
    pattern = Struct(
        "pIrp" / Int64ul
    )


@declare(guid=guid("548c4417-ce45-41ff-99dd-528f01ce0fe1"), event_id=203, version=0)
class Microsoft_Windows_KernelStreaming_203_0(Etw):
    pattern = Struct(
        "pIrp" / Int64ul
    )


@declare(guid=guid("548c4417-ce45-41ff-99dd-528f01ce0fe1"), event_id=204, version=0)
class Microsoft_Windows_KernelStreaming_204_0(Etw):
    pattern = Struct(
        "ProcessId" / Int64ul,
        "PinId" / Int32ul,
        "FilterAddress" / Int64ul
    )


@declare(guid=guid("548c4417-ce45-41ff-99dd-528f01ce0fe1"), event_id=205, version=0)
class Microsoft_Windows_KernelStreaming_205_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("548c4417-ce45-41ff-99dd-528f01ce0fe1"), event_id=208, version=0)
class Microsoft_Windows_KernelStreaming_208_0(Etw):
    pattern = Struct(
        "FilterExt" / Int64ul,
        "PinState" / Int32ul
    )


@declare(guid=guid("548c4417-ce45-41ff-99dd-528f01ce0fe1"), event_id=209, version=0)
class Microsoft_Windows_KernelStreaming_209_0(Etw):
    pattern = Struct(
        "EntryCount" / Int32ul
    )


@declare(guid=guid("548c4417-ce45-41ff-99dd-528f01ce0fe1"), event_id=211, version=0)
class Microsoft_Windows_KernelStreaming_211_0(Etw):
    pattern = Struct(
        "PinId" / Int32ul,
        "BufSize" / Int32ul
    )


@declare(guid=guid("548c4417-ce45-41ff-99dd-528f01ce0fe1"), event_id=212, version=0)
class Microsoft_Windows_KernelStreaming_212_0(Etw):
    pattern = Struct(
        "PinId" / Int32ul,
        "BufSize" / Int32ul
    )


@declare(guid=guid("548c4417-ce45-41ff-99dd-528f01ce0fe1"), event_id=213, version=0)
class Microsoft_Windows_KernelStreaming_213_0(Etw):
    pattern = Struct(
        "pKsDevice" / Int64ul,
        "pIrp" / Int64ul,
        "InterfaceGuid" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("548c4417-ce45-41ff-99dd-528f01ce0fe1"), event_id=214, version=0)
class Microsoft_Windows_KernelStreaming_214_0(Etw):
    pattern = Struct(
        "pKsDevice" / Int64ul,
        "pIrp" / Int64ul,
        "InterfaceGuid" / Guid,
        "Status" / Int32ul
    )

