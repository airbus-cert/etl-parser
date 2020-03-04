# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MediaFoundation-MFReadWrite
GUID : 4b7eac67-fc53-448c-a49d-7cc6db524da7
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=0, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_0_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "MajorType" / Guid,
        "Subtype" / Guid
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=1, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_1_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=2, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_2_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TimeFormat" / Guid,
        "VariantType" / Int32ul,
        "Position" / Int64ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=3, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_3_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=4, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_4_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "ControlFlags" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=5, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_5_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul,
        "ActualStreamIndex" / Int32ul,
        "StreamFlags" / Int32ul,
        "Sample" / Int64ul,
        "Timestamp" / Int64ul,
        "Duration" / Int64ul,
        "Size" / Int32ul,
        "Discontinuity" / Int8ul,
        "CleanPoint" / Int8ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=6, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_6_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=7, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_7_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=9, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_9_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "EventType" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=10, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_10_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "EventType" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=11, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_11_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=12, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_12_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "MFT" / Int64ul,
        "CLSID" / Guid,
        "vtable" / Int64ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=14, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_14_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=15, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_15_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "RequestCounter" / Int64ul,
        "StreamIndex" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=16, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_16_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "RequestCounter" / Int64ul,
        "StreamIndex" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=100, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_100_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "MajorType" / Guid,
        "Subtype" / Guid
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=101, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_101_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=102, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_102_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=103, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_103_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "Sample" / Int64ul,
        "Timestamp" / Int64ul,
        "Duration" / Int64ul,
        "Size" / Int32ul,
        "Discontinuity" / Int8ul,
        "CleanPoint" / Int8ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=104, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_104_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "Timestamp" / Int64ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=105, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_105_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "Context" / Int64ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=106, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_106_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "Context" / Int64ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=107, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_107_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "Sample" / Int64ul,
        "Timestamp" / Int64ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=108, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_108_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=109, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_109_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=110, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_110_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "EventType" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=111, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_111_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "EventType" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=112, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_112_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "Threshold" / Int32ul,
        "ClockTime" / Int64ul,
        "Timestamp" / Int64ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=113, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_113_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "Delay" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=114, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_114_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=115, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_115_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=116, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_116_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "OldState" / Int32ul,
        "NewState" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=117, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_117_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=118, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_118_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=200, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_200_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "Transform" / Int64ul,
        "Sample" / Int64ul,
        "Timestamp" / Int64ul,
        "Duration" / Int64ul,
        "Size" / Int32ul,
        "Discontinuity" / Int8ul,
        "CleanPoint" / Int8ul,
        "TransformType" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=201, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_201_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "Transform" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=202, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_202_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "Transform" / Int64ul,
        "OutputStreamIndex" / Int32ul,
        "Sample" / Int64ul,
        "Timestamp" / Int64ul,
        "Duration" / Int64ul,
        "Size" / Int32ul,
        "Discontinuity" / Int8ul,
        "CleanPoint" / Int8ul,
        "TransformType" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=203, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_203_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "Transform" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=204, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_204_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "Transform" / Int64ul,
        "Message" / Int32ul,
        "Param" / Int64ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=205, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_205_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "Transform" / Int64ul,
        "EventType" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=206, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_206_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "Transform" / Int64ul,
        "EventType" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=207, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_207_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "MFT" / Int64ul,
        "CLSID" / Guid,
        "vtable" / Int64ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=208, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_208_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "MFT" / Int64ul,
        "CLSID" / Guid,
        "vtable" / Int64ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=209, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_209_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "Transform" / Int64ul,
        "Sample" / Int64ul,
        "Timestamp" / Int64ul,
        "Duration" / Int64ul,
        "Size" / Int32ul,
        "Discontinuity" / Int8ul,
        "CleanPoint" / Int8ul,
        "TransformType" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=210, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_210_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "Transform" / Int64ul,
        "OutputStreamIndex" / Int32ul,
        "Sample" / Int64ul,
        "Timestamp" / Int64ul,
        "Duration" / Int64ul,
        "Size" / Int32ul,
        "Discontinuity" / Int8ul,
        "CleanPoint" / Int8ul,
        "TransformType" / Int32ul
    )


@declare(guid=guid("4b7eac67-fc53-448c-a49d-7cc6db524da7"), event_id=211, version=0)
class Microsoft_Windows_MediaFoundation_MFReadWrite_211_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TransformType" / Int32ul,
        "MediaType" / CString
    )

