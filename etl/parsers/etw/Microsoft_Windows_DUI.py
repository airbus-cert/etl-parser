# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DUI
GUID : 8360bd0f-a7dc-4391-91a7-a457c5c381e4
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=46, version=0)
class Microsoft_Windows_DUI_46_0(Etw):
    pattern = Struct(
        "loops" / Int32ul,
        "cGC" / Int32ul,
        "cGCLP" / Int32ul
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=48, version=0)
class Microsoft_Windows_DUI_48_0(Etw):
    pattern = Struct(
        "cPC" / Int32ul
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=66, version=0)
class Microsoft_Windows_DUI_66_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "type" / Int32ul
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=69, version=0)
class Microsoft_Windows_DUI_69_0(Etw):
    pattern = Struct(
        "type" / Int32ul,
        "target" / Int32ul,
        "atomname" / WString
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=70, version=0)
class Microsoft_Windows_DUI_70_0(Etw):
    pattern = Struct(
        "type" / Int32ul,
        "target" / Int32ul,
        "atomname" / WString
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=74, version=0)
class Microsoft_Windows_DUI_74_0(Etw):
    pattern = Struct(
        "atomname" / WString,
        "hGadChange" / Int32ul,
        "hGadClone" / Int32ul,
        "flDelay" / Float32l,
        "flDuration" / Float32l,
        "zOrder" / Int32sl,
        "nProperty" / Int32ul,
        "nFlags" / Int32ul,
        "flInitScalar" / Float32l,
        "flInitX" / Float32l,
        "flInitY" / Float32l,
        "flInitZ" / Float32l,
        "flInitOriginX" / Float32l,
        "flInitOriginY" / Float32l,
        "flInitOriginZ" / Float32l
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=75, version=0)
class Microsoft_Windows_DUI_75_0(Etw):
    pattern = Struct(
        "state" / Int32ul
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=76, version=0)
class Microsoft_Windows_DUI_76_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "type" / Int32ul,
        "dwCookie" / Int32ul,
        "nCode" / Int32ul
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=78, version=0)
class Microsoft_Windows_DUI_78_0(Etw):
    pattern = Struct(
        "FrameTime" / Int64ul
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=80, version=0)
class Microsoft_Windows_DUI_80_0(Etw):
    pattern = Struct(
        "FrameTime" / Int64ul,
        "DotsPainted" / Int32ul
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=81, version=0)
class Microsoft_Windows_DUI_81_0(Etw):
    pattern = Struct(
        "width" / Int32ul,
        "height" / Int32ul
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=82, version=0)
class Microsoft_Windows_DUI_82_0(Etw):
    pattern = Struct(
        "percent" / Int32ul
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=83, version=0)
class Microsoft_Windows_DUI_83_0(Etw):
    pattern = Struct(
        "flRadius" / Float32l
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=84, version=0)
class Microsoft_Windows_DUI_84_0(Etw):
    pattern = Struct(
        "ForegroundColor" / Int32ul
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=87, version=0)
class Microsoft_Windows_DUI_87_0(Etw):
    pattern = Struct(
        "PreviousState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=88, version=0)
class Microsoft_Windows_DUI_88_0(Etw):
    pattern = Struct(
        "PreviousState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=89, version=0)
class Microsoft_Windows_DUI_89_0(Etw):
    pattern = Struct(
        "atomname" / WString,
        "hGadChange" / Int32ul,
        "flEndScalar" / Float32l,
        "flEndX" / Float32l,
        "flEndY" / Float32l,
        "flEndZ" / Float32l,
        "flEndOriginX" / Float32l,
        "flEndOriginY" / Float32l,
        "flEndOriginZ" / Float32l,
        "flCurveX1" / Float32l,
        "flCurveY1" / Float32l,
        "flCurveX2" / Float32l,
        "flCurveY2" / Float32l,
        "fTransitionCancelled" / Int8ul
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=90, version=0)
class Microsoft_Windows_DUI_90_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "type" / Int32ul
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=93, version=0)
class Microsoft_Windows_DUI_93_0(Etw):
    pattern = Struct(
        "ForegroundColor" / Int32ul
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=94, version=0)
class Microsoft_Windows_DUI_94_0(Etw):
    pattern = Struct(
        "BackgroundColor" / Int32ul
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=95, version=0)
class Microsoft_Windows_DUI_95_0(Etw):
    pattern = Struct(
        "PreviousState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=117, version=0)
class Microsoft_Windows_DUI_117_0(Etw):
    pattern = Struct(
        "hr" / Int32sl,
        "fNew" / Int8ul,
        "cUses" / Int32ul,
        "szModule" / WString,
        "szResource" / WString,
        "szSheet" / WString
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=121, version=0)
class Microsoft_Windows_DUI_121_0(Etw):
    pattern = Struct(
        "uiTileID" / Int64ul,
        "nRectTop" / Int32sl,
        "nRectBottom" / Int32sl,
        "nRectLeft" / Int32sl,
        "nRectRight" / Int32sl
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=122, version=0)
class Microsoft_Windows_DUI_122_0(Etw):
    pattern = Struct(
        "uiTileID" / Int64ul,
        "nRectTop" / Int32sl,
        "nRectBottom" / Int32sl,
        "nRectLeft" / Int32sl,
        "nRectRight" / Int32sl
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=126, version=0)
class Microsoft_Windows_DUI_126_0(Etw):
    pattern = Struct(
        "uiTileID" / Int64ul,
        "nRectTop" / Int32sl,
        "nRectBottom" / Int32sl,
        "nRectLeft" / Int32sl,
        "nRectRight" / Int32sl
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=127, version=0)
class Microsoft_Windows_DUI_127_0(Etw):
    pattern = Struct(
        "uiTileID" / Int64ul,
        "nRectTop" / Int32sl,
        "nRectBottom" / Int32sl,
        "nRectLeft" / Int32sl,
        "nRectRight" / Int32sl
    )


@declare(guid=guid("8360bd0f-a7dc-4391-91a7-a457c5c381e4"), event_id=128, version=0)
class Microsoft_Windows_DUI_128_0(Etw):
    pattern = Struct(
        "szResId" / WString
    )

