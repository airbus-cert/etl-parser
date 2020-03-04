# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-Power
GUID : 331c3b3a-2005-44c2-ac5e-77220c37d6b4
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=1, version=0)
class Microsoft_Windows_Kernel_Power_1_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "Time" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=2, version=0)
class Microsoft_Windows_Kernel_Power_2_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "Time" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=4, version=0)
class Microsoft_Windows_Kernel_Power_4_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=6, version=0)
class Microsoft_Windows_Kernel_Power_6_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=7, version=0)
class Microsoft_Windows_Kernel_Power_7_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "PowerStateType" / Int32ul,
        "MinorFunction" / Int8ul,
        "TargetDevice" / Int64ul,
        "InstanceNameLength" / Int16ul,
        "InstanceName" / Bytes(lambda this: this.InstanceNameLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=7, version=1)
class Microsoft_Windows_Kernel_Power_7_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "PowerStateType" / Int32ul,
        "MinorFunction" / Int8ul,
        "TargetDevice" / Int64ul,
        "InstanceNameLength" / Int16ul,
        "InstanceName" / Bytes(lambda this: this.InstanceNameLength),
        "PowerState" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=8, version=0)
class Microsoft_Windows_Kernel_Power_8_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Status" / Int32ul,
        "FailedDriver" / WString
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=9, version=0)
class Microsoft_Windows_Kernel_Power_9_0(Etw):
    pattern = Struct(
        "Pid" / Int32ul,
        "Window" / Int64ul,
        "AppNameLength" / Int16ul,
        "AppName" / Bytes(lambda this: this.AppNameLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=10, version=0)
class Microsoft_Windows_Kernel_Power_10_0(Etw):
    pattern = Struct(
        "Pid" / Int32ul,
        "ServiceNameLength" / Int16ul,
        "ServiceName" / Bytes(lambda this: this.ServiceNameLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=11, version=0)
class Microsoft_Windows_Kernel_Power_11_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=12, version=0)
class Microsoft_Windows_Kernel_Power_12_0(Etw):
    pattern = Struct(
        "Pid" / Int32ul,
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=13, version=0)
class Microsoft_Windows_Kernel_Power_13_0(Etw):
    pattern = Struct(
        "Pid" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=14, version=0)
class Microsoft_Windows_Kernel_Power_14_0(Etw):
    pattern = Struct(
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=15, version=0)
class Microsoft_Windows_Kernel_Power_15_0(Etw):
    pattern = Struct(
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=16, version=0)
class Microsoft_Windows_Kernel_Power_16_0(Etw):
    pattern = Struct(
        "Pid" / Int32ul,
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=17, version=0)
class Microsoft_Windows_Kernel_Power_17_0(Etw):
    pattern = Struct(
        "Pid" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=18, version=0)
class Microsoft_Windows_Kernel_Power_18_0(Etw):
    pattern = Struct(
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=19, version=0)
class Microsoft_Windows_Kernel_Power_19_0(Etw):
    pattern = Struct(
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=20, version=0)
class Microsoft_Windows_Kernel_Power_20_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Device" / Int64ul,
        "DriverName" / WString
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=21, version=0)
class Microsoft_Windows_Kernel_Power_21_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Device" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=28, version=0)
class Microsoft_Windows_Kernel_Power_28_0(Etw):
    pattern = Struct(
        "Pid" / Int32ul,
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=29, version=0)
class Microsoft_Windows_Kernel_Power_29_0(Etw):
    pattern = Struct(
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=32, version=0)
class Microsoft_Windows_Kernel_Power_32_0(Etw):
    pattern = Struct(
        "Pid" / Int32ul,
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=33, version=0)
class Microsoft_Windows_Kernel_Power_33_0(Etw):
    pattern = Struct(
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=34, version=0)
class Microsoft_Windows_Kernel_Power_34_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=35, version=0)
class Microsoft_Windows_Kernel_Power_35_0(Etw):
    pattern = Struct(
        "Query" / Int8ul,
        "TargetState" / Int32ul,
        "EffectiveState" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=39, version=0)
class Microsoft_Windows_Kernel_Power_39_0(Etw):
    pattern = Struct(
        "SleepTime" / Int32ul,
        "ResumeTime" / Int32ul,
        "DriverWakeTime" / Int32ul,
        "HiberWriteTime" / Int32ul,
        "HiberReadTime" / Int32ul,
        "HiberPagesWritten" / Int32ul,
        "BiosInitTime" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=39, version=1)
class Microsoft_Windows_Kernel_Power_39_1(Etw):
    pattern = Struct(
        "SleepTime" / Int32ul,
        "ResumeTime" / Int32ul,
        "DriverWakeTime" / Int32ul,
        "HiberWriteTime" / Int32ul,
        "HiberReadTime" / Int32ul,
        "HiberPagesWritten" / Int32ul,
        "BiosInitTime" / Int32ul,
        "CheckpointTime" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=40, version=0)
class Microsoft_Windows_Kernel_Power_40_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength),
        "InstanceNameLength" / Int16ul,
        "InstanceName" / Bytes(lambda this: this.InstanceNameLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=41, version=1)
class Microsoft_Windows_Kernel_Power_41_1(Etw):
    pattern = Struct(
        "BugcheckCode" / Int32ul,
        "BugcheckParameter" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=41, version=2)
class Microsoft_Windows_Kernel_Power_41_2(Etw):
    pattern = Struct(
        "BugcheckCode" / Int32ul,
        "BugcheckParameter1" / Int64ul,
        "BugcheckParameter2" / Int64ul,
        "BugcheckParameter3" / Int64ul,
        "BugcheckParameter4" / Int64ul,
        "SleepInProgress" / Int8ul,
        "PowerButtonTimestamp" / Int64ul,
        "BootAppStatus" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=41, version=3)
class Microsoft_Windows_Kernel_Power_41_3(Etw):
    pattern = Struct(
        "BugcheckCode" / Int32ul,
        "BugcheckParameter1" / Int64ul,
        "BugcheckParameter2" / Int64ul,
        "BugcheckParameter3" / Int64ul,
        "BugcheckParameter4" / Int64ul,
        "SleepInProgress" / Int32ul,
        "PowerButtonTimestamp" / Int64ul,
        "BootAppStatus" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=41, version=4)
class Microsoft_Windows_Kernel_Power_41_4(Etw):
    pattern = Struct(
        "BugcheckCode" / Int32ul,
        "BugcheckParameter1" / Int64ul,
        "BugcheckParameter2" / Int64ul,
        "BugcheckParameter3" / Int64ul,
        "BugcheckParameter4" / Int64ul,
        "SleepInProgress" / Int32ul,
        "PowerButtonTimestamp" / Int64ul,
        "BootAppStatus" / Int32ul,
        "Checkpoint" / Int8ul,
        "ConnectedStandbyInProgress" / Int8ul,
        "SystemSleepTransitionsToOn" / Int32ul,
        "CsEntryScenarioInstanceId" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=41, version=5)
class Microsoft_Windows_Kernel_Power_41_5(Etw):
    pattern = Struct(
        "BugcheckCode" / Int32ul,
        "BugcheckParameter1" / Int64ul,
        "BugcheckParameter2" / Int64ul,
        "BugcheckParameter3" / Int64ul,
        "BugcheckParameter4" / Int64ul,
        "SleepInProgress" / Int32ul,
        "PowerButtonTimestamp" / Int64ul,
        "BootAppStatus" / Int32ul,
        "Checkpoint" / Int8ul,
        "ConnectedStandbyInProgress" / Int8ul,
        "SystemSleepTransitionsToOn" / Int32ul,
        "CsEntryScenarioInstanceId" / Int8ul,
        "BugcheckInfoFromEFI" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=41, version=6)
class Microsoft_Windows_Kernel_Power_41_6(Etw):
    pattern = Struct(
        "BugcheckCode" / Int32ul,
        "BugcheckParameter1" / Int64ul,
        "BugcheckParameter2" / Int64ul,
        "BugcheckParameter3" / Int64ul,
        "BugcheckParameter4" / Int64ul,
        "SleepInProgress" / Int32ul,
        "PowerButtonTimestamp" / Int64ul,
        "BootAppStatus" / Int32ul,
        "Checkpoint" / Int8ul,
        "ConnectedStandbyInProgress" / Int8ul,
        "SystemSleepTransitionsToOn" / Int32ul,
        "CsEntryScenarioInstanceId" / Int8ul,
        "BugcheckInfoFromEFI" / Int8ul,
        "CheckpointStatus" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=42, version=0)
class Microsoft_Windows_Kernel_Power_42_0(Etw):
    pattern = Struct(
        "TargetState" / Int32ul,
        "EffectiveState" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=42, version=2)
class Microsoft_Windows_Kernel_Power_42_2(Etw):
    pattern = Struct(
        "TargetState" / Int32ul,
        "EffectiveState" / Int32ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=42, version=3)
class Microsoft_Windows_Kernel_Power_42_3(Etw):
    pattern = Struct(
        "TargetState" / Int32ul,
        "EffectiveState" / Int32ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "TransitionsToOn" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=60, version=0)
class Microsoft_Windows_Kernel_Power_60_0(Etw):
    pattern = Struct(
        "Value" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=61, version=0)
class Microsoft_Windows_Kernel_Power_61_0(Etw):
    pattern = Struct(
        "Value" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=62, version=0)
class Microsoft_Windows_Kernel_Power_62_0(Etw):
    pattern = Struct(
        "ExecutionState" / Int32ul,
        "AppNameLength" / Int16ul,
        "AppName" / Bytes(lambda this: this.AppNameLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=62, version=1)
class Microsoft_Windows_Kernel_Power_62_1(Etw):
    pattern = Struct(
        "ExecutionState" / Int32ul,
        "AppNameLength" / Int16ul,
        "AppName" / Bytes(lambda this: this.AppNameLength),
        "Pid" / Int32ul,
        "Tid" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=63, version=0)
class Microsoft_Windows_Kernel_Power_63_0(Etw):
    pattern = Struct(
        "ExecutionState" / Int32ul,
        "AppNameLength" / Int16ul,
        "AppName" / Bytes(lambda this: this.AppNameLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=63, version=1)
class Microsoft_Windows_Kernel_Power_63_1(Etw):
    pattern = Struct(
        "RequestedResolution" / Int32ul,
        "Pid" / Int32ul,
        "AppNameLength" / Int16ul,
        "AppName" / Bytes(lambda this: this.AppNameLength),
        "SubProcessTag" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=72, version=0)
class Microsoft_Windows_Kernel_Power_72_0(Etw):
    pattern = Struct(
        "Threshold" / Int32ul,
        "LowestIdleness" / Int32ul,
        "AverageIdleness" / Int32ul,
        "AccruedIdleTime" / Int32ul,
        "NonIdleIgnored" / Int8ul,
        "IdleToSleep" / Int8ul,
        "NonIdleReferences" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=73, version=0)
class Microsoft_Windows_Kernel_Power_73_0(Etw):
    pattern = Struct(
        "ExecutionState" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=74, version=0)
class Microsoft_Windows_Kernel_Power_74_0(Etw):
    pattern = Struct(
        "ExecutionState" / Int32ul,
        "StateHandle" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=77, version=0)
class Microsoft_Windows_Kernel_Power_77_0(Etw):
    pattern = Struct(
        "Device" / Int64ul,
        "Pdo" / Int64ul,
        "InstancePathLength" / Int16ul,
        "InstancePath" / Bytes(lambda this: this.InstancePathLength),
        "ConservativeTimeout" / Int32ul,
        "PerformanceTimeout" / Int32ul,
        "IdleTime" / Int32ul,
        "BusyCount" / Int32ul,
        "TotalBusyCount" / Int32ul,
        "IdlePowerState" / Int8ul,
        "CurrentPowerState" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=78, version=0)
class Microsoft_Windows_Kernel_Power_78_0(Etw):
    pattern = Struct(
        "Device" / Int64ul,
        "Timeout" / Int32ul,
        "IgnoreThreshold" / Int32ul,
        "IdleTime" / Int32ul,
        "NonIdleTime" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=79, version=0)
class Microsoft_Windows_Kernel_Power_79_0(Etw):
    pattern = Struct(
        "Disabled" / Int8ul,
        "Overridden" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=80, version=0)
class Microsoft_Windows_Kernel_Power_80_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "CoolingModeLength" / Int16ul,
        "CoolingMode" / Bytes(lambda this: this.CoolingModeLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=81, version=0)
class Microsoft_Windows_Kernel_Power_81_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "EventTime" / Int64ul,
        "PassiveCoolingStateLength" / Int16ul,
        "PassiveCoolingState" / Bytes(lambda this: this.PassiveCoolingStateLength),
        "AffinityCount" / Int16ul,
        "_PSV" / Int32ul,
        "_TMP" / Int32ul,
        "_TC1" / Int32ul,
        "_TC2" / Int32ul,
        "_TSP" / Int32ul,
        "DeltaP" / Int32sl,
        "_PSL" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=82, version=0)
class Microsoft_Windows_Kernel_Power_82_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "EventTime" / Int64ul,
        "PassiveCoolingStateLength" / Int16ul,
        "PassiveCoolingState" / Bytes(lambda this: this.PassiveCoolingStateLength),
        "AffinityCount" / Int16ul,
        "_PSV" / Int32ul,
        "_TMP" / Int32ul,
        "_TC1" / Int32ul,
        "_TC2" / Int32ul,
        "_TSP" / Int32ul,
        "DeltaP" / Int32sl,
        "_PSL" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=83, version=0)
