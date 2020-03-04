# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WMPNSSUI
GUID : 7c314e58-8246-47d1-8f7a-4049dc543e0b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7c314e58-8246-47d1-8f7a-4049dc543e0b"), event_id=1009, version=0)
class Microsoft_Windows_WMPNSSUI_1009_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("7c314e58-8246-47d1-8f7a-4049dc543e0b"), event_id=1010, version=0)
class Microsoft_Windows_WMPNSSUI_1010_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("7c314e58-8246-47d1-8f7a-4049dc543e0b"), event_id=2001, version=0)
class Microsoft_Windows_WMPNSSUI_2001_0(Etw):
    pattern = Struct(
        "EnableDevice" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("7c314e58-8246-47d1-8f7a-4049dc543e0b"), event_id=2002, version=0)
class Microsoft_Windows_WMPNSSUI_2002_0(Etw):
    pattern = Struct(
        "EnableDevice" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("7c314e58-8246-47d1-8f7a-4049dc543e0b"), event_id=2003, version=0)
class Microsoft_Windows_WMPNSSUI_2003_0(Etw):
    pattern = Struct(
        "ShouldDisplayMenu" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("7c314e58-8246-47d1-8f7a-4049dc543e0b"), event_id=2004, version=0)
class Microsoft_Windows_WMPNSSUI_2004_0(Etw):
    pattern = Struct(
        "ShouldDisplayMenu" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("7c314e58-8246-47d1-8f7a-4049dc543e0b"), event_id=2005, version=0)
class Microsoft_Windows_WMPNSSUI_2005_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("7c314e58-8246-47d1-8f7a-4049dc543e0b"), event_id=2006, version=0)
class Microsoft_Windows_WMPNSSUI_2006_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("7c314e58-8246-47d1-8f7a-4049dc543e0b"), event_id=3001, version=0)
class Microsoft_Windows_WMPNSSUI_3001_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("7c314e58-8246-47d1-8f7a-4049dc543e0b"), event_id=3002, version=0)
class Microsoft_Windows_WMPNSSUI_3002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )

