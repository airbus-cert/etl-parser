# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DriverFrameworks-UserMode-Performance
GUID : 9fa5dd5d-999e-466a-8ca9-7b3a66f8882f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9fa5dd5d-999e-466a-8ca9-7b3a66f8882f"), event_id=1, version=0)
class Microsoft_Windows_DriverFrameworks_UserMode_Performance_1_0(Etw):
    pattern = Struct(
        "Type" / Int8ul,
        "DrvPtr" / Int64ul,
        "DevPtr" / Int64ul
    )


@declare(guid=guid("9fa5dd5d-999e-466a-8ca9-7b3a66f8882f"), event_id=2, version=0)
class Microsoft_Windows_DriverFrameworks_UserMode_Performance_2_0(Etw):
    pattern = Struct(
        "Type" / Int8ul,
        "DrvPtr" / Int64ul,
        "DevPtr" / Int64ul
    )


@declare(guid=guid("9fa5dd5d-999e-466a-8ca9-7b3a66f8882f"), event_id=3, version=0)
class Microsoft_Windows_DriverFrameworks_UserMode_Performance_3_0(Etw):
    pattern = Struct(
        "DrvPtr" / Int64ul,
        "DevPtr" / Int64ul
    )


@declare(guid=guid("9fa5dd5d-999e-466a-8ca9-7b3a66f8882f"), event_id=4, version=0)
class Microsoft_Windows_DriverFrameworks_UserMode_Performance_4_0(Etw):
    pattern = Struct(
        "DrvPtr" / Int64ul,
        "DevPtr" / Int64ul
    )


@declare(guid=guid("9fa5dd5d-999e-466a-8ca9-7b3a66f8882f"), event_id=5, version=0)
class Microsoft_Windows_DriverFrameworks_UserMode_Performance_5_0(Etw):
    pattern = Struct(
        "DrvPtr" / Int64ul,
        "DevPtr" / Int64ul
    )


@declare(guid=guid("9fa5dd5d-999e-466a-8ca9-7b3a66f8882f"), event_id=6, version=0)
class Microsoft_Windows_DriverFrameworks_UserMode_Performance_6_0(Etw):
    pattern = Struct(
        "DrvPtr" / Int64ul,
        "DevPtr" / Int64ul
    )


@declare(guid=guid("9fa5dd5d-999e-466a-8ca9-7b3a66f8882f"), event_id=7, version=0)
class Microsoft_Windows_DriverFrameworks_UserMode_Performance_7_0(Etw):
    pattern = Struct(
        "DrvPtr" / Int64ul,
        "DevPtr" / Int64ul
    )


@declare(guid=guid("9fa5dd5d-999e-466a-8ca9-7b3a66f8882f"), event_id=8, version=0)
class Microsoft_Windows_DriverFrameworks_UserMode_Performance_8_0(Etw):
    pattern = Struct(
        "DrvPtr" / Int64ul,
        "DevPtr" / Int64ul
    )


@declare(guid=guid("9fa5dd5d-999e-466a-8ca9-7b3a66f8882f"), event_id=9, version=0)
class Microsoft_Windows_DriverFrameworks_UserMode_Performance_9_0(Etw):
    pattern = Struct(
        "DrvPtr" / Int64ul,
        "DevPtr" / Int64ul
    )


@declare(guid=guid("9fa5dd5d-999e-466a-8ca9-7b3a66f8882f"), event_id=10, version=0)
class Microsoft_Windows_DriverFrameworks_UserMode_Performance_10_0(Etw):
    pattern = Struct(
        "DrvPtr" / Int64ul,
        "DevPtr" / Int64ul
    )


@declare(guid=guid("9fa5dd5d-999e-466a-8ca9-7b3a66f8882f"), event_id=11, version=0)
class Microsoft_Windows_DriverFrameworks_UserMode_Performance_11_0(Etw):
    pattern = Struct(
        "DrvPtr" / Int64ul,
        "DevPtr" / Int64ul
    )


@declare(guid=guid("9fa5dd5d-999e-466a-8ca9-7b3a66f8882f"), event_id=12, version=0)
class Microsoft_Windows_DriverFrameworks_UserMode_Performance_12_0(Etw):
    pattern = Struct(
        "DrvPtr" / Int64ul,
        "DevPtr" / Int64ul
    )

