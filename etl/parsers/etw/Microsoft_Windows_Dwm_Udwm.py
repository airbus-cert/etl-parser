# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Dwm-Udwm
GUID : a2d1c713-093b-43a7-b445-d09370ec9f47
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=1, version=0)
class Microsoft_Windows_Dwm_Udwm_1_0(Etw):
    pattern = Struct(
        "flags" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=2, version=0)
class Microsoft_Windows_Dwm_Udwm_2_0(Etw):
    pattern = Struct(
        "flags" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5, version=0)
class Microsoft_Windows_Dwm_Udwm_5_0(Etw):
    pattern = Struct(
        "Height" / Int32ul,
        "Width" / Int32ul,
        "Depth" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5000, version=0)
class Microsoft_Windows_Dwm_Udwm_5000_0(Etw):
    pattern = Struct(
        "Schedules" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5002, version=0)
class Microsoft_Windows_Dwm_Udwm_5002_0(Etw):
    pattern = Struct(
        "AnimationType" / Int32ul,
        "Hwnd" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5003, version=0)
class Microsoft_Windows_Dwm_Udwm_5003_0(Etw):
    pattern = Struct(
        "AnimationType" / Int32ul,
        "Hwnd" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5005, version=0)
class Microsoft_Windows_Dwm_Udwm_5005_0(Etw):
    pattern = Struct(
        "Action" / Int32ul,
        "Hwnd" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5006, version=0)
class Microsoft_Windows_Dwm_Udwm_5006_0(Etw):
    pattern = Struct(
        "Action" / Int32ul,
        "Hwnd" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5007, version=0)
class Microsoft_Windows_Dwm_Udwm_5007_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5008, version=0)
class Microsoft_Windows_Dwm_Udwm_5008_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5009, version=0)
class Microsoft_Windows_Dwm_Udwm_5009_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5010, version=0)
class Microsoft_Windows_Dwm_Udwm_5010_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5014, version=0)
class Microsoft_Windows_Dwm_Udwm_5014_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5015, version=0)
class Microsoft_Windows_Dwm_Udwm_5015_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5016, version=0)
class Microsoft_Windows_Dwm_Udwm_5016_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5017, version=0)
class Microsoft_Windows_Dwm_Udwm_5017_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5020, version=0)
class Microsoft_Windows_Dwm_Udwm_5020_0(Etw):
    pattern = Struct(
        "Left" / Int32sl,
        "Top" / Int32sl,
        "Right" / Int32sl,
        "Bottom" / Int32sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5027, version=0)
class Microsoft_Windows_Dwm_Udwm_5027_0(Etw):
    pattern = Struct(
        "PointerID" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5030, version=0)
class Microsoft_Windows_Dwm_Udwm_5030_0(Etw):
    pattern = Struct(
        "PointerID" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5031, version=0)
class Microsoft_Windows_Dwm_Udwm_5031_0(Etw):
    pattern = Struct(
        "Enum" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5032, version=0)
class Microsoft_Windows_Dwm_Udwm_5032_0(Etw):
    pattern = Struct(
        "Enum" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5051, version=0)
class Microsoft_Windows_Dwm_Udwm_5051_0(Etw):
    pattern = Struct(
        "flags" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5052, version=0)
class Microsoft_Windows_Dwm_Udwm_5052_0(Etw):
    pattern = Struct(
        "flags" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5053, version=0)
class Microsoft_Windows_Dwm_Udwm_5053_0(Etw):
    pattern = Struct(
        "Enum" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5054, version=0)
class Microsoft_Windows_Dwm_Udwm_5054_0(Etw):
    pattern = Struct(
        "Enum" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5055, version=0)
class Microsoft_Windows_Dwm_Udwm_5055_0(Etw):
    pattern = Struct(
        "PointerID" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5058, version=0)
class Microsoft_Windows_Dwm_Udwm_5058_0(Etw):
    pattern = Struct(
        "alignment" / Int32sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5059, version=0)
class Microsoft_Windows_Dwm_Udwm_5059_0(Etw):
    pattern = Struct(
        "AnimationID" / Int32ul,
        "StoryboardID" / Int32sl,
        "TickCount" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5060, version=0)
class Microsoft_Windows_Dwm_Udwm_5060_0(Etw):
    pattern = Struct(
        "AnimationID" / Int32ul,
        "StoryboardID" / Int32sl,
        "TickCount" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5063, version=0)
class Microsoft_Windows_Dwm_Udwm_5063_0(Etw):
    pattern = Struct(
        "StoryboardID" / Int32sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5064, version=0)
class Microsoft_Windows_Dwm_Udwm_5064_0(Etw):
    pattern = Struct(
        "StoryboardID" / Int32sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5065, version=0)
class Microsoft_Windows_Dwm_Udwm_5065_0(Etw):
    pattern = Struct(
        "StoryboardID" / Int32sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5070, version=0)
class Microsoft_Windows_Dwm_Udwm_5070_0(Etw):
    pattern = Struct(
        "EventId" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5071, version=0)
