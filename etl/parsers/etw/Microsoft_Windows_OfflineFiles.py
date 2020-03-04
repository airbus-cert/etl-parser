# -*- coding: utf-8 -*-
"""
Microsoft-Windows-OfflineFiles
GUID : 95353826-4fbe-41d4-9c42-f521c6e86360
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=7, version=0)
class Microsoft_Windows_OfflineFiles_7_0(Etw):
    pattern = Struct(
        "Account" / WString,
        "Session" / Int32ul
    )


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=8, version=0)
class Microsoft_Windows_OfflineFiles_8_0(Etw):
    pattern = Struct(
        "Account" / WString,
        "Session" / Int32ul
    )


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=9, version=0)
class Microsoft_Windows_OfflineFiles_9_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=10, version=0)
class Microsoft_Windows_OfflineFiles_10_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=1000, version=0)
class Microsoft_Windows_OfflineFiles_1000_0(Etw):
    pattern = Struct(
        "Text" / WString
    )


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=1001, version=0)
class Microsoft_Windows_OfflineFiles_1001_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "ResultCode" / WString,
        "Result" / WString
    )


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=1003, version=0)
class Microsoft_Windows_OfflineFiles_1003_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "MinutesSinceLastSync" / Int32ul
    )


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=1004, version=0)
class Microsoft_Windows_OfflineFiles_1004_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "Latency" / Int64ul,
        "Bandwidth" / Int64ul
    )


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=1005, version=0)
class Microsoft_Windows_OfflineFiles_1005_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "Latency" / Int64ul
    )


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=1006, version=0)
class Microsoft_Windows_OfflineFiles_1006_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "FailedFileCount" / Int32ul
    )


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=1007, version=0)
class Microsoft_Windows_OfflineFiles_1007_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=1008, version=0)
class Microsoft_Windows_OfflineFiles_1008_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "FileName" / WString
    )


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=1009, version=0)
class Microsoft_Windows_OfflineFiles_1009_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=2000, version=0)
class Microsoft_Windows_OfflineFiles_2000_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "ServerIsDir" / Int8ul,
        "ClientDeleted" / Int8ul,
        "ServerChanged" / Int8ul,
        "ServerLastWriteTime" / Int64ul,
        "ServerChangeTime" / Int64ul,
        "ServerAttributes" / Int32ul,
        "ServerSize" / Int64ul,
        "SyncState" / Int32ul,
        "SyncStateText" / WString
    )


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=2001, version=0)
class Microsoft_Windows_OfflineFiles_2001_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "ClientIsDir" / Int8ul,
        "ClientChanged" / Int8ul,
        "ClientIsSparse" / Int8ul,
        "ClientCreatedOffline" / Int8ul,
        "ClientDeletedOffline" / Int8ul,
        "ClientLastWriteTime" / Int64ul,
        "ClientChangeTime" / Int64ul,
        "ClientAttributes" / Int32ul,
        "ClientSize" / Int64ul,
        "ServerDeleted" / Int8ul,
        "SyncState" / Int32ul,
        "SyncStateText" / WString
    )


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=2002, version=0)
class Microsoft_Windows_OfflineFiles_2002_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "ClientIsDir" / Int8ul,
        "ClientChanged" / Int8ul,
        "ClientIsSparse" / Int8ul,
        "ClientCreatedOffline" / Int8ul,
        "ClientLastWriteTime" / Int64ul,
        "ClientChangeTime" / Int64ul,
        "ClientAttributes" / Int32ul,
        "ClientSize" / Int64ul,
        "ServerIsDir" / Int8ul,
        "ServerChanged" / Int8ul,
        "ServerLastWriteTime" / Int64ul,
        "ServerChangeTime" / Int64ul,
        "ServerAttributes" / Int32ul,
        "ServerSize" / Int64ul,
        "SyncState" / Int32ul,
        "SyncStateText" / WString
    )


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=2003, version=0)
class Microsoft_Windows_OfflineFiles_2003_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "ClientIsDir" / Int8ul,
        "ClientChanged" / Int8ul,
        "ClientIsSparse" / Int8ul,
        "ClientCreatedOffline" / Int8ul,
        "ServerIsDir" / Int8ul,
        "ServerChanged" / Int8ul,
        "ServerLastWriteTime" / Int64ul,
        "ServerChangeTime" / Int64ul,
        "ServerAttributes" / Int32ul,
        "ServerSize" / Int64ul,
        "SyncState" / Int32ul,
        "SyncStateText" / WString
    )


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=2004, version=0)
class Microsoft_Windows_OfflineFiles_2004_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "ClientIsDir" / Int8ul,
        "ServerIsDir" / Int8ul,
        "ServerChanged" / Int8ul,
        "ServerLastWriteTime" / Int64ul,
        "ServerChangeTime" / Int64ul,
        "ServerAttributes" / Int32ul,
        "ServerSize" / Int64ul,
        "SyncState" / Int32ul,
        "SyncStateText" / WString
    )


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=2005, version=0)
class Microsoft_Windows_OfflineFiles_2005_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "Operation" / WString
    )


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=2006, version=0)
class Microsoft_Windows_OfflineFiles_2006_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "Operation" / WString,
        "ResultCode" / WString,
        "Result" / WString
    )


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=2010, version=0)
class Microsoft_Windows_OfflineFiles_2010_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("95353826-4fbe-41d4-9c42-f521c6e86360"), event_id=2011, version=0)
class Microsoft_Windows_OfflineFiles_2011_0(Etw):
    pattern = Struct(
        "SourcePath" / WString,
        "TargetPath" / WString
    )

