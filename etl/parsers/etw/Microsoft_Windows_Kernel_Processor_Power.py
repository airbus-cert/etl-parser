# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-Processor-Power
GUID : 0f67e49f-fe51-4e9f-b490-6f2948cc6027
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=1, version=0)
class Microsoft_Windows_Kernel_Processor_Power_1_0(Etw):
    pattern = Struct(
        "Processor" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=2, version=0)
class Microsoft_Windows_Kernel_Processor_Power_2_0(Etw):
    pattern = Struct(
        "Processor" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=3, version=0)
class Microsoft_Windows_Kernel_Processor_Power_3_0(Etw):
    pattern = Struct(
        "Processor" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=4, version=0)
class Microsoft_Windows_Kernel_Processor_Power_4_0(Etw):
    pattern = Struct(
        "Processor" / Int32ul,
        "IdleStateCount" / Int32ul,
        "PerfStateCount" / Int32ul,
        "ThrottleStateCount" / Int32ul,
        "IdleState" / Int16ul,
        "PerfState" / Int32sl
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=7, version=0)
class Microsoft_Windows_Kernel_Processor_Power_7_0(Etw):
    pattern = Struct(
        "Processor" / Int32ul,
        "CapDurationInSeconds" / Int32ul,
        "PpcChanges" / Int32ul,
        "TpcChanges" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=8, version=0)
class Microsoft_Windows_Kernel_Processor_Power_8_0(Etw):
    pattern = Struct(
        "Processor" / Int32ul,
        "CapDurationInSeconds" / Int32ul,
        "PpcChanges" / Int32ul,
        "TpcChanges" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=9, version=0)
class Microsoft_Windows_Kernel_Processor_Power_9_0(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "Speed" / Int32ul,
        "GroupCount" / Int16ul,
        "Group" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=9, version=1)
class Microsoft_Windows_Kernel_Processor_Power_9_1(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "Speed" / Int32ul,
        "GroupCount" / Int16ul,
        "Group" / Int16sl,
        "Performance" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=9, version=2)
class Microsoft_Windows_Kernel_Processor_Power_9_2(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "Speed" / Int32ul,
        "GroupCount" / Int16ul,
        "Group" / Int32ul,
        "Performance" / Int32ul,
        "MinPercent" / Int32ul,
        "MaxPercent" / Int32ul,
        "TolerancePercent" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=9, version=3)
class Microsoft_Windows_Kernel_Processor_Power_9_3(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "Speed" / Int32ul,
        "GroupCount" / Int16ul,
        "Group" / Int64sl,
        "Performance" / Int32ul,
        "MinPercent" / Int32ul,
        "MaxPercent" / Int32ul,
        "TolerancePercent" / Int32ul,
        "Autonomous" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=10, version=0)
class Microsoft_Windows_Kernel_Processor_Power_10_0(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "Speed" / Int32ul,
        "Group" / Int16ul,
        "Number" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=10, version=1)
