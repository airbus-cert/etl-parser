# -*- coding: utf-8 -*-
"""
Microsoft-Windows-CertificateServicesClient
GUID : 73370bd6-85e5-430b-b60a-fea1285808a7
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("73370bd6-85e5-430b-b60a-fea1285808a7"), event_id=501, version=0)
class Microsoft_Windows_CertificateServicesClient_501_0(Etw):
    pattern = Struct(
        "Parameter" / WString
    )


@declare(guid=guid("73370bd6-85e5-430b-b60a-fea1285808a7"), event_id=502, version=0)
class Microsoft_Windows_CertificateServicesClient_502_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("73370bd6-85e5-430b-b60a-fea1285808a7"), event_id=1001, version=0)
class Microsoft_Windows_CertificateServicesClient_1001_0(Etw):
    pattern = Struct(
        "ProviderName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("73370bd6-85e5-430b-b60a-fea1285808a7"), event_id=1002, version=0)
class Microsoft_Windows_CertificateServicesClient_1002_0(Etw):
    pattern = Struct(
        "ProviderName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("73370bd6-85e5-430b-b60a-fea1285808a7"), event_id=1003, version=0)
class Microsoft_Windows_CertificateServicesClient_1003_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("73370bd6-85e5-430b-b60a-fea1285808a7"), event_id=1004, version=0)
class Microsoft_Windows_CertificateServicesClient_1004_0(Etw):
    pattern = Struct(
        "ProviderName" / WString,
        "ErrorCode" / Int32ul
    )

