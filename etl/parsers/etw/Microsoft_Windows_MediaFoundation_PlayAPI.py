# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MediaFoundation-PlayAPI
GUID : b65471e1-019d-436f-bc38-e15fa8e87f53
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=0, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_0_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "URL" / WString,
        "StartPlayback" / Int8ul,
        "Options" / Int32ul,
        "Callback" / Int64ul,
        "HWND" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=1, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_1_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=2, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_2_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=3, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_3_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=4, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_4_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=5, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_5_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=6, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_6_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=7, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_7_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=8, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_8_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=9, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_9_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=10, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_10_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=11, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_11_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=12, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_12_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Frames" / Int32sl
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=13, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_13_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=14, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_14_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "PositionType" / Guid,
        "PositionValueSize" / Int32ul,
        "PositionValue" / Bytes(lambda this: this.PositionValueSize)
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=15, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_15_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=16, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_16_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "PositionType" / Guid
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=17, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_17_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul,
        "PositionValueSize" / Int32ul,
        "PositionValue" / Bytes(lambda this: this.PositionValueSize)
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=18, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_18_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "PositionType" / Guid
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=19, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_19_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul,
        "DurationValueSize" / Int32ul,
        "DurationValue" / Bytes(lambda this: this.DurationValueSize)
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=20, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_20_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Rate" / Float32l
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=20, version=1)
class Microsoft_Windows_MediaFoundation_PlayAPI_20_1(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Rate" / Float32l,
        "Thin" / Int8ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=21, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_21_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=22, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_22_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=23, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_23_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul,
        "Rate" / Float32l
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=24, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_24_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=25, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_25_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul,
        "State" / Int32sl
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=26, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_26_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TimeIn100ns" / Int64ul,
        "UserData" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=27, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_27_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "CancelCookiePtr" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=28, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_28_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "URL" / WString,
        "Synchronous" / Int8ul,
        "UserData" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=29, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_29_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul,
        "MediaItem" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=30, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_30_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "SourceObject" / Int64ul,
        "Synchronous" / Int8ul,
        "UserData" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=31, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_31_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul,
        "MediaItem" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=32, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_32_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "MediaItem" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=33, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_33_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=34, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_34_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=35, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_35_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=36, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_36_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=37, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_37_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul,
        "MediaItem" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=38, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_38_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=39, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_39_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul,
        "Volume" / Float32l
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=40, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_40_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Volume" / Float32l
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=41, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_41_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=42, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_42_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=43, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_43_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul,
        "Balance" / Float32l
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=44, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_44_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Balance" / Float32l
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=45, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_45_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=46, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_46_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=47, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_47_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul,
        "VideoSizeSize" / Int32ul,
        "VideoSize" / Bytes(lambda this: this.VideoSizeSize),
        "AspectSizeSize" / Int32ul,
        "AspectSize" / Bytes(lambda this: this.AspectSizeSize)
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=48, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_48_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=49, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_49_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul,
        "MinSizeSize" / Int32ul,
        "MinSize" / Bytes(lambda this: this.MinSizeSize),
        "MaxSizeSize" / Int32ul,
        "MaxSize" / Bytes(lambda this: this.MaxSizeSize)
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=50, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_50_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Left" / Float32l,
        "Top" / Float32l,
        "Right" / Float32l,
        "Bottom" / Float32l
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=51, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_51_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=52, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_52_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=53, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_53_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul,
        "Left" / Float32l,
        "Top" / Float32l,
        "Right" / Float32l,
        "Bottom" / Float32l
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=54, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_54_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "AspectRatioFlags" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=55, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_55_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=56, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_56_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=57, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_57_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul,
        "AspectRatioFlags" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=58, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_58_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=59, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_59_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul,
        "HWND" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=60, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_60_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=61, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_61_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=62, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_62_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ColorRGB" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=63, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_63_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=64, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_64_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=65, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_65_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul,
        "ColorRGB" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=66, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_66_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Effect" / Int64ul,
        "Optional" / Int8ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=67, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_67_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=68, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_68_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Effect" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=69, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_69_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=70, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_70_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=71, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_71_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=72, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_72_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=73, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_73_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=74, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_74_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StartPositionType" / Guid,
        "StartPositionSize" / Int32ul,
        "StartPosition" / Bytes(lambda this: this.StartPositionSize),
        "StopPositionType" / Guid,
        "StopPositionSize" / Int32ul,
        "StopPosition" / Bytes(lambda this: this.StopPositionSize)
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=75, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_75_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=76, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_76_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "Select" / Int8ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=77, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_77_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=78, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_78_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "CancelCookiePtrPtr" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=79, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_79_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=80, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_80_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=81, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_81_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul,
        "Mute" / Int8ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=82, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_82_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Mute" / Int8ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=83, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_83_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=84, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_84_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=85, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_85_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul,
        "ForwardDirection" / Int8ul,
        "SlowestRate" / Float32l,
        "FastestRate" / Float32l
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=500, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_500_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "EventCookie" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=501, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_501_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "EventCookie" / Int64ul,
        "EventType" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=502, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_502_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "EventCookie" / Int64ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=503, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_503_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Options" / Int32ul
    )


@declare(guid=guid("b65471e1-019d-436f-bc38-e15fa8e87f53"), event_id=504, version=0)
class Microsoft_Windows_MediaFoundation_PlayAPI_504_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )

