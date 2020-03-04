# -*- coding: utf-8 -*-
"""
Microsoft-Windows-IsolatedUserMode
GUID : 73a33ab2-1966-4999-8add-868c41415269
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("73a33ab2-1966-4999-8add-868c41415269"), event_id=1, version=0)
class Microsoft_Windows_IsolatedUserMode_1_0(Etw):
    pattern = Struct(
        "TrustletIdentity" / Int64ul,
        "NormalProcessId" / Int32ul,
        "Status" / Int32ul,
        "ImageName" / WString
    )


@declare(guid=guid("73a33ab2-1966-4999-8add-868c41415269"), event_id=2, version=0)
class Microsoft_Windows_IsolatedUserMode_2_0(Etw):
    pattern = Struct(
        "TrustletIdentity" / Int64ul,
        "NormalProcessId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("73a33ab2-1966-4999-8add-868c41415269"), event_id=3, version=0)
class Microsoft_Windows_IsolatedUserMode_3_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("73a33ab2-1966-4999-8add-868c41415269"), event_id=4, version=0)
class Microsoft_Windows_IsolatedUserMode_4_0(Etw):
    pattern = Struct(
        "TrustletIdentity" / Int64ul,
        "NormalProcessId" / Int32ul,
        "Status" / Int32ul
    )