class Microsoft_Windows_Dwm_Udwm_5071_0(Etw):
    pattern = Struct(
        "AnimationID" / Int32ul,
        "x0" / Float32l,
        "y0" / Float32l,
        "x1" / Float32l,
        "y1" / Float32l
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5072, version=0)
class Microsoft_Windows_Dwm_Udwm_5072_0(Etw):
    pattern = Struct(
        "PointerID" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5073, version=0)
class Microsoft_Windows_Dwm_Udwm_5073_0(Etw):
    pattern = Struct(
        "PointerID" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5074, version=0)
class Microsoft_Windows_Dwm_Udwm_5074_0(Etw):
    pattern = Struct(
        "PointerID" / Int32ul,
        "Enum" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5075, version=0)
class Microsoft_Windows_Dwm_Udwm_5075_0(Etw):
    pattern = Struct(
        "PointerID" / Int32ul,
        "Enum" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5076, version=0)
class Microsoft_Windows_Dwm_Udwm_5076_0(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "AnimationID" / Int32sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5081, version=0)
class Microsoft_Windows_Dwm_Udwm_5081_0(Etw):
    pattern = Struct(
        "ResourceId" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5083, version=0)
class Microsoft_Windows_Dwm_Udwm_5083_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "StoryboardId" / Int32sl,
        "Target" / Int32sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5084, version=0)
class Microsoft_Windows_Dwm_Udwm_5084_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "StoryboardId" / Int32sl,
        "Target" / Int32sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5085, version=0)
class Microsoft_Windows_Dwm_Udwm_5085_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "StoryboardId" / Int32sl,
        "Target" / Int32sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5086, version=0)
class Microsoft_Windows_Dwm_Udwm_5086_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "StoryboardId" / Int32sl,
        "Target" / Int32sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5087, version=0)
class Microsoft_Windows_Dwm_Udwm_5087_0(Etw):
    pattern = Struct(
        "Enum" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5088, version=0)
class Microsoft_Windows_Dwm_Udwm_5088_0(Etw):
    pattern = Struct(
        "Enum" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5089, version=0)
class Microsoft_Windows_Dwm_Udwm_5089_0(Etw):
    pattern = Struct(
        "StoryboardId" / Int32sl,
        "TargetId" / Int32sl,
        "BeginLeft" / Int32sl,
        "BeginTop" / Int32sl,
        "BeginRight" / Int32sl,
        "BeginBottom" / Int32sl,
        "EndLeft" / Int32sl,
        "EndTop" / Int32sl,
        "EndRight" / Int32sl,
        "EndBottom" / Int32sl,
        "BeginOpacity" / Float32l,
        "EndOpacity" / Float32l,
        "BeginDepth" / Float32l,
        "EndDepth" / Float32l,
        "ResourceHandle" / Int32ul,
        "StaggerOrder" / Int32ul,
        "AnimationId" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5090, version=0)
class Microsoft_Windows_Dwm_Udwm_5090_0(Etw):
    pattern = Struct(
        "PointerID" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5091, version=0)
class Microsoft_Windows_Dwm_Udwm_5091_0(Etw):
    pattern = Struct(
        "StoryboardID" / Int32sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5092, version=0)
class Microsoft_Windows_Dwm_Udwm_5092_0(Etw):
    pattern = Struct(
        "StoryboardID" / Int32sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5093, version=0)
class Microsoft_Windows_Dwm_Udwm_5093_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "Target" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5096, version=0)
class Microsoft_Windows_Dwm_Udwm_5096_0(Etw):
    pattern = Struct(
        "Title" / WString
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5115, version=0)
class Microsoft_Windows_Dwm_Udwm_5115_0(Etw):
    pattern = Struct(
        "EventId" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5117, version=0)
class Microsoft_Windows_Dwm_Udwm_5117_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "Cloaked" / Int32ul,
        "Tracked" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5118, version=0)
class Microsoft_Windows_Dwm_Udwm_5118_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "Target" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5119, version=0)
class Microsoft_Windows_Dwm_Udwm_5119_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "Show" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5120, version=0)
class Microsoft_Windows_Dwm_Udwm_5120_0(Etw):
    pattern = Struct(
        "StoryboardID" / Int32sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5121, version=0)
class Microsoft_Windows_Dwm_Udwm_5121_0(Etw):
    pattern = Struct(
        "StoryboardID" / Int32sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5122, version=0)
class Microsoft_Windows_Dwm_Udwm_5122_0(Etw):
    pattern = Struct(
        "StoryboardID" / Int32sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5123, version=0)
class Microsoft_Windows_Dwm_Udwm_5123_0(Etw):
    pattern = Struct(
        "hwndCloned" / Int64ul,
        "hwndAfter" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5124, version=0)
class Microsoft_Windows_Dwm_Udwm_5124_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5125, version=0)
class Microsoft_Windows_Dwm_Udwm_5125_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5126, version=0)
class Microsoft_Windows_Dwm_Udwm_5126_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5127, version=0)
class Microsoft_Windows_Dwm_Udwm_5127_0(Etw):
    pattern = Struct(
        "clockId" / Guid,
        "timespan" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5128, version=0)
