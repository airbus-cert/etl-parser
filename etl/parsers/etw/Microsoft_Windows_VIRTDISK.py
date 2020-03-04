# -*- coding: utf-8 -*-
"""
Microsoft-Windows-VIRTDISK
GUID : 4d20df22-e177-4514-a369-f1759feedeb3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4d20df22-e177-4514-a369-f1759feedeb3"), event_id=1, version=0)
class Microsoft_Windows_VIRTDISK_1_0(Etw):
    pattern = Struct(
        "VhdFileName" / WString,
        "VhdVirtualStorageType" / Int32ul
    )


@declare(guid=guid("4d20df22-e177-4514-a369-f1759feedeb3"), event_id=2, version=0)
class Microsoft_Windows_VIRTDISK_2_0(Etw):
    pattern = Struct(
        "VhdHandle" / Int64ul,
        "VhdStatus" / Int32ul
    )


@declare(guid=guid("4d20df22-e177-4514-a369-f1759feedeb3"), event_id=3, version=0)
class Microsoft_Windows_VIRTDISK_3_0(Etw):
    pattern = Struct(
        "VhdHandle" / Int64ul
    )


@declare(guid=guid("4d20df22-e177-4514-a369-f1759feedeb3"), event_id=4, version=0)
class Microsoft_Windows_VIRTDISK_4_0(Etw):
    pattern = Struct(
        "VhdStatus" / Int32ul
    )


@declare(guid=guid("4d20df22-e177-4514-a369-f1759feedeb3"), event_id=5, version=0)
class Microsoft_Windows_VIRTDISK_5_0(Etw):
    pattern = Struct(
        "VhdHandle" / Int64ul
    )


@declare(guid=guid("4d20df22-e177-4514-a369-f1759feedeb3"), event_id=6, version=0)
class Microsoft_Windows_VIRTDISK_6_0(Etw):
    pattern = Struct(
        "VhdStatus" / Int32ul
    )


@declare(guid=guid("4d20df22-e177-4514-a369-f1759feedeb3"), event_id=1000, version=0)
class Microsoft_Windows_VIRTDISK_1000_0(Etw):
    pattern = Struct(
        "TraceData" / WString,
        "VmName" / WString,
        "VmId" / WString,
        "StackFrameCount" / Int32ul,
        "StackFrame" / Int64ul,
        "ModuleCount" / Int32ul,
        "Module" / Int32sl
    )


@declare(guid=guid("4d20df22-e177-4514-a369-f1759feedeb3"), event_id=1001, version=0)
class Microsoft_Windows_VIRTDISK_1001_0(Etw):
    pattern = Struct(
        "TraceData" / WString,
        "VmName" / WString,
        "VmId" / WString,
        "StackFrameCount" / Int32ul,
        "StackFrame" / Int64ul,
        "ModuleCount" / Int32ul,
        "Module" / Int32sl
    )


@declare(guid=guid("4d20df22-e177-4514-a369-f1759feedeb3"), event_id=1002, version=0)
class Microsoft_Windows_VIRTDISK_1002_0(Etw):
    pattern = Struct(
        "TraceData" / WString,
        "VmName" / WString,
        "VmId" / WString,
        "StackFrameCount" / Int32ul,
        "StackFrame" / Int64ul,
        "ModuleCount" / Int32ul,
        "Module" / Int32sl
    )


@declare(guid=guid("4d20df22-e177-4514-a369-f1759feedeb3"), event_id=1003, version=0)
class Microsoft_Windows_VIRTDISK_1003_0(Etw):
    pattern = Struct(
        "TraceData" / WString,
        "VmName" / WString,
        "VmId" / WString,
        "StackFrameCount" / Int32ul,
        "StackFrame" / Int64ul,
        "ModuleCount" / Int32ul,
        "Module" / Int32sl
    )

