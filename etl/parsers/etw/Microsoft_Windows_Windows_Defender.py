# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Windows Defender
GUID : 11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=101, version=0)
class Microsoft_Windows_Windows_Defender_101_0(Etw):
    pattern = Struct(
        "hc_stateid" / Int32ul
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1000, version=0)
class Microsoft_Windows_Windows_Defender_1000_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "ScanID" / WString,
        "ScanTypeIndex" / WString,
        "ScanType" / WString,
        "ScanParametersIndex" / WString,
        "ScanParameters" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString,
        "ScanResources" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1001, version=0)
class Microsoft_Windows_Windows_Defender_1001_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "ScanID" / WString,
        "ScanTypeIndex" / WString,
        "ScanType" / WString,
        "ScanParametersIndex" / WString,
        "ScanParameters" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString,
        "ScanTimeHours" / WString,
        "ScanTimeMinutes" / WString,
        "ScanTimeSeconds" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1002, version=0)
class Microsoft_Windows_Windows_Defender_1002_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "ScanID" / WString,
        "ScanTypeIndex" / WString,
        "ScanType" / WString,
        "ScanParametersIndex" / WString,
        "ScanParameters" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1003, version=0)
class Microsoft_Windows_Windows_Defender_1003_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "ScanID" / WString,
        "ScanTypeIndex" / WString,
        "ScanType" / WString,
        "ScanParametersIndex" / WString,
        "ScanParameters" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1004, version=0)
class Microsoft_Windows_Windows_Defender_1004_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "ScanID" / WString,
        "ScanTypeIndex" / WString,
        "ScanType" / WString,
        "ScanParametersIndex" / WString,
        "ScanParameters" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1005, version=0)
class Microsoft_Windows_Windows_Defender_1005_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "ScanID" / WString,
        "ScanTypeIndex" / WString,
        "ScanType" / WString,
        "ScanParametersIndex" / WString,
        "ScanParameters" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString,
        "ErrorCode" / WString,
        "ErrorDescription" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1006, version=0)
class Microsoft_Windows_Windows_Defender_1006_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "DetectionID" / WString,
        "DetectionSourceIndex" / WString,
        "DetectionSource" / WString,
        "Unused" / WString,
        "ProcessName" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString,
        "ThreatName" / WString,
        "ThreatID" / WString,
        "SeverityID" / WString,
        "CategoryID" / WString,
        "FWLink" / WString,
        "PathFound" / WString,
        "DetectionOriginIndex" / WString,
        "DetectionOrigin" / WString,
        "ExecutionStatusIndex" / WString,
        "ExecutionStatus" / WString,
        "DetectionTypeIndex" / WString,
        "DetectionType" / WString,
        "Unused2" / WString,
        "Unused3" / WString,
        "SeverityName" / WString,
        "CategoryName" / WString,
        "SecurityintelligenceVersion" / WString,
        "EngineVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1007, version=0)
class Microsoft_Windows_Windows_Defender_1007_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "DetectionID" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "StatusCode" / WString,
        "StatusDescription" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString,
        "ThreatName" / WString,
        "ThreatID" / WString,
        "SeverityID" / WString,
        "CategoryID" / WString,
        "FWLink" / WString,
        "Path" / WString,
        "Unused3" / WString,
        "Unused4" / WString,
        "CleaningActionIndex" / WString,
        "CleaningAction" / WString,
        "Unused5" / WString,
        "Unused6" / WString,
        "Unused7" / WString,
        "Unused8" / WString,
        "SeverityName" / WString,
        "CategoryName" / WString,
        "SecurityintelligenceVersion" / WString,
        "EngineVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1008, version=0)
