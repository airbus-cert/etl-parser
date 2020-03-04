# -*- coding: utf-8 -*-
"""
Microsoft-Windows-FileHistory-UI
GUID : b447b4e1-7780-11e0-ada3-18a90531a85a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b447b4e1-7780-11e0-ada3-18a90531a85a"), event_id=1, version=0)
class Microsoft_Windows_FileHistory_UI_1_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("b447b4e1-7780-11e0-ada3-18a90531a85a"), event_id=60, version=0)
class Microsoft_Windows_FileHistory_UI_60_0(Etw):
    pattern = Struct(
        "CommandLineParameters" / WString
    )


@declare(guid=guid("b447b4e1-7780-11e0-ada3-18a90531a85a"), event_id=61, version=0)
class Microsoft_Windows_FileHistory_UI_61_0(Etw):
    pattern = Struct(
        "CommandLineParameters" / WString
    )


@declare(guid=guid("b447b4e1-7780-11e0-ada3-18a90531a85a"), event_id=64, version=0)
class Microsoft_Windows_FileHistory_UI_64_0(Etw):
    pattern = Struct(
        "SearchFlags" / Int32ul
    )


@declare(guid=guid("b447b4e1-7780-11e0-ada3-18a90531a85a"), event_id=65, version=0)
class Microsoft_Windows_FileHistory_UI_65_0(Etw):
    pattern = Struct(
        "SearchFlags" / Int32ul
    )


@declare(guid=guid("b447b4e1-7780-11e0-ada3-18a90531a85a"), event_id=68, version=0)
class Microsoft_Windows_FileHistory_UI_68_0(Etw):
    pattern = Struct(
        "Message" / WString
    )

