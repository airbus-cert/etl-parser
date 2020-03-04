# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SrumTelemetry
GUID : 48d445a8-2f64-4d49-b093-a5774d8dc531
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("48d445a8-2f64-4d49-b093-a5774d8dc531"), event_id=2003, version=0)
class Microsoft_Windows_SrumTelemetry_2003_0(Etw):
    pattern = Struct(
        "BatteryDrainRate" / Int32ul,
        "PowerBitpack" / Int32ul,
        "Duration" / Int32ul,
        "AppCpuCyclesBitpack" / Int32ul,
        "TimeStamp" / WString
    )


@declare(guid=guid("48d445a8-2f64-4d49-b093-a5774d8dc531"), event_id=2004, version=0)
class Microsoft_Windows_SrumTelemetry_2004_0(Etw):
    pattern = Struct(
        "JoulesPerHourScreenOnDC" / Int32ul,
        "JoulesPerHourScreenOffDC" / Int32ul,
        "DCTimeBitpack" / Int32ul,
        "CPUCyclesOnDCBitpack" / Int32ul,
        "DiskMBRead" / Int32ul,
        "DiskMBWritten" / Int32ul
    )


@declare(guid=guid("48d445a8-2f64-4d49-b093-a5774d8dc531"), event_id=2005, version=0)
class Microsoft_Windows_SrumTelemetry_2005_0(Etw):
    pattern = Struct(
        "PowerInMilliwatts" / Int32ul,
        "CpuStatsBitpack" / Int32ul,
        "DiskAndNetStatsBitPack" / Int32ul,
        "DurationBitPack" / Int32ul,
        "ModernAppPackageName" / WString
    )


@declare(guid=guid("48d445a8-2f64-4d49-b093-a5774d8dc531"), event_id=3003, version=0)
class Microsoft_Windows_SrumTelemetry_3003_0(Etw):
    pattern = Struct(
        "PreviousBrightnessLevel" / Int32sl,
        "PreviousBrightnessDurationInSeconds" / Int32ul,
        "NewBrightnessLevel" / Int32sl
    )


@declare(guid=guid("48d445a8-2f64-4d49-b093-a5774d8dc531"), event_id=3004, version=0)
class Microsoft_Windows_SrumTelemetry_3004_0(Etw):
    pattern = Struct(
        "CurrentBrightnessLevel" / Int32sl
    )


@declare(guid=guid("48d445a8-2f64-4d49-b093-a5774d8dc531"), event_id=3005, version=0)
class Microsoft_Windows_SrumTelemetry_3005_0(Etw):
    pattern = Struct(
        "PreviousStateDurationInSeconds" / Int32ul,
        "NewEnergySaverState" / Int8sl
    )


@declare(guid=guid("48d445a8-2f64-4d49-b093-a5774d8dc531"), event_id=3006, version=0)
class Microsoft_Windows_SrumTelemetry_3006_0(Etw):
    pattern = Struct(
        "TimeStamp" / SystemTime,
        "AppId" / WString,
        "UserId" / WString,
        "EnergyLoss" / Int64ul,
        "CpuEnergyConsumption" / Int64ul,
        "SocEnergyConsumption" / Int64ul,
        "DisplayEnergyConsumption" / Int64ul,
        "DiskEnergyConsumption" / Int64ul,
        "NetworkEnergyConsumption" / Int64ul,
        "MbbEnergyConsumption" / Int64ul,
        "OtherEnergyConsumption" / Int64ul,
        "TotalEnergyConsumption" / Int64ul,
        "MeasuredPower" / Int8ul,
        "OnBattery" / Int8ul,
        "Foreground" / Int8ul,
        "ScreenOn" / Int8ul,
        "BatterySaverActive" / Int8ul,
        "LowPowerEpochActive" / Int8ul
    )

