# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Photo-Image-Codec
GUID : be3a31ea-aa6c-4196-9dcc-9ca13a49e09f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("be3a31ea-aa6c-4196-9dcc-9ca13a49e09f"), event_id=8, version=0)
class Microsoft_Windows_Photo_Image_Codec_8_0(Etw):
    pattern = Struct(
        "Ratio" / Int32ul
    )


@declare(guid=guid("be3a31ea-aa6c-4196-9dcc-9ca13a49e09f"), event_id=10, version=0)
class Microsoft_Windows_Photo_Image_Codec_10_0(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Orientation" / Int8ul
    )


@declare(guid=guid("be3a31ea-aa6c-4196-9dcc-9ca13a49e09f"), event_id=11, version=0)
class Microsoft_Windows_Photo_Image_Codec_11_0(Etw):
    pattern = Struct(
        "ROIWidth" / Int32sl,
        "ROIHeight" / Int32sl,
        "ROIX" / Int32sl,
        "ROIY" / Int32sl,
        "OutWidth" / Int32ul,
        "OutHeight" / Int32ul,
        "Orientation" / Int8ul
    )


@declare(guid=guid("be3a31ea-aa6c-4196-9dcc-9ca13a49e09f"), event_id=12, version=0)
class Microsoft_Windows_Photo_Image_Codec_12_0(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Subband" / Int8ul,
        "BitStreamFormat" / Int8ul,
        "Orientation" / Int8ul,
        "IgnoreOverlap" / Int8ul,
        "DiscardAlpha" / Int8ul
    )


@declare(guid=guid("be3a31ea-aa6c-4196-9dcc-9ca13a49e09f"), event_id=13, version=0)
class Microsoft_Windows_Photo_Image_Codec_13_0(Etw):
    pattern = Struct(
        "ROIWidth" / Int32sl,
        "ROIHeight" / Int32sl,
        "ROIX" / Int32sl,
        "ROIY" / Int32sl,
        "Subband" / Int8ul,
        "BitStreamFormat" / Int8ul,
        "Orientation" / Int8ul,
        "IgnoreOverlap" / Int8ul,
        "DiscardAlpha" / Int8ul
    )

