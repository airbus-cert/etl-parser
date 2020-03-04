# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Crypto-NCrypt
GUID : e8ed09dc-100c-45e2-9fc8-b53399ec1f70
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e8ed09dc-100c-45e2-9fc8-b53399ec1f70"), event_id=1, version=0)
class Microsoft_Windows_Crypto_NCrypt_1_0(Etw):
    pattern = Struct(
        "OperationType" / Int32ul,
        "ProviderName" / WString,
        "KeyName" / WString,
        "KeyType" / WString,
        "AlgorithmName" / WString,
        "Status" / Int32ul,
        "ProcessName" / WString
    )


@declare(guid=guid("e8ed09dc-100c-45e2-9fc8-b53399ec1f70"), event_id=2, version=0)
class Microsoft_Windows_Crypto_NCrypt_2_0(Etw):
    pattern = Struct(
        "ProviderName" / WString,
        "Status" / Int32ul,
        "ProcessName" / WString
    )


@declare(guid=guid("e8ed09dc-100c-45e2-9fc8-b53399ec1f70"), event_id=3, version=0)
class Microsoft_Windows_Crypto_NCrypt_3_0(Etw):
    pattern = Struct(
        "ProviderName" / WString,
        "KeyName" / WString,
        "Status" / Int32ul,
        "ProcessName" / WString
    )


@declare(guid=guid("e8ed09dc-100c-45e2-9fc8-b53399ec1f70"), event_id=4, version=0)
class Microsoft_Windows_Crypto_NCrypt_4_0(Etw):
    pattern = Struct(
        "ProviderName" / WString,
        "KeyName" / WString,
        "AlgorithmName" / WString,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessName" / WString
    )


@declare(guid=guid("e8ed09dc-100c-45e2-9fc8-b53399ec1f70"), event_id=5, version=0)
class Microsoft_Windows_Crypto_NCrypt_5_0(Etw):
    pattern = Struct(
        "ProtectorName" / WString,
        "ProtectorAttributes" / WString,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessName" / WString
    )


@declare(guid=guid("e8ed09dc-100c-45e2-9fc8-b53399ec1f70"), event_id=6, version=0)
class Microsoft_Windows_Crypto_NCrypt_6_0(Etw):
    pattern = Struct(
        "ProtectorName" / WString,
        "RecipientType" / Int32ul,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessName" / WString,
        "KeyIdLength" / Int32ul,
        "KeyId" / Bytes(lambda this: this.KeyIdLength)
    )


@declare(guid=guid("e8ed09dc-100c-45e2-9fc8-b53399ec1f70"), event_id=7, version=0)
class Microsoft_Windows_Crypto_NCrypt_7_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessName" / WString
    )


@declare(guid=guid("e8ed09dc-100c-45e2-9fc8-b53399ec1f70"), event_id=8, version=0)
class Microsoft_Windows_Crypto_NCrypt_8_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessName" / WString
    )

