# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Magnification
GUID : c882ff1d-7585-4b33-b135-95c577179137
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c882ff1d-7585-4b33-b135-95c577179137"), event_id=1, version=0)
class Microsoft_Windows_Magnification_1_0(Etw):
    pattern = Struct(
        "hWndLensCtx" / Int64ul
    )


@declare(guid=guid("c882ff1d-7585-4b33-b135-95c577179137"), event_id=2, version=0)
class Microsoft_Windows_Magnification_2_0(Etw):
    pattern = Struct(
        "hWndLensCtx" / Int64ul
    )


@declare(guid=guid("c882ff1d-7585-4b33-b135-95c577179137"), event_id=3, version=0)
class Microsoft_Windows_Magnification_3_0(Etw):
    pattern = Struct(
        "hWndLensCtx" / Int64ul,
        "SrcRect" / CString
    )


@declare(guid=guid("c882ff1d-7585-4b33-b135-95c577179137"), event_id=4, version=0)
class Microsoft_Windows_Magnification_4_0(Etw):
    pattern = Struct(
        "hWndLensCtx" / Int64ul,
        "Transform" / CString
    )


@declare(guid=guid("c882ff1d-7585-4b33-b135-95c577179137"), event_id=5, version=0)
class Microsoft_Windows_Magnification_5_0(Etw):
    pattern = Struct(
        "hWndLensCtx" / Int64ul,
        "DesktopComposited" / Int32ul
    )


@declare(guid=guid("c882ff1d-7585-4b33-b135-95c577179137"), event_id=6, version=0)
class Microsoft_Windows_Magnification_6_0(Etw):
    pattern = Struct(
        "hWndLensCtx" / Int64ul,
        "DesktopComposited" / Int32ul
    )


@declare(guid=guid("c882ff1d-7585-4b33-b135-95c577179137"), event_id=7, version=0)
class Microsoft_Windows_Magnification_7_0(Etw):
    pattern = Struct(
        "hWndLensCtx" / Int64ul,
        "UpdateId" / Int64ul
    )


@declare(guid=guid("c882ff1d-7585-4b33-b135-95c577179137"), event_id=8, version=0)
class Microsoft_Windows_Magnification_8_0(Etw):
    pattern = Struct(
        "hWndLensCtx" / Int64ul,
        "UpdateId" / Int64ul
    )


@declare(guid=guid("c882ff1d-7585-4b33-b135-95c577179137"), event_id=9, version=0)
class Microsoft_Windows_Magnification_9_0(Etw):
    pattern = Struct(
        "hWndLensCtx" / Int64ul,
        "UpdateId" / Int64ul
    )


@declare(guid=guid("c882ff1d-7585-4b33-b135-95c577179137"), event_id=10, version=0)
class Microsoft_Windows_Magnification_10_0(Etw):
    pattern = Struct(
        "hWndLensCtx" / Int64ul,
        "UpdateId" / Int64ul
    )


@declare(guid=guid("c882ff1d-7585-4b33-b135-95c577179137"), event_id=11, version=0)
class Microsoft_Windows_Magnification_11_0(Etw):
    pattern = Struct(
        "hWndLensCtx" / Int64ul,
        "UpdateId" / Int64ul
    )


@declare(guid=guid("c882ff1d-7585-4b33-b135-95c577179137"), event_id=12, version=0)
class Microsoft_Windows_Magnification_12_0(Etw):
    pattern = Struct(
        "hWndLensCtx" / Int64ul,
        "UpdateId" / Int64ul
    )


@declare(guid=guid("c882ff1d-7585-4b33-b135-95c577179137"), event_id=13, version=0)
class Microsoft_Windows_Magnification_13_0(Etw):
    pattern = Struct(
        "hWndLensCtx" / Int64ul
    )


@declare(guid=guid("c882ff1d-7585-4b33-b135-95c577179137"), event_id=14, version=0)
class Microsoft_Windows_Magnification_14_0(Etw):
    pattern = Struct(
        "hWndLensCtx" / Int64ul
    )


@declare(guid=guid("c882ff1d-7585-4b33-b135-95c577179137"), event_id=15, version=0)
class Microsoft_Windows_Magnification_15_0(Etw):
    pattern = Struct(
        "hWndLensCtx" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("c882ff1d-7585-4b33-b135-95c577179137"), event_id=16, version=0)
class Microsoft_Windows_Magnification_16_0(Etw):
    pattern = Struct(
        "hWndLensCtx" / Int64ul
    )

