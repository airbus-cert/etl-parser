# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SpellChecker
GUID : b2fcd41f-9a40-4150-8c92-b224b7d8c8aa
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b2fcd41f-9a40-4150-8c92-b224b7d8c8aa"), event_id=1, version=0)
class Microsoft_Windows_SpellChecker_1_0(Etw):
    pattern = Struct(
        "WordlistType" / Int32ul
    )


@declare(guid=guid("b2fcd41f-9a40-4150-8c92-b224b7d8c8aa"), event_id=2, version=0)
class Microsoft_Windows_SpellChecker_2_0(Etw):
    pattern = Struct(
        "WordlistType" / Int32ul
    )


@declare(guid=guid("b2fcd41f-9a40-4150-8c92-b224b7d8c8aa"), event_id=33, version=0)
class Microsoft_Windows_SpellChecker_33_0(Etw):
    pattern = Struct(
        "First" / WString,
        "Second" / WString,
        "hr" / Int32sl
    )

