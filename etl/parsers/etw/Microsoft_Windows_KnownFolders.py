# -*- coding: utf-8 -*-
"""
Microsoft-Windows-KnownFolders
GUID : 8939299f-2315-4c5c-9b91-abb86aa0627d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("8939299f-2315-4c5c-9b91-abb86aa0627d"), event_id=1000, version=0)
class Microsoft_Windows_KnownFolders_1000_0(Etw):
    pattern = Struct(
        "hrError" / Int32ul,
        "FolderId" / Guid,
        "Path" / WString
    )


@declare(guid=guid("8939299f-2315-4c5c-9b91-abb86aa0627d"), event_id=1001, version=0)
class Microsoft_Windows_KnownFolders_1001_0(Etw):
    pattern = Struct(
        "hrError" / Int32ul,
        "FolderId" / Guid,
        "Path" / WString
    )


@declare(guid=guid("8939299f-2315-4c5c-9b91-abb86aa0627d"), event_id=1002, version=0)
class Microsoft_Windows_KnownFolders_1002_0(Etw):
    pattern = Struct(
        "hrError" / Int32ul,
        "FolderId" / Guid,
        "Path" / WString
    )


@declare(guid=guid("8939299f-2315-4c5c-9b91-abb86aa0627d"), event_id=1003, version=0)
class Microsoft_Windows_KnownFolders_1003_0(Etw):
    pattern = Struct(
        "hrError" / Int32ul,
        "FolderId" / Guid,
        "Path" / WString
    )

