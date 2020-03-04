# -*- coding: utf-8 -*-
"""
Microsoft-Windows-AppHost
GUID : 98e0765d-8c42-44a3-a57b-760d7f93225a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=102, version=0)
class Microsoft_Windows_AppHost_102_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul,
        "PID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=112, version=0)
class Microsoft_Windows_AppHost_112_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "PID" / Int32sl,
        "ProcessCreationTime" / WString,
        "ApplicationBinaryPath" / WString,
        "ReportId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=121, version=0)
class Microsoft_Windows_AppHost_121_0(Etw):
    pattern = Struct(
        "HResultErrorCode" / Int32ul,
        "PID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=122, version=0)
class Microsoft_Windows_AppHost_122_0(Etw):
    pattern = Struct(
        "HResultErrorCode" / Int32ul,
        "PID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=126, version=0)
class Microsoft_Windows_AppHost_126_0(Etw):
    pattern = Struct(
        "DisplayName" / WString,
        "ApplicationName" / WString,
        "AppUserModelId" / WString,
        "PackageFullName" / WString,
        "ProcessId" / Int32sl,
        "ErrorType" / WString,
        "ErrorDescription" / WString,
        "DocumentFile" / WString,
        "SourceFile" / WString,
        "SourceLine" / Int32sl,
        "SourceColumn" / Int32sl,
        "StackTrace" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=127, version=0)
class Microsoft_Windows_AppHost_127_0(Etw):
    pattern = Struct(
        "DisplayName" / WString,
        "ApplicationName" / WString,
        "AppUserModelId" / WString,
        "PackageFullName" / WString,
        "ProcessId" / Int32sl,
        "ErrorDescription" / WString,
        "DocumentFile" / WString,
        "StackTrace" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=128, version=0)
class Microsoft_Windows_AppHost_128_0(Etw):
    pattern = Struct(
        "PID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=129, version=0)
class Microsoft_Windows_AppHost_129_0(Etw):
    pattern = Struct(
        "PID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=131, version=0)
class Microsoft_Windows_AppHost_131_0(Etw):
    pattern = Struct(
        "DisplayName" / WString,
        "ApplicationName" / WString,
        "AppUserModelId" / WString,
        "PackageFullName" / WString,
        "ProcessId" / Int32sl,
        "DocumentFile" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=132, version=0)
class Microsoft_Windows_AppHost_132_0(Etw):
    pattern = Struct(
        "DisplayName" / WString,
        "ApplicationName" / WString,
        "AppUserModelId" / WString,
        "PackageFullName" / WString,
        "ProcessId" / Int32sl,
        "DocumentFile" / WString,
        "TargetUrl" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=133, version=0)
class Microsoft_Windows_AppHost_133_0(Etw):
    pattern = Struct(
        "Function" / WString,
        "Module" / WString,
        "HResult" / Int32ul,
        "PID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=134, version=0)
class Microsoft_Windows_AppHost_134_0(Etw):
    pattern = Struct(
        "Function" / WString,
        "Module" / WString,
        "WebInstance" / Int32sl,
        "HResult" / Int32ul,
        "PID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=135, version=0)
class Microsoft_Windows_AppHost_135_0(Etw):
    pattern = Struct(
        "WebInstance" / Int32sl,
        "HResult" / Int32ul,
        "PID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=136, version=0)
class Microsoft_Windows_AppHost_136_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul,
        "PID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=137, version=0)
class Microsoft_Windows_AppHost_137_0(Etw):
    pattern = Struct(
        "PID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=500, version=0)
class Microsoft_Windows_AppHost_500_0(Etw):
    pattern = Struct(
        "Function" / WString,
        "Module" / WString,
        "PID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=502, version=0)
class Microsoft_Windows_AppHost_502_0(Etw):
    pattern = Struct(
        "Function" / WString,
        "Module" / WString,
        "WebInstance" / Int32sl,
        "PID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=504, version=0)
class Microsoft_Windows_AppHost_504_0(Etw):
    pattern = Struct(
        "Action" / WString,
        "WebInstance" / Int32sl,
        "PID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=506, version=0)
class Microsoft_Windows_AppHost_506_0(Etw):
    pattern = Struct(
        "PID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=507, version=0)
class Microsoft_Windows_AppHost_507_0(Etw):
    pattern = Struct(
        "PID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=508, version=0)
class Microsoft_Windows_AppHost_508_0(Etw):
    pattern = Struct(
        "PID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=509, version=0)
class Microsoft_Windows_AppHost_509_0(Etw):
    pattern = Struct(
        "WindowType" / Int32sl,
        "WebPlatformSuspendDownloadPending" / Int8ul,
        "WebPlatformCleanupPending" / Int8ul,
        "WerReportDuringSuspend" / Int8ul,
        "suspendSubdownloadsCount" / Int32sl,
        "NewTimeout" / Int32sl,
        "CurrentTimeout" / Int32sl,
        "PID" / Int32sl,
        "TID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=511, version=0)
class Microsoft_Windows_AppHost_511_0(Etw):
    pattern = Struct(
        "PID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=512, version=0)
class Microsoft_Windows_AppHost_512_0(Etw):
    pattern = Struct(
        "PID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=513, version=0)
class Microsoft_Windows_AppHost_513_0(Etw):
    pattern = Struct(
        "PID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=514, version=0)
class Microsoft_Windows_AppHost_514_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "OSVersion" / Int64ul,
        "WebPlatformVersion" / Int64ul,
        "ScriptProjectionVersion" / Int32ul
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=515, version=0)
class Microsoft_Windows_AppHost_515_0(Etw):
    pattern = Struct(
        "MainWebInstanceInitializeTime" / Int64ul,
        "AppSuspendHandlerInvoked" / Int64ul,
        "AppSuspendHandlerCompleted" / Int64ul,
        "WebPlatformSuspendDownloadPending" / Int8ul,
        "WebPlatformSuspendDownloadCount" / Int32sl,
        "WebPlatformSuspendDownloadWaitStart" / Int64ul,
        "WebPlatformCleanupPending" / Int8ul,
        "WebPlatformCleanupStart" / Int64ul,
        "CurrentSuspendingTimeout" / Int32sl,
        "NewSuspendingTimeout" / Int32sl,
        "PID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=516, version=0)
class Microsoft_Windows_AppHost_516_0(Etw):
    pattern = Struct(
        "WindowType" / Int32sl,
        "WebPlatformSuspendDownloadPending" / Int8ul,
        "WebPlatformCleanupPending" / Int8ul,
        "suspendSubdownloadsCount" / Int32sl,
        "PID" / Int32sl,
        "TID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=517, version=0)
class Microsoft_Windows_AppHost_517_0(Etw):
    pattern = Struct(
        "WindowType" / Int32sl,
        "WebPlatformSuspendDownloadPending" / Int8ul,
        "WebPlatformCleanupPending" / Int8ul,
        "PID" / Int32sl,
        "TID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=518, version=0)
class Microsoft_Windows_AppHost_518_0(Etw):
    pattern = Struct(
        "WindowType" / Int32sl,
        "WebPlatformSuspendDownloadPending" / Int8ul,
        "WebPlatformCleanupPending" / Int8ul,
        "PID" / Int32sl,
        "TID" / Int32sl,
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=1011, version=0)
class Microsoft_Windows_AppHost_1011_0(Etw):
    pattern = Struct(
        "ObjectWWA" / Int64ul,
        "Counter" / Int32ul,
        "PackageFullName" / WString,
        "AppID" / WString,
        "NavigationInfo" / Int32ul
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=1012, version=0)
class Microsoft_Windows_AppHost_1012_0(Etw):
    pattern = Struct(
        "ObjectWWA" / Int64ul,
        "Counter" / Int32ul,
        "PackageFullName" / WString,
        "AppID" / WString,
        "NavigationInfo" / Int32ul
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=1019, version=0)
class Microsoft_Windows_AppHost_1019_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "AppID" / WString,
        "ContractID" / WString,
        "IsReactivation" / Int32ul
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=1020, version=0)
class Microsoft_Windows_AppHost_1020_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "AppID" / WString,
        "ContractID" / WString,
        "IsReactivation" / Int32ul
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=1021, version=0)
class Microsoft_Windows_AppHost_1021_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "AppID" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=1022, version=0)
class Microsoft_Windows_AppHost_1022_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "AppID" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=1061, version=0)
class Microsoft_Windows_AppHost_1061_0(Etw):
    pattern = Struct(
        "Priority" / Int32sl,
        "Id" / Int64ul
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=1062, version=0)
class Microsoft_Windows_AppHost_1062_0(Etw):
    pattern = Struct(
        "Priority" / Int32sl,
        "Id" / Int64ul
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=1063, version=0)
class Microsoft_Windows_AppHost_1063_0(Etw):
    pattern = Struct(
        "JSHeapSizeMB" / Int32ul,
        "TotalWorkingSetMBandPrivateCommitMB" / Int32ul,
        "PackageAgeS" / Int32ul,
        "AppID" / WString,
        "PackageFullName" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=1066, version=0)
class Microsoft_Windows_AppHost_1066_0(Etw):
    pattern = Struct(
        "ToggleCount" / Int32ul,
        "ToggleDetail" / Int32ul,
        "PackageFullName" / WString,
        "AppID" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=1067, version=0)
class Microsoft_Windows_AppHost_1067_0(Etw):
    pattern = Struct(
        "FilePath" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=1068, version=0)
class Microsoft_Windows_AppHost_1068_0(Etw):
    pattern = Struct(
        "FilePath" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=10000, version=0)
class Microsoft_Windows_AppHost_10000_0(Etw):
    pattern = Struct(
        "DisplayName" / WString,
        "ApplicationName" / WString,
        "AppUserModelId" / WString,
        "PackageFullName" / WString,
        "ProcessId" / Int32sl,
        "Source" / WString,
        "DocumentFile" / WString,
        "Line" / Int32sl,
        "Column" / Int32sl,
        "MessageId" / Int32sl,
        "Message" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=10001, version=0)
class Microsoft_Windows_AppHost_10001_0(Etw):
    pattern = Struct(
        "DisplayName" / WString,
        "ApplicationName" / WString,
        "AppUserModelId" / WString,
        "PackageFullName" / WString,
        "ProcessId" / Int32sl,
        "Source" / WString,
        "DocumentFile" / WString,
        "Line" / Int32sl,
        "Column" / Int32sl,
        "MessageId" / Int32sl,
        "Message" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=10002, version=0)
class Microsoft_Windows_AppHost_10002_0(Etw):
    pattern = Struct(
        "DisplayName" / WString,
        "ApplicationName" / WString,
        "AppUserModelId" / WString,
        "PackageFullName" / WString,
        "ProcessId" / Int32sl,
        "Source" / WString,
        "DocumentFile" / WString,
        "Line" / Int32sl,
        "Column" / Int32sl,
        "MessageId" / Int32sl,
        "Message" / WString
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=10003, version=0)
class Microsoft_Windows_AppHost_10003_0(Etw):
    pattern = Struct(
        "DeferralCount" / Int32sl
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=10004, version=0)
class Microsoft_Windows_AppHost_10004_0(Etw):
    pattern = Struct(
        "DeferralCount" / Int32sl
    )


@declare(guid=guid("98e0765d-8c42-44a3-a57b-760d7f93225a"), event_id=10007, version=0)
class Microsoft_Windows_AppHost_10007_0(Etw):
    pattern = Struct(
        "Value" / WString
    )

