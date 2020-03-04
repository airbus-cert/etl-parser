# -*- coding: utf-8 -*-
"""
Microsoft-Windows-VolumeSnapshot-Driver
GUID : 67fe2216-727a-40cb-94b2-c02211edb34a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=0, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_0_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "SnapshotGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=2, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_2_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=3, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_3_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=4, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_4_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "SnapshotGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=5, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_5_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "SnapshotGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=6, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_6_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=7, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_7_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=8, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_8_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=9, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_9_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=10, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_10_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "SnapshotGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=11, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_11_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "SnapshotGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=12, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_12_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "SnapshotGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=13, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_13_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "SnapshotGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=14, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_14_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=15, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_15_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=16, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_16_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=17, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_17_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=18, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_18_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=19, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_19_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=20, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_20_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=21, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_21_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=22, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_22_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=23, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_23_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=24, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_24_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=25, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_25_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=26, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_26_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=27, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_27_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=28, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_28_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=29, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_29_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=30, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_30_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=31, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_31_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=32, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_32_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=33, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_33_0(Etw):
    pattern = Struct(
        "RealThreadID" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=100, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_100_0(Etw):
    pattern = Struct(
        "TargetVolumeGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=101, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_101_0(Etw):
    pattern = Struct(
        "TargetVolumeGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=102, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_102_0(Etw):
    pattern = Struct(
        "TargetVolumeGuid" / Guid,
        "Error" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=103, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_103_0(Etw):
    pattern = Struct(
        "TargetVolumeGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=104, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_104_0(Etw):
    pattern = Struct(
        "TargetVolumeGuid" / Guid,
        "SnapshotCount" / Int32ul,
        "CountDeleted" / Int32ul,
        "CountVisible" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=105, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_105_0(Etw):
    pattern = Struct(
        "TargetVolumeGuid" / Guid,
        "Error" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=106, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_106_0(Etw):
    pattern = Struct(
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "Deleted" / Int8ul,
        "Visible" / Int8ul,
        "CommitTime" / SystemTime,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=107, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_107_0(Etw):
    pattern = Struct(
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=110, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_110_0(Etw):
    pattern = Struct(
        "TargetVolumeGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=111, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_111_0(Etw):
    pattern = Struct(
        "TargetVolumeGuid" / Guid,
        "DiffAreaCount" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=112, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_112_0(Etw):
    pattern = Struct(
        "TargetVolumeGuid" / Guid,
        "Error" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=113, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_113_0(Etw):
    pattern = Struct(
        "TargetVolumeGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=114, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_114_0(Etw):
    pattern = Struct(
        "TargetVolumeGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=115, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_115_0(Etw):
    pattern = Struct(
        "TargetVolumeGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=116, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_116_0(Etw):
    pattern = Struct(
        "TargetVolumeGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=117, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_117_0(Etw):
    pattern = Struct(
        "TargetVolumeGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=118, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_118_0(Etw):
    pattern = Struct(
        "TargetVolumeGuid" / Guid,
        "Error" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=119, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_119_0(Etw):
    pattern = Struct(
        "TargetVolumeGuid" / Guid,
        "PersistentDeleteReason" / Int16ul,
        "PersistentDeleteStatus" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=120, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_120_0(Etw):
    pattern = Struct(
        "TargetVolumeGuid" / Guid,
        "TimeoutInSeconds" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=121, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_121_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "DiffVolumeNameLength" / Int16ul,
        "DiffVolumeName" / Bytes(lambda this: this.DiffVolumeNameLength),
        "OriginalErrorLogCode" / Int32ul,
        "OriginalErrorStatus" / Int32ul,
        "OriginalSourceFile" / Int32ul,
        "OriginalSourceLine" / Int16ul,
        "OriginalSourceTag" / Int32ul,
        "ErrorStatus" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=122, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_122_0(Etw):
    pattern = Struct(
        "TargetVolumeGuid" / Guid,
        "Error" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1000, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1000_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1001, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1001_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "ExitStatus" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1002, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1002_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1003, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1003_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "ExitStatus" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1004, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1004_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1005, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1005_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "ExitStatus" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1006, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1006_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1007, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1007_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "ExitStatus" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1008, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1008_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1009, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1009_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "ExitStatus" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1010, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1010_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1011, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1011_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "ExitStatus" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1012, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1012_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1013, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1013_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "ExitStatus" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1014, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1014_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1015, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1015_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "ExitStatus" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1016, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1016_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1017, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1017_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "ExitStatus" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1018, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1018_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1019, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1019_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "ExitStatus" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1020, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1020_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1021, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1021_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "ExitStatus" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1022, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1022_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1023, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1023_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "ExitStatus" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1024, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1024_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1025, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1025_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "ExitStatus" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1026, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1026_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1027, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1027_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "ExitStatus" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1028, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1028_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1029, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1029_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "ExitStatus" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1030, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1030_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1031, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1031_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "ExitStatus" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1032, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1032_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("67fe2216-727a-40cb-94b2-c02211edb34a"), event_id=1033, version=0)
class Microsoft_Windows_VolumeSnapshot_Driver_1033_0(Etw):
    pattern = Struct(
        "DiagPrefixLength" / Int16ul,
        "DiagPrefix" / Bytes(lambda this: this.DiagPrefixLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "TargetVolumeGuid" / Guid,
        "SnapshotGuid" / Guid,
        "ExitStatus" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )

