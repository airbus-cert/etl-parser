# -*- coding: utf-8 -*-
"""
Microsoft-Windows-HealthCenterCPL
GUID : 959f1fac-7ca8-4ed1-89dc-cdfa7e093cb0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("959f1fac-7ca8-4ed1-89dc-cdfa7e093cb0"), event_id=104, version=0)
class Microsoft_Windows_HealthCenterCPL_104_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("959f1fac-7ca8-4ed1-89dc-cdfa7e093cb0"), event_id=105, version=0)
class Microsoft_Windows_HealthCenterCPL_105_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("959f1fac-7ca8-4ed1-89dc-cdfa7e093cb0"), event_id=106, version=0)
class Microsoft_Windows_HealthCenterCPL_106_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("959f1fac-7ca8-4ed1-89dc-cdfa7e093cb0"), event_id=107, version=0)
class Microsoft_Windows_HealthCenterCPL_107_0(Etw):
    pattern = Struct(
        "psz" / WString
    )