class Microsoft_Windows_Kernel_Power_83_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "EventTime" / Int64ul,
        "ActiveCoolingStateLength" / Int16ul,
        "ActiveCoolingState" / Bytes(lambda this: this.ActiveCoolingStateLength),
        "_AC0" / Int32ul,
        "_AC1" / Int32ul,
        "_AC2" / Int32ul,
        "_AC3" / Int32ul,
        "_AC4" / Int32ul,
        "_AC5" / Int32ul,
        "_AC6" / Int32ul,
        "_AC7" / Int32ul,
        "_AC8" / Int32ul,
        "_AC9" / Int32ul,
        "_TMP" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=84, version=0)
class Microsoft_Windows_Kernel_Power_84_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "EventTime" / Int64ul,
        "ActiveCoolingStateLength" / Int16ul,
        "ActiveCoolingState" / Bytes(lambda this: this.ActiveCoolingStateLength),
        "_AC0" / Int32ul,
        "_AC1" / Int32ul,
        "_AC2" / Int32ul,
        "_AC3" / Int32ul,
        "_AC4" / Int32ul,
        "_AC5" / Int32ul,
        "_AC6" / Int32ul,
        "_AC7" / Int32ul,
        "_AC8" / Int32ul,
        "_AC9" / Int32ul,
        "_TMP" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=85, version=0)
class Microsoft_Windows_Kernel_Power_85_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "ShutdownTime" / Int64ul,
        "_CRT" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=86, version=0)
class Microsoft_Windows_Kernel_Power_86_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "ShutdownTime" / Int64ul,
        "_CRT" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=87, version=0)
class Microsoft_Windows_Kernel_Power_87_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "HibernateTime" / Int64ul,
        "_HOT" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=88, version=0)
class Microsoft_Windows_Kernel_Power_88_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "HibernateTime" / Int64ul,
        "_HOT" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=89, version=0)
class Microsoft_Windows_Kernel_Power_89_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "AffinityCount" / Int16ul,
        "_PSV" / Int32ul,
        "_TC1" / Int32ul,
        "_TC2" / Int32ul,
        "_TSP" / Int32ul,
        "_AC0" / Int32ul,
        "_AC1" / Int32ul,
        "_AC2" / Int32ul,
        "_AC3" / Int32ul,
        "_AC4" / Int32ul,
        "_AC5" / Int32ul,
        "_AC6" / Int32ul,
        "_AC7" / Int32ul,
        "_AC8" / Int32ul,
        "_AC9" / Int32ul,
        "_CRT" / Int32ul,
        "_HOT" / Int32ul,
        "_PSL" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=90, version=0)
class Microsoft_Windows_Kernel_Power_90_0(Etw):
    pattern = Struct(
        "ProcessorId" / Int32ul,
        "ThrottleMSR" / Int64ul,
        "ElapsedTime" / Int32ul,
        "LogInterval" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=91, version=0)
class Microsoft_Windows_Kernel_Power_91_0(Etw):
    pattern = Struct(
        "ProcessorId" / Int32ul,
        "ThrottleMSR" / Int64ul,
        "ElapsedTime" / Int32ul,
        "LogInterval" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=92, version=0)
class Microsoft_Windows_Kernel_Power_92_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Type" / Int32ul,
        "ProcessID" / Int32ul,
        "SessionID" / Int32ul,
        "Legacy" / Int8ul,
        "SystemAllowed" / Int8ul,
        "DisplayAllowed" / Int8ul,
        "AwayModeAllowed" / Int8ul,
        "SystemCount" / Int32ul,
        "DisplayCount" / Int32ul,
        "AwayModeCount" / Int32ul,
        "CallerLength" / Int16ul,
        "ContextLength" / Int16ul,
        "Caller" / Bytes(lambda this: this.CallerLength),
        "Context" / Bytes(lambda this: this.ContextLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=92, version=1)
class Microsoft_Windows_Kernel_Power_92_1(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Type" / Int32ul,
        "ProcessID" / Int32ul,
        "SessionID" / Int32ul,
        "Legacy" / Int8ul,
        "SystemAllowed" / Int8ul,
        "DisplayAllowed" / Int8ul,
        "AwayModeAllowed" / Int8ul,
        "SystemCount" / Int32ul,
        "DisplayCount" / Int32ul,
        "AwayModeCount" / Int32ul,
        "CallerLength" / Int16ul,
        "ContextLength" / Int16ul,
        "Caller" / Bytes(lambda this: this.CallerLength),
        "Context" / Bytes(lambda this: this.ContextLength),
        "ExecutionRequiredAllowed" / Int8ul,
        "PerformanceBoostAllowed" / Int8ul,
        "FullScreenVideoAllowed" / Int8ul,
        "ExecutionRequiredCount" / Int32ul,
        "PerformanceBoostCount" / Int32ul,
        "FullScreenVideoCount" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=93, version=0)
class Microsoft_Windows_Kernel_Power_93_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "SystemCount" / Int32ul,
        "DisplayCount" / Int32ul,
        "AwayModeCount" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=93, version=1)
class Microsoft_Windows_Kernel_Power_93_1(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "SystemCount" / Int32ul,
        "DisplayCount" / Int32ul,
        "AwayModeCount" / Int32ul,
        "ExecutionRequiredCount" / Int32ul,
        "PerformanceBoostCount" / Int32ul,
        "FullScreenVideoCount" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=94, version=0)
class Microsoft_Windows_Kernel_Power_94_0(Etw):
    pattern = Struct(
        "Token" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=95, version=0)
class Microsoft_Windows_Kernel_Power_95_0(Etw):
    pattern = Struct(
        "NewResolution" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=96, version=0)
class Microsoft_Windows_Kernel_Power_96_0(Etw):
    pattern = Struct(
        "CurrentPeriod" / Int32ul,
        "MinimumPeriod" / Int32ul,
        "MaximumPeriod" / Int32ul,
        "KernelRequestCount" / Int32ul,
        "KernelRequestedPeriod" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=96, version=1)
class Microsoft_Windows_Kernel_Power_96_1(Etw):
    pattern = Struct(
        "CurrentPeriod" / Int32ul,
        "MinimumPeriod" / Int32ul,
        "MaximumPeriod" / Int32ul,
        "KernelRequestCount" / Int32ul,
        "KernelRequestedPeriod" / Int32ul,
        "InternalSetPeriod" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=97, version=0)
class Microsoft_Windows_Kernel_Power_97_0(Etw):
    pattern = Struct(
        "RequestedPeriod" / Int32ul,
        "Pid" / Int32ul,
        "AppNameLength" / Int16ul,
        "AppName" / Bytes(lambda this: this.AppNameLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=98, version=0)
class Microsoft_Windows_Kernel_Power_98_0(Etw):
    pattern = Struct(
        "RequestedResolution" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=98, version=1)
class Microsoft_Windows_Kernel_Power_98_1(Etw):
    pattern = Struct(
        "RequestedResolution" / Int32ul,
        "Tag" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=99, version=0)
class Microsoft_Windows_Kernel_Power_99_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Type" / Int32ul,
        "ProcessID" / Int32ul,
        "SessionID" / Int32ul,
        "Legacy" / Int8ul,
        "SystemAllowed" / Int8ul,
        "DisplayAllowed" / Int8ul,
        "AwayModeAllowed" / Int8ul,
        "SystemCount" / Int32ul,
        "DisplayCount" / Int32ul,
        "AwayModeCount" / Int32ul,
        "CallerLength" / Int16ul,
        "ContextLength" / Int16ul,
        "Caller" / Bytes(lambda this: this.CallerLength),
        "Context" / Bytes(lambda this: this.ContextLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=99, version=1)
class Microsoft_Windows_Kernel_Power_99_1(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Type" / Int32ul,
        "ProcessID" / Int32ul,
        "SessionID" / Int32ul,
        "Legacy" / Int8ul,
        "SystemAllowed" / Int8ul,
        "DisplayAllowed" / Int8ul,
        "AwayModeAllowed" / Int8ul,
        "SystemCount" / Int32ul,
        "DisplayCount" / Int32ul,
        "AwayModeCount" / Int32ul,
        "CallerLength" / Int16ul,
        "ContextLength" / Int16ul,
        "Caller" / Bytes(lambda this: this.CallerLength),
        "Context" / Bytes(lambda this: this.ContextLength),
        "ExecutionRequiredAllowed" / Int8ul,
        "PerformanceBoostAllowed" / Int8ul,
        "FullScreenVideoAllowed" / Int8ul,
        "ExecutionRequiredCount" / Int32ul,
        "PerformanceBoostCount" / Int32ul,
        "FullScreenVideoCount" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=104, version=0)
class Microsoft_Windows_Kernel_Power_104_0(Etw):
    pattern = Struct(
        "AffectedState" / Int8ul,
        "PowerReasonCode" / Int32ul,
        "PowerReasonLength" / Int32ul,
        "PowerReasonInfo" / Bytes(lambda this: this.PowerReasonLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=105, version=0)
class Microsoft_Windows_Kernel_Power_105_0(Etw):
    pattern = Struct(
        "AcOnline" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=105, version=1)
class Microsoft_Windows_Kernel_Power_105_1(Etw):
    pattern = Struct(
        "AcOnline" / Int8ul,
        "RemainingCapacity" / Int32ul,
        "FullChargeCapacity" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=106, version=0)
class Microsoft_Windows_Kernel_Power_106_0(Etw):
    pattern = Struct(
        "AcOnline" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=107, version=0)
class Microsoft_Windows_Kernel_Power_107_0(Etw):
    pattern = Struct(
        "TargetState" / Int32ul,
        "EffectiveState" / Int32ul,
        "WakeFromState" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=107, version=1)
class Microsoft_Windows_Kernel_Power_107_1(Etw):
    pattern = Struct(
        "TargetState" / Int32ul,
        "EffectiveState" / Int32ul,
        "WakeFromState" / Int32ul,
        "ProgrammedWakeTimeAc" / Int64ul,
        "ProgrammedWakeTimeDc" / Int64ul,
        "WakeRequesterTypeAc" / Int32ul,
        "WakeRequesterTypeDc" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=108, version=0)
class Microsoft_Windows_Kernel_Power_108_0(Etw):
    pattern = Struct(
        "CopyBytes" / Int64ul,
        "ElapsedTime" / Int32ul,
        "IoTime" / Int32ul,
        "InitTime" / Int32ul,
        "CopyTime" / Int32ul,
        "PagesWritten" / Int32ul,
        "PagesProcessed" / Int32ul,
        "DumpCount" / Int32ul,
        "FileRuns" / Int32ul,
        "ReadTime" / Int32ul,
        "ResumeAppTime" / Int32ul,
        "CompressTime" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=109, version=0)
class Microsoft_Windows_Kernel_Power_109_0(Etw):
    pattern = Struct(
        "ShutdownActionType" / Int32ul,
        "ShutdownEventCode" / Int32ul,
        "ShutdownReason" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=110, version=0)
class Microsoft_Windows_Kernel_Power_110_0(Etw):
    pattern = Struct(
        "RequestedPeriod" / Int32ul,
        "Pid" / Int32ul,
        "AppNameLength" / Int16ul,
        "AppName" / Bytes(lambda this: this.AppNameLength),
        "StackSize" / Int32ul,
        "Stack" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=111, version=0)
class Microsoft_Windows_Kernel_Power_111_0(Etw):
    pattern = Struct(
        "SettingGuid" / Guid,
        "DataSize" / Int32ul,
        "Data" / Bytes(lambda this: this.DataSize)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=111, version=1)
class Microsoft_Windows_Kernel_Power_111_1(Etw):
    pattern = Struct(
        "SettingGuid" / Guid,
        "DataSize" / Int32ul,
        "Data" / Bytes(lambda this: this.DataSize),
        "Override" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=112, version=0)
class Microsoft_Windows_Kernel_Power_112_0(Etw):
    pattern = Struct(
        "SettingGuid" / Guid,
        "DataSize" / Int32ul,
        "Data" / Bytes(lambda this: this.DataSize)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=112, version=1)
class Microsoft_Windows_Kernel_Power_112_1(Etw):
    pattern = Struct(
        "SettingGuid" / Guid,
        "DataSize" / Int32ul,
        "Data" / Bytes(lambda this: this.DataSize),
        "Override" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=113, version=0)
class Microsoft_Windows_Kernel_Power_113_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "EventTime" / Int64ul,
        "PassiveCoolingState" / Int16ul,
        "_PSV" / Int32ul,
        "_TMP" / Int32ul,
        "_TC1" / Int32ul,
        "_TC2" / Int32ul,
        "_TSP" / Int32ul,
        "DeltaP" / Int32sl
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=113, version=1)
class Microsoft_Windows_Kernel_Power_113_1(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "EventTime" / Int64ul,
        "PassiveCoolingState" / Int16ul,
        "_PSV" / Int32ul,
        "_TMP" / Int32ul,
        "_TC1" / Int32ul,
        "_TC2" / Int32ul,
        "_TSP" / Int32ul,
        "DeltaP" / Int32sl,
        "MinimumThrottle" / Int32sl
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=114, version=0)
class Microsoft_Windows_Kernel_Power_114_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "EventTime" / Int64ul,
        "PassiveCoolingState" / Int16ul,
        "_PSV" / Int32ul,
        "_TMP" / Int32ul,
        "_TC1" / Int32ul,
        "_TC2" / Int32ul,
        "_TSP" / Int32ul,
        "DeltaP" / Int32sl
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=114, version=1)
class Microsoft_Windows_Kernel_Power_114_1(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "EventTime" / Int64ul,
        "PassiveCoolingState" / Int16ul,
        "_PSV" / Int32ul,
        "_TMP" / Int32ul,
        "_TC1" / Int32ul,
        "_TC2" / Int32ul,
        "_TSP" / Int32ul,
        "DeltaP" / Int32sl,
        "MinimumThrottle" / Int32sl
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=115, version=0)
class Microsoft_Windows_Kernel_Power_115_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "EventTime" / Int64ul,
        "ActiveCoolingState" / Int16ul,
        "_AC0" / Int32ul,
        "_AC1" / Int32ul,
        "_AC2" / Int32ul,
        "_AC3" / Int32ul,
        "_AC4" / Int32ul,
        "_AC5" / Int32ul,
        "_AC6" / Int32ul,
        "_AC7" / Int32ul,
        "_AC8" / Int32ul,
        "_AC9" / Int32ul,
        "_TMP" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=116, version=0)
