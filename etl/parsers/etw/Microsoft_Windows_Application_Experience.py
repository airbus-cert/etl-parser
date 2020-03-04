# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Application-Experience
GUID : eef54e71-0661-422d-9a98-82fd4940b820
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=60, version=0)
class Microsoft_Windows_Application_Experience_60_0(Etw):
    pattern = Struct(
        "DialogGuid" / Guid,
        "ChainId" / Int32ul,
        "ButtonId" / Int32ul
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=70, version=0)
class Microsoft_Windows_Application_Experience_70_0(Etw):
    pattern = Struct(
        "QuestionId" / Guid,
        "QuestionText" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=81, version=0)
class Microsoft_Windows_Application_Experience_81_0(Etw):
    pattern = Struct(
        "QuestionId" / Guid,
        "QuestionKind" / WString,
        "QuestionValue" / Int32ul,
        "FollowupValue" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=100, version=0)
class Microsoft_Windows_Application_Experience_100_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "ApplicationVersion" / WString,
        "ExecutablePath" / WString,
        "ScenarioId" / WString,
        "UserAction" / WString,
        "UserActionID" / WString,
        "CompatibilityLayer" / WString,
        "FileID" / WString,
        "ProgramID" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=103, version=0)
class Microsoft_Windows_Application_Experience_103_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "ApplicationVersion" / WString,
        "ExecutablePath" / WString,
        "ScenarioId" / WString,
        "UserAction" / WString,
        "UserActionID" / WString,
        "CompatibilityLayer" / WString,
        "FileID" / WString,
        "ProgramID" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=104, version=0)
class Microsoft_Windows_Application_Experience_104_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "ApplicationVersion" / WString,
        "ExecutablePath" / WString,
        "ScenarioId" / WString,
        "UserAction" / WString,
        "UserActionID" / WString,
        "CompatibilityLayer" / WString,
        "FileID" / WString,
        "ProgramID" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=105, version=0)
class Microsoft_Windows_Application_Experience_105_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "ApplicationVersion" / WString,
        "ExecutablePath" / WString,
        "ScenarioId" / WString,
        "UserAction" / WString,
        "UserActionID" / WString,
        "CompatibilityLayer" / WString,
        "FileID" / WString,
        "ProgramID" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=207, version=0)
class Microsoft_Windows_Application_Experience_207_0(Etw):
    pattern = Struct(
        "ExecutablePath" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=208, version=0)
class Microsoft_Windows_Application_Experience_208_0(Etw):
    pattern = Struct(
        "ExecutablePath" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=209, version=0)
class Microsoft_Windows_Application_Experience_209_0(Etw):
    pattern = Struct(
        "ExecutablePath" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=210, version=0)
class Microsoft_Windows_Application_Experience_210_0(Etw):
    pattern = Struct(
        "ExecutablePath" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=211, version=0)
class Microsoft_Windows_Application_Experience_211_0(Etw):
    pattern = Struct(
        "ExecutablePath" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=212, version=0)
class Microsoft_Windows_Application_Experience_212_0(Etw):
    pattern = Struct(
        "ExecutablePath" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=213, version=0)
class Microsoft_Windows_Application_Experience_213_0(Etw):
    pattern = Struct(
        "ExecutablePath" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=214, version=0)
class Microsoft_Windows_Application_Experience_214_0(Etw):
    pattern = Struct(
        "ExecutablePath" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=215, version=0)
class Microsoft_Windows_Application_Experience_215_0(Etw):
    pattern = Struct(
        "ExecutablePath" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=300, version=0)
class Microsoft_Windows_Application_Experience_300_0(Etw):
    pattern = Struct(
        "ExecutablePath" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=301, version=0)
class Microsoft_Windows_Application_Experience_301_0(Etw):
    pattern = Struct(
        "ExecutablePath" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=302, version=0)
class Microsoft_Windows_Application_Experience_302_0(Etw):
    pattern = Struct(
        "ExecutablePath" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=303, version=0)
class Microsoft_Windows_Application_Experience_303_0(Etw):
    pattern = Struct(
        "ExecutablePath" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=304, version=0)
class Microsoft_Windows_Application_Experience_304_0(Etw):
    pattern = Struct(
        "ExecutablePath" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=305, version=0)
class Microsoft_Windows_Application_Experience_305_0(Etw):
    pattern = Struct(
        "ExecutablePath" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=306, version=0)
class Microsoft_Windows_Application_Experience_306_0(Etw):
    pattern = Struct(
        "ExecutablePath" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=400, version=0)
