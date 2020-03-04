# -*- coding: utf-8 -*-
"""
Microsoft-Windows-System-Restore
GUID : 126cdb97-d346-4894-8a34-658da5eea1b6
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("126cdb97-d346-4894-8a34-658da5eea1b6"), event_id=8300, version=0)
class Microsoft_Windows_System_Restore_8300_0(Etw):
    pattern = Struct(
        "SnapshotPath" / WString
    )


@declare(guid=guid("126cdb97-d346-4894-8a34-658da5eea1b6"), event_id=8301, version=0)
class Microsoft_Windows_System_Restore_8301_0(Etw):
    pattern = Struct(
        "SnapshotPath" / WString,
        "ErrorCode" / Int32ul,
        "TotalDirectories" / Int64ul,
        "TotalFiles" / Int64ul,
        "FilesScoped" / Int64ul,
        "FilesResident" / Int64ul,
        "FilesCachedFirstPass" / Int64ul,
        "FilesMissedSecondPass" / Int64ul
    )


@declare(guid=guid("126cdb97-d346-4894-8a34-658da5eea1b6"), event_id=8302, version=0)
class Microsoft_Windows_System_Restore_8302_0(Etw):
    pattern = Struct(
        "SnapshotPath" / WString,
        "ErrorCode" / Int32ul,
        "TotalDirectories" / Int64ul,
        "TotalFiles" / Int64ul,
        "FilesScoped" / Int64ul,
        "FilesResident" / Int64ul,
        "FilesCachedFirstPass" / Int64ul,
        "FilesMissedSecondPass" / Int64ul
    )


@declare(guid=guid("126cdb97-d346-4894-8a34-658da5eea1b6"), event_id=8303, version=0)
class Microsoft_Windows_System_Restore_8303_0(Etw):
    pattern = Struct(
        "SnapshotPath" / WString,
        "ErrorCode" / Int32ul,
        "TotalDirectories" / Int64ul,
        "TotalFiles" / Int64ul,
        "FilesScoped" / Int64ul,
        "FilesResident" / Int64ul,
        "FilesCachedFirstPass" / Int64ul,
        "FilesMissedSecondPass" / Int64ul
    )

