# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ReFS
GUID : cd9c6198-bf73-4106-803b-c17d26559018
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=4, version=0)
class Microsoft_Windows_ReFS_4_0(Etw):
    pattern = Struct(
        "Vcb" / Int64ul,
        "DeviceNameLength" / Int16ul,
        "DeviceName" / Bytes(lambda this: this.DeviceNameLength),
        "VolumeGuid" / Guid,
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "VolumeLabelLength" / Int16ul,
        "VolumeLabel" / Bytes(lambda this: this.VolumeNameLength)
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=5, version=0)
class Microsoft_Windows_ReFS_5_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "Status" / Int32ul,
        "VolumeGuid" / Guid,
        "DeviceNameLength" / Int16ul,
        "DeviceName" / Bytes(lambda this: this.DeviceNameLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "StackCount" / Int32ul,
        "Stack" / Int64ul,
        "SourceLine" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=6, version=0)
class Microsoft_Windows_ReFS_6_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "Progress" / Int32ul,
        "StackCount" / Int32ul,
        "Stack" / Int64ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=7, version=0)
class Microsoft_Windows_ReFS_7_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "MajorVersionExpected" / Int8ul,
        "MinorVersionExpected" / Int8ul,
        "MajorVersionOnDisk" / Int8ul,
        "MinorVersionOnDisk" / Int8ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=8, version=0)
class Microsoft_Windows_ReFS_8_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "FillRatio" / Int32ul,
        "VolumeGuid" / Guid,
        "DeviceNameLength" / Int16ul,
        "DeviceName" / Bytes(lambda this: this.DeviceNameLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength)
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=130, version=0)
class Microsoft_Windows_ReFS_130_0(Etw):
    pattern = Struct(
        "VolumeIdLength" / Int16ul,
        "VolumeId" / Bytes(lambda this: this.VolumeIdLength),
        "RepairDetail" / WString,
        "RepairDataLength" / Int16ul,
        "RepairData" / Bytes(lambda this: this.RepairDataLength)
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=131, version=0)
class Microsoft_Windows_ReFS_131_0(Etw):
    pattern = Struct(
        "VolumeIdLength" / Int16ul,
        "VolumeId" / Bytes(lambda this: this.VolumeIdLength),
        "FailureReason" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=132, version=0)
class Microsoft_Windows_ReFS_132_0(Etw):
    pattern = Struct(
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=133, version=0)
class Microsoft_Windows_ReFS_133_0(Etw):
    pattern = Struct(
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=134, version=0)
class Microsoft_Windows_ReFS_134_0(Etw):
    pattern = Struct(
        "VolumeIdLength" / Int16ul,
        "VolumeId" / Bytes(lambda this: this.VolumeIdLength),
        "FailureReason" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=135, version=0)
