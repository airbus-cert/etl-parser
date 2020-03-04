# -*- coding: utf-8 -*-
"""
Microsoft-Windows-UxInit
GUID : 4154a29c-40d9-445f-8d65-24da473e8f65
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4154a29c-40d9-445f-8d65-24da473e8f65"), event_id=1, version=0)
class Microsoft_Windows_UxInit_1_0(Etw):
    pattern = Struct(
        "CacheFileName" / WString
    )


@declare(guid=guid("4154a29c-40d9-445f-8d65-24da473e8f65"), event_id=3, version=0)
class Microsoft_Windows_UxInit_3_0(Etw):
    pattern = Struct(
        "hr" / Int32sl
    )


@declare(guid=guid("4154a29c-40d9-445f-8d65-24da473e8f65"), event_id=5, version=0)
class Microsoft_Windows_UxInit_5_0(Etw):
    pattern = Struct(
        "hr" / Int32sl
    )


@declare(guid=guid("4154a29c-40d9-445f-8d65-24da473e8f65"), event_id=6, version=0)
class Microsoft_Windows_UxInit_6_0(Etw):
    pattern = Struct(
        "monitorConfig" / Int32sl,
        "fPolicyCheckOnly" / Int8ul
    )


@declare(guid=guid("4154a29c-40d9-445f-8d65-24da473e8f65"), event_id=7, version=0)
class Microsoft_Windows_UxInit_7_0(Etw):
    pattern = Struct(
        "monitorConfig" / Int32sl,
        "fPolicyCheckOnly" / Int8ul
    )


@declare(guid=guid("4154a29c-40d9-445f-8d65-24da473e8f65"), event_id=8, version=0)
class Microsoft_Windows_UxInit_8_0(Etw):
    pattern = Struct(
        "monitorConfig" / Int32sl,
        "systemDpi" / Int32sl,
        "IsHighContrastMode" / Int8ul,
        "hr" / Int32sl
    )


@declare(guid=guid("4154a29c-40d9-445f-8d65-24da473e8f65"), event_id=9, version=0)
class Microsoft_Windows_UxInit_9_0(Etw):
    pattern = Struct(
        "monitorConfig" / Int32sl,
        "systemDpi" / Int32sl,
        "IsHighContrastMode" / Int8ul,
        "hr" / Int32sl
    )


@declare(guid=guid("4154a29c-40d9-445f-8d65-24da473e8f65"), event_id=10, version=0)
class Microsoft_Windows_UxInit_10_0(Etw):
    pattern = Struct(
        "monitorConfig" / Int32sl,
        "systemDpi" / Int32sl,
        "IsHighContrastMode" / Int8ul,
        "hr" / Int32sl
    )

