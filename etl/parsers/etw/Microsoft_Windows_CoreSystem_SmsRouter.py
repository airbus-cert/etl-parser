# -*- coding: utf-8 -*-
"""
Microsoft-Windows-CoreSystem-SmsRouter
GUID : a9c11050-9e93-4fa4-8fe0-7c4750a345b2
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a9c11050-9e93-4fa4-8fe0-7c4750a345b2"), event_id=102, version=0)
class Microsoft_Windows_CoreSystem_SmsRouter_102_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString,
        "LineNumber" / Int32ul,
        "HResultName" / Int32sl,
        "Context" / CString
    )


@declare(guid=guid("a9c11050-9e93-4fa4-8fe0-7c4750a345b2"), event_id=103, version=0)
class Microsoft_Windows_CoreSystem_SmsRouter_103_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString,
        "LineNumber" / Int32ul,
        "Context" / CString
    )


@declare(guid=guid("a9c11050-9e93-4fa4-8fe0-7c4750a345b2"), event_id=1022, version=0)
class Microsoft_Windows_CoreSystem_SmsRouter_1022_0(Etw):
    pattern = Struct(
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("a9c11050-9e93-4fa4-8fe0-7c4750a345b2"), event_id=1023, version=0)
class Microsoft_Windows_CoreSystem_SmsRouter_1023_0(Etw):
    pattern = Struct(
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("a9c11050-9e93-4fa4-8fe0-7c4750a345b2"), event_id=1024, version=0)
class Microsoft_Windows_CoreSystem_SmsRouter_1024_0(Etw):
    pattern = Struct(
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("a9c11050-9e93-4fa4-8fe0-7c4750a345b2"), event_id=1025, version=0)
class Microsoft_Windows_CoreSystem_SmsRouter_1025_0(Etw):
    pattern = Struct(
        "error" / Int32ul,
        "hresult" / Int32sl
    )