class Microsoft_Windows_Kernel_Power_116_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "EventTime" / Int64ul,
        "ActiveCoolingState" / Int16ul,
        "_AC0" / Int32ul,
        "_AC1" / Int32ul,
        "_AC2" / Int32ul,
        "_AC3" / Int32ul,
        "_AC4" / Int32ul,
        "_AC5" / Int32ul,
        "_AC6" / Int32ul,
        "_AC7" / Int32ul,
        "_AC8" / Int32ul,
        "_AC9" / Int32ul,
        "_TMP" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=117, version=0)
class Microsoft_Windows_Kernel_Power_117_0(Etw):
    pattern = Struct(
        "TotalResumeTime" / Int32ul,
        "POSTTime" / Int32ul,
        "ResumeBootMgrTime" / Int32ul,
        "ResumeAppTime" / Int32ul,
        "ResumeAppStartTime" / Int32ul,
        "ResumeLibraryInitTime" / Int32ul,
        "ResumeInitTime" / Int32ul,
        "ResumeHiberFileTime" / Int32ul,
        "ResumeRestoreImageStartTimestamp" / Int32ul,
        "ResumeIoTime" / Int32ul,
        "ResumeDecompressTime" / Int32ul,
        "ResumeMapTime" / Int32ul,
        "ResumeUnmapTime" / Int32ul,
        "ResumeUserInOutTime" / Int32ul,
        "ResumeAllocateTime" / Int32ul,
        "ResumeKernelSwitchTimestamp" / Int32ul,
        "KernelReturnFromHandlerTimestamp" / Int32ul,
        "SleeperThreadEndTimestamp" / Int32ul,
        "TimeStampCounterAtSwitchTime" / Int32ul,
        "KernelReturnSystemPowerStateTimestamp" / Int32ul,
        "HiberHiberFileTime" / Int32ul,
        "InitTime" / Int32ul,
        "HiberSharedBufferTime" / Int32ul,
        "TotalHibernateTime" / Int32ul,
        "KernelResumeHiberFileTime" / Int32ul,
        "KernelResumeInitTime" / Int32ul,
        "KernelResumeSharedBufferTime" / Int32ul,
        "DeviceResumeTime" / Int32ul,
        "KernelAnimationTime" / Int32ul,
        "KernelPagesProcessed" / Int32ul,
        "KernelPagesWritten" / Int64ul,
        "BootPagesProcessed" / Int32ul,
        "BootPagesWritten" / Int64ul,
        "HiberWriteRate" / Int32ul,
        "HiberCompressRate" / Int32ul,
        "ResumeReadRate" / Int32ul,
        "ResumeDecompressRate" / Int32ul,
        "FileRuns" / Int32ul,
        "NoMultiStageResumeReason" / Int32ul,
        "MaxHuffRatio" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=117, version=1)
class Microsoft_Windows_Kernel_Power_117_1(Etw):
    pattern = Struct(
        "TotalResumeTime" / Int32ul,
        "POSTTime" / Int32ul,
        "ResumeBootMgrTime" / Int32ul,
        "ResumeAppTime" / Int32ul,
        "ResumeAppStartTime" / Int32ul,
        "ResumeLibraryInitTime" / Int32ul,
        "ResumeInitTime" / Int32ul,
        "ResumeHiberFileTime" / Int32ul,
        "ResumeRestoreImageStartTimestamp" / Int32ul,
        "ResumeIoTime" / Int32ul,
        "ResumeDecompressTime" / Int32ul,
        "ResumeMapTime" / Int32ul,
        "ResumeUnmapTime" / Int32ul,
        "ResumeUserInOutTime" / Int32ul,
        "ResumeAllocateTime" / Int32ul,
        "ResumeKernelSwitchTimestamp" / Int32ul,
        "KernelReturnFromHandlerTimestamp" / Int32ul,
        "SleeperThreadEndTimestamp" / Int32ul,
        "TimeStampCounterAtSwitchTime" / Int32ul,
        "KernelReturnSystemPowerStateTimestamp" / Int32ul,
        "HiberHiberFileTime" / Int32ul,
        "InitTime" / Int32ul,
        "HiberSharedBufferTime" / Int32ul,
        "TotalHibernateTime" / Int32ul,
        "KernelResumeHiberFileTime" / Int32ul,
        "KernelResumeInitTime" / Int32ul,
        "KernelResumeSharedBufferTime" / Int32ul,
        "DeviceResumeTime" / Int32ul,
        "KernelAnimationTime" / Int32ul,
        "KernelPagesProcessed" / Int32ul,
        "KernelPagesWritten" / Int64ul,
        "BootPagesProcessed" / Int32ul,
        "BootPagesWritten" / Int64ul,
        "HiberWriteRate" / Int32ul,
        "HiberCompressRate" / Int32ul,
        "ResumeReadRate" / Int32ul,
        "ResumeDecompressRate" / Int32ul,
        "FileRuns" / Int32ul,
        "NoMultiStageResumeReason" / Int32ul,
        "MaxHuffRatio" / Int32ul,
        "SecurePagesProcessed" / Int32ul,
        "HiberChecksumTime" / Int32ul,
        "HiberChecksumIoTime" / Int32ul,
        "ResumeChecksumTime" / Int32ul,
        "ResumeChecksumIoTime" / Int32ul,
        "KernelChecksumTime" / Int32ul,
        "KernelChecksumIoTime" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=118, version=0)
class Microsoft_Windows_Kernel_Power_118_0(Etw):
    pattern = Struct(
        "RequestedResolution" / Int32ul,
        "Flags" / Int32ul,
        "Ticks" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=119, version=0)
class Microsoft_Windows_Kernel_Power_119_0(Etw):
    pattern = Struct(
        "RequestedResolution" / Int32ul,
        "Flags" / Int32ul,
        "Ticks" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=120, version=0)
class Microsoft_Windows_Kernel_Power_120_0(Etw):
    pattern = Struct(
        "HiberfileSizeKB" / Int32ul,
        "TotalHibernateTime" / Int32ul,
        "HiberHiberFileTime" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=121, version=0)
class Microsoft_Windows_Kernel_Power_121_0(Etw):
    pattern = Struct(
        "DriverWakeTime" / Int32ul,
        "TotalResumeTime" / Int32ul,
        "BiosInitTime" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=121, version=1)
class Microsoft_Windows_Kernel_Power_121_1(Etw):
    pattern = Struct(
        "DriverWakeTime" / Int32ul,
        "TotalResumeTime" / Int32ul,
        "BiosInitTime" / Int32ul,
        "ResumeAppsTime" / Int32ul,
        "ResumeServicesTime" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=122, version=0)
class Microsoft_Windows_Kernel_Power_122_0(Etw):
    pattern = Struct(
        "TotalResumeTime" / Int32ul,
        "PhasePagesWrittenMB" / Int32ul,
        "ResumeAppAndKernelResumeHiberFileTime" / Int32ul,
        "POSTAndDeviceResumeTime" / Int32ul,
        "RatesAndResumeAppsServicesTime" / Int32ul,
        "PhasePagesProcessedMB" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=123, version=1)
class Microsoft_Windows_Kernel_Power_123_1(Etw):
    pattern = Struct(
        "HiberfileSize" / Int32ul,
        "TotalHybridShutdownTime" / Int32ul,
        "HiberfileCreateTime" / Int32ul,
        "SystemShutdownTime" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=124, version=0)
class Microsoft_Windows_Kernel_Power_124_0(Etw):
    pattern = Struct(
        "TotalResumeTime" / Int32ul,
        "PhasePagesWrittenMB" / Int32ul,
        "ResumeAppAndKernelResumeHiberFileTime" / Int32ul,
        "POSTAndDeviceResumeTime" / Int32ul,
        "RatesAndResumeAppsServicesTime" / Int32ul,
        "PhasePagesProcessedMB" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=125, version=0)
class Microsoft_Windows_Kernel_Power_125_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "_PSV" / Int32ul,
        "_TC1" / Int32ul,
        "_TC2" / Int32ul,
        "_TSP" / Int32ul,
        "_AC0" / Int32ul,
        "_AC1" / Int32ul,
        "_AC2" / Int32ul,
        "_AC3" / Int32ul,
        "_AC4" / Int32ul,
        "_AC5" / Int32ul,
        "_AC6" / Int32ul,
        "_AC7" / Int32ul,
        "_AC8" / Int32ul,
        "_AC9" / Int32ul,
        "_CRT" / Int32ul,
        "_HOT" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=125, version=1)
class Microsoft_Windows_Kernel_Power_125_1(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "_PSV" / Int32ul,
        "_TC1" / Int32ul,
        "_TC2" / Int32ul,
        "_TSP" / Int32ul,
        "_AC0" / Int32ul,
        "_AC1" / Int32ul,
        "_AC2" / Int32ul,
        "_AC3" / Int32ul,
        "_AC4" / Int32ul,
        "_AC5" / Int32ul,
        "_AC6" / Int32ul,
        "_AC7" / Int32ul,
        "_AC8" / Int32ul,
        "_AC9" / Int32ul,
        "_CRT" / Int32ul,
        "_HOT" / Int32ul,
        "MinimumThrottle" / Int32sl
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=125, version=2)
class Microsoft_Windows_Kernel_Power_125_2(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "_PSV" / Int32ul,
        "_TC1" / Int32ul,
        "_TC2" / Int32ul,
        "_TSP" / Int32ul,
        "_AC0" / Int32ul,
        "_AC1" / Int32ul,
        "_AC2" / Int32ul,
        "_AC3" / Int32ul,
        "_AC4" / Int32ul,
        "_AC5" / Int32ul,
        "_AC6" / Int32ul,
        "_AC7" / Int32ul,
        "_AC8" / Int32ul,
        "_AC9" / Int32ul,
        "_CRT" / Int32ul,
        "_HOT" / Int32ul,
        "MinimumThrottle" / Int32sl,
        "_CR3" / Int32ul,
        "OverThrottleThreshold" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=125, version=3)
