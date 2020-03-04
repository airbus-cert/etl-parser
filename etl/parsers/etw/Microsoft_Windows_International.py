# -*- coding: utf-8 -*-
"""
Microsoft-Windows-International
GUID : 3aa52b8b-6357-4c18-a92e-b53fb177853b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=1001, version=0)
class Microsoft_Windows_International_1001_0(Etw):
    pattern = Struct(
        "RegistryKey" / WString,
        "ErrorCode" / Int32ul,
        "Message" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=1002, version=0)
class Microsoft_Windows_International_1002_0(Etw):
    pattern = Struct(
        "RegistryKey" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=1003, version=0)
class Microsoft_Windows_International_1003_0(Etw):
    pattern = Struct(
        "CodePage" / Int32ul,
        "FileName" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=1004, version=0)
class Microsoft_Windows_International_1004_0(Etw):
    pattern = Struct(
        "CodePage" / Int32ul,
        "FileName" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=1005, version=0)
class Microsoft_Windows_International_1005_0(Etw):
    pattern = Struct(
        "LocaleName" / WString,
        "WinDir" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=1006, version=0)
class Microsoft_Windows_International_1006_0(Etw):
    pattern = Struct(
        "LocaleName" / WString,
        "WinDir" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=1500, version=0)
class Microsoft_Windows_International_1500_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "ProdessName" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=1502, version=0)
class Microsoft_Windows_International_1502_0(Etw):
    pattern = Struct(
        "LocaleName" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=1503, version=0)
class Microsoft_Windows_International_1503_0(Etw):
    pattern = Struct(
        "LocaleName" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=2000, version=0)
class Microsoft_Windows_International_2000_0(Etw):
    pattern = Struct(
        "RegistryKey" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=3000, version=0)
class Microsoft_Windows_International_3000_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "ProdessName" / WString,
        "Locale" / Int32ul,
        "LCType" / Int32ul,
        "lpLCData" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=3001, version=0)
class Microsoft_Windows_International_3001_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "ProdessName" / WString,
        "Locale" / Int32ul,
        "Calendar" / Int32ul,
        "CalType" / Int32ul,
        "lpLCalData" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=3002, version=0)
class Microsoft_Windows_International_3002_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "ProdessName" / WString,
        "GeoId" / Int32ul
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=3003, version=0)
class Microsoft_Windows_International_3003_0(Etw):
    pattern = Struct(
        "LocaleName" / WString,
        "Flags" / Int32ul,
        "ProcessId" / Int32ul,
        "ProdessName" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=10000, version=0)
class Microsoft_Windows_International_10000_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "LineNumber" / Int32ul,
        "Reason" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=10003, version=0)
class Microsoft_Windows_International_10003_0(Etw):
    pattern = Struct(
        "LocaleName" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=10004, version=0)
class Microsoft_Windows_International_10004_0(Etw):
    pattern = Struct(
        "LocaleName" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=10005, version=0)
class Microsoft_Windows_International_10005_0(Etw):
    pattern = Struct(
        "AltSort" / WString,
        "Locale" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=10007, version=0)
class Microsoft_Windows_International_10007_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=10008, version=0)
class Microsoft_Windows_International_10008_0(Etw):
    pattern = Struct(
        "LocaleName" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=10009, version=0)
class Microsoft_Windows_International_10009_0(Etw):
    pattern = Struct(
        "Value" / Int32ul,
        "Win32ErrorCode" / Int32ul,
        "Win32ErrorMessage" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=10010, version=0)
class Microsoft_Windows_International_10010_0(Etw):
    pattern = Struct(
        "LocaleName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=10011, version=0)
class Microsoft_Windows_International_10011_0(Etw):
    pattern = Struct(
        "LocaleName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=10012, version=0)
class Microsoft_Windows_International_10012_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=10013, version=0)
class Microsoft_Windows_International_10013_0(Etw):
    pattern = Struct(
        "LCType" / WString,
        "Value" / WString,
        "Win32ErrorCode" / Int32ul,
        "Win32ErrorMessage" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=10014, version=0)
class Microsoft_Windows_International_10014_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=10015, version=0)
class Microsoft_Windows_International_10015_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=10111, version=0)
class Microsoft_Windows_International_10111_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=10221, version=0)
class Microsoft_Windows_International_10221_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=13000, version=0)
class Microsoft_Windows_International_13000_0(Etw):
    pattern = Struct(
        "LocaleName" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=13001, version=0)
class Microsoft_Windows_International_13001_0(Etw):
    pattern = Struct(
        "LocaleName" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=13002, version=0)
class Microsoft_Windows_International_13002_0(Etw):
    pattern = Struct(
        "LCType" / WString,
        "Value" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=13004, version=0)
class Microsoft_Windows_International_13004_0(Etw):
    pattern = Struct(
        "LocaleName" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=13005, version=0)
class Microsoft_Windows_International_13005_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=13006, version=0)
class Microsoft_Windows_International_13006_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=13007, version=0)
class Microsoft_Windows_International_13007_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=13008, version=0)
class Microsoft_Windows_International_13008_0(Etw):
    pattern = Struct(
        "LocaleName" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=13011, version=0)
class Microsoft_Windows_International_13011_0(Etw):
    pattern = Struct(
        "LocaleName" / WString
    )


@declare(guid=guid("3aa52b8b-6357-4c18-a92e-b53fb177853b"), event_id=13012, version=0)
class Microsoft_Windows_International_13012_0(Etw):
    pattern = Struct(
        "LocaleName" / WString
    )

