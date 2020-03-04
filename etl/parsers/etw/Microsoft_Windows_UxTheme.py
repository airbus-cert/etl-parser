# -*- coding: utf-8 -*-
"""
Microsoft-Windows-UxTheme
GUID : 422088e6-cd0c-4f99-bd0b-6985fa290bdf
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("422088e6-cd0c-4f99-bd0b-6985fa290bdf"), event_id=3, version=0)
class Microsoft_Windows_UxTheme_3_0(Etw):
    pattern = Struct(
        "PartId" / Int32sl,
        "StateId" / Int32sl
    )


@declare(guid=guid("422088e6-cd0c-4f99-bd0b-6985fa290bdf"), event_id=6, version=0)
class Microsoft_Windows_UxTheme_6_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("422088e6-cd0c-4f99-bd0b-6985fa290bdf"), event_id=17, version=0)
class Microsoft_Windows_UxTheme_17_0(Etw):
    pattern = Struct(
        "X" / Int16sl,
        "Y" / Int16sl
    )


@declare(guid=guid("422088e6-cd0c-4f99-bd0b-6985fa290bdf"), event_id=19, version=0)
class Microsoft_Windows_UxTheme_19_0(Etw):
    pattern = Struct(
        "DeltaTime" / Double
    )


@declare(guid=guid("422088e6-cd0c-4f99-bd0b-6985fa290bdf"), event_id=21, version=0)
class Microsoft_Windows_UxTheme_21_0(Etw):
    pattern = Struct(
        "ProcessName" / WString
    )


@declare(guid=guid("422088e6-cd0c-4f99-bd0b-6985fa290bdf"), event_id=25, version=0)
class Microsoft_Windows_UxTheme_25_0(Etw):
    pattern = Struct(
        "ApiNumber" / Int64sl,
        "ClientSessionId" / Int32sl,
        "status" / Int32ul
    )


@declare(guid=guid("422088e6-cd0c-4f99-bd0b-6985fa290bdf"), event_id=27, version=0)
class Microsoft_Windows_UxTheme_27_0(Etw):
    pattern = Struct(
        "ClientSessionId" / Int32sl,
        "status" / Int32ul
    )


@declare(guid=guid("422088e6-cd0c-4f99-bd0b-6985fa290bdf"), event_id=29, version=0)
class Microsoft_Windows_UxTheme_29_0(Etw):
    pattern = Struct(
        "ApiNumber" / Int64sl,
        "ClientSessionId" / Int32sl,
        "status" / Int32ul
    )


@declare(guid=guid("422088e6-cd0c-4f99-bd0b-6985fa290bdf"), event_id=31, version=0)
class Microsoft_Windows_UxTheme_31_0(Etw):
    pattern = Struct(
        "status" / Int32ul
    )


@declare(guid=guid("422088e6-cd0c-4f99-bd0b-6985fa290bdf"), event_id=33, version=0)
class Microsoft_Windows_UxTheme_33_0(Etw):
    pattern = Struct(
        "fRequestPending" / Int8ul,
        "status" / Int32ul
    )


@declare(guid=guid("422088e6-cd0c-4f99-bd0b-6985fa290bdf"), event_id=34, version=0)
class Microsoft_Windows_UxTheme_34_0(Etw):
    pattern = Struct(
        "status" / Int32ul
    )


@declare(guid=guid("422088e6-cd0c-4f99-bd0b-6985fa290bdf"), event_id=35, version=0)
class Microsoft_Windows_UxTheme_35_0(Etw):
    pattern = Struct(
        "fConnectionClosed" / Int8ul
    )


@declare(guid=guid("422088e6-cd0c-4f99-bd0b-6985fa290bdf"), event_id=36, version=0)
class Microsoft_Windows_UxTheme_36_0(Etw):
    pattern = Struct(
        "status" / Int32ul
    )


@declare(guid=guid("422088e6-cd0c-4f99-bd0b-6985fa290bdf"), event_id=37, version=0)
class Microsoft_Windows_UxTheme_37_0(Etw):
    pattern = Struct(
        "fConnectionClosed" / Int8ul
    )


@declare(guid=guid("422088e6-cd0c-4f99-bd0b-6985fa290bdf"), event_id=40, version=0)
class Microsoft_Windows_UxTheme_40_0(Etw):
    pattern = Struct(
        "HangingThreadId" / Int32sl,
        "TimeoutUsed" / Int32sl
    )

