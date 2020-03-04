# -*- coding: utf-8 -*-
"""
Microsoft-Windows-HAL
GUID : 63d1e632-95cc-4443-9312-af927761d52a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("63d1e632-95cc-4443-9312-af927761d52a"), event_id=1, version=0)
class Microsoft_Windows_HAL_1_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("63d1e632-95cc-4443-9312-af927761d52a"), event_id=2, version=0)
class Microsoft_Windows_HAL_2_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("63d1e632-95cc-4443-9312-af927761d52a"), event_id=3, version=0)
class Microsoft_Windows_HAL_3_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("63d1e632-95cc-4443-9312-af927761d52a"), event_id=4, version=0)
class Microsoft_Windows_HAL_4_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("63d1e632-95cc-4443-9312-af927761d52a"), event_id=5, version=0)
class Microsoft_Windows_HAL_5_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("63d1e632-95cc-4443-9312-af927761d52a"), event_id=7, version=0)
class Microsoft_Windows_HAL_7_0(Etw):
    pattern = Struct(
        "LeadProcessor" / Int32sl,
        "TargetProcessor" / Int32sl,
        "Delta" / Int64sl,
        "NopCycles" / Int32ul
    )


@declare(guid=guid("63d1e632-95cc-4443-9312-af927761d52a"), event_id=8, version=0)
class Microsoft_Windows_HAL_8_0(Etw):
    pattern = Struct(
        "LeadProcessor" / Int32sl,
        "MaximumPositiveDeltaProcessor" / Int32sl,
        "MaximumPositiveDelta" / Int32sl,
        "MaximumNegativeDelta" / Int32sl,
        "Microseconds" / Int32sl
    )


@declare(guid=guid("63d1e632-95cc-4443-9312-af927761d52a"), event_id=9, version=0)
class Microsoft_Windows_HAL_9_0(Etw):
    pattern = Struct(
        "SourceProcessor" / Int32sl,
        "TargetProcessor" / Int32sl,
        "Delta" / Int64sl,
        "Bias" / Int64sl,
        "Wave" / Int32ul
    )


@declare(guid=guid("63d1e632-95cc-4443-9312-af927761d52a"), event_id=10, version=0)
class Microsoft_Windows_HAL_10_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("63d1e632-95cc-4443-9312-af927761d52a"), event_id=11, version=0)
class Microsoft_Windows_HAL_11_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("63d1e632-95cc-4443-9312-af927761d52a"), event_id=12, version=0)
class Microsoft_Windows_HAL_12_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "FirstPage" / Int32ul,
        "LastPage" / Int32ul
    )