class Microsoft_Windows_Application_Experience_400_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=500, version=0)
class Microsoft_Windows_Application_Experience_500_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "StartTime" / Int64ul,
        "FixID" / Guid,
        "Flags" / Int32ul,
        "ExePath" / WString,
        "FixName" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=501, version=0)
class Microsoft_Windows_Application_Experience_501_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "StartTime" / Int64ul,
        "FixID" / Guid,
        "Flags" / Int32ul,
        "ExePath" / WString,
        "FixName" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=502, version=0)
class Microsoft_Windows_Application_Experience_502_0(Etw):
    pattern = Struct(
        "ClientProcessId" / Int32ul,
        "ClientStartTime" / Int64ul,
        "FixID" / Guid,
        "Flags" / Int32ul,
        "ProductCode" / Guid,
        "PackageCode" / Guid,
        "MsiPath" / WString,
        "FixName" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=503, version=0)
class Microsoft_Windows_Application_Experience_503_0(Etw):
    pattern = Struct(
        "ClientProcessId" / Int32ul,
        "ClientStartTime" / Int64ul,
        "FixID" / Guid,
        "Flags" / Int32ul,
        "ProductCode" / Guid,
        "PackageCode" / Guid,
        "MsiPath" / WString,
        "FixName" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=504, version=0)
class Microsoft_Windows_Application_Experience_504_0(Etw):
    pattern = Struct(
        "FixNameLength" / Int32ul,
        "FixName" / WString,
        "FixType" / Int32ul
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=505, version=0)
class Microsoft_Windows_Application_Experience_505_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "StartTime" / Int64ul,
        "FixID" / Guid,
        "Flags" / Int32ul,
        "ExePath" / WString,
        "FixName" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=600, version=0)
class Microsoft_Windows_Application_Experience_600_0(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "StopTime" / Int64ul,
        "ActionCount" / Int32ul,
        "MissedActionCount" / Int32ul,
        "OutputFileLocation" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=601, version=0)
class Microsoft_Windows_Application_Experience_601_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=700, version=0)
class Microsoft_Windows_Application_Experience_700_0(Etw):
    pattern = Struct(
        "FailureCode" / Int32ul
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=703, version=0)
class Microsoft_Windows_Application_Experience_703_0(Etw):
    pattern = Struct(
        "FailureCode" / Int32ul
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=704, version=0)
class Microsoft_Windows_Application_Experience_704_0(Etw):
    pattern = Struct(
        "FailureCode" / Int32ul
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=705, version=0)
class Microsoft_Windows_Application_Experience_705_0(Etw):
    pattern = Struct(
        "FailureCode" / Int32ul
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=706, version=0)
class Microsoft_Windows_Application_Experience_706_0(Etw):
    pattern = Struct(
        "FailureCode" / Int32ul
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=707, version=0)
class Microsoft_Windows_Application_Experience_707_0(Etw):
    pattern = Struct(
        "FailureCode" / Int32ul
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=708, version=0)
class Microsoft_Windows_Application_Experience_708_0(Etw):
    pattern = Struct(
        "FailureCode" / Int32ul
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=910, version=0)
class Microsoft_Windows_Application_Experience_910_0(Etw):
    pattern = Struct(
        "ProgramID" / WString,
        "Name" / WString,
        "Publisher" / WString,
        "Version" / WString,
        "Language" / WString,
        "ProgramType" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=911, version=0)
class Microsoft_Windows_Application_Experience_911_0(Etw):
    pattern = Struct(
        "ProgramID" / WString,
        "FilePath" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=1003, version=0)