class Microsoft_Windows_Windows_Defender_1008_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "DetectionID" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "StatusCode" / WString,
        "StatusDescription" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString,
        "ThreatName" / WString,
        "ThreatID" / WString,
        "SeverityID" / WString,
        "CategoryID" / WString,
        "FWLink" / WString,
        "Path" / WString,
        "Unused3" / WString,
        "Unused4" / WString,
        "CleaningActionIndex" / WString,
        "CleaningAction" / WString,
        "ErrorCode" / WString,
        "ErrorDescription" / WString,
        "Unused5" / WString,
        "Unused6" / WString,
        "SeverityName" / WString,
        "CategoryName" / WString,
        "SecurityintelligenceVersion" / WString,
        "EngineVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1009, version=0)
class Microsoft_Windows_Windows_Defender_1009_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "Unused3" / WString,
        "Unused4" / WString,
        "Unused5" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString,
        "ThreatName" / WString,
        "ThreatID" / WString,
        "SeverityID" / WString,
        "CategoryID" / WString,
        "FWLink" / WString,
        "Path" / WString,
        "Unused6" / WString,
        "Unused7" / WString,
        "Unused8" / WString,
        "Unused9" / WString,
        "Unused10" / WString,
        "Unused11" / WString,
        "Unused12" / WString,
        "Unused13" / WString,
        "SeverityName" / WString,
        "CategoryName" / WString,
        "SecurityintelligenceVersion" / WString,
        "EngineVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1010, version=0)
class Microsoft_Windows_Windows_Defender_1010_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "ErrorCode" / WString,
        "ErrorDescription" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "Unused3" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString,
        "ThreatName" / WString,
        "ThreatID" / WString,
        "SeverityID" / WString,
        "CategoryID" / WString,
        "FWLink" / WString,
        "Path" / WString,
        "Unused4" / WString,
        "Unused5" / WString,
        "Unused6" / WString,
        "Unused7" / WString,
        "Unused8" / WString,
        "Unused9" / WString,
        "Unused10" / WString,
        "Unused11" / WString,
        "SeverityName" / WString,
        "CategoryName" / WString,
        "SecurityintelligenceVersion" / WString,
        "EngineVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1011, version=0)
class Microsoft_Windows_Windows_Defender_1011_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "Unused3" / WString,
        "Unused4" / WString,
        "Unused5" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString,
        "ThreatName" / WString,
        "ThreatID" / WString,
        "SeverityID" / WString,
        "CategoryID" / WString,
        "FWLink" / WString,
        "Path" / WString,
        "Unused6" / WString,
        "Unused7" / WString,
        "Unused8" / WString,
        "Unused9" / WString,
        "Unused10" / WString,
        "Unused11" / WString,
        "Unused12" / WString,
        "Unused13" / WString,
        "SeverityName" / WString,
        "CategoryName" / WString,
        "SecurityintelligenceVersion" / WString,
        "EngineVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1012, version=0)
class Microsoft_Windows_Windows_Defender_1012_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "ErrorCode" / WString,
        "ErrorDescription" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "Unused3" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString,
        "ThreatName" / WString,
        "ThreatID" / WString,
        "SeverityID" / WString,
        "CategoryID" / WString,
        "FWLink" / WString,
        "Path" / WString,
        "Unused4" / WString,
        "Unused5" / WString,
        "Unused6" / WString,
        "Unused7" / WString,
        "Unused8" / WString,
        "Unused9" / WString,
        "Unused10" / WString,
        "Unused11" / WString,
        "SeverityName" / WString,
        "CategoryName" / WString,
        "SecurityintelligenceVersion" / WString,
        "EngineVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1013, version=0)
class Microsoft_Windows_Windows_Defender_1013_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "Timestamp" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "Unused3" / WString,
        "Unused4" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1014, version=0)
class Microsoft_Windows_Windows_Defender_1014_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "Timestamp" / WString,
        "ErrorCode" / WString,
        "ErrorDescription" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1015, version=0)
