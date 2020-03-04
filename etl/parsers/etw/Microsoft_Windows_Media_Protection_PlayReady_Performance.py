# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Media-Protection-PlayReady-Performance
GUID : d2402fde-7526-5a7b-501a-25dc7c9c282e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=1, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_1_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul,
        "NewCount" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=2, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_2_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=3, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_3_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=4, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_4_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=5, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_5_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=6, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_6_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=7, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_7_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=8, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_8_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=9, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_9_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=10, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_10_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=11, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_11_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=12, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_12_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=13, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_13_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=14, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_14_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=15, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_15_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=16, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_16_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=17, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_17_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=18, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_18_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=19, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_19_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=20, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_20_0(Etw):
    pattern = Struct(
        "FunctionMapOEMValue" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=21, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_21_0(Etw):
    pattern = Struct(
        "FunctionMapOEMValue" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=22, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_22_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=23, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_23_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=24, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_24_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=25, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_25_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=26, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_26_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=27, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_27_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=28, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_28_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=29, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_29_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=30, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_30_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=31, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_31_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=32, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_32_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=33, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_33_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=34, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_34_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=35, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_35_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=36, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_36_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=37, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_37_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=38, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_38_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=39, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_39_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=40, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_40_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=41, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_41_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=42, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_42_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=43, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_43_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=44, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_44_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=45, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_45_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=46, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_46_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=47, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_47_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=48, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_48_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=49, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_49_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=50, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_50_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=51, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_51_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=52, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_52_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=53, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_53_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=54, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_54_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=55, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_55_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=56, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_56_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=57, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_57_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=58, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_58_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=59, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_59_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=60, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_60_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=61, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_61_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=62, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_62_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=63, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_63_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=64, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_64_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=65, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_65_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=66, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_66_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=67, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_67_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=68, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_68_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=69, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_69_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=70, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_70_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=71, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_71_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=72, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_72_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=73, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_73_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=74, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_74_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=75, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_75_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=76, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_76_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=77, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_77_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=78, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_78_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=79, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_79_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=80, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_80_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=81, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_81_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=82, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_82_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=83, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_83_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=84, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_84_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=85, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_85_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=86, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_86_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=87, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_87_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=88, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_88_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=89, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_89_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=90, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_90_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Flag" / Int8ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=91, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_91_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Flag" / Int8ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=92, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_92_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=93, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_93_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=94, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_94_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=95, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_95_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=96, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_96_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=97, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_97_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=98, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_98_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=99, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_99_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=100, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_100_0(Etw):
    pattern = Struct(
        "Arg1" / Int32ul,
        "Arg2" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=101, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_101_0(Etw):
    pattern = Struct(
        "Arg1" / Int32ul,
        "Arg2" / Int32ul,
        "Arg3" / Int32ul,
        "Arg4" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=102, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_102_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=103, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_103_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=104, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_104_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=105, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_105_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=106, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_106_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=107, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_107_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=108, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_108_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=109, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_109_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=110, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_110_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=111, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_111_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=112, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_112_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=113, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_113_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=114, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_114_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=115, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_115_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=116, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_116_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=117, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_117_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=118, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_118_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=119, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_119_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=120, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_120_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=121, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_121_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=122, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_122_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=123, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_123_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=124, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_124_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=125, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_125_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=126, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_126_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=127, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_127_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=128, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_128_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=129, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_129_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=130, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_130_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=131, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_131_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=132, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_132_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=133, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_133_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=134, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_134_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=135, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_135_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=136, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_136_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=137, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_137_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ptr" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=138, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_138_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_lock" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=139, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_139_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_lock" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=140, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_140_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_AcquireStateLock" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=141, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_141_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_AcquireStateLock" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=142, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_142_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ProcessOutput" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=143, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_143_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_ProcessOutput" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=144, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_144_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_OutputLock" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=145, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_145_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_OutputLock" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=146, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_146_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_AcquireOutputLock" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=147, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_147_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_AcquireOutputLock" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=148, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_148_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_StateLock" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=149, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_149_0(Etw):
    pattern = Struct(
        "CMFTAsyncSimpleBase_StateLock" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=150, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_150_0(Etw):
    pattern = Struct(
        "Size" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=151, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_151_0(Etw):
    pattern = Struct(
        "Size" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=152, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_152_0(Etw):
    pattern = Struct(
        "Oem_MemFree_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=153, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_153_0(Etw):
    pattern = Struct(
        "Oem_MemFree_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=154, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_154_0(Etw):
    pattern = Struct(
        "Size" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=155, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_155_0(Etw):
    pattern = Struct(
        "Size" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=156, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_156_0(Etw):
    pattern = Struct(
        "CDRMMemoryCacheFree_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=157, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_157_0(Etw):
    pattern = Struct(
        "CDRMMemoryCacheFree_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=158, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_158_0(Etw):
    pattern = Struct(
        "Size" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=159, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_159_0(Etw):
    pattern = Struct(
        "Size" / Int32ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=160, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_160_0(Etw):
    pattern = Struct(
        "CDRMMemoryCacheDRM_FREE_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=161, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_161_0(Etw):
    pattern = Struct(
        "CDRMMemoryCacheDRM_FREE_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=162, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_162_0(Etw):
    pattern = Struct(
        "CDRMMemoryCacheClearFreeList_ptr" / Int64ul
    )


@declare(guid=guid("d2402fde-7526-5a7b-501a-25dc7c9c282e"), event_id=163, version=0)
class Microsoft_Windows_Media_Protection_PlayReady_Performance_163_0(Etw):
    pattern = Struct(
        "CDRMMemoryCacheClearFreeList_ptr" / Int64ul
    )

