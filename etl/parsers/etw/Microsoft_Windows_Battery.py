# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Battery
GUID : 59819d0a-adaf-46b2-8d7c-990bc39c7c15
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("59819d0a-adaf-46b2-8d7c-990bc39c7c15"), event_id=1, version=0)
class Microsoft_Windows_Battery_1_0(Etw):
    pattern = Struct(
        "BatteryPresent" / Int8ul,
        "PowerState" / Int32ul,
        "Capacity" / Int32ul
    )


@declare(guid=guid("59819d0a-adaf-46b2-8d7c-990bc39c7c15"), event_id=2, version=0)
class Microsoft_Windows_Battery_2_0(Etw):
    pattern = Struct(
        "BatteryPresent" / Int8ul,
        "PowerState" / Int32ul,
        "Capacity" / Int32ul
    )


@declare(guid=guid("59819d0a-adaf-46b2-8d7c-990bc39c7c15"), event_id=3, version=0)
class Microsoft_Windows_Battery_3_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "BatteryPresent" / Int8ul
    )


@declare(guid=guid("59819d0a-adaf-46b2-8d7c-990bc39c7c15"), event_id=4, version=0)
class Microsoft_Windows_Battery_4_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "Revision" / Int32ul,
        "PowerUnit" / Int32ul,
        "DesignCapacity" / Int32ul,
        "LastFullChargeCapacity" / Int32ul,
        "BatteryTechnology" / Int32ul,
        "DesignVoltage" / Int32ul,
        "WarningDesignCapacity" / Int32ul,
        "LowDesignCapacity" / Int32ul,
        "CapacityGranularity1" / Int32ul,
        "CapacityGranularity2" / Int32ul,
        "CycleCount" / Int32ul,
        "MeasurementAccuracy" / Int32ul,
        "MaxSamplingTime" / Int32ul,
        "MinSamplingTIme" / Int32ul,
        "MaxAveragingInterval" / Int32ul,
        "MinAveragingInterval" / Int32ul,
        "ModelNumber" / CString,
        "SerialNumber" / CString,
        "BatteryType" / CString,
        "OemInformation" / CString
    )


@declare(guid=guid("59819d0a-adaf-46b2-8d7c-990bc39c7c15"), event_id=5, version=0)
class Microsoft_Windows_Battery_5_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "Revision" / Int32ul,
        "PowerUnit" / Int32ul,
        "DesignCapacity" / Int32ul,
        "LastFullChargeCapacity" / Int32ul,
        "BatteryTechnology" / Int32ul,
        "DesignVoltage" / Int32ul,
        "WarningDesignCapacity" / Int32ul,
        "LowDesignCapacity" / Int32ul,
        "CapacityGranularity1" / Int32ul,
        "CapacityGranularity2" / Int32ul,
        "CycleCount" / Int32ul,
        "MeasurementAccuracy" / Int32ul,
        "MaxSamplingTime" / Int32ul,
        "MinSamplingTIme" / Int32ul,
        "MaxAveragingInterval" / Int32ul,
        "MinAveragingInterval" / Int32ul,
        "ModelNumber" / CString,
        "SerialNumber" / CString,
        "BatteryType" / CString,
        "OemInformation" / CString
    )


@declare(guid=guid("59819d0a-adaf-46b2-8d7c-990bc39c7c15"), event_id=6, version=0)
class Microsoft_Windows_Battery_6_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "PowerUnit" / Int32ul,
        "DesignCapacity" / Int32ul,
        "LastFullChargeCapacity" / Int32ul,
        "BatteryTechnology" / Int32ul,
        "DesignVoltage" / Int32ul,
        "WarningDesignCapacity" / Int32ul,
        "LowDesignCapacity" / Int32ul,
        "CapacityGranularity1" / Int32ul,
        "CapacityGranularity2" / Int32ul,
        "ModelNumber" / CString,
        "SerialNumber" / CString,
        "BatteryType" / CString,
        "OemInformation" / CString
    )


@declare(guid=guid("59819d0a-adaf-46b2-8d7c-990bc39c7c15"), event_id=7, version=0)
class Microsoft_Windows_Battery_7_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "PowerUnit" / Int32ul,
        "DesignCapacity" / Int32ul,
        "LastFullChargeCapacity" / Int32ul,
        "BatteryTechnology" / Int32ul,
        "DesignVoltage" / Int32ul,
        "WarningDesignCapacity" / Int32ul,
        "LowDesignCapacity" / Int32ul,
        "CapacityGranularity1" / Int32ul,
        "CapacityGranularity2" / Int32ul,
        "ModelNumber" / CString,
        "SerialNumber" / CString,
        "BatteryType" / CString,
        "OemInformation" / CString
    )


@declare(guid=guid("59819d0a-adaf-46b2-8d7c-990bc39c7c15"), event_id=8, version=0)
class Microsoft_Windows_Battery_8_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "State" / Int32ul,
        "PresentRate" / Int32ul,
        "RemainingCapacity" / Int32ul,
        "PresentVoltage" / Int32ul
    )


@declare(guid=guid("59819d0a-adaf-46b2-8d7c-990bc39c7c15"), event_id=9, version=0)
class Microsoft_Windows_Battery_9_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "State" / Int32ul,
        "PresentRate" / Int32ul,
        "RemainingCapacity" / Int32ul,
        "PresentVoltage" / Int32ul
    )


@declare(guid=guid("59819d0a-adaf-46b2-8d7c-990bc39c7c15"), event_id=10, version=0)
class Microsoft_Windows_Battery_10_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "TripPoint" / Int32ul
    )


@declare(guid=guid("59819d0a-adaf-46b2-8d7c-990bc39c7c15"), event_id=11, version=0)
class Microsoft_Windows_Battery_11_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "TripPoint" / Int32ul
    )


@declare(guid=guid("59819d0a-adaf-46b2-8d7c-990bc39c7c15"), event_id=12, version=0)
class Microsoft_Windows_Battery_12_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "Notification" / Int32ul
    )


@declare(guid=guid("59819d0a-adaf-46b2-8d7c-990bc39c7c15"), event_id=13, version=0)
class Microsoft_Windows_Battery_13_0(Etw):
    pattern = Struct(
        "RemainingPercentage" / Int32ul,
        "PercentageChange" / Int32sl,
        "AcDc" / Int32ul,
        "ElapsedTimeMs" / Int32ul
    )


@declare(guid=guid("59819d0a-adaf-46b2-8d7c-990bc39c7c15"), event_id=14, version=0)
class Microsoft_Windows_Battery_14_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "BatteryState" / Int32ul,
        "WatchdogState" / Int32ul,
        "WatchdogTimeout" / Int32ul
    )


@declare(guid=guid("59819d0a-adaf-46b2-8d7c-990bc39c7c15"), event_id=15, version=0)
class Microsoft_Windows_Battery_15_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "BatteryState" / Int32ul,
        "WatchdogState" / Int32ul,
        "WatchdogTimeout" / Int32ul
    )