class Microsoft_Windows_Windows_Defender_1015_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "DetectionID" / WString,
        "DetectionSourceIndex" / WString,
        "DetectionSource" / WString,
        "Unused" / WString,
        "ProcessName" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString,
        "ThreatName" / WString,
        "ThreatID" / WString,
        "SeverityID" / WString,
        "CategoryID" / WString,
        "FWLink" / WString,
        "PathFound" / WString,
        "DetectionOriginIndex" / WString,
        "DetectionOrigin" / WString,
        "ExecutionStatusIndex" / WString,
        "ExecutionStatus" / WString,
        "DetectionTypeIndex" / WString,
        "DetectionType" / WString,
        "Unused2" / WString,
        "Unused3" / WString,
        "SeverityName" / WString,
        "CategoryName" / WString,
        "SecurityintelligenceVersion" / WString,
        "EngineVersion" / WString,
        "ProcessID" / WString,
        "SecurityintelligenceID" / WString,
        "FidelityValue" / WString,
        "FidelityLabel" / WString,
        "ImageFileHash" / WString,
        "Unused4" / WString,
        "Unused5" / WString,
        "TargetFileName" / WString,
        "TargetFileHash" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1116, version=0)
class Microsoft_Windows_Windows_Defender_1116_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "DetectionID" / WString,
        "DetectionTime" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "ThreatID" / WString,
        "ThreatName" / WString,
        "SeverityID" / WString,
        "SeverityName" / WString,
        "CategoryID" / WString,
        "CategoryName" / WString,
        "FWLink" / WString,
        "StatusCode" / WString,
        "StatusDescription" / WString,
        "State" / WString,
        "SourceID" / WString,
        "SourceName" / WString,
        "ProcessName" / WString,
        "DetectionUser" / WString,
        "Unused3" / WString,
        "Path" / WString,
        "OriginID" / WString,
        "OriginName" / WString,
        "ExecutionID" / WString,
        "ExecutionName" / WString,
        "TypeID" / WString,
        "TypeName" / WString,
        "PreExecutionStatus" / WString,
        "ActionID" / WString,
        "ActionName" / WString,
        "Unused4" / WString,
        "ErrorCode" / WString,
        "ErrorDescription" / WString,
        "Unused5" / WString,
        "PostCleanStatus" / WString,
        "AdditionalActionsID" / WString,
        "AdditionalActionsString" / WString,
        "RemediationUser" / WString,
        "Unused6" / WString,
        "SecurityintelligenceVersion" / WString,
        "EngineVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1117, version=0)
class Microsoft_Windows_Windows_Defender_1117_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "DetectionID" / WString,
        "DetectionTime" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "ThreatID" / WString,
        "ThreatName" / WString,
        "SeverityID" / WString,
        "SeverityName" / WString,
        "CategoryID" / WString,
        "CategoryName" / WString,
        "FWLink" / WString,
        "StatusCode" / WString,
        "StatusDescription" / WString,
        "State" / WString,
        "SourceID" / WString,
        "SourceName" / WString,
        "ProcessName" / WString,
        "DetectionUser" / WString,
        "Unused3" / WString,
        "Path" / WString,
        "OriginID" / WString,
        "OriginName" / WString,
        "ExecutionID" / WString,
        "ExecutionName" / WString,
        "TypeID" / WString,
        "TypeName" / WString,
        "PreExecutionStatus" / WString,
        "ActionID" / WString,
        "ActionName" / WString,
        "Unused4" / WString,
        "ErrorCode" / WString,
        "ErrorDescription" / WString,
        "Unused5" / WString,
        "PostCleanStatus" / WString,
        "AdditionalActionsID" / WString,
        "AdditionalActionsString" / WString,
        "RemediationUser" / WString,
        "Unused6" / WString,
        "SecurityintelligenceVersion" / WString,
        "EngineVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1118, version=0)