class Microsoft_Windows_Dwm_Udwm_5128_0(Etw):
    pattern = Struct(
        "clockId" / Guid
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5129, version=0)
class Microsoft_Windows_Dwm_Udwm_5129_0(Etw):
    pattern = Struct(
        "clockId" / Guid,
        "timespan" / Int32ul,
        "count" / Int64sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5130, version=0)
class Microsoft_Windows_Dwm_Udwm_5130_0(Etw):
    pattern = Struct(
        "clockId" / Guid,
        "count" / Int64sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5131, version=0)
class Microsoft_Windows_Dwm_Udwm_5131_0(Etw):
    pattern = Struct(
        "clockId" / Guid,
        "time" / Int64sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5132, version=0)
class Microsoft_Windows_Dwm_Udwm_5132_0(Etw):
    pattern = Struct(
        "clockId" / Guid
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5133, version=0)
class Microsoft_Windows_Dwm_Udwm_5133_0(Etw):
    pattern = Struct(
        "clockId" / Guid,
        "time" / Int64sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5134, version=0)
class Microsoft_Windows_Dwm_Udwm_5134_0(Etw):
    pattern = Struct(
        "clockId" / Guid,
        "oldValue" / Int32sl,
        "newValue" / Int32sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5150, version=0)
class Microsoft_Windows_Dwm_Udwm_5150_0(Etw):
    pattern = Struct(
        "Enum" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5151, version=0)
class Microsoft_Windows_Dwm_Udwm_5151_0(Etw):
    pattern = Struct(
        "StoryboardId" / Int32sl,
        "TargetId" / Int32sl,
        "VisualHandle" / Int32ul,
        "EffectGroupHandle" / Int32ul,
        "Transform3DGroupHandle" / Int32ul,
        "TranslateTransform3DHandle" / Int32ul,
        "ScaleTransform3DHandle" / Int32ul,
        "RotateTransform3DHandle" / Int32ul,
        "Channel" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5152, version=0)
class Microsoft_Windows_Dwm_Udwm_5152_0(Etw):
    pattern = Struct(
        "AnimationHandle" / Int32ul,
        "ResourceHandle" / Int32ul,
        "PropertyID" / Int32ul,
        "Channel" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5153, version=0)
class Microsoft_Windows_Dwm_Udwm_5153_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "DPI" / Int32sl,
        "LogicalOriginX" / Int32sl,
        "LogicalOriginY" / Int32sl,
        "PhysicalOriginX" / Int32sl,
        "PhysicalOriginY" / Int32sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5154, version=0)
class Microsoft_Windows_Dwm_Udwm_5154_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5155, version=0)
class Microsoft_Windows_Dwm_Udwm_5155_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "StoryboardId" / Int32sl,
        "Target" / Int32sl,
        "CreationMethod" / Int32sl,
        "Left" / Int32sl,
        "Top" / Int32sl,
        "Right" / Int32sl,
        "Bottom" / Int32sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=5156, version=0)
class Microsoft_Windows_Dwm_Udwm_5156_0(Etw):
    pattern = Struct(
        "UseDelayStoryboard" / Int8ul,
        "AbandonCrossfade" / Int8ul,
        "FoundValidTarget" / Int8ul,
        "IsResize" / Int8ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=9001, version=0)
class Microsoft_Windows_Dwm_Udwm_9001_0(Etw):
    pattern = Struct(
        "secondarywindowpointer" / Int64ul,
        "hwnd" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=9002, version=0)
class Microsoft_Windows_Dwm_Udwm_9002_0(Etw):
    pattern = Struct(
        "secondarywindowpointer" / Int64ul,
        "hwnd" / Int64ul,
        "representationType" / Int32sl
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=9003, version=0)
class Microsoft_Windows_Dwm_Udwm_9003_0(Etw):
    pattern = Struct(
        "secondarywindowpointer" / Int64ul,
        "hwnd" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=9004, version=0)
class Microsoft_Windows_Dwm_Udwm_9004_0(Etw):
    pattern = Struct(
        "CWindowData" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=9005, version=0)
class Microsoft_Windows_Dwm_Udwm_9005_0(Etw):
    pattern = Struct(
        "hwndDestination" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=9006, version=0)
class Microsoft_Windows_Dwm_Udwm_9006_0(Etw):
    pattern = Struct(
        "pwd" / Int64ul,
        "hwnd" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=9009, version=0)
class Microsoft_Windows_Dwm_Udwm_9009_0(Etw):
    pattern = Struct(
        "pSnapshot" / Int64ul
    )


@declare(guid=guid("a2d1c713-093b-43a7-b445-d09370ec9f47"), event_id=10000, version=0)
class Microsoft_Windows_Dwm_Udwm_10000_0(Etw):
    pattern = Struct(
        "PerfTrackId" / Int32ul
    )

