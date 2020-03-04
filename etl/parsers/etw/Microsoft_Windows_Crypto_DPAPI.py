# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Crypto-DPAPI
GUID : 89fe8f40-cdce-464e-8217-15ef97d4c7c3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("89fe8f40-cdce-464e-8217-15ef97d4c7c3"), event_id=1, version=0)
class Microsoft_Windows_Crypto_DPAPI_1_0(Etw):
    pattern = Struct(
        "MasterKeyGUID" / Guid,
        "UserStorage" / WString
    )


@declare(guid=guid("89fe8f40-cdce-464e-8217-15ef97d4c7c3"), event_id=2, version=0)
class Microsoft_Windows_Crypto_DPAPI_2_0(Etw):
    pattern = Struct(
        "MasterKeyGUID" / WString,
        "UserStorage" / WString
    )


@declare(guid=guid("89fe8f40-cdce-464e-8217-15ef97d4c7c3"), event_id=3, version=0)
class Microsoft_Windows_Crypto_DPAPI_3_0(Etw):
    pattern = Struct(
        "MasterKeyGUID" / Guid,
        "Success" / Int8ul,
        "LastError" / Int32ul,
        "MasterKeyDisposition" / Int32ul
    )


@declare(guid=guid("89fe8f40-cdce-464e-8217-15ef97d4c7c3"), event_id=4, version=0)
class Microsoft_Windows_Crypto_DPAPI_4_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("89fe8f40-cdce-464e-8217-15ef97d4c7c3"), event_id=8193, version=0)
class Microsoft_Windows_Crypto_DPAPI_8193_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("89fe8f40-cdce-464e-8217-15ef97d4c7c3"), event_id=8194, version=0)
class Microsoft_Windows_Crypto_DPAPI_8194_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "Access" / Int32ul
    )


@declare(guid=guid("89fe8f40-cdce-464e-8217-15ef97d4c7c3"), event_id=8197, version=0)
class Microsoft_Windows_Crypto_DPAPI_8197_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "ReasonForFailure" / Int32ul
    )


@declare(guid=guid("89fe8f40-cdce-464e-8217-15ef97d4c7c3"), event_id=8198, version=0)
class Microsoft_Windows_Crypto_DPAPI_8198_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "ReasonForFailure" / Int32ul
    )


@declare(guid=guid("89fe8f40-cdce-464e-8217-15ef97d4c7c3"), event_id=8199, version=0)
class Microsoft_Windows_Crypto_DPAPI_8199_0(Etw):
    pattern = Struct(
        "CredKeyIdentifier" / Bytes(32),
        "UserName" / WString,
        "UserSid" / Sid
    )


@declare(guid=guid("89fe8f40-cdce-464e-8217-15ef97d4c7c3"), event_id=12289, version=0)
class Microsoft_Windows_Crypto_DPAPI_12289_0(Etw):
    pattern = Struct(
        "CredKeyIdentifier" / Bytes(32),
        "UserName" / WString,
        "UserSid" / Sid
    )

