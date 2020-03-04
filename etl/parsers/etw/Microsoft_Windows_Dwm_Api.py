# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Dwm-Api
GUID : 292a52c4-fa27-4461-b526-54a46430bd54
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=2, version=0)
class Microsoft_Windows_Dwm_Api_2_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=4, version=0)
class Microsoft_Windows_Dwm_Api_4_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=6, version=0)
class Microsoft_Windows_Dwm_Api_6_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=8, version=0)
class Microsoft_Windows_Dwm_Api_8_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=9, version=0)
class Microsoft_Windows_Dwm_Api_9_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=10, version=0)
class Microsoft_Windows_Dwm_Api_10_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "Hwnd" / Int64ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=11, version=0)
class Microsoft_Windows_Dwm_Api_11_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=12, version=0)
class Microsoft_Windows_Dwm_Api_12_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "Hwnd" / Int64ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=14, version=0)
class Microsoft_Windows_Dwm_Api_14_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=16, version=0)
class Microsoft_Windows_Dwm_Api_16_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=18, version=0)
class Microsoft_Windows_Dwm_Api_18_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=20, version=0)
class Microsoft_Windows_Dwm_Api_20_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=24, version=0)
class Microsoft_Windows_Dwm_Api_24_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=26, version=0)
class Microsoft_Windows_Dwm_Api_26_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=27, version=0)
class Microsoft_Windows_Dwm_Api_27_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=28, version=0)
class Microsoft_Windows_Dwm_Api_28_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "hwnd" / Int64ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=30, version=0)
class Microsoft_Windows_Dwm_Api_30_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=32, version=0)
class Microsoft_Windows_Dwm_Api_32_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=34, version=0)
class Microsoft_Windows_Dwm_Api_34_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=36, version=0)
class Microsoft_Windows_Dwm_Api_36_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=38, version=0)
class Microsoft_Windows_Dwm_Api_38_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=40, version=0)
class Microsoft_Windows_Dwm_Api_40_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=42, version=0)
class Microsoft_Windows_Dwm_Api_42_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=44, version=0)
class Microsoft_Windows_Dwm_Api_44_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=45, version=0)
class Microsoft_Windows_Dwm_Api_45_0(Etw):
    pattern = Struct(
        "Hwnd" / Int64ul,
        "luidAdapter" / Int64ul,
        "hmonAssociation" / Int64ul,
        "dwFlags" / Int32ul,
        "DxgiFormat" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=46, version=0)
class Microsoft_Windows_Dwm_Api_46_0(Etw):
    pattern = Struct(
        "Hwnd" / Int64ul,
        "hr" / Int32ul,
        "hDxSurface" / Int64ul,
        "uiUpdateId" / Int64ul,
        "DxgiFormat" / Int32ul,
        "cTries" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=48, version=0)
class Microsoft_Windows_Dwm_Api_48_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "Hwnd" / Int64ul,
        "left" / Int32ul,
        "top" / Int32ul,
        "right" / Int32ul,
        "bottom" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=50, version=0)
class Microsoft_Windows_Dwm_Api_50_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "fEnable" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=52, version=0)
class Microsoft_Windows_Dwm_Api_52_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=54, version=0)
class Microsoft_Windows_Dwm_Api_54_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=56, version=0)
class Microsoft_Windows_Dwm_Api_56_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=58, version=0)
class Microsoft_Windows_Dwm_Api_58_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=66, version=0)
class Microsoft_Windows_Dwm_Api_66_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=68, version=0)
class Microsoft_Windows_Dwm_Api_68_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=70, version=0)
class Microsoft_Windows_Dwm_Api_70_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=71, version=0)
class Microsoft_Windows_Dwm_Api_71_0(Etw):
    pattern = Struct(
        "hwndDst" / Int64ul,
        "hwndSrc" / Int64ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=72, version=0)
class Microsoft_Windows_Dwm_Api_72_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "hwnd" / Int64ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=73, version=0)
class Microsoft_Windows_Dwm_Api_73_0(Etw):
    pattern = Struct(
        "fActivate" / Int8ul,
        "hwndExclude" / Int64ul,
        "trigger" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=74, version=0)
class Microsoft_Windows_Dwm_Api_74_0(Etw):
    pattern = Struct(
        "fActivate" / Int8ul,
        "hwndExclude" / Int64ul,
        "trigger" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=75, version=0)
class Microsoft_Windows_Dwm_Api_75_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=76, version=0)
class Microsoft_Windows_Dwm_Api_76_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "hwnd" / Int64ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=77, version=0)
class Microsoft_Windows_Dwm_Api_77_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=78, version=0)
class Microsoft_Windows_Dwm_Api_78_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "hwnd" / Int64ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=80, version=0)
class Microsoft_Windows_Dwm_Api_80_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "Hwnd" / Int64ul,
        "left" / Int32ul,
        "top" / Int32ul,
        "right" / Int32ul,
        "bottom" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=82, version=0)
class Microsoft_Windows_Dwm_Api_82_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "Hwnd" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=84, version=0)
class Microsoft_Windows_Dwm_Api_84_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=85, version=0)
class Microsoft_Windows_Dwm_Api_85_0(Etw):
    pattern = Struct(
        "Enum" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=86, version=0)
class Microsoft_Windows_Dwm_Api_86_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "Enum" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=88, version=0)
class Microsoft_Windows_Dwm_Api_88_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=90, version=0)
class Microsoft_Windows_Dwm_Api_90_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=92, version=0)
class Microsoft_Windows_Dwm_Api_92_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=94, version=0)
class Microsoft_Windows_Dwm_Api_94_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=96, version=0)
class Microsoft_Windows_Dwm_Api_96_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=98, version=0)
class Microsoft_Windows_Dwm_Api_98_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=99, version=0)
class Microsoft_Windows_Dwm_Api_99_0(Etw):
    pattern = Struct(
        "storyid" / Int32sl
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=100, version=0)
class Microsoft_Windows_Dwm_Api_100_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=101, version=0)
class Microsoft_Windows_Dwm_Api_101_0(Etw):
    pattern = Struct(
        "storyid" / Int32sl
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=102, version=0)
class Microsoft_Windows_Dwm_Api_102_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=103, version=0)
class Microsoft_Windows_Dwm_Api_103_0(Etw):
    pattern = Struct(
        "Hwnd" / Int64ul,
        "target" / Int32sl
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=104, version=0)
class Microsoft_Windows_Dwm_Api_104_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=105, version=0)
class Microsoft_Windows_Dwm_Api_105_0(Etw):
    pattern = Struct(
        "Hwnd" / Int64ul,
        "target" / Int32sl
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=106, version=0)
class Microsoft_Windows_Dwm_Api_106_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=107, version=0)
class Microsoft_Windows_Dwm_Api_107_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=108, version=0)
class Microsoft_Windows_Dwm_Api_108_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=110, version=0)
class Microsoft_Windows_Dwm_Api_110_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("292a52c4-fa27-4461-b526-54a46430bd54"), event_id=112, version=0)
class Microsoft_Windows_Dwm_Api_112_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )

