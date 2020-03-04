# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SetupCl
GUID : 75ebc33e-d017-4d0f-93ab-0b4f86579164
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("75ebc33e-d017-4d0f-93ab-0b4f86579164"), event_id=1, version=0)
class Microsoft_Windows_SetupCl_1_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Description" / WString,
        "Statistic" / Int64ul
    )


@declare(guid=guid("75ebc33e-d017-4d0f-93ab-0b4f86579164"), event_id=2, version=0)
class Microsoft_Windows_SetupCl_2_0(Etw):
    pattern = Struct(
        "SourceLine" / Int32ul,
        "SourceFunction" / CString,
        "Message" / CString
    )


@declare(guid=guid("75ebc33e-d017-4d0f-93ab-0b4f86579164"), event_id=3, version=0)
class Microsoft_Windows_SetupCl_3_0(Etw):
    pattern = Struct(
        "SourceLine" / Int32ul,
        "SourceFunction" / CString,
        "Message" / CString
    )


@declare(guid=guid("75ebc33e-d017-4d0f-93ab-0b4f86579164"), event_id=12, version=0)
class Microsoft_Windows_SetupCl_12_0(Etw):
    pattern = Struct(
        "HiveName" / WString
    )


@declare(guid=guid("75ebc33e-d017-4d0f-93ab-0b4f86579164"), event_id=13, version=0)
class Microsoft_Windows_SetupCl_13_0(Etw):
    pattern = Struct(
        "HiveName" / WString
    )


@declare(guid=guid("75ebc33e-d017-4d0f-93ab-0b4f86579164"), event_id=16, version=0)
class Microsoft_Windows_SetupCl_16_0(Etw):
    pattern = Struct(
        "SID" / Sid
    )


@declare(guid=guid("75ebc33e-d017-4d0f-93ab-0b4f86579164"), event_id=17, version=0)
class Microsoft_Windows_SetupCl_17_0(Etw):
    pattern = Struct(
        "SID" / Sid
    )


@declare(guid=guid("75ebc33e-d017-4d0f-93ab-0b4f86579164"), event_id=18, version=0)
class Microsoft_Windows_SetupCl_18_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("75ebc33e-d017-4d0f-93ab-0b4f86579164"), event_id=19, version=0)
class Microsoft_Windows_SetupCl_19_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("75ebc33e-d017-4d0f-93ab-0b4f86579164"), event_id=22, version=0)
class Microsoft_Windows_SetupCl_22_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("75ebc33e-d017-4d0f-93ab-0b4f86579164"), event_id=25, version=0)
class Microsoft_Windows_SetupCl_25_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("75ebc33e-d017-4d0f-93ab-0b4f86579164"), event_id=26, version=0)
class Microsoft_Windows_SetupCl_26_0(Etw):
    pattern = Struct(
        "SourceLine" / Int32ul,
        "SourceFunction" / CString,
        "Message" / CString
    )

