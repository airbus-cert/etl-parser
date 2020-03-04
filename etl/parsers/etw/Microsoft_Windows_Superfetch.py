# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Superfetch
GUID : 99806515-9f51-4c2f-b918-1eae407aa8cb
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1000, version=1)
class Microsoft_Windows_Superfetch_1000_1(Etw):
    pattern = Struct(
        "StoreBitmap" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1001, version=1)
class Microsoft_Windows_Superfetch_1001_1(Etw):
    pattern = Struct(
        "StoreBitmap" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1002, version=1)
class Microsoft_Windows_Superfetch_1002_1(Etw):
    pattern = Struct(
        "StoreId" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1003, version=1)
class Microsoft_Windows_Superfetch_1003_1(Etw):
    pattern = Struct(
        "StoreId" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1004, version=1)
class Microsoft_Windows_Superfetch_1004_1(Etw):
    pattern = Struct(
        "StoreId" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1005, version=1)
class Microsoft_Windows_Superfetch_1005_1(Etw):
    pattern = Struct(
        "StoreId" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1006, version=1)
class Microsoft_Windows_Superfetch_1006_1(Etw):
    pattern = Struct(
        "StoreId" / Int32ul,
        "PageCount" / Int32ul,
        "ScoreLevel" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1007, version=1)
class Microsoft_Windows_Superfetch_1007_1(Etw):
    pattern = Struct(
        "StoreId" / Int32ul,
        "PageCount" / Int32ul,
        "ScoreLevel" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1008, version=1)
class Microsoft_Windows_Superfetch_1008_1(Etw):
    pattern = Struct(
        "ContainerKey" / Int64ul,
        "VirtualAddress" / Int64ul,
        "Flags" / Int32ul,
        "InterpretedPid" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1009, version=1)
class Microsoft_Windows_Superfetch_1009_1(Etw):
    pattern = Struct(
        "ContainerKey" / Int64ul,
        "VirtualAddress" / Int64ul,
        "Flags" / Int32ul,
        "InterpretedPid" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1011, version=1)
class Microsoft_Windows_Superfetch_1011_1(Etw):
    pattern = Struct(
        "StoreBitmap" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1012, version=1)
class Microsoft_Windows_Superfetch_1012_1(Etw):
    pattern = Struct(
        "StoreBitmap" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1013, version=2)
class Microsoft_Windows_Superfetch_1013_2(Etw):
    pattern = Struct(
        "Private" / Int32ul,
        "TotalPrivate" / Int32ul,
        "Total" / Int32ul,
        "ProcessName" / WString
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1014, version=1)
class Microsoft_Windows_Superfetch_1014_1(Etw):
    pattern = Struct(
        "AllocPages" / Int32ul,
        "AllocCount" / Int32ul,
        "FreeCount" / Int32ul,
        "Tag" / CString
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1015, version=1)
class Microsoft_Windows_Superfetch_1015_1(Etw):
    pattern = Struct(
        "AllocPages" / Int32ul,
        "AllocCount" / Int32ul,
        "FreeCount" / Int32ul,
        "Tag" / CString
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1016, version=1)
class Microsoft_Windows_Superfetch_1016_1(Etw):
    pattern = Struct(
        "InUse" / Int32ul,
        "Free" / Int32ul,
        "Available" / Int32ul,
        "Cached" / Int32ul,
        "PagedPool" / Int32ul,
        "NonPagedPool" / Int32ul,
        "Commit" / Int32ul,
        "CommitLimit" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1017, version=1)
class Microsoft_Windows_Superfetch_1017_1(Etw):
    pattern = Struct(
        "AllocPages" / Int32ul,
        "AllocCount" / Int32ul,
        "FreeCount" / Int32ul,
        "Tag" / CString
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1018, version=1)
class Microsoft_Windows_Superfetch_1018_1(Etw):
    pattern = Struct(
        "AllocPages" / Int32ul,
        "AllocCount" / Int32ul,
        "FreeCount" / Int32ul,
        "Tag" / CString
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1019, version=1)
class Microsoft_Windows_Superfetch_1019_1(Etw):
    pattern = Struct(
        "Fragmentation" / Int32ul,
        "AllocPages" / Int32ul,
        "CommitPages" / Int32ul,
        "ActivePages" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1020, version=1)
class Microsoft_Windows_Superfetch_1020_1(Etw):
    pattern = Struct(
        "Fragmentation" / Int32ul,
        "AllocPages" / Int32ul,
        "CommitPages" / Int32ul,
        "ActivePages" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1021, version=1)
class Microsoft_Windows_Superfetch_1021_1(Etw):
    pattern = Struct(
        "Fragmentation" / Int32ul,
        "AllocPages" / Int32ul,
        "CommitPages" / Int32ul,
        "ActivePages" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1038, version=1)
class Microsoft_Windows_Superfetch_1038_1(Etw):
    pattern = Struct(
        "Processes" / Int32ul,
        "Handles" / Int32ul,
        "Objects" / Int32ul,
        "Threads" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1039, version=1)
