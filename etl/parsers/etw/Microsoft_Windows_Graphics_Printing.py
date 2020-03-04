# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Graphics-Printing
GUID : e7aa32fb-77d0-477f-987d-7e83df1b7ed0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e7aa32fb-77d0-477f-987d-7e83df1b7ed0"), event_id=2, version=0)
class Microsoft_Windows_Graphics_Printing_2_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("e7aa32fb-77d0-477f-987d-7e83df1b7ed0"), event_id=4, version=0)
class Microsoft_Windows_Graphics_Printing_4_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("e7aa32fb-77d0-477f-987d-7e83df1b7ed0"), event_id=5, version=0)
class Microsoft_Windows_Graphics_Printing_5_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("e7aa32fb-77d0-477f-987d-7e83df1b7ed0"), event_id=6, version=0)
class Microsoft_Windows_Graphics_Printing_6_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul,
        "Name" / WString
    )

