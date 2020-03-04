# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Security-IdentityListener
GUID : 3c6c422b-019b-4f48-b67b-f79a3fa8b4ed
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3c6c422b-019b-4f48-b67b-f79a3fa8b4ed"), event_id=0, version=0)
class Microsoft_Windows_Security_IdentityListener_0_0(Etw):
    pattern = Struct(
        "Number" / Int32ul
    )


@declare(guid=guid("3c6c422b-019b-4f48-b67b-f79a3fa8b4ed"), event_id=1, version=0)
class Microsoft_Windows_Security_IdentityListener_1_0(Etw):
    pattern = Struct(
        "LastError" / Int32ul
    )


@declare(guid=guid("3c6c422b-019b-4f48-b67b-f79a3fa8b4ed"), event_id=2, version=0)
class Microsoft_Windows_Security_IdentityListener_2_0(Etw):
    pattern = Struct(
        "Sid" / Sid
    )


@declare(guid=guid("3c6c422b-019b-4f48-b67b-f79a3fa8b4ed"), event_id=3, version=0)
class Microsoft_Windows_Security_IdentityListener_3_0(Etw):
    pattern = Struct(
        "Sid" / Sid
    )


@declare(guid=guid("3c6c422b-019b-4f48-b67b-f79a3fa8b4ed"), event_id=4, version=0)
class Microsoft_Windows_Security_IdentityListener_4_0(Etw):
    pattern = Struct(
        "Sid" / Sid
    )


@declare(guid=guid("3c6c422b-019b-4f48-b67b-f79a3fa8b4ed"), event_id=5, version=0)
class Microsoft_Windows_Security_IdentityListener_5_0(Etw):
    pattern = Struct(
        "Sid" / Sid
    )


@declare(guid=guid("3c6c422b-019b-4f48-b67b-f79a3fa8b4ed"), event_id=6, version=0)
class Microsoft_Windows_Security_IdentityListener_6_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("3c6c422b-019b-4f48-b67b-f79a3fa8b4ed"), event_id=7, version=0)
class Microsoft_Windows_Security_IdentityListener_7_0(Etw):
    pattern = Struct(
        "LastError" / Int32ul
    )


@declare(guid=guid("3c6c422b-019b-4f48-b67b-f79a3fa8b4ed"), event_id=8, version=0)
class Microsoft_Windows_Security_IdentityListener_8_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("3c6c422b-019b-4f48-b67b-f79a3fa8b4ed"), event_id=9, version=0)
class Microsoft_Windows_Security_IdentityListener_9_0(Etw):
    pattern = Struct(
        "RemoteMachineName" / WString,
        "Errorcode" / Int32ul
    )


@declare(guid=guid("3c6c422b-019b-4f48-b67b-f79a3fa8b4ed"), event_id=10, version=0)
class Microsoft_Windows_Security_IdentityListener_10_0(Etw):
    pattern = Struct(
        "ProviderGUID" / Guid,
        "IdentityUID" / WString,
        "IdentityDisplayName" / WString
    )


@declare(guid=guid("3c6c422b-019b-4f48-b67b-f79a3fa8b4ed"), event_id=11, version=0)
class Microsoft_Windows_Security_IdentityListener_11_0(Etw):
    pattern = Struct(
        "LastError" / Int32ul
    )


@declare(guid=guid("3c6c422b-019b-4f48-b67b-f79a3fa8b4ed"), event_id=13, version=0)
class Microsoft_Windows_Security_IdentityListener_13_0(Etw):
    pattern = Struct(
        "LastError" / Int32ul
    )


@declare(guid=guid("3c6c422b-019b-4f48-b67b-f79a3fa8b4ed"), event_id=14, version=0)
class Microsoft_Windows_Security_IdentityListener_14_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("3c6c422b-019b-4f48-b67b-f79a3fa8b4ed"), event_id=15, version=0)
class Microsoft_Windows_Security_IdentityListener_15_0(Etw):
    pattern = Struct(
        "RemoteMachineName" / WString,
        "Errorcode" / Int32ul
    )

