# -*- coding: utf-8 -*-
"""
Microsoft-Windows-FileHistory-Engine
GUID : b447b4de-7780-11e0-ada3-18a90531a85a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b447b4de-7780-11e0-ada3-18a90531a85a"), event_id=3, version=0)
class Microsoft_Windows_FileHistory_Engine_3_0(Etw):
    pattern = Struct(
        "SourcePath" / WString,
        "DestPath" / WString,
        "Size" / Int64sl
    )


@declare(guid=guid("b447b4de-7780-11e0-ada3-18a90531a85a"), event_id=4, version=0)
class Microsoft_Windows_FileHistory_Engine_4_0(Etw):
    pattern = Struct(
        "SourcePath" / WString,
        "DestPath" / WString,
        "Size" / Int64sl
    )


@declare(guid=guid("b447b4de-7780-11e0-ada3-18a90531a85a"), event_id=6, version=0)
class Microsoft_Windows_FileHistory_Engine_6_0(Etw):
    pattern = Struct(
        "TotalSize" / Int64sl,
        "TotalFiles" / Int64ul
    )


@declare(guid=guid("b447b4de-7780-11e0-ada3-18a90531a85a"), event_id=9, version=0)
class Microsoft_Windows_FileHistory_Engine_9_0(Etw):
    pattern = Struct(
        "OldQuota" / Int64ul,
        "NewQuota" / Int64ul
    )


@declare(guid=guid("b447b4de-7780-11e0-ada3-18a90531a85a"), event_id=100, version=0)
class Microsoft_Windows_FileHistory_Engine_100_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("b447b4de-7780-11e0-ada3-18a90531a85a"), event_id=101, version=0)
class Microsoft_Windows_FileHistory_Engine_101_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("b447b4de-7780-11e0-ada3-18a90531a85a"), event_id=102, version=0)
class Microsoft_Windows_FileHistory_Engine_102_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "Hr" / Int32ul
    )


@declare(guid=guid("b447b4de-7780-11e0-ada3-18a90531a85a"), event_id=103, version=0)
class Microsoft_Windows_FileHistory_Engine_103_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "Hr" / Int32ul
    )


@declare(guid=guid("b447b4de-7780-11e0-ada3-18a90531a85a"), event_id=104, version=0)
class Microsoft_Windows_FileHistory_Engine_104_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("b447b4de-7780-11e0-ada3-18a90531a85a"), event_id=105, version=0)
class Microsoft_Windows_FileHistory_Engine_105_0(Etw):
    pattern = Struct(
        "Path" / WString
    )

