# -*- coding: utf-8 -*-
"""
Microsoft-Windows-User-Loader
GUID : b059b83f-d946-4b13-87ca-4292839dc2f2
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b059b83f-d946-4b13-87ca-4292839dc2f2"), event_id=1, version=0)
class Microsoft_Windows_User_Loader_1_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("b059b83f-d946-4b13-87ca-4292839dc2f2"), event_id=2, version=0)
class Microsoft_Windows_User_Loader_2_0(Etw):
    pattern = Struct(
        "ProcessFileNamePathLength" / Int16ul,
        "ProcessFileNamePath" / Bytes(lambda this: this.ProcessFileNamePathLength)
    )


@declare(guid=guid("b059b83f-d946-4b13-87ca-4292839dc2f2"), event_id=3, version=0)
class Microsoft_Windows_User_Loader_3_0(Etw):
    pattern = Struct(
        "FailureReason" / Int32ul,
        "ImportDllName" / WString,
        "ProcessImagePath" / WString
    )


@declare(guid=guid("b059b83f-d946-4b13-87ca-4292839dc2f2"), event_id=4, version=0)
class Microsoft_Windows_User_Loader_4_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("b059b83f-d946-4b13-87ca-4292839dc2f2"), event_id=5, version=0)
class Microsoft_Windows_User_Loader_5_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "SuspendProcessRequest" / Int32ul,
        "DLLName" / WString
    )


@declare(guid=guid("b059b83f-d946-4b13-87ca-4292839dc2f2"), event_id=6, version=0)
class Microsoft_Windows_User_Loader_6_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("b059b83f-d946-4b13-87ca-4292839dc2f2"), event_id=7, version=0)
class Microsoft_Windows_User_Loader_7_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("b059b83f-d946-4b13-87ca-4292839dc2f2"), event_id=8, version=0)
class Microsoft_Windows_User_Loader_8_0(Etw):
    pattern = Struct(
        "FailureReason" / Int32ul,
        "ImportDllName" / WString,
        "ExportModule" / WString
    )


@declare(guid=guid("b059b83f-d946-4b13-87ca-4292839dc2f2"), event_id=9, version=0)
class Microsoft_Windows_User_Loader_9_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("b059b83f-d946-4b13-87ca-4292839dc2f2"), event_id=10, version=0)
class Microsoft_Windows_User_Loader_10_0(Etw):
    pattern = Struct(
        "FailureReason" / Int32ul,
        "ImportDllName" / WString,
        "ProcessImagePath" / WString
    )


@declare(guid=guid("b059b83f-d946-4b13-87ca-4292839dc2f2"), event_id=11, version=0)
class Microsoft_Windows_User_Loader_11_0(Etw):
    pattern = Struct(
        "ProcessImagePath" / WString,
        "CurDirDllPath" / WString,
        "FoundDllPath" / WString
    )


@declare(guid=guid("b059b83f-d946-4b13-87ca-4292839dc2f2"), event_id=12, version=0)
class Microsoft_Windows_User_Loader_12_0(Etw):
    pattern = Struct(
        "ProcessImagePath" / WString,
        "CurDirDllPath" / WString
    )

