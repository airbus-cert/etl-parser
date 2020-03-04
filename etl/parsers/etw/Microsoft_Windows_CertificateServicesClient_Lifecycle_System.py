# -*- coding: utf-8 -*-
"""
Microsoft-Windows-CertificateServicesClient-Lifecycle-System
GUID : bc0669e1-a10d-4a78-834e-1ca3c806c93b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("bc0669e1-a10d-4a78-834e-1ca3c806c93b"), event_id=1001, version=0)
class Microsoft_Windows_CertificateServicesClient_Lifecycle_System_1001_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("bc0669e1-a10d-4a78-834e-1ca3c806c93b"), event_id=1002, version=0)
class Microsoft_Windows_CertificateServicesClient_Lifecycle_System_1002_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("bc0669e1-a10d-4a78-834e-1ca3c806c93b"), event_id=1003, version=0)
class Microsoft_Windows_CertificateServicesClient_Lifecycle_System_1003_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("bc0669e1-a10d-4a78-834e-1ca3c806c93b"), event_id=1004, version=0)
class Microsoft_Windows_CertificateServicesClient_Lifecycle_System_1004_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("bc0669e1-a10d-4a78-834e-1ca3c806c93b"), event_id=1005, version=0)
class Microsoft_Windows_CertificateServicesClient_Lifecycle_System_1005_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("bc0669e1-a10d-4a78-834e-1ca3c806c93b"), event_id=1006, version=0)
class Microsoft_Windows_CertificateServicesClient_Lifecycle_System_1006_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("bc0669e1-a10d-4a78-834e-1ca3c806c93b"), event_id=1007, version=0)
class Microsoft_Windows_CertificateServicesClient_Lifecycle_System_1007_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("bc0669e1-a10d-4a78-834e-1ca3c806c93b"), event_id=1008, version=0)
class Microsoft_Windows_CertificateServicesClient_Lifecycle_System_1008_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("bc0669e1-a10d-4a78-834e-1ca3c806c93b"), event_id=1009, version=0)
class Microsoft_Windows_CertificateServicesClient_Lifecycle_System_1009_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("bc0669e1-a10d-4a78-834e-1ca3c806c93b"), event_id=1010, version=0)
class Microsoft_Windows_CertificateServicesClient_Lifecycle_System_1010_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )

