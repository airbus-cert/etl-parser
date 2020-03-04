# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DriverFrameworks-UserMode
GUID : 2e35aaeb-857f-4beb-a418-2e6c0e54d988
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=1000, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_1000_1(Etw):
    pattern = Struct(
        "Version" / WString
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=1001, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_1001_1(Etw):
    pattern = Struct(
        "Version" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=1001, version=2)
class Microsoft_Windows_DriverFrameworks_UserMode_1001_2(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=1003, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_1003_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "HostGuid" / WString,
        "InstanceId" / WString
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=1004, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_1004_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "FinalStatus" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=1005, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_1005_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "FinalStatus" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=1006, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_1006_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=1007, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_1007_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "Problem" / Int8ul,
        "DetectedBy" / Int8ul,
        "ActiveOperation" / Int8ul,
        "ExitCode" / Int32ul,
        "Message" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=1008, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_1008_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "TerminationStatus" / Int32ul,
        "ExitCode" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=2000, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_2000_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=2001, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_2001_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "ExitCode" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=2002, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_2002_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "ExitCode" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=2003, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_2003_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "InstanceId" / WString
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=2004, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_2004_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "InstanceId" / WString,
        "Level" / Int32ul,
        "Service" / WString,
        "ClsId" / Guid
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=2005, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_2005_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "InstanceId" / WString,
        "ModulePath" / WString,
        "CompanyName" / WString,
        "FileDescription" / WString,
        "FileVersion" / WString
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=2006, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_2006_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "InstanceId" / WString,
        "Level" / Int32ul,
        "FinalStatus" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=2007, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_2007_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "InstanceId" / WString,
        "Level" / Int32ul,
        "FinalStatus" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=2010, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_2010_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "InstanceId" / WString,
        "FinalStatus" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=2011, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_2011_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "InstanceId" / WString,
        "FinalStatus" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=2100, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_2100_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "InstanceId" / WString,
        "MajorCode" / Int8ul,
        "MinorCode" / Int8ul,
        "Argument1" / Int64ul,
        "Argument2" / Int64ul,
        "Argument3" / Int64ul,
        "Argument4" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=2101, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_2101_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "InstanceId" / WString,
        "MajorCode" / Int8ul,
        "MinorCode" / Int8ul,
        "Argument1" / Int64ul,
        "Argument2" / Int64ul,
        "Argument3" / Int64ul,
        "Argument4" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=2102, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_2102_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "InstanceId" / WString,
        "MajorCode" / Int8ul,
        "MinorCode" / Int8ul,
        "Argument1" / Int64ul,
        "Argument2" / Int64ul,
        "Argument3" / Int64ul,
        "Argument4" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=2103, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_2103_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "InstanceId" / WString,
        "MajorCode" / Int8ul,
        "MinorCode" / Int8ul,
        "Argument1" / Int64ul,
        "Argument2" / Int64ul,
        "Argument3" / Int64ul,
        "Argument4" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=2105, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_2105_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "InstanceId" / WString,
        "MajorCode" / Int8ul,
        "MinorCode" / Int8ul,
        "Argument1" / Int64ul,
        "Argument2" / Int64ul,
        "Argument3" / Int64ul,
        "Argument4" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=2106, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_2106_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "InstanceId" / WString,
        "MajorCode" / Int8ul,
        "MinorCode" / Int8ul,
        "Argument1" / Int64ul,
        "Argument2" / Int64ul,
        "Argument3" / Int64ul,
        "Argument4" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=2107, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_2107_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "InstanceId" / WString,
        "MajorCode" / Int8ul,
        "MinorCode" / Int8ul,
        "Argument1" / Int64ul,
        "Argument2" / Int64ul,
        "Argument3" / Int64ul,
        "Argument4" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=2900, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_2900_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=2901, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_2901_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=3000, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_3000_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "InstanceId" / WString,
        "Level" / Int32ul,
        "StateMachine" / Int8ul,
        "Event" / Int32ul,
        "Queueing" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=3001, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_3001_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "InstanceId" / WString,
        "Level" / Int32ul,
        "StateMachine" / Int8ul,
        "Event" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=3010, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_3010_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "InstanceId" / WString,
        "Level" / Int32ul,
        "StateMachine" / Int32ul,
        "CurrentState" / Int32ul,
        "Event" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=3011, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_3011_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "InstanceId" / WString,
        "Level" / Int32ul,
        "StateMachine" / Int8ul,
        "CurrentState" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=3020, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_3020_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "InstanceId" / WString,
        "Level" / Int32ul,
        "StateMachine" / Int8ul,
        "Event" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=10000, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_10000_1(Etw):
    pattern = Struct(
        "DeviceId" / WString,
        "FrameworkVersion" / WString
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=10001, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_10001_1(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "CLSID" / Guid,
        "FxVersion" / WString,
        "Upgrade" / Int8ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=10002, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_10002_1(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "CLSID" / Guid,
        "FxVersion" / WString,
        "Upgrade" / Int8ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=10100, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_10100_1(Etw):
    pattern = Struct(
        "FinalStatus" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=10101, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_10101_1(Etw):
    pattern = Struct(
        "FinalStatus" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=10110, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_10110_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "Problem" / Int8ul,
        "DetectedBy" / Int8ul,
        "ActiveOperation" / Int8ul,
        "ExitCode" / Int32ul,
        "Message" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=10111, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_10111_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "FriendlyName" / WString,
        "Location" / WString,
        "InstanceId" / WString,
        "RestartCount" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=10112, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_10112_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "FriendlyName" / WString,
        "Location" / WString,
        "InstanceId" / WString,
        "RestartCount" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=10113, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_10113_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "InstanceId" / WString,
        "ConflictingParameter" / WString,
        "Value" / Int64ul,
        "DriverName" / WString
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=10115, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_10115_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "FriendlyName" / WString,
        "Location" / WString,
        "InstanceId" / WString,
        "RestartCount" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=10116, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_10116_1(Etw):
    pattern = Struct(
        "LifetimeId" / Guid,
        "FriendlyName" / WString,
        "Location" / WString,
        "InstanceId" / WString,
        "RestartCount" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=10117, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_10117_1(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ActualFuntionTableCount" / Int32ul,
        "ExpectedFuntionTableCount" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=19999, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_19999_1(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=20030, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_20030_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Device" / Int64ul,
        "DriverName" / WString
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=20031, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_20031_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Device" / Int64ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=20032, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_20032_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Device" / Int64ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=20033, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_20033_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Device" / Int64ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=30008, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_30008_1(Etw):
    pattern = Struct(
        "HwAccessTargetType" / Int32ul,
        "HwAccessTargetSize" / Int32ul,
        "HwAccessBufferCount" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=30009, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_30009_1(Etw):
    pattern = Struct(
        "HwAccessTargetType" / Int32ul,
        "HwAccessTargetSize" / Int32ul,
        "HwAccessBufferCount" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=30010, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_30010_1(Etw):
    pattern = Struct(
        "HwAccessTargetType" / Int32ul,
        "HwAccessTargetSize" / Int32ul,
        "HwAccessBufferCount" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=30011, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_30011_1(Etw):
    pattern = Struct(
        "HwAccessTargetType" / Int32ul,
        "HwAccessTargetSize" / Int32ul,
        "HwAccessBufferCount" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=30012, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_30012_1(Etw):
    pattern = Struct(
        "HwAccessTargetType" / Int32ul,
        "HwAccessTargetSize" / Int32ul,
        "HwAccessBufferCount" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=30013, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_30013_1(Etw):
    pattern = Struct(
        "HwAccessTargetType" / Int32ul,
        "HwAccessTargetSize" / Int32ul,
        "HwAccessBufferCount" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=30014, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_30014_1(Etw):
    pattern = Struct(
        "HwAccessTargetType" / Int32ul,
        "HwAccessTargetSize" / Int32ul,
        "HwAccessBufferCount" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=30015, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_30015_1(Etw):
    pattern = Struct(
        "HwAccessTargetType" / Int32ul,
        "HwAccessTargetSize" / Int32ul,
        "HwAccessBufferCount" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=30016, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_30016_1(Etw):
    pattern = Struct(
        "HwAccessTargetType" / Int32ul,
        "HwAccessTargetSize" / Int32ul,
        "HwAccessBufferCount" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=30017, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_30017_1(Etw):
    pattern = Struct(
        "HwAccessTargetType" / Int32ul,
        "HwAccessTargetSize" / Int32ul,
        "HwAccessBufferCount" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=30018, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_30018_1(Etw):
    pattern = Struct(
        "HwAccessTargetType" / Int32ul,
        "HwAccessTargetSize" / Int32ul,
        "HwAccessBufferCount" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=30019, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_30019_1(Etw):
    pattern = Struct(
        "HwAccessTargetType" / Int32ul,
        "HwAccessTargetSize" / Int32ul,
        "HwAccessBufferCount" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=30020, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_30020_1(Etw):
    pattern = Struct(
        "InterruptMessageNumber" / Int32ul
    )


@declare(guid=guid("2e35aaeb-857f-4beb-a418-2e6c0e54d988"), event_id=30021, version=1)
class Microsoft_Windows_DriverFrameworks_UserMode_30021_1(Etw):
    pattern = Struct(
        "InterruptMessageNumber" / Int32ul
    )