class Microsoft_Windows_Kernel_Processor_Power_10_1(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "Speed" / Int32ul,
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Performance" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=10, version=2)
class Microsoft_Windows_Kernel_Processor_Power_10_2(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "Speed" / Int32ul,
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Performance" / Int32ul,
        "TolerancePercent" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=10, version=3)
class Microsoft_Windows_Kernel_Processor_Power_10_3(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "Speed" / Int32ul,
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Performance" / Int32ul,
        "TolerancePercent" / Int32ul,
        "MinPercent" / Int32ul,
        "MaxPercent" / Int32ul,
        "EppPercent" / Int32ul,
        "ActivityWindow" / Int32ul,
        "Autonomous" / Int8ul,
        "Initiated" / Int8ul,
        "VirtualLittle" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=10, version=4)
class Microsoft_Windows_Kernel_Processor_Power_10_4(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "Speed" / Int32ul,
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Performance" / Int32ul,
        "TolerancePercent" / Int32ul,
        "MinPercent" / Int32ul,
        "MaxPercent" / Int32ul,
        "EppPercent" / Int32ul,
        "ActivityWindow" / Int32ul,
        "Autonomous" / Int8ul,
        "Initiated" / Int8ul,
        "QosClass" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=11, version=0)
class Microsoft_Windows_Kernel_Processor_Power_11_0(Etw):
    pattern = Struct(
        "PpmCheckTime" / Int64ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=11, version=1)
class Microsoft_Windows_Kernel_Processor_Power_11_1(Etw):
    pattern = Struct(
        "PpmCheckTime" / Int64ul,
        "AdjustedCheckTime" / Int64ul,
        "StartPhase" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=12, version=0)
class Microsoft_Windows_Kernel_Processor_Power_12_0(Etw):
    pattern = Struct(
        "PpmCheckTime" / Int64ul,
        "IdleTime" / Int64ul,
        "BusyTime" / Int64ul,
        "Frequency" / Int32ul,
        "Group" / Int16ul,
        "Number" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=12, version=1)
class Microsoft_Windows_Kernel_Processor_Power_12_1(Etw):
    pattern = Struct(
        "PpmCheckTime" / Int64ul,
        "IdleTime" / Int64ul,
        "BusyTime" / Int64ul,
        "Frequency" / Int32ul,
        "Group" / Int16ul,
        "Number" / Int8ul,
        "DeliveredPerformance" / Int32ul,
        "Utility" / Int16ul,
        "AffinitizedUtility" / Int16ul,
        "FrequencySensitivity" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=12, version=2)
class Microsoft_Windows_Kernel_Processor_Power_12_2(Etw):
    pattern = Struct(
        "PpmCheckTime" / Int64ul,
        "IdleTime" / Int64ul,
        "BusyTime" / Int64ul,
        "Frequency" / Int32ul,
        "Group" / Int16ul,
        "Number" / Int8ul,
        "DeliveredPerformance" / Int32ul,
        "Utility" / Int16ul,
        "AffinitizedUtility" / Int16ul,
        "FrequencySensitivity" / Int8ul,
        "BufferingPercent" / Int8ul,
        "StallTime" / Int64ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=13, version=0)
class Microsoft_Windows_Kernel_Processor_Power_13_0(Etw):
    pattern = Struct(
        "PpmCheckTime" / Int64ul,
        "IdleTimeInMs" / Int32ul,
        "BusyTimeInMs" / Int32ul,
        "ExcessBusyTimeInMs" / Int32ul,
        "Frequency" / Int32ul,
        "Group" / Int16ul,
        "Number" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=14, version=0)
class Microsoft_Windows_Kernel_Processor_Power_14_0(Etw):
    pattern = Struct(
        "PpmCheckTime" / Int64ul,
        "Group" / Int16ul,
        "Number" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=14, version=1)
class Microsoft_Windows_Kernel_Processor_Power_14_1(Etw):
    pattern = Struct(
        "PpmCheckTime" / Int64ul,
        "Group" / Int16ul,
        "Number" / Int8ul,
        "SoftParked" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=15, version=0)
class Microsoft_Windows_Kernel_Processor_Power_15_0(Etw):
    pattern = Struct(
        "PpmCheckTime" / Int64ul,
        "Group" / Int16ul,
        "Number" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=16, version=0)
class Microsoft_Windows_Kernel_Processor_Power_16_0(Etw):
    pattern = Struct(
        "PpmCheckTime" / Int64ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=18, version=0)
class Microsoft_Windows_Kernel_Processor_Power_18_0(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "Speed" / Int32ul,
        "Group" / Int16ul,
        "Number" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=18, version=1)
class Microsoft_Windows_Kernel_Processor_Power_18_1(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "Speed" / Int32ul,
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Performance" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=18, version=2)
class Microsoft_Windows_Kernel_Processor_Power_18_2(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "Speed" / Int32ul,
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Performance" / Int32ul,
        "TolerancePercent" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=19, version=0)
class Microsoft_Windows_Kernel_Processor_Power_19_0(Etw):
    pattern = Struct(
        "StateCount" / Int32ul,
        "TotalTransitions" / Int32ul,
        "ResetCount" / Int32ul,
        "Pad" / Int32ul,
        "StartTime" / Int64ul,
        "State" / Int32ul,
        "Group" / Int16ul,
        "Number" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=19, version=1)
class Microsoft_Windows_Kernel_Processor_Power_19_1(Etw):
    pattern = Struct(
        "StateCount" / Int32ul,
        "TotalTransitions" / Int32ul,
        "ResetCount" / Int32ul,
        "AbortCount" / Int32ul,
        "StartTime" / Int64ul,
        "State" / Int64sl,
        "Group" / Int16ul,
        "Number" / Int8ul,
        "IdleTime" / Int64ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=19, version=2)
class Microsoft_Windows_Kernel_Processor_Power_19_2(Etw):
    pattern = Struct(
        "StateCount" / Int32ul,
        "TotalTransitions" / Int32ul,
        "ResetCount" / Int32ul,
        "AbortCount" / Int32ul,
        "StartTime" / Int64ul,
        "State" / Float32l,
        "Group" / Int16ul,
        "Number" / Int8ul,
        "IdleTime" / Int64ul,
        "SelectionCount" / Int32ul,
        "SelectionAccounting" / Sid
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=20, version=0)
class Microsoft_Windows_Kernel_Processor_Power_20_0(Etw):
    pattern = Struct(
        "FeaturesPresent" / Int32ul,
        "FeaturesAccessed" / Int32ul,
        "FeaturesValidated" / Int32ul,
        "Group" / Int16ul,
        "Number" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=21, version=0)
class Microsoft_Windows_Kernel_Processor_Power_21_0(Etw):
    pattern = Struct(
        "DomainId" / Int32ul,
        "MemberCount" / Int32ul,
        "MembersEnumerated" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=22, version=0)
class Microsoft_Windows_Kernel_Processor_Power_22_0(Etw):
    pattern = Struct(
        "DomainId" / Int32ul,
        "MemberCount" / Int32ul,
        "MembersEnumerated" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=23, version=0)
class Microsoft_Windows_Kernel_Processor_Power_23_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "IdleStateCount" / Int32ul,
        "PerfStateCount" / Int32ul,
        "ThrottleStateCount" / Int32ul,
        "IdleState" / Int32sl,
        "PerfState" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=26, version=0)
class Microsoft_Windows_Kernel_Processor_Power_26_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "IdleStateCount" / Int32ul,
        "PerfStateCount" / Int32ul,
        "ThrottleStateCount" / Int32ul,
        "IdleState" / Int32sl,
        "PerfState" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=26, version=1)
class Microsoft_Windows_Kernel_Processor_Power_26_1(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "IdleStateCount" / Int32ul,
        "PerfStateCount" / Int32ul,
        "ThrottleStateCount" / Int32ul,
        "IdleState" / Int32sl,
        "PerfState" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=29, version=0)
class Microsoft_Windows_Kernel_Processor_Power_29_0(Etw):
    pattern = Struct(
        "MajorVersion" / Int8ul,
        "MinorVersion" / Int8ul,
        "MinPerfPercent" / Int8ul,
        "MinThrottlePercent" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=30, version=0)
class Microsoft_Windows_Kernel_Processor_Power_30_0(Etw):
    pattern = Struct(
        "MajorVersion" / Int8ul,
        "MinorVersion" / Int8ul,
        "MinPerfPercent" / Int8ul,
        "MinThrottlePercent" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=33, version=0)
class Microsoft_Windows_Kernel_Processor_Power_33_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=34, version=0)
class Microsoft_Windows_Kernel_Processor_Power_34_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=34, version=1)
class Microsoft_Windows_Kernel_Processor_Power_34_1(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=35, version=0)
class Microsoft_Windows_Kernel_Processor_Power_35_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=35, version=1)
class Microsoft_Windows_Kernel_Processor_Power_35_1(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=36, version=0)
class Microsoft_Windows_Kernel_Processor_Power_36_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=36, version=1)
class Microsoft_Windows_Kernel_Processor_Power_36_1(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=37, version=0)
class Microsoft_Windows_Kernel_Processor_Power_37_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "CapDurationInSeconds" / Int32ul,
        "PpcChanges" / Int32ul,
        "TpcChanges" / Int32ul,
        "PccChanges" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=37, version=1)
