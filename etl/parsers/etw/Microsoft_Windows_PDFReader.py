# -*- coding: utf-8 -*-
"""
Microsoft-Windows-PDFReader
GUID : dfa86faa-2c55-4140-bff9-5cc586217a7b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=1, version=0)
class Microsoft_Windows_PDFReader_1_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "WindowID" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=2, version=0)
class Microsoft_Windows_PDFReader_2_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=35, version=0)
class Microsoft_Windows_PDFReader_35_0(Etw):
    pattern = Struct(
        "StringParam" / CString,
        "HResultParam" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=44, version=0)
class Microsoft_Windows_PDFReader_44_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=45, version=0)
class Microsoft_Windows_PDFReader_45_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=58, version=0)
class Microsoft_Windows_PDFReader_58_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=60, version=0)
class Microsoft_Windows_PDFReader_60_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=62, version=0)
class Microsoft_Windows_PDFReader_62_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=64, version=0)
class Microsoft_Windows_PDFReader_64_0(Etw):
    pattern = Struct(
        "DoubleParam" / Double
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=68, version=0)
class Microsoft_Windows_PDFReader_68_0(Etw):
    pattern = Struct(
        "PageId" / Int32ul,
        "RectLeft" / Float32l,
        "RectTop" / Float32l,
        "RectRight" / Float32l,
        "RectBottom" / Float32l
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=70, version=0)
class Microsoft_Windows_PDFReader_70_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=71, version=0)
class Microsoft_Windows_PDFReader_71_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=72, version=0)
class Microsoft_Windows_PDFReader_72_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=73, version=0)
class Microsoft_Windows_PDFReader_73_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=74, version=0)
class Microsoft_Windows_PDFReader_74_0(Etw):
    pattern = Struct(
        "DoubleParam" / Double
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=75, version=0)
class Microsoft_Windows_PDFReader_75_0(Etw):
    pattern = Struct(
        "DoubleParam" / Double
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=87, version=0)
class Microsoft_Windows_PDFReader_87_0(Etw):
    pattern = Struct(
        "FloatParam" / Float32l
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=88, version=0)
class Microsoft_Windows_PDFReader_88_0(Etw):
    pattern = Struct(
        "RangeMin" / Float32l,
        "RangeMax" / Float32l
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=91, version=0)
class Microsoft_Windows_PDFReader_91_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=92, version=0)
class Microsoft_Windows_PDFReader_92_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=93, version=0)
class Microsoft_Windows_PDFReader_93_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=94, version=0)
class Microsoft_Windows_PDFReader_94_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=95, version=0)
class Microsoft_Windows_PDFReader_95_0(Etw):
    pattern = Struct(
        "ControlId" / WString,
        "RectLeft" / Int32ul,
        "RectTop" / Int32ul,
        "RectRight" / Int32ul,
        "RectBottom" / Int32ul,
        "ControlName" / WString,
        "ControlToolTip" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=96, version=0)
class Microsoft_Windows_PDFReader_96_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=97, version=0)
class Microsoft_Windows_PDFReader_97_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=98, version=0)
class Microsoft_Windows_PDFReader_98_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=99, version=0)
class Microsoft_Windows_PDFReader_99_0(Etw):
    pattern = Struct(
        "Aspect" / Int32sl,
        "PageIndex" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=100, version=0)
class Microsoft_Windows_PDFReader_100_0(Etw):
    pattern = Struct(
        "Aspect" / Int32sl,
        "PageIndex" / Int32ul,
        "IsCancelled" / Int8ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=101, version=0)
class Microsoft_Windows_PDFReader_101_0(Etw):
    pattern = Struct(
        "StringParam" / WString,
        "HResultParam" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=102, version=0)
class Microsoft_Windows_PDFReader_102_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=103, version=0)
class Microsoft_Windows_PDFReader_103_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=104, version=0)
class Microsoft_Windows_PDFReader_104_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=106, version=0)
class Microsoft_Windows_PDFReader_106_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=107, version=0)
class Microsoft_Windows_PDFReader_107_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=109, version=0)
class Microsoft_Windows_PDFReader_109_0(Etw):
    pattern = Struct(
        "BooleanParam" / Int8ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=110, version=0)
class Microsoft_Windows_PDFReader_110_0(Etw):
    pattern = Struct(
        "BooleanParam" / Int8ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=111, version=0)
class Microsoft_Windows_PDFReader_111_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=113, version=0)
class Microsoft_Windows_PDFReader_113_0(Etw):
    pattern = Struct(
        "Zoom" / Float32l,
        "Rotation" / Float32l
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=114, version=0)
class Microsoft_Windows_PDFReader_114_0(Etw):
    pattern = Struct(
        "Zoom" / Float32l,
        "Rotation" / Float32l
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=115, version=0)
class Microsoft_Windows_PDFReader_115_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=116, version=0)
class Microsoft_Windows_PDFReader_116_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=117, version=0)
class Microsoft_Windows_PDFReader_117_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=120, version=0)
class Microsoft_Windows_PDFReader_120_0(Etw):
    pattern = Struct(
        "StringParam" / CString,
        "HResultParam" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=130, version=0)
class Microsoft_Windows_PDFReader_130_0(Etw):
    pattern = Struct(
        "BooleanParam" / Int8ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=131, version=0)
class Microsoft_Windows_PDFReader_131_0(Etw):
    pattern = Struct(
        "BooleanParam" / Int8ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=134, version=0)
class Microsoft_Windows_PDFReader_134_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=135, version=0)
class Microsoft_Windows_PDFReader_135_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=136, version=0)
class Microsoft_Windows_PDFReader_136_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=137, version=0)
class Microsoft_Windows_PDFReader_137_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=139, version=0)
class Microsoft_Windows_PDFReader_139_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=142, version=0)
class Microsoft_Windows_PDFReader_142_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=153, version=0)
class Microsoft_Windows_PDFReader_153_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=154, version=0)
class Microsoft_Windows_PDFReader_154_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=157, version=0)
class Microsoft_Windows_PDFReader_157_0(Etw):
    pattern = Struct(
        "RectLeft" / Float32l,
        "RectTop" / Float32l,
        "RectRight" / Float32l,
        "RectBottom" / Float32l
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=158, version=0)
class Microsoft_Windows_PDFReader_158_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=163, version=0)
class Microsoft_Windows_PDFReader_163_0(Etw):
    pattern = Struct(
        "PageNumber" / Int32ul,
        "PageRectLeft" / Int32sl,
        "PageRectTop" / Int32sl,
        "PageRectRight" / Int32sl,
        "PageRectBottom" / Int32sl
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=166, version=0)
class Microsoft_Windows_PDFReader_166_0(Etw):
    pattern = Struct(
        "PageId" / Int32ul,
        "RectLeft" / Float32l,
        "RectTop" / Float32l,
        "RectRight" / Float32l,
        "RectBottom" / Float32l
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=167, version=0)
class Microsoft_Windows_PDFReader_167_0(Etw):
    pattern = Struct(
        "PageId" / Int32ul,
        "RectLeft" / Float32l,
        "RectTop" / Float32l,
        "RectRight" / Float32l,
        "RectBottom" / Float32l
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=171, version=0)
class Microsoft_Windows_PDFReader_171_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=172, version=0)
class Microsoft_Windows_PDFReader_172_0(Etw):
    pattern = Struct(
        "NewZoom" / Float32l,
        "TranslationDeltaX" / Float32l,
        "TranslationDeltaY" / Float32l,
        "TranslationDeltaIsInertial" / Int8ul,
        "TranslationDeltaAnchorPointX" / Float32l,
        "TranslationDeltaAnchorPointY" / Float32l
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=179, version=0)
class Microsoft_Windows_PDFReader_179_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=180, version=0)
class Microsoft_Windows_PDFReader_180_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=181, version=0)
class Microsoft_Windows_PDFReader_181_0(Etw):
    pattern = Struct(
        "X" / Float32l,
        "Y" / Float32l
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=182, version=0)
class Microsoft_Windows_PDFReader_182_0(Etw):
    pattern = Struct(
        "X" / Float32l,
        "Y" / Float32l
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=183, version=0)
class Microsoft_Windows_PDFReader_183_0(Etw):
    pattern = Struct(
        "X" / Float32l,
        "Y" / Float32l
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=199, version=0)
class Microsoft_Windows_PDFReader_199_0(Etw):
    pattern = Struct(
        "StringParam" / WString,
        "HResultParam" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=200, version=0)
class Microsoft_Windows_PDFReader_200_0(Etw):
    pattern = Struct(
        "Aspect" / Int32sl,
        "PageIndex" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=201, version=0)
class Microsoft_Windows_PDFReader_201_0(Etw):
    pattern = Struct(
        "BooleanParam" / Int8ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=202, version=0)
class Microsoft_Windows_PDFReader_202_0(Etw):
    pattern = Struct(
        "BooleanParam" / Int8ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=210, version=0)
class Microsoft_Windows_PDFReader_210_0(Etw):
    pattern = Struct(
        "Zoom" / Float32l,
        "PageSetId" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=216, version=0)
class Microsoft_Windows_PDFReader_216_0(Etw):
    pattern = Struct(
        "PageId" / Int32ul,
        "RectLeft" / Float32l,
        "RectTop" / Float32l,
        "RectRight" / Float32l,
        "RectBottom" / Float32l
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=218, version=0)
class Microsoft_Windows_PDFReader_218_0(Etw):
    pattern = Struct(
        "PageId" / Int32ul,
        "RectLeft" / Float32l,
        "RectTop" / Float32l,
        "RectRight" / Float32l,
        "RectBottom" / Float32l
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=219, version=0)
class Microsoft_Windows_PDFReader_219_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=220, version=0)
class Microsoft_Windows_PDFReader_220_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=221, version=0)
class Microsoft_Windows_PDFReader_221_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=222, version=0)
class Microsoft_Windows_PDFReader_222_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=225, version=0)
class Microsoft_Windows_PDFReader_225_0(Etw):
    pattern = Struct(
        "PageId" / Int32ul,
        "RectLeft" / Float32l,
        "RectTop" / Float32l,
        "RectRight" / Float32l,
        "RectBottom" / Float32l
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=226, version=0)
class Microsoft_Windows_PDFReader_226_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=227, version=0)
class Microsoft_Windows_PDFReader_227_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=228, version=0)
class Microsoft_Windows_PDFReader_228_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=229, version=0)
class Microsoft_Windows_PDFReader_229_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=230, version=0)
class Microsoft_Windows_PDFReader_230_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=231, version=0)
class Microsoft_Windows_PDFReader_231_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=232, version=0)
class Microsoft_Windows_PDFReader_232_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=233, version=0)
class Microsoft_Windows_PDFReader_233_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=234, version=0)
class Microsoft_Windows_PDFReader_234_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=235, version=0)
class Microsoft_Windows_PDFReader_235_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=236, version=0)
class Microsoft_Windows_PDFReader_236_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=237, version=0)
class Microsoft_Windows_PDFReader_237_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=238, version=0)
class Microsoft_Windows_PDFReader_238_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=239, version=0)
class Microsoft_Windows_PDFReader_239_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=240, version=0)
class Microsoft_Windows_PDFReader_240_0(Etw):
    pattern = Struct(
        "PageId" / Int32ul,
        "RectLeft" / Float32l,
        "RectTop" / Float32l,
        "RectRight" / Float32l,
        "RectBottom" / Float32l
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=241, version=0)
class Microsoft_Windows_PDFReader_241_0(Etw):
    pattern = Struct(
        "PageId" / Int32ul,
        "RectLeft" / Float32l,
        "RectTop" / Float32l,
        "RectRight" / Float32l,
        "RectBottom" / Float32l
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=247, version=0)
class Microsoft_Windows_PDFReader_247_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=248, version=0)
class Microsoft_Windows_PDFReader_248_0(Etw):
    pattern = Struct(
        "PageId" / Int32ul,
        "RectLeft" / Float32l,
        "RectTop" / Float32l,
        "RectRight" / Float32l,
        "RectBottom" / Float32l
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=250, version=0)
class Microsoft_Windows_PDFReader_250_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul,
        "StringParam" / WString,
        "BooleanParam" / Int8ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=251, version=0)
class Microsoft_Windows_PDFReader_251_0(Etw):
    pattern = Struct(
        "SameWindow" / Int8ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=253, version=0)
class Microsoft_Windows_PDFReader_253_0(Etw):
    pattern = Struct(
        "PageId" / Int32ul,
        "RectLeft" / Float32l,
        "RectTop" / Float32l,
        "RectRight" / Float32l,
        "RectBottom" / Float32l
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=254, version=0)
class Microsoft_Windows_PDFReader_254_0(Etw):
    pattern = Struct(
        "PageId" / Int32ul,
        "RectLeft" / Float32l,
        "RectTop" / Float32l,
        "RectRight" / Float32l,
        "RectBottom" / Float32l
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=256, version=0)
class Microsoft_Windows_PDFReader_256_0(Etw):
    pattern = Struct(
        "ScriptUniqueIdentifier" / Int32ul,
        "ScriptMetadata" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=257, version=0)
class Microsoft_Windows_PDFReader_257_0(Etw):
    pattern = Struct(
        "ScriptUniqueIdentifier" / Int32ul,
        "ScriptMetadata" / WString,
        "ScriptCompletedSuccessfully" / Int8ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=258, version=0)
class Microsoft_Windows_PDFReader_258_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=259, version=0)
class Microsoft_Windows_PDFReader_259_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=260, version=0)
class Microsoft_Windows_PDFReader_260_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=261, version=0)
class Microsoft_Windows_PDFReader_261_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=264, version=0)
class Microsoft_Windows_PDFReader_264_0(Etw):
    pattern = Struct(
        "MailtoProtocolString" / WString
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=272, version=0)
class Microsoft_Windows_PDFReader_272_0(Etw):
    pattern = Struct(
        "PageId" / Int32ul,
        "ModelType" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=274, version=0)
class Microsoft_Windows_PDFReader_274_0(Etw):
    pattern = Struct(
        "WindowID" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=278, version=0)
class Microsoft_Windows_PDFReader_278_0(Etw):
    pattern = Struct(
        "WindowID" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=279, version=0)
class Microsoft_Windows_PDFReader_279_0(Etw):
    pattern = Struct(
        "WindowID" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=280, version=0)
class Microsoft_Windows_PDFReader_280_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=281, version=0)
class Microsoft_Windows_PDFReader_281_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=282, version=0)
class Microsoft_Windows_PDFReader_282_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )


@declare(guid=guid("dfa86faa-2c55-4140-bff9-5cc586217a7b"), event_id=283, version=0)
class Microsoft_Windows_PDFReader_283_0(Etw):
    pattern = Struct(
        "UInt32Param" / Int32ul
    )

