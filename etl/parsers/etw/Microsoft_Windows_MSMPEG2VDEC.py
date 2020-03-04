# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MSMPEG2VDEC
GUID : ae5cf422-786a-476a-ac96-753b05877c99
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ae5cf422-786a-476a-ac96-753b05877c99"), event_id=0, version=0)
class Microsoft_Windows_MSMPEG2VDEC_0_0(Etw):
    pattern = Struct(
        "IDRCount" / Int32ul,
        "POC" / Int32sl,
        "PictureType" / Int8ul
    )


@declare(guid=guid("ae5cf422-786a-476a-ac96-753b05877c99"), event_id=1, version=0)
class Microsoft_Windows_MSMPEG2VDEC_1_0(Etw):
    pattern = Struct(
        "IDRCount" / Int32ul,
        "POC" / Int32sl,
        "PictureType" / Int8ul
    )


@declare(guid=guid("ae5cf422-786a-476a-ac96-753b05877c99"), event_id=2, version=0)
class Microsoft_Windows_MSMPEG2VDEC_2_0(Etw):
    pattern = Struct(
        "IDRCount" / Int32ul,
        "POC" / Int32sl
    )


@declare(guid=guid("ae5cf422-786a-476a-ac96-753b05877c99"), event_id=3, version=0)
class Microsoft_Windows_MSMPEG2VDEC_3_0(Etw):
    pattern = Struct(
        "TaskID" / Int8ul,
        "IDRCount" / Int32ul,
        "POC" / Int32sl
    )


@declare(guid=guid("ae5cf422-786a-476a-ac96-753b05877c99"), event_id=4, version=0)
class Microsoft_Windows_MSMPEG2VDEC_4_0(Etw):
    pattern = Struct(
        "TaskID" / Int8ul,
        "IDRCount" / Int32ul,
        "POC" / Int32sl
    )


@declare(guid=guid("ae5cf422-786a-476a-ac96-753b05877c99"), event_id=8, version=0)
class Microsoft_Windows_MSMPEG2VDEC_8_0(Etw):
    pattern = Struct(
        "QualityMode" / Int8ul
    )


@declare(guid=guid("ae5cf422-786a-476a-ac96-753b05877c99"), event_id=9, version=0)
class Microsoft_Windows_MSMPEG2VDEC_9_0(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul,
        "SARWidth" / Int32ul,
        "SARHeight" / Int32ul,
        "BitDepthLuma" / Int8ul,
        "BitDepthChroma" / Int8ul,
        "ChromaFormat" / Int8ul
    )


@declare(guid=guid("ae5cf422-786a-476a-ac96-753b05877c99"), event_id=10, version=0)
class Microsoft_Windows_MSMPEG2VDEC_10_0(Etw):
    pattern = Struct(
        "PictureType" / Int8ul
    )


@declare(guid=guid("ae5cf422-786a-476a-ac96-753b05877c99"), event_id=11, version=0)
class Microsoft_Windows_MSMPEG2VDEC_11_0(Etw):
    pattern = Struct(
        "PictureType" / Int8ul
    )


@declare(guid=guid("ae5cf422-786a-476a-ac96-753b05877c99"), event_id=17, version=0)
class Microsoft_Windows_MSMPEG2VDEC_17_0(Etw):
    pattern = Struct(
        "CodecID" / Int8ul
    )


@declare(guid=guid("ae5cf422-786a-476a-ac96-753b05877c99"), event_id=22, version=0)
class Microsoft_Windows_MSMPEG2VDEC_22_0(Etw):
    pattern = Struct(
        "SampleTime" / Int64sl,
        "SampleDuration" / Int64sl
    )


@declare(guid=guid("ae5cf422-786a-476a-ac96-753b05877c99"), event_id=23, version=0)
class Microsoft_Windows_MSMPEG2VDEC_23_0(Etw):
    pattern = Struct(
        "QualityType" / Int8ul,
        "Proportion" / Int32sl,
        "Late" / Int64sl,
        "TimeStamp" / Int64sl
    )


@declare(guid=guid("ae5cf422-786a-476a-ac96-753b05877c99"), event_id=24, version=0)
class Microsoft_Windows_MSMPEG2VDEC_24_0(Etw):
    pattern = Struct(
        "DecoderGUID" / Guid,
        "ConfigBitstreamEncryption" / Guid,
        "ConfigMBcontrolEncryption" / Guid,
        "ConfigResidDiffEncryption" / Guid,
        "ConfigBitstreamRaw" / Int32ul,
        "ConfigMBcontrolRasterOrder" / Int32ul,
        "ConfigResidDiffHost" / Int32ul,
        "ConfigSpatialResid8" / Int32ul,
        "ConfigResid8Subtraction" / Int32ul,
        "ConfigSpatialHost8or9Clipping" / Int32ul,
        "ConfigSpatialResidInterleaved" / Int32ul,
        "ConfigIntraResidUnsigned" / Int32ul,
        "ConfigResidDiffAccelerator" / Int32ul,
        "ConfigHostInverseScan" / Int32ul,
        "ConfigSpecificIDCT" / Int32ul,
        "Config4GroupedCoefs" / Int32ul,
        "ConfigMinRenderTargetBuffCount" / Int32ul
    )


@declare(guid=guid("ae5cf422-786a-476a-ac96-753b05877c99"), event_id=33, version=0)
class Microsoft_Windows_MSMPEG2VDEC_33_0(Etw):
    pattern = Struct(
        "SampleTime" / Int64sl,
        "SampleDuration" / Int64sl,
        "PicStructPresent" / Int8sl,
        "PicStruct" / Int8sl
    )


@declare(guid=guid("ae5cf422-786a-476a-ac96-753b05877c99"), event_id=34, version=0)
class Microsoft_Windows_MSMPEG2VDEC_34_0(Etw):
    pattern = Struct(
        "SampleLag" / Int64sl
    )


@declare(guid=guid("ae5cf422-786a-476a-ac96-753b05877c99"), event_id=35, version=0)
class Microsoft_Windows_MSMPEG2VDEC_35_0(Etw):
    pattern = Struct(
        "Message" / Int32ul
    )


@declare(guid=guid("ae5cf422-786a-476a-ac96-753b05877c99"), event_id=36, version=0)
class Microsoft_Windows_MSMPEG2VDEC_36_0(Etw):
    pattern = Struct(
        "DecoderGUID" / Guid,
        "NumSurfaces" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "RenderTarget" / Int32ul,
        "D3DFormat" / Int32ul
    )


@declare(guid=guid("ae5cf422-786a-476a-ac96-753b05877c99"), event_id=37, version=0)
class Microsoft_Windows_MSMPEG2VDEC_37_0(Etw):
    pattern = Struct(
        "DecoderGUID" / Guid,
        "NumSurfaces" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "RenderTarget" / Int32ul,
        "D3DFormat" / Int32ul
    )

