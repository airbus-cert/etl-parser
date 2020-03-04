# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Dism-Api
GUID : 75b0da21-8b50-42eb-9448-ec48b1729b57
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=5, version=0)
class Microsoft_Windows_Dism_Api_5_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=6, version=0)
class Microsoft_Windows_Dism_Api_6_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=7, version=0)
class Microsoft_Windows_Dism_Api_7_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=8, version=0)
class Microsoft_Windows_Dism_Api_8_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=9, version=0)
class Microsoft_Windows_Dism_Api_9_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=10, version=0)
class Microsoft_Windows_Dism_Api_10_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=11, version=0)
class Microsoft_Windows_Dism_Api_11_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=12, version=0)
class Microsoft_Windows_Dism_Api_12_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=13, version=0)
class Microsoft_Windows_Dism_Api_13_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=14, version=0)
class Microsoft_Windows_Dism_Api_14_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=15, version=0)
class Microsoft_Windows_Dism_Api_15_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=16, version=0)
class Microsoft_Windows_Dism_Api_16_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=23, version=0)
class Microsoft_Windows_Dism_Api_23_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=24, version=0)
class Microsoft_Windows_Dism_Api_24_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=25, version=0)
class Microsoft_Windows_Dism_Api_25_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=26, version=0)
class Microsoft_Windows_Dism_Api_26_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=27, version=0)
class Microsoft_Windows_Dism_Api_27_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=28, version=0)
class Microsoft_Windows_Dism_Api_28_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=29, version=0)
class Microsoft_Windows_Dism_Api_29_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=30, version=0)
class Microsoft_Windows_Dism_Api_30_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=35, version=0)
class Microsoft_Windows_Dism_Api_35_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=36, version=0)
class Microsoft_Windows_Dism_Api_36_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=37, version=0)
class Microsoft_Windows_Dism_Api_37_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=38, version=0)
class Microsoft_Windows_Dism_Api_38_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=39, version=0)
class Microsoft_Windows_Dism_Api_39_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=40, version=0)
class Microsoft_Windows_Dism_Api_40_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=41, version=0)
class Microsoft_Windows_Dism_Api_41_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=42, version=0)
class Microsoft_Windows_Dism_Api_42_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=43, version=0)
class Microsoft_Windows_Dism_Api_43_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=44, version=0)
class Microsoft_Windows_Dism_Api_44_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=45, version=0)
class Microsoft_Windows_Dism_Api_45_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=46, version=0)
class Microsoft_Windows_Dism_Api_46_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=47, version=0)
class Microsoft_Windows_Dism_Api_47_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=48, version=0)
class Microsoft_Windows_Dism_Api_48_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=49, version=0)
class Microsoft_Windows_Dism_Api_49_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=50, version=0)
class Microsoft_Windows_Dism_Api_50_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=51, version=0)
class Microsoft_Windows_Dism_Api_51_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=52, version=0)
class Microsoft_Windows_Dism_Api_52_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=53, version=0)
class Microsoft_Windows_Dism_Api_53_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=54, version=0)
class Microsoft_Windows_Dism_Api_54_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=55, version=0)
class Microsoft_Windows_Dism_Api_55_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=56, version=0)
class Microsoft_Windows_Dism_Api_56_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=57, version=0)
class Microsoft_Windows_Dism_Api_57_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=58, version=0)
class Microsoft_Windows_Dism_Api_58_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=59, version=0)
class Microsoft_Windows_Dism_Api_59_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=60, version=0)
class Microsoft_Windows_Dism_Api_60_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=61, version=0)
class Microsoft_Windows_Dism_Api_61_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=62, version=0)
class Microsoft_Windows_Dism_Api_62_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=63, version=0)
class Microsoft_Windows_Dism_Api_63_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=64, version=0)
class Microsoft_Windows_Dism_Api_64_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=65, version=0)
class Microsoft_Windows_Dism_Api_65_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=66, version=0)
class Microsoft_Windows_Dism_Api_66_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=67, version=0)
class Microsoft_Windows_Dism_Api_67_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=68, version=0)
class Microsoft_Windows_Dism_Api_68_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=69, version=0)
class Microsoft_Windows_Dism_Api_69_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=70, version=0)
class Microsoft_Windows_Dism_Api_70_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=71, version=0)
class Microsoft_Windows_Dism_Api_71_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=72, version=0)
class Microsoft_Windows_Dism_Api_72_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=73, version=0)
class Microsoft_Windows_Dism_Api_73_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=74, version=0)
class Microsoft_Windows_Dism_Api_74_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=75, version=0)
class Microsoft_Windows_Dism_Api_75_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=76, version=0)
class Microsoft_Windows_Dism_Api_76_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=77, version=0)
class Microsoft_Windows_Dism_Api_77_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=78, version=0)
class Microsoft_Windows_Dism_Api_78_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=79, version=0)
class Microsoft_Windows_Dism_Api_79_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=80, version=0)
class Microsoft_Windows_Dism_Api_80_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=81, version=0)
class Microsoft_Windows_Dism_Api_81_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=82, version=0)
class Microsoft_Windows_Dism_Api_82_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=83, version=0)
class Microsoft_Windows_Dism_Api_83_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=84, version=0)
class Microsoft_Windows_Dism_Api_84_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=85, version=0)
class Microsoft_Windows_Dism_Api_85_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=86, version=0)
class Microsoft_Windows_Dism_Api_86_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=87, version=0)
class Microsoft_Windows_Dism_Api_87_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("75b0da21-8b50-42eb-9448-ec48b1729b57"), event_id=88, version=0)
class Microsoft_Windows_Dism_Api_88_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "String" / WString
    )

