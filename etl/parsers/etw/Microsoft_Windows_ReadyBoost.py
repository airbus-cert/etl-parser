# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ReadyBoost
GUID : e6307a09-292c-497e-aad6-498f68e2b619
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1000, version=0)
class Microsoft_Windows_ReadyBoost_1000_0(Etw):
    pattern = Struct(
        "DeviceName" / WString,
        "FreeSpace" / Int32ul,
        "ReadRate" / Int32ul,
        "WriteRate" / Int32ul
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1002, version=0)
class Microsoft_Windows_ReadyBoost_1002_0(Etw):
    pattern = Struct(
        "DeviceName" / WString
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1003, version=0)
class Microsoft_Windows_ReadyBoost_1003_0(Etw):
    pattern = Struct(
        "DeviceName" / WString,
        "IntValue" / Int32ul
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1003, version=1)
class Microsoft_Windows_ReadyBoost_1003_1(Etw):
    pattern = Struct(
        "DeviceName" / WString,
        "IntValue" / Int32ul,
        "SecondIntValue" / Int32ul
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1004, version=0)
class Microsoft_Windows_ReadyBoost_1004_0(Etw):
    pattern = Struct(
        "DeviceName" / WString,
        "IORate" / Int32ul
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1005, version=0)
class Microsoft_Windows_ReadyBoost_1005_0(Etw):
    pattern = Struct(
        "DeviceName" / WString,
        "IORate" / Int32ul
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1006, version=0)
class Microsoft_Windows_ReadyBoost_1006_0(Etw):
    pattern = Struct(
        "DeviceName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1007, version=0)
class Microsoft_Windows_ReadyBoost_1007_0(Etw):
    pattern = Struct(
        "DeviceName" / WString,
        "StringLabel" / WString
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1007, version=1)
class Microsoft_Windows_ReadyBoost_1007_1(Etw):
    pattern = Struct(
        "DeviceName" / WString
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1008, version=0)
class Microsoft_Windows_ReadyBoost_1008_0(Etw):
    pattern = Struct(
        "DeviceName" / WString,
        "IntValue" / Int32ul
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1009, version=0)
class Microsoft_Windows_ReadyBoost_1009_0(Etw):
    pattern = Struct(
        "DeviceName" / WString,
        "IntValue" / Int32ul,
        "SecondIntValue" / Int32ul
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1010, version=0)
class Microsoft_Windows_ReadyBoost_1010_0(Etw):
    pattern = Struct(
        "DeviceName" / WString,
        "IntValue" / Int32ul
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1011, version=0)
class Microsoft_Windows_ReadyBoost_1011_0(Etw):
    pattern = Struct(
        "DeviceName" / WString
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1012, version=0)
class Microsoft_Windows_ReadyBoost_1012_0(Etw):
    pattern = Struct(
        "DeviceName" / WString,
        "StringLabel" / WString
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1013, version=0)
class Microsoft_Windows_ReadyBoost_1013_0(Etw):
    pattern = Struct(
        "DeviceName" / WString
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1014, version=0)
class Microsoft_Windows_ReadyBoost_1014_0(Etw):
    pattern = Struct(
        "DeviceName" / WString
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1015, version=0)
class Microsoft_Windows_ReadyBoost_1015_0(Etw):
    pattern = Struct(
        "RB_BootTimeUTC" / Int64ul,
        "RB_LastBootPlanUTC" / Int64ul,
        "RB_IoReadKB" / Int64ul,
        "RB_CacheHitKB" / Int64ul,
        "RB_CompressedDataSizeKB" / Int64ul,
        "RB_RawDataSizeKB" / Int64ul,
        "RB_BootPrefetchDiskTimeUs" / Int64sl,
        "RB_BootPrefetchDataReadBytes" / Int64sl,
        "RB_CacheHitPercentage" / Double,
        "RB_CacheFragmentation" / Double,
        "RB_CompressionRatio" / Double,
        "RB_IoReadCount" / Int32ul,
        "RB_CacheHitCount" / Int32ul,
        "RB_CacheSizeKB" / Int32ul,
        "RB_LastBootPlanUserTimeLength" / Int32ul,
        "RB_LastBootPlanUserTime" / Bytes(lambda this: this.RB_LastBootPlanUserTimeLength)
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1015, version=1)
class Microsoft_Windows_ReadyBoost_1015_1(Etw):
    pattern = Struct(
        "RB_IoReadBytes" / Int64ul,
        "RB_CacheHitBytes" / Int64ul,
        "RB_PrefetchBytes" / Int64ul,
        "RB_CacheHitPercentage" / Double,
        "RB_IoReadCount" / Int32ul,
        "RB_CacheHitCount" / Int32ul,
        "RB_PrefetchReadCount" / Int32ul,
        "RB_PrefetchDiskTimeUs" / Int32ul
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1015, version=2)
class Microsoft_Windows_ReadyBoost_1015_2(Etw):
    pattern = Struct(
        "RB_IoReadBytes" / Int64ul,
        "RB_CacheHitBytes" / Int64ul,
        "RB_PrefetchBytes" / Int64ul,
        "RB_CacheHitPercentage" / Double,
        "RB_IoReadCount" / Int32ul,
        "RB_CacheHitCount" / Int32ul,
        "RB_PrefetchReadCount" / Int32ul,
        "RB_PrefetchDiskTimeUs" / Int32ul,
        "RB_SyncPrefetchIoBytes" / Int64ul,
        "RB_SyncPrefetchIoCount" / Int32ul,
        "RB_SyncPhaseDurationUs" / Int32ul,
        "RB_PostSyncPhasePendCount" / Int32ul,
        "RB_Flags" / Int32ul
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1016, version=0)
class Microsoft_Windows_ReadyBoost_1016_0(Etw):
    pattern = Struct(
        "BootPlanTimestamp" / Int64ul,
        "ValidBootPlan" / Int8ul
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1016, version=1)
class Microsoft_Windows_ReadyBoost_1016_1(Etw):
    pattern = Struct(
        "BootPlanTimestamp" / Int64ul,
        "ErrorCode" / Int32ul,
        "Durationms" / Int16ul,
        "Reason" / Int8ul
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1017, version=0)
class Microsoft_Windows_ReadyBoost_1017_0(Etw):
    pattern = Struct(
        "DefragCompletionTimestamp" / Int64ul
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1017, version=1)
class Microsoft_Windows_ReadyBoost_1017_1(Etw):
    pattern = Struct(
        "DeviceName" / WString
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1018, version=0)
class Microsoft_Windows_ReadyBoost_1018_0(Etw):
    pattern = Struct(
        "DiskAssessmentTimestamp" / Int64ul,
        "Success" / Int8ul
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1018, version=1)
class Microsoft_Windows_ReadyBoost_1018_1(Etw):
    pattern = Struct(
        "DiskAssessmentTimestamp" / Int64ul,
        "ErrorCode" / Int32ul,
        "Durationms" / Int16ul
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1019, version=1)
class Microsoft_Windows_ReadyBoost_1019_1(Etw):
    pattern = Struct(
        "DeviceName" / WString
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1020, version=1)
class Microsoft_Windows_ReadyBoost_1020_1(Etw):
    pattern = Struct(
        "DeviceName" / WString
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1021, version=1)
class Microsoft_Windows_ReadyBoost_1021_1(Etw):
    pattern = Struct(
        "DeviceName" / WString
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1022, version=1)
class Microsoft_Windows_ReadyBoost_1022_1(Etw):
    pattern = Struct(
        "DeviceName" / WString
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1023, version=1)
class Microsoft_Windows_ReadyBoost_1023_1(Etw):
    pattern = Struct(
        "DeviceName" / WString
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1024, version=1)
class Microsoft_Windows_ReadyBoost_1024_1(Etw):
    pattern = Struct(
        "RB_HistoryCount" / Int32ul,
        "RB_BootPlanAge" / Int32ul,
        "RB_DiskAssessmentRPM" / Int32ul
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1024, version=2)
class Microsoft_Windows_ReadyBoost_1024_2(Etw):
    pattern = Struct(
        "RB_HistoryCount" / Int32ul,
        "RB_BootPlanAge" / Int32ul,
        "RB_DiskAssessmentRPM" / Int32ul,
        "RB_Flags" / Int32ul
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1025, version=1)
class Microsoft_Windows_ReadyBoost_1025_1(Etw):
    pattern = Struct(
        "DeviceName" / WString
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1026, version=1)
class Microsoft_Windows_ReadyBoost_1026_1(Etw):
    pattern = Struct(
        "VolumeUniqueId" / WString,
        "OldRdbAttachState" / Int16ul,
        "NewRdbAttachState" / Int16ul,
        "OldHbdrvAttachState" / Int16ul,
        "NewHbdrvAttachState" / Int16ul,
        "VolumePath" / WString
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1027, version=1)
class Microsoft_Windows_ReadyBoost_1027_1(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "UniqueIdLength" / Int32ul,
        "VolumeUniqueId" / Bytes(lambda this: this.UniqueIdLength)
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1028, version=1)
class Microsoft_Windows_ReadyBoost_1028_1(Etw):
    pattern = Struct(
        "DiskNumber" / Int32ul
    )


@declare(guid=guid("e6307a09-292c-497e-aad6-498f68e2b619"), event_id=1029, version=1)
class Microsoft_Windows_ReadyBoost_1029_1(Etw):
    pattern = Struct(
        "HbdrvSpeedTestResult" / Int32ul,
        "DiskSeqReadKbps" / Int32ul,
        "DiskSeqWriteKbps" / Int32ul,
        "FlashSeqReadKbps" / Int32ul,
        "FlashSeqWriteKbps" / Int32ul,
        "FlashRndReadKbps" / Int32ul,
        "ErrorCode" / Int32ul
    )

