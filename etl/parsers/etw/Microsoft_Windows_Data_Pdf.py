# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Data-Pdf
GUID : b97561fe-b27a-4c48-aa3e-7d3addc105b1
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b97561fe-b27a-4c48-aa3e-7d3addc105b1"), event_id=1, version=0)
class Microsoft_Windows_Data_Pdf_1_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("b97561fe-b27a-4c48-aa3e-7d3addc105b1"), event_id=2, version=0)
class Microsoft_Windows_Data_Pdf_2_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("b97561fe-b27a-4c48-aa3e-7d3addc105b1"), event_id=5, version=0)
class Microsoft_Windows_Data_Pdf_5_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("b97561fe-b27a-4c48-aa3e-7d3addc105b1"), event_id=6, version=0)
class Microsoft_Windows_Data_Pdf_6_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("b97561fe-b27a-4c48-aa3e-7d3addc105b1"), event_id=7, version=0)
class Microsoft_Windows_Data_Pdf_7_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("b97561fe-b27a-4c48-aa3e-7d3addc105b1"), event_id=8, version=0)
class Microsoft_Windows_Data_Pdf_8_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )

