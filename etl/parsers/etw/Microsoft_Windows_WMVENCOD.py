# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WMVENCOD
GUID : 313b0545-bf9c-492e-9173-8de4863b8573
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("313b0545-bf9c-492e-9173-8de4863b8573"), event_id=0, version=0)
class Microsoft_Windows_WMVENCOD_0_0(Etw):
    pattern = Struct(
        "SampleTime" / Int64sl,
        "SamplePointer" / Int64ul,
        "EncoderInstance" / Int64ul
    )


@declare(guid=guid("313b0545-bf9c-492e-9173-8de4863b8573"), event_id=1, version=0)
class Microsoft_Windows_WMVENCOD_1_0(Etw):
    pattern = Struct(
        "SampleTime" / Int64sl,
        "SamplePointer" / Int64ul,
        "EncoderInstance" / Int64ul
    )


@declare(guid=guid("313b0545-bf9c-492e-9173-8de4863b8573"), event_id=2, version=0)
class Microsoft_Windows_WMVENCOD_2_0(Etw):
    pattern = Struct(
        "SampleTime" / Int64sl,
        "SamplePointer" / Int64ul,
        "EncoderInstance" / Int64ul
    )


@declare(guid=guid("313b0545-bf9c-492e-9173-8de4863b8573"), event_id=3, version=0)
class Microsoft_Windows_WMVENCOD_3_0(Etw):
    pattern = Struct(
        "SampleTime" / Int64sl,
        "SamplePointer" / Int64ul,
        "EncoderInstance" / Int64ul
    )


@declare(guid=guid("313b0545-bf9c-492e-9173-8de4863b8573"), event_id=4, version=0)
class Microsoft_Windows_WMVENCOD_4_0(Etw):
    pattern = Struct(
        "CodingMode" / Int32sl,
        "InterlaceCodingType" / Int32ul,
        "EncoderInstance" / Int64ul
    )


@declare(guid=guid("313b0545-bf9c-492e-9173-8de4863b8573"), event_id=5, version=0)
class Microsoft_Windows_WMVENCOD_5_0(Etw):
    pattern = Struct(
        "BufferLevelInfo" / Int32sl,
        "SampleTime" / Int64sl,
        "EncoderInstance" / Int64ul
    )


@declare(guid=guid("313b0545-bf9c-492e-9173-8de4863b8573"), event_id=6, version=0)
class Microsoft_Windows_WMVENCOD_6_0(Etw):
    pattern = Struct(
        "NumberOfReencode" / Int32sl,
        "SampleTime" / Int64sl,
        "EncoderInstance" / Int64ul
    )


@declare(guid=guid("313b0545-bf9c-492e-9173-8de4863b8573"), event_id=7, version=0)
class Microsoft_Windows_WMVENCOD_7_0(Etw):
    pattern = Struct(
        "SampleTime" / Int64sl,
        "EncoderInstance" / Int64ul
    )


@declare(guid=guid("313b0545-bf9c-492e-9173-8de4863b8573"), event_id=8, version=0)
class Microsoft_Windows_WMVENCOD_8_0(Etw):
    pattern = Struct(
        "MixedMVCost" / Double,
        "OneMVQPBicubicCost" / Double,
        "OneMVHPBicubicCost" / Double,
        "OneMVHPBilinearCost" / Double,
        "IntraCost" / Double,
        "SampleTime" / Int64sl,
        "EncoderInstance" / Int64ul
    )


@declare(guid=guid("313b0545-bf9c-492e-9173-8de4863b8573"), event_id=9, version=0)
class Microsoft_Windows_WMVENCOD_9_0(Etw):
    pattern = Struct(
        "SampleTime" / Int64sl,
        "EncoderInstance" / Int64ul
    )


@declare(guid=guid("313b0545-bf9c-492e-9173-8de4863b8573"), event_id=10, version=0)
class Microsoft_Windows_WMVENCOD_10_0(Etw):
    pattern = Struct(
        "Resolution" / Int32ul,
        "EncoderInstance" / Int64ul
    )


@declare(guid=guid("313b0545-bf9c-492e-9173-8de4863b8573"), event_id=11, version=0)
class Microsoft_Windows_WMVENCOD_11_0(Etw):
    pattern = Struct(
        "Bitrate" / Int32ul,
        "EncoderInstance" / Int64ul
    )


@declare(guid=guid("313b0545-bf9c-492e-9173-8de4863b8573"), event_id=12, version=0)
class Microsoft_Windows_WMVENCOD_12_0(Etw):
    pattern = Struct(
        "Bitrate" / Int32ul,
        "EncoderInstance" / Int64ul
    )