class Microsoft_Windows_Superfetch_1039_1(Etw):
    pattern = Struct(
        "AppKey" / Int32ul,
        "PredictionPurpose" / Int32ul,
        "Probability" / Double
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1041, version=2)
class Microsoft_Windows_Superfetch_1041_2(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1042, version=1)
class Microsoft_Windows_Superfetch_1042_1(Etw):
    pattern = Struct(
        "AppKey" / Int32ul,
        "AUMID" / WString
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1043, version=1)
class Microsoft_Windows_Superfetch_1043_1(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "AUMID" / WString
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1044, version=1)
class Microsoft_Windows_Superfetch_1044_1(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1045, version=1)
class Microsoft_Windows_Superfetch_1045_1(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "AUMID" / WString
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1046, version=1)
class Microsoft_Windows_Superfetch_1046_1(Etw):
    pattern = Struct(
        "SecondsSpentInQueue" / Int32ul,
        "AUMID" / WString,
        "Reason" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1048, version=2)
class Microsoft_Windows_Superfetch_1048_2(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1049, version=1)
class Microsoft_Windows_Superfetch_1049_1(Etw):
    pattern = Struct(
        "CommandCode" / Int32ul,
        "AUMID" / WString
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1050, version=1)
class Microsoft_Windows_Superfetch_1050_1(Etw):
    pattern = Struct(
        "CPUUtilization" / Int32ul,
        "DiskUtilization" / Int32ul,
        "GPUUtilization" / Int32ul,
        "AvailableMemory" / Int32ul,
        "ModifiedMemory" / Int32ul,
        "OkToPrelaunch" / Int8ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1051, version=0)
class Microsoft_Windows_Superfetch_1051_0(Etw):
    pattern = Struct(
        "PrivateWS" / Int32ul,
        "TotalPrivate" / Int32ul,
        "TotalWS" / Int32ul,
        "ProcessAgeMHiandAppStateLo" / Int32ul,
        "ProcessName" / WString
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1052, version=1)
class Microsoft_Windows_Superfetch_1052_1(Etw):
    pattern = Struct(
        "BgTaskCountUnrestricted" / Int8ul,
        "BgTaskCountACOnly" / Int8ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1053, version=2)
class Microsoft_Windows_Superfetch_1053_2(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1054, version=1)
class Microsoft_Windows_Superfetch_1054_1(Etw):
    pattern = Struct(
        "AppKey" / Int32ul,
        "FullPackageName" / WString,
        "LongLookahead" / Int8ul,
        "BenefitScore" / Int16sl
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1055, version=1)
class Microsoft_Windows_Superfetch_1055_1(Etw):
    pattern = Struct(
        "AppKey" / Int32ul,
        "FullPackageName" / WString,
        "UsedConditions" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1055, version=2)
class Microsoft_Windows_Superfetch_1055_2(Etw):
    pattern = Struct(
        "AppKey" / Int32ul,
        "FullPackageName" / WString
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1056, version=1)
class Microsoft_Windows_Superfetch_1056_1(Etw):
    pattern = Struct(
        "AppNameKey" / Int32ul,
        "AUMID" / WString,
        "NewFailCount" / Int8ul,
        "LaunchResult" / Int32ul,
        "Requeue" / Int8ul,
        "AppStatus" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1057, version=1)
class Microsoft_Windows_Superfetch_1057_1(Etw):
    pattern = Struct(
        "AppNameKey" / Int32ul,
        "AUMID" / WString,
        "AppSkipReason" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1058, version=1)
class Microsoft_Windows_Superfetch_1058_1(Etw):
    pattern = Struct(
        "AppKey" / Int32ul,
        "FullPackageName" / WString,
        "TimeFromPrefetchToSwitchInMS" / Int32ul,
        "NewBenefitScore" / Int16sl,
        "NewAggregateBenefitScore" / Int16sl
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1059, version=1)
class Microsoft_Windows_Superfetch_1059_1(Etw):
    pattern = Struct(
        "AppKey" / Int32ul,
        "FullPackageName" / WString,
        "ReasonsNotToPrefetch" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1060, version=1)
class Microsoft_Windows_Superfetch_1060_1(Etw):
    pattern = Struct(
        "AppKey" / Int32ul,
        "FullPackageName" / WString,
        "ACPowered" / Int8ul,
        "Threshold" / Double,
        "Probability" / Double
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1061, version=1)
class Microsoft_Windows_Superfetch_1061_1(Etw):
    pattern = Struct(
        "AppKey" / Int32ul,
        "FullPackageName" / WString,
        "PreviousPrefetchTime" / Int64ul,
        "PrefetchCount" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1062, version=1)
class Microsoft_Windows_Superfetch_1062_1(Etw):
    pattern = Struct(
        "AppKey" / Int32ul,
        "AUMID" / WString,
        "Command" / Int32ul,
        "AppType" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1063, version=1)
class Microsoft_Windows_Superfetch_1063_1(Etw):
    pattern = Struct(
        "AppKey" / Int32ul,
        "FullPackageName" / WString,
        "Command" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1064, version=1)
class Microsoft_Windows_Superfetch_1064_1(Etw):
    pattern = Struct(
        "AppKey" / Int32ul,
        "FullPackageName" / WString,
        "PID" / Int32ul
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1065, version=1)
class Microsoft_Windows_Superfetch_1065_1(Etw):
    pattern = Struct(
        "AppKey" / Int32ul,
        "AUMID" / WString
    )


@declare(guid=guid("99806515-9f51-4c2f-b918-1eae407aa8cb"), event_id=1067, version=1)
class Microsoft_Windows_Superfetch_1067_1(Etw):
    pattern = Struct(
        "PagesCombined" / Int64ul
    )

