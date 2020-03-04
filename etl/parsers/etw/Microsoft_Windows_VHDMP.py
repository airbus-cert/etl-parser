# -*- coding: utf-8 -*-
"""
Microsoft-Windows-VHDMP
GUID : e2816346-87f4-4f85-95c3-0c79409aa89d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=1, version=0)
class Microsoft_Windows_VHDMP_1_0(Etw):
    pattern = Struct(
        "VhdFileName" / WString,
        "VhdDiskNumber" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=2, version=0)
class Microsoft_Windows_VHDMP_2_0(Etw):
    pattern = Struct(
        "VhdFileName" / WString,
        "VhdDiskNumber" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=3, version=0)
class Microsoft_Windows_VHDMP_3_0(Etw):
    pattern = Struct(
        "VhdFileName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=4, version=0)
class Microsoft_Windows_VHDMP_4_0(Etw):
    pattern = Struct(
        "VhdFileName" / WString
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=5, version=0)
class Microsoft_Windows_VHDMP_5_0(Etw):
    pattern = Struct(
        "VhdMetaOps" / CString,
        "VhdFileName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=6, version=0)
class Microsoft_Windows_VHDMP_6_0(Etw):
    pattern = Struct(
        "VhdIoType" / Int32ul,
        "VhdFileName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=7, version=0)
class Microsoft_Windows_VHDMP_7_0(Etw):
    pattern = Struct(
        "ParentLastWriteGUID" / Guid,
        "ExpectedParentLastWriteGUID1" / Guid,
        "ExpectedParentLastWriteGUID2" / Guid,
        "VhdFileName" / WString
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=8, version=0)
class Microsoft_Windows_VHDMP_8_0(Etw):
    pattern = Struct(
        "VhdFileName" / WString,
        "CorruptionReason" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=9, version=0)
class Microsoft_Windows_VHDMP_9_0(Etw):
    pattern = Struct(
        "VhdFileName" / WString
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=10, version=0)
class Microsoft_Windows_VHDMP_10_0(Etw):
    pattern = Struct(
        "VhdFileName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=11, version=0)
class Microsoft_Windows_VHDMP_11_0(Etw):
    pattern = Struct(
        "VhdIoType" / Int32ul,
        "VhdFileName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=12, version=0)
class Microsoft_Windows_VHDMP_12_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "VhdFile" / WString,
        "VmId" / Guid,
        "VhdType" / Int32ul,
        "Version" / Int32ul,
        "Flags" / Int32ul,
        "AccessMask" / Int32ul,
        "WriteDepth" / Int32ul,
        "GetInfoOnly" / Int8ul,
        "ReadOnly" / Int8ul,
        "HandleContext" / Int64ul,
        "VirtualDisk" / Int64ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=13, version=0)
class Microsoft_Windows_VHDMP_13_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "VhdFile" / WString,
        "VmId" / Guid,
        "VhdType" / Int32ul,
        "Version" / Int32ul,
        "Flags" / Int32ul,
        "AccessMask" / Int32ul,
        "WriteDepth" / Int32ul,
        "GetInfoOnly" / Int8ul,
        "ReadOnly" / Int8ul,
        "HandleContext" / Int64ul,
        "VirtualDisk" / Int64ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=14, version=0)
class Microsoft_Windows_VHDMP_14_0(Etw):
    pattern = Struct(
        "HandleContext" / Int64ul,
        "VirtualDisk" / Int64ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=15, version=0)
class Microsoft_Windows_VHDMP_15_0(Etw):
    pattern = Struct(
        "VirtualDisk" / Int64ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=16, version=0)
class Microsoft_Windows_VHDMP_16_0(Etw):
    pattern = Struct(
        "VirtualDisk" / Int64ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=17, version=0)
class Microsoft_Windows_VHDMP_17_0(Etw):
    pattern = Struct(
        "VhdFileName" / WString,
        "VhdDiskNumber" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=18, version=0)
class Microsoft_Windows_VHDMP_18_0(Etw):
    pattern = Struct(
        "VhdFileName" / WString,
        "VhdDiskNumber" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=19, version=0)
class Microsoft_Windows_VHDMP_19_0(Etw):
    pattern = Struct(
        "VhdFileName" / WString,
        "VhdInstanceId" / Guid
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=20, version=0)
class Microsoft_Windows_VHDMP_20_0(Etw):
    pattern = Struct(
        "VhdFileName" / WString,
        "VhdInstanceId" / Guid
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=50, version=0)
class Microsoft_Windows_VHDMP_50_0(Etw):
    pattern = Struct(
        "VhdMetaOps" / CString,
        "VhdFileName" / WString,
        "TargetVhdFileName" / WString
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=51, version=0)
class Microsoft_Windows_VHDMP_51_0(Etw):
    pattern = Struct(
        "VhdMetaOps" / CString,
        "VhdFileName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=100, version=0)
class Microsoft_Windows_VHDMP_100_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid,
        "VhdIoType" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=101, version=0)
class Microsoft_Windows_VHDMP_101_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=102, version=0)
class Microsoft_Windows_VHDMP_102_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=110, version=0)
class Microsoft_Windows_VHDMP_110_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=111, version=0)
class Microsoft_Windows_VHDMP_111_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=112, version=0)
class Microsoft_Windows_VHDMP_112_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=113, version=0)
class Microsoft_Windows_VHDMP_113_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid,
        "Mode" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=114, version=0)
class Microsoft_Windows_VHDMP_114_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid,
        "Status" / Int32ul,
        "RefType" / Int32ul,
        "Mode" / Int32ul,
        "PendingRecoveryCount" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=115, version=0)
class Microsoft_Windows_VHDMP_115_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid,
        "Status" / Int32ul,
        "RefType" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=116, version=0)
class Microsoft_Windows_VHDMP_116_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid,
        "RefType" / Int32ul,
        "Mode" / Int32ul,
        "PendingRecoveryCount" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=117, version=0)
class Microsoft_Windows_VHDMP_117_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid,
        "Status" / Int32ul,
        "RefType" / Int32ul,
        "Mode" / Int32ul,
        "PendingRecoveryCount" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=118, version=0)
class Microsoft_Windows_VHDMP_118_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=119, version=0)
class Microsoft_Windows_VHDMP_119_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid,
        "Mode" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=120, version=0)
class Microsoft_Windows_VHDMP_120_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=121, version=0)
class Microsoft_Windows_VHDMP_121_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=122, version=0)
class Microsoft_Windows_VHDMP_122_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=123, version=0)
class Microsoft_Windows_VHDMP_123_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=124, version=0)
class Microsoft_Windows_VHDMP_124_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=125, version=0)
class Microsoft_Windows_VHDMP_125_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=126, version=0)
class Microsoft_Windows_VHDMP_126_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=208, version=0)
class Microsoft_Windows_VHDMP_208_0(Etw):
    pattern = Struct(
        "VhdFileName" / WString,
        "VirtualDisk" / Int64ul,
        "LogFileName" / WString
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=209, version=0)
class Microsoft_Windows_VHDMP_209_0(Etw):
    pattern = Struct(
        "VhdFileName" / WString,
        "VirtualDisk" / Int64ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=210, version=0)
class Microsoft_Windows_VHDMP_210_0(Etw):
    pattern = Struct(
        "VirtualDisk" / Int64ul,
        "LogFileName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=211, version=0)
class Microsoft_Windows_VHDMP_211_0(Etw):
    pattern = Struct(
        "LogFileName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=212, version=0)
class Microsoft_Windows_VHDMP_212_0(Etw):
    pattern = Struct(
        "LogFileName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=213, version=0)
class Microsoft_Windows_VHDMP_213_0(Etw):
    pattern = Struct(
        "LogFileName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=214, version=0)
class Microsoft_Windows_VHDMP_214_0(Etw):
    pattern = Struct(
        "LogFileName" / WString,
        "VhdFileName" / WString,
        "Status" / Int32ul,
        "VHDFileTime" / Int64ul,
        "LogFileTime" / Int64ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=1001, version=0)
class Microsoft_Windows_VHDMP_1001_0(Etw):
    pattern = Struct(
        "VhdId" / WString,
        "VhdIoType" / Int32ul,
        "VhdSrbType" / Int32ul,
        "Offset" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=1002, version=0)
class Microsoft_Windows_VHDMP_1002_0(Etw):
    pattern = Struct(
        "VhdId" / WString,
        "VhdIoType" / Int32ul,
        "VhdSrbType" / Int32ul,
        "Offset" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=1010, version=0)
class Microsoft_Windows_VHDMP_1010_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid,
        "VhdIoType" / Int32ul,
        "VhdSrbType" / Int32ul,
        "Offset" / Int64ul,
        "Length" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e2816346-87f4-4f85-95c3-0c79409aa89d"), event_id=1011, version=0)
class Microsoft_Windows_VHDMP_1011_0(Etw):
    pattern = Struct(
        "VhdFile" / WString,
        "VmId" / Guid,
        "VhdIoType" / Int32ul,
        "VhdSrbType" / Int32ul,
        "Offset" / Int64ul,
        "Length" / Int32ul,
        "Status" / Int32ul
    )

