# -*- coding: utf-8 -*-
"""
Microsoft-WindowsPhone-ConfigManager2
GUID : 2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=1, version=0)
class Microsoft_WindowsPhone_ConfigManager2_1_0(Etw):
    pattern = Struct(
        "URI" / WString,
        "URICHILD" / WString,
        "NodeOptions" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=3, version=0)
class Microsoft_WindowsPhone_ConfigManager2_3_0(Etw):
    pattern = Struct(
        "URI1" / WString,
        "URI2" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=5, version=0)
class Microsoft_WindowsPhone_ConfigManager2_5_0(Etw):
    pattern = Struct(
        "StringOne" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=7, version=0)
class Microsoft_WindowsPhone_ConfigManager2_7_0(Etw):
    pattern = Struct(
        "StringOne" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=9, version=0)
class Microsoft_WindowsPhone_ConfigManager2_9_0(Etw):
    pattern = Struct(
        "Property" / Guid,
        "Value" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=11, version=0)
class Microsoft_WindowsPhone_ConfigManager2_11_0(Etw):
    pattern = Struct(
        "Property" / Guid,
        "Value" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=13, version=0)
class Microsoft_WindowsPhone_ConfigManager2_13_0(Etw):
    pattern = Struct(
        "URI" / WString,
        "NodeOptions" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=15, version=0)
class Microsoft_WindowsPhone_ConfigManager2_15_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=17, version=0)
class Microsoft_WindowsPhone_ConfigManager2_17_0(Etw):
    pattern = Struct(
        "StringOne" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=19, version=0)
class Microsoft_WindowsPhone_ConfigManager2_19_0(Etw):
    pattern = Struct(
        "StringOne" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=21, version=0)
class Microsoft_WindowsPhone_ConfigManager2_21_0(Etw):
    pattern = Struct(
        "Guid" / Guid,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=23, version=0)
class Microsoft_WindowsPhone_ConfigManager2_23_0(Etw):
    pattern = Struct(
        "PropCount" / Int32sl,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=25, version=0)
class Microsoft_WindowsPhone_ConfigManager2_25_0(Etw):
    pattern = Struct(
        "ChildCount" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=26, version=0)
class Microsoft_WindowsPhone_ConfigManager2_26_0(Etw):
    pattern = Struct(
        "CmdType" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=27, version=0)
class Microsoft_WindowsPhone_ConfigManager2_27_0(Etw):
    pattern = Struct(
        "CmdType" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=28, version=0)
class Microsoft_WindowsPhone_ConfigManager2_28_0(Etw):
    pattern = Struct(
        "CmdType" / Int32ul,
        "IsRecovery" / Int8ul,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=29, version=0)
class Microsoft_WindowsPhone_ConfigManager2_29_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=30, version=0)
class Microsoft_WindowsPhone_ConfigManager2_30_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=31, version=0)
class Microsoft_WindowsPhone_ConfigManager2_31_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=32, version=0)
class Microsoft_WindowsPhone_ConfigManager2_32_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=50, version=0)
class Microsoft_WindowsPhone_ConfigManager2_50_0(Etw):
    pattern = Struct(
        "URI" / WString,
        "NodeOptions" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=51, version=0)
class Microsoft_WindowsPhone_ConfigManager2_51_0(Etw):
    pattern = Struct(
        "Notification" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=54, version=0)
class Microsoft_WindowsPhone_ConfigManager2_54_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=56, version=0)
class Microsoft_WindowsPhone_ConfigManager2_56_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=58, version=0)
class Microsoft_WindowsPhone_ConfigManager2_58_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=60, version=0)
class Microsoft_WindowsPhone_ConfigManager2_60_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=62, version=0)
class Microsoft_WindowsPhone_ConfigManager2_62_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=64, version=0)
class Microsoft_WindowsPhone_ConfigManager2_64_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=66, version=0)
class Microsoft_WindowsPhone_ConfigManager2_66_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=68, version=0)
class Microsoft_WindowsPhone_ConfigManager2_68_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=70, version=0)
class Microsoft_WindowsPhone_ConfigManager2_70_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=72, version=0)
class Microsoft_WindowsPhone_ConfigManager2_72_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=74, version=0)
class Microsoft_WindowsPhone_ConfigManager2_74_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=76, version=0)
class Microsoft_WindowsPhone_ConfigManager2_76_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=78, version=0)
class Microsoft_WindowsPhone_ConfigManager2_78_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=80, version=0)
class Microsoft_WindowsPhone_ConfigManager2_80_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=82, version=0)
class Microsoft_WindowsPhone_ConfigManager2_82_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=84, version=0)
class Microsoft_WindowsPhone_ConfigManager2_84_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=86, version=0)
class Microsoft_WindowsPhone_ConfigManager2_86_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=88, version=0)
class Microsoft_WindowsPhone_ConfigManager2_88_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=90, version=0)
class Microsoft_WindowsPhone_ConfigManager2_90_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=92, version=0)
class Microsoft_WindowsPhone_ConfigManager2_92_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=94, version=0)
class Microsoft_WindowsPhone_ConfigManager2_94_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=96, version=0)
class Microsoft_WindowsPhone_ConfigManager2_96_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=98, version=0)
class Microsoft_WindowsPhone_ConfigManager2_98_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=100, version=0)
class Microsoft_WindowsPhone_ConfigManager2_100_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=102, version=0)
class Microsoft_WindowsPhone_ConfigManager2_102_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=104, version=0)
class Microsoft_WindowsPhone_ConfigManager2_104_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=106, version=0)
class Microsoft_WindowsPhone_ConfigManager2_106_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=108, version=0)
class Microsoft_WindowsPhone_ConfigManager2_108_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=110, version=0)
class Microsoft_WindowsPhone_ConfigManager2_110_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=112, version=0)
class Microsoft_WindowsPhone_ConfigManager2_112_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=114, version=0)
class Microsoft_WindowsPhone_ConfigManager2_114_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=117, version=0)
class Microsoft_WindowsPhone_ConfigManager2_117_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=119, version=0)
class Microsoft_WindowsPhone_ConfigManager2_119_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=121, version=0)
class Microsoft_WindowsPhone_ConfigManager2_121_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=122, version=0)
class Microsoft_WindowsPhone_ConfigManager2_122_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=124, version=0)
class Microsoft_WindowsPhone_ConfigManager2_124_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=125, version=0)
class Microsoft_WindowsPhone_ConfigManager2_125_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=126, version=0)
class Microsoft_WindowsPhone_ConfigManager2_126_0(Etw):
    pattern = Struct(
        "URI" / WString,
        "NodeOptions" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=127, version=0)
class Microsoft_WindowsPhone_ConfigManager2_127_0(Etw):
    pattern = Struct(
        "URI" / WString,
        "URICHILD" / WString,
        "NodeOptions" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=128, version=0)
class Microsoft_WindowsPhone_ConfigManager2_128_0(Etw):
    pattern = Struct(
        "URI1" / WString,
        "URI2" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=129, version=0)
class Microsoft_WindowsPhone_ConfigManager2_129_0(Etw):
    pattern = Struct(
        "StringOne" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=130, version=0)
class Microsoft_WindowsPhone_ConfigManager2_130_0(Etw):
    pattern = Struct(
        "StringOne" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=131, version=0)
class Microsoft_WindowsPhone_ConfigManager2_131_0(Etw):
    pattern = Struct(
        "Property" / Guid,
        "Value" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=132, version=0)
class Microsoft_WindowsPhone_ConfigManager2_132_0(Etw):
    pattern = Struct(
        "Property" / Guid,
        "Value" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=133, version=0)
class Microsoft_WindowsPhone_ConfigManager2_133_0(Etw):
    pattern = Struct(
        "URI" / WString,
        "NodeOptions" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=134, version=0)
class Microsoft_WindowsPhone_ConfigManager2_134_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=135, version=0)
class Microsoft_WindowsPhone_ConfigManager2_135_0(Etw):
    pattern = Struct(
        "StringOne" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=136, version=0)
class Microsoft_WindowsPhone_ConfigManager2_136_0(Etw):
    pattern = Struct(
        "StringOne" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=137, version=0)
class Microsoft_WindowsPhone_ConfigManager2_137_0(Etw):
    pattern = Struct(
        "Guid" / Guid,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=138, version=0)
class Microsoft_WindowsPhone_ConfigManager2_138_0(Etw):
    pattern = Struct(
        "PropCount" / Int32sl,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=139, version=0)
class Microsoft_WindowsPhone_ConfigManager2_139_0(Etw):
    pattern = Struct(
        "ChildCount" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=140, version=0)
class Microsoft_WindowsPhone_ConfigManager2_140_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=141, version=0)
class Microsoft_WindowsPhone_ConfigManager2_141_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=142, version=0)
class Microsoft_WindowsPhone_ConfigManager2_142_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=143, version=0)
class Microsoft_WindowsPhone_ConfigManager2_143_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=144, version=0)
class Microsoft_WindowsPhone_ConfigManager2_144_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=145, version=0)
class Microsoft_WindowsPhone_ConfigManager2_145_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=146, version=0)
class Microsoft_WindowsPhone_ConfigManager2_146_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=147, version=0)
class Microsoft_WindowsPhone_ConfigManager2_147_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=148, version=0)
class Microsoft_WindowsPhone_ConfigManager2_148_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=149, version=0)
class Microsoft_WindowsPhone_ConfigManager2_149_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=150, version=0)
class Microsoft_WindowsPhone_ConfigManager2_150_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=151, version=0)
class Microsoft_WindowsPhone_ConfigManager2_151_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=152, version=0)
class Microsoft_WindowsPhone_ConfigManager2_152_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=153, version=0)
class Microsoft_WindowsPhone_ConfigManager2_153_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=154, version=0)
class Microsoft_WindowsPhone_ConfigManager2_154_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=155, version=0)
class Microsoft_WindowsPhone_ConfigManager2_155_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=156, version=0)
class Microsoft_WindowsPhone_ConfigManager2_156_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=157, version=0)
class Microsoft_WindowsPhone_ConfigManager2_157_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=158, version=0)
class Microsoft_WindowsPhone_ConfigManager2_158_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=159, version=0)
class Microsoft_WindowsPhone_ConfigManager2_159_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=160, version=0)
class Microsoft_WindowsPhone_ConfigManager2_160_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=161, version=0)
class Microsoft_WindowsPhone_ConfigManager2_161_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=162, version=0)
class Microsoft_WindowsPhone_ConfigManager2_162_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=163, version=0)
class Microsoft_WindowsPhone_ConfigManager2_163_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=164, version=0)
class Microsoft_WindowsPhone_ConfigManager2_164_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=165, version=0)
class Microsoft_WindowsPhone_ConfigManager2_165_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=166, version=0)
class Microsoft_WindowsPhone_ConfigManager2_166_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=167, version=0)
class Microsoft_WindowsPhone_ConfigManager2_167_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=168, version=0)
class Microsoft_WindowsPhone_ConfigManager2_168_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=169, version=0)
class Microsoft_WindowsPhone_ConfigManager2_169_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=170, version=0)
class Microsoft_WindowsPhone_ConfigManager2_170_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=171, version=0)
class Microsoft_WindowsPhone_ConfigManager2_171_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=172, version=0)
class Microsoft_WindowsPhone_ConfigManager2_172_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=173, version=0)
class Microsoft_WindowsPhone_ConfigManager2_173_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=174, version=0)
class Microsoft_WindowsPhone_ConfigManager2_174_0(Etw):
    pattern = Struct(
        "Notification" / Int32ul,
        "URI" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=175, version=0)
class Microsoft_WindowsPhone_ConfigManager2_175_0(Etw):
    pattern = Struct(
        "StringOne" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=176, version=0)
class Microsoft_WindowsPhone_ConfigManager2_176_0(Etw):
    pattern = Struct(
        "StringOne" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=177, version=0)
class Microsoft_WindowsPhone_ConfigManager2_177_0(Etw):
    pattern = Struct(
        "StringOne" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=178, version=0)
class Microsoft_WindowsPhone_ConfigManager2_178_0(Etw):
    pattern = Struct(
        "StringOne" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=179, version=0)
class Microsoft_WindowsPhone_ConfigManager2_179_0(Etw):
    pattern = Struct(
        "CmdType" / Int32ul,
        "TrackedURI" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=180, version=0)
class Microsoft_WindowsPhone_ConfigManager2_180_0(Etw):
    pattern = Struct(
        "CmdType" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=181, version=0)
class Microsoft_WindowsPhone_ConfigManager2_181_0(Etw):
    pattern = Struct(
        "CmdType" / Int32ul,
        "IsRecovery" / Int8ul,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=182, version=0)
class Microsoft_WindowsPhone_ConfigManager2_182_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=183, version=0)
class Microsoft_WindowsPhone_ConfigManager2_183_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=184, version=0)
class Microsoft_WindowsPhone_ConfigManager2_184_0(Etw):
    pattern = Struct(
        "hr1" / Int32ul,
        "hr2" / Int32ul,
        "hr3" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=185, version=0)
class Microsoft_WindowsPhone_ConfigManager2_185_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=186, version=0)
class Microsoft_WindowsPhone_ConfigManager2_186_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=187, version=0)
class Microsoft_WindowsPhone_ConfigManager2_187_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=188, version=0)
class Microsoft_WindowsPhone_ConfigManager2_188_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=189, version=0)
class Microsoft_WindowsPhone_ConfigManager2_189_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=190, version=0)
class Microsoft_WindowsPhone_ConfigManager2_190_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=191, version=0)
class Microsoft_WindowsPhone_ConfigManager2_191_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=192, version=0)
class Microsoft_WindowsPhone_ConfigManager2_192_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=193, version=0)
class Microsoft_WindowsPhone_ConfigManager2_193_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=194, version=0)
class Microsoft_WindowsPhone_ConfigManager2_194_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=195, version=0)
class Microsoft_WindowsPhone_ConfigManager2_195_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=196, version=0)
class Microsoft_WindowsPhone_ConfigManager2_196_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=200, version=0)
class Microsoft_WindowsPhone_ConfigManager2_200_0(Etw):
    pattern = Struct(
        "UriPath" / WString,
        "IsAllowed" / Int8ul,
        "Hresult" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=201, version=0)
class Microsoft_WindowsPhone_ConfigManager2_201_0(Etw):
    pattern = Struct(
        "UriPath" / WString,
        "IsAllowed" / Int8ul,
        "Hresult" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=202, version=0)
class Microsoft_WindowsPhone_ConfigManager2_202_0(Etw):
    pattern = Struct(
        "Ccmdtype" / Int32ul,
        "Resourceuri" / WString
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=203, version=0)
class Microsoft_WindowsPhone_ConfigManager2_203_0(Etw):
    pattern = Struct(
        "hr1" / Int32ul,
        "hr2" / Int32ul,
        "hr3" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=204, version=0)
class Microsoft_WindowsPhone_ConfigManager2_204_0(Etw):
    pattern = Struct(
        "StringOne" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=205, version=0)
class Microsoft_WindowsPhone_ConfigManager2_205_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e"), event_id=206, version=0)
class Microsoft_WindowsPhone_ConfigManager2_206_0(Etw):
    pattern = Struct(
        "StringOne" / WString,
        "Result" / Int32ul
    )