class Microsoft_Windows_Kernel_Processor_Power_37_1(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "CapDurationInSeconds" / Int32ul,
        "PpcChanges" / Int32ul,
        "TpcChanges" / Int32ul,
        "PccChanges" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=38, version=0)
class Microsoft_Windows_Kernel_Processor_Power_38_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "CapDurationInSeconds" / Int32ul,
        "PpcChanges" / Int32ul,
        "TpcChanges" / Int32ul,
        "PccChanges" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=39, version=0)
class Microsoft_Windows_Kernel_Processor_Power_39_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Cap" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=40, version=0)
class Microsoft_Windows_Kernel_Processor_Power_40_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=41, version=0)
class Microsoft_Windows_Kernel_Processor_Power_41_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Cap" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=42, version=0)
class Microsoft_Windows_Kernel_Processor_Power_42_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "StateCount" / Int32ul,
        "States" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=43, version=0)
class Microsoft_Windows_Kernel_Processor_Power_43_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "PBlockAddress" / Int32ul,
        "PBlockLength" / Int8ul,
        "ProcessorId" / Int32ul,
        "ApicId" / Int32ul,
        "Ppc" / Int32ul,
        "PctControl" / Float32l,
        "PctStatus" / Int64ul,
        "StateCount" / Int32ul,
        "PssStates" / Int64ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=44, version=0)
class Microsoft_Windows_Kernel_Processor_Power_44_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "FadtC2Latency" / Int16ul,
        "FadtC3Latency" / Int16ul,
        "CStateVersionInUse" / Int32ul,
        "StateCount" / Int32ul,
        "CstStates" / Int32sl
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=45, version=0)
class Microsoft_Windows_Kernel_Processor_Power_45_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "FadtDutyWidth" / Int8ul,
        "FadtDutyOffset" / Int8ul,
        "Tpc" / Int32ul,
        "TStateVersionInUse" / Int32ul,
        "PtcControl" / Int64ul,
        "PtcStatus" / Guid,
        "StateCount" / Int32ul,
        "TssStates" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=46, version=0)
class Microsoft_Windows_Kernel_Processor_Power_46_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Cap" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=47, version=0)
class Microsoft_Windows_Kernel_Processor_Power_47_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Cap" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=48, version=0)
class Microsoft_Windows_Kernel_Processor_Power_48_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Cap" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=50, version=0)
class Microsoft_Windows_Kernel_Processor_Power_50_0(Etw):
    pattern = Struct(
        "Cap" / Int32ul,
        "IsApplied" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=51, version=0)
class Microsoft_Windows_Kernel_Processor_Power_51_0(Etw):
    pattern = Struct(
        "Cap" / Int32ul,
        "IsApplied" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=52, version=0)
class Microsoft_Windows_Kernel_Processor_Power_52_0(Etw):
    pattern = Struct(
        "HintType" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=53, version=0)
class Microsoft_Windows_Kernel_Processor_Power_53_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Affinity" / Int64ul,
        "ConcurrentCores" / Int8ul,
        "HistogramSize" / Int32ul,
        "ConcurrencyHistogram" / Int64ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=53, version=1)
class Microsoft_Windows_Kernel_Processor_Power_53_1(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Affinity" / Int64ul,
        "ConcurrentCores" / Int8ul,
        "HistogramSize" / Int32ul,
        "ConcurrencyHistogram" / Int64ul,
        "DistributeCores" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=54, version=0)
class Microsoft_Windows_Kernel_Processor_Power_54_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=55, version=0)
class Microsoft_Windows_Kernel_Processor_Power_55_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "IdleStateCount" / Int32ul,
        "IdleImplementation" / Int32ul,
        "NominalFrequency" / Int32ul,
        "MaximumPerformancePercent" / Int32ul,
        "MinimumPerformancePercent" / Int32ul,
        "MinimumThrottlePercent" / Int32ul,
        "PerformanceImplementation" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=55, version=1)
class Microsoft_Windows_Kernel_Processor_Power_55_1(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "IdleStateCount" / Int32ul,
        "IdleImplementation" / Int32ul,
        "NominalFrequency" / Int32ul,
        "MaximumPerformancePercent" / Int32ul,
        "MinimumPerformancePercent" / Int32ul,
        "MinimumThrottlePercent" / Int32ul,
        "PerformanceImplementation" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=56, version=0)
class Microsoft_Windows_Kernel_Processor_Power_56_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "IdleStateCount" / Int32ul,
        "IdleImplementation" / Int32ul,
        "NominalFrequency" / Int32ul,
        "MaximumPerformancePercent" / Int32ul,
        "MinimumPerformancePercent" / Int32ul,
        "MinimumThrottlePercent" / Int32ul,
        "PerformanceImplementation" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=57, version=0)
class Microsoft_Windows_Kernel_Processor_Power_57_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "MaximumCoordinatedProcessors" / Int32ul,
        "StateCount" / Int32ul,
        "States" / Int16sl
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=58, version=0)
class Microsoft_Windows_Kernel_Processor_Power_58_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "MaximumCoordinatedProcessors" / Int32ul,
        "StateCount" / Int32ul,
        "States" / Int16sl
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=59, version=0)
class Microsoft_Windows_Kernel_Processor_Power_59_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "FeedbackCounterCount" / Int32ul,
        "IdleStateCount" / Int32ul,
        "PerformanceStatesSupported" / Int8ul,
        "ParkingSupported" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=59, version=1)
class Microsoft_Windows_Kernel_Processor_Power_59_1(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "FeedbackCounterCount" / Int32ul,
        "IdleStateCount" / Int32ul,
        "PerformanceStatesSupported" / Int8ul,
        "ParkingSupported" / Int8ul,
        "DiscretePerformanceStateCount" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=60, version=0)
class Microsoft_Windows_Kernel_Processor_Power_60_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "FeedbackCounterCount" / Int32ul,
        "IdleStateCount" / Int32ul,
        "PerformanceStatesSupported" / Int8ul,
        "ParkingSupported" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=60, version=1)
