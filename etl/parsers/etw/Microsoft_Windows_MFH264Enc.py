# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MFH264Enc
GUID : 2a49de31-8a5b-4d3a-a904-7fc7409ae90d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("2a49de31-8a5b-4d3a-a904-7fc7409ae90d"), event_id=1, version=0)
class Microsoft_Windows_MFH264Enc_1_0(Etw):
    pattern = Struct(
        "EncoderInstance" / Int64ul,
        "Complexity" / Int32sl,
        "RateCtrlMode" / Int32sl,
        "ContentType" / Int32sl,
        "BufferSize" / Int32sl,
        "AverageBitRate" / Int32sl,
        "PeakBitRate" / Int32sl,
        "EntropyMode" / Int32sl,
        "MultithreadEncodingMode" / Int32sl,
        "NumberOfWorkerThreads" / Int32sl
    )


@declare(guid=guid("2a49de31-8a5b-4d3a-a904-7fc7409ae90d"), event_id=2, version=0)
class Microsoft_Windows_MFH264Enc_2_0(Etw):
    pattern = Struct(
        "EncoderInstance" / Int64ul
    )


@declare(guid=guid("2a49de31-8a5b-4d3a-a904-7fc7409ae90d"), event_id=3, version=0)
class Microsoft_Windows_MFH264Enc_3_0(Etw):
    pattern = Struct(
        "EncoderInstance" / Int64ul,
        "SampleTime" / Int64sl
    )


@declare(guid=guid("2a49de31-8a5b-4d3a-a904-7fc7409ae90d"), event_id=4, version=0)
class Microsoft_Windows_MFH264Enc_4_0(Etw):
    pattern = Struct(
        "EncoderInstance" / Int64ul,
        "SampleTime" / Int64sl
    )


@declare(guid=guid("2a49de31-8a5b-4d3a-a904-7fc7409ae90d"), event_id=5, version=0)
class Microsoft_Windows_MFH264Enc_5_0(Etw):
    pattern = Struct(
        "EncoderInstance" / Int64ul,
        "TimeStamp" / Int64sl,
        "Type" / Int32sl
    )


@declare(guid=guid("2a49de31-8a5b-4d3a-a904-7fc7409ae90d"), event_id=6, version=0)
class Microsoft_Windows_MFH264Enc_6_0(Etw):
    pattern = Struct(
        "EncoderInstance" / Int64ul,
        "TimeStamp" / Int64sl,
        "Type" / Int32sl
    )


@declare(guid=guid("2a49de31-8a5b-4d3a-a904-7fc7409ae90d"), event_id=7, version=0)
class Microsoft_Windows_MFH264Enc_7_0(Etw):
    pattern = Struct(
        "EncoderInstance" / Int64ul,
        "TimeStamp" / Int64sl,
        "GOPNumber" / Int32sl,
        "FrameNumber" / Int32sl,
        "FrameRate" / Double
    )


@declare(guid=guid("2a49de31-8a5b-4d3a-a904-7fc7409ae90d"), event_id=8, version=0)
class Microsoft_Windows_MFH264Enc_8_0(Etw):
    pattern = Struct(
        "EncoderInstance" / Int64ul,
        "TimeStamp" / Int64sl,
        "GOPNumber" / Int32sl,
        "FrameNumber" / Int32sl,
        "BitRate" / Int32sl
    )

