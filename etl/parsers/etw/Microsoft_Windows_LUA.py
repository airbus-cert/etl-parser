# -*- coding: utf-8 -*-
"""
Microsoft-Windows-LUA
GUID : 93c05d69-51a3-485e-877f-1806a8731346
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("93c05d69-51a3-485e-877f-1806a8731346"), event_id=15028, version=0)
class Microsoft_Windows_LUA_15028_0(Etw):
    pattern = Struct(
        "Parameters" / Int64ul
    )


@declare(guid=guid("93c05d69-51a3-485e-877f-1806a8731346"), event_id=16001, version=0)
class Microsoft_Windows_LUA_16001_0(Etw):
    pattern = Struct(
        "EventId" / Int32ul,
        "UACElevateFileID" / WString
    )


@declare(guid=guid("93c05d69-51a3-485e-877f-1806a8731346"), event_id=16002, version=0)
class Microsoft_Windows_LUA_16002_0(Etw):
    pattern = Struct(
        "EventId" / Int32ul,
        "UACElevateFileID" / WString
    )


@declare(guid=guid("93c05d69-51a3-485e-877f-1806a8731346"), event_id=16003, version=0)
class Microsoft_Windows_LUA_16003_0(Etw):
    pattern = Struct(
        "EventId" / Int32ul,
        "UACElevateFileID" / WString
    )


@declare(guid=guid("93c05d69-51a3-485e-877f-1806a8731346"), event_id=16004, version=0)
class Microsoft_Windows_LUA_16004_0(Etw):
    pattern = Struct(
        "EventId" / Int32ul,
        "UACElevateFileID" / WString
    )


@declare(guid=guid("93c05d69-51a3-485e-877f-1806a8731346"), event_id=16005, version=0)
class Microsoft_Windows_LUA_16005_0(Etw):
    pattern = Struct(
        "EventId" / Int32ul,
        "UACElevateFileID" / WString
    )


@declare(guid=guid("93c05d69-51a3-485e-877f-1806a8731346"), event_id=16006, version=0)
class Microsoft_Windows_LUA_16006_0(Etw):
    pattern = Struct(
        "EventId" / Int32ul,
        "UACElevateFileID" / WString
    )


@declare(guid=guid("93c05d69-51a3-485e-877f-1806a8731346"), event_id=16007, version=0)
class Microsoft_Windows_LUA_16007_0(Etw):
    pattern = Struct(
        "EventId" / Int32ul,
        "UACElevateFileID" / WString
    )


@declare(guid=guid("93c05d69-51a3-485e-877f-1806a8731346"), event_id=16008, version=0)
class Microsoft_Windows_LUA_16008_0(Etw):
    pattern = Struct(
        "EventId" / Int32ul,
        "UACElevateFileID" / WString
    )


@declare(guid=guid("93c05d69-51a3-485e-877f-1806a8731346"), event_id=16009, version=0)
class Microsoft_Windows_LUA_16009_0(Etw):
    pattern = Struct(
        "EventId" / Int32ul,
        "UACElevateFileID" / WString
    )


@declare(guid=guid("93c05d69-51a3-485e-877f-1806a8731346"), event_id=16010, version=0)
class Microsoft_Windows_LUA_16010_0(Etw):
    pattern = Struct(
        "EventId" / Int32ul,
        "UACElevateFileID" / WString
    )


@declare(guid=guid("93c05d69-51a3-485e-877f-1806a8731346"), event_id=16011, version=0)
class Microsoft_Windows_LUA_16011_0(Etw):
    pattern = Struct(
        "EventId" / Int32ul,
        "UACElevateFileID" / WString
    )

