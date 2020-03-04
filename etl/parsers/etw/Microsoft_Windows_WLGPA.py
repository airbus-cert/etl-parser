# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WLGPA
GUID : 46098845-8a94-442d-9095-366a6bcfefa9
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("46098845-8a94-442d-9095-366a6bcfefa9"), event_id=14001, version=0)
class Microsoft_Windows_WLGPA_14001_0(Etw):
    pattern = Struct(
        "PolicyType" / Int32ul,
        "PolicyName" / WString,
        "PolicyNamePlaceholder" / Int32ul,
        "AutoConfigEnabled" / Int32ul,
        "ShowDeniednetworks" / Int32ul,
        "Profilesapplied" / WString,
        "Profilesappliedplaceholder" / Int32ul,
        "Profilesnotapplied" / WString,
        "Profilesnotappliedplaceholder" / Int32ul
    )


@declare(guid=guid("46098845-8a94-442d-9095-366a6bcfefa9"), event_id=14003, version=0)
class Microsoft_Windows_WLGPA_14003_0(Etw):
    pattern = Struct(
        "PolicyType" / Int32ul,
        "PolicyName" / WString,
        "PolicyNamePlaceholder" / WString,
        "ReasonCode" / Int32ul
    )