class Microsoft_Windows_Kernel_Processor_Power_60_1(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "FeedbackCounterCount" / Int32ul,
        "IdleStateCount" / Int32ul,
        "PerformanceStatesSupported" / Int8ul,
        "ParkingSupported" / Int8ul,
        "DiscretePerformanceStateCount" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=61, version=0)
class Microsoft_Windows_Kernel_Processor_Power_61_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "GuaranteedPerformance" / Int32ul,
        "LimitReasons" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=62, version=0)
class Microsoft_Windows_Kernel_Processor_Power_62_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "FeedbackCount" / Int32ul,
        "Feedback" / Int64ul,
        "HighestPerformance" / Int32ul,
        "NominalPerformance" / Int32ul,
        "LowestNonlinearPerformance" / Int32ul,
        "LowestPerformance" / Int32ul,
        "DomainId" / Int32ul,
        "DomainMembers" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=62, version=1)
class Microsoft_Windows_Kernel_Processor_Power_62_1(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "FeedbackCount" / Int32ul,
        "Feedback" / Double,
        "HighestPerformance" / Int32ul,
        "NominalPerformance" / Int32ul,
        "LowestNonlinearPerformance" / Int32ul,
        "LowestPerformance" / Int32ul,
        "DomainId" / Int32ul,
        "DomainMembers" / Int32ul,
        "PerfStateCount" / Int8ul,
        "PerfStates" / Int64ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=63, version=0)
class Microsoft_Windows_Kernel_Processor_Power_63_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "FeedbackCount" / Int32ul,
        "Feedback" / Int64ul,
        "HighestPerformance" / Int32ul,
        "NominalPerformance" / Int32ul,
        "LowestNonlinearPerformance" / Int32ul,
        "LowestPerformance" / Int32ul,
        "DomainId" / Int32ul,
        "DomainMembers" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=63, version=1)
class Microsoft_Windows_Kernel_Processor_Power_63_1(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "FeedbackCount" / Int32ul,
        "Feedback" / Double,
        "HighestPerformance" / Int32ul,
        "NominalPerformance" / Int32ul,
        "LowestNonlinearPerformance" / Int32ul,
        "LowestPerformance" / Int32ul,
        "DomainId" / Int32ul,
        "DomainMembers" / Int32ul,
        "PerfStateCount" / Int8ul,
        "PerfStates" / Int64ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=64, version=0)
class Microsoft_Windows_Kernel_Processor_Power_64_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Parked" / Int8ul,
        "BiosCap" / Int32ul,
        "ThermalCap" / Int32ul,
        "DesiredPerformance" / Int32ul,
        "NominalFrequency" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=64, version=1)
class Microsoft_Windows_Kernel_Processor_Power_64_1(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Parked" / Int8ul,
        "BiosCap" / Int32ul,
        "ThermalCap" / Int32ul,
        "DesiredPerformance" / Int32ul,
        "NominalFrequency" / Int32ul,
        "MinPercent" / Int32ul,
        "MaxPercent" / Int32ul,
        "TolerancePercent" / Int32ul,
        "DeliveredPerformance" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=64, version=2)
class Microsoft_Windows_Kernel_Processor_Power_64_2(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Parked" / Int8ul,
        "BiosCap" / Int32ul,
        "ThermalCap" / Int32ul,
        "DesiredPerformance" / Int32ul,
        "NominalFrequency" / Int32ul,
        "MinPercent" / Int32ul,
        "MaxPercent" / Int32ul,
        "TolerancePercent" / Int32ul,
        "DeliveredPerformance" / Int32ul,
        "EfficiencyClass" / Int8ul,
        "SchedulingClass" / Int8ul,
        "Autonomous" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=64, version=3)
class Microsoft_Windows_Kernel_Processor_Power_64_3(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Parked" / Int8ul,
        "BiosCap" / Int32ul,
        "ThermalCap" / Int32ul,
        "DesiredPerformance" / Int32ul,
        "NominalFrequency" / Int32ul,
        "MinPercent" / Int32ul,
        "MaxPercent" / Int32ul,
        "TolerancePercent" / Int32ul,
        "DeliveredPerformance" / Int32ul,
        "EfficiencyClass" / Int8ul,
        "SchedulingClass" / Int8ul,
        "Autonomous" / Int8ul,
        "EppPercent" / Int32ul,
        "ActivityWindow" / Int32ul,
        "VirtualLittle" / Int8ul,
        "RelativePerformance" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=64, version=4)
class Microsoft_Windows_Kernel_Processor_Power_64_4(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Parked" / Int8ul,
        "BiosCap" / Int32ul,
        "ThermalCap" / Int32ul,
        "DesiredPerformance" / Int32ul,
        "NominalFrequency" / Int32ul,
        "MinPercent" / Int32ul,
        "MaxPercent" / Int32ul,
        "TolerancePercent" / Int32ul,
        "DeliveredPerformance" / Int32ul,
        "EfficiencyClass" / Int8ul,
        "SchedulingClass" / Int8ul,
        "Autonomous" / Int8ul,
        "EppPercent" / Int32ul,
        "ActivityWindow" / Int32ul,
        "QosClass" / Int32ul,
        "RelativePerformance" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=64, version=5)
class Microsoft_Windows_Kernel_Processor_Power_64_5(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Parked" / Int8ul,
        "BiosCap" / Int32ul,
        "ThermalCap" / Int32ul,
        "DesiredPerformance" / Int32ul,
        "NominalFrequency" / Int32ul,
        "MinPercent" / Int32ul,
        "MaxPercent" / Int32ul,
        "TolerancePercent" / Int32ul,
        "DeliveredPerformance" / Int32ul,
        "EfficiencyClass" / Int8ul,
        "SchedulingClass" / Int8ul,
        "Autonomous" / Int8ul,
        "EppPercent" / Int32ul,
        "ActivityWindow" / Int32ul,
        "QosClass" / Int32ul,
        "RelativePerformance" / Int32ul,
        "EfficiencySchedulingClass" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=64, version=6)
