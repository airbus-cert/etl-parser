# -*- coding: utf-8 -*-
"""
Microsoft-Windows-CertificateServicesClient-AutoEnrollment
GUID : f0db7ef8-b6f3-4005-9937-feb77b9e1b43
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f0db7ef8-b6f3-4005-9937-feb77b9e1b43"), event_id=1, version=0)
class Microsoft_Windows_CertificateServicesClient_AutoEnrollment_1_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "StoreName" / WString,
        "LdapStore" / WString,
        "ErrorCode" / WString,
        "ErrorMsg" / WString
    )


@declare(guid=guid("f0db7ef8-b6f3-4005-9937-feb77b9e1b43"), event_id=2, version=0)
class Microsoft_Windows_CertificateServicesClient_AutoEnrollment_2_0(Etw):
    pattern = Struct(
        "Context" / WString
    )


@declare(guid=guid("f0db7ef8-b6f3-4005-9937-feb77b9e1b43"), event_id=3, version=0)
class Microsoft_Windows_CertificateServicesClient_AutoEnrollment_3_0(Etw):
    pattern = Struct(
        "Context" / WString
    )


@declare(guid=guid("f0db7ef8-b6f3-4005-9937-feb77b9e1b43"), event_id=4, version=0)
class Microsoft_Windows_CertificateServicesClient_AutoEnrollment_4_0(Etw):
    pattern = Struct(
        "Context" / WString
    )


@declare(guid=guid("f0db7ef8-b6f3-4005-9937-feb77b9e1b43"), event_id=5, version=0)
class Microsoft_Windows_CertificateServicesClient_AutoEnrollment_5_0(Etw):
    pattern = Struct(
        "Context" / WString
    )


@declare(guid=guid("f0db7ef8-b6f3-4005-9937-feb77b9e1b43"), event_id=6, version=0)
class Microsoft_Windows_CertificateServicesClient_AutoEnrollment_6_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "ErrorCode" / WString,
        "ErrorMsg" / WString
    )


@declare(guid=guid("f0db7ef8-b6f3-4005-9937-feb77b9e1b43"), event_id=15, version=0)
class Microsoft_Windows_CertificateServicesClient_AutoEnrollment_15_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "ErrorCode" / WString,
        "ErrorMsg" / WString
    )


@declare(guid=guid("f0db7ef8-b6f3-4005-9937-feb77b9e1b43"), event_id=64, version=0)
class Microsoft_Windows_CertificateServicesClient_AutoEnrollment_64_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "ObjId" / WString
    )

