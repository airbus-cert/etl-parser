# -*- coding: utf-8 -*-
"""
Microsoft-Gaming-Services
GUID : bc1bdb57-71a2-581a-147b-e0b49474a2d4
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("bc1bdb57-71a2-581a-147b-e0b49474a2d4"), event_id=9001, version=0)
class Microsoft_Gaming_Services_9001_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("bc1bdb57-71a2-581a-147b-e0b49474a2d4"), event_id=9002, version=0)
class Microsoft_Gaming_Services_9002_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("bc1bdb57-71a2-581a-147b-e0b49474a2d4"), event_id=9003, version=0)
class Microsoft_Gaming_Services_9003_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("bc1bdb57-71a2-581a-147b-e0b49474a2d4"), event_id=9004, version=0)
class Microsoft_Gaming_Services_9004_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("bc1bdb57-71a2-581a-147b-e0b49474a2d4"), event_id=9005, version=0)
class Microsoft_Gaming_Services_9005_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("bc1bdb57-71a2-581a-147b-e0b49474a2d4"), event_id=9006, version=0)
class Microsoft_Gaming_Services_9006_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("bc1bdb57-71a2-581a-147b-e0b49474a2d4"), event_id=9007, version=0)
class Microsoft_Gaming_Services_9007_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("bc1bdb57-71a2-581a-147b-e0b49474a2d4"), event_id=9008, version=0)
class Microsoft_Gaming_Services_9008_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("bc1bdb57-71a2-581a-147b-e0b49474a2d4"), event_id=9009, version=0)
class Microsoft_Gaming_Services_9009_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("bc1bdb57-71a2-581a-147b-e0b49474a2d4"), event_id=9010, version=0)
class Microsoft_Gaming_Services_9010_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("bc1bdb57-71a2-581a-147b-e0b49474a2d4"), event_id=9011, version=0)
class Microsoft_Gaming_Services_9011_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("bc1bdb57-71a2-581a-147b-e0b49474a2d4"), event_id=9012, version=0)
class Microsoft_Gaming_Services_9012_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "ErrorCode" / Int32ul
    )