class Microsoft_Windows_Kernel_Processor_Power_64_6(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Parked" / Int8ul,
        "BiosCap" / Int32ul,
        "ThermalCap" / Int32ul,
        "DesiredPerformance" / Int32ul,
        "NominalFrequency" / Int32ul,
        "MinPercent" / Int32ul,
        "MaxPercent" / Int32ul,
        "TolerancePercent" / Int32ul,
        "DeliveredPerformance" / Int32ul,
        "EfficiencyClass" / Int8ul,
        "SchedulingClass" / Int8ul,
        "Autonomous" / Int8ul,
        "EppPercent" / Int32ul,
        "ActivityWindow" / Int32ul,
        "QosClass" / Int32ul,
        "RelativePerformance" / Int32ul,
        "EfficiencySchedulingClass" / Int8ul,
        "TargetFrequency" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=64, version=7)
class Microsoft_Windows_Kernel_Processor_Power_64_7(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Parked" / Int8ul,
        "BiosCap" / Int32ul,
        "ThermalCap" / Int32ul,
        "DesiredPerformance" / Int32ul,
        "NominalFrequency" / Int32ul,
        "MinPercent" / Int32ul,
        "MaxPercent" / Int32ul,
        "TolerancePercent" / Int32ul,
        "DeliveredPerformance" / Int32ul,
        "EfficiencyClass" / Int8ul,
        "SchedulingClass" / Int8ul,
        "Autonomous" / Int8ul,
        "EppPercent" / Int32ul,
        "ActivityWindow" / Int32ul,
        "QosClass" / Int32ul,
        "RelativePerformance" / Int32ul,
        "EfficiencySchedulingClass" / Int8ul,
        "TargetFrequency" / Int32ul,
        "SoftParked" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=65, version=0)
class Microsoft_Windows_Kernel_Processor_Power_65_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Affinity" / Int64ul,
        "Parked" / Int64ul,
        "LpiCap" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=65, version=1)
class Microsoft_Windows_Kernel_Processor_Power_65_1(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Affinity" / Int64ul,
        "Parked" / Int64ul,
        "LpiCap" / Int8ul,
        "ThermalCap" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=65, version=2)
class Microsoft_Windows_Kernel_Processor_Power_65_2(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Affinity" / Int64ul,
        "Parked" / Int64ul,
        "LpiCap" / Int8ul,
        "ThermalCap" / Int8ul,
        "ParkHint" / Int64ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=65, version=3)
class Microsoft_Windows_Kernel_Processor_Power_65_3(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Affinity" / Int64ul,
        "Parked" / Int64ul,
        "LpiCap" / Int8ul,
        "ThermalCap" / Int8ul,
        "ParkHint" / Int64ul,
        "SoftParked" / Int64ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=66, version=0)
class Microsoft_Windows_Kernel_Processor_Power_66_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Affinity" / Int64ul,
        "LpiCap" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=66, version=1)
class Microsoft_Windows_Kernel_Processor_Power_66_1(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Affinity" / Int64ul,
        "LpiCap" / Int8ul,
        "ThermalCap" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=67, version=0)
class Microsoft_Windows_Kernel_Processor_Power_67_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Type" / Int32ul,
        "StateCount" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=67, version=1)
class Microsoft_Windows_Kernel_Processor_Power_67_1(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Type" / Int32ul,
        "StateCount" / Int32ul,
        "States" / Int16sl
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=68, version=0)
class Microsoft_Windows_Kernel_Processor_Power_68_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "AcpiId" / Int32ul,
        "InterruptControllerId" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=68, version=1)
class Microsoft_Windows_Kernel_Processor_Power_68_1(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "AcpiId" / Int32ul,
        "InterruptControllerId" / Int32ul,
        "ProcessorIndex" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=69, version=0)
class Microsoft_Windows_Kernel_Processor_Power_69_0(Etw):
    pattern = Struct(
        "PlatformIdleStateCount" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=70, version=0)
class Microsoft_Windows_Kernel_Processor_Power_70_0(Etw):
    pattern = Struct(
        "PlatformIdleStateCount" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=71, version=0)
class Microsoft_Windows_Kernel_Processor_Power_71_0(Etw):
    pattern = Struct(
        "AdjustedCheckTime" / Int64ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=72, version=0)
class Microsoft_Windows_Kernel_Processor_Power_72_0(Etw):
    pattern = Struct(
        "StateCount" / Int32ul,
        "ResetCount" / Int32ul,
        "TotalTransitions" / Int64ul,
        "StartTime" / Int64ul,
        "Reserved" / Int64ul,
        "State" / Int32ul,
        "Group" / Int16ul,
        "Number" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=72, version=1)
class Microsoft_Windows_Kernel_Processor_Power_72_1(Etw):
    pattern = Struct(
        "StateCount" / Int32ul,
        "ResetCount" / Int32ul,
        "TotalTransitions" / Int64ul,
        "StartTime" / Int64ul,
        "Reserved" / Int64ul,
        "State" / Int64ul,
        "Group" / Int16ul,
        "Number" / Int8ul,
        "SelectionCount" / Int32ul,
        "SelectionAccounting" / Sid
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=73, version=0)
class Microsoft_Windows_Kernel_Processor_Power_73_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Affinity" / Int64ul,
        "UnparkCount" / Int8ul,
        "OSPreferencePark" / Int64ul,
        "OSPreferenceUnpark" / Int64ul,
        "PlatformPreferencePark" / Int64ul,
        "PlatformPreferenceUnpark" / Int64ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=74, version=0)
class Microsoft_Windows_Kernel_Processor_Power_74_0(Etw):
    pattern = Struct(
        "PreviousActiveScenarioId" / Int32ul,
        "NewActiveScenarioId" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=75, version=0)
class Microsoft_Windows_Kernel_Processor_Power_75_0(Etw):
    pattern = Struct(
        "CurrentActiveScenarioId" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=76, version=0)
class Microsoft_Windows_Kernel_Processor_Power_76_0(Etw):
    pattern = Struct(
        "ScenarioId" / Int32ul,
        "PlatformIdleStateIndex" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=77, version=0)
class Microsoft_Windows_Kernel_Processor_Power_77_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "StateCount" / Int32ul,
        "States" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=78, version=0)
class Microsoft_Windows_Kernel_Processor_Power_78_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "StateCount" / Int32ul,
        "States" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=79, version=0)
