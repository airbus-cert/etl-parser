# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MCCS-EngineShared
GUID : bf460fc6-45c5-4119-add3-e361a6e7d5ac
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("bf460fc6-45c5-4119-add3-e361a6e7d5ac"), event_id=1, version=0)
class Microsoft_Windows_MCCS_EngineShared_1_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("bf460fc6-45c5-4119-add3-e361a6e7d5ac"), event_id=2, version=0)
class Microsoft_Windows_MCCS_EngineShared_2_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("bf460fc6-45c5-4119-add3-e361a6e7d5ac"), event_id=3001, version=0)
class Microsoft_Windows_MCCS_EngineShared_3001_0(Etw):
    pattern = Struct(
        "Prop_UnicodeString" / WString
    )