class Microsoft_Windows_Kernel_Power_125_3(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "_PSV" / Int32ul,
        "_TC1" / Int32ul,
        "_TC2" / Int32ul,
        "_TSP" / Int32ul,
        "_AC0" / Int32ul,
        "_AC1" / Int32ul,
        "_AC2" / Int32ul,
        "_AC3" / Int32ul,
        "_AC4" / Int32ul,
        "_AC5" / Int32ul,
        "_AC6" / Int32ul,
        "_AC7" / Int32ul,
        "_AC8" / Int32ul,
        "_AC9" / Int32ul,
        "_CRT" / Int32ul,
        "_HOT" / Int32ul,
        "MinimumThrottle" / Int32sl,
        "_CR3" / Int32ul,
        "OverThrottleThreshold" / Int32ul,
        "DescriptionLength" / Int16ul,
        "Description" / Bytes(lambda this: this.DescriptionLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=125, version=4)
class Microsoft_Windows_Kernel_Power_125_4(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "_PSV" / Int32ul,
        "_TC1" / Int32ul,
        "_TC2" / Int32ul,
        "_TSP" / Int32ul,
        "_AC0" / Int32ul,
        "_AC1" / Int32ul,
        "_AC2" / Int32ul,
        "_AC3" / Int32ul,
        "_AC4" / Int32ul,
        "_AC5" / Int32ul,
        "_AC6" / Int32ul,
        "_AC7" / Int32ul,
        "_AC8" / Int32ul,
        "_AC9" / Int32ul,
        "_CRT" / Int32ul,
        "_HOT" / Int32ul,
        "MinimumThrottle" / Int32sl,
        "_CR3" / Int32ul,
        "OverThrottleThreshold" / Int32ul,
        "DescriptionLength" / Int16ul,
        "Description" / Bytes(lambda this: this.DescriptionLength),
        "_TZP" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=126, version=0)
class Microsoft_Windows_Kernel_Power_126_0(Etw):
    pattern = Struct(
        "Level" / Int32ul,
        "MinorFunction" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=127, version=0)
class Microsoft_Windows_Kernel_Power_127_0(Etw):
    pattern = Struct(
        "Level" / Int32ul,
        "MinorFunction" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=128, version=0)
class Microsoft_Windows_Kernel_Power_128_0(Etw):
    pattern = Struct(
        "Level" / Int32ul,
        "MinorFunction" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=129, version=0)
class Microsoft_Windows_Kernel_Power_129_0(Etw):
    pattern = Struct(
        "Level" / Int32ul,
        "MinorFunction" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=130, version=0)
class Microsoft_Windows_Kernel_Power_130_0(Etw):
    pattern = Struct(
        "SuspendStart" / Int64ul,
        "SuspendEnd" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=131, version=0)
class Microsoft_Windows_Kernel_Power_131_0(Etw):
    pattern = Struct(
        "ResumeCount" / Int32ul,
        "FullResume" / Int32ul,
        "AverageResume" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=132, version=0)
class Microsoft_Windows_Kernel_Power_132_0(Etw):
    pattern = Struct(
        "PlatformRole" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=135, version=0)
class Microsoft_Windows_Kernel_Power_135_0(Etw):
    pattern = Struct(
        "DisplayState" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=136, version=0)
class Microsoft_Windows_Kernel_Power_136_0(Etw):
    pattern = Struct(
        "DeviceNode" / Int64ul,
        "PowerState" / Int8ul,
        "InstancePathLength" / Int16ul,
        "InstancePath" / Bytes(lambda this: this.InstancePathLength),
        "FriendlyNameLength" / Int16ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=137, version=0)
class Microsoft_Windows_Kernel_Power_137_0(Etw):
    pattern = Struct(
        "SleepState" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=138, version=0)
class Microsoft_Windows_Kernel_Power_138_0(Etw):
    pattern = Struct(
        "Throttle" / Int32ul,
        "Temperature" / Int32ul,
        "ZoneLength" / Int16ul,
        "Zone" / Bytes(lambda this: this.ZoneLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=139, version=0)
class Microsoft_Windows_Kernel_Power_139_0(Etw):
    pattern = Struct(
        "ThrottleDuration" / Int32ul,
        "ZoneLength" / Int16ul,
        "Zone" / Bytes(lambda this: this.ZoneLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=140, version=0)
class Microsoft_Windows_Kernel_Power_140_0(Etw):
    pattern = Struct(
        "EnergyDrain" / Int32ul,
        "Duration" / Int32ul,
        "DripsTransitions" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=141, version=0)
class Microsoft_Windows_Kernel_Power_141_0(Etw):
    pattern = Struct(
        "FanDuration" / Int32ul,
        "ActivationDelay" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=142, version=0)
class Microsoft_Windows_Kernel_Power_142_0(Etw):
    pattern = Struct(
        "ResetReasonMask" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=143, version=0)
class Microsoft_Windows_Kernel_Power_143_0(Etw):
    pattern = Struct(
        "ResiliencyPhaseNonActivatedNoDripsMs" / Int32ul,
        "NonActivatedCpuTimeMs" / Int32ul,
        "DurationThisPeriodMs" / Int32ul,
        "ActionsTakenAndOnAc" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=144, version=0)
class Microsoft_Windows_Kernel_Power_144_0(Etw):
    pattern = Struct(
        "InitiatorLength" / Int16ul,
        "Initiator" / Bytes(lambda this: this.InitiatorLength),
        "Type" / Int32ul,
        "Temperature" / Int32ul,
        "TripPointTemperature" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=145, version=0)
class Microsoft_Windows_Kernel_Power_145_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "ActiveCoolingState" / Int16ul,
        "ActivePoint" / Int32sl,
        "PassiveCoolingState" / Int16ul,
        "ThrottleLimit" / Int32sl
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=145, version=1)
class Microsoft_Windows_Kernel_Power_145_1(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "ActiveCoolingState" / Int16ul,
        "ActivePoint" / Int32sl,
        "PassiveCoolingState" / Int16ul,
        "ThrottleLimit" / Int32sl,
        "ThermalStandby" / Int8ul,
        "OverThrottled" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=145, version=2)
class Microsoft_Windows_Kernel_Power_145_2(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "ActiveCoolingState" / Int16ul,
        "ActivePoint" / Int32sl,
        "PassiveCoolingState" / Int16ul,
        "ThrottleLimit" / Int32sl,
        "ThermalStandby" / Int8ul,
        "OverThrottled" / Int8ul,
        "DescriptionLength" / Int16ul,
        "Description" / Bytes(lambda this: this.DescriptionLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=146, version=0)
class Microsoft_Windows_Kernel_Power_146_0(Etw):
    pattern = Struct(
        "Callback" / Int64ul,
        "SettingGuid" / Guid,
        "DataSize" / Int32ul,
        "Data" / Bytes(lambda this: this.DataSize)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=147, version=0)
class Microsoft_Windows_Kernel_Power_147_0(Etw):
    pattern = Struct(
        "Callback" / Int64ul,
        "SettingGuid" / Guid
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=148, version=0)
class Microsoft_Windows_Kernel_Power_148_0(Etw):
    pattern = Struct(
        "State" / Int32sl,
        "Reason" / Int32sl
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=149, version=0)
class Microsoft_Windows_Kernel_Power_149_0(Etw):
    pattern = Struct(
        "Session" / Int32ul,
        "Console" / Int8ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=150, version=0)
class Microsoft_Windows_Kernel_Power_150_0(Etw):
    pattern = Struct(
        "Session" / Int32ul,
        "Console" / Int8ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=151, version=0)
class Microsoft_Windows_Kernel_Power_151_0(Etw):
    pattern = Struct(
        "PassiveSupported" / Int8ul,
        "ActiveSupported" / Int8ul,
        "Throttle" / Int8ul,
        "ActiveEngaged" / Int8ul,
        "Token" / Int64ul,
        "DeviceIdLength" / Int16ul,
        "DeviceId" / Bytes(lambda this: this.DeviceIdLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=152, version=0)
class Microsoft_Windows_Kernel_Power_152_0(Etw):
    pattern = Struct(
        "PassiveSupported" / Int8ul,
        "ActiveSupported" / Int8ul,
        "Throttle" / Int8ul,
        "ActiveEngaged" / Int8ul,
        "Token" / Int64ul,
        "DeviceIdLength" / Int16ul,
        "DeviceId" / Bytes(lambda this: this.DeviceIdLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=153, version=0)
class Microsoft_Windows_Kernel_Power_153_0(Etw):
    pattern = Struct(
        "PassiveSupported" / Int8ul,
        "ActiveSupported" / Int8ul,
        "Throttle" / Int8ul,
        "ActiveEngaged" / Int8ul,
        "Token" / Int64ul,
        "DeviceIdLength" / Int16ul,
        "DeviceId" / Bytes(lambda this: this.DeviceIdLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=154, version=0)
class Microsoft_Windows_Kernel_Power_154_0(Etw):
    pattern = Struct(
        "Throttle" / Int8ul,
        "Token" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=155, version=0)
class Microsoft_Windows_Kernel_Power_155_0(Etw):
    pattern = Struct(
        "ActiveEngaged" / Int8ul,
        "Token" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=156, version=0)
class Microsoft_Windows_Kernel_Power_156_0(Etw):
    pattern = Struct(
        "Throttle" / Int8ul,
        "ActiveEngaged" / Int8ul,
        "Token" / Int64ul,
        "DeviceIdLength" / Int16ul,
        "CallerLength" / Int16ul,
        "ContextLength" / Int16ul,
        "PolicyLength" / Int16ul,
        "DeviceId" / Bytes(lambda this: this.DeviceIdLength),
        "Caller" / Bytes(lambda this: this.CallerLength),
        "Context" / Bytes(lambda this: this.ContextLength),
        "Policy" / Bytes(lambda this: this.PolicyLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=157, version=0)
class Microsoft_Windows_Kernel_Power_157_0(Etw):
    pattern = Struct(
        "Throttle" / Int8ul,
        "ActiveEngaged" / Int8ul,
        "Token" / Int64ul,
        "DeviceIdLength" / Int16ul,
        "CallerLength" / Int16ul,
        "ContextLength" / Int16ul,
        "PolicyLength" / Int16ul,
        "DeviceId" / Bytes(lambda this: this.DeviceIdLength),
        "Caller" / Bytes(lambda this: this.CallerLength),
        "Context" / Bytes(lambda this: this.ContextLength),
        "Policy" / Bytes(lambda this: this.PolicyLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=158, version=0)
class Microsoft_Windows_Kernel_Power_158_0(Etw):
    pattern = Struct(
        "Throttle" / Int8ul,
        "ActiveEngaged" / Int8ul,
        "Token" / Int64ul,
        "DeviceIdLength" / Int16ul,
        "CallerLength" / Int16ul,
        "ContextLength" / Int16ul,
        "PolicyLength" / Int16ul,
        "DeviceId" / Bytes(lambda this: this.DeviceIdLength),
        "Caller" / Bytes(lambda this: this.CallerLength),
        "Context" / Bytes(lambda this: this.ContextLength),
        "Policy" / Bytes(lambda this: this.PolicyLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=159, version=0)
class Microsoft_Windows_Kernel_Power_159_0(Etw):
    pattern = Struct(
        "Throttle" / Int8ul,
        "Token" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=160, version=0)
class Microsoft_Windows_Kernel_Power_160_0(Etw):
    pattern = Struct(
        "ActiveEngaged" / Int8ul,
        "Token" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=161, version=0)
class Microsoft_Windows_Kernel_Power_161_0(Etw):
    pattern = Struct(
        "ResiliencyPhaseNonActivatedNoDripsMs" / Int32ul,
        "NonActivatedCpuTimeMs" / Int32ul,
        "DurationThisPeriodMs" / Int32ul,
        "OnAc" / Int8ul,
        "EnergyDrainMw" / Int32ul,
        "DeviceConstraint" / Int8ul,
        "ActionsTaken" / Int8ul,
        "DeviceServiceNameLength" / Int16ul,
        "DeviceServiceName" / Bytes(lambda this: this.DeviceServiceNameLength),
        "ChildServiceNameLength" / Int16ul,
        "ChildServiceName" / Bytes(lambda this: this.ChildServiceNameLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=161, version=1)
class Microsoft_Windows_Kernel_Power_161_1(Etw):
    pattern = Struct(
        "ResiliencyPhaseNonActivatedNoDripsMs" / Int32ul,
        "NonActivatedCpuTimeMs" / Int32ul,
        "DurationThisPeriodMs" / Int32ul,
        "OnAc" / Int8ul,
        "EnergyDrainMw" / Int32ul,
        "DeviceConstraint" / Int8ul,
        "ActionsTaken" / Int8ul,
        "DeviceServiceNameLength" / Int16ul,
        "DeviceServiceName" / Bytes(lambda this: this.DeviceServiceNameLength),
        "ChildServiceNameLength" / Int16ul,
        "ChildServiceName" / Bytes(lambda this: this.ChildServiceNameLength),
        "PepPreVeto" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=161, version=2)
class Microsoft_Windows_Kernel_Power_161_2(Etw):
    pattern = Struct(
        "ResiliencyPhaseNonActivatedNoDripsMs" / Int32ul,
        "NonActivatedCpuTimeMs" / Int32ul,
        "DurationThisPeriodMs" / Int32ul,
        "OnAc" / Int8ul,
        "EnergyDrainMw" / Int32ul,
        "DeviceConstraint" / Int8ul,
        "ActionsTaken" / Int8ul,
        "DeviceServiceNameLength" / Int16ul,
        "DeviceServiceName" / Bytes(lambda this: this.DeviceServiceNameLength),
        "ChildServiceNameLength" / Int16ul,
        "ChildServiceName" / Bytes(lambda this: this.ChildServiceNameLength),
        "PepPreVeto" / Int32ul,
        "InvocationCount" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=161, version=3)
class Microsoft_Windows_Kernel_Power_161_3(Etw):
    pattern = Struct(
        "ResiliencyPhaseNonActivatedNoDripsMs" / Int32ul,
        "NonActivatedCpuTimeMs" / Int32ul,
        "DurationThisPeriodMs" / Int32ul,
        "OnAc" / Int8ul,
        "EnergyDrainMw" / Int32ul,
        "DeviceConstraint" / Int8ul,
        "ActionsTaken" / Int32ul,
        "DeviceServiceNameLength" / Int16ul,
        "DeviceServiceName" / Bytes(lambda this: this.DeviceServiceNameLength),
        "ChildServiceNameLength" / Int16ul,
        "ChildServiceName" / Bytes(lambda this: this.ChildServiceNameLength),
        "PepPreVeto" / Int32ul,
        "InvocationCount" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=162, version=0)
class Microsoft_Windows_Kernel_Power_162_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "Engaged" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=163, version=0)
class Microsoft_Windows_Kernel_Power_163_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "Engaged" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=165, version=0)
class Microsoft_Windows_Kernel_Power_165_0(Etw):
    pattern = Struct(
        "IdleInformationUpdated" / Int8ul,
        "TimeoutSource" / Int32ul,
        "Action" / Int32ul,
        "MinState" / Int32ul,
        "Timeout" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=165, version=1)
class Microsoft_Windows_Kernel_Power_165_1(Etw):
    pattern = Struct(
        "IdleInformationUpdated" / Int8ul,
        "TimeoutSource" / Int32ul,
        "Action" / Int32ul,
        "MinState" / Int32ul,
        "Timeout" / Int32ul,
        "Flags" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=166, version=0)
class Microsoft_Windows_Kernel_Power_166_0(Etw):
    pattern = Struct(
        "AccumulatedIdleTime" / Int32ul,
        "SystemIdle" / Int8ul,
        "Flags" / Int32ul,
        "Action" / Int32ul,
        "MinState" / Int32ul,
        "DozeS4Timeout" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=166, version=1)
class Microsoft_Windows_Kernel_Power_166_1(Etw):
    pattern = Struct(
        "AccumulatedIdleTime" / Int32ul,
        "SystemIdle" / Int8ul,
        "Flags" / Int32ul,
        "Action" / Int32ul,
        "MinState" / Int32ul,
        "DozeS4Timeout" / Int32ul,
        "PredictedUserReturnTime" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=167, version=0)
class Microsoft_Windows_Kernel_Power_167_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "S0LowPowerDozeTimerCancelled" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=168, version=0)
class Microsoft_Windows_Kernel_Power_168_0(Etw):
    pattern = Struct(
        "CancelledDueToUserInput" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=169, version=0)
class Microsoft_Windows_Kernel_Power_169_0(Etw):
    pattern = Struct(
        "Source" / Int32ul,
        "Time" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=170, version=0)
class Microsoft_Windows_Kernel_Power_170_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=171, version=0)
class Microsoft_Windows_Kernel_Power_171_0(Etw):
    pattern = Struct(
        "ResiliencyPhaseNonActivatedNoDeepSleepMs" / Int32ul,
        "NonActivatedCpuTimeMs" / Int32ul,
        "DurationThisPeriodMs" / Int32ul,
        "OnAc" / Int8ul,
        "ActionsTaken" / Int8ul,
        "PowerSettingPending" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=171, version=1)
class Microsoft_Windows_Kernel_Power_171_1(Etw):
    pattern = Struct(
        "ResiliencyPhaseNonActivatedNoDeepSleepMs" / Int32ul,
        "NonActivatedCpuTimeMs" / Int32ul,
        "DurationThisPeriodMs" / Int32ul,
        "OnAc" / Int8ul,
        "ActionsTaken" / Int32ul,
        "PowerSettingPending" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=172, version=0)
class Microsoft_Windows_Kernel_Power_172_0(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=175, version=0)
class Microsoft_Windows_Kernel_Power_175_0(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=176, version=0)
class Microsoft_Windows_Kernel_Power_176_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=177, version=0)
class Microsoft_Windows_Kernel_Power_177_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=178, version=0)
class Microsoft_Windows_Kernel_Power_178_0(Etw):
    pattern = Struct(
        "PreviousPolicy" / Int32ul,
        "NewPolicy" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=179, version=0)
class Microsoft_Windows_Kernel_Power_179_0(Etw):
    pattern = Struct(
        "PrevState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=180, version=0)
class Microsoft_Windows_Kernel_Power_180_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=181, version=0)
class Microsoft_Windows_Kernel_Power_181_0(Etw):
    pattern = Struct(
        "Constraint" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=182, version=0)
class Microsoft_Windows_Kernel_Power_182_0(Etw):
    pattern = Struct(
        "Constraint" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=183, version=0)
class Microsoft_Windows_Kernel_Power_183_0(Etw):
    pattern = Struct(
        "ConstraintCount" / Int16ul,
        "Constraints" / CString
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=184, version=0)
class Microsoft_Windows_Kernel_Power_184_0(Etw):
    pattern = Struct(
        "ExpiryCount" / Int32ul,
        "RelativeId" / Int16ul,
        "ComponentName" / WString
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=185, version=0)
class Microsoft_Windows_Kernel_Power_185_0(Etw):
    pattern = Struct(
        "WokeSystem" / Int8ul,
        "RejectReason" / Int32ul,
        "Uncertain" / Int8ul,
        "Spurious" / Int8ul,
        "FixedWakeSourceMask" / Int32ul,
        "AcAlarmSignaled" / Int8ul,
        "DcAlarmSignaled" / Int8ul,
        "RtcSignaled" / Int8ul,
        "AcProgrammedTime" / Int64ul,
        "DcProgrammedTime" / Int64ul,
        "UsingAcTime" / Int8ul,
        "WakeTime" / Int64ul,
        "AdjustedWakeTime" / Int64ul,
        "FullWake" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=186, version=0)
class Microsoft_Windows_Kernel_Power_186_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=187, version=0)
class Microsoft_Windows_Kernel_Power_187_0(Etw):
    pattern = Struct(
        "ApiCallerNameLength" / Int16ul,
        "ApiCallerName" / Bytes(lambda this: this.ApiCallerNameLength),
        "SystemAction" / Int32ul,
        "LightestSystemState" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=200, version=0)
class Microsoft_Windows_Kernel_Power_200_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmSid" / Sid,
        "SqmWindowsSessionId" / Int32ul,
        "SqmSessionFlags" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=201, version=0)
class Microsoft_Windows_Kernel_Power_201_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=202, version=0)
class Microsoft_Windows_Kernel_Power_202_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=203, version=0)
class Microsoft_Windows_Kernel_Power_203_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=204, version=0)
class Microsoft_Windows_Kernel_Power_204_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=205, version=0)
class Microsoft_Windows_Kernel_Power_205_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=206, version=0)
class Microsoft_Windows_Kernel_Power_206_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=207, version=0)
class Microsoft_Windows_Kernel_Power_207_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmStringDatapointValue" / WString
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=208, version=0)
class Microsoft_Windows_Kernel_Power_208_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=300, version=0)
class Microsoft_Windows_Kernel_Power_300_0(Etw):
    pattern = Struct(
        "Plugin" / Int64ul,
        "Attributes" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=301, version=0)
