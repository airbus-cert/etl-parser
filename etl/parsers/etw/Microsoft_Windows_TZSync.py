# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TZSync
GUID : 3527cb55-1298-49d4-ab94-1243db0fcaff
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3527cb55-1298-49d4-ab94-1243db0fcaff"), event_id=7, version=0)
class Microsoft_Windows_TZSync_7_0(Etw):
    pattern = Struct(
        "TimeZoneId" / WString
    )


@declare(guid=guid("3527cb55-1298-49d4-ab94-1243db0fcaff"), event_id=8, version=0)
class Microsoft_Windows_TZSync_8_0(Etw):
    pattern = Struct(
        "TimeZoneId" / WString
    )


@declare(guid=guid("3527cb55-1298-49d4-ab94-1243db0fcaff"), event_id=10, version=0)
class Microsoft_Windows_TZSync_10_0(Etw):
    pattern = Struct(
        "TimeZoneId" / WString
    )

