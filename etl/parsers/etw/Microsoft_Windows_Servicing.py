# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Servicing
GUID : bd12f3b8-fc40-4a61-a307-b7a013a069c1
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=1, version=0)
class Microsoft_Windows_Servicing_1_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "currentPackageState" / Int32ul,
        "currentPackageStateTextized" / WString,
        "targetPackageState" / Int32ul,
        "targetPackageStateTextized" / WString,
        "client" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=2, version=0)
class Microsoft_Windows_Servicing_2_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "targetPackageState" / Int32ul,
        "targetPackageStateTextized" / WString,
        "errorCode" / WString,
        "client" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=3, version=0)
class Microsoft_Windows_Servicing_3_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "targetPackageState" / Int32ul,
        "targetPackageStateTextized" / WString,
        "errorCode" / WString,
        "client" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4, version=0)
class Microsoft_Windows_Servicing_4_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "targetPackageState" / Int32ul,
        "targetPackageStateTextized" / WString,
        "errorCode" / WString,
        "client" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=5, version=0)
class Microsoft_Windows_Servicing_5_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "targetPackageState" / Int32ul,
        "targetPackageStateTextized" / WString,
        "errorCode" / WString,
        "client" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=6, version=0)
class Microsoft_Windows_Servicing_6_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "targetPackageState" / Int32ul,
        "targetPackageStateTextized" / WString,
        "errorCode" / WString,
        "client" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=7, version=0)
class Microsoft_Windows_Servicing_7_0(Etw):
    pattern = Struct(
        "updateName" / WString,
        "identifier" / WString,
        "errorCode" / WString,
        "client" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=8, version=0)
class Microsoft_Windows_Servicing_8_0(Etw):
    pattern = Struct(
        "updateName" / WString,
        "identifier" / WString,
        "errorCode" / WString,
        "client" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=9, version=0)
class Microsoft_Windows_Servicing_9_0(Etw):
    pattern = Struct(
        "updateName" / WString,
        "identifier" / WString,
        "errorCode" / WString,
        "client" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=10, version=0)
class Microsoft_Windows_Servicing_10_0(Etw):
    pattern = Struct(
        "updateName" / WString,
        "identifier" / WString,
        "errorCode" / WString,
        "client" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=11, version=0)
class Microsoft_Windows_Servicing_11_0(Etw):
    pattern = Struct(
        "updateName" / WString,
        "identifier" / WString,
        "errorCode" / WString,
        "client" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=12, version=0)
class Microsoft_Windows_Servicing_12_0(Etw):
    pattern = Struct(
        "updateName" / WString,
        "identifier" / WString,
        "errorCode" / WString,
        "client" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=13, version=0)
class Microsoft_Windows_Servicing_13_0(Etw):
    pattern = Struct(
        "updateName" / WString,
        "identifier" / WString,
        "errorCode" / WString,
        "client" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=14, version=0)
class Microsoft_Windows_Servicing_14_0(Etw):
    pattern = Struct(
        "updateName" / WString,
        "identifier" / WString,
        "errorCode" / WString,
        "client" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=15, version=0)
class Microsoft_Windows_Servicing_15_0(Etw):
    pattern = Struct(
        "updateName" / WString,
        "identifier" / WString,
        "errorCode" / WString,
        "client" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=16, version=0)
class Microsoft_Windows_Servicing_16_0(Etw):
    pattern = Struct(
        "updateName" / WString,
        "identifier" / WString,
        "errorCode" / WString,
        "client" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=17, version=0)