class Microsoft_Windows_Kernel_Processor_Power_79_0(Etw):
    pattern = Struct(
        "StateIndex" / Int32ul,
        "InitiatingProcessor" / Int32sl,
        "OneInitiator" / Int8ul,
        "Latency" / Int32ul,
        "BreakEvenDuration" / Int32ul,
        "DependencyCount" / Int32ul,
        "Dependencies" / Int64sl
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=80, version=0)
class Microsoft_Windows_Kernel_Processor_Power_80_0(Etw):
    pattern = Struct(
        "StateIndex" / Int32ul,
        "InitiatingProcessor" / Int32sl,
        "OneInitiator" / Int8ul,
        "Latency" / Int32ul,
        "BreakEvenDuration" / Int32ul,
        "DependencyCount" / Int32ul,
        "Dependencies" / Int64sl
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=81, version=0)
class Microsoft_Windows_Kernel_Processor_Power_81_0(Etw):
    pattern = Struct(
        "ScenarioInstanceId" / Int8ul,
        "DripsBucketsCount" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=82, version=0)
class Microsoft_Windows_Kernel_Processor_Power_82_0(Etw):
    pattern = Struct(
        "IntervalLimitsCount" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=83, version=0)
class Microsoft_Windows_Kernel_Processor_Power_83_0(Etw):
    pattern = Struct(
        "StateIndex" / Int32ul,
        "VetoReason" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=84, version=0)
class Microsoft_Windows_Kernel_Processor_Power_84_0(Etw):
    pattern = Struct(
        "StateIndex" / Int32ul,
        "VetoReason" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=85, version=0)
class Microsoft_Windows_Kernel_Processor_Power_85_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "StateIndex" / Int32ul,
        "VetoReason" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=86, version=0)
class Microsoft_Windows_Kernel_Processor_Power_86_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "StateIndex" / Int32ul,
        "VetoReason" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=87, version=0)
class Microsoft_Windows_Kernel_Processor_Power_87_0(Etw):
    pattern = Struct(
        "StateIndex" / Int32ul,
        "VetoReason" / Int32ul,
        "VetoCount" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=88, version=0)
class Microsoft_Windows_Kernel_Processor_Power_88_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "StateIndex" / Int32ul,
        "VetoReason" / Int32ul,
        "VetoCount" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=89, version=0)
class Microsoft_Windows_Kernel_Processor_Power_89_0(Etw):
    pattern = Struct(
        "PerfBoostAtGuaranteed" / Int8ul,
        "PerfIdealAggressiveIncreasePolicyThreshold" / Int32ul,
        "PerfSingleStepSize" / Int32ul,
        "PerfCalculateActualUtilization" / Int32ul,
        "PerfArtificialDomain" / Int8ul,
        "LowLatencyScalingPercentage" / Int32ul,
        "ParkWithCoreGranularity" / Int8ul,
        "MultiparkGranularity" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=89, version=1)
class Microsoft_Windows_Kernel_Processor_Power_89_1(Etw):
    pattern = Struct(
        "PerfBoostAtGuaranteed" / Int8ul,
        "PerfIdealAggressiveIncreasePolicyThreshold" / Int32ul,
        "PerfSingleStepSize" / Int32ul,
        "PerfCalculateActualUtilization" / Int32ul,
        "PerfArtificialDomain" / Int8ul,
        "LowLatencyScalingPercentage" / Int32ul,
        "ParkWithCoreGranularity" / Int8ul,
        "MultiparkGranularity" / Int32ul,
        "QosManagesIdleProcessors" / Int8ul,
        "QosHysteresis" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=90, version=0)
class Microsoft_Windows_Kernel_Processor_Power_90_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "ResolvedUtilization" / Int32ul,
        "Target" / Int32ul,
        "ResolvedTarget" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=91, version=0)
class Microsoft_Windows_Kernel_Processor_Power_91_0(Etw):
    pattern = Struct(
        "VetoReason" / Int32ul,
        "Name" / WString
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=92, version=0)
class Microsoft_Windows_Kernel_Processor_Power_92_0(Etw):
    pattern = Struct(
        "StateCount" / Int32ul,
        "CoordinatedStates" / CString
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=93, version=0)
class Microsoft_Windows_Kernel_Processor_Power_93_0(Etw):
    pattern = Struct(
        "StateCount" / Int32ul,
        "CoordinatedStates" / CString
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=94, version=0)
class Microsoft_Windows_Kernel_Processor_Power_94_0(Etw):
    pattern = Struct(
        "StateIndex" / Int32ul,
        "DependencyIndex" / Int32ul,
        "ProcessorDependency" / Int8ul,
        "TargetProcessor" / Int16ul,
        "OptionCount" / Int32ul,
        "Options" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=95, version=0)
class Microsoft_Windows_Kernel_Processor_Power_95_0(Etw):
    pattern = Struct(
        "StateIndex" / Int32ul,
        "DependencyIndex" / Int32ul,
        "ProcessorDependency" / Int8ul,
        "TargetProcessor" / Int16ul,
        "OptionCount" / Int32ul,
        "Options" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=96, version=0)
class Microsoft_Windows_Kernel_Processor_Power_96_0(Etw):
    pattern = Struct(
        "Engaged" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=97, version=0)
class Microsoft_Windows_Kernel_Processor_Power_97_0(Etw):
    pattern = Struct(
        "EfficiencyClass" / Int32ul,
        "EnergyInMicroJoules" / Int64ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=98, version=0)
class Microsoft_Windows_Kernel_Processor_Power_98_0(Etw):
    pattern = Struct(
        "StateCount" / Int32ul,
        "States" / CString
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=99, version=0)
class Microsoft_Windows_Kernel_Processor_Power_99_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Affinity" / Int64ul,
        "ProcCount" / Int8ul,
        "ActualUtility" / Int32ul,
        "EstimatedUtility" / Int64ul,
        "ActiveTime" / Int64ul,
        "CheckCount" / Int8ul,
        "Decision" / Int8ul,
        "IdealClass1Count" / Int8ul,
        "ActualClass1Count" / Int8ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=100, version=0)
