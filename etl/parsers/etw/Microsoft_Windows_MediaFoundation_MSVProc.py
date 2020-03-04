# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MediaFoundation-MSVProc
GUID : a4112d1a-6dfa-476e-bb75-e350d24934e1
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a4112d1a-6dfa-476e-bb75-e350d24934e1"), event_id=100, version=0)
class Microsoft_Windows_MediaFoundation_MSVProc_100_0(Etw):
    pattern = Struct(
        "VideoDevice" / Int64ul,
        "VP" / Int64ul,
        "RateConversionIndex" / Int32ul,
        "PastFrames" / Int32ul
    )


@declare(guid=guid("a4112d1a-6dfa-476e-bb75-e350d24934e1"), event_id=101, version=0)
class Microsoft_Windows_MediaFoundation_MSVProc_101_0(Etw):
    pattern = Struct(
        "Sample" / Int64ul,
        "BufferIndex" / Int32ul,
        "hr" / Int32ul,
        "View" / Int64ul
    )


@declare(guid=guid("a4112d1a-6dfa-476e-bb75-e350d24934e1"), event_id=102, version=0)
class Microsoft_Windows_MediaFoundation_MSVProc_102_0(Etw):
    pattern = Struct(
        "Sample" / Int64ul,
        "BufferIndex" / Int32ul,
        "hr" / Int32ul,
        "View" / Int64ul
    )


@declare(guid=guid("a4112d1a-6dfa-476e-bb75-e350d24934e1"), event_id=103, version=0)
class Microsoft_Windows_MediaFoundation_MSVProc_103_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "InputSample" / Int64ul,
        "InputViewIndex" / Int32ul,
        "OutputSample" / Int64ul,
        "InputFrameOrField" / Int32ul,
        "OutputIndex" / Int32ul,
        "OutputFrame" / Int32ul,
        "SrcWidth" / Int32sl,
        "SrcHeight" / Int32sl,
        "DestWidth" / Int32sl,
        "DestHeight" / Int32sl,
        "SourceFormat" / Int32ul,
        "DestFormat" / Int32ul,
        "Rotation" / Int32ul,
        "Mirrored" / Int32ul,
        "MaxLuminanceIn" / Int32ul,
        "MaxLuminanceOut" / Int32ul
    )


