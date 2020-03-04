# -*- coding: utf-8 -*-
"""
Microsoft-Windows-CertificateServicesClient-CredentialRoaming
GUID : 89a2278b-c662-4aff-a06c-46ad3f220bca
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("89a2278b-c662-4aff-a06c-46ad3f220bca"), event_id=1001, version=0)
class Microsoft_Windows_CertificateServicesClient_CredentialRoaming_1001_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("89a2278b-c662-4aff-a06c-46ad3f220bca"), event_id=1002, version=0)
class Microsoft_Windows_CertificateServicesClient_CredentialRoaming_1002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ErrorMsg" / WString
    )


@declare(guid=guid("89a2278b-c662-4aff-a06c-46ad3f220bca"), event_id=1003, version=0)
class Microsoft_Windows_CertificateServicesClient_CredentialRoaming_1003_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ErrorMsg" / WString
    )


@declare(guid=guid("89a2278b-c662-4aff-a06c-46ad3f220bca"), event_id=1004, version=0)
class Microsoft_Windows_CertificateServicesClient_CredentialRoaming_1004_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ErrorMsg" / WString
    )


@declare(guid=guid("89a2278b-c662-4aff-a06c-46ad3f220bca"), event_id=1005, version=0)
class Microsoft_Windows_CertificateServicesClient_CredentialRoaming_1005_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ErrorMsg" / WString
    )


@declare(guid=guid("89a2278b-c662-4aff-a06c-46ad3f220bca"), event_id=1006, version=0)
class Microsoft_Windows_CertificateServicesClient_CredentialRoaming_1006_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ErrorMsg" / WString
    )


@declare(guid=guid("89a2278b-c662-4aff-a06c-46ad3f220bca"), event_id=1007, version=0)
class Microsoft_Windows_CertificateServicesClient_CredentialRoaming_1007_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ErrorMsg" / WString
    )


@declare(guid=guid("89a2278b-c662-4aff-a06c-46ad3f220bca"), event_id=1010, version=0)
class Microsoft_Windows_CertificateServicesClient_CredentialRoaming_1010_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ErrorMsg" / WString
    )


@declare(guid=guid("89a2278b-c662-4aff-a06c-46ad3f220bca"), event_id=1012, version=0)
class Microsoft_Windows_CertificateServicesClient_CredentialRoaming_1012_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ErrorMsg" / WString
    )

