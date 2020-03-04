# -*- coding: utf-8 -*-
"""
Microsoft-Windows-osk
GUID : 4f768be8-9c69-4bbc-87fc-95291d3f9d0c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4f768be8-9c69-4bbc-87fc-95291d3f9d0c"), event_id=9, version=0)
class Microsoft_Windows_osk_9_0(Etw):
    pattern = Struct(
        "tcid" / Int32sl
    )


@declare(guid=guid("4f768be8-9c69-4bbc-87fc-95291d3f9d0c"), event_id=13, version=0)
class Microsoft_Windows_osk_13_0(Etw):
    pattern = Struct(
        "tcid" / Int32sl
    )


@declare(guid=guid("4f768be8-9c69-4bbc-87fc-95291d3f9d0c"), event_id=15, version=0)
class Microsoft_Windows_osk_15_0(Etw):
    pattern = Struct(
        "tcid" / Int32sl
    )


@declare(guid=guid("4f768be8-9c69-4bbc-87fc-95291d3f9d0c"), event_id=17, version=0)
class Microsoft_Windows_osk_17_0(Etw):
    pattern = Struct(
        "tcid" / Int32sl
    )


@declare(guid=guid("4f768be8-9c69-4bbc-87fc-95291d3f9d0c"), event_id=19, version=0)
class Microsoft_Windows_osk_19_0(Etw):
    pattern = Struct(
        "tcid" / Int32sl
    )

