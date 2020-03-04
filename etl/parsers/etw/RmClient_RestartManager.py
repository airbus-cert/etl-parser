# -*- coding: utf-8 -*-
"""
Microsoft-Windows-RestartManager
GUID : 0888e5ef-9b98-4695-979d-e92ce4247224
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("0888e5ef-9b98-4695-979d-e92ce4247224"), event_id=10000, version=0)
class Microsoft_Windows_RestartManager_10000_0(Etw):
    pattern = Struct(
        "RmSessionId" / Int32ul,
        "UTCStartTime" / Int64ul
    )


@declare(guid=guid("0888e5ef-9b98-4695-979d-e92ce4247224"), event_id=10001, version=0)
class Microsoft_Windows_RestartManager_10001_0(Etw):
    pattern = Struct(
        "RmSessionId" / Int32ul,
        "UTCStartTime" / Int64ul
    )


@declare(guid=guid("0888e5ef-9b98-4695-979d-e92ce4247224"), event_id=10002, version=0)
class Microsoft_Windows_RestartManager_10002_0(Etw):
    pattern = Struct(
        "RmSessionId" / Int32ul,
        "FullPath" / WString,
        "DisplayName" / WString,
        "AppVersion" / Int32ul,
        "AppType" / Int32ul,
        "TSSessionId" / Int32ul,
        "Status" / Int32ul,
        "Pid" / Int32ul,
        "nFiles" / Int32ul,
        "File" / WString
    )


@declare(guid=guid("0888e5ef-9b98-4695-979d-e92ce4247224"), event_id=10003, version=0)
class Microsoft_Windows_RestartManager_10003_0(Etw):
    pattern = Struct(
        "RmSessionId" / Int32ul,
        "FullPath" / WString,
        "DisplayName" / WString,
        "AppVersion" / Int32ul,
        "AppType" / Int32ul,
        "TSSessionId" / Int32ul,
        "Status" / Int32ul,
        "Pid" / Int32ul,
        "nFiles" / Int32ul,
        "File" / WString
    )


@declare(guid=guid("0888e5ef-9b98-4695-979d-e92ce4247224"), event_id=10004, version=0)
class Microsoft_Windows_RestartManager_10004_0(Etw):
    pattern = Struct(
        "RmSessionId" / Int32ul,
        "nFiles" / Int32ul,
        "nRegProcs" / Int32ul,
        "nRegServices" / Int32ul,
        "Files" / WString,
        "RegProcs" / WString,
        "RegServices" / WString
    )


@declare(guid=guid("0888e5ef-9b98-4695-979d-e92ce4247224"), event_id=10005, version=0)
class Microsoft_Windows_RestartManager_10005_0(Etw):
    pattern = Struct(
        "RmSessionId" / Int32ul,
        "nApplications" / Int32ul,
        "Applications" / WString,
        "dwRebootReasons" / Int32ul
    )


@declare(guid=guid("0888e5ef-9b98-4695-979d-e92ce4247224"), event_id=10006, version=0)
class Microsoft_Windows_RestartManager_10006_0(Etw):
    pattern = Struct(
        "RmSessionId" / Int32ul,
        "FullPath" / WString,
        "DisplayName" / WString,
        "AppVersion" / Int32ul,
        "AppType" / Int32ul,
        "TSSessionId" / Int32ul,
        "Status" / Int32ul,
        "Pid" / Int32ul,
        "nFiles" / Int32ul,
        "File" / WString
    )


@declare(guid=guid("0888e5ef-9b98-4695-979d-e92ce4247224"), event_id=10007, version=0)
class Microsoft_Windows_RestartManager_10007_0(Etw):
    pattern = Struct(
        "RmSessionId" / Int32ul,
        "FullPath" / WString,
        "DisplayName" / WString,
        "AppVersion" / Int32ul,
        "AppType" / Int32ul,
        "TSSessionId" / Int32ul,
        "Status" / Int32ul,
        "Pid" / Int32ul,
        "nFiles" / Int32ul,
        "File" / WString
    )


@declare(guid=guid("0888e5ef-9b98-4695-979d-e92ce4247224"), event_id=10008, version=0)
class Microsoft_Windows_RestartManager_10008_0(Etw):
    pattern = Struct(
        "RmSessionId" / Int32ul,
        "cbSize" / Int32ul,
        "pbBinary" / Bytes(lambda this: this.cbSize)
    )


@declare(guid=guid("0888e5ef-9b98-4695-979d-e92ce4247224"), event_id=10009, version=0)
class Microsoft_Windows_RestartManager_10009_0(Etw):
    pattern = Struct(
        "RmSessionId" / Int32ul,
        "SvcHostPid" / Int32ul,
        "nFiles" / Int32ul,
        "nServices" / Int32ul,
        "FileName" / WString,
        "Service" / WString
    )


@declare(guid=guid("0888e5ef-9b98-4695-979d-e92ce4247224"), event_id=10010, version=0)
class Microsoft_Windows_RestartManager_10010_0(Etw):
    pattern = Struct(
        "RmSessionId" / Int32ul,
        "Pid" / Int32ul,
        "FullPath" / WString,
        "DisplayName" / WString,
        "AppVersion" / Int32ul,
        "AppType" / Int32ul,
        "TSSessionId" / Int32ul,
        "Status" / Int32ul,
        "Reason" / Int32ul
    )

