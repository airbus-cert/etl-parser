# -*- coding: utf-8 -*-
"""
Microsoft-Windows-AllJoyn
GUID : 2ed299d2-2f6b-411d-8d15-f4cc6fde0c70
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("2ed299d2-2f6b-411d-8d15-f4cc6fde0c70"), event_id=1, version=0)
class Microsoft_Windows_AllJoyn_1_0(Etw):
    pattern = Struct(
        "QStatus" / Int32ul,
        "Message" / CString,
        "Module" / CString,
        "File" / CString,
        "Line" / Int32ul
    )


@declare(guid=guid("2ed299d2-2f6b-411d-8d15-f4cc6fde0c70"), event_id=2, version=0)
class Microsoft_Windows_AllJoyn_2_0(Etw):
    pattern = Struct(
        "QStatus" / Int32ul,
        "Message" / CString,
        "Module" / CString,
        "File" / CString,
        "Line" / Int32ul
    )


@declare(guid=guid("2ed299d2-2f6b-411d-8d15-f4cc6fde0c70"), event_id=3, version=0)
class Microsoft_Windows_AllJoyn_3_0(Etw):
    pattern = Struct(
        "Message" / CString,
        "Module" / CString,
        "File" / CString,
        "Line" / Int32ul
    )


@declare(guid=guid("2ed299d2-2f6b-411d-8d15-f4cc6fde0c70"), event_id=4, version=0)
class Microsoft_Windows_AllJoyn_4_0(Etw):
    pattern = Struct(
        "Message" / CString,
        "Module" / CString,
        "File" / CString,
        "Line" / Int32ul
    )

