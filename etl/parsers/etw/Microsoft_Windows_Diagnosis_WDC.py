# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Diagnosis-WDC
GUID : 05921578-2261-42c7-a0d3-26ddbce6c50d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("05921578-2261-42c7-a0d3-26ddbce6c50d"), event_id=5016, version=0)
class Microsoft_Windows_Diagnosis_WDC_5016_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "Line" / Int32ul,
        "Address" / Int64ul,
        "Size" / Int64ul
    )


@declare(guid=guid("05921578-2261-42c7-a0d3-26ddbce6c50d"), event_id=5017, version=0)
class Microsoft_Windows_Diagnosis_WDC_5017_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "Line" / Int32ul,
        "Address" / Int64ul
    )


@declare(guid=guid("05921578-2261-42c7-a0d3-26ddbce6c50d"), event_id=5018, version=0)
class Microsoft_Windows_Diagnosis_WDC_5018_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "Line" / Int32ul,
        "Address" / Int64ul,
        "Size" / Int64ul,
        "OrigAddress" / Int64ul
    )


@declare(guid=guid("05921578-2261-42c7-a0d3-26ddbce6c50d"), event_id=5100, version=0)
class Microsoft_Windows_Diagnosis_WDC_5100_0(Etw):
    pattern = Struct(
        "TableId" / Int32ul,
        "ItemPos" / Int32ul,
        "ItemState" / Int32ul,
        "ItemContent" / WString
    )


@declare(guid=guid("05921578-2261-42c7-a0d3-26ddbce6c50d"), event_id=5101, version=0)
class Microsoft_Windows_Diagnosis_WDC_5101_0(Etw):
    pattern = Struct(
        "TableId" / Int32ul,
        "ItemPos" / Int32ul,
        "ItemState" / Int32ul,
        "ItemContent" / WString
    )


@declare(guid=guid("05921578-2261-42c7-a0d3-26ddbce6c50d"), event_id=5102, version=0)
class Microsoft_Windows_Diagnosis_WDC_5102_0(Etw):
    pattern = Struct(
        "TableId" / Int32ul,
        "ItemPos" / Int32ul,
        "ItemState" / Int32ul,
        "ItemContent" / WString
    )


@declare(guid=guid("05921578-2261-42c7-a0d3-26ddbce6c50d"), event_id=5103, version=0)
class Microsoft_Windows_Diagnosis_WDC_5103_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "Function" / CString,
        "Line" / Int32ul,
        "ErrorText" / WString
    )


@declare(guid=guid("05921578-2261-42c7-a0d3-26ddbce6c50d"), event_id=5202, version=0)
class Microsoft_Windows_Diagnosis_WDC_5202_0(Etw):
    pattern = Struct(
        "TabId" / Int32ul
    )


@declare(guid=guid("05921578-2261-42c7-a0d3-26ddbce6c50d"), event_id=5203, version=0)
class Microsoft_Windows_Diagnosis_WDC_5203_0(Etw):
    pattern = Struct(
        "TabId" / Int32ul
    )


@declare(guid=guid("05921578-2261-42c7-a0d3-26ddbce6c50d"), event_id=5204, version=0)
class Microsoft_Windows_Diagnosis_WDC_5204_0(Etw):
    pattern = Struct(
        "RequestCookie" / Int32ul
    )


@declare(guid=guid("05921578-2261-42c7-a0d3-26ddbce6c50d"), event_id=5205, version=0)
class Microsoft_Windows_Diagnosis_WDC_5205_0(Etw):
    pattern = Struct(
        "RequestCookie" / Int32ul
    )


@declare(guid=guid("05921578-2261-42c7-a0d3-26ddbce6c50d"), event_id=5206, version=0)
class Microsoft_Windows_Diagnosis_WDC_5206_0(Etw):
    pattern = Struct(
        "TableId" / Int32ul,
        "ColumnId" / Int32ul
    )


@declare(guid=guid("05921578-2261-42c7-a0d3-26ddbce6c50d"), event_id=5207, version=0)
class Microsoft_Windows_Diagnosis_WDC_5207_0(Etw):
    pattern = Struct(
        "TableId" / Int32ul,
        "ColumnId" / Int32ul
    )

