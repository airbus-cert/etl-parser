# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MediaFoundation-Performance
GUID : f404b94e-27e0-4384-bfe8-1d8d390b0aa3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=3062, version=0)
class Microsoft_Windows_MediaFoundation_Performance_3062_0(Etw):
    pattern = Struct(
        "dwType" / Int32ul,
        "dwConfig" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=3063, version=0)
class Microsoft_Windows_MediaFoundation_Performance_3063_0(Etw):
    pattern = Struct(
        "dwScaleX" / Int32ul,
        "dwScaleY" / Int32ul,
        "dwWindowX" / Int32ul,
        "dwWindowY" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=3067, version=0)
class Microsoft_Windows_MediaFoundation_Performance_3067_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=3068, version=0)
class Microsoft_Windows_MediaFoundation_Performance_3068_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=3069, version=0)
class Microsoft_Windows_MediaFoundation_Performance_3069_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=3070, version=0)
class Microsoft_Windows_MediaFoundation_Performance_3070_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=3071, version=0)
class Microsoft_Windows_MediaFoundation_Performance_3071_0(Etw):
    pattern = Struct(
        "subtype" / Guid
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=3072, version=0)
class Microsoft_Windows_MediaFoundation_Performance_3072_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=3073, version=0)
class Microsoft_Windows_MediaFoundation_Performance_3073_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=3074, version=0)
class Microsoft_Windows_MediaFoundation_Performance_3074_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=3075, version=0)
class Microsoft_Windows_MediaFoundation_Performance_3075_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=3076, version=0)
class Microsoft_Windows_MediaFoundation_Performance_3076_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4000, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4000_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "objectType" / Int8ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4001, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4001_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "objectType" / Int8ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4002, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4002_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "byteCount" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4003, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4003_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "timestamp" / Int64sl,
        "targetTime" / Int64sl,
        "offset" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4004, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4004_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "targetQPC" / Int64sl,
        "submittedQPC" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4005, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4005_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "originalTargetQPC" / Int64sl,
        "targetQPC" / Int64sl,
        "targetAhead" / Int64sl,
        "submittedQPC" / Int64sl,
        "submittedAhead" / Int64sl,
        "now" / Int64sl,
        "presentTime" / Int64sl,
        "dwmFramesPresented" / Int64ul,
        "dwmRefreshStartCount" / Int64sl,
        "buffersEmpty" / Int32ul,
        "refreshFrameCount" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4006, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4006_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "cPresentCount" / Int32ul,
        "dwFlags" / Int32ul,
        "hrResult" / Int32ul,
        "llPresentTime" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4007, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4007_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "screenHeight" / Int32ul,
        "frameHeightx1000" / Int32sl,
        "frameRatex1000" / Int32sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4008, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4008_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hThread" / Int64ul,
        "sleepType" / Int8ul,
        "width" / Int32sl,
        "height" / Int32sl,
        "format" / Int32ul,
        "retryCount" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4009, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4009_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "dataType" / Int8ul,
        "sampleTime" / Int64sl,
        "bytesDropped" / Int32ul,
        "dropReasons" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4010, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4010_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "time" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4011, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4011_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "time" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4012, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4012_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "streamType" / Int8ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4013, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4013_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "stream" / Int64ul,
        "byteCount" / Int32ul,
        "type" / Bytes(lambda this: this.byteCount)
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4014, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4014_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "clsid" / Guid,
        "transform" / Int64ul,
        "userTransform" / Int8ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4015, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4015_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "objectCategory" / Int8ul,
        "stream" / Int64ul,
        "timestamp" / Int64sl,
        "clock" / Int64ul,
        "sample" / Int64ul,
        "bufferSize" / Int32ul,
        "sampleSize" / Int32ul,
        "duration" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4016, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4016_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "objectCategory" / Int8ul,
        "stream" / Int64ul,
        "timestamp" / Int64sl,
        "clock" / Int64ul,
        "sample" / Int64ul,
        "bufferSize" / Int32ul,
        "sampleSize" / Int32ul,
        "duration" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4017, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4017_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "objectCategory" / Int8ul,
        "stream" / Int64ul,
        "timestamp" / Int64sl,
        "clock" / Int64ul,
        "sample" / Int64ul,
        "bufferSize" / Int32ul,
        "sampleSize" / Int32ul,
        "duration" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4018, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4018_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "objectCategory" / Int8ul,
        "stream" / Int64ul,
        "timestamp" / Int64sl,
        "clock" / Int64ul,
        "sample" / Int64ul,
        "bufferSize" / Int32ul,
        "sampleSize" / Int32ul,
        "duration" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4019, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4019_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "objectCategory" / Int8ul,
        "sample" / Int64ul,
        "byteCount" / Int32ul,
        "sampleTime" / Int64sl,
        "processTime" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4020, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4020_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "objectCategory" / Int8ul,
        "sample" / Int64ul,
        "byteCount" / Int32ul,
        "sampleTime" / Int64sl,
        "processTime" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4021, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4021_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "objectCategory" / Int8ul,
        "sample" / Int64ul,
        "byteCount" / Int32ul,
        "sampleTime" / Int64sl,
        "processTime" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4022, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4022_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "processingType" / Int8sl,
        "event" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4023, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4023_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "handle" / Int64ul,
        "fileName" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4024, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4024_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "handle" / Int64ul,
        "offset" / Int64ul,
        "byteCount" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4025, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4025_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "handle" / Int64ul,
        "offset" / Int64ul,
        "byteCount" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4026, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4026_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "handle" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4027, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4027_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "handle" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4028, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4028_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "sampleTime" / Int64sl,
        "sampleDuration" / Int64sl,
        "clock" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4029, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4029_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "sampleTime" / Int64sl,
        "sampleDuration" / Int64sl,
        "clock" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4030, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4030_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "sampleTime" / Int64sl,
        "sampleDuration" / Int64sl,
        "clock" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4031, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4031_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "sampleTime" / Int64sl,
        "sampleDuration" / Int64sl,
        "clock" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4032, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4032_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "sampleTime" / Int64sl,
        "sampleDuration" / Int64sl,
        "clock" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4033, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4033_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "sampleTime" / Int64sl,
        "sampleDuration" / Int64sl,
        "clock" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4034, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4034_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "sampleTime" / Int64sl,
        "sampleDuration" / Int64sl,
        "clock" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4035, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4035_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "sampleTime" / Int64sl,
        "sampleDuration" / Int64sl,
        "clock" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4036, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4036_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "sampleTime" / Int64sl,
        "sampleDuration" / Int64sl,
        "clock" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4037, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4037_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "sampleTime" / Int64sl,
        "sampleDuration" / Int64sl,
        "clock" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4038, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4038_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "sampleTime" / Int64sl,
        "sampleDuration" / Int64sl,
        "clock" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4039, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4039_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "sampleTime" / Int64sl,
        "sampleDuration" / Int64sl,
        "clock" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4040, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4040_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "sampleTime" / Int64sl,
        "sampleDuration" / Int64sl,
        "clock" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4041, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4041_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "sampleTime" / Int64sl,
        "sampleDuration" / Int64sl,
        "clock" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4042, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4042_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "sampleTime" / Int64sl,
        "sampleDuration" / Int64sl,
        "clock" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4043, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4043_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "sampleTime" / Int64sl,
        "sampleDuration" / Int64sl,
        "clock" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4044, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4044_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "sampleTime" / Int64sl,
        "sampleDuration" / Int64sl,
        "clock" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4045, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4045_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "fullness" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4046, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4046_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4047, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4047_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4048, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4048_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4049, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4049_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4050, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4050_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4051, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4051_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4052, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4052_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4053, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4053_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "rtpSeq" / Int32ul,
        "packetNumber" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4054, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4054_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "rtpSeq" / Int32ul,
        "packetNumber" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4055, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4055_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "rtpSeq" / Int32ul,
        "packetNumber" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4056, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4056_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "segmentID" / Int32ul,
        "numberPending" / Int32ul,
        "time" / Int64sl,
        "sample" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4057, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4057_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "segmentID" / Int32ul,
        "numberPending" / Int32ul,
        "time" / Int64sl,
        "sample" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4058, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4058_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "segmentID" / Int32ul,
        "numberPending" / Int32ul,
        "time" / Int64sl,
        "sample" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4059, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4059_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "segmentID" / Int32ul,
        "numberPending" / Int32ul,
        "time" / Int64sl,
        "sample" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4060, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4060_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "segmentID" / Int32ul,
        "numberPending" / Int32ul,
        "time" / Int64sl,
        "sample" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4061, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4061_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "segmentID" / Int32ul,
        "numberPending" / Int32ul,
        "time" / Int64sl,
        "sample" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4062, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4062_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "segmentID" / Int32ul,
        "numberPending" / Int32ul,
        "time" / Int64sl,
        "sample" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4063, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4063_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "segmentID" / Int32ul,
        "numberPending" / Int32ul,
        "time" / Int64sl,
        "sample" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4064, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4064_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4065, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4065_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4066, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4066_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "bytes" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4067, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4067_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "bytes" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4068, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4068_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "bytes" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4069, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4069_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "bytes" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4070, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4070_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "bytes" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4071, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4071_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "bytes" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4072, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4072_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "bytes" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4073, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4073_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "bytes" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4074, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4074_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "bytes" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4075, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4075_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "bytes" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4076, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4076_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "bytes" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4077, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4077_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "bytes" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4078, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4078_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "bytes" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4079, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4079_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "bytes" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4080, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4080_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "bytes" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4081, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4081_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4082, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4082_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4083, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4083_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4084, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4084_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4085, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4085_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4086, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4086_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4087, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4087_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4088, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4088_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4089, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4089_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4090, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4090_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4091, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4091_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4092, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4092_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4093, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4093_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4094, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4094_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4095, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4095_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4096, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4096_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4097, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4097_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4098, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4098_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4099, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4099_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4100, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4100_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4101, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4101_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4102, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4102_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4103, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4103_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4104, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4104_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4105, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4105_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4106, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4106_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4107, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4107_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4108, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4108_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4109, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4109_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4110, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4110_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4111, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4111_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4112, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4112_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4113, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4113_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4114, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4114_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "guid" / Guid
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4115, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4115_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "arg1" / Int32ul,
        "arg2" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4116, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4116_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "arg1" / Int32ul,
        "arg2" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4117, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4117_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "arg1" / Int32ul,
        "arg2" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4118, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4118_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "arg1" / Int32ul,
        "arg2" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4119, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4119_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "arg1" / Int32ul,
        "arg2" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4120, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4120_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "arg1" / Int32ul,
        "arg2" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4121, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4121_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "arg1" / Int32ul,
        "arg2" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4122, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4122_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "arg1" / Int32ul,
        "arg2" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4123, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4123_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "arg1" / Int32ul,
        "arg2" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4124, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4124_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "arg1" / Int32ul,
        "arg2" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4125, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4125_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "arg1" / Int32ul,
        "arg2" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4126, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4126_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "arg1" / Int32ul,
        "arg2" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4127, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4127_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "arg1" / Int32ul,
        "arg2" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4128, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4128_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "arg1" / Int32ul,
        "arg2" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4129, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4129_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4130, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4130_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4131, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4131_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4132, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4132_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4133, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4133_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4134, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4134_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4135, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4135_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4136, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4136_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4137, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4137_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4138, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4138_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4139, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4139_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4140, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4140_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4141, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4141_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4142, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4142_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4143, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4143_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4144, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4144_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4145, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4145_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4146, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4146_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4147, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4147_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4148, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4148_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4149, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4149_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4150, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4150_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4151, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4151_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4152, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4152_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4153, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4153_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4154, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4154_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4155, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4155_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4156, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4156_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4157, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4157_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4158, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4158_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4159, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4159_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4160, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4160_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4161, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4161_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4162, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4162_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4163, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4163_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4164, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4164_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4165, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4165_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4166, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4166_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4167, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4167_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4168, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4168_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4169, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4169_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4170, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4170_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4171, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4171_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4172, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4172_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4173, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4173_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4174, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4174_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4175, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4175_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4176, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4176_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4177, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4177_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4178, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4178_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4179, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4179_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4180, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4180_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4181, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4181_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4182, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4182_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4183, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4183_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4184, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4184_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4185, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4185_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4186, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4186_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4187, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4187_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4188, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4188_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4189, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4189_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4190, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4190_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4191, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4191_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4192, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4192_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4193, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4193_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4194, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4194_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4195, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4195_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4196, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4196_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4197, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4197_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4198, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4198_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4199, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4199_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4200, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4200_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4201, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4201_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4202, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4202_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4203, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4203_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4204, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4204_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4205, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4205_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4206, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4206_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "arg" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4207, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4207_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4208, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4208_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4209, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4209_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4210, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4210_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4211, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4211_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4212, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4212_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4213, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4213_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4214, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4214_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4215, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4215_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4216, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4216_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4217, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4217_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4218, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4218_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4219, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4219_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4220, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4220_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4221, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4221_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4222, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4222_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4223, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4223_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4224, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4224_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4225, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4225_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4226, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4226_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4227, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4227_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4228, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4228_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4229, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4229_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4230, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4230_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "url" / WString,
        "objectCreated" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4231, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4231_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "state" / Int32ul,
        "context" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4232, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4232_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "state" / Int32ul,
        "context" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4233, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4233_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "state" / Int32ul,
        "context" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4234, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4234_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "state" / Int32ul,
        "context" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4235, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4235_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "state" / Int32ul,
        "context" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4236, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4236_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "state" / Int32ul,
        "context" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4237, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4237_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "state" / Int32ul,
        "context" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4238, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4238_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "state" / Int32ul,
        "context" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4239, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4239_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "state" / Int32ul,
        "context" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4240, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4240_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4241, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4241_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4242, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4242_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4243, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4243_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4244, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4244_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4245, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4245_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4246, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4246_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4247, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4247_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4248, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4248_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4249, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4249_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4250, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4250_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4251, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4251_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4252, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4252_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4253, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4253_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4254, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4254_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "eventType" / Int32ul,
        "time" / Int64sl,
        "parameter" / Int64ul,
        "url" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4255, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4255_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "eventType" / Int32ul,
        "time" / Int64sl,
        "parameter" / Int64ul,
        "url" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4256, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4256_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "eventType" / Int32ul,
        "time" / Int64sl,
        "parameter" / Int64ul,
        "url" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4257, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4257_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "eventType" / Int32ul,
        "time" / Int64sl,
        "parameter" / Int64ul,
        "url" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4258, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4258_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "eventType" / Int32ul,
        "time" / Int64sl,
        "parameter" / Int64ul,
        "url" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4259, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4259_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "eventType" / Int32ul,
        "time" / Int64sl,
        "parameter" / Int64ul,
        "url" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4260, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4260_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "eventType" / Int32ul,
        "time" / Int64sl,
        "parameter" / Int64ul,
        "url" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4261, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4261_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "knobID" / Int32ul,
        "previousLevel" / Int32ul,
        "newLevel" / Int32ul,
        "dropTime" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4262, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4262_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "knobID" / Int32ul,
        "previousLevel" / Int32ul,
        "newLevel" / Int32ul,
        "dropTime" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4263, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4263_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "knobID" / Int32ul,
        "previousLevel" / Int32ul,
        "newLevel" / Int32ul,
        "dropTime" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4264, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4264_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "eventType" / Int32ul,
        "time" / Int64sl,
        "parameter" / Int64ul,
        "url" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4265, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4265_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "eventType" / Int32ul,
        "time" / Int64sl,
        "parameter" / Int64ul,
        "url" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4266, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4266_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "eventType" / Int32ul,
        "time" / Int64sl,
        "parameter" / Int64ul,
        "url" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4267, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4267_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "eventType" / Int32ul,
        "time" / Int64sl,
        "parameter" / Int64ul,
        "url" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4268, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4268_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "eventType" / Int32ul,
        "time" / Int64sl,
        "parameter" / Int64ul,
        "url" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4269, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4269_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "eventType" / Int32ul,
        "time" / Int64sl,
        "parameter" / Int64ul,
        "url" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4270, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4270_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "eventType" / Int32ul,
        "time" / Int64sl,
        "parameter" / Int64ul,
        "url" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4271, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4271_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "eventType" / Int32ul,
        "time" / Int64sl,
        "parameter" / Int64ul,
        "url" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4272, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4272_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "originalTime" / Int64sl,
        "adjustment" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4273, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4273_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "originalTime" / Int64sl,
        "adjustment" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4274, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4274_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "sampleTime" / Int64sl,
        "sampleDuration" / Int64sl,
        "clockTime" / Int64sl,
        "hwnd" / Int64ul,
        "refreshRate" / Int32ul,
        "width" / Int32ul,
        "height" / Int32ul,
        "left" / Int32ul,
        "top" / Int32ul,
        "right" / Int32ul,
        "bottom" / Int32ul,
        "left1" / Int32ul,
        "top1" / Int32ul,
        "right1" / Int32ul,
        "bottom1" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4275, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4275_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "sample" / Int64ul,
        "sampleTime" / Int64sl,
        "sampleDuration" / Int64sl,
        "masterTime" / Int64sl,
        "deviceTime" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4276, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4276_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "propertyKey" / Int64ul,
        "propvariant" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4277, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4277_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "propertyKey" / Int64ul,
        "propvariant" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4278, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4278_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "propertyKey" / Int64ul,
        "propvariant" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4279, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4279_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "propertyKey" / Int64ul,
        "propvariant" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4280, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4280_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "propertyKey" / Int64ul,
        "propvariant" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4281, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4281_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "propertyKey" / Int64ul,
        "propvariant" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4282, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4282_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "propertyKey" / Int64ul,
        "propvariant" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4283, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4283_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "propertyKey" / Int64ul,
        "propvariant" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4284, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4284_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "propertyKey" / Int64ul,
        "propvariant" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4285, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4285_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "propertyKey" / Int64ul,
        "propvariant" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4286, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4286_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "propertyKey" / Int64ul,
        "propvariant" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4287, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4287_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul,
        "propertyKey" / Int64ul,
        "propvariant" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4288, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4288_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "streamNumber" / Int32ul,
        "sampleTime" / Int64sl,
        "sampleByteCount" / Int32ul,
        "packetNumber" / Int64sl,
        "packetSendTime" / Int64sl,
        "packetByteCount" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4289, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4289_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "streamNumber" / Int32ul,
        "sampleTime" / Int64sl,
        "sampleByteCount" / Int32ul,
        "packetNumber" / Int64sl,
        "packetSendTime" / Int64sl,
        "packetByteCount" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4290, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4290_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "streamNumber" / Int32ul,
        "sampleTime" / Int64sl,
        "sampleByteCount" / Int32ul,
        "packetNumber" / Int64sl,
        "packetSendTime" / Int64sl,
        "packetByteCount" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4291, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4291_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "eventTime" / Int64sl,
        "lateBy" / Int64sl,
        "callback" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4292, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4292_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4293, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4293_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4294, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4294_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4295, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4295_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4296, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4296_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4297, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4297_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4298, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4298_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4299, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4299_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4300, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4300_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4301, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4301_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4302, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4302_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4303, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4303_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4304, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4304_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4305, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4305_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4306, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4306_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4307, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4307_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4308, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4308_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4309, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4309_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4310, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4310_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4311, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4311_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4312, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4312_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4313, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4313_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4314, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4314_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4315, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4315_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4316, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4316_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4317, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4317_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4318, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4318_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4319, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4319_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4320, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4320_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4321, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4321_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4322, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4322_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4323, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4323_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4324, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4324_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4325, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4325_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4326, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4326_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4327, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4327_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4328, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4328_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4329, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4329_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4330, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4330_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4331, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4331_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4332, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4332_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4333, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4333_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4334, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4334_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4335, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4335_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4336, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4336_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4337, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4337_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4338, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4338_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4339, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4339_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4340, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4340_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4341, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4341_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4342, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4342_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4343, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4343_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4344, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4344_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4345, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4345_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4346, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4346_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4347, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4347_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4348, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4348_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4349, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4349_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4350, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4350_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4351, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4351_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4352, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4352_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4353, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4353_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4354, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4354_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4355, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4355_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4356, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4356_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4357, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4357_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4358, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4358_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4359, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4359_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4360, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4360_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4361, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4361_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4362, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4362_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4363, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4363_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4364, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4364_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4365, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4365_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4366, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4366_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4367, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4367_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4368, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4368_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4369, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4369_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4370, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4370_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4371, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4371_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4372, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4372_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4373, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4373_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4374, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4374_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4375, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4375_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4376, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4376_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4377, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4377_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4378, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4378_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4379, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4379_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4380, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4380_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4381, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4381_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4382, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4382_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4383, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4383_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4384, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4384_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4385, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4385_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int32ul,
        "bstr" / WString
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4386, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4386_0(Etw):
    pattern = Struct(
        "fileName" / WString,
        "graphType" / Int8ul,
        "lastHr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4387, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4387_0(Etw):
    pattern = Struct(
        "fileName" / WString,
        "graphType" / Int8ul,
        "lastHr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4388, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4388_0(Etw):
    pattern = Struct(
        "fileName" / WString,
        "graphType" / Int8ul,
        "lastHr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4389, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4389_0(Etw):
    pattern = Struct(
        "fileName" / WString,
        "graphType" / Int8ul,
        "lastHr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4390, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4390_0(Etw):
    pattern = Struct(
        "fileName" / WString,
        "graphType" / Int8ul,
        "lastHr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4391, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4391_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4392, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4392_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4393, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4393_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4394, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4394_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4395, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4395_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4396, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4396_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4397, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4397_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4398, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4398_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4399, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4399_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4400, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4400_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4401, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4401_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "initialOffset" / Int64sl,
        "finalOffset" / Int64sl,
        "bytesInCache" / Int32ul,
        "cacheSize" / Int32ul,
        "sectorSize" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4402, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4402_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "frameIndex" / Int32ul,
        "sampleTime" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4403, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4403_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "frameIndex" / Int32ul,
        "sampleTime" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4404, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4404_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "frameIndex" / Int32ul,
        "sampleTime" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4405, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4405_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "frameIndex" / Int32ul,
        "sampleTime" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4406, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4406_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "frameIndex" / Int32ul,
        "sampleTime" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4407, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4407_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "frameIndex" / Int32ul,
        "sampleTime" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4408, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4408_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4409, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4409_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "parameter" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4410, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4410_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "operation" / Int32sl,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4411, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4411_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "operation" / Int32sl,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4412, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4412_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "contentType" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4413, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4413_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "contentType" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4414, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4414_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "contentType" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4415, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4415_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "contentType" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4416, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4416_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "contentType" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4417, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4417_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "contentType" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4418, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4418_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "contentType" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4419, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4419_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "contentType" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4420, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4420_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "contentType" / Int32ul,
        "propertyKeyGuid" / Guid,
        "propertyKeyFmtId" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4421, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4421_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "contentType" / Int32ul,
        "propertyKeyGuid" / Guid,
        "propertyKeyFmtId" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4422, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4422_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "contentType" / Int32ul,
        "propertyKeyGuid" / Guid,
        "propertyKeyFmtId" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4423, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4423_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "contentType" / Int32ul,
        "propertyKeyGuid" / Guid,
        "propertyKeyFmtId" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4424, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4424_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "contentType" / Int32ul,
        "propertyKeyGuid" / Guid,
        "propertyKeyFmtId" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4425, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4425_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "contentType" / Int32ul,
        "propertyKeyGuid" / Guid,
        "propertyKeyFmtId" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4426, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4426_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "contentType" / Int32ul,
        "propertyKeyGuid" / Guid,
        "propertyKeyFmtId" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4427, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4427_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "contentType" / Int32ul,
        "propertyKeyGuid" / Guid,
        "propertyKeyFmtId" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4428, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4428_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4429, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4429_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4430, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4430_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4431, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4431_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4432, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4432_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "duration" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4433, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4433_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "duration" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4434, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4434_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "duration" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4437, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4437_0(Etw):
    pattern = Struct(
        "Buffer" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Format" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4438, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4438_0(Etw):
    pattern = Struct(
        "Buffer" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4439, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4439_0(Etw):
    pattern = Struct(
        "Buffer" / Int64ul,
        "GUID" / Guid,
        "Unknown" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4440, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4440_0(Etw):
    pattern = Struct(
        "Buffer" / Int64ul,
        "GUID" / Guid,
        "Unknown" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4441, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4441_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "Length" / Int32sl,
        "Type" / Int32sl,
        "Max" / Int32sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4442, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4442_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "Length" / Int32sl,
        "Type" / Int32sl,
        "Max" / Int32sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4443, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4443_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "ParentQueuePointer" / Int64ul,
        "Free" / Int32sl,
        "Allocated" / Int32sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4444, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4444_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "ParentQueuePointer" / Int64ul,
        "Free" / Int32sl,
        "Allocated" / Int32sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4445, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4445_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "Direction" / Int32sl,
        "Width" / Int32sl,
        "Height" / Int32sl,
        "Format" / Int32sl,
        "Length" / Int32sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4446, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4446_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "Direction" / Int32sl,
        "Width" / Int32sl,
        "Height" / Int32sl,
        "Format" / Int32sl,
        "Length" / Int32sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4447, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4447_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "contentType" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4448, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4448_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "contentType" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4449, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4449_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "contentType" / Int32ul,
        "bestFrameIndex" / Int32ul,
        "totalFrameDecoded" / Int32ul,
        "timeoutin100NS" / Int64ul,
        "isTimeout" / Int8ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4450, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4450_0(Etw):
    pattern = Struct(
        "Sample" / Int64ul,
        "StreamIndex" / Int32ul,
        "SampleTimestamp" / Int64ul,
        "AdjustedTimestamp" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4451, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4451_0(Etw):
    pattern = Struct(
        "Sample" / Int64ul,
        "StreamIndex" / Int32ul,
        "SampleTimestamp" / Int64ul,
        "AdjustedTimestamp" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4452, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4452_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4453, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4453_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4456, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4456_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "isLowLatency" / Int8ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4457, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4457_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "StreamIndex" / Int32ul,
        "SampleTimestamp" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4458, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4458_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "byteCount" / Int64ul,
        "totalByteCount" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4459, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4459_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "isRetryWorkItem" / Int8ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4460, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4460_0(Etw):
    pattern = Struct(
        "surface" / Int64ul,
        "uSubresource" / Int32ul,
        "Type" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4461, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4461_0(Etw):
    pattern = Struct(
        "surface" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4462, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4462_0(Etw):
    pattern = Struct(
        "isLosigHardwareResource" / Int8ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4463, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4463_0(Etw):
    pattern = Struct(
        "IsGoingOn" / Int8ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4464, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4464_0(Etw):
    pattern = Struct(
        "SoundLevel" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4465, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4465_0(Etw):
    pattern = Struct(
        "status" / Int8ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4466, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4466_0(Etw):
    pattern = Struct(
        "tag" / CString,
        "object" / Int64ul,
        "BufferDuration" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4467, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4467_0(Etw):
    pattern = Struct(
        "SrcPtr" / Int64ul,
        "DstPtr" / Int64ul,
        "Width" / Int32sl,
        "Height" / Int32sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4468, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4468_0(Etw):
    pattern = Struct(
        "SrcPtr" / Int64ul,
        "DstPtr" / Int64ul,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4469, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4469_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4470, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4470_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4471, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4471_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "dwStreamID" / Int32ul,
        "uiPinID" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4472, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4472_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Sample" / Int64ul,
        "Free" / Int32sl,
        "Allocated" / Int32sl,
        "MinSampleCount" / Int32sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4473, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4473_0(Etw):
    pattern = Struct(
        "SrcPtr" / Int64ul,
        "Count" / Int32ul,
        "DstPtr" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4474, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4474_0(Etw):
    pattern = Struct(
        "SrcPtr" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4475, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4475_0(Etw):
    pattern = Struct(
        "surface" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4476, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4476_0(Etw):
    pattern = Struct(
        "surface" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4500, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4500_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "PendingCount" / Int32sl,
        "BytesSent" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4501, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4501_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "PendingCount" / Int32sl,
        "BytesSent" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4502, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4502_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "PendingCount" / Int32sl,
        "BytesSent" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4503, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4503_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "PendingReceives" / Int32sl,
        "BytesReceived" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4504, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4504_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "PendingReceives" / Int32sl,
        "BytesReceived" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4505, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4505_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "PendingReceives" / Int32sl,
        "BytesReceived" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4600, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4600_0(Etw):
    pattern = Struct(
        "system" / Guid
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4601, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4601_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hrResult" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4602, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4602_0(Etw):
    pattern = Struct(
        "system" / Guid
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4603, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4603_0(Etw):
    pattern = Struct(
        "available" / Int8ul,
        "hrResult" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4604, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4604_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4605, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4605_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "functionID" / Int32ul,
        "inputbytes" / Int32ul,
        "outputbytes" / Int32ul,
        "msTransportTime" / Int32ul,
        "msExecutionTime" / Int32ul,
        "msTotal" / Int32ul,
        "hrResult" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4606, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4606_0(Etw):
    pattern = Struct(
        "system" / Guid,
        "manager" / Int64ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4607, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4607_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hrResult" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4608, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4608_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hrResult" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4612, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4612_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4614, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4614_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4615, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4615_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "bytestowrite" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4616, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4616_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "byteswritten" / Int32ul,
        "hrResult" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4617, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4617_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "StreamIndex" / Int32ul,
        "StreamType" / Int32ul,
        "timestamp" / Int64sl,
        "sample" / Int64ul,
        "duration" / Int64sl
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4618, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4618_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "StreamIndex" / Int32ul,
        "hrResult" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4619, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4619_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Index" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4620, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4620_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hrResult" / Int32ul
    )


@declare(guid=guid("f404b94e-27e0-4384-bfe8-1d8d390b0aa3"), event_id=4621, version=0)
class Microsoft_Windows_MediaFoundation_Performance_4621_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "StreamIndex" / Int32ul,
        "StreamType" / Int32ul,
        "timestamp" / Int64sl,
        "sample" / Int64ul,
        "duration" / Int64sl
    )