class Microsoft_Windows_Servicing_17_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=18, version=0)
class Microsoft_Windows_Servicing_18_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=20, version=0)
class Microsoft_Windows_Servicing_20_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=21, version=0)
class Microsoft_Windows_Servicing_21_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=23, version=0)
class Microsoft_Windows_Servicing_23_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=24, version=0)
class Microsoft_Windows_Servicing_24_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=26, version=0)
class Microsoft_Windows_Servicing_26_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=33, version=0)
class Microsoft_Windows_Servicing_33_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=34, version=0)
class Microsoft_Windows_Servicing_34_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=35, version=0)
class Microsoft_Windows_Servicing_35_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=37, version=0)
class Microsoft_Windows_Servicing_37_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=38, version=0)
class Microsoft_Windows_Servicing_38_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=39, version=0)
class Microsoft_Windows_Servicing_39_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=40, version=0)
class Microsoft_Windows_Servicing_40_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=41, version=0)
class Microsoft_Windows_Servicing_41_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=42, version=0)
class Microsoft_Windows_Servicing_42_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=43, version=0)
class Microsoft_Windows_Servicing_43_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=44, version=0)
class Microsoft_Windows_Servicing_44_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=45, version=0)
class Microsoft_Windows_Servicing_45_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=46, version=0)
class Microsoft_Windows_Servicing_46_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=47, version=0)
class Microsoft_Windows_Servicing_47_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=48, version=0)
class Microsoft_Windows_Servicing_48_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=49, version=0)
class Microsoft_Windows_Servicing_49_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=50, version=0)
class Microsoft_Windows_Servicing_50_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=51, version=0)
class Microsoft_Windows_Servicing_51_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=52, version=0)
class Microsoft_Windows_Servicing_52_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=53, version=0)
class Microsoft_Windows_Servicing_53_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=54, version=0)
class Microsoft_Windows_Servicing_54_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=55, version=0)
class Microsoft_Windows_Servicing_55_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=56, version=0)
class Microsoft_Windows_Servicing_56_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=57, version=0)
class Microsoft_Windows_Servicing_57_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=58, version=0)
class Microsoft_Windows_Servicing_58_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=59, version=0)
class Microsoft_Windows_Servicing_59_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=60, version=0)
class Microsoft_Windows_Servicing_60_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=61, version=0)
class Microsoft_Windows_Servicing_61_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=62, version=0)
class Microsoft_Windows_Servicing_62_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=63, version=0)
class Microsoft_Windows_Servicing_63_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=64, version=0)
class Microsoft_Windows_Servicing_64_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=65, version=0)
class Microsoft_Windows_Servicing_65_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=66, version=0)
class Microsoft_Windows_Servicing_66_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=67, version=0)
class Microsoft_Windows_Servicing_67_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=68, version=0)
class Microsoft_Windows_Servicing_68_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=69, version=0)
class Microsoft_Windows_Servicing_69_0(Etw):
    pattern = Struct(
        "DescString" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=70, version=0)
class Microsoft_Windows_Servicing_70_0(Etw):
    pattern = Struct(
        "DescString" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=71, version=0)
class Microsoft_Windows_Servicing_71_0(Etw):
    pattern = Struct(
        "DescString" / WString,
        "Phase" / Int32ul,
        "Mode" / Int32ul,
        "PrevComponent" / WString,
        "NewComponent" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=72, version=0)
class Microsoft_Windows_Servicing_72_0(Etw):
    pattern = Struct(
        "DescString" / WString,
        "InstallerEndEvent" / Int64ul
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=73, version=0)
class Microsoft_Windows_Servicing_73_0(Etw):
    pattern = Struct(
        "DescString" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=74, version=0)
class Microsoft_Windows_Servicing_74_0(Etw):
    pattern = Struct(
        "DescString" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=75, version=0)
class Microsoft_Windows_Servicing_75_0(Etw):
    pattern = Struct(
        "DescString" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=76, version=0)
class Microsoft_Windows_Servicing_76_0(Etw):
    pattern = Struct(
        "DescString" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=77, version=0)
class Microsoft_Windows_Servicing_77_0(Etw):
    pattern = Struct(
        "DescString" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=78, version=0)
class Microsoft_Windows_Servicing_78_0(Etw):
    pattern = Struct(
        "DescString" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=79, version=0)
class Microsoft_Windows_Servicing_79_0(Etw):
    pattern = Struct(
        "DescString" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=80, version=0)
class Microsoft_Windows_Servicing_80_0(Etw):
    pattern = Struct(
        "DescString" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=82, version=0)
class Microsoft_Windows_Servicing_82_0(Etw):
    pattern = Struct(
        "DescString" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=83, version=0)
class Microsoft_Windows_Servicing_83_0(Etw):
    pattern = Struct(
        "DescString" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=84, version=0)
class Microsoft_Windows_Servicing_84_0(Etw):
    pattern = Struct(
        "DescString" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=85, version=0)