class Microsoft_Windows_Kernel_Power_301_0(Etw):
    pattern = Struct(
        "Plugin" / Int64ul,
        "Attributes" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=302, version=0)
class Microsoft_Windows_Kernel_Power_302_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Plugin" / Int64ul,
        "IdLength" / Int16ul,
        "Id" / Bytes(lambda this: this.IdLength),
        "Prepared" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=303, version=0)
class Microsoft_Windows_Kernel_Power_303_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Plugin" / Int64ul,
        "PowerState" / Int8ul,
        "Status" / Int32ul,
        "IdLength" / Int16ul,
        "Id" / Bytes(lambda this: this.IdLength),
        "ComponentCount" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=303, version=1)
class Microsoft_Windows_Kernel_Power_303_1(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Plugin" / Int64ul,
        "PowerState" / Int8ul,
        "Status" / Int32ul,
        "IdLength" / Int16ul,
        "Id" / Bytes(lambda this: this.IdLength),
        "ComponentCount" / Int32ul,
        "VetoMasks" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=304, version=0)
class Microsoft_Windows_Kernel_Power_304_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Plugin" / Int64ul,
        "PowerState" / Int8ul,
        "Status" / Int32ul,
        "IdLength" / Int16ul,
        "Id" / Bytes(lambda this: this.IdLength),
        "ComponentCount" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=304, version=1)
class Microsoft_Windows_Kernel_Power_304_1(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Plugin" / Int64ul,
        "PowerState" / Int8ul,
        "Status" / Int32ul,
        "IdLength" / Int16ul,
        "Id" / Bytes(lambda this: this.IdLength),
        "ComponentCount" / Int32ul,
        "VetoMasks" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=305, version=0)
class Microsoft_Windows_Kernel_Power_305_0(Etw):
    pattern = Struct(
        "Token" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=306, version=0)
class Microsoft_Windows_Kernel_Power_306_0(Etw):
    pattern = Struct(
        "Token" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=307, version=0)
class Microsoft_Windows_Kernel_Power_307_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "PowerRequired" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=308, version=0)
class Microsoft_Windows_Kernel_Power_308_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "PowerState" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=309, version=0)
class Microsoft_Windows_Kernel_Power_309_0(Etw):
    pattern = Struct(
        "Token" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=310, version=0)
class Microsoft_Windows_Kernel_Power_310_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Component" / Int32ul,
        "Active" / Int8ul,
        "IdleState" / Int32ul,
        "IdleStateCount" / Int32ul,
        "IdleStates" / Int16ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=310, version=1)
class Microsoft_Windows_Kernel_Power_310_1(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Component" / Int32ul,
        "Active" / Int8ul,
        "IdleState" / Int32ul,
        "IdleStateCount" / Int32ul,
        "IdleStates" / Int16ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=311, version=0)
class Microsoft_Windows_Kernel_Power_311_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Component" / Int32ul,
        "Active" / Int8ul,
        "IdleState" / Int32ul,
        "IdleStateCount" / Int32ul,
        "IdleStates" / Int16ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=311, version=1)
class Microsoft_Windows_Kernel_Power_311_1(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Component" / Int32ul,
        "Active" / Int8ul,
        "IdleState" / Int32ul,
        "IdleStateCount" / Int32ul,
        "IdleStates" / Int16ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=312, version=0)
class Microsoft_Windows_Kernel_Power_312_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Component" / Int32ul,
        "Active" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=313, version=0)
class Microsoft_Windows_Kernel_Power_313_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Component" / Int32ul,
        "IdleState" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=314, version=0)
class Microsoft_Windows_Kernel_Power_314_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Component" / Int32ul,
        "Latency" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=315, version=0)
class Microsoft_Windows_Kernel_Power_315_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Component" / Int32ul,
        "Residency" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=316, version=0)
class Microsoft_Windows_Kernel_Power_316_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Component" / Int32ul,
        "ArmedForWake" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=317, version=0)
class Microsoft_Windows_Kernel_Power_317_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "PowerRequired" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=318, version=0)
class Microsoft_Windows_Kernel_Power_318_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "StateCount" / Int32ul,
        "MinimumDStates" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=319, version=0)
class Microsoft_Windows_Kernel_Power_319_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Component" / Int32ul,
        "StateCount" / Int32ul,
        "MinimumFStates" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=320, version=0)
class Microsoft_Windows_Kernel_Power_320_0(Etw):
    pattern = Struct(
        "DeviceNode" / Int64ul,
        "DeviceIdLength" / Int16ul,
        "DeviceId" / Bytes(lambda this: this.DeviceIdLength),
        "InstancePathLength" / Int16ul,
        "InstancePath" / Bytes(lambda this: this.InstancePathLength),
        "ServiceNameLength" / Int16ul,
        "ServiceName" / Bytes(lambda this: this.ServiceNameLength),
        "PlatformStateDependents" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=320, version=1)
class Microsoft_Windows_Kernel_Power_320_1(Etw):
    pattern = Struct(
        "DeviceNode" / Int64ul,
        "DeviceIdLength" / Int16ul,
        "DeviceId" / Bytes(lambda this: this.DeviceIdLength),
        "InstancePathLength" / Int16ul,
        "InstancePath" / Bytes(lambda this: this.InstancePathLength),
        "ServiceNameLength" / Int16ul,
        "ServiceName" / Bytes(lambda this: this.ServiceNameLength),
        "PlatformStateDependents" / Int32ul,
        "Pdo" / Int64ul,
        "ParentDeviceNode" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=320, version=2)
class Microsoft_Windows_Kernel_Power_320_2(Etw):
    pattern = Struct(
        "DeviceNode" / Int64ul,
        "DeviceIdLength" / Int16ul,
        "DeviceId" / Bytes(lambda this: this.DeviceIdLength),
        "InstancePathLength" / Int16ul,
        "InstancePath" / Bytes(lambda this: this.InstancePathLength),
        "ServiceNameLength" / Int16ul,
        "ServiceName" / Bytes(lambda this: this.ServiceNameLength),
        "PlatformStateDependents" / Int32ul,
        "Pdo" / Int64ul,
        "ParentDeviceNode" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=320, version=3)
class Microsoft_Windows_Kernel_Power_320_3(Etw):
    pattern = Struct(
        "DeviceNode" / Int64ul,
        "DeviceIdLength" / Int16ul,
        "DeviceId" / Bytes(lambda this: this.DeviceIdLength),
        "InstancePathLength" / Int16ul,
        "InstancePath" / Bytes(lambda this: this.InstancePathLength),
        "ServiceNameLength" / Int16ul,
        "ServiceName" / Bytes(lambda this: this.ServiceNameLength),
        "PlatformStateDependents" / Int32ul,
        "Pdo" / Int64ul,
        "ParentDeviceNode" / Int64ul,
        "Flags" / Int32ul,
        "FriendlyNameLength" / Int16ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLength),
        "DripsRequiredState" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=321, version=0)
class Microsoft_Windows_Kernel_Power_321_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Component" / Int32ul,
        "SetCount" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=322, version=0)
class Microsoft_Windows_Kernel_Power_322_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Component" / Int32ul,
        "SetCount" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=323, version=0)
class Microsoft_Windows_Kernel_Power_323_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Component" / Int32ul,
        "Set" / Int32ul,
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "Type" / Int32ul,
        "Unit" / Int32ul,
        "Minimum" / Int64ul,
        "Maximum" / Int64ul,
        "StateCount" / Int32ul,
        "StateValues" / Int64ul,
        "CurrentState" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=324, version=0)
class Microsoft_Windows_Kernel_Power_324_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Component" / Int32ul,
        "Set" / Int32ul,
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "Type" / Int32ul,
        "Unit" / Int32ul,
        "Minimum" / Int64ul,
        "Maximum" / Int64ul,
        "StateCount" / Int32ul,
        "StateValues" / Int64ul,
        "CurrentState" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=325, version=0)
class Microsoft_Windows_Kernel_Power_325_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Component" / Int32ul,
        "PerformanceStateSetCount" / Int32ul,
        "PerformanceStateSets" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=326, version=0)
class Microsoft_Windows_Kernel_Power_326_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Component" / Int32ul,
        "Progress" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=327, version=0)
