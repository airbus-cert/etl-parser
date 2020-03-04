# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Sysmon
GUID : 5770385f-c22a-43e0-bf4c-06f5698ffbd9
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=1, version=5)
class Microsoft_Windows_Sysmon_1_5(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "UtcTime" / WString,
        "ProcessGuid" / Guid,
        "ProcessId" / Int32ul,
        "Image" / WString,
        "FileVersion" / WString,
        "Description" / WString,
        "Product" / WString,
        "Company" / WString,
        "OriginalFileName" / WString,
        "CommandLine" / WString,
        "CurrentDirectory" / WString,
        "User" / WString,
        "LogonGuid" / Guid,
        "LogonId" / Int64ul,
        "TerminalSessionId" / Int32ul,
        "IntegrityLevel" / WString,
        "Hashes" / WString,
        "ParentProcessGuid" / Guid,
        "ParentProcessId" / Int32ul,
        "ParentImage" / WString,
        "ParentCommandLine" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=2, version=4)
class Microsoft_Windows_Sysmon_2_4(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "UtcTime" / WString,
        "ProcessGuid" / Guid,
        "ProcessId" / Int32ul,
        "Image" / WString,
        "TargetFilename" / WString,
        "CreationUtcTime" / WString,
        "PreviousCreationUtcTime" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=3, version=5)
class Microsoft_Windows_Sysmon_3_5(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "UtcTime" / WString,
        "ProcessGuid" / Guid,
        "ProcessId" / Int32ul,
        "Image" / WString,
        "User" / WString,
        "Protocol" / WString,
        "Initiated" / Int8ul,
        "SourceIsIpv6" / Int8ul,
        "SourceIp" / WString,
        "SourceHostname" / WString,
        "SourcePort" / Int16ul,
        "SourcePortName" / WString,
        "DestinationIsIpv6" / Int8ul,
        "DestinationIp" / WString,
        "DestinationHostname" / WString,
        "DestinationPort" / Int16ul,
        "DestinationPortName" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=4, version=3)
class Microsoft_Windows_Sysmon_4_3(Etw):
    pattern = Struct(
        "UtcTime" / WString,
        "State" / WString,
        "Version" / WString,
        "SchemaVersion" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=5, version=3)
class Microsoft_Windows_Sysmon_5_3(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "UtcTime" / WString,
        "ProcessGuid" / Guid,
        "ProcessId" / Int32ul,
        "Image" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=6, version=3)
class Microsoft_Windows_Sysmon_6_3(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "UtcTime" / WString,
        "ImageLoaded" / WString,
        "Hashes" / WString,
        "Signed" / WString,
        "Signature" / WString,
        "SignatureStatus" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=7, version=3)
class Microsoft_Windows_Sysmon_7_3(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "UtcTime" / WString,
        "ProcessGuid" / Guid,
        "ProcessId" / Int32ul,
        "Image" / WString,
        "ImageLoaded" / WString,
        "FileVersion" / WString,
        "Description" / WString,
        "Product" / WString,
        "Company" / WString,
        "OriginalFileName" / WString,
        "Hashes" / WString,
        "Signed" / WString,
        "Signature" / WString,
        "SignatureStatus" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=8, version=2)
class Microsoft_Windows_Sysmon_8_2(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "UtcTime" / WString,
        "SourceProcessGuid" / Guid,
        "SourceProcessId" / Int32ul,
        "SourceImage" / WString,
        "TargetProcessGuid" / Guid,
        "TargetProcessId" / Int32ul,
        "TargetImage" / WString,
        "NewThreadId" / Int32ul,
        "StartAddress" / WString,
        "StartModule" / WString,
        "StartFunction" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=9, version=2)
class Microsoft_Windows_Sysmon_9_2(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "UtcTime" / WString,
        "ProcessGuid" / Guid,
        "ProcessId" / Int32ul,
        "Image" / WString,
        "Device" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=10, version=3)