class Microsoft_Windows_Servicing_85_0(Etw):
    pattern = Struct(
        "DescString" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=86, version=0)
class Microsoft_Windows_Servicing_86_0(Etw):
    pattern = Struct(
        "DescString" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=87, version=0)
class Microsoft_Windows_Servicing_87_0(Etw):
    pattern = Struct(
        "DescString" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=88, version=0)
class Microsoft_Windows_Servicing_88_0(Etw):
    pattern = Struct(
        "DescString" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=89, version=0)
class Microsoft_Windows_Servicing_89_0(Etw):
    pattern = Struct(
        "DescString" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=90, version=0)
class Microsoft_Windows_Servicing_90_0(Etw):
    pattern = Struct(
        "DescString" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=91, version=0)
class Microsoft_Windows_Servicing_91_0(Etw):
    pattern = Struct(
        "DescString" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=92, version=0)
class Microsoft_Windows_Servicing_92_0(Etw):
    pattern = Struct(
        "DescString" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=93, version=0)
class Microsoft_Windows_Servicing_93_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=94, version=0)
class Microsoft_Windows_Servicing_94_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=95, version=0)
class Microsoft_Windows_Servicing_95_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=96, version=0)
class Microsoft_Windows_Servicing_96_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=97, version=0)
class Microsoft_Windows_Servicing_97_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=98, version=0)
class Microsoft_Windows_Servicing_98_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=99, version=0)
class Microsoft_Windows_Servicing_99_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=100, version=0)
class Microsoft_Windows_Servicing_100_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=101, version=0)
class Microsoft_Windows_Servicing_101_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=102, version=0)
class Microsoft_Windows_Servicing_102_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=103, version=0)
class Microsoft_Windows_Servicing_103_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=104, version=0)
class Microsoft_Windows_Servicing_104_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=105, version=0)
class Microsoft_Windows_Servicing_105_0(Etw):
    pattern = Struct(
        "EventReport" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=1000, version=0)
class Microsoft_Windows_Servicing_1000_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=1001, version=0)
class Microsoft_Windows_Servicing_1001_0(Etw):
    pattern = Struct(
        "updateName" / WString,
        "identifier" / WString,
        "releaseType" / WString,
        "updateStateLoc" / WString,
        "updateState" / WString,
        "packageAssembly" / WString,
        "updateDisplayName" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=1002, version=0)
class Microsoft_Windows_Servicing_1002_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=1003, version=0)
class Microsoft_Windows_Servicing_1003_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=1004, version=0)
class Microsoft_Windows_Servicing_1004_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=1005, version=0)
class Microsoft_Windows_Servicing_1005_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=1006, version=0)
class Microsoft_Windows_Servicing_1006_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=1007, version=0)
class Microsoft_Windows_Servicing_1007_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=1008, version=0)
class Microsoft_Windows_Servicing_1008_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=1009, version=0)
class Microsoft_Windows_Servicing_1009_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=1010, version=0)
class Microsoft_Windows_Servicing_1010_0(Etw):
    pattern = Struct(
        "updateName" / WString,
        "identifier" / WString,
        "releaseType" / WString,
        "updateStateLoc" / WString,
        "updateState" / WString,
        "packageAssembly" / WString,
        "updateDisplayName" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=1011, version=0)
class Microsoft_Windows_Servicing_1011_0(Etw):
    pattern = Struct(
        "updateName" / WString,
        "identifier" / WString,
        "releaseType" / WString,
        "updateStateLoc" / WString,
        "updateState" / WString,
        "packageAssembly" / WString,
        "updateDisplayName" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=1012, version=0)
class Microsoft_Windows_Servicing_1012_0(Etw):
    pattern = Struct(
        "updateName" / WString,
        "identifier" / WString,
        "releaseType" / WString,
        "updateStateLoc" / WString,
        "updateState" / WString,
        "packageAssembly" / WString,
        "updateDisplayName" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=1013, version=0)
