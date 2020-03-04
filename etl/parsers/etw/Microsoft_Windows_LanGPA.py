# -*- coding: utf-8 -*-
"""
Microsoft-Windows-LanGPA
GUID : cb070027-1534-4cf3-98ea-b9751f508376
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("cb070027-1534-4cf3-98ea-b9751f508376"), event_id=14001, version=0)
class Microsoft_Windows_LanGPA_14001_0(Etw):
    pattern = Struct(
        "PolicyType" / Int32ul,
        "PolicyName" / WString,
        "PolicyNamePlaceholder" / Int32ul,
        "AutoConfigEnabled" / Int32ul,
        "Profileapplied" / Int32ul,
        "ReasonCode" / Int32ul
    )


@declare(guid=guid("cb070027-1534-4cf3-98ea-b9751f508376"), event_id=14003, version=0)
class Microsoft_Windows_LanGPA_14003_0(Etw):
    pattern = Struct(
        "PolicyType" / Int32ul,
        "PolicyName" / WString,
        "PolicyNamePlaceholder" / WString,
        "ReasonCode" / Int32ul
    )

