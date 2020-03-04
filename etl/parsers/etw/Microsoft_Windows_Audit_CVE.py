# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Audit-CVE
GUID : 85a62a0d-7e17-485f-9d4f-749a287193a6
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("85a62a0d-7e17-485f-9d4f-749a287193a6"), event_id=1, version=0)
class Microsoft_Windows_Audit_CVE_1_0(Etw):
    pattern = Struct(
        "CVEID" / WString,
        "AdditionalDetails" / WString
    )


@declare(guid=guid("85a62a0d-7e17-485f-9d4f-749a287193a6"), event_id=2, version=0)
class Microsoft_Windows_Audit_CVE_2_0(Etw):
    pattern = Struct(
        "CVEID" / WString,
        "AdditionalDetails" / WString
    )