class Microsoft_Windows_Windows_Defender_1118_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "DetectionID" / WString,
        "DetectionTime" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "ThreatID" / WString,
        "ThreatName" / WString,
        "SeverityID" / WString,
        "SeverityName" / WString,
        "CategoryID" / WString,
        "CategoryName" / WString,
        "FWLink" / WString,
        "StatusCode" / WString,
        "StatusDescription" / WString,
        "State" / WString,
        "SourceID" / WString,
        "SourceName" / WString,
        "ProcessName" / WString,
        "DetectionUser" / WString,
        "Unused3" / WString,
        "Path" / WString,
        "OriginID" / WString,
        "OriginName" / WString,
        "ExecutionID" / WString,
        "ExecutionName" / WString,
        "TypeID" / WString,
        "TypeName" / WString,
        "PreExecutionStatus" / WString,
        "ActionID" / WString,
        "ActionName" / WString,
        "Unused4" / WString,
        "ErrorCode" / WString,
        "ErrorDescription" / WString,
        "Unused5" / WString,
        "PostCleanStatus" / WString,
        "AdditionalActionsID" / WString,
        "AdditionalActionsString" / WString,
        "RemediationUser" / WString,
        "Unused6" / WString,
        "SecurityintelligenceVersion" / WString,
        "EngineVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1119, version=0)
class Microsoft_Windows_Windows_Defender_1119_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "DetectionID" / WString,
        "DetectionTime" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "ThreatID" / WString,
        "ThreatName" / WString,
        "SeverityID" / WString,
        "SeverityName" / WString,
        "CategoryID" / WString,
        "CategoryName" / WString,
        "FWLink" / WString,
        "StatusCode" / WString,
        "StatusDescription" / WString,
        "State" / WString,
        "SourceID" / WString,
        "SourceName" / WString,
        "ProcessName" / WString,
        "DetectionUser" / WString,
        "Unused3" / WString,
        "Path" / WString,
        "OriginID" / WString,
        "OriginName" / WString,
        "ExecutionID" / WString,
        "ExecutionName" / WString,
        "TypeID" / WString,
        "TypeName" / WString,
        "PreExecutionStatus" / WString,
        "ActionID" / WString,
        "ActionName" / WString,
        "Unused4" / WString,
        "ErrorCode" / WString,
        "ErrorDescription" / WString,
        "Unused5" / WString,
        "PostCleanStatus" / WString,
        "AdditionalActionsID" / WString,
        "AdditionalActionsString" / WString,
        "RemediationUser" / WString,
        "Unused6" / WString,
        "SecurityintelligenceVersion" / WString,
        "EngineVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1120, version=0)
class Microsoft_Windows_Windows_Defender_1120_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "Unused" / WString,
        "Threatresourcepath" / WString,
        "Hashes" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1121, version=0)
class Microsoft_Windows_Windows_Defender_1121_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "Unused" / WString,
        "ID" / WString,
        "DetectionTime" / WString,
        "User" / WString,
        "Path" / WString,
        "ProcessName" / WString,
        "SecurityintelligenceVersion" / WString,
        "EngineVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1122, version=0)
class Microsoft_Windows_Windows_Defender_1122_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "Unused" / WString,
        "ID" / WString,
        "DetectionTime" / WString,
        "User" / WString,
        "Path" / WString,
        "ProcessName" / WString,
        "SecurityintelligenceVersion" / WString,
        "EngineVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1123, version=0)
class Microsoft_Windows_Windows_Defender_1123_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "Unused" / WString,
        "ID" / WString,
        "DetectionTime" / WString,
        "User" / WString,
        "Path" / WString,
        "ProcessName" / WString,
        "SecurityintelligenceVersion" / WString,
        "EngineVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1124, version=0)
class Microsoft_Windows_Windows_Defender_1124_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "Unused" / WString,
        "ID" / WString,
        "DetectionTime" / WString,
        "User" / WString,
        "Path" / WString,
        "ProcessName" / WString,
        "SecurityintelligenceVersion" / WString,
        "EngineVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1125, version=0)
class Microsoft_Windows_Windows_Defender_1125_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "ID" / WString,
        "DetectionTime" / WString,
        "User" / WString,
        "Destination" / WString,
        "ProcessName" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1126, version=0)
class Microsoft_Windows_Windows_Defender_1126_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "ID" / WString,
        "DetectionTime" / WString,
        "User" / WString,
        "Destination" / WString,
        "ProcessName" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1127, version=0)