class Microsoft_Windows_Kernel_Power_327_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Component" / Int32ul,
        "Succeeded" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=328, version=0)
class Microsoft_Windows_Kernel_Power_328_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Component" / Int32ul,
        "DeviceTransition" / Int8ul,
        "PowerState" / Int32ul,
        "PerformanceStateSetCount" / Int32ul,
        "PerformanceStateSets" / Int16ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=329, version=0)
class Microsoft_Windows_Kernel_Power_329_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "StateCount" / Int32ul,
        "TransitionRequired" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=330, version=0)
class Microsoft_Windows_Kernel_Power_330_0(Etw):
    pattern = Struct(
        "StartDevice" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=331, version=0)
class Microsoft_Windows_Kernel_Power_331_0(Etw):
    pattern = Struct(
        "EndDevice" / Int64ul,
        "WorkType" / Int8sl,
        "Phase" / Int8ul,
        "NumberExtraDevices" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=332, version=0)
class Microsoft_Windows_Kernel_Power_332_0(Etw):
    pattern = Struct(
        "EndDevice" / Int64ul,
        "WorkType" / Int8sl,
        "Phase" / Int8ul,
        "NumberExtraDevices" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=333, version=0)
class Microsoft_Windows_Kernel_Power_333_0(Etw):
    pattern = Struct(
        "EndDevice" / Int64ul,
        "WorkType" / Int8sl,
        "Phase" / Int8ul,
        "NumberExtraDevices" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=400, version=0)
class Microsoft_Windows_Kernel_Power_400_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Console" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=401, version=0)
class Microsoft_Windows_Kernel_Power_401_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Console" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=402, version=0)
class Microsoft_Windows_Kernel_Power_402_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Console" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=403, version=0)
class Microsoft_Windows_Kernel_Power_403_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Console" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=404, version=0)
class Microsoft_Windows_Kernel_Power_404_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Console" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=405, version=0)
class Microsoft_Windows_Kernel_Power_405_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Console" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=406, version=0)
class Microsoft_Windows_Kernel_Power_406_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Console" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=407, version=0)
class Microsoft_Windows_Kernel_Power_407_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Console" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=408, version=0)
class Microsoft_Windows_Kernel_Power_408_0(Etw):
    pattern = Struct(
        "UserPresence" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=409, version=0)
class Microsoft_Windows_Kernel_Power_409_0(Etw):
    pattern = Struct(
        "Code" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=410, version=0)
class Microsoft_Windows_Kernel_Power_410_0(Etw):
    pattern = Struct(
        "Engaged" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=411, version=0)
class Microsoft_Windows_Kernel_Power_411_0(Etw):
    pattern = Struct(
        "Engaged" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=412, version=0)
class Microsoft_Windows_Kernel_Power_412_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=413, version=0)
class Microsoft_Windows_Kernel_Power_413_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=414, version=0)
class Microsoft_Windows_Kernel_Power_414_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=414, version=1)
class Microsoft_Windows_Kernel_Power_414_1(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "State" / Int32ul,
        "TransitionCount" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=415, version=0)
class Microsoft_Windows_Kernel_Power_415_0(Etw):
    pattern = Struct(
        "Old" / Int32ul,
        "New" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=416, version=0)
class Microsoft_Windows_Kernel_Power_416_0(Etw):
    pattern = Struct(
        "Value" / Int32ul,
        "Zeroed" / Int32ul,
        "Computed" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=417, version=0)
class Microsoft_Windows_Kernel_Power_417_0(Etw):
    pattern = Struct(
        "Value" / Int32ul,
        "Zeroed" / Int32ul,
        "Computed" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=418, version=0)
class Microsoft_Windows_Kernel_Power_418_0(Etw):
    pattern = Struct(
        "SensorDisplayTimeout" / Int32ul,
        "DisplayTimeout" / Int32ul,
        "SensorInputTimeout" / Int32ul,
        "InputTimeout" / Int32ul,
        "SessionLockedTimeout" / Int32ul,
        "SensorEnabled" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=500, version=0)
class Microsoft_Windows_Kernel_Power_500_0(Etw):
    pattern = Struct(
        "SpindownTimeout" / Int32ul,
        "TimerInterval" / Int32ul,
        "FlushInterval" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=503, version=0)
class Microsoft_Windows_Kernel_Power_503_0(Etw):
    pattern = Struct(
        "DiskDeviceObject" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=504, version=0)
class Microsoft_Windows_Kernel_Power_504_0(Etw):
    pattern = Struct(
        "SystemLatency" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=505, version=0)
class Microsoft_Windows_Kernel_Power_505_0(Etw):
    pattern = Struct(
        "SystemLatency" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=506, version=0)
class Microsoft_Windows_Kernel_Power_506_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=506, version=1)
class Microsoft_Windows_Kernel_Power_506_1(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "LidOpenState" / Int8ul,
        "ExternalMonitorConnectedState" / Int8ul,
        "ScenarioInstanceId" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=506, version=2)
class Microsoft_Windows_Kernel_Power_506_2(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "LidOpenState" / Int8ul,
        "ExternalMonitorConnectedState" / Int8ul,
        "ScenarioInstanceId" / Int8ul,
        "BatteryRemainingCapacityOnEnter" / Int32ul,
        "BatteryFullChargeCapacityOnEnter" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=506, version=3)
class Microsoft_Windows_Kernel_Power_506_3(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "LidOpenState" / Int8ul,
        "ExternalMonitorConnectedState" / Int8ul,
        "ScenarioInstanceId" / Int8ul,
        "BatteryRemainingCapacityOnEnter" / Int32ul,
        "BatteryFullChargeCapacityOnEnter" / Int32ul,
        "ScenarioInstanceIdV2" / Int64ul,
        "BootId" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=507, version=0)
class Microsoft_Windows_Kernel_Power_507_0(Etw):
    pattern = Struct(
        "EnergyDrain" / Int32ul,
        "ActiveResidencyInUs" / Int64ul,
        "NonDripsTimeActivatedInUs" / Int64ul,
        "FirstDripsEntryInUs" / Int64ul,
        "DripsResidencyInUs" / Int64ul,
        "DurationInUs" / Int64ul,
        "DripsTransitions" / Int32ul,
        "FullChargeCapacityRatio" / Int8ul,
        "AudioPlaying" / Int8ul,
        "Reason" / Int32ul,
        "AudioPlaybackInUs" / Int64ul,
        "NonActivatedCpuInUs" / Int64ul,
        "PowerStateAc" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=507, version=1)
class Microsoft_Windows_Kernel_Power_507_1(Etw):
    pattern = Struct(
        "EnergyDrain" / Int32ul,
        "ActiveResidencyInUs" / Int64ul,
        "NonDripsTimeActivatedInUs" / Int64ul,
        "FirstDripsEntryInUs" / Int64ul,
        "DripsResidencyInUs" / Int64ul,
        "DurationInUs" / Int64ul,
        "DripsTransitions" / Int32ul,
        "FullChargeCapacityRatio" / Int8ul,
        "AudioPlaying" / Int8ul,
        "Reason" / Int32ul,
        "AudioPlaybackInUs" / Int64ul,
        "NonActivatedCpuInUs" / Int64ul,
        "PowerStateAc" / Int8ul,
        "HwDripsResidencyInUs" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=507, version=2)
class Microsoft_Windows_Kernel_Power_507_2(Etw):
    pattern = Struct(
        "EnergyDrain" / Int32ul,
        "ActiveResidencyInUs" / Int64ul,
        "NonDripsTimeActivatedInUs" / Int64ul,
        "FirstDripsEntryInUs" / Int64ul,
        "DripsResidencyInUs" / Int64ul,
        "DurationInUs" / Int64ul,
        "DripsTransitions" / Int32ul,
        "FullChargeCapacityRatio" / Int8ul,
        "AudioPlaying" / Int8ul,
        "Reason" / Int32ul,
        "AudioPlaybackInUs" / Int64ul,
        "NonActivatedCpuInUs" / Int64ul,
        "PowerStateAc" / Int8ul,
        "HwDripsResidencyInUs" / Int64ul,
        "ExitLatencyInUs" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=507, version=3)
class Microsoft_Windows_Kernel_Power_507_3(Etw):
    pattern = Struct(
        "EnergyDrain" / Int32ul,
        "ActiveResidencyInUs" / Int64ul,
        "NonDripsTimeActivatedInUs" / Int64ul,
        "FirstDripsEntryInUs" / Int64ul,
        "DripsResidencyInUs" / Int64ul,
        "DurationInUs" / Int64ul,
        "DripsTransitions" / Int32ul,
        "FullChargeCapacityRatio" / Int8ul,
        "AudioPlaying" / Int8ul,
        "Reason" / Int32ul,
        "AudioPlaybackInUs" / Int64ul,
        "NonActivatedCpuInUs" / Int64ul,
        "PowerStateAc" / Int8ul,
        "HwDripsResidencyInUs" / Int64ul,
        "ExitLatencyInUs" / Int64ul,
        "DisconnectedStandby" / Int8ul,
        "AoAcCompliantNic" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=507, version=4)
class Microsoft_Windows_Kernel_Power_507_4(Etw):
    pattern = Struct(
        "EnergyDrain" / Int32ul,
        "ActiveResidencyInUs" / Int64ul,
        "NonDripsTimeActivatedInUs" / Int64ul,
        "FirstDripsEntryInUs" / Int64ul,
        "DripsResidencyInUs" / Int64ul,
        "DurationInUs" / Int64ul,
        "DripsTransitions" / Int32ul,
        "FullChargeCapacityRatio" / Int8ul,
        "AudioPlaying" / Int8ul,
        "Reason" / Int32ul,
        "AudioPlaybackInUs" / Int64ul,
        "NonActivatedCpuInUs" / Int64ul,
        "PowerStateAc" / Int8ul,
        "HwDripsResidencyInUs" / Int64ul,
        "ExitLatencyInUs" / Int64ul,
        "DisconnectedStandby" / Int8ul,
        "AoAcCompliantNic" / Int8ul,
        "NonAttributedCpuInUs" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=507, version=5)
class Microsoft_Windows_Kernel_Power_507_5(Etw):
    pattern = Struct(
        "EnergyDrain" / Int32ul,
        "ActiveResidencyInUs" / Int64ul,
        "NonDripsTimeActivatedInUs" / Int64ul,
        "FirstDripsEntryInUs" / Int64ul,
        "DripsResidencyInUs" / Int64ul,
        "DurationInUs" / Int64ul,
        "DripsTransitions" / Int32ul,
        "FullChargeCapacityRatio" / Int8ul,
        "AudioPlaying" / Int8ul,
        "Reason" / Int32ul,
        "AudioPlaybackInUs" / Int64ul,
        "NonActivatedCpuInUs" / Int64ul,
        "PowerStateAc" / Int8ul,
        "HwDripsResidencyInUs" / Int64ul,
        "ExitLatencyInUs" / Int64ul,
        "DisconnectedStandby" / Int8ul,
        "AoAcCompliantNic" / Int8ul,
        "NonAttributedCpuInUs" / Int64ul,
        "ModernSleepEnabledActionsBitmask" / Int32ul,
        "ModernSleepAppliedActionsBitmask" / Int32ul,
        "LidOpenState" / Int8ul,
        "ExternalMonitorConnectedState" / Int8ul,
        "ScenarioInstanceId" / Int8ul,
        "IsCsSessionInProgressOnExit" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=507, version=6)
class Microsoft_Windows_Kernel_Power_507_6(Etw):
    pattern = Struct(
        "EnergyDrain" / Int32ul,
        "ActiveResidencyInUs" / Int64ul,
        "NonDripsTimeActivatedInUs" / Int64ul,
        "FirstDripsEntryInUs" / Int64ul,
        "DripsResidencyInUs" / Int64ul,
        "DurationInUs" / Int64ul,
        "DripsTransitions" / Int32ul,
        "FullChargeCapacityRatio" / Int8ul,
        "AudioPlaying" / Int8ul,
        "Reason" / Int32ul,
        "AudioPlaybackInUs" / Int64ul,
        "NonActivatedCpuInUs" / Int64ul,
        "PowerStateAc" / Int8ul,
        "HwDripsResidencyInUs" / Int64ul,
        "ExitLatencyInUs" / Int64ul,
        "DisconnectedStandby" / Int8ul,
        "AoAcCompliantNic" / Int8ul,
        "NonAttributedCpuInUs" / Int64ul,
        "ModernSleepEnabledActionsBitmask" / Int32ul,
        "ModernSleepAppliedActionsBitmask" / Int32ul,
        "LidOpenState" / Int8ul,
        "ExternalMonitorConnectedState" / Int8ul,
        "ScenarioInstanceId" / Int8ul,
        "IsCsSessionInProgressOnExit" / Int8ul,
        "BatteryRemainingCapacityOnExit" / Int32ul,
        "BatteryFullChargeCapacityOnExit" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=507, version=7)
