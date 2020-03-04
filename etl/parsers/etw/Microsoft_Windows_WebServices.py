# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WebServices
GUID : e04fe2e0-c6cf-4273-b59d-5c97c9c374a4
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e04fe2e0-c6cf-4273-b59d-5c97c9c374a4"), event_id=1, version=0)
class Microsoft_Windows_WebServices_1_0(Etw):
    pattern = Struct(
        "api" / Int32ul
    )


@declare(guid=guid("e04fe2e0-c6cf-4273-b59d-5c97c9c374a4"), event_id=2, version=0)
class Microsoft_Windows_WebServices_2_0(Etw):
    pattern = Struct(
        "api" / Int32ul,
        "result" / Int32ul
    )


@declare(guid=guid("e04fe2e0-c6cf-4273-b59d-5c97c9c374a4"), event_id=3, version=0)
class Microsoft_Windows_WebServices_3_0(Etw):
    pattern = Struct(
        "api" / Int32ul,
        "result" / Int32ul
    )


@declare(guid=guid("e04fe2e0-c6cf-4273-b59d-5c97c9c374a4"), event_id=4, version=0)
class Microsoft_Windows_WebServices_4_0(Etw):
    pattern = Struct(
        "api" / Int32ul
    )


@declare(guid=guid("e04fe2e0-c6cf-4273-b59d-5c97c9c374a4"), event_id=5, version=0)
class Microsoft_Windows_WebServices_5_0(Etw):
    pattern = Struct(
        "api" / Int32ul,
        "result" / Int32ul
    )


@declare(guid=guid("e04fe2e0-c6cf-4273-b59d-5c97c9c374a4"), event_id=6, version=0)
class Microsoft_Windows_WebServices_6_0(Etw):
    pattern = Struct(
        "api" / Int32ul,
        "result" / Int32ul
    )


@declare(guid=guid("e04fe2e0-c6cf-4273-b59d-5c97c9c374a4"), event_id=7, version=0)
class Microsoft_Windows_WebServices_7_0(Etw):
    pattern = Struct(
        "error" / Int32ul,
        "errorString" / WString
    )


@declare(guid=guid("e04fe2e0-c6cf-4273-b59d-5c97c9c374a4"), event_id=8, version=0)
class Microsoft_Windows_WebServices_8_0(Etw):
    pattern = Struct(
        "operation" / Int32ul
    )


@declare(guid=guid("e04fe2e0-c6cf-4273-b59d-5c97c9c374a4"), event_id=9, version=0)
class Microsoft_Windows_WebServices_9_0(Etw):
    pattern = Struct(
        "operation" / Int32ul,
        "size" / Int32ul
    )


@declare(guid=guid("e04fe2e0-c6cf-4273-b59d-5c97c9c374a4"), event_id=10, version=0)
class Microsoft_Windows_WebServices_10_0(Etw):
    pattern = Struct(
        "operation" / Int32ul,
        "error" / Int32ul
    )


@declare(guid=guid("e04fe2e0-c6cf-4273-b59d-5c97c9c374a4"), event_id=11, version=0)
class Microsoft_Windows_WebServices_11_0(Etw):
    pattern = Struct(
        "correlationId" / Int64ul,
        "length" / Int16ul,
        "message" / Bytes(lambda this: this.length)
    )


@declare(guid=guid("e04fe2e0-c6cf-4273-b59d-5c97c9c374a4"), event_id=12, version=0)
class Microsoft_Windows_WebServices_12_0(Etw):
    pattern = Struct(
        "correlationId" / Int64ul,
        "length" / Int16ul,
        "message" / Bytes(lambda this: this.length)
    )


@declare(guid=guid("e04fe2e0-c6cf-4273-b59d-5c97c9c374a4"), event_id=13, version=0)
class Microsoft_Windows_WebServices_13_0(Etw):
    pattern = Struct(
        "correlationId" / Int64ul,
        "length" / Int16ul,
        "message" / Bytes(lambda this: this.length)
    )


@declare(guid=guid("e04fe2e0-c6cf-4273-b59d-5c97c9c374a4"), event_id=14, version=0)
class Microsoft_Windows_WebServices_14_0(Etw):
    pattern = Struct(
        "correlationId" / Int64ul,
        "length" / Int16ul,
        "message" / Bytes(lambda this: this.length)
    )


@declare(guid=guid("e04fe2e0-c6cf-4273-b59d-5c97c9c374a4"), event_id=15, version=0)
class Microsoft_Windows_WebServices_15_0(Etw):
    pattern = Struct(
        "correlationId" / Int64ul
    )


@declare(guid=guid("e04fe2e0-c6cf-4273-b59d-5c97c9c374a4"), event_id=16, version=0)
class Microsoft_Windows_WebServices_16_0(Etw):
    pattern = Struct(
        "correlationId" / Int64ul
    )


@declare(guid=guid("e04fe2e0-c6cf-4273-b59d-5c97c9c374a4"), event_id=17, version=0)
class Microsoft_Windows_WebServices_17_0(Etw):
    pattern = Struct(
        "correlationId" / Int64ul
    )


@declare(guid=guid("e04fe2e0-c6cf-4273-b59d-5c97c9c374a4"), event_id=18, version=0)
class Microsoft_Windows_WebServices_18_0(Etw):
    pattern = Struct(
        "correlationId" / Int64ul
    )


@declare(guid=guid("e04fe2e0-c6cf-4273-b59d-5c97c9c374a4"), event_id=19, version=0)
class Microsoft_Windows_WebServices_19_0(Etw):
    pattern = Struct(
        "length" / Int16ul,
        "traceString" / Bytes(lambda this: this.length)
    )


@declare(guid=guid("e04fe2e0-c6cf-4273-b59d-5c97c9c374a4"), event_id=20, version=0)
class Microsoft_Windows_WebServices_20_0(Etw):
    pattern = Struct(
        "length" / Int16ul,
        "traceString" / Bytes(lambda this: this.length)
    )


@declare(guid=guid("e04fe2e0-c6cf-4273-b59d-5c97c9c374a4"), event_id=21, version=0)
class Microsoft_Windows_WebServices_21_0(Etw):
    pattern = Struct(
        "traceString" / WString
    )

