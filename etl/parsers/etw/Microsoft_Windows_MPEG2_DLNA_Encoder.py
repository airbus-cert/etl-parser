# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MPEG2_DLNA-Encoder
GUID : 86efff39-2bdd-4efd-bd0b-853d71b2a9dc
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("86efff39-2bdd-4efd-bd0b-853d71b2a9dc"), event_id=0, version=0)
class Microsoft_Windows_MPEG2_DLNA_Encoder_0_0(Etw):
    pattern = Struct(
        "Region" / WString,
        "VideoX" / Int32ul,
        "VideoY" / Int32ul,
        "AudioChannels" / Int32ul,
        "VideoBitRate" / Int32ul,
        "AudioBitRate" / Int32ul,
        "SeekOffsetMs" / Int64sl
    )


@declare(guid=guid("86efff39-2bdd-4efd-bd0b-853d71b2a9dc"), event_id=1, version=0)
class Microsoft_Windows_MPEG2_DLNA_Encoder_1_0(Etw):
    pattern = Struct(
        "TotalBytesEncoded" / Int64ul,
        "VideoFramesReceived" / Int64ul,
        "VideoFramesEncoded" / Int64ul,
        "AudioBytesReceived" / Int64ul,
        "AudioFramesEncoded" / Int64ul
    )


@declare(guid=guid("86efff39-2bdd-4efd-bd0b-853d71b2a9dc"), event_id=2, version=0)
class Microsoft_Windows_MPEG2_DLNA_Encoder_2_0(Etw):
    pattern = Struct(
        "hr" / Int32sl
    )


@declare(guid=guid("86efff39-2bdd-4efd-bd0b-853d71b2a9dc"), event_id=3, version=0)
class Microsoft_Windows_MPEG2_DLNA_Encoder_3_0(Etw):
    pattern = Struct(
        "Timestamp" / Int64sl,
        "ID" / Int32ul
    )


@declare(guid=guid("86efff39-2bdd-4efd-bd0b-853d71b2a9dc"), event_id=4, version=0)
class Microsoft_Windows_MPEG2_DLNA_Encoder_4_0(Etw):
    pattern = Struct(
        "InputID" / Int32ul,
        "InputTimestamp" / Int64sl,
        "TargetTimestamp" / Int64sl
    )


@declare(guid=guid("86efff39-2bdd-4efd-bd0b-853d71b2a9dc"), event_id=5, version=0)
class Microsoft_Windows_MPEG2_DLNA_Encoder_5_0(Etw):
    pattern = Struct(
        "Timestamp" / Int64sl,
        "Bytes" / Int32ul
    )


@declare(guid=guid("86efff39-2bdd-4efd-bd0b-853d71b2a9dc"), event_id=7, version=0)
class Microsoft_Windows_MPEG2_DLNA_Encoder_7_0(Etw):
    pattern = Struct(
        "MaxBitRate" / Int32ul,
        "SampleRate" / Int32sl,
        "InputFormat" / Int8ul
    )


@declare(guid=guid("86efff39-2bdd-4efd-bd0b-853d71b2a9dc"), event_id=12, version=0)
class Microsoft_Windows_MPEG2_DLNA_Encoder_12_0(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32sl,
        "Progressive" / Int8ul,
        "MaxBitRate" / Int32sl
    )


@declare(guid=guid("86efff39-2bdd-4efd-bd0b-853d71b2a9dc"), event_id=17, version=0)
class Microsoft_Windows_MPEG2_DLNA_Encoder_17_0(Etw):
    pattern = Struct(
        "MuxFormat" / Int8ul
    )