class Microsoft_Windows_ReFS_135_0(Etw):
    pattern = Struct(
        "VolumeIdLength" / Int16ul,
        "VolumeId" / Bytes(lambda this: this.VolumeIdLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=136, version=0)
class Microsoft_Windows_ReFS_136_0(Etw):
    pattern = Struct(
        "VolumeIdLength" / Int16ul,
        "VolumeId" / Bytes(lambda this: this.VolumeIdLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=137, version=0)
class Microsoft_Windows_ReFS_137_0(Etw):
    pattern = Struct(
        "VolumeIdLength" / Int16ul,
        "VolumeId" / Bytes(lambda this: this.VolumeIdLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=138, version=0)
class Microsoft_Windows_ReFS_138_0(Etw):
    pattern = Struct(
        "VolumeIdLength" / Int16ul,
        "VolumeId" / Bytes(lambda this: this.VolumeIdLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=139, version=0)
class Microsoft_Windows_ReFS_139_0(Etw):
    pattern = Struct(
        "VolumeIdLength" / Int16ul,
        "VolumeId" / Bytes(lambda this: this.VolumeIdLength),
        "FailureReason" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=140, version=0)
class Microsoft_Windows_ReFS_140_0(Etw):
    pattern = Struct(
        "VolumeIdLength" / Int16ul,
        "VolumeId" / Bytes(lambda this: this.VolumeIdLength),
        "FailureReason" / Int32ul,
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=145, version=2)
class Microsoft_Windows_ReFS_145_2(Etw):
    pattern = Struct(
        "VolumeCorrelationId" / Guid,
        "VolumeNameLength" / Int32ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "IsBootVolume" / Int8ul,
        "TierIndex" / Int32ul,
        "MaxLatencyMs" / Int64ul,
        "ReadWriteLatencyBucket1" / Int64sl,
        "ReadWriteLatencyBucket2" / Int64sl,
        "ReadWriteLatencyBucket3" / Int64sl,
        "ReadWriteLatencyBucket4" / Int64sl,
        "ReadWriteLatencyBucket5" / Int64sl,
        "ReadWriteLatencyBucket6" / Int64sl,
        "ReadWriteLatencyBucket7" / Int64sl,
        "TrimLatencyBucket1" / Int64sl,
        "TrimLatencyBucket2" / Int64sl,
        "TrimLatencyBucket3" / Int64sl,
        "TrimLatencyBucket4" / Int64sl,
        "TrimLatencyBucket5" / Int64sl,
        "TrimLatencyBucket6" / Int64sl,
        "TrimLatencyBucket7" / Int64sl,
        "FlushLatencyBucket1" / Int64sl,
        "FlushLatencyBucket2" / Int64sl,
        "FlushLatencyBucket3" / Int64sl,
        "FlushLatencyBucket4" / Int64sl,
        "FlushLatencyBucket5" / Int64sl,
        "FlushLatencyBucket6" / Int64sl,
        "FlushLatencyBucket7" / Int64sl
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=146, version=2)
class Microsoft_Windows_ReFS_146_2(Etw):
    pattern = Struct(
        "Version" / Int32ul,
        "VolumeCorrelationId" / Guid,
        "VolumeNameLength" / Int32ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "IsBootVolume" / Int8ul,
        "TierIndex" / Int32ul,
        "MaxLatencyMs" / Int64ul,
        "ReadWriteLatencyBucket1" / Int64sl,
        "ReadWriteLatencyBucket2" / Int64sl,
        "ReadWriteLatencyBucket3" / Int64sl,
        "ReadWriteLatencyBucket4" / Int64sl,
        "ReadWriteLatencyBucket5" / Int64sl,
        "ReadWriteLatencyBucket6" / Int64sl,
        "ReadWriteLatencyBucket7" / Int64sl,
        "TrimLatencyBucket1" / Int64sl,
        "TrimLatencyBucket2" / Int64sl,
        "TrimLatencyBucket3" / Int64sl,
        "TrimLatencyBucket4" / Int64sl,
        "TrimLatencyBucket5" / Int64sl,
        "TrimLatencyBucket6" / Int64sl,
        "TrimLatencyBucket7" / Int64sl,
        "FlushLatencyBucket1" / Int64sl,
        "FlushLatencyBucket2" / Int64sl,
        "FlushLatencyBucket3" / Int64sl,
        "FlushLatencyBucket4" / Int64sl,
        "FlushLatencyBucket5" / Int64sl,
        "FlushLatencyBucket6" / Int64sl,
        "FlushLatencyBucket7" / Int64sl,
        "HighIoLatencyCount" / Int32ul,
        "IntervalDurationUs" / Int64sl,
        "NCReadIOCount" / Int64ul,
        "NCReadTotalBytes" / Int64ul,
        "NCReadAvgLatencyNs" / Int64ul,
        "NCWriteIOCount" / Int64ul,
        "NCWriteTotalBytes" / Int64ul,
        "NCWriteAvgLatencyNs" / Int64ul,
        "FileFlushCount" / Int64ul,
        "FileFlushAvgLatencyNs" / Int64ul,
        "DirectoryFlushCount" / Int64ul,
        "DirectoryFlushAvgLatencyNs" / Int64ul,
        "VolumeFlushCount" / Int64ul,
        "VolumeFlushAvgLatencyNs" / Int64ul,
        "FileLevelTrimCount" / Int64ul,
        "FileLevelTrimTotalBytes" / Int64ul,
        "FileLevelTrimExtentsCount" / Int64ul,
        "FileLevelTrimAvgLatencyNs" / Int64ul,
        "VolumeTrimCount" / Int64ul,
        "VolumeTrimTotalBytes" / Int64ul,
        "VolumeTrimExtentsCount" / Int64ul,
        "VolumeTrimAvgLatencyNs" / Int64ul,
        "IoBucketsCount" / Int8ul,
        "TotalBytesBucketsCount" / Int8ul,
        "ExtentsBucketsCount" / Int8ul,
        "IoCount" / Int64ul,
        "TotalLatencyUs" / Int64ul,
        "TotalBytes" / Int64ul,
        "TrimExtentsCount" / Int64ul,
        "IoTypeIndex" / Int16ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=147, version=1)
class Microsoft_Windows_ReFS_147_1(Etw):
    pattern = Struct(
        "VolumeCorrelationId" / Guid,
        "VolumeNameLength" / Int32ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "IsBootVolume" / Int8ul,
        "TierIndex" / Int32ul,
        "MaxLatencyMs" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessName" / CString,
        "FileNameLength" / Int32ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "IoType" / Int32ul,
        "IoSize" / Int32ul,
        "FileOffset" / Int64ul,
        "LatencyMs" / Int64ul,
        "StartingLcn" / Int64ul,
        "ClustersCount" / Int32ul,
        "TableIndex" / Int32sl
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=148, version=0)
class Microsoft_Windows_ReFS_148_0(Etw):
    pattern = Struct(
        "VolumeCorrelationId" / Guid,
        "VolumeNameLength" / Int32ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "IsBootVolume" / Int8ul,
        "TierIndex" / Int32ul,
        "ProcessId" / Int32ul,
        "ProcessName" / CString,
        "FileNameLength" / Int32ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "IoType" / Int32ul,
        "IoSize" / Int32ul,
        "FileOffset" / Int64ul,
        "StartingLcn" / Int64ul,
        "ClustersCount" / Int32ul,
        "FailureStatus" / Int32ul,
        "TableIndex" / Int32sl
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=149, version=0)
class Microsoft_Windows_ReFS_149_0(Etw):
    pattern = Struct(
        "VolumeCorrelationId" / Guid,
        "VolumeNameLength" / Int32ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "IsBootVolume" / Int8ul,
        "SecondsElapsed" / Int32ul,
        "HighLatencyCount" / Int32ul,
        "FailedWriteCount" / Int32ul,
        "FailedReadCount" / Int32ul,
        "BadClusterHotfixCount" / Int32ul,
        "ValuesCount" / Int32ul,
        "HighLatencyArray" / Int32ul,
        "FailedWriteArray" / Int32ul,
        "FailedReadArray" / Int32ul,
        "BadClusterHotfixArray" / Int32ul,
        "StatusArray" / Int32ul,
        "TableIndexArray" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=150, version=1)
class Microsoft_Windows_ReFS_150_1(Etw):
    pattern = Struct(
        "VolumeCorrelationId" / Guid,
        "VolumeNameLength" / Int32ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "SampleDuration" / Int64ul,
        "FreeSpaceInRandomlyWriteableTierMin" / Int64ul,
        "FreeSpaceInRandomlyWriteableTierMax" / Int64ul,
        "FreeSpaceInRandomlyWriteableTierAvg" / Int64ul,
        "FreeSpaceInSMRTierMin" / Int64ul,
        "FreeSpaceInSMRTierMax" / Int64ul,
        "FreeSpaceInSMRTierAvg" / Int64ul,
        "UsableFreeSpaceInSMRTierMin" / Int64ul,
        "UsableFreeSpaceInSMRTierMax" / Int64ul,
        "UsableFreeSpaceInSMRTierAvg" / Int64ul,
        "WriteSerializationAbortedWrites" / Int64ul,
        "WriteSerializationEvents" / Int64ul,
        "WriteSerializationLatencyAvg" / Int64ul,
        "WriteSerializationLatencyMax" / Int64ul,
        "WriteSerializationBlockedEvents" / Int64ul,
        "WriteSerializationBlockedLatencyAvg" / Int64ul,
        "StartGCCallsInvoked" / Int64ul,
        "StartGCCallsFailed" / Int64ul,
        "StartGCFullSpeedCallsInvoked" / Int64ul,
        "StartGCFullSpeedCallsFailed" / Int64ul,
        "PauseGCCallsInvoked" / Int64ul,
        "PauseGCCallsFailed" / Int64ul,
        "StopGCCallsInvoked" / Int64ul,
        "StopGCCallsFailed" / Int64ul,
        "FullSMRBandClusterAllocations" / Int64ul,
        "SharedSMRBandClusterAllocations" / Int64ul,
        "GCReadLatencyTotal" / Int64ul,
        "GCReadLatencyAvg" / Int64ul,
        "GCReadLatencyMax" / Int64ul,
        "GCTotalReadIOs" / Int64ul,
        "GCWriteLatencyTotal" / Int64ul,
        "GCWriteLatencyAvg" / Int64ul,
        "GCWriteLatencyMax" / Int64ul,
        "GCTotalWriteIOs" / Int64ul,
        "DiskFullRequiresGC" / Int64ul,
        "SMRZoneFull" / Int64ul,
        "CMRZoneFull" / Int64ul,
        "InvalidSectorErrors" / Int64ul,
        "IoDeviceErrors" / Int64ul,
        "WriteErrors" / Int64ul,
        "ReadErrors" / Int64ul,
        "SMRWriteHeadRequeries" / Int64ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=237, version=0)
class Microsoft_Windows_ReFS_237_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=238, version=0)
class Microsoft_Windows_ReFS_238_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmStringDatapointValue" / WString
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=272, version=0)
class Microsoft_Windows_ReFS_272_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmProcessHashValue" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=273, version=0)
class Microsoft_Windows_ReFS_273_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmProcessHashValue" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamEntriesSize" / Int32ul,
        "SqmStreamEntries" / Bytes(lambda this: this.SqmStreamEntriesSize),
        "SqmStreamFlags" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=274, version=0)
class Microsoft_Windows_ReFS_274_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORD64DatapointValue" / Int64ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=513, version=0)
class Microsoft_Windows_ReFS_513_0(Etw):
    pattern = Struct(
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=514, version=0)
class Microsoft_Windows_ReFS_514_0(Etw):
    pattern = Struct(
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=515, version=0)
class Microsoft_Windows_ReFS_515_0(Etw):
    pattern = Struct(
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=516, version=0)
class Microsoft_Windows_ReFS_516_0(Etw):
    pattern = Struct(
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=517, version=0)
class Microsoft_Windows_ReFS_517_0(Etw):
    pattern = Struct(
        "VolumeIdLength" / Int16ul,
        "VolumeId" / Bytes(lambda this: this.VolumeIdLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=518, version=0)
class Microsoft_Windows_ReFS_518_0(Etw):
    pattern = Struct(
        "VolumeIdLength" / Int16ul,
        "VolumeId" / Bytes(lambda this: this.VolumeIdLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=519, version=0)
class Microsoft_Windows_ReFS_519_0(Etw):
    pattern = Struct(
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=520, version=0)
class Microsoft_Windows_ReFS_520_0(Etw):
    pattern = Struct(
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=521, version=0)
class Microsoft_Windows_ReFS_521_0(Etw):
    pattern = Struct(
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("cd9c6198-bf73-4106-803b-c17d26559018"), event_id=522, version=0)
class Microsoft_Windows_ReFS_522_0(Etw):
    pattern = Struct(
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "FailureReason" / Int32ul
    )