class Microsoft_Windows_Windows_Defender_1127_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "Unused" / WString,
        "ID" / WString,
        "DetectionTime" / WString,
        "User" / WString,
        "Path" / WString,
        "ProcessName" / WString,
        "SecurityintelligenceVersion" / WString,
        "EngineVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1128, version=0)
class Microsoft_Windows_Windows_Defender_1128_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "Unused" / WString,
        "ID" / WString,
        "DetectionTime" / WString,
        "User" / WString,
        "Path" / WString,
        "ProcessName" / WString,
        "SecurityintelligenceVersion" / WString,
        "EngineVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1150, version=0)
class Microsoft_Windows_Windows_Defender_1150_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "Platformversion" / WString,
        "Unused" / WString,
        "Engineversion" / WString,
        "Securityintelligenceversion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1151, version=0)
class Microsoft_Windows_Windows_Defender_1151_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "Platformversion" / WString,
        "Unused" / WString,
        "Engineversion" / WString,
        "NRIengineversion" / WString,
        "AVsecurityintelligenceversion" / WString,
        "ASsecurityintelligenceversion" / WString,
        "NRIsecurityintelligenceversion" / WString,
        "RTPstate" / WString,
        "OAstate" / WString,
        "IOAVstate" / WString,
        "BMstate" / WString,
        "LastAVsecurityintelligenceage" / WString,
        "LastASsecurityintelligenceage" / WString,
        "Lastquickscanage" / WString,
        "Lastfullscanage" / WString,
        "AVsecurityintelligencecreationtime" / WString,
        "ASsecurityintelligencecreationtime" / WString,
        "Lastquickscanstarttime" / WString,
        "Lastquickscanendtime" / WString,
        "Lastquickscansource" / WString,
        "Lastfullscanstarttime" / WString,
        "Lastfullscanendtime" / WString,
        "Lastfullscansource" / WString,
        "Productstatus" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=1160, version=0)
class Microsoft_Windows_Windows_Defender_1160_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "DetectionID" / WString,
        "DetectionTime" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "ThreatID" / WString,
        "ThreatName" / WString,
        "SeverityID" / WString,
        "SeverityName" / WString,
        "CategoryID" / WString,
        "CategoryName" / WString,
        "FWLink" / WString,
        "StatusCode" / WString,
        "StatusDescription" / WString,
        "State" / WString,
        "SourceID" / WString,
        "SourceName" / WString,
        "ProcessName" / WString,
        "DetectionUser" / WString,
        "Unused3" / WString,
        "Path" / WString,
        "OriginID" / WString,
        "OriginName" / WString,
        "ExecutionID" / WString,
        "ExecutionName" / WString,
        "TypeID" / WString,
        "TypeName" / WString,
        "PreExecutionStatus" / WString,
        "ActionID" / WString,
        "ActionName" / WString,
        "Unused4" / WString,
        "ErrorCode" / WString,
        "ErrorDescription" / WString,
        "Unused5" / WString,
        "PostCleanStatus" / WString,
        "AdditionalActionsID" / WString,
        "AdditionalActionsString" / WString,
        "RemediationUser" / WString,
        "Unused6" / WString,
        "SecurityintelligenceVersion" / WString,
        "EngineVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=2000, version=0)
class Microsoft_Windows_Windows_Defender_2000_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "CurrentsecurityintelligenceVersion" / WString,
        "PrevioussecurityintelligenceVersion" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "Unused3" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString,
        "SecurityintelligenceTypeIndex" / WString,
        "SecurityintelligenceType" / WString,
        "UpdateTypeIndex" / WString,
        "UpdateType" / WString,
        "CurrentEngineVersion" / WString,
        "PreviousEngineVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=2001, version=0)