class Microsoft_Windows_Sysmon_10_3(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "UtcTime" / WString,
        "SourceProcessGUID" / Guid,
        "SourceProcessId" / Int32ul,
        "SourceThreadId" / Int32ul,
        "SourceImage" / WString,
        "TargetProcessGUID" / Guid,
        "TargetProcessId" / Int32ul,
        "TargetImage" / WString,
        "GrantedAccess" / Int32ul,
        "CallTrace" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=11, version=2)
class Microsoft_Windows_Sysmon_11_2(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "UtcTime" / WString,
        "ProcessGuid" / Guid,
        "ProcessId" / Int32ul,
        "Image" / WString,
        "TargetFilename" / WString,
        "CreationUtcTime" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=12, version=2)
class Microsoft_Windows_Sysmon_12_2(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "EventType" / WString,
        "UtcTime" / WString,
        "ProcessGuid" / Guid,
        "ProcessId" / Int32ul,
        "Image" / WString,
        "TargetObject" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=13, version=2)
class Microsoft_Windows_Sysmon_13_2(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "EventType" / WString,
        "UtcTime" / WString,
        "ProcessGuid" / Guid,
        "ProcessId" / Int32ul,
        "Image" / WString,
        "TargetObject" / WString,
        "Details" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=14, version=2)
class Microsoft_Windows_Sysmon_14_2(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "EventType" / WString,
        "UtcTime" / WString,
        "ProcessGuid" / Guid,
        "ProcessId" / Int32ul,
        "Image" / WString,
        "TargetObject" / WString,
        "NewName" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=15, version=2)
class Microsoft_Windows_Sysmon_15_2(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "UtcTime" / WString,
        "ProcessGuid" / Guid,
        "ProcessId" / Int32ul,
        "Image" / WString,
        "TargetFilename" / WString,
        "CreationUtcTime" / WString,
        "Hash" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=16, version=3)
class Microsoft_Windows_Sysmon_16_3(Etw):
    pattern = Struct(
        "UtcTime" / WString,
        "Configuration" / WString,
        "ConfigurationFileHash" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=17, version=1)
class Microsoft_Windows_Sysmon_17_1(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "EventType" / WString,
        "UtcTime" / WString,
        "ProcessGuid" / Guid,
        "ProcessId" / Int32ul,
        "PipeName" / WString,
        "Image" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=18, version=1)
class Microsoft_Windows_Sysmon_18_1(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "EventType" / WString,
        "UtcTime" / WString,
        "ProcessGuid" / Guid,
        "ProcessId" / Int32ul,
        "PipeName" / WString,
        "Image" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=19, version=3)
class Microsoft_Windows_Sysmon_19_3(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "EventType" / WString,
        "UtcTime" / WString,
        "Operation" / WString,
        "User" / WString,
        "EventNamespace" / WString,
        "Name" / WString,
        "Query" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=20, version=3)
class Microsoft_Windows_Sysmon_20_3(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "EventType" / WString,
        "UtcTime" / WString,
        "Operation" / WString,
        "User" / WString,
        "Name" / WString,
        "Type" / WString,
        "Destination" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=21, version=3)
class Microsoft_Windows_Sysmon_21_3(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "EventType" / WString,
        "UtcTime" / WString,
        "Operation" / WString,
        "User" / WString,
        "Consumer" / WString,
        "Filter" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=22, version=5)
class Microsoft_Windows_Sysmon_22_5(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "UtcTime" / WString,
        "ProcessGuid" / Guid,
        "ProcessId" / Int32ul,
        "QueryName" / WString,
        "QueryStatus" / WString,
        "QueryResults" / WString,
        "Image" / WString
    )


@declare(guid=guid("5770385f-c22a-43e0-bf4c-06f5698ffbd9"), event_id=255, version=3)
class Microsoft_Windows_Sysmon_255_3(Etw):
    pattern = Struct(
        "UtcTime" / WString,
        "ID" / WString,
        "Description" / WString
    )

