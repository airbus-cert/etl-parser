# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WinJson
GUID : 4637124c-1d40-4b4d-892f-2aaecf24ff06
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=0, version=0)
class Microsoft_Windows_WinJson_0_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=1, version=0)
class Microsoft_Windows_WinJson_1_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=2, version=0)
class Microsoft_Windows_WinJson_2_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=3, version=0)
class Microsoft_Windows_WinJson_3_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=4, version=0)
class Microsoft_Windows_WinJson_4_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=8, version=0)
class Microsoft_Windows_WinJson_8_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=9, version=0)
class Microsoft_Windows_WinJson_9_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=10, version=0)
class Microsoft_Windows_WinJson_10_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=11, version=0)
class Microsoft_Windows_WinJson_11_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=13, version=0)
class Microsoft_Windows_WinJson_13_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=14, version=0)
class Microsoft_Windows_WinJson_14_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=16, version=0)
class Microsoft_Windows_WinJson_16_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=17, version=0)
class Microsoft_Windows_WinJson_17_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=18, version=0)
class Microsoft_Windows_WinJson_18_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=19, version=0)
class Microsoft_Windows_WinJson_19_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=20, version=0)
class Microsoft_Windows_WinJson_20_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=21, version=0)
class Microsoft_Windows_WinJson_21_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=22, version=0)
class Microsoft_Windows_WinJson_22_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=28, version=0)
class Microsoft_Windows_WinJson_28_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=29, version=0)
class Microsoft_Windows_WinJson_29_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=30, version=0)
class Microsoft_Windows_WinJson_30_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=31, version=0)
class Microsoft_Windows_WinJson_31_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=32, version=0)
class Microsoft_Windows_WinJson_32_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=34, version=0)
class Microsoft_Windows_WinJson_34_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=35, version=0)
class Microsoft_Windows_WinJson_35_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=37, version=0)
class Microsoft_Windows_WinJson_37_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=39, version=0)
class Microsoft_Windows_WinJson_39_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4637124c-1d40-4b4d-892f-2aaecf24ff06"), event_id=99, version=0)
class Microsoft_Windows_WinJson_99_0(Etw):
    pattern = Struct(
        "szString" / CString
    )

