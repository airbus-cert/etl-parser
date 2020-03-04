# -*- coding: utf-8 -*-
"""
Microsoft-Windows-msmpeg2venc
GUID : d17b213a-c505-49c9-98cc-734253ef65d4
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d17b213a-c505-49c9-98cc-734253ef65d4"), event_id=0, version=0)
class Microsoft_Windows_msmpeg2venc_0_0(Etw):
    pattern = Struct(
        "InputStreamID" / Int64ul,
        "pSample" / Int64ul,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("d17b213a-c505-49c9-98cc-734253ef65d4"), event_id=1, version=0)
class Microsoft_Windows_msmpeg2venc_1_0(Etw):
    pattern = Struct(
        "hr" / Int32sl
    )


@declare(guid=guid("d17b213a-c505-49c9-98cc-734253ef65d4"), event_id=2, version=0)
class Microsoft_Windows_msmpeg2venc_2_0(Etw):
    pattern = Struct(
        "InputStreamID" / Int64ul,
        "pEvent" / Int64ul
    )


@declare(guid=guid("d17b213a-c505-49c9-98cc-734253ef65d4"), event_id=3, version=0)
class Microsoft_Windows_msmpeg2venc_3_0(Etw):
    pattern = Struct(
        "hr" / Int32sl
    )


@declare(guid=guid("d17b213a-c505-49c9-98cc-734253ef65d4"), event_id=4, version=0)
class Microsoft_Windows_msmpeg2venc_4_0(Etw):
    pattern = Struct(
        "MessageType" / Int32ul,
        "Param" / Int64ul
    )


@declare(guid=guid("d17b213a-c505-49c9-98cc-734253ef65d4"), event_id=5, version=0)
class Microsoft_Windows_msmpeg2venc_5_0(Etw):
    pattern = Struct(
        "hr" / Int32sl
    )


@declare(guid=guid("d17b213a-c505-49c9-98cc-734253ef65d4"), event_id=6, version=0)
class Microsoft_Windows_msmpeg2venc_6_0(Etw):
    pattern = Struct(
        "OldBitrate" / Int64ul,
        "NewBitrate" / Int64ul
    )


@declare(guid=guid("d17b213a-c505-49c9-98cc-734253ef65d4"), event_id=7, version=0)
class Microsoft_Windows_msmpeg2venc_7_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "OutputBufferCount" / Int64ul,
        "pOutputSamples" / Int64ul,
        "pdwStatus" / Int64ul
    )


@declare(guid=guid("d17b213a-c505-49c9-98cc-734253ef65d4"), event_id=8, version=0)
class Microsoft_Windows_msmpeg2venc_8_0(Etw):
    pattern = Struct(
        "hr" / Int32sl
    )


@declare(guid=guid("d17b213a-c505-49c9-98cc-734253ef65d4"), event_id=9, version=0)
class Microsoft_Windows_msmpeg2venc_9_0(Etw):
    pattern = Struct(
        "pSample" / Int64ul,
        "cSampleLength" / Int64ul
    )


@declare(guid=guid("d17b213a-c505-49c9-98cc-734253ef65d4"), event_id=11, version=0)
class Microsoft_Windows_msmpeg2venc_11_0(Etw):
    pattern = Struct(
        "pSample" / Int64ul,
        "cSampleLength" / Int64ul,
        "bEndOfEncoding" / Int8ul
    )


@declare(guid=guid("d17b213a-c505-49c9-98cc-734253ef65d4"), event_id=12, version=0)
class Microsoft_Windows_msmpeg2venc_12_0(Etw):
    pattern = Struct(
        "CodingMode" / Int32ul,
        "Bitrate" / Int64ul,
        "Complexity" / Int64ul,
        "pEncoder" / Int64ul
    )

