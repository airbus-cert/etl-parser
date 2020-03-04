# -*- coding: utf-8 -*-
"""
Microsoft-Windows-RasSstp
GUID : 6c260f2c-049a-43d8-bf4d-d350a4e6611a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=1, version=0)
class Microsoft_Windows_RasSstp_1_0(Etw):
    pattern = Struct(
        "CoId" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=2, version=0)
class Microsoft_Windows_RasSstp_2_0(Etw):
    pattern = Struct(
        "CoId" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=3, version=0)
class Microsoft_Windows_RasSstp_3_0(Etw):
    pattern = Struct(
        "CoId" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=4, version=0)
class Microsoft_Windows_RasSstp_4_0(Etw):
    pattern = Struct(
        "CoId" / WString,
        "HTTPResponseCode" / WString
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=5, version=0)
class Microsoft_Windows_RasSstp_5_0(Etw):
    pattern = Struct(
        "CoId" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=6, version=0)
class Microsoft_Windows_RasSstp_6_0(Etw):
    pattern = Struct(
        "CoId" / WString,
        "SHA1CertificateHash" / WString,
        "SHA256CertificateHash" / WString
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=7, version=0)
class Microsoft_Windows_RasSstp_7_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=8, version=0)
class Microsoft_Windows_RasSstp_8_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=9, version=0)
class Microsoft_Windows_RasSstp_9_0(Etw):
    pattern = Struct(
        "Url" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=10, version=0)
class Microsoft_Windows_RasSstp_10_0(Etw):
    pattern = Struct(
        "Url" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=12, version=0)
class Microsoft_Windows_RasSstp_12_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString,
        "CertificateName" / WString
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=13, version=0)
class Microsoft_Windows_RasSstp_13_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString,
        "CertificateName" / WString
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=14, version=0)
class Microsoft_Windows_RasSstp_14_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=15, version=0)
class Microsoft_Windows_RasSstp_15_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=16, version=0)
class Microsoft_Windows_RasSstp_16_0(Etw):
    pattern = Struct(
        "CoId" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=17, version=0)
class Microsoft_Windows_RasSstp_17_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=18, version=0)
class Microsoft_Windows_RasSstp_18_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=19, version=0)
class Microsoft_Windows_RasSstp_19_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=20, version=0)
class Microsoft_Windows_RasSstp_20_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=21, version=0)
class Microsoft_Windows_RasSstp_21_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=22, version=0)
class Microsoft_Windows_RasSstp_22_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=23, version=0)
class Microsoft_Windows_RasSstp_23_0(Etw):
    pattern = Struct(
        "CoId" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("6c260f2c-049a-43d8-bf4d-d350a4e6611a"), event_id=33, version=0)
class Microsoft_Windows_RasSstp_33_0(Etw):
    pattern = Struct(
        "CoId" / WString,
        "ErrorMessage" / WString
    )