class Microsoft_Windows_Application_Experience_1003_0(Etw):
    pattern = Struct(
        "ExtraDataSize" / Int32ul,
        "ExtraData" / Bytes(lambda this: this.ExtraDataSize)
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=1004, version=0)
class Microsoft_Windows_Application_Experience_1004_0(Etw):
    pattern = Struct(
        "ExtraDataSize" / Int32ul,
        "ExtraData" / Bytes(lambda this: this.ExtraDataSize)
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=1005, version=0)
class Microsoft_Windows_Application_Experience_1005_0(Etw):
    pattern = Struct(
        "ExtraDataSize" / Int32ul,
        "ExtraData" / Bytes(lambda this: this.ExtraDataSize)
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=1006, version=0)
class Microsoft_Windows_Application_Experience_1006_0(Etw):
    pattern = Struct(
        "ExtraDataSize" / Int32ul,
        "ExtraData" / Bytes(lambda this: this.ExtraDataSize)
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=1100, version=0)
class Microsoft_Windows_Application_Experience_1100_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "ExtraDataSize" / Int32ul,
        "ExtraData" / Bytes(lambda this: this.ExtraDataSize)
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=1101, version=0)
class Microsoft_Windows_Application_Experience_1101_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "ExtraDataSize" / Int32ul,
        "ExtraData" / Bytes(lambda this: this.ExtraDataSize)
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=1102, version=0)
class Microsoft_Windows_Application_Experience_1102_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "ExtraDataSize" / Int32ul,
        "ExtraData" / Bytes(lambda this: this.ExtraDataSize)
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=2001, version=0)
class Microsoft_Windows_Application_Experience_2001_0(Etw):
    pattern = Struct(
        "cchIdAnalyzedIncludingNull" / Int16ul,
        "cchProgramIdIncludingNull" / Int16ul,
        "ExitCode" / Int32ul,
        "IdTypeAnalyzed" / Int32ul,
        "NumFilesAnalyzed" / Int32ul,
        "NumFilesFailed" / Int32ul,
        "StartTime" / Int64ul,
        "StopTime" / Int64ul,
        "RunTime" / Int64ul,
        "IdAnalyzed" / Bytes(lambda this: this.cchIdAnalyzedIncludingNull),
        "ProgramId" / Bytes(lambda this: this.cchProgramIdIncludingNull)
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=2002, version=0)
class Microsoft_Windows_Application_Experience_2002_0(Etw):
    pattern = Struct(
        "ErrorMessage" / CString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=2003, version=0)
class Microsoft_Windows_Application_Experience_2003_0(Etw):
    pattern = Struct(
        "cchIdAnalyzedIncludingNull" / Int16ul,
        "cchProgramIdIncludingNull" / Int16ul,
        "ExitCode" / Int32ul,
        "IdTypeAnalyzed" / Int32ul,
        "NumFilesAnalyzed" / Int32ul,
        "NumFilesFailed" / Int32ul,
        "StartTime" / Int64ul,
        "StopTime" / Int64ul,
        "RunTime" / Int64ul,
        "IdAnalyzed" / Bytes(lambda this: this.cchIdAnalyzedIncludingNull),
        "ProgramId" / Bytes(lambda this: this.cchProgramIdIncludingNull)
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=2005, version=0)
class Microsoft_Windows_Application_Experience_2005_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "QuirkId" / Int32ul,
        "QuirkName" / WString,
        "CommandLine" / WString,
        "Enabled" / Int8ul,
        "Forced" / Int8ul,
        "PackageFullName" / WString,
        "ApplicationUserModelId" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=5001, version=0)
class Microsoft_Windows_Application_Experience_5001_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "ApplicationVersion" / WString,
        "ExecutablePath" / WString,
        "ScenarioId" / WString,
        "Result" / WString,
        "ResultID" / WString,
        "CompatibilityLayer" / WString,
        "FileID" / WString,
        "ProgramID" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=5002, version=0)
class Microsoft_Windows_Application_Experience_5002_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "ApplicationVersion" / WString,
        "ExecutablePath" / WString,
        "RecommendedLayer" / WString,
        "URL" / WString,
        "CompatStatus" / Int32ul,
        "FileID" / WString,
        "ProgramID" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=5003, version=0)
class Microsoft_Windows_Application_Experience_5003_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "ApplicationVersion" / WString,
        "ExecutablePath" / WString,
        "RecommendedLayer" / WString,
        "VistaPlus" / Int32ul,
        "FileID" / WString,
        "ProgramID" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=5004, version=0)
