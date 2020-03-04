# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MCCS-AccountAccessor
GUID : 4025d192-273d-42ec-bdf8-940ec34eedca
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4025d192-273d-42ec-bdf8-940ec34eedca"), event_id=1, version=0)
class Microsoft_Windows_MCCS_AccountAccessor_1_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("4025d192-273d-42ec-bdf8-940ec34eedca"), event_id=2, version=0)
class Microsoft_Windows_MCCS_AccountAccessor_2_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("4025d192-273d-42ec-bdf8-940ec34eedca"), event_id=151, version=0)
class Microsoft_Windows_MCCS_AccountAccessor_151_0(Etw):
    pattern = Struct(
        "P1_Dword" / Int32ul,
        "P2_Boolean" / Int8ul
    )


@declare(guid=guid("4025d192-273d-42ec-bdf8-940ec34eedca"), event_id=201, version=0)
class Microsoft_Windows_MCCS_AccountAccessor_201_0(Etw):
    pattern = Struct(
        "P1_Dword" / Int32ul
    )


@declare(guid=guid("4025d192-273d-42ec-bdf8-940ec34eedca"), event_id=202, version=0)
class Microsoft_Windows_MCCS_AccountAccessor_202_0(Etw):
    pattern = Struct(
        "P1_Dword" / Int32ul
    )


@declare(guid=guid("4025d192-273d-42ec-bdf8-940ec34eedca"), event_id=221, version=0)
class Microsoft_Windows_MCCS_AccountAccessor_221_0(Etw):
    pattern = Struct(
        "P1_Dword" / Int32ul
    )