@declare(guid=guid("a4112d1a-6dfa-476e-bb75-e350d24934e1"), event_id=104, version=0)
class Microsoft_Windows_MediaFoundation_MSVProc_104_0(Etw):
    pattern = Struct(
        "OutputSample" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a4112d1a-6dfa-476e-bb75-e350d24934e1"), event_id=105, version=0)
class Microsoft_Windows_MediaFoundation_MSVProc_105_0(Etw):
    pattern = Struct(
        "MSVProcObj" / Int64ul
    )


@declare(guid=guid("a4112d1a-6dfa-476e-bb75-e350d24934e1"), event_id=106, version=0)
class Microsoft_Windows_MediaFoundation_MSVProc_106_0(Etw):
    pattern = Struct(
        "MSVProcObj" / Int64ul
    )


@declare(guid=guid("a4112d1a-6dfa-476e-bb75-e350d24934e1"), event_id=107, version=0)
class Microsoft_Windows_MediaFoundation_MSVProc_107_0(Etw):
    pattern = Struct(
        "MSVProcObj" / Int64ul
    )


@declare(guid=guid("a4112d1a-6dfa-476e-bb75-e350d24934e1"), event_id=108, version=0)
class Microsoft_Windows_MediaFoundation_MSVProc_108_0(Etw):
    pattern = Struct(
        "MSVProcObj" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a4112d1a-6dfa-476e-bb75-e350d24934e1"), event_id=109, version=0)
class Microsoft_Windows_MediaFoundation_MSVProc_109_0(Etw):
    pattern = Struct(
        "MSVProcObj" / Int64ul
    )


@declare(guid=guid("a4112d1a-6dfa-476e-bb75-e350d24934e1"), event_id=110, version=0)
class Microsoft_Windows_MediaFoundation_MSVProc_110_0(Etw):
    pattern = Struct(
        "MSVProcObj" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a4112d1a-6dfa-476e-bb75-e350d24934e1"), event_id=111, version=0)
class Microsoft_Windows_MediaFoundation_MSVProc_111_0(Etw):
    pattern = Struct(
        "fourCCSrc" / Int32ul,
        "fourCCDst" / Int32ul
    )


@declare(guid=guid("a4112d1a-6dfa-476e-bb75-e350d24934e1"), event_id=113, version=0)
class Microsoft_Windows_MediaFoundation_MSVProc_113_0(Etw):
    pattern = Struct(
        "fourCC" / Int32ul,
        "srcWidth" / Int32ul,
        "srcHeight" / Int32ul,
        "dstWidth" / Int32ul,
        "dstHeight" / Int32ul
    )


@declare(guid=guid("a4112d1a-6dfa-476e-bb75-e350d24934e1"), event_id=115, version=0)
class Microsoft_Windows_MediaFoundation_MSVProc_115_0(Etw):
    pattern = Struct(
        "fourCC" / Int32ul,
        "Rotation" / Int32ul
    )


@declare(guid=guid("a4112d1a-6dfa-476e-bb75-e350d24934e1"), event_id=117, version=0)
class Microsoft_Windows_MediaFoundation_MSVProc_117_0(Etw):
    pattern = Struct(
        "fourCC" / Int32ul,
        "Mirror" / Int32ul
    )


@declare(guid=guid("a4112d1a-6dfa-476e-bb75-e350d24934e1"), event_id=119, version=0)
class Microsoft_Windows_MediaFoundation_MSVProc_119_0(Etw):
    pattern = Struct(
        "MSVProcObj" / Int64ul,
        "Context" / Int64ul,
        "uiInputViewCount" / Int32ul,
        "uiOutputViewCount" / Int32ul,
        "uiOutWidth" / Int32ul,
        "uiOutHeight" / Int32ul,
        "uiOffsetX" / Int32ul,
        "uiOffsetY" / Int32ul,
        "SourceFormat" / Int32ul,
        "DestFormat" / Int32ul,
        "Shader" / Int32ul,
        "lightLevelIn" / Int32ul,
        "lightLevelOut" / Int32ul
    )


@declare(guid=guid("a4112d1a-6dfa-476e-bb75-e350d24934e1"), event_id=120, version=0)
class Microsoft_Windows_MediaFoundation_MSVProc_120_0(Etw):
    pattern = Struct(
        "MSVProcObj" / Int64ul
    )


@declare(guid=guid("a4112d1a-6dfa-476e-bb75-e350d24934e1"), event_id=121, version=0)
class Microsoft_Windows_MediaFoundation_MSVProc_121_0(Etw):
    pattern = Struct(
        "MSVProcObj" / Int64ul,
        "RedPrimaryX" / Float32l,
        "RedPrimaryY" / Float32l,
        "GreenPrimaryX" / Float32l,
        "GreenPrimaryY" / Float32l,
        "BluePrimaryX" / Float32l,
        "BluePrimaryY" / Float32l,
        "WhitePrimaryX" / Float32l,
        "WhitePrimaryY" / Float32l,
        "MaxLuminance" / Int32ul,
        "MinLuminance" / Int32ul
    )


@declare(guid=guid("a4112d1a-6dfa-476e-bb75-e350d24934e1"), event_id=122, version=0)
class Microsoft_Windows_MediaFoundation_MSVProc_122_0(Etw):
    pattern = Struct(
        "MSVProcObj" / Int64ul,
        "RedPrimaryX" / Float32l,
        "RedPrimaryY" / Float32l,
        "GreenPrimaryX" / Float32l,
        "GreenPrimaryY" / Float32l,
        "BluePrimaryX" / Float32l,
        "BluePrimaryY" / Float32l,
        "WhitePrimaryX" / Float32l,
        "WhitePrimaryY" / Float32l,
        "MaxLuminance" / Int32ul,
        "MinLuminance" / Int32ul
    )


@declare(guid=guid("a4112d1a-6dfa-476e-bb75-e350d24934e1"), event_id=123, version=0)
class Microsoft_Windows_MediaFoundation_MSVProc_123_0(Etw):
    pattern = Struct(
        "fourCC" / Int32ul,
        "srcWidth" / Int32ul,
        "srcHeight" / Int32ul,
        "dstWidth" / Int32ul,
        "dstHeight" / Int32ul
    )