class Microsoft_Windows_Windows_Defender_2001_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "CurrentsecurityintelligenceVersion" / WString,
        "PrevioussecurityintelligenceVersion" / WString,
        "UpdateSourceIndex" / WString,
        "UpdateSource" / WString,
        "Unused" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString,
        "SecurityintelligenceTypeIndex" / WString,
        "SecurityintelligenceType" / WString,
        "UpdateTypeIndex" / WString,
        "UpdateType" / WString,
        "CurrentEngineVersion" / WString,
        "PreviousEngineVersion" / WString,
        "ErrorCode" / WString,
        "ErrorDescription" / WString,
        "UpdateStateIndex" / WString,
        "UpdateState" / WString,
        "SourcePath" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=2002, version=0)
class Microsoft_Windows_Windows_Defender_2002_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "CurrentEngineVersion" / WString,
        "PreviousEngineVersion" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "Unused3" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString,
        "Unused4" / WString,
        "Unused5" / WString,
        "FeatureIndex" / WString,
        "FeatureName" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=2003, version=0)
class Microsoft_Windows_Windows_Defender_2003_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "CurrentEngineVersion" / WString,
        "PreviousEngineVersion" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "Unused3" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString,
        "ErrorCode" / WString,
        "ErrorDescription" / WString,
        "UpdateStateIndex" / WString,
        "UpdateState" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=2004, version=0)
class Microsoft_Windows_Windows_Defender_2004_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "SecurityintelligenceAttemptedIndex" / WString,
        "SecurityintelligenceAttempted" / WString,
        "ErrorCode" / WString,
        "ErrorDescription" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "Loadingsecurityintelligenceversion" / WString,
        "Loadingengineversion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=2005, version=0)
class Microsoft_Windows_Windows_Defender_2005_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=2006, version=0)
class Microsoft_Windows_Windows_Defender_2006_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "Unused" / WString,
        "ErrorCode" / WString,
        "ErrorDescription" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=2007, version=0)
class Microsoft_Windows_Windows_Defender_2007_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=2010, version=0)
class Microsoft_Windows_Windows_Defender_2010_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "CurrentsecurityintelligenceVersion" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "Unused3" / WString,
        "Unused4" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString,
        "SecurityintelligenceTypeIndex" / WString,
        "SecurityintelligenceType" / WString,
        "Unused5" / WString,
        "Unused6" / WString,
        "CurrentEngineVersion" / WString,
        "Unused7" / WString,
        "Unused8" / WString,
        "Unused9" / WString,
        "Unused10" / WString,
        "Unused11" / WString,
        "Unused12" / WString,
        "DynamicsecurityintelligenceTypeIndex" / WString,
        "DynamicsecurityintelligenceType" / WString,
        "PersistencePath" / WString,
        "DynamicsecurityintelligenceVersion" / WString,
        "DynamicsecurityintelligenceCompilationTimestamp" / WString,
        "PersistenceLimitTypeIndex" / WString,
        "PersistenceLimitType" / WString,
        "PersistenceLimitValue" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=2011, version=0)
class Microsoft_Windows_Windows_Defender_2011_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "CurrentsecurityintelligenceVersion" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "Unused3" / WString,
        "Unused4" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString,
        "SecurityintelligenceTypeIndex" / WString,
        "SecurityintelligenceType" / WString,
        "Unused5" / WString,
        "Unused6" / WString,
        "CurrentEngineVersion" / WString,
        "Unused7" / WString,
        "Unused8" / WString,
        "Unused9" / WString,
        "Unused10" / WString,
        "Unused11" / WString,
        "Unused12" / WString,
        "DynamicsecurityintelligenceTypeIndex" / WString,
        "DynamicsecurityintelligenceType" / WString,
        "PersistencePath" / WString,
        "DynamicsecurityintelligenceVersion" / WString,
        "DynamicsecurityintelligenceCompilationTimestamp" / WString,
        "PersistenceLimitTypeIndex" / WString,
        "PersistenceLimitType" / WString,
        "PersistenceLimitValue" / WString,
        "RemovalReasonIndex" / WString,
        "RemovalReasonValue" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=2012, version=0)
