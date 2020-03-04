# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TPM-WMI
GUID : 7d5387b0-cbe0-11da-a94d-0800200c9a66
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7d5387b0-cbe0-11da-a94d-0800200c9a66"), event_id=514, version=0)
class Microsoft_Windows_TPM_WMI_514_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("7d5387b0-cbe0-11da-a94d-0800200c9a66"), event_id=517, version=0)
class Microsoft_Windows_TPM_WMI_517_0(Etw):
    pattern = Struct(
        "HResult" / Int32sl
    )


@declare(guid=guid("7d5387b0-cbe0-11da-a94d-0800200c9a66"), event_id=518, version=0)
class Microsoft_Windows_TPM_WMI_518_0(Etw):
    pattern = Struct(
        "HResult" / Int32sl
    )


@declare(guid=guid("7d5387b0-cbe0-11da-a94d-0800200c9a66"), event_id=519, version=0)
class Microsoft_Windows_TPM_WMI_519_0(Etw):
    pattern = Struct(
        "ClearReason" / WString
    )


@declare(guid=guid("7d5387b0-cbe0-11da-a94d-0800200c9a66"), event_id=769, version=0)
class Microsoft_Windows_TPM_WMI_769_0(Etw):
    pattern = Struct(
        "OldOSManagedAuthLevel" / Int32ul,
        "NewOSManagedAuthLevel" / Int32ul
    )


@declare(guid=guid("7d5387b0-cbe0-11da-a94d-0800200c9a66"), event_id=1026, version=0)
class Microsoft_Windows_TPM_WMI_1026_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl,
        "StatusInformation" / Int32ul
    )


@declare(guid=guid("7d5387b0-cbe0-11da-a94d-0800200c9a66"), event_id=1029, version=0)
class Microsoft_Windows_TPM_WMI_1029_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("7d5387b0-cbe0-11da-a94d-0800200c9a66"), event_id=1031, version=0)
class Microsoft_Windows_TPM_WMI_1031_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("7d5387b0-cbe0-11da-a94d-0800200c9a66"), event_id=1537, version=0)
class Microsoft_Windows_TPM_WMI_1537_0(Etw):
    pattern = Struct(
        "HealthAttestationServer" / WString
    )


@declare(guid=guid("7d5387b0-cbe0-11da-a94d-0800200c9a66"), event_id=1538, version=0)
class Microsoft_Windows_TPM_WMI_1538_0(Etw):
    pattern = Struct(
        "HealthAttestationServer" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("7d5387b0-cbe0-11da-a94d-0800200c9a66"), event_id=1539, version=0)
class Microsoft_Windows_TPM_WMI_1539_0(Etw):
    pattern = Struct(
        "HealthAttestationServer" / WString,
        "HTTPStatus" / Int32sl,
        "ServerResponse" / WString
    )

