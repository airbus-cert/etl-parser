# -*- coding: utf-8 -*-
"""
Microsoft-Windows-FileHistory-ConfigManager
GUID : b447b4dd-7780-11e0-ada3-18a90531a85a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b447b4dd-7780-11e0-ada3-18a90531a85a"), event_id=1, version=0)
class Microsoft_Windows_FileHistory_ConfigManager_1_0(Etw):
    pattern = Struct(
        "TargetUrl" / WString
    )


@declare(guid=guid("b447b4dd-7780-11e0-ada3-18a90531a85a"), event_id=2, version=0)
class Microsoft_Windows_FileHistory_ConfigManager_2_0(Etw):
    pattern = Struct(
        "TargetUrl" / WString
    )


@declare(guid=guid("b447b4dd-7780-11e0-ada3-18a90531a85a"), event_id=3, version=0)
class Microsoft_Windows_FileHistory_ConfigManager_3_0(Etw):
    pattern = Struct(
        "TargetUrl" / WString
    )


@declare(guid=guid("b447b4dd-7780-11e0-ada3-18a90531a85a"), event_id=4, version=0)
class Microsoft_Windows_FileHistory_ConfigManager_4_0(Etw):
    pattern = Struct(
        "TargetUrl" / WString
    )


@declare(guid=guid("b447b4dd-7780-11e0-ada3-18a90531a85a"), event_id=5, version=0)
class Microsoft_Windows_FileHistory_ConfigManager_5_0(Etw):
    pattern = Struct(
        "TargetUrl" / WString
    )


@declare(guid=guid("b447b4dd-7780-11e0-ada3-18a90531a85a"), event_id=6, version=0)
class Microsoft_Windows_FileHistory_ConfigManager_6_0(Etw):
    pattern = Struct(
        "TargetUrl" / WString
    )


@declare(guid=guid("b447b4dd-7780-11e0-ada3-18a90531a85a"), event_id=7, version=0)
class Microsoft_Windows_FileHistory_ConfigManager_7_0(Etw):
    pattern = Struct(
        "OverwriteIfExists" / Int8ul
    )


@declare(guid=guid("b447b4dd-7780-11e0-ada3-18a90531a85a"), event_id=9, version=0)
class Microsoft_Windows_FileHistory_ConfigManager_9_0(Etw):
    pattern = Struct(
        "TargetUrl" / WString
    )


@declare(guid=guid("b447b4dd-7780-11e0-ada3-18a90531a85a"), event_id=11, version=0)
class Microsoft_Windows_FileHistory_ConfigManager_11_0(Etw):
    pattern = Struct(
        "TargetUrl" / WString
    )


@declare(guid=guid("b447b4dd-7780-11e0-ada3-18a90531a85a"), event_id=13, version=0)
class Microsoft_Windows_FileHistory_ConfigManager_13_0(Etw):
    pattern = Struct(
        "TargetUrl" / WString
    )

