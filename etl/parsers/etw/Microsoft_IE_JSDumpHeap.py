# -*- coding: utf-8 -*-
"""
Microsoft-IE-JSDumpHeap
GUID : 7f8e35ca-68e8-41b9-86fe-d6adc5b327e7
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7f8e35ca-68e8-41b9-86fe-d6adc5b327e7"), event_id=1, version=0)
class Microsoft_IE_JSDumpHeap_1_0(Etw):
    pattern = Struct(
        "Settings" / WString
    )


@declare(guid=guid("7f8e35ca-68e8-41b9-86fe-d6adc5b327e7"), event_id=2, version=1)
class Microsoft_IE_JSDumpHeap_2_1(Etw):
    pattern = Struct(
        "Summary" / WString
    )


@declare(guid=guid("7f8e35ca-68e8-41b9-86fe-d6adc5b327e7"), event_id=3, version=0)
class Microsoft_IE_JSDumpHeap_3_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Count" / Int32ul,
        "Values" / Int8sl
    )


@declare(guid=guid("7f8e35ca-68e8-41b9-86fe-d6adc5b327e7"), event_id=4, version=0)
class Microsoft_IE_JSDumpHeap_4_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Count" / Int32ul,
        "Values" / Int8sl
    )


@declare(guid=guid("7f8e35ca-68e8-41b9-86fe-d6adc5b327e7"), event_id=5, version=0)
class Microsoft_IE_JSDumpHeap_5_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Count" / Int32ul,
        "Values" / Int8sl
    )


@declare(guid=guid("7f8e35ca-68e8-41b9-86fe-d6adc5b327e7"), event_id=6, version=0)
class Microsoft_IE_JSDumpHeap_6_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Count" / Int32ul,
        "Values" / Int8sl
    )


@declare(guid=guid("7f8e35ca-68e8-41b9-86fe-d6adc5b327e7"), event_id=7, version=0)
class Microsoft_IE_JSDumpHeap_7_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Count" / Int32ul,
        "Values" / Int8sl
    )

