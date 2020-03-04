# -*- coding: utf-8 -*-
"""
Microsoft-Windows-FileHistory-EventListener
GUID : b447b4df-7780-11e0-ada3-18a90531a85a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b447b4df-7780-11e0-ada3-18a90531a85a"), event_id=106, version=0)
class Microsoft_Windows_FileHistory_EventListener_106_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("b447b4df-7780-11e0-ada3-18a90531a85a"), event_id=107, version=0)
class Microsoft_Windows_FileHistory_EventListener_107_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "Hr" / Int32ul
    )