class Microsoft_Windows_Kernel_Power_507_7(Etw):
    pattern = Struct(
        "EnergyDrain" / Int32ul,
        "ActiveResidencyInUs" / Int64ul,
        "NonDripsTimeActivatedInUs" / Int64ul,
        "FirstDripsEntryInUs" / Int64ul,
        "DripsResidencyInUs" / Int64ul,
        "DurationInUs" / Int64ul,
        "DripsTransitions" / Int32ul,
        "FullChargeCapacityRatio" / Int8ul,
        "AudioPlaying" / Int8ul,
        "Reason" / Int32ul,
        "AudioPlaybackInUs" / Int64ul,
        "NonActivatedCpuInUs" / Int64ul,
        "PowerStateAc" / Int8ul,
        "HwDripsResidencyInUs" / Int64ul,
        "ExitLatencyInUs" / Int64ul,
        "DisconnectedStandby" / Int8ul,
        "AoAcCompliantNic" / Int8ul,
        "NonAttributedCpuInUs" / Int64ul,
        "ModernSleepEnabledActionsBitmask" / Int32ul,
        "ModernSleepAppliedActionsBitmask" / Int32ul,
        "LidOpenState" / Int8ul,
        "ExternalMonitorConnectedState" / Int8ul,
        "ScenarioInstanceId" / Int8ul,
        "IsCsSessionInProgressOnExit" / Int8ul,
        "BatteryRemainingCapacityOnExit" / Int32ul,
        "BatteryFullChargeCapacityOnExit" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=507, version=8)
class Microsoft_Windows_Kernel_Power_507_8(Etw):
    pattern = Struct(
        "EnergyDrain" / Int32ul,
        "ActiveResidencyInUs" / Int64ul,
        "NonDripsTimeActivatedInUs" / Int64ul,
        "FirstDripsEntryInUs" / Int64ul,
        "DripsResidencyInUs" / Int64ul,
        "DurationInUs" / Int64ul,
        "DripsTransitions" / Int32ul,
        "FullChargeCapacityRatio" / Int8ul,
        "AudioPlaying" / Int8ul,
        "Reason" / Int32ul,
        "AudioPlaybackInUs" / Int64ul,
        "NonActivatedCpuInUs" / Int64ul,
        "PowerStateAc" / Int8ul,
        "HwDripsResidencyInUs" / Int64ul,
        "ExitLatencyInUs" / Int64ul,
        "DisconnectedStandby" / Int8ul,
        "AoAcCompliantNic" / Int8ul,
        "NonAttributedCpuInUs" / Int64ul,
        "ModernSleepEnabledActionsBitmask" / Int32ul,
        "ModernSleepAppliedActionsBitmask" / Int32ul,
        "LidOpenState" / Int8ul,
        "ExternalMonitorConnectedState" / Int8ul,
        "ScenarioInstanceId" / Int8ul,
        "IsCsSessionInProgressOnExit" / Int8ul,
        "BatteryRemainingCapacityOnExit" / Int32ul,
        "BatteryFullChargeCapacityOnExit" / Int32ul,
        "ScenarioInstanceIdV2" / Int64ul,
        "BootId" / Int32ul,
        "InputSuppressionActionCount" / Int32ul,
        "NonResiliencyTimeInUs" / Int64ul,
        "ResiliencyDripsTimeInUs" / Int64ul,
        "ResiliencyHwDripsTimeInUs" / Int64ul,
        "GdiOnTime" / Int64ul,
        "DwmSyncFlushTime" / Int64ul,
        "MonitorPowerOnTime" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=508, version=0)
class Microsoft_Windows_Kernel_Power_508_0(Etw):
    pattern = Struct(
        "Reason" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=509, version=0)
class Microsoft_Windows_Kernel_Power_509_0(Etw):
    pattern = Struct(
        "Flags" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=510, version=0)
class Microsoft_Windows_Kernel_Power_510_0(Etw):
    pattern = Struct(
        "SpmStatus" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=511, version=0)
class Microsoft_Windows_Kernel_Power_511_0(Etw):
    pattern = Struct(
        "SpmStatus" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=512, version=0)
class Microsoft_Windows_Kernel_Power_512_0(Etw):
    pattern = Struct(
        "PolicyGuid" / Guid,
        "PolicyAliasLength" / Int16ul,
        "PolicyAlias" / Bytes(lambda this: this.PolicyAliasLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=513, version=0)
class Microsoft_Windows_Kernel_Power_513_0(Etw):
    pattern = Struct(
        "ScenarioGuid" / Guid,
        "ScenarioNameLength" / Int16ul,
        "ScenarioName" / Bytes(lambda this: this.ScenarioNameLength),
        "Flags" / Int32ul,
        "DefaultSettingsScenarioGuid" / Guid,
        "PolicyCount" / Int16ul,
        "PolicySettings" / Int32sl
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=514, version=0)
class Microsoft_Windows_Kernel_Power_514_0(Etw):
    pattern = Struct(
        "ScenarioInstanceId" / Int8ul,
        "DeviceNode" / Int64ul,
        "Component" / Int32ul,
        "ActiveTime" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=515, version=0)
class Microsoft_Windows_Kernel_Power_515_0(Etw):
    pattern = Struct(
        "ScenarioGuid" / Guid,
        "ScenarioInstanceId" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=515, version=1)
class Microsoft_Windows_Kernel_Power_515_1(Etw):
    pattern = Struct(
        "ScenarioGuid" / Guid,
        "ScenarioInstanceId" / Int8ul,
        "CsEnterReason" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=515, version=2)
class Microsoft_Windows_Kernel_Power_515_2(Etw):
    pattern = Struct(
        "ScenarioGuid" / Guid,
        "ScenarioInstanceId" / Int8ul,
        "CsEnterReason" / Int32ul,
        "BatteryRemainingCapacityOnEnter" / Int32ul,
        "BatteryFullChargeCapacityOnEnter" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=515, version=3)
class Microsoft_Windows_Kernel_Power_515_3(Etw):
    pattern = Struct(
        "ScenarioGuid" / Guid,
        "ScenarioInstanceId" / Int8ul,
        "CsEnterReason" / Int32ul,
        "BatteryRemainingCapacityOnEnter" / Int32ul,
        "BatteryFullChargeCapacityOnEnter" / Int32ul,
        "ScenarioInstanceIdV2" / Int64ul,
        "BootId" / Int32ul,
        "CurrentSystemTime" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=516, version=0)
class Microsoft_Windows_Kernel_Power_516_0(Etw):
    pattern = Struct(
        "EnergyDrain" / Int32ul,
        "DripsResidencyInUs" / Int64ul,
        "OnAc" / Int8ul,
        "HwDripsResidencyInUs" / Int64ul,
        "PreVetoCount" / Int64ul,
        "VetoCount" / Int64ul,
        "DurationInUs" / Int64ul,
        "FullChargeCapacity" / Int32ul,
        "NonActivatedCpuInUs" / Int64ul,
        "IRTruncatePercentage" / Int8ul,
        "DesignCapacity" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=516, version=1)
class Microsoft_Windows_Kernel_Power_516_1(Etw):
    pattern = Struct(
        "EnergyDrain" / Int32ul,
        "DripsResidencyInUs" / Int64ul,
        "OnAc" / Int8ul,
        "HwDripsResidencyInUs" / Int64ul,
        "PreVetoCount" / Int64ul,
        "VetoCount" / Int64ul,
        "DurationInUs" / Int64ul,
        "FullChargeCapacity" / Int32ul,
        "NonActivatedCpuInUs" / Int64ul,
        "IRTruncatePercentage" / Int8ul,
        "DesignCapacity" / Int32ul,
        "AudioDurationInUs" / Int64ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=516, version=2)
class Microsoft_Windows_Kernel_Power_516_2(Etw):
    pattern = Struct(
        "EnergyDrain" / Int32ul,
        "DripsResidencyInUs" / Int64ul,
        "OnAc" / Int8ul,
        "HwDripsResidencyInUs" / Int64ul,
        "PreVetoCount" / Int64ul,
        "VetoCount" / Int64ul,
        "DurationInUs" / Int64ul,
        "FullChargeCapacity" / Int32ul,
        "NonActivatedCpuInUs" / Int64ul,
        "IRTruncatePercentage" / Int8ul,
        "DesignCapacity" / Int32ul,
        "AudioDurationInUs" / Int64ul,
        "Reason" / Int32ul,
        "DisconnectedStandby" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=516, version=3)
class Microsoft_Windows_Kernel_Power_516_3(Etw):
    pattern = Struct(
        "EnergyDrain" / Int32ul,
        "DripsResidencyInUs" / Int64ul,
        "OnAc" / Int8ul,
        "HwDripsResidencyInUs" / Int64ul,
        "PreVetoCount" / Int64ul,
        "VetoCount" / Int64ul,
        "DurationInUs" / Int64ul,
        "FullChargeCapacity" / Int32ul,
        "NonActivatedCpuInUs" / Int64ul,
        "IRTruncatePercentage" / Int8ul,
        "DesignCapacity" / Int32ul,
        "AudioDurationInUs" / Int64ul,
        "Reason" / Int32ul,
        "DisconnectedStandby" / Int8ul,
        "AoAcCompliantNic" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=516, version=4)
class Microsoft_Windows_Kernel_Power_516_4(Etw):
    pattern = Struct(
        "EnergyDrain" / Int32ul,
        "DripsResidencyInUs" / Int64ul,
        "OnAc" / Int8ul,
        "HwDripsResidencyInUs" / Int64ul,
        "PreVetoCount" / Int64ul,
        "VetoCount" / Int64ul,
        "DurationInUs" / Int64ul,
        "FullChargeCapacity" / Int32ul,
        "NonActivatedCpuInUs" / Int64ul,
        "IRTruncatePercentage" / Int8ul,
        "DesignCapacity" / Int32ul,
        "AudioDurationInUs" / Int64ul,
        "Reason" / Int32ul,
        "DisconnectedStandby" / Int8ul,
        "AoAcCompliantNic" / Int8ul,
        "NonAttributedCpuInUs" / Int64ul,
        "EnergySaverPolicy" / Int8ul,
        "VideoTimeoutInSec" / Int32ul,
        "LockConsoleTimeoutInSec" / Int32ul,
        "StandbyTimeoutInSec" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=516, version=5)
class Microsoft_Windows_Kernel_Power_516_5(Etw):
    pattern = Struct(
        "EnergyDrain" / Int32ul,
        "DripsResidencyInUs" / Int64ul,
        "OnAc" / Int8ul,
        "HwDripsResidencyInUs" / Int64ul,
        "PreVetoCount" / Int64ul,
        "VetoCount" / Int64ul,
        "DurationInUs" / Int64ul,
        "FullChargeCapacity" / Int32ul,
        "NonActivatedCpuInUs" / Int64ul,
        "IRTruncatePercentage" / Int8ul,
        "DesignCapacity" / Int32ul,
        "AudioDurationInUs" / Int64ul,
        "Reason" / Int32ul,
        "DisconnectedStandby" / Int8ul,
        "AoAcCompliantNic" / Int8ul,
        "NonAttributedCpuInUs" / Int64ul,
        "EnergySaverPolicy" / Int8ul,
        "VideoTimeoutInSec" / Int32ul,
        "LockConsoleTimeoutInSec" / Int32ul,
        "StandbyTimeoutInSec" / Int32ul,
        "ModernSleepEnabledActionsBitmask" / Int32ul,
        "ModernSleepAppliedActionsBitmask" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=516, version=6)
class Microsoft_Windows_Kernel_Power_516_6(Etw):
    pattern = Struct(
        "EnergyDrain" / Int32ul,
        "DripsResidencyInUs" / Int64ul,
        "OnAc" / Int8ul,
        "HwDripsResidencyInUs" / Int64ul,
        "PreVetoCount" / Int64ul,
        "VetoCount" / Int64ul,
        "DurationInUs" / Int64ul,
        "FullChargeCapacity" / Int32ul,
        "NonActivatedCpuInUs" / Int64ul,
        "IRTruncatePercentage" / Int8ul,
        "DesignCapacity" / Int32ul,
        "AudioDurationInUs" / Int64ul,
        "Reason" / Int32ul,
        "DisconnectedStandby" / Int8ul,
        "AoAcCompliantNic" / Int8ul,
        "NonAttributedCpuInUs" / Int64ul,
        "EnergySaverPolicy" / Int8ul,
        "VideoTimeoutInSec" / Int32ul,
        "LockConsoleTimeoutInSec" / Int32ul,
        "StandbyTimeoutInSec" / Int32ul,
        "ModernSleepEnabledActionsBitmask" / Int32ul,
        "ModernSleepAppliedActionsBitmask" / Int32ul,
        "EnergyDrainV2Flags" / Int32ul,
        "EnergyDrainV2" / Int64sl
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=516, version=7)
class Microsoft_Windows_Kernel_Power_516_7(Etw):
    pattern = Struct(
        "EnergyDrain" / Int32ul,
        "DripsResidencyInUs" / Int64ul,
        "OnAc" / Int8ul,
        "HwDripsResidencyInUs" / Int64ul,
        "PreVetoCount" / Int64ul,
        "VetoCount" / Int64ul,
        "DurationInUs" / Int64ul,
        "FullChargeCapacity" / Int32ul,
        "NonActivatedCpuInUs" / Int64ul,
        "IRTruncatePercentage" / Int8ul,
        "DesignCapacity" / Int32ul,
        "AudioDurationInUs" / Int64ul,
        "Reason" / Int32ul,
        "DisconnectedStandby" / Int8ul,
        "AoAcCompliantNic" / Int8ul,
        "NonAttributedCpuInUs" / Int64ul,
        "EnergySaverPolicy" / Int8ul,
        "VideoTimeoutInSec" / Int32ul,
        "LockConsoleTimeoutInSec" / Int32ul,
        "StandbyTimeoutInSec" / Int32ul,
        "ModernSleepEnabledActionsBitmask" / Int32ul,
        "ModernSleepAppliedActionsBitmask" / Int32ul,
        "EnergyDrainV2Flags" / Int32ul,
        "EnergyDrainV2" / Int64sl,
        "DirectedDripsTransitionCount" / Int32ul,
        "IsHibernateEnabled" / Int8ul,
        "HibernateTimeoutInSec" / Int32ul,
        "HibernateBudgetPercentage" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=516, version=8)
class Microsoft_Windows_Kernel_Power_516_8(Etw):
    pattern = Struct(
        "EnergyDrain" / Int32ul,
        "DripsResidencyInUs" / Int64ul,
        "OnAc" / Int8ul,
        "HwDripsResidencyInUs" / Int64ul,
        "PreVetoCount" / Int64ul,
        "VetoCount" / Int64ul,
        "DurationInUs" / Int64ul,
        "FullChargeCapacity" / Int32ul,
        "NonActivatedCpuInUs" / Int64ul,
        "IRTruncatePercentage" / Int8ul,
        "DesignCapacity" / Int32ul,
        "AudioDurationInUs" / Int64ul,
        "Reason" / Int32ul,
        "DisconnectedStandby" / Int8ul,
        "AoAcCompliantNic" / Int8ul,
        "NonAttributedCpuInUs" / Int64ul,
        "EnergySaverPolicy" / Int8ul,
        "VideoTimeoutInSec" / Int32ul,
        "LockConsoleTimeoutInSec" / Int32ul,
        "StandbyTimeoutInSec" / Int32ul,
        "ModernSleepEnabledActionsBitmask" / Int32ul,
        "ModernSleepAppliedActionsBitmask" / Int32ul,
        "EnergyDrainV2Flags" / Int32ul,
        "EnergyDrainV2" / Int64sl,
        "DirectedDripsTransitionCount" / Int32ul,
        "IsHibernateEnabled" / Int8ul,
        "HibernateTimeoutInSec" / Int32ul,
        "HibernateBudgetPercentage" / Int32ul,
        "IsLockConsoleTimeoutActive" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=516, version=9)
class Microsoft_Windows_Kernel_Power_516_9(Etw):
    pattern = Struct(
        "EnergyDrain" / Int32ul,
        "DripsResidencyInUs" / Int64ul,
        "OnAc" / Int8ul,
        "HwDripsResidencyInUs" / Int64ul,
        "PreVetoCount" / Int64ul,
        "VetoCount" / Int64ul,
        "DurationInUs" / Int64ul,
        "FullChargeCapacity" / Int32ul,
        "NonActivatedCpuInUs" / Int64ul,
        "IRTruncatePercentage" / Int8ul,
        "DesignCapacity" / Int32ul,
        "AudioDurationInUs" / Int64ul,
        "Reason" / Int32ul,
        "DisconnectedStandby" / Int8ul,
        "AoAcCompliantNic" / Int8ul,
        "NonAttributedCpuInUs" / Int64ul,
        "EnergySaverPolicy" / Int8ul,
        "VideoTimeoutInSec" / Int32ul,
        "LockConsoleTimeoutInSec" / Int32ul,
        "StandbyTimeoutInSec" / Int32ul,
        "ModernSleepEnabledActionsBitmask" / Int32ul,
        "ModernSleepAppliedActionsBitmask" / Int32ul,
        "EnergyDrainV2Flags" / Int32ul,
        "EnergyDrainV2" / Int64sl,
        "DirectedDripsTransitionCount" / Int32ul,
        "IsHibernateEnabled" / Int8ul,
        "HibernateTimeoutInSec" / Int32ul,
        "HibernateBudgetPercentage" / Int32ul,
        "IsLockConsoleTimeoutActive" / Int8ul,
        "IsDebuggerEnabled" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=517, version=0)
class Microsoft_Windows_Kernel_Power_517_0(Etw):
    pattern = Struct(
        "ScenarioInstanceId" / Int8ul,
        "DeviceNode" / Int64ul,
        "ActiveTime" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=521, version=0)
class Microsoft_Windows_Kernel_Power_521_0(Etw):
    pattern = Struct(
        "ValidBatteryCount" / Int32ul,
        "ErrorBatteryCount" / Int32ul,
        "AbandonedBatteryCount" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=522, version=0)
class Microsoft_Windows_Kernel_Power_522_0(Etw):
    pattern = Struct(
        "HwDripsTotalTimeValid" / Int8ul,
        "DripsTotalTimeThisPeriodUs" / Int64ul,
        "HwDripsTotalTimeThisPeriodUs" / Int64ul,
        "PopDripsSwHwDivergenceThreshold" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=523, version=0)
class Microsoft_Windows_Kernel_Power_523_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Status" / Int32ul,
        "FailedDriver" / WString,
        "ElapsedTime" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=524, version=0)
