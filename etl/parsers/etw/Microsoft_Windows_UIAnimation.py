# -*- coding: utf-8 -*-
"""
Microsoft-Windows-UIAnimation
GUID : e0a40b26-30c4-4656-bc9a-74a5c3a0b2ec
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e0a40b26-30c4-4656-bc9a-74a5c3a0b2ec"), event_id=1, version=0)
class Microsoft_Windows_UIAnimation_1_0(Etw):
    pattern = Struct(
        "secondsNow" / Double
    )


@declare(guid=guid("e0a40b26-30c4-4656-bc9a-74a5c3a0b2ec"), event_id=3, version=0)
class Microsoft_Windows_UIAnimation_3_0(Etw):
    pattern = Struct(
        "secondsNow" / Double
    )


@declare(guid=guid("e0a40b26-30c4-4656-bc9a-74a5c3a0b2ec"), event_id=7, version=0)
class Microsoft_Windows_UIAnimation_7_0(Etw):
    pattern = Struct(
        "secondsNow" / Double,
        "tag" / Int32ul,
        "value0" / Double,
        "value1" / Double,
        "value2" / Double,
        "value3" / Double
    )


@declare(guid=guid("e0a40b26-30c4-4656-bc9a-74a5c3a0b2ec"), event_id=8, version=0)
class Microsoft_Windows_UIAnimation_8_0(Etw):
    pattern = Struct(
        "secondsNow" / Double,
        "tag" / Int32ul,
        "value0" / Double,
        "value1" / Double,
        "value2" / Double,
        "value3" / Double
    )


@declare(guid=guid("e0a40b26-30c4-4656-bc9a-74a5c3a0b2ec"), event_id=9, version=0)
class Microsoft_Windows_UIAnimation_9_0(Etw):
    pattern = Struct(
        "secondsNow" / Double,
        "tag" / Int32ul,
        "value0" / Double,
        "value1" / Double,
        "value2" / Double,
        "value3" / Double
    )


@declare(guid=guid("e0a40b26-30c4-4656-bc9a-74a5c3a0b2ec"), event_id=10, version=0)
class Microsoft_Windows_UIAnimation_10_0(Etw):
    pattern = Struct(
        "numIterations" / Int32ul
    )


@declare(guid=guid("e0a40b26-30c4-4656-bc9a-74a5c3a0b2ec"), event_id=11, version=0)
class Microsoft_Windows_UIAnimation_11_0(Etw):
    pattern = Struct(
        "numIterations" / Int32ul,
        "numComputations" / Int32ul
    )

