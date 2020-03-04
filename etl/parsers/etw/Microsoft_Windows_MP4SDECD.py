# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MP4SDECD
GUID : 7f2bd991-ae93-454a-b219-0bc23f02262a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7f2bd991-ae93-454a-b219-0bc23f02262a"), event_id=2, version=0)
class Microsoft_Windows_MP4SDECD_2_0(Etw):
    pattern = Struct(
        "FourCC" / Int32ul,
        "FrameRate" / Int32ul,
        "WidthSource" / Int32sl,
        "WidthHeight" / Int32sl
    )


@declare(guid=guid("7f2bd991-ae93-454a-b219-0bc23f02262a"), event_id=4, version=0)
class Microsoft_Windows_MP4SDECD_4_0(Etw):
    pattern = Struct(
        "FormatSize" / Int32ul,
        "Format" / Bytes(lambda this: this.FormatSize)
    )


@declare(guid=guid("7f2bd991-ae93-454a-b219-0bc23f02262a"), event_id=6, version=0)
class Microsoft_Windows_MP4SDECD_6_0(Etw):
    pattern = Struct(
        "SampleSizeInBytes" / Int32ul,
        "SampleTime" / Int64sl,
        "SampleDuration" / Int64sl
    )


@declare(guid=guid("7f2bd991-ae93-454a-b219-0bc23f02262a"), event_id=7, version=0)
class Microsoft_Windows_MP4SDECD_7_0(Etw):
    pattern = Struct(
        "Frame" / Int32ul
    )


@declare(guid=guid("7f2bd991-ae93-454a-b219-0bc23f02262a"), event_id=8, version=0)
class Microsoft_Windows_MP4SDECD_8_0(Etw):
    pattern = Struct(
        "Frame" / Int32ul,
        "SampleTime" / Int64sl,
        "SampleDuration" / Int64sl
    )


@declare(guid=guid("7f2bd991-ae93-454a-b219-0bc23f02262a"), event_id=10, version=0)
class Microsoft_Windows_MP4SDECD_10_0(Etw):
    pattern = Struct(
        "SampleTime" / Int64sl,
        "SampleDuration" / Int64sl
    )


@declare(guid=guid("7f2bd991-ae93-454a-b219-0bc23f02262a"), event_id=19, version=0)
class Microsoft_Windows_MP4SDECD_19_0(Etw):
    pattern = Struct(
        "ThinningMode" / Int8ul,
        "Rate" / Float32l
    )


@declare(guid=guid("7f2bd991-ae93-454a-b219-0bc23f02262a"), event_id=23, version=0)
class Microsoft_Windows_MP4SDECD_23_0(Etw):
    pattern = Struct(
        "DropMode" / Int32ul
    )


@declare(guid=guid("7f2bd991-ae93-454a-b219-0bc23f02262a"), event_id=24, version=0)
class Microsoft_Windows_MP4SDECD_24_0(Etw):
    pattern = Struct(
        "PostProcessingLevel" / Int32ul
    )

