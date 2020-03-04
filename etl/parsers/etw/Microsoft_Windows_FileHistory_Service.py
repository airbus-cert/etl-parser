# -*- coding: utf-8 -*-
"""
Microsoft-Windows-FileHistory-Service
GUID : b447b4e0-7780-11e0-ada3-18a90531a85a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b447b4e0-7780-11e0-ada3-18a90531a85a"), event_id=2, version=0)
class Microsoft_Windows_FileHistory_Service_2_0(Etw):
    pattern = Struct(
        "Result" / Int32sl,
        "ConfigFilePath" / WString
    )


@declare(guid=guid("b447b4e0-7780-11e0-ada3-18a90531a85a"), event_id=3, version=0)
class Microsoft_Windows_FileHistory_Service_3_0(Etw):
    pattern = Struct(
        "CatalogPath1" / WString,
        "CatalogPath2" / WString
    )


@declare(guid=guid("b447b4e0-7780-11e0-ada3-18a90531a85a"), event_id=4, version=0)
class Microsoft_Windows_FileHistory_Service_4_0(Etw):
    pattern = Struct(
        "Result" / Int32sl,
        "CatalogPath1" / WString,
        "CatalogPath2" / WString
    )


@declare(guid=guid("b447b4e0-7780-11e0-ada3-18a90531a85a"), event_id=5, version=0)
class Microsoft_Windows_FileHistory_Service_5_0(Etw):
    pattern = Struct(
        "ConfigFilePath" / WString
    )


@declare(guid=guid("b447b4e0-7780-11e0-ada3-18a90531a85a"), event_id=6, version=0)
class Microsoft_Windows_FileHistory_Service_6_0(Etw):
    pattern = Struct(
        "ConfigFilePath" / WString
    )


@declare(guid=guid("b447b4e0-7780-11e0-ada3-18a90531a85a"), event_id=7, version=0)
class Microsoft_Windows_FileHistory_Service_7_0(Etw):
    pattern = Struct(
        "ConfigFilePath" / WString,
        "BackupType" / Int32ul
    )


@declare(guid=guid("b447b4e0-7780-11e0-ada3-18a90531a85a"), event_id=8, version=0)
class Microsoft_Windows_FileHistory_Service_8_0(Etw):
    pattern = Struct(
        "ConfigFilePath" / WString
    )


@declare(guid=guid("b447b4e0-7780-11e0-ada3-18a90531a85a"), event_id=9, version=0)
class Microsoft_Windows_FileHistory_Service_9_0(Etw):
    pattern = Struct(
        "ConfigFilePath" / WString,
        "StopSync" / Int8ul
    )


@declare(guid=guid("b447b4e0-7780-11e0-ada3-18a90531a85a"), event_id=10, version=0)
class Microsoft_Windows_FileHistory_Service_10_0(Etw):
    pattern = Struct(
        "ConfigFilePath" / WString,
        "StopSync" / Int8ul
    )

