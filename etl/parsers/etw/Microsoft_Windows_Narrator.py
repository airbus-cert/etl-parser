# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Narrator
GUID : 835b79e2-e76a-44c4-9885-26ad122d3b4d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=5, version=0)
class Microsoft_Windows_Narrator_5_0(Etw):
    pattern = Struct(
        "Channel" / Int32sl,
        "SpokenText" / WString
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=6, version=0)
class Microsoft_Windows_Narrator_6_0(Etw):
    pattern = Struct(
        "Channel" / Int32sl,
        "SpokenText" / WString
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=7, version=0)
class Microsoft_Windows_Narrator_7_0(Etw):
    pattern = Struct(
        "CancelledMessage" / WString
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=9, version=0)
class Microsoft_Windows_Narrator_9_0(Etw):
    pattern = Struct(
        "NewMode" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=11, version=0)
class Microsoft_Windows_Narrator_11_0(Etw):
    pattern = Struct(
        "Command" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=12, version=0)
class Microsoft_Windows_Narrator_12_0(Etw):
    pattern = Struct(
        "Command" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=15, version=0)
class Microsoft_Windows_Narrator_15_0(Etw):
    pattern = Struct(
        "AutomationContext" / WString
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=17, version=0)
class Microsoft_Windows_Narrator_17_0(Etw):
    pattern = Struct(
        "AutomationContext" / WString
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=21, version=0)
class Microsoft_Windows_Narrator_21_0(Etw):
    pattern = Struct(
        "SpokenText" / WString
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=25, version=0)
class Microsoft_Windows_Narrator_25_0(Etw):
    pattern = Struct(
        "Priority" / Int32sl,
        "EventClass" / WString,
        "Parameter" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=31, version=0)
class Microsoft_Windows_Narrator_31_0(Etw):
    pattern = Struct(
        "IsWindowActive" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=35, version=0)
class Microsoft_Windows_Narrator_35_0(Etw):
    pattern = Struct(
        "CurrentOSKState" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=37, version=0)
class Microsoft_Windows_Narrator_37_0(Etw):
    pattern = Struct(
        "CurrentOrientation" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=41, version=0)
class Microsoft_Windows_Narrator_41_0(Etw):
    pattern = Struct(
        "CurrentState" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=44, version=0)
class Microsoft_Windows_Narrator_44_0(Etw):
    pattern = Struct(
        "EventCancelled" / Int32sl,
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=45, version=0)
class Microsoft_Windows_Narrator_45_0(Etw):
    pattern = Struct(
        "SeletionModeEnabled" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=47, version=0)
class Microsoft_Windows_Narrator_47_0(Etw):
    pattern = Struct(
        "Command" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=48, version=0)
class Microsoft_Windows_Narrator_48_0(Etw):
    pattern = Struct(
        "Command" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=50, version=0)
class Microsoft_Windows_Narrator_50_0(Etw):
    pattern = Struct(
        "SoundResourceId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=51, version=0)
class Microsoft_Windows_Narrator_51_0(Etw):
    pattern = Struct(
        "EventType" / WString,
        "EventId" / Int32sl,
        "Priority" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=52, version=0)
class Microsoft_Windows_Narrator_52_0(Etw):
    pattern = Struct(
        "EventType" / WString,
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=53, version=0)
class Microsoft_Windows_Narrator_53_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=54, version=0)
class Microsoft_Windows_Narrator_54_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=55, version=0)
class Microsoft_Windows_Narrator_55_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=56, version=0)
class Microsoft_Windows_Narrator_56_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=57, version=0)
class Microsoft_Windows_Narrator_57_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=58, version=0)
class Microsoft_Windows_Narrator_58_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=59, version=0)
class Microsoft_Windows_Narrator_59_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=60, version=0)
class Microsoft_Windows_Narrator_60_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=61, version=0)
class Microsoft_Windows_Narrator_61_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=62, version=0)
class Microsoft_Windows_Narrator_62_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=63, version=0)
class Microsoft_Windows_Narrator_63_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=64, version=0)
class Microsoft_Windows_Narrator_64_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=65, version=0)
class Microsoft_Windows_Narrator_65_0(Etw):
    pattern = Struct(
        "WasCanceled" / Int32sl,
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=66, version=0)
class Microsoft_Windows_Narrator_66_0(Etw):
    pattern = Struct(
        "EventType" / WString,
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=67, version=0)
class Microsoft_Windows_Narrator_67_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=68, version=0)
class Microsoft_Windows_Narrator_68_0(Etw):
    pattern = Struct(
        "SpokenText" / WString
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=69, version=0)
class Microsoft_Windows_Narrator_69_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=70, version=0)
class Microsoft_Windows_Narrator_70_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=71, version=0)
class Microsoft_Windows_Narrator_71_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=72, version=0)
class Microsoft_Windows_Narrator_72_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=74, version=0)
class Microsoft_Windows_Narrator_74_0(Etw):
    pattern = Struct(
        "ElementAddress" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=75, version=0)
class Microsoft_Windows_Narrator_75_0(Etw):
    pattern = Struct(
        "ElementAddress" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=76, version=0)