class Microsoft_Windows_Servicing_1013_0(Etw):
    pattern = Struct(
        "detectionType" / Int32ul,
        "triggerType" / Int32ul
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=1014, version=0)
class Microsoft_Windows_Servicing_1014_0(Etw):
    pattern = Struct(
        "errorCode" / WString,
        "repaired" / Int32ul,
        "totalCorruption" / Int32ul
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=1015, version=0)
class Microsoft_Windows_Servicing_1015_0(Etw):
    pattern = Struct(
        "errorCode" / WString,
        "repaired" / Int32ul,
        "totalCorruption" / Int32ul
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4371, version=0)
class Microsoft_Windows_Servicing_4371_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "initialPackageStateLoc" / WString,
        "initialPackageState" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "client" / WString,
        "supportInformation" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4372, version=0)
class Microsoft_Windows_Servicing_4372_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4373, version=0)
class Microsoft_Windows_Servicing_4373_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4374, version=0)
class Microsoft_Windows_Servicing_4374_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4375, version=0)
class Microsoft_Windows_Servicing_4375_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4376, version=0)
class Microsoft_Windows_Servicing_4376_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4383, version=0)
class Microsoft_Windows_Servicing_4383_0(Etw):
    pattern = Struct(
        "updateName" / WString,
        "identifier" / WString,
        "releaseType" / WString,
        "updateStateLoc" / WString,
        "updateState" / WString,
        "packageAssembly" / WString,
        "updateDisplayName" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4385, version=0)
class Microsoft_Windows_Servicing_4385_0(Etw):
    pattern = Struct(
        "updateName" / WString,
        "identifier" / WString,
        "releaseType" / WString,
        "updateStateLoc" / WString,
        "updateState" / WString,
        "packageAssembly" / WString,
        "updateDisplayName" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4386, version=0)
class Microsoft_Windows_Servicing_4386_0(Etw):
    pattern = Struct(
        "updateName" / WString,
        "identifier" / WString,
        "releaseType" / WString,
        "updateStateLoc" / WString,
        "updateState" / WString,
        "packageAssembly" / WString,
        "updateDisplayName" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4400, version=0)
class Microsoft_Windows_Servicing_4400_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4401, version=0)
class Microsoft_Windows_Servicing_4401_0(Etw):
    pattern = Struct(
        "updateName" / WString,
        "identifier" / WString,
        "releaseType" / WString,
        "updateStateLoc" / WString,
        "updateState" / WString,
        "packageAssembly" / WString,
        "updateDisplayName" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4402, version=0)
class Microsoft_Windows_Servicing_4402_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4403, version=0)
class Microsoft_Windows_Servicing_4403_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4404, version=0)
class Microsoft_Windows_Servicing_4404_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4405, version=0)
class Microsoft_Windows_Servicing_4405_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4406, version=0)
class Microsoft_Windows_Servicing_4406_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4407, version=0)
class Microsoft_Windows_Servicing_4407_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4408, version=0)
class Microsoft_Windows_Servicing_4408_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4409, version=0)
class Microsoft_Windows_Servicing_4409_0(Etw):
    pattern = Struct(
        "identifier" / WString,
        "releaseType" / WString,
        "packageStateLoc" / WString,
        "packageState" / WString,
        "packageAssembly" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString,
        "missingElements" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4416, version=0)
class Microsoft_Windows_Servicing_4416_0(Etw):
    pattern = Struct(
        "updateName" / WString,
        "identifier" / WString,
        "releaseType" / WString,
        "updateStateLoc" / WString,
        "updateState" / WString,
        "packageAssembly" / WString,
        "updateDisplayName" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4417, version=0)
class Microsoft_Windows_Servicing_4417_0(Etw):
    pattern = Struct(
        "updateName" / WString,
        "identifier" / WString,
        "releaseType" / WString,
        "updateStateLoc" / WString,
        "updateState" / WString,
        "packageAssembly" / WString,
        "updateDisplayName" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString
    )


@declare(guid=guid("bd12f3b8-fc40-4a61-a307-b7a013a069c1"), event_id=4418, version=0)
class Microsoft_Windows_Servicing_4418_0(Etw):
    pattern = Struct(
        "updateName" / WString,
        "identifier" / WString,
        "releaseType" / WString,
        "updateStateLoc" / WString,
        "updateState" / WString,
        "packageAssembly" / WString,
        "updateDisplayName" / WString,
        "operation" / WString,
        "operationCompleted" / WString,
        "errorCode" / WString,
        "rebootOption" / WString
    )