class Microsoft_Windows_Kernel_Processor_Power_100_0(Etw):
    pattern = Struct(
        "PpmCheckTime" / Int64ul,
        "AdjustedCheckTime" / Int64ul,
        "PipelineId" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=101, version=0)
class Microsoft_Windows_Kernel_Processor_Power_101_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Affinity" / Int64ul,
        "Class0FloorPerf" / Int8ul,
        "Class1MinimumPerf" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=102, version=0)
class Microsoft_Windows_Kernel_Processor_Power_102_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Id" / Int8ul,
        "Priority" / Int8ul,
        "Flags" / Int32ul,
        "Guid" / Guid,
        "ActiveCount" / Int64ul,
        "MaxActiveDurationInUs" / Int64ul,
        "MinActiveDurationInUs" / Int64ul,
        "TotalActiveDurationInUs" / Int64ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=103, version=0)
class Microsoft_Windows_Kernel_Processor_Power_103_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Id" / Int8ul,
        "Priority" / Int8ul,
        "Flags" / Int32ul,
        "Guid" / Guid,
        "ActiveCount" / Int64ul,
        "MaxActiveDurationInUs" / Int64ul,
        "MinActiveDurationInUs" / Int64ul,
        "TotalActiveDurationInUs" / Int64ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=104, version=0)
class Microsoft_Windows_Kernel_Processor_Power_104_0(Etw):
    pattern = Struct(
        "PreviousProfileId" / Int8ul,
        "NextProfileId" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=105, version=0)
class Microsoft_Windows_Kernel_Processor_Power_105_0(Etw):
    pattern = Struct(
        "ProfileId" / Int8ul,
        "Name" / CString,
        "Type" / Int32ul,
        "Class" / Int8ul,
        "Guid" / Guid,
        "ValueSize" / Int32ul,
        "Value" / Bytes(lambda this: this.ValueSize)
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=106, version=0)
class Microsoft_Windows_Kernel_Processor_Power_106_0(Etw):
    pattern = Struct(
        "ProfileId" / Int8ul,
        "Name" / CString,
        "Type" / Int32ul,
        "Class" / Int8ul,
        "Guid" / Guid,
        "ValueSize" / Int32ul,
        "Value" / Bytes(lambda this: this.ValueSize)
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=107, version=0)
class Microsoft_Windows_Kernel_Processor_Power_107_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=108, version=0)
class Microsoft_Windows_Kernel_Processor_Power_108_0(Etw):
    pattern = Struct(
        "ProfileId" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=109, version=0)
class Microsoft_Windows_Kernel_Processor_Power_109_0(Etw):
    pattern = Struct(
        "ProfileId" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=110, version=0)
class Microsoft_Windows_Kernel_Processor_Power_110_0(Etw):
    pattern = Struct(
        "GroupCount" / Int16ul,
        "Group" / CString
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=111, version=0)
class Microsoft_Windows_Kernel_Processor_Power_111_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "DeliveredPerformance" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=111, version=1)
class Microsoft_Windows_Kernel_Processor_Power_111_1(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "DeliveredPerformance" / Int32ul,
        "DurationInUs" / Int64ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=111, version=2)
class Microsoft_Windows_Kernel_Processor_Power_111_2(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "DeliveredPerformance" / Int32ul,
        "DurationInUs" / Int64ul,
        "DeliveredFrequency" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=112, version=0)
class Microsoft_Windows_Kernel_Processor_Power_112_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Processors" / Int64ul,
        "OldPark" / Int64ul,
        "NewPark" / Int64ul,
        "OverUtilizedSet" / Int64ul,
        "IsolatedCores" / Int64ul,
        "IdealUnparked" / Int8ul,
        "UnparkCount" / Int8ul,
        "ParkReason" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=113, version=0)
class Microsoft_Windows_Kernel_Processor_Power_113_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "CounterId" / Int32ul,
        "CounterValue" / Int64ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=114, version=0)
class Microsoft_Windows_Kernel_Processor_Power_114_0(Etw):
    pattern = Struct(
        "CounterId" / Int32ul,
        "CounterValue" / Int64ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=115, version=0)
class Microsoft_Windows_Kernel_Processor_Power_115_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "StateIndex" / Int32ul,
        "VetoCodeCount" / Int32ul,
        "Accounting" / Int16sl
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=116, version=0)
class Microsoft_Windows_Kernel_Processor_Power_116_0(Etw):
    pattern = Struct(
        "StateIndex" / Int32ul,
        "VetoCodeCount" / Int32ul,
        "Accounting" / Int8sl
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=117, version=0)
class Microsoft_Windows_Kernel_Processor_Power_117_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=118, version=0)
class Microsoft_Windows_Kernel_Processor_Power_118_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "EfficiencyClass" / Int8ul,
        "SchedulingClass" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=118, version=1)
class Microsoft_Windows_Kernel_Processor_Power_118_1(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "EfficiencyClass" / Int8ul,
        "SchedulingClass" / Int8ul,
        "EfficiencySchedulingClass" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=119, version=0)
class Microsoft_Windows_Kernel_Processor_Power_119_0(Etw):
    pattern = Struct(
        "HeterogeneousPolicy" / Int32ul,
        "HeterogeneousSystemType" / Int32ul,
        "DefaultPolicy" / Int32ul,
        "DefaultDynamicPolicy" / Int32ul,
        "DynamicCpuPolicyMask" / Int32ul,
        "DynamicCpuPolicyImportant" / Int32ul,
        "DynamicCpuPolicyImportantShort" / Int32ul,
        "DynamicCpuPolicyImportantPriority" / Int32ul,
        "DynamicCpuPolicyExpectedRuntime" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=120, version=0)
class Microsoft_Windows_Kernel_Processor_Power_120_0(Etw):
    pattern = Struct(
        "HeterogeneousPolicy" / Int32ul,
        "HeterogeneousSystemType" / Int32ul,
        "DefaultPolicy" / Int32ul,
        "DefaultDynamicPolicy" / Int32ul,
        "DynamicCpuPolicyMask" / Int32ul,
        "DynamicCpuPolicyImportant" / Int32ul,
        "DynamicCpuPolicyImportantShort" / Int32ul,
        "DynamicCpuPolicyImportantPriority" / Int32ul,
        "DynamicCpuPolicyExpectedRuntime" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=121, version=0)