class Microsoft_Windows_Kernel_Power_524_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "ActiveBatteryCount" / Int32ul,
        "RemainingPercentage" / Int32ul,
        "IsAcOnline" / Int32ul,
        "BatteryActionInternalFlags" / Int32ul,
        "IsPowerActionCallIgnored" / Int32ul,
        "IsPowerPolicyEnabled" / Int32ul,
        "PowerPolicyAction" / Int32ul,
        "PowerPolicyBatteryLevel" / Int32ul,
        "PowerPolicyEventCode" / Int32ul,
        "PowerPolicyMinState" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=525, version=0)
class Microsoft_Windows_Kernel_Power_525_0(Etw):
    pattern = Struct(
        "DurationInUs" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=527, version=0)
class Microsoft_Windows_Kernel_Power_527_0(Etw):
    pattern = Struct(
        "Event" / Int32ul,
        "Class" / Int32ul,
        "Count" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=528, version=0)
class Microsoft_Windows_Kernel_Power_528_0(Etw):
    pattern = Struct(
        "Event" / Int32ul,
        "Intent" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=529, version=0)
class Microsoft_Windows_Kernel_Power_529_0(Etw):
    pattern = Struct(
        "Intent" / Int32ul,
        "Class" / Int32ul,
        "PowerEvent" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=530, version=0)
class Microsoft_Windows_Kernel_Power_530_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "RequestQueueId" / Int32ul,
        "Intent" / Int32ul,
        "Class" / Int32ul,
        "PowerEvent" / Int32ul,
        "VetoReason" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=531, version=0)
class Microsoft_Windows_Kernel_Power_531_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Action" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=532, version=0)
class Microsoft_Windows_Kernel_Power_532_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=533, version=0)
class Microsoft_Windows_Kernel_Power_533_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "PowerEvent" / Int32ul,
        "Action" / Int32ul,
        "AudioActivity" / Int8ul,
        "DisconnectedStandbyMode" / Int32ul,
        "DsEnabled" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=534, version=0)
class Microsoft_Windows_Kernel_Power_534_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=535, version=0)
class Microsoft_Windows_Kernel_Power_535_0(Etw):
    pattern = Struct(
        "CsSessionId" / Int8ul,
        "Engaged" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=536, version=0)
class Microsoft_Windows_Kernel_Power_536_0(Etw):
    pattern = Struct(
        "CsSessionId" / Int8ul,
        "WorkFlags" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=537, version=0)
class Microsoft_Windows_Kernel_Power_537_0(Etw):
    pattern = Struct(
        "CsSessionId" / Int8ul,
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=538, version=0)
class Microsoft_Windows_Kernel_Power_538_0(Etw):
    pattern = Struct(
        "CsSessionId" / Int8ul,
        "Suspended" / Int8ul,
        "Result" / Int32ul,
        "DurationMs" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=539, version=0)
class Microsoft_Windows_Kernel_Power_539_0(Etw):
    pattern = Struct(
        "CsSessionId" / Int8ul,
        "Suspended" / Int8ul,
        "Result" / Int32ul,
        "DurationMs" / Int64ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=540, version=0)
class Microsoft_Windows_Kernel_Power_540_0(Etw):
    pattern = Struct(
        "EnableResult" / Int32ul,
        "InitializationResult" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=541, version=0)
class Microsoft_Windows_Kernel_Power_541_0(Etw):
    pattern = Struct(
        "SystemIdle" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=541, version=1)
class Microsoft_Windows_Kernel_Power_541_1(Etw):
    pattern = Struct(
        "SystemIdle" / Int8ul,
        "Status" / Int32ul,
        "TimeoutSource" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=542, version=0)
class Microsoft_Windows_Kernel_Power_542_0(Etw):
    pattern = Struct(
        "RequestIndex" / Int32ul,
        "NumberOfRequests" / Int32ul,
        "QueueSize" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=543, version=0)
class Microsoft_Windows_Kernel_Power_543_0(Etw):
    pattern = Struct(
        "CsSessionId" / Int8ul,
        "Count" / Int32ul,
        "IdleMinDurationInUs" / Int64ul,
        "IdleMaxDurationInUs" / Int64ul,
        "IdleTotalDurationInUs" / Int64ul,
        "ReasonDescriptionLength" / Int32ul,
        "ReasonDescription" / Bytes(lambda this: this.ReasonDescriptionLength),
        "GroupCount" / Int16ul,
        "Group" / Int64sl
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=544, version=0)
class Microsoft_Windows_Kernel_Power_544_0(Etw):
    pattern = Struct(
        "OldMask" / Int32ul,
        "NewMask" / Int32ul,
        "SetFlags" / Int32ul,
        "ClearedFlags" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=545, version=0)
class Microsoft_Windows_Kernel_Power_545_0(Etw):
    pattern = Struct(
        "BroadcastTreeId" / Int32ul,
        "IsRootDevice" / Int8ul,
        "DeviceNode" / Int64ul,
        "InstancePathLength" / Int32ul,
        "InstancePath" / Bytes(lambda this: this.InstancePathLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=545, version=1)
class Microsoft_Windows_Kernel_Power_545_1(Etw):
    pattern = Struct(
        "BroadcastTreeId" / Int32ul,
        "IsRootDevice" / Int8ul,
        "DeviceNode" / Int64ul,
        "InstancePathLength" / Int32ul,
        "InstancePath" / Bytes(lambda this: this.InstancePathLength),
        "VisitType" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=546, version=0)
class Microsoft_Windows_Kernel_Power_546_0(Etw):
    pattern = Struct(
        "BroadcastTreeId" / Int32ul,
        "DeviceNode" / Int64ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=547, version=0)
class Microsoft_Windows_Kernel_Power_547_0(Etw):
    pattern = Struct(
        "DeviceNode" / Int64ul,
        "PowerDown" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=548, version=0)
class Microsoft_Windows_Kernel_Power_548_0(Etw):
    pattern = Struct(
        "DeviceNode" / Int64ul,
        "PowerDown" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=548, version=1)
class Microsoft_Windows_Kernel_Power_548_1(Etw):
    pattern = Struct(
        "DeviceNode" / Int64ul,
        "PowerDown" / Int8ul,
        "DevicePowerState" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=549, version=0)
class Microsoft_Windows_Kernel_Power_549_0(Etw):
    pattern = Struct(
        "IdleTimeout" / Int32ul,
        "NotIdleEvents" / Int32ul,
        "IsSystemIdle" / Int8ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=550, version=0)
class Microsoft_Windows_Kernel_Power_550_0(Etw):
    pattern = Struct(
        "EventType" / Int32ul,
        "TimeSinceEvent" / Int32ul,
        "IdleTimeout" / Int32ul,
        "WasIgnored" / Int8ul,
        "BusyReason" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=551, version=0)
class Microsoft_Windows_Kernel_Power_551_0(Etw):
    pattern = Struct(
        "ScanInterval" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=552, version=0)
class Microsoft_Windows_Kernel_Power_552_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "PreviousTimeoutSource" / Int32ul,
        "PreviousTimeout" / Int32ul,
        "NewTimeoutSource" / Int32ul,
        "NewTimeout" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=553, version=0)
class Microsoft_Windows_Kernel_Power_553_0(Etw):
    pattern = Struct(
        "FxDevice" / Int64ul,
        "DeviceNode" / Int64ul,
        "InstancePathLength" / Int32ul,
        "InstancePath" / Bytes(lambda this: this.InstancePathLength)
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=554, version=0)
class Microsoft_Windows_Kernel_Power_554_0(Etw):
    pattern = Struct(
        "CsSessionId" / Int8ul,
        "DeviceNode" / Int64ul,
        "FriendlyNameLength" / Int32ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLength),
        "HardwareIdLength" / Int32ul,
        "HardwareId" / Bytes(lambda this: this.HardwareIdLength),
        "DeviceClassNameLength" / Int32ul,
        "DeviceClassName" / Bytes(lambda this: this.DeviceClassNameLength),
        "DeviceClassGuidLength" / Int32ul,
        "DeviceClassGuid" / Bytes(lambda this: this.DeviceClassGuidLength),
        "BroadcastTreeId" / Int32ul,
        "DfxTransitionCount" / Int32ul,
        "Ps4TransitionCount" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("331c3b3a-2005-44c2-ac5e-77220c37d6b4"), event_id=555, version=0)
class Microsoft_Windows_Kernel_Power_555_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "TriggerFlags" / Int32ul,
        "UserNotify" / Int32ul,
        "PowerAction" / Int32ul,
        "PowerActionFlags" / Int32ul,
        "PowerActionEventCode" / Int32ul,
        "MinState" / Int32ul,
        "SubstitutionPolicy" / Int32ul
    )