class Microsoft_Windows_Narrator_76_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=77, version=0)
class Microsoft_Windows_Narrator_77_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=78, version=0)
class Microsoft_Windows_Narrator_78_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=79, version=0)
class Microsoft_Windows_Narrator_79_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=104, version=0)
class Microsoft_Windows_Narrator_104_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=105, version=0)
class Microsoft_Windows_Narrator_105_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=106, version=0)
class Microsoft_Windows_Narrator_106_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=107, version=0)
class Microsoft_Windows_Narrator_107_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=108, version=0)
class Microsoft_Windows_Narrator_108_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=109, version=0)
class Microsoft_Windows_Narrator_109_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=110, version=0)
class Microsoft_Windows_Narrator_110_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=111, version=0)
class Microsoft_Windows_Narrator_111_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=112, version=0)
class Microsoft_Windows_Narrator_112_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=113, version=0)
class Microsoft_Windows_Narrator_113_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=114, version=0)
class Microsoft_Windows_Narrator_114_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=115, version=0)
class Microsoft_Windows_Narrator_115_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=118, version=0)
class Microsoft_Windows_Narrator_118_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=119, version=0)
class Microsoft_Windows_Narrator_119_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=123, version=0)
class Microsoft_Windows_Narrator_123_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=124, version=0)
class Microsoft_Windows_Narrator_124_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=127, version=0)
class Microsoft_Windows_Narrator_127_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=128, version=0)
class Microsoft_Windows_Narrator_128_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=129, version=0)
class Microsoft_Windows_Narrator_129_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=130, version=0)
class Microsoft_Windows_Narrator_130_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=131, version=0)
class Microsoft_Windows_Narrator_131_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=132, version=0)
class Microsoft_Windows_Narrator_132_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=133, version=0)
class Microsoft_Windows_Narrator_133_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=134, version=0)
class Microsoft_Windows_Narrator_134_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=135, version=0)
class Microsoft_Windows_Narrator_135_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=136, version=0)
class Microsoft_Windows_Narrator_136_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=137, version=0)
class Microsoft_Windows_Narrator_137_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=138, version=0)
class Microsoft_Windows_Narrator_138_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=139, version=0)
class Microsoft_Windows_Narrator_139_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=140, version=0)
class Microsoft_Windows_Narrator_140_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=141, version=0)
class Microsoft_Windows_Narrator_141_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=142, version=0)
class Microsoft_Windows_Narrator_142_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=143, version=0)
class Microsoft_Windows_Narrator_143_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=144, version=0)
class Microsoft_Windows_Narrator_144_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=155, version=0)
class Microsoft_Windows_Narrator_155_0(Etw):
    pattern = Struct(
        "AutomationContext" / WString
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=156, version=0)
class Microsoft_Windows_Narrator_156_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=157, version=0)
class Microsoft_Windows_Narrator_157_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=158, version=0)
class Microsoft_Windows_Narrator_158_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=159, version=0)
class Microsoft_Windows_Narrator_159_0(Etw):
    pattern = Struct(
        "EventId" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=162, version=0)
class Microsoft_Windows_Narrator_162_0(Etw):
    pattern = Struct(
        "MessageType" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=163, version=0)
class Microsoft_Windows_Narrator_163_0(Etw):
    pattern = Struct(
        "MessageType" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=170, version=0)
class Microsoft_Windows_Narrator_170_0(Etw):
    pattern = Struct(
        "ElementAddress" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=171, version=0)
class Microsoft_Windows_Narrator_171_0(Etw):
    pattern = Struct(
        "ElementAddress" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=174, version=0)
class Microsoft_Windows_Narrator_174_0(Etw):
    pattern = Struct(
        "NarratorPerfScenario" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=175, version=0)
class Microsoft_Windows_Narrator_175_0(Etw):
    pattern = Struct(
        "NarratorPerfScenario" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=177, version=0)
class Microsoft_Windows_Narrator_177_0(Etw):
    pattern = Struct(
        "IsElementInPeripheralUI" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=186, version=0)
class Microsoft_Windows_Narrator_186_0(Etw):
    pattern = Struct(
        "Command" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=187, version=0)
class Microsoft_Windows_Narrator_187_0(Etw):
    pattern = Struct(
        "Command" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=221, version=0)
class Microsoft_Windows_Narrator_221_0(Etw):
    pattern = Struct(
        "HitCount" / Int32sl,
        "MissCount" / Int32sl,
        "IgnoreCount" / Int32sl,
        "RemoveCount" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=229, version=0)
class Microsoft_Windows_Narrator_229_0(Etw):
    pattern = Struct(
        "GroupNumber" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=230, version=0)
class Microsoft_Windows_Narrator_230_0(Etw):
    pattern = Struct(
        "GroupNumber" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=232, version=0)
class Microsoft_Windows_Narrator_232_0(Etw):
    pattern = Struct(
        "NumberSegments" / Int32sl
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=238, version=0)
class Microsoft_Windows_Narrator_238_0(Etw):
    pattern = Struct(
        "EventType" / WString
    )


@declare(guid=guid("835b79e2-e76a-44c4-9885-26ad122d3b4d"), event_id=251, version=0)
class Microsoft_Windows_Narrator_251_0(Etw):
    pattern = Struct(
        "Trigger" / WString
    )