class Microsoft_Windows_Kernel_Processor_Power_121_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Autonomous" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=122, version=0)
class Microsoft_Windows_Kernel_Processor_Power_122_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Number" / Int8ul,
        "Revision" / Int32ul,
        "LevelId" / Int64ul,
        "StateCount" / Int32ul,
        "States" / Int16ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=123, version=0)
class Microsoft_Windows_Kernel_Processor_Power_123_0(Etw):
    pattern = Struct(
        "NamespacePath" / WString,
        "Revision" / Int32ul,
        "LevelId" / Int64ul,
        "StateCount" / Int32ul,
        "States" / Int16sl
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=124, version=0)
class Microsoft_Windows_Kernel_Processor_Power_124_0(Etw):
    pattern = Struct(
        "VirtualHeterogeneitySupported" / Int8ul,
        "VirtualHeterogeneityOn" / Int8ul,
        "DisableReasons" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=125, version=0)
class Microsoft_Windows_Kernel_Processor_Power_125_0(Etw):
    pattern = Struct(
        "VirtualHeterogeneitySupported" / Int8ul,
        "VirtualHeterogeneityOn" / Int8ul,
        "DisableReasons" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=126, version=0)
class Microsoft_Windows_Kernel_Processor_Power_126_0(Etw):
    pattern = Struct(
        "SchedulerDirectedPerfStatesSupported" / Int8ul,
        "PpmQosEnabled" / Int8ul,
        "PpmQosDisableReasons" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=127, version=0)
class Microsoft_Windows_Kernel_Processor_Power_127_0(Etw):
    pattern = Struct(
        "SchedulerDirectedPerfStatesSupported" / Int8ul,
        "PpmQosEnabled" / Int8ul,
        "PpmQosDisableReasons" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=128, version=0)
class Microsoft_Windows_Kernel_Processor_Power_128_0(Etw):
    pattern = Struct(
        "DomainId" / Int32ul,
        "CoordinationType" / Int8ul,
        "IdleProcessorsDiscounted" / Int8ul,
        "SchedulerDirectedTransitionsSupported" / Int8ul,
        "WorstCaseTransitionLatency" / Int32ul,
        "WorstCaseTransitionOverhead" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=128, version=1)
class Microsoft_Windows_Kernel_Processor_Power_128_1(Etw):
    pattern = Struct(
        "DomainId" / Int32ul,
        "CoordinationType" / Int8ul,
        "IdleProcessorsDiscounted" / Int8ul,
        "SchedulerDirectedTransitionsSupported" / Int8ul,
        "WorstCaseTransitionLatency" / Int32ul,
        "WorstCaseTransitionOverhead" / Int32ul,
        "AffinitizePerfSet" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=129, version=0)
class Microsoft_Windows_Kernel_Processor_Power_129_0(Etw):
    pattern = Struct(
        "DomainId" / Int32ul,
        "CoordinationType" / Int8ul,
        "IdleProcessorsDiscounted" / Int8ul,
        "SchedulerDirectedTransitionsSupported" / Int8ul,
        "WorstCaseTransitionLatency" / Int32ul,
        "WorstCaseTransitionOverhead" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=129, version=1)
class Microsoft_Windows_Kernel_Processor_Power_129_1(Etw):
    pattern = Struct(
        "DomainId" / Int32ul,
        "CoordinationType" / Int8ul,
        "IdleProcessorsDiscounted" / Int8ul,
        "SchedulerDirectedTransitionsSupported" / Int8ul,
        "WorstCaseTransitionLatency" / Int32ul,
        "WorstCaseTransitionOverhead" / Int32ul,
        "AffinitizePerfSet" / Int8ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=131, version=0)
class Microsoft_Windows_Kernel_Processor_Power_131_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Affinity" / Int64ul,
        "Class" / Int8ul,
        "DistributeCores" / Int8ul,
        "HistogramSize" / Int32ul,
        "ConcurrencyHistogram" / Int64ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=132, version=0)
class Microsoft_Windows_Kernel_Processor_Power_132_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Affinity" / Int64ul,
        "ParkHint" / Int64ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=133, version=0)
class Microsoft_Windows_Kernel_Processor_Power_133_0(Etw):
    pattern = Struct(
        "DomainMasterGroup" / Int16ul,
        "DomainMasterNumber" / Int8ul,
        "ProcessorId" / Int32ul,
        "BiosCap" / Int32ul,
        "ThermalCap" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=134, version=0)
class Microsoft_Windows_Kernel_Processor_Power_134_0(Etw):
    pattern = Struct(
        "DomainMasterGroup" / Int16ul,
        "DomainMasterNumber" / Int8ul,
        "ProcessorId" / Int32ul,
        "Cap" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=135, version=0)
class Microsoft_Windows_Kernel_Processor_Power_135_0(Etw):
    pattern = Struct(
        "DomainMasterGroup" / Int16ul,
        "DomainMasterNumber" / Int8ul,
        "ProcessorId" / Int32ul,
        "Cap" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=137, version=0)
class Microsoft_Windows_Kernel_Processor_Power_137_0(Etw):
    pattern = Struct(
        "Group" / Int16ul,
        "Processors" / Int64ul,
        "OldPark" / Int64ul,
        "NewPark" / Int64ul,
        "NewSoftPark" / Int64ul,
        "UnparkCap" / Int8ul,
        "UnparkFloor" / Int8ul,
        "ForceParkSet" / Int64ul,
        "ForceUnparkSet" / Int64ul,
        "OverUtilizedSet" / Int64ul,
        "IsolatedCores" / Int64ul,
        "IdealUnparkCount" / Int8ul,
        "UnparkCount" / Int8ul,
        "ParkReason" / Int32ul
    )


@declare(guid=guid("0f67e49f-fe51-4e9f-b490-6f2948cc6027"), event_id=138, version=0)
class Microsoft_Windows_Kernel_Processor_Power_138_0(Etw):
    pattern = Struct(
        "PpmCheckTime" / Int64ul,
        "Group" / Int16ul,
        "Number" / Int8ul,
        "SoftParked" / Int8ul
    )

