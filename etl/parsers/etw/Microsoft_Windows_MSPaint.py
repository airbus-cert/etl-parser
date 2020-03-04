# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MSPaint
GUID : 1d75856d-36a7-4ecb-a3f5-b13152222d29
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("1d75856d-36a7-4ecb-a3f5-b13152222d29"), event_id=7, version=0)
class Microsoft_Windows_MSPaint_7_0(Etw):
    pattern = Struct(
        "ToolID" / Int32sl
    )


@declare(guid=guid("1d75856d-36a7-4ecb-a3f5-b13152222d29"), event_id=9, version=0)
class Microsoft_Windows_MSPaint_9_0(Etw):
    pattern = Struct(
        "ToolID" / Int32sl
    )


@declare(guid=guid("1d75856d-36a7-4ecb-a3f5-b13152222d29"), event_id=13, version=0)
class Microsoft_Windows_MSPaint_13_0(Etw):
    pattern = Struct(
        "ToolID" / Int32sl,
        "ToolThickness" / Int32sl
    )


@declare(guid=guid("1d75856d-36a7-4ecb-a3f5-b13152222d29"), event_id=14, version=0)
class Microsoft_Windows_MSPaint_14_0(Etw):
    pattern = Struct(
        "Color" / Int64ul
    )


@declare(guid=guid("1d75856d-36a7-4ecb-a3f5-b13152222d29"), event_id=15, version=0)
class Microsoft_Windows_MSPaint_15_0(Etw):
    pattern = Struct(
        "Color" / Int64ul
    )


@declare(guid=guid("1d75856d-36a7-4ecb-a3f5-b13152222d29"), event_id=16, version=0)
class Microsoft_Windows_MSPaint_16_0(Etw):
    pattern = Struct(
        "ShapeDrawMode" / Int32sl
    )


@declare(guid=guid("1d75856d-36a7-4ecb-a3f5-b13152222d29"), event_id=17, version=0)
class Microsoft_Windows_MSPaint_17_0(Etw):
    pattern = Struct(
        "ToolCrosssection" / Int32sl
    )


@declare(guid=guid("1d75856d-36a7-4ecb-a3f5-b13152222d29"), event_id=18, version=0)
class Microsoft_Windows_MSPaint_18_0(Etw):
    pattern = Struct(
        "ToolCrosssection" / Int32sl
    )


@declare(guid=guid("1d75856d-36a7-4ecb-a3f5-b13152222d29"), event_id=19, version=0)
class Microsoft_Windows_MSPaint_19_0(Etw):
    pattern = Struct(
        "Color" / Int64ul
    )


@declare(guid=guid("1d75856d-36a7-4ecb-a3f5-b13152222d29"), event_id=20, version=0)
class Microsoft_Windows_MSPaint_20_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("1d75856d-36a7-4ecb-a3f5-b13152222d29"), event_id=26, version=0)
class Microsoft_Windows_MSPaint_26_0(Etw):
    pattern = Struct(
        "Saveoperationresult" / Int32sl
    )


@declare(guid=guid("1d75856d-36a7-4ecb-a3f5-b13152222d29"), event_id=38, version=0)
class Microsoft_Windows_MSPaint_38_0(Etw):
    pattern = Struct(
        "ResizeskewOperationresult" / Int32sl,
        "Widthofthecanvas" / Int32sl,
        "Heightofthecanvas" / Int32sl,
        "Horizontalresizepercentage" / Int32sl,
        "Verticalresizepercentage" / Int32sl,
        "Horizontalskewangle" / Int32sl,
        "Verticalskewangle" / Int32sl
    )

