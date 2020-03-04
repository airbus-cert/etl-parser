# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Graphics-Printing3D
GUID : be967569-e3c8-425b-ad0e-4f2c790b1848
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("be967569-e3c8-425b-ad0e-4f2c790b1848"), event_id=2, version=0)
class Microsoft_Windows_Graphics_Printing3D_2_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("be967569-e3c8-425b-ad0e-4f2c790b1848"), event_id=4, version=0)
class Microsoft_Windows_Graphics_Printing3D_4_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("be967569-e3c8-425b-ad0e-4f2c790b1848"), event_id=5, version=0)
class Microsoft_Windows_Graphics_Printing3D_5_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("be967569-e3c8-425b-ad0e-4f2c790b1848"), event_id=6, version=0)
class Microsoft_Windows_Graphics_Printing3D_6_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul,
        "Name" / WString
    )

