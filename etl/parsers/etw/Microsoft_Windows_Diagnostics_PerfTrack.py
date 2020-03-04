# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Diagnostics-PerfTrack
GUID : 030f2f57-abd0-4427-bcf1-3a3587d7dc7d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=200, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_200_0(Etw):
    pattern = Struct(
        "StartTimeStamp" / Int64sl,
        "StartProviderId" / Guid,
        "StartEventId" / Int16ul,
        "StartEventVersion" / Int8ul,
        "StopTimeStamp" / Int64sl,
        "StopProviderId" / Guid,
        "StopEventId" / Int16ul,
        "StopEventVersion" / Int8ul,
        "ScenarioId" / Guid,
        "SqmId" / Int32ul,
        "Duration" / Int32ul,
        "RuleId" / Int32ul
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=218, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_218_0(Etw):
    pattern = Struct(
        "TriggerTimeStamp" / Int64sl,
        "TriggerProviderId" / Guid,
        "TriggerEventId" / Int16ul,
        "TriggerEventVersion" / Int8ul,
        "ScenarioId" / Guid,
        "SqmId" / Int32ul,
        "Duration" / Int32ul,
        "RuleId" / Int32ul
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=500, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_500_0(Etw):
    pattern = Struct(
        "CanAddToScenarioStream" / Int32ul,
        "ScenarioId" / Int32ul,
        "ScenarioDuration" / Int32ul,
        "ScenarioPackedContext" / Int32ul,
        "MoshTimeValue" / Int32ul,
        "ScenarioMetadata" / WString
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=800, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_800_0(Etw):
    pattern = Struct(
        "SqmId" / Int32ul,
        "SqmValue" / Int32ul
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1100, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1100_0(Etw):
    pattern = Struct(
        "MostRecentPreviousBuild" / WString,
        "WhenUpgradedFrom" / Int64ul
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1101, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1101_0(Etw):
    pattern = Struct(
        "MostRecentPreviousBuild" / WString,
        "WhenUpgradedFrom" / Int64ul
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1102, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1102_0(Etw):
    pattern = Struct(
        "MostRecentPreviousBuild" / WString,
        "WhenUpgradedFrom" / Int64ul
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1105, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1105_0(Etw):
    pattern = Struct(
        "Resource" / WString,
        "NumResources" / Int32ul,
        "SliceDuration_msec" / Int32ul,
        "RequiredIdleDuration_msec" / Int32ul,
        "NumOverlaps" / Int32ul,
        "MaximumUsagePerSlice_Percent" / Int32ul,
        "NormalizeTime" / Int8ul
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1106, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1106_0(Etw):
    pattern = Struct(
        "Resource" / WString,
        "ResourceId" / Int32ul,
        "BusyPercentage" / Int32ul,
        "LastIdleTime" / Int64sl,
        "LastTotalTime" / Int64sl,
        "CurrentIdleTime" / Int64sl,
        "CurrentTotalTime" / Int64sl
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1107, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1107_0(Etw):
    pattern = Struct(
        "Resource" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1108, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1108_0(Etw):
    pattern = Struct(
        "Resource" / WString,
        "CombinedBusyPercentage" / Int32ul,
        "IsIdle" / Int8ul,
        "IdleTimeFound" / Int64ul
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1109, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1109_0(Etw):
    pattern = Struct(
        "DevicePath" / WString
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1110, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1110_0(Etw):
    pattern = Struct(
        "AccumulatedIdleTime" / Int64sl
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1111, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1111_0(Etw):
    pattern = Struct(
        "MostRecentPreviousBuild" / WString,
        "WhenUpgradedFrom" / Int64ul
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1112, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1112_0(Etw):
    pattern = Struct(
        "MostRecentPreviousBuild" / WString,
        "WhenUpgradedFrom" / Int64ul
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1500, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1500_0(Etw):
    pattern = Struct(
        "MainPathHybridbootTimeMs" / Int32ul,
        "PostTimeMs" / Int32ul,
        "ResumeTimeMs" / Int32ul,
        "AdditionalMetadata" / Int32ul
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1500, version=1)
class Microsoft_Windows_Diagnostics_PerfTrack_1500_1(Etw):
    pattern = Struct(
        "MainPathHybridbootTimeMs" / Int32ul,
        "PostTimeMs" / Int32ul,
        "ResumeTimeMs" / Int32ul,
        "AdditionalMetadata" / Int32ul,
        "ReadyBootTrainingCountSinceLastServicing" / Int32ul
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1501, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1501_0(Etw):
    pattern = Struct(
        "ScenarioId" / Int32ul,
        "ControlFlags" / Int32ul,
        "MatchKey" / WString,
        "ScenarioName" / WString
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1502, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1502_0(Etw):
    pattern = Struct(
        "ScenarioId" / Int32ul,
        "ControlFlags" / Int32ul,
        "MatchKey" / WString,
        "ScenarioName" / WString,
        "PackageFullName" / WString,
        "PRAID" / WString,
        "Dword1" / Int32ul,
        "Dword2" / Int32ul,
        "Dword3" / Int32ul,
        "Dword4" / Int32ul,
        "Dword5" / Int32ul,
        "String1" / WString,
        "String2" / WString
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1503, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1503_0(Etw):
    pattern = Struct(
        "ScenarioId" / Int32ul,
        "ControlFlags" / Int32ul,
        "MatchKey" / WString,
        "ScenarioName" / WString,
        "PackageFullName" / WString,
        "PRAID" / WString
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1504, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1504_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul,
        "ScenarioId" / Int32ul,
        "ControlFlags" / Int32ul,
        "ScenarioName" / WString,
        "PackageFullName" / WString,
        "PRAID" / WString,
        "Dword1" / Int32ul,
        "Dword2" / Int32ul,
        "Dword3" / Int32ul,
        "Dword4" / Int32ul,
        "Dword5" / Int32ul,
        "String1" / WString,
        "String2" / WString
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1505, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1505_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul,
        "ScenarioId" / Int32ul,
        "ControlFlags" / Int32ul,
        "ScenarioName" / WString,
        "PackageFullName" / WString,
        "PRAID" / WString
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1506, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1506_0(Etw):
    pattern = Struct(
        "ControlFlags" / Int32ul,
        "MatchKey" / WString,
        "PackageFullName" / WString,
        "AUMID" / WString,
        "ActivationKind" / Int32ul
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1507, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1507_0(Etw):
    pattern = Struct(
        "ControlFlags" / Int32ul,
        "MatchKey" / WString,
        "PackageFullName" / WString,
        "AUMID" / WString,
        "ActivationKind" / Int32ul
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1508, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1508_0(Etw):
    pattern = Struct(
        "ControlFlags" / Int32ul,
        "MatchKey" / WString,
        "PackageFullName" / WString,
        "AUMID" / WString
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1509, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1509_0(Etw):
    pattern = Struct(
        "ControlFlags" / Int32ul,
        "MatchKey" / WString,
        "PackageFullName" / WString,
        "AUMID" / WString
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1510, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1510_0(Etw):
    pattern = Struct(
        "ControlFlags" / Int32ul,
        "ViewId" / Int32ul,
        "PackageFullName" / WString,
        "AUMID" / WString,
        "ResizeFlags" / Int32ul,
        "WindowSize" / Int32ul
    )


@declare(guid=guid("030f2f57-abd0-4427-bcf1-3a3587d7dc7d"), event_id=1511, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_1511_0(Etw):
    pattern = Struct(
        "ControlFlags" / Int32ul,
        "ViewId" / Int32ul,
        "PackageFullName" / WString,
        "AUMID" / WString,
        "ResizeFlags" / Int32ul,
        "WindowSize" / Int32ul
    )

