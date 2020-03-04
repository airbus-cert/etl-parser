# -*- coding: utf-8 -*-
"""
Microsoft-Windows-UserModePowerService
GUID : ce8dee0b-d539-4000-b0f8-77bed049c590
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=1, version=0)
class Microsoft_Windows_UserModePowerService_1_0(Etw):
    pattern = Struct(
        "PlatformRole" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=2, version=0)
class Microsoft_Windows_UserModePowerService_2_0(Etw):
    pattern = Struct(
        "SchemeGuid" / Guid
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=3, version=0)
class Microsoft_Windows_UserModePowerService_3_0(Etw):
    pattern = Struct(
        "SubgroupGuid" / Guid,
        "SettingGuid" / Guid,
        "ValueIndex" / Int32ul,
        "Type" / Int32ul,
        "DataSize" / Int32ul,
        "Data" / Bytes(lambda this: this.DataSize)
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=4, version=0)
class Microsoft_Windows_UserModePowerService_4_0(Etw):
    pattern = Struct(
        "SubgroupGuid" / Guid,
        "SettingGuid" / Guid,
        "ValueIndex" / Int32ul,
        "Type" / Int32ul,
        "DataSize" / Int32ul,
        "Data" / Bytes(lambda this: this.DataSize)
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=5, version=0)
class Microsoft_Windows_UserModePowerService_5_0(Etw):
    pattern = Struct(
        "Timeout" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=7, version=0)
class Microsoft_Windows_UserModePowerService_7_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=8, version=0)
class Microsoft_Windows_UserModePowerService_8_0(Etw):
    pattern = Struct(
        "DeviceName" / WString,
        "ManufacturerName" / WString,
        "ManufactureDay" / Int8ul,
        "ManufactureMonth" / Int8ul,
        "ManufactureYear" / Int16ul,
        "SerialNumber" / WString,
        "Capabilities" / Int32ul,
        "Technology" / Int8ul,
        "Chemistry" / CString,
        "DesignCapacity" / Int32ul,
        "FullChargeCapacity" / Int32ul,
        "DefaultAlert1" / Int32ul,
        "DefaultAlert2" / Int32ul,
        "CriticalBias" / Int32ul,
        "CycleCount" / Int32ul,
        "GranularityScaleCount" / Int32ul,
        "GranularityScale" / Sid,
        "UniqueId" / WString
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=9, version=0)
class Microsoft_Windows_UserModePowerService_9_0(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "Capacity" / Int32ul,
        "Voltage" / Int32ul,
        "Rate" / Int32sl,
        "EstimatedRuntime" / Int32ul,
        "UniqueId" / WString
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=10, version=0)
class Microsoft_Windows_UserModePowerService_10_0(Etw):
    pattern = Struct(
        "BrightnessCapable" / Int8ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=11, version=0)
class Microsoft_Windows_UserModePowerService_11_0(Etw):
    pattern = Struct(
        "AcOnline" / Int8ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=12, version=0)
class Microsoft_Windows_UserModePowerService_12_0(Etw):
    pattern = Struct(
        "ProcessPath" / WString,
        "ProcessPid" / Int32ul,
        "OldSchemeGuid" / Guid,
        "NewSchemeGuid" / Guid
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=13, version=0)
class Microsoft_Windows_UserModePowerService_13_0(Etw):
    pattern = Struct(
        "MeterId" / Int64ul,
        "value" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=14, version=0)
class Microsoft_Windows_UserModePowerService_14_0(Etw):
    pattern = Struct(
        "MeterId" / Int64ul,
        "SamplingPeriod" / Int64ul,
        "MeterNameLength" / Int32ul,
        "MeterName" / Bytes(lambda this: this.MeterNameLength),
        "MeteredHardwareCount" / Int32ul,
        "MeteredHardwareName" / WString
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=15, version=0)
class Microsoft_Windows_UserModePowerService_15_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "ProcessorVendor" / Int32ul,
        "ProcessorType" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=16, version=0)
class Microsoft_Windows_UserModePowerService_16_0(Etw):
    pattern = Struct(
        "SchemeGuid" / Guid,
        "SubgroupGuid" / Guid,
        "SettingGuid" / Guid,
        "Flags" / Int32ul,
        "DataType" / Int32ul,
        "DataSize" / Int32ul,
        "Data" / Bytes(lambda this: this.DataSize)
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=16, version=1)
class Microsoft_Windows_UserModePowerService_16_1(Etw):
    pattern = Struct(
        "SchemeGuid" / Guid,
        "SubgroupGuid" / Guid,
        "SettingGuid" / Guid,
        "Flags" / Int32ul,
        "DataType" / Int32ul,
        "DataSize" / Int32ul,
        "Data" / Bytes(lambda this: this.DataSize),
        "ProfileGuid" / Guid
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=17, version=0)
class Microsoft_Windows_UserModePowerService_17_0(Etw):
    pattern = Struct(
        "ProfileGuid" / Guid,
        "SubgroupGuid" / Guid,
        "SettingGuid" / Guid,
        "SchemePersonalityGuid" / Guid,
        "Flags" / Int32ul,
        "ValueIndex" / Int32ul,
        "Type" / Int32ul,
        "DataSize" / Int32ul,
        "Data" / Bytes(lambda this: this.DataSize)
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=18, version=0)
class Microsoft_Windows_UserModePowerService_18_0(Etw):
    pattern = Struct(
        "MeterId" / Int64ul,
        "AbsoluteEnergy" / Int64ul,
        "AbsoluteTime" / Int64ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=19, version=0)
class Microsoft_Windows_UserModePowerService_19_0(Etw):
    pattern = Struct(
        "MeterId" / Int64ul,
        "SamplingPeriod" / Int64ul,
        "ChannelNameLength" / Int32ul,
        "ChannelName" / Bytes(lambda this: this.ChannelNameLength)
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=22, version=0)
class Microsoft_Windows_UserModePowerService_22_0(Etw):
    pattern = Struct(
        "Turn" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=23, version=0)
class Microsoft_Windows_UserModePowerService_23_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=24, version=0)
class Microsoft_Windows_UserModePowerService_24_0(Etw):
    pattern = Struct(
        "Event" / Int32ul,
        "SessionId" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=25, version=0)
class Microsoft_Windows_UserModePowerService_25_0(Etw):
    pattern = Struct(
        "UserContextToken" / Int64ul,
        "SessionId" / Int32ul,
        "UserSid" / Sid
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=26, version=0)
class Microsoft_Windows_UserModePowerService_26_0(Etw):
    pattern = Struct(
        "Event" / Int32ul,
        "UserContextToken" / Int64ul,
        "SessionId" / Int32ul,
        "UserSid" / Sid
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=27, version=0)
class Microsoft_Windows_UserModePowerService_27_0(Etw):
    pattern = Struct(
        "Supported" / Int8ul,
        "GlobalUserPresent" / Int8ul,
        "UserPredictionMode" / Int32ul,
        "MinConfidence" / Int8ul,
        "SuspendCount" / Int32ul,
        "LastUserAwayEndSystemTime" / Int64ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=28, version=0)
class Microsoft_Windows_UserModePowerService_28_0(Etw):
    pattern = Struct(
        "UserSid" / Sid,
        "IntervalCount" / Int32ul,
        "AwayIntervals" / Int8sl
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=28, version=1)
class Microsoft_Windows_UserModePowerService_28_1(Etw):
    pattern = Struct(
        "UserSid" / Sid,
        "IntervalCount" / Int32ul,
        "AwayIntervals" / Int8ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=29, version=0)
class Microsoft_Windows_UserModePowerService_29_0(Etw):
    pattern = Struct(
        "UserSid" / Sid,
        "IntervalCount" / Int32ul,
        "AwayIntervals" / Int8sl
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=29, version=1)
class Microsoft_Windows_UserModePowerService_29_1(Etw):
    pattern = Struct(
        "UserSid" / Sid,
        "IntervalCount" / Int32ul,
        "AwayIntervals" / Int8ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=30, version=0)
class Microsoft_Windows_UserModePowerService_30_0(Etw):
    pattern = Struct(
        "UserSid" / Sid
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=31, version=0)
class Microsoft_Windows_UserModePowerService_31_0(Etw):
    pattern = Struct(
        "UserAwayEndSystemTime" / Int64ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=32, version=0)
class Microsoft_Windows_UserModePowerService_32_0(Etw):
    pattern = Struct(
        "Suspend" / Int8ul,
        "SuspendCount" / Int32ul,
        "GlobalUserPresent" / Int8ul,
        "UserPredictionMode" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=33, version=0)
class Microsoft_Windows_UserModePowerService_33_0(Etw):
    pattern = Struct(
        "SystemTimeShift" / Int64sl
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=34, version=0)
class Microsoft_Windows_UserModePowerService_34_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Id" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=35, version=0)
class Microsoft_Windows_UserModePowerService_35_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Id" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=36, version=0)
class Microsoft_Windows_UserModePowerService_36_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Id" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=37, version=0)
class Microsoft_Windows_UserModePowerService_37_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Id" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=38, version=0)
class Microsoft_Windows_UserModePowerService_38_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Id" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=39, version=0)
class Microsoft_Windows_UserModePowerService_39_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Id" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=40, version=0)
class Microsoft_Windows_UserModePowerService_40_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Id" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=41, version=0)
class Microsoft_Windows_UserModePowerService_41_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Id" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=42, version=0)
class Microsoft_Windows_UserModePowerService_42_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Id" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=43, version=0)
class Microsoft_Windows_UserModePowerService_43_0(Etw):
    pattern = Struct(
        "EffectiveBrightnessPercentage" / Int32ul,
        "EffectiveBrightnessMillinits" / Int32ul,
        "NewBrightnessTransitionTime" / Int32ul,
        "DimmingTransitionTime" / Int32ul,
        "DimmedBrightnessPercentage" / Int32ul,
        "DimmedBrightnessMillinits" / Int32ul,
        "NewDimmedTransitionTime" / Int32ul,
        "UnDimmingTransitionTime" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=44, version=0)
class Microsoft_Windows_UserModePowerService_44_0(Etw):
    pattern = Struct(
        "TimeInStandby" / Int32ul,
        "RemainingBatteryPercentage" / Int32ul,
        "RemainingBatteryTime" / Int32ul,
        "ReserveBatteryTime" / Int32ul,
        "ExecuteAction" / Int8ul,
        "RejectReason" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=44, version=1)
class Microsoft_Windows_UserModePowerService_44_1(Etw):
    pattern = Struct(
        "TimeInStandby" / Int32ul,
        "GracePeriod" / Int32ul,
        "RemainingBatteryPercentage" / Int32ul,
        "RemainingBatteryTime" / Int32ul,
        "ReserveBatteryTime" / Int32ul,
        "ExecuteAction" / Int8ul,
        "RejectReason" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=44, version=2)
class Microsoft_Windows_UserModePowerService_44_2(Etw):
    pattern = Struct(
        "TimeInStandby" / Int32ul,
        "GracePeriod" / Int32ul,
        "RemainingBatteryPercentage" / Int32ul,
        "RemainingBatteryTime" / Int32ul,
        "ReserveBatteryTime" / Int32ul,
        "ExecuteAction" / Int8ul,
        "RejectReason" / Int32ul,
        "DataSources" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=44, version=3)
class Microsoft_Windows_UserModePowerService_44_3(Etw):
    pattern = Struct(
        "TimeInStandby" / Int32ul,
        "GracePeriod" / Int32ul,
        "RemainingBatteryPercentage" / Int32ul,
        "RemainingBatteryTime" / Int32ul,
        "ReserveBatteryTime" / Int32ul,
        "ExecuteAction" / Int8ul,
        "RejectReason" / Int32ul,
        "DataSources" / Int32ul,
        "CsSessionId" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=45, version=0)
class Microsoft_Windows_UserModePowerService_45_0(Etw):
    pattern = Struct(
        "TimeInStandby" / Int32ul,
        "RemainingBatteryPercentage" / Int32ul,
        "StandbyBatteryDrainPercentage" / Int32ul,
        "BatteryDrainPercentageThreshold" / Int32ul,
        "ExecuteAction" / Int8ul,
        "RejectReason" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=45, version=1)
class Microsoft_Windows_UserModePowerService_45_1(Etw):
    pattern = Struct(
        "TimeInStandby" / Int32ul,
        "GracePeriod" / Int32ul,
        "RemainingBatteryPercentage" / Int32ul,
        "StandbyBatteryDrainPercentage" / Int32ul,
        "BatteryDrainPercentageThreshold" / Int32ul,
        "ExecuteAction" / Int8ul,
        "RejectReason" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=45, version=2)
class Microsoft_Windows_UserModePowerService_45_2(Etw):
    pattern = Struct(
        "TimeInStandby" / Int32ul,
        "GracePeriod" / Int32ul,
        "RemainingBatteryPercentage" / Int32ul,
        "StandbyBatteryDrainPercentage" / Int32ul,
        "BatteryDrainPercentageThreshold" / Int32ul,
        "ExecuteAction" / Int8ul,
        "RejectReason" / Int32ul,
        "DataSources" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=45, version=3)
class Microsoft_Windows_UserModePowerService_45_3(Etw):
    pattern = Struct(
        "TimeInStandby" / Int32ul,
        "GracePeriod" / Int32ul,
        "RemainingBatteryPercentage" / Int32ul,
        "StandbyBatteryDrainPercentage" / Int32ul,
        "BatteryDrainPercentageThreshold" / Int32ul,
        "ExecuteAction" / Int8ul,
        "RejectReason" / Int32ul,
        "DataSources" / Int32ul,
        "CsSessionId" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=46, version=0)
class Microsoft_Windows_UserModePowerService_46_0(Etw):
    pattern = Struct(
        "ActualTimeRange" / Int32ul,
        "RemainingBatteryPercentage" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=47, version=0)
class Microsoft_Windows_UserModePowerService_47_0(Etw):
    pattern = Struct(
        "Action" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=48, version=0)
class Microsoft_Windows_UserModePowerService_48_0(Etw):
    pattern = Struct(
        "Id" / Int8ul,
        "GpuCount" / Int8ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=49, version=0)
class Microsoft_Windows_UserModePowerService_49_0(Etw):
    pattern = Struct(
        "OverlaySchemeGuid" / Guid,
        "SubgroupGuid" / Guid,
        "SettingGuid" / Guid,
        "Flags" / Int32ul,
        "ValueIndex" / Int32ul,
        "Type" / Int32ul,
        "DataSize" / Int32ul,
        "Data" / Bytes(lambda this: this.DataSize)
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=50, version=0)
class Microsoft_Windows_UserModePowerService_50_0(Etw):
    pattern = Struct(
        "SchemeGuid" / Guid
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=50, version=1)
class Microsoft_Windows_UserModePowerService_50_1(Etw):
    pattern = Struct(
        "SchemeGuid" / Guid,
        "AcOverlay" / Int8ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=51, version=0)
class Microsoft_Windows_UserModePowerService_51_0(Etw):
    pattern = Struct(
        "ProcessPath" / WString,
        "ProcessPid" / Int32ul,
        "OldSchemeGuid" / Guid,
        "NewSchemeGuid" / Guid
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=52, version=0)
class Microsoft_Windows_UserModePowerService_52_0(Etw):
    pattern = Struct(
        "SchemeGuid" / Guid
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=53, version=0)
class Microsoft_Windows_UserModePowerService_53_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=54, version=0)
class Microsoft_Windows_UserModePowerService_54_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Suspend" / Int8ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=56, version=0)
class Microsoft_Windows_UserModePowerService_56_0(Etw):
    pattern = Struct(
        "SchemeGuid" / Guid,
        "SubgroupGuid" / Guid,
        "SettingGuid" / Guid,
        "Flags" / Int32ul,
        "DataType" / Int32ul,
        "DataSize" / Int32ul,
        "Data" / Bytes(lambda this: this.DataSize),
        "ProfileGuid" / Guid
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=57, version=0)
class Microsoft_Windows_UserModePowerService_57_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul
    )


@declare(guid=guid("ce8dee0b-d539-4000-b0f8-77bed049c590"), event_id=58, version=0)
class Microsoft_Windows_UserModePowerService_58_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul
    )