class Microsoft_Windows_Windows_Defender_2012_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "CurrentsecurityintelligenceVersion" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "Unused3" / WString,
        "Unused4" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString,
        "SecurityintelligenceTypeIndex" / WString,
        "SecurityintelligenceType" / WString,
        "Unused5" / WString,
        "Unused6" / WString,
        "CurrentEngineVersion" / WString,
        "Unused7" / WString,
        "ErrorCode" / WString,
        "ErrorDescription" / WString,
        "Unused8" / WString,
        "Unused9" / WString,
        "Unused10" / WString,
        "DynamicsecurityintelligenceTypeIndex" / WString,
        "DynamicsecurityintelligenceType" / WString,
        "PersistencePath" / WString,
        "DynamicsecurityintelligenceVersion" / WString,
        "DynamicsecurityintelligenceCompilationTimestamp" / WString,
        "PersistenceLimitTypeIndex" / WString,
        "PersistenceLimitType" / WString,
        "PersistenceLimitValue" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=2013, version=0)
class Microsoft_Windows_Windows_Defender_2013_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "CurrentsecurityintelligenceVersion" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "Unused3" / WString,
        "Unused4" / WString,
        "Domain" / WString,
        "User" / WString,
        "SID" / WString,
        "SecurityintelligenceTypeIndex" / WString,
        "SecurityintelligenceType" / WString,
        "Unused5" / WString,
        "Unused6" / WString,
        "CurrentEngineVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=2030, version=0)
class Microsoft_Windows_Windows_Defender_2030_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=2031, version=0)
class Microsoft_Windows_Windows_Defender_2031_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "Unused" / WString,
        "ErrorCode" / WString,
        "ErrorDescription" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=2040, version=0)
class Microsoft_Windows_Windows_Defender_2040_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "Unused" / WString,
        "Unused2" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=2041, version=0)
class Microsoft_Windows_Windows_Defender_2041_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "Unused" / WString,
        "Unused2" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=2042, version=0)
class Microsoft_Windows_Windows_Defender_2042_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "Unused" / WString,
        "Unused2" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=2050, version=0)
class Microsoft_Windows_Windows_Defender_2050_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "Filename" / WString,
        "Sha256" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=2051, version=0)
class Microsoft_Windows_Windows_Defender_2051_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "Filename" / WString,
        "Sha256" / WString,
        "CurrentsecurityintelligenceVersion" / WString,
        "CurrentEngineVersion" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=3002, version=0)
class Microsoft_Windows_Windows_Defender_3002_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "FeatureName" / WString,
        "Reason" / WString,
        "ErrorCode" / WString,
        "ErrorDescription" / WString,
        "FeatureID" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=3007, version=0)
class Microsoft_Windows_Windows_Defender_3007_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "FeatureName" / WString,
        "Reason" / WString,
        "Unused" / WString,
        "Unused2" / WString,
        "FeatureID" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=5000, version=0)
class Microsoft_Windows_Windows_Defender_5000_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=5001, version=0)
class Microsoft_Windows_Windows_Defender_5001_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=5004, version=0)
class Microsoft_Windows_Windows_Defender_5004_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "FeatureName" / WString,
        "Configuration" / WString,
        "Unused" / WString,
        "FeatureID" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=5007, version=0)
class Microsoft_Windows_Windows_Defender_5007_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "OldValue" / WString,
        "NewValue" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=5008, version=0)
class Microsoft_Windows_Windows_Defender_5008_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString,
        "Resource" / WString,
        "FailureTypeIndex" / WString,
        "FailureType" / WString,
        "ExceptionCode" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=5009, version=0)
class Microsoft_Windows_Windows_Defender_5009_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=5010, version=0)
class Microsoft_Windows_Windows_Defender_5010_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=5011, version=0)
class Microsoft_Windows_Windows_Defender_5011_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString
    )


@declare(guid=guid("11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78"), event_id=5012, version=0)
class Microsoft_Windows_Windows_Defender_5012_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "ProductVersion" / WString
    )

