# -*- coding: utf-8 -*-
"""
Microsoft-JScript
GUID : 57277741-3638-4a4b-bdba-0ac6e45da56c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=5, version=0)
class Microsoft_JScript_5_0(Etw):
    pattern = Struct(
        "ScriptContextID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int64ul,
        "MethodID" / Int32ul,
        "MethodFlags" / Int16ul,
        "MethodAddressRangeID" / Int16ul,
        "SourceID" / Int64ul,
        "Line" / Int32ul,
        "Column" / Int32ul,
        "MethodName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=6, version=0)
class Microsoft_JScript_6_0(Etw):
    pattern = Struct(
        "ScriptContextID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int64ul,
        "MethodID" / Int32ul,
        "MethodFlags" / Int16ul,
        "MethodAddressRangeID" / Int16ul,
        "SourceID" / Int64ul,
        "Line" / Int32ul,
        "Column" / Int32ul,
        "MethodName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=7, version=0)
class Microsoft_JScript_7_0(Etw):
    pattern = Struct(
        "ScriptContextID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=8, version=0)
class Microsoft_JScript_8_0(Etw):
    pattern = Struct(
        "ScriptContextID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=9, version=0)
class Microsoft_JScript_9_0(Etw):
    pattern = Struct(
        "ScriptContextID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int64ul,
        "MethodID" / Int32ul,
        "MethodFlags" / Int16ul,
        "MethodAddressRangeID" / Int16ul,
        "SourceID" / Int64ul,
        "Line" / Int32ul,
        "Column" / Int32ul,
        "MethodName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=10, version=0)
class Microsoft_JScript_10_0(Etw):
    pattern = Struct(
        "ScriptContextID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int64ul,
        "MethodID" / Int32ul,
        "MethodFlags" / Int16ul,
        "MethodAddressRangeID" / Int16ul,
        "SourceID" / Int64ul,
        "Line" / Int32ul,
        "Column" / Int32ul,
        "MethodName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=11, version=0)
class Microsoft_JScript_11_0(Etw):
    pattern = Struct(
        "ScriptContextID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=12, version=0)
class Microsoft_JScript_12_0(Etw):
    pattern = Struct(
        "ScriptContextID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=13, version=0)
class Microsoft_JScript_13_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=14, version=0)
class Microsoft_JScript_14_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=15, version=0)
class Microsoft_JScript_15_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=16, version=0)
class Microsoft_JScript_16_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=17, version=0)
class Microsoft_JScript_17_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "MethodName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=18, version=0)
class Microsoft_JScript_18_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "MethodName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=19, version=0)
class Microsoft_JScript_19_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "MethodName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=20, version=0)
class Microsoft_JScript_20_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "MethodName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=21, version=0)
class Microsoft_JScript_21_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "MethodName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=22, version=0)
class Microsoft_JScript_22_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "MethodName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=23, version=0)
class Microsoft_JScript_23_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "MethodName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=24, version=0)
class Microsoft_JScript_24_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "MethodName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=25, version=0)
class Microsoft_JScript_25_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "MethodName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=26, version=0)
class Microsoft_JScript_26_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "MethodName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=27, version=0)
class Microsoft_JScript_27_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "MethodName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=28, version=0)
class Microsoft_JScript_28_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "MethodName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=29, version=0)
class Microsoft_JScript_29_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=30, version=0)
class Microsoft_JScript_30_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=31, version=0)
class Microsoft_JScript_31_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "EventName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=32, version=0)
class Microsoft_JScript_32_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "EventName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=33, version=0)
class Microsoft_JScript_33_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=34, version=0)
class Microsoft_JScript_34_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=35, version=0)
class Microsoft_JScript_35_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "EventName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=36, version=0)
class Microsoft_JScript_36_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "EventName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=37, version=0)
class Microsoft_JScript_37_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "EventName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=38, version=0)
class Microsoft_JScript_38_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "EventName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=39, version=0)
class Microsoft_JScript_39_0(Etw):
    pattern = Struct(
        "SourceID" / Int64ul,
        "ScriptContextID" / Int64ul,
        "SourceFlags" / Int32ul,
        "Url" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=40, version=0)
class Microsoft_JScript_40_0(Etw):
    pattern = Struct(
        "SourceID" / Int64ul,
        "ScriptContextID" / Int64ul,
        "SourceFlags" / Int32ul,
        "Url" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=41, version=0)
class Microsoft_JScript_41_0(Etw):
    pattern = Struct(
        "SourceID" / Int64ul,
        "ScriptContextID" / Int64ul,
        "SourceFlags" / Int32ul,
        "Url" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=42, version=0)
class Microsoft_JScript_42_0(Etw):
    pattern = Struct(
        "SourceID" / Int64ul,
        "ScriptContextID" / Int64ul,
        "SourceFlags" / Int32ul,
        "Url" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=43, version=0)
class Microsoft_JScript_43_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=44, version=0)
class Microsoft_JScript_44_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=45, version=0)
class Microsoft_JScript_45_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=46, version=0)
class Microsoft_JScript_46_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=47, version=0)
class Microsoft_JScript_47_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=48, version=0)
class Microsoft_JScript_48_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=49, version=0)
class Microsoft_JScript_49_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=50, version=0)
class Microsoft_JScript_50_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=51, version=0)
class Microsoft_JScript_51_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=52, version=0)
class Microsoft_JScript_52_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=53, version=0)
class Microsoft_JScript_53_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=54, version=0)
class Microsoft_JScript_54_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=55, version=0)
class Microsoft_JScript_55_0(Etw):
    pattern = Struct(
        "IsBoxed" / Int8ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=56, version=0)
class Microsoft_JScript_56_0(Etw):
    pattern = Struct(
        "IsBoxed" / Int8ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=57, version=0)
class Microsoft_JScript_57_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=58, version=0)
class Microsoft_JScript_58_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=59, version=0)
class Microsoft_JScript_59_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=60, version=0)
class Microsoft_JScript_60_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=61, version=0)
class Microsoft_JScript_61_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=62, version=0)
class Microsoft_JScript_62_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=63, version=0)
class Microsoft_JScript_63_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=64, version=0)
class Microsoft_JScript_64_0(Etw):
    pattern = Struct(
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=65, version=0)
class Microsoft_JScript_65_0(Etw):
    pattern = Struct(
        "SourceID" / Int64ul,
        "ScriptContextID" / Int64ul,
        "MethodID" / Int32ul,
        "ASTSize" / Int32ul,
        "IsDeferred" / Int8ul,
        "MethodName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=66, version=0)
class Microsoft_JScript_66_0(Etw):
    pattern = Struct(
        "SourceID" / Int64ul,
        "ScriptContextID" / Int64ul,
        "MethodID" / Int32ul,
        "ASTSize" / Int32ul,
        "IsDeferred" / Int8ul,
        "MethodName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=67, version=0)
class Microsoft_JScript_67_0(Etw):
    pattern = Struct(
        "SourceID" / Int64ul,
        "ScriptContextID" / Int64ul,
        "MethodID" / Int32ul,
        "BytecodeCount" / Int32ul,
        "BytecodeSize" / Int32ul,
        "MethodName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=68, version=0)
class Microsoft_JScript_68_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=69, version=0)
class Microsoft_JScript_69_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=70, version=0)
class Microsoft_JScript_70_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=71, version=0)
class Microsoft_JScript_71_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=72, version=0)
class Microsoft_JScript_72_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=73, version=0)
class Microsoft_JScript_73_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=74, version=0)
class Microsoft_JScript_74_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=75, version=0)
class Microsoft_JScript_75_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=76, version=0)
class Microsoft_JScript_76_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=77, version=0)
class Microsoft_JScript_77_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=78, version=0)
class Microsoft_JScript_78_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=79, version=0)
class Microsoft_JScript_79_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "SweptBytes" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=80, version=0)
class Microsoft_JScript_80_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=81, version=0)
class Microsoft_JScript_81_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=82, version=0)
class Microsoft_JScript_82_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=83, version=0)
class Microsoft_JScript_83_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "SweptBytes" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=84, version=0)
class Microsoft_JScript_84_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=85, version=0)
class Microsoft_JScript_85_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=86, version=0)
class Microsoft_JScript_86_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=87, version=0)
class Microsoft_JScript_87_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "SweptBytes" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=88, version=0)
class Microsoft_JScript_88_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "BackgroundMarkRescanCount" / Int8sl
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=89, version=0)
class Microsoft_JScript_89_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "BackgroundMarkRescanCount" / Int8sl
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=90, version=0)
class Microsoft_JScript_90_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=91, version=0)
class Microsoft_JScript_91_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=92, version=0)
class Microsoft_JScript_92_0(Etw):
    pattern = Struct(
        "SourceID" / Int64ul,
        "ScriptContextID" / Int64ul,
        "Size" / Int32ul,
        "IsSaveOnClose" / Int8ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=93, version=0)
class Microsoft_JScript_93_0(Etw):
    pattern = Struct(
        "ScriptContextID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=94, version=0)
class Microsoft_JScript_94_0(Etw):
    pattern = Struct(
        "SourceID" / Int64ul,
        "ScriptContextID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=95, version=0)
class Microsoft_JScript_95_0(Etw):
    pattern = Struct(
        "CallerMethodID" / Int32ul,
        "InlineeMethodID" / Int32ul,
        "Caller" / WString,
        "Inlinee" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=96, version=0)
class Microsoft_JScript_96_0(Etw):
    pattern = Struct(
        "MethodID" / Int32ul,
        "MethodName" / WString,
        "ScriptContext" / Int64ul,
        "InterpretedCount" / Int32ul,
        "SourceCodeSize" / Int32ul,
        "ByteCodeSize" / Int32ul,
        "ByteCodeInLoopSize" / Int32ul,
        "JitLevel" / Int16ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=97, version=0)
class Microsoft_JScript_97_0(Etw):
    pattern = Struct(
        "MethodID" / Int32ul,
        "MethodName" / WString,
        "ScriptContext" / Int64ul,
        "InterpretedCount" / Int32ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=98, version=0)
class Microsoft_JScript_98_0(Etw):
    pattern = Struct(
        "MethodID" / Int32ul,
        "MethodName" / WString,
        "ScriptContext" / Int64ul,
        "InterpretedCount" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=99, version=0)
class Microsoft_JScript_99_0(Etw):
    pattern = Struct(
        "MethodID" / Int32ul,
        "MethodName" / WString,
        "ScriptContext" / Int64ul,
        "InterpretedCount" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=100, version=0)
class Microsoft_JScript_100_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=101, version=0)
class Microsoft_JScript_101_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=102, version=0)
class Microsoft_JScript_102_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=103, version=0)
class Microsoft_JScript_103_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=104, version=0)
class Microsoft_JScript_104_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=105, version=0)
class Microsoft_JScript_105_0(Etw):
    pattern = Struct(
        "SizeInBytes" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=106, version=0)
class Microsoft_JScript_106_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "Values" / CString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=107, version=0)
class Microsoft_JScript_107_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul,
        "BlockSize" / Int32ul,
        "ObjectSize" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=108, version=0)
class Microsoft_JScript_108_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=109, version=0)
class Microsoft_JScript_109_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=110, version=0)
class Microsoft_JScript_110_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul,
        "MethodID" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=111, version=0)
class Microsoft_JScript_111_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul,
        "TypeId" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=112, version=0)
class Microsoft_JScript_112_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul,
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=113, version=0)
class Microsoft_JScript_113_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=114, version=0)
class Microsoft_JScript_114_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=115, version=0)
class Microsoft_JScript_115_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=116, version=0)
class Microsoft_JScript_116_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul,
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=117, version=0)
class Microsoft_JScript_117_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul,
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=118, version=0)
class Microsoft_JScript_118_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul,
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=119, version=0)
class Microsoft_JScript_119_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul,
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=120, version=0)
class Microsoft_JScript_120_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul,
        "TypeName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=121, version=0)
class Microsoft_JScript_121_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul,
        "TypeName" / WString,
        "jsVar" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=122, version=0)
class Microsoft_JScript_122_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul,
        "TypeName" / WString,
        "callback" / Int64ul,
        "EventName" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=123, version=0)
class Microsoft_JScript_123_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul,
        "TypeName" / WString,
        "jsVar" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=124, version=0)
class Microsoft_JScript_124_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul,
        "TypeName" / WString,
        "IsArray" / Int8ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=125, version=0)
class Microsoft_JScript_125_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=126, version=0)
class Microsoft_JScript_126_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=127, version=0)
class Microsoft_JScript_127_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=128, version=0)
class Microsoft_JScript_128_0(Etw):
    pattern = Struct(
        "MemoryAddress" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=129, version=0)
class Microsoft_JScript_129_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=130, version=0)
class Microsoft_JScript_130_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=131, version=0)
class Microsoft_JScript_131_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=132, version=0)
class Microsoft_JScript_132_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=133, version=0)
class Microsoft_JScript_133_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=134, version=0)
class Microsoft_JScript_134_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=135, version=0)
class Microsoft_JScript_135_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=136, version=0)
class Microsoft_JScript_136_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=137, version=0)
class Microsoft_JScript_137_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=138, version=0)
class Microsoft_JScript_138_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=139, version=0)
class Microsoft_JScript_139_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=140, version=0)
class Microsoft_JScript_140_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=141, version=0)
class Microsoft_JScript_141_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=142, version=0)
class Microsoft_JScript_142_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=143, version=0)
class Microsoft_JScript_143_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "BackgroundMarkRescanCount" / Int8sl
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=144, version=0)
class Microsoft_JScript_144_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "BackgroundMarkRescanCount" / Int8sl
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=145, version=0)
class Microsoft_JScript_145_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "BackgroundMarkRescanCount" / Int8sl
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=146, version=0)
class Microsoft_JScript_146_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "BackgroundMarkRescanCount" / Int8sl
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=147, version=0)
class Microsoft_JScript_147_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=148, version=0)
class Microsoft_JScript_148_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=149, version=0)
class Microsoft_JScript_149_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=150, version=0)
class Microsoft_JScript_150_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=151, version=0)
class Microsoft_JScript_151_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=152, version=0)
class Microsoft_JScript_152_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "HasTimedout" / Int8ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=153, version=0)
class Microsoft_JScript_153_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=154, version=0)
class Microsoft_JScript_154_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "HasTimedout" / Int8ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=155, version=0)
class Microsoft_JScript_155_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=156, version=0)
class Microsoft_JScript_156_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "HasTimedout" / Int8ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=157, version=0)
class Microsoft_JScript_157_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=158, version=0)
class Microsoft_JScript_158_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=159, version=0)
class Microsoft_JScript_159_0(Etw):
    pattern = Struct(
        "AsyncOperationId" / Int64ul,
        "FrameCount" / Int16ul,
        "NameBufferCount" / Int16ul,
        "NameBuffer" / Bytes(lambda this: this.NameBufferCount),
        "Frames" / Int16sl
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=160, version=0)
class Microsoft_JScript_160_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=161, version=0)
class Microsoft_JScript_161_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=162, version=0)
class Microsoft_JScript_162_0(Etw):
    pattern = Struct(
        "Jscript9EngineSize" / Int32ul,
        "MshtmlEngineSize" / Int32ul,
        "Jscript9ContextSize" / Int32ul,
        "MshtmlContextSize" / Int32ul,
        "Jscript9LibrarySize" / Int32ul,
        "MshtmlLibrarySize" / Int32ul,
        "Jscript9CEOSize" / Int32ul,
        "MshtmlCEOSize" / Int32ul,
        "Jscript9ScriptEngineOffset" / Int32ul,
        "MshtmlScriptEngineOffset" / Int32ul,
        "Jscript9ScriptContextOffset" / Int32ul,
        "MshtmlScriptContextOffset" / Int32ul,
        "Jscript9LibraryOffset" / Int32ul,
        "MshtmlLibraryOffset" / Int32ul,
        "Jscript9TypeOffset" / Int32ul,
        "MshtmlTypeOffset" / Int32ul,
        "Jscript9TypeIdOffset" / Int32ul,
        "MshtmlTypeIdOffset" / Int32ul,
        "Jscript9TaggedIntSize" / Int32ul,
        "MshtmlTaggIntSize" / Int32ul,
        "Jscript9NumberSize" / Int32ul,
        "MshtmlNumberSize" / Int32ul,
        "Jscript9TypeIdLimit" / Int32ul,
        "MshtmlTypeIdLimit" / Int32ul,
        "JScript9NumberUtilitiesSize" / Int32ul,
        "MsHtmlNumberUtilitiesSize" / Int32ul,
        "JScript9NumberUtilitiesOffset" / Int32ul,
        "MsHtmlNumberUtilitiesOffset" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=163, version=0)
class Microsoft_JScript_163_0(Etw):
    pattern = Struct(
        "MshtmlEngineSize" / Int32ul,
        "MshtmlContextSize" / Int32ul,
        "MshtmlLibrarySize" / Int32ul,
        "MshtmlCEOSize" / Int32ul,
        "MshtmlScriptEngineOffset" / Int32ul,
        "MshtmlScriptContextOffset" / Int32ul,
        "MshtmlLibraryOffset" / Int32ul,
        "MshtmlTypeOffset" / Int32ul,
        "MshtmlTypeIdOffset" / Int32ul,
        "MshtmlTaggIntSize" / Int32ul,
        "MshtmlNumberSize" / Int32ul,
        "MshtmlTypeIdLimit" / Int32ul,
        "MsHtmlNumberUtilitiesSize" / Int32ul,
        "MsHtmlNumberUtilitiesOffset" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=164, version=0)
class Microsoft_JScript_164_0(Etw):
    pattern = Struct(
        "OperationId" / Int64ul,
        "FrameCount" / Int16ul,
        "FrameNameBufferCount" / Int32ul,
        "FrameNameBuffer" / Bytes(lambda this: this.FrameNameBufferCount),
        "Frames" / Int16sl
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=165, version=0)
class Microsoft_JScript_165_0(Etw):
    pattern = Struct(
        "OperationId" / Int64ul,
        "FrameCount" / Int16ul,
        "FrameNameBufferCount" / Int32ul,
        "FrameNameBuffer" / Bytes(lambda this: this.FrameNameBufferCount),
        "Frames" / Int16sl
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=166, version=0)
class Microsoft_JScript_166_0(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "SHA1Hash" / Bytes(20),
        "Url" / WString,
        "ModuleSize" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=167, version=0)
class Microsoft_JScript_167_0(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "SerializationIndex" / Int32ul,
        "Name" / WString,
        "FunctionOffset" / Int32ul,
        "FunctionSize" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=168, version=0)
class Microsoft_JScript_168_0(Etw):
    pattern = Struct(
        "ReasonBuffer" / WString,
        "SourceRequestFor" / Int16ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=169, version=0)
class Microsoft_JScript_169_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=170, version=0)
class Microsoft_JScript_170_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=171, version=0)
class Microsoft_JScript_171_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "BackgroundMarkRescanCount" / Int8sl
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=172, version=0)
class Microsoft_JScript_172_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "BackgroundMarkRescanCount" / Int8sl
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=173, version=0)
class Microsoft_JScript_173_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=174, version=0)
class Microsoft_JScript_174_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=175, version=0)
class Microsoft_JScript_175_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=176, version=0)
class Microsoft_JScript_176_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=177, version=0)
class Microsoft_JScript_177_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=178, version=0)
class Microsoft_JScript_178_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=179, version=0)
class Microsoft_JScript_179_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=180, version=0)
class Microsoft_JScript_180_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=181, version=0)
class Microsoft_JScript_181_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=182, version=0)
class Microsoft_JScript_182_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=183, version=0)
class Microsoft_JScript_183_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=184, version=0)
class Microsoft_JScript_184_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "SweptBytes" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=185, version=0)
class Microsoft_JScript_185_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=186, version=0)
class Microsoft_JScript_186_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=187, version=0)
class Microsoft_JScript_187_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=188, version=0)
class Microsoft_JScript_188_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "SweptBytes" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=189, version=0)
class Microsoft_JScript_189_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=190, version=0)
class Microsoft_JScript_190_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=191, version=0)
class Microsoft_JScript_191_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=192, version=0)
class Microsoft_JScript_192_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "SweptBytes" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=193, version=0)
class Microsoft_JScript_193_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "BackgroundMarkRescanCount" / Int8sl
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=194, version=0)
class Microsoft_JScript_194_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "BackgroundMarkRescanCount" / Int8sl
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=195, version=0)
class Microsoft_JScript_195_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=196, version=0)
class Microsoft_JScript_196_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=197, version=0)
class Microsoft_JScript_197_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=198, version=0)
class Microsoft_JScript_198_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=199, version=0)
class Microsoft_JScript_199_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=200, version=0)
class Microsoft_JScript_200_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=201, version=0)
class Microsoft_JScript_201_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=202, version=0)
class Microsoft_JScript_202_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=203, version=0)
class Microsoft_JScript_203_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=204, version=0)
class Microsoft_JScript_204_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=205, version=0)
class Microsoft_JScript_205_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=206, version=0)
class Microsoft_JScript_206_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=207, version=0)
class Microsoft_JScript_207_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=208, version=0)
class Microsoft_JScript_208_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=209, version=0)
class Microsoft_JScript_209_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=210, version=0)
class Microsoft_JScript_210_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=211, version=0)
class Microsoft_JScript_211_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=212, version=0)
class Microsoft_JScript_212_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=213, version=0)
class Microsoft_JScript_213_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=214, version=0)
class Microsoft_JScript_214_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=215, version=0)
class Microsoft_JScript_215_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=216, version=0)
class Microsoft_JScript_216_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "BackgroundMarkRescanCount" / Int8sl
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=217, version=0)
class Microsoft_JScript_217_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "BackgroundMarkRescanCount" / Int8sl
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=218, version=0)
class Microsoft_JScript_218_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "BackgroundMarkRescanCount" / Int8sl
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=219, version=0)
class Microsoft_JScript_219_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "BackgroundMarkRescanCount" / Int8sl
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=220, version=0)
class Microsoft_JScript_220_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=221, version=0)
class Microsoft_JScript_221_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=222, version=0)
class Microsoft_JScript_222_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=223, version=0)
class Microsoft_JScript_223_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=224, version=0)
class Microsoft_JScript_224_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=225, version=0)
class Microsoft_JScript_225_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "HasTimedout" / Int8ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=226, version=0)
class Microsoft_JScript_226_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=227, version=0)
class Microsoft_JScript_227_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "HasTimedout" / Int8ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=228, version=0)
class Microsoft_JScript_228_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=229, version=0)
class Microsoft_JScript_229_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "HasTimedout" / Int8ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=230, version=0)
class Microsoft_JScript_230_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=231, version=0)
class Microsoft_JScript_231_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=232, version=0)
class Microsoft_JScript_232_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=233, version=0)
class Microsoft_JScript_233_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=234, version=0)
class Microsoft_JScript_234_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "BackgroundMarkRescanCount" / Int8sl
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=235, version=0)
class Microsoft_JScript_235_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "BackgroundMarkRescanCount" / Int8sl
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=236, version=0)
class Microsoft_JScript_236_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=237, version=0)
class Microsoft_JScript_237_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=238, version=0)
class Microsoft_JScript_238_0(Etw):
    pattern = Struct(
        "HeapHandle" / Int64ul,
        "Size" / Int64ul,
        "Address" / Int64ul,
        "Source" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=239, version=0)
class Microsoft_JScript_239_0(Etw):
    pattern = Struct(
        "HeapHandle" / Int64ul,
        "Address" / Int64ul,
        "Source" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=240, version=0)
class Microsoft_JScript_240_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "Timestamp" / Double
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=241, version=0)
class Microsoft_JScript_241_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "UsedBytes" / Int64ul,
        "ReservedBytes" / Int64ul,
        "CommittedBytes" / Int64ul,
        "NumberOfSegments" / Int64ul,
        "FromGC" / Int8ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=242, version=0)
class Microsoft_JScript_242_0(Etw):
    pattern = Struct(
        "eventData" / WString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=243, version=0)
class Microsoft_JScript_243_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "Type" / Int16ul,
        "SizeCat" / Int16ul,
        "UsedBytes" / Int64ul,
        "TotalBytes" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=244, version=0)
class Microsoft_JScript_244_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "Type" / Int16ul,
        "SizeCat" / Int16ul,
        "UsedBytes" / Int64ul,
        "TotalBytes" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=245, version=0)
class Microsoft_JScript_245_0(Etw):
    pattern = Struct(
        "FunctionMethodID" / Int32ul,
        "FunctionSourceID" / Int32ul,
        "FunctionDisplayName" / WString,
        "BailoutKind" / Int32ul,
        "BailoutCount" / Int32ul,
        "CallCount" / Int32ul,
        "RejitReason" / CString,
        "Rethunk" / Int8ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=246, version=0)
class Microsoft_JScript_246_0(Etw):
    pattern = Struct(
        "FunctionMethodID" / Int32ul,
        "FunctionSourceID" / Int32ul,
        "FunctionDisplayName" / WString,
        "LoopNumber" / Int32ul,
        "BailoutKind" / Int32ul,
        "RejitReason" / CString
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=248, version=0)
class Microsoft_JScript_248_0(Etw):
    pattern = Struct(
        "ThreadContextID" / Int64ul,
        "ScriptContextCount" / Int32ul,
        "AllocatedSize" / Int32ul,
        "PreClearFreeSize" / Int32ul,
        "FreeSize" / Int32ul,
        "PolyInlineCacheSize" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=249, version=0)
class Microsoft_JScript_249_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=250, version=0)
class Microsoft_JScript_250_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=251, version=0)
class Microsoft_JScript_251_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=252, version=0)
class Microsoft_JScript_252_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=253, version=0)
class Microsoft_JScript_253_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "ScannedCount" / Int32ul,
        "ClearedCount" / Int32ul,
        "RegionScannedCount" / Int32ul,
        "RegionClearedCount" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=254, version=0)
class Microsoft_JScript_254_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "ScannedCount" / Int32ul,
        "ClearedCount" / Int32ul,
        "RegionScannedCount" / Int32ul,
        "RegionClearedCount" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=255, version=0)
class Microsoft_JScript_255_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "Phase" / Int32ul,
        "CollectionTrigger" / Int32ul,
        "CollectionStartFlags" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=256, version=0)
class Microsoft_JScript_256_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "Phase" / Int32ul,
        "CollectionTrigger" / Int32ul,
        "CollectionStartFlags" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=257, version=0)
class Microsoft_JScript_257_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "Phase" / Int32ul,
        "CollectionTrigger" / Int32ul,
        "CollectionStartFlags" / Int32ul
    )


@declare(guid=guid("57277741-3638-4a4b-bdba-0ac6e45da56c"), event_id=258, version=0)
class Microsoft_JScript_258_0(Etw):
    pattern = Struct(
        "RecyclerID" / Int64ul,
        "Phase" / Int32ul,
        "CollectionTrigger" / Int32ul,
        "CollectionStartFlags" / Int32ul
    )

