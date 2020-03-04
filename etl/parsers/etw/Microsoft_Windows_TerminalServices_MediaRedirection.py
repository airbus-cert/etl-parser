# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TerminalServices-MediaRedirection
GUID : 3f7b2f99-b863-4045-ad05-f6afb62e7af1
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3f7b2f99-b863-4045-ad05-f6afb62e7af1"), event_id=1000, version=0)
class Microsoft_Windows_TerminalServices_MediaRedirection_1000_0(Etw):
    pattern = Struct(
        "UInt32_1" / Int32ul,
        "UInt32_2" / Int32ul,
        "UInt32_3" / Int32ul,
        "UInt32_4" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("3f7b2f99-b863-4045-ad05-f6afb62e7af1"), event_id=1001, version=0)
class Microsoft_Windows_TerminalServices_MediaRedirection_1001_0(Etw):
    pattern = Struct(
        "UInt32_1" / Int32ul,
        "UInt32_2" / Int32ul,
        "UInt32_3" / Int32ul,
        "UInt32_4" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("3f7b2f99-b863-4045-ad05-f6afb62e7af1"), event_id=1002, version=0)
class Microsoft_Windows_TerminalServices_MediaRedirection_1002_0(Etw):
    pattern = Struct(
        "Guid1" / Guid,
        "String1" / WString,
        "Guid2" / Guid,
        "String2" / WString,
        "UInt32_1" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("3f7b2f99-b863-4045-ad05-f6afb62e7af1"), event_id=1003, version=0)
class Microsoft_Windows_TerminalServices_MediaRedirection_1003_0(Etw):
    pattern = Struct(
        "Guid1" / Guid,
        "String1" / WString,
        "Guid2" / Guid,
        "String2" / WString,
        "UInt32_1" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("3f7b2f99-b863-4045-ad05-f6afb62e7af1"), event_id=1004, version=0)
class Microsoft_Windows_TerminalServices_MediaRedirection_1004_0(Etw):
    pattern = Struct(
        "Guid1" / Guid,
        "String1" / WString,
        "Guid2" / Guid,
        "String2" / WString,
        "UInt32_1" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("3f7b2f99-b863-4045-ad05-f6afb62e7af1"), event_id=1005, version=0)
class Microsoft_Windows_TerminalServices_MediaRedirection_1005_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "SessionID" / Int32ul
    )


@declare(guid=guid("3f7b2f99-b863-4045-ad05-f6afb62e7af1"), event_id=1006, version=0)
class Microsoft_Windows_TerminalServices_MediaRedirection_1006_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "SessionID" / Int32ul
    )


@declare(guid=guid("3f7b2f99-b863-4045-ad05-f6afb62e7af1"), event_id=1007, version=0)
class Microsoft_Windows_TerminalServices_MediaRedirection_1007_0(Etw):
    pattern = Struct(
        "SessionID" / Int32ul
    )


@declare(guid=guid("3f7b2f99-b863-4045-ad05-f6afb62e7af1"), event_id=1008, version=0)
class Microsoft_Windows_TerminalServices_MediaRedirection_1008_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "UInt32Parameter" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("3f7b2f99-b863-4045-ad05-f6afb62e7af1"), event_id=1009, version=0)
class Microsoft_Windows_TerminalServices_MediaRedirection_1009_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "UInt32Parameter" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("3f7b2f99-b863-4045-ad05-f6afb62e7af1"), event_id=1010, version=0)
class Microsoft_Windows_TerminalServices_MediaRedirection_1010_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "UInt32Parameter" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("3f7b2f99-b863-4045-ad05-f6afb62e7af1"), event_id=1011, version=0)
class Microsoft_Windows_TerminalServices_MediaRedirection_1011_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "UInt32Parameter" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("3f7b2f99-b863-4045-ad05-f6afb62e7af1"), event_id=1012, version=0)
class Microsoft_Windows_TerminalServices_MediaRedirection_1012_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "UInt32Parameter" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("3f7b2f99-b863-4045-ad05-f6afb62e7af1"), event_id=1013, version=0)
class Microsoft_Windows_TerminalServices_MediaRedirection_1013_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "UInt32Parameter" / Int32ul,
        "SessionID" / Int32ul
    )