class Microsoft_Windows_Application_Experience_5004_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "qwData" / Int64ul
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=8000, version=0)
class Microsoft_Windows_Application_Experience_8000_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "ExtraDataSize" / Int32ul,
        "ExtraData" / Bytes(lambda this: this.ExtraDataSize)
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=8001, version=0)
class Microsoft_Windows_Application_Experience_8001_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "ExtraDataSize" / Int32ul,
        "ExtraData" / Bytes(lambda this: this.ExtraDataSize)
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=8002, version=0)
class Microsoft_Windows_Application_Experience_8002_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "ExtraDataSize" / Int32ul,
        "ExtraData" / Bytes(lambda this: this.ExtraDataSize)
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=8003, version=0)
class Microsoft_Windows_Application_Experience_8003_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "ExtraDataSize" / Int32ul,
        "ExtraData" / Bytes(lambda this: this.ExtraDataSize)
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=8004, version=0)
class Microsoft_Windows_Application_Experience_8004_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "ExtraDataSize" / Int32ul,
        "ExtraData" / Bytes(lambda this: this.ExtraDataSize)
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=8005, version=0)
class Microsoft_Windows_Application_Experience_8005_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "ExtraDataSize" / Int32ul,
        "ExtraData" / Bytes(lambda this: this.ExtraDataSize)
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=8006, version=0)
class Microsoft_Windows_Application_Experience_8006_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "ExtraDataSize" / Int32ul,
        "ExtraData" / Bytes(lambda this: this.ExtraDataSize)
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=8007, version=0)
class Microsoft_Windows_Application_Experience_8007_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "ExtraDataSize" / Int32ul,
        "ExtraData" / Bytes(lambda this: this.ExtraDataSize)
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=8008, version=0)
class Microsoft_Windows_Application_Experience_8008_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "ExtraDataSize" / Int32ul,
        "ExtraData" / Bytes(lambda this: this.ExtraDataSize)
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=8010, version=0)
class Microsoft_Windows_Application_Experience_8010_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "ExtraDataSize" / Int32ul,
        "ExtraData" / Bytes(lambda this: this.ExtraDataSize)
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=8011, version=0)
class Microsoft_Windows_Application_Experience_8011_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "ExtraDataSize" / Int32ul,
        "ExtraData" / Bytes(lambda this: this.ExtraDataSize)
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=16000, version=0)
class Microsoft_Windows_Application_Experience_16000_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "CommandLine" / WString,
        "RoutingMode" / WString,
        "Class" / WString,
        "HostDll" / WString,
        "InExMode" / WString,
        "InExIncludes" / WString,
        "InExExcludes" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=16001, version=0)
class Microsoft_Windows_Application_Experience_16001_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Type" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=16002, version=0)
class Microsoft_Windows_Application_Experience_16002_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=16003, version=0)
class Microsoft_Windows_Application_Experience_16003_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "CommandLine" / WString,
        "Enabled" / Int8ul
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=16010, version=0)
class Microsoft_Windows_Application_Experience_16010_0(Etw):
    pattern = Struct(
        "ModuleToHook" / WString,
        "HookModule" / CString,
        "HookApi" / CString,
        "Hooked" / Int8ul,
        "Reason" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=16011, version=0)
class Microsoft_Windows_Application_Experience_16011_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Patched" / Int8ul,
        "Reason" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=16012, version=0)
class Microsoft_Windows_Application_Experience_16012_0(Etw):
    pattern = Struct(
        "Class" / WString,
        "Interface" / WString,
        "ApiIndex" / Int32ul,
        "Hooked" / Int8ul,
        "Reason" / WString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=16100, version=0)
class Microsoft_Windows_Application_Experience_16100_0(Etw):
    pattern = Struct(
        "ShimName" / CString,
        "Message" / CString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=16101, version=0)
class Microsoft_Windows_Application_Experience_16101_0(Etw):
    pattern = Struct(
        "ShimName" / CString,
        "Message" / CString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=16102, version=0)
class Microsoft_Windows_Application_Experience_16102_0(Etw):
    pattern = Struct(
        "ShimName" / CString,
        "Message" / CString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=16103, version=0)
class Microsoft_Windows_Application_Experience_16103_0(Etw):
    pattern = Struct(
        "ShimName" / CString,
        "Message" / CString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=16110, version=0)
class Microsoft_Windows_Application_Experience_16110_0(Etw):
    pattern = Struct(
        "ShimName" / CString,
        "ModuleName" / CString,
        "ApiName" / CString,
        "Info" / CString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=16111, version=0)
class Microsoft_Windows_Application_Experience_16111_0(Etw):
    pattern = Struct(
        "ShimName" / CString,
        "ModuleName" / CString,
        "ApiName" / CString,
        "Info" / CString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=16112, version=0)
class Microsoft_Windows_Application_Experience_16112_0(Etw):
    pattern = Struct(
        "ShimName" / CString,
        "ModuleName" / CString,
        "ApiName" / CString,
        "Info" / CString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=16113, version=0)
class Microsoft_Windows_Application_Experience_16113_0(Etw):
    pattern = Struct(
        "ShimName" / CString,
        "ModuleName" / CString,
        "ApiName" / CString,
        "Info" / CString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=32764, version=0)
class Microsoft_Windows_Application_Experience_32764_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=32765, version=0)
class Microsoft_Windows_Application_Experience_32765_0(Etw):
    pattern = Struct(
        "ChainID" / Int32ul,
        "ProcessID" / Int32ul,
        "Type" / CString,
        "Component" / CString,
        "Message" / CString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=32766, version=0)
class Microsoft_Windows_Application_Experience_32766_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("eef54e71-0661-422d-9a98-82fd4940b820"), event_id=32767, version=0)
class Microsoft_Windows_Application_Experience_32767_0(Etw):
    pattern = Struct(
        "Message" / CString
    )

