# -*- coding: utf-8 -*-
"""
Microsoft-Windows-FileHistory-Core
GUID : b447b4db-7780-11e0-ada3-18a90531a85a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b447b4db-7780-11e0-ada3-18a90531a85a"), event_id=100, version=0)
class Microsoft_Windows_FileHistory_Core_100_0(Etw):
    pattern = Struct(
        "hc_stateid" / Int32ul,
        "ProtectedUpToTime" / WString
    )


@declare(guid=guid("b447b4db-7780-11e0-ada3-18a90531a85a"), event_id=200, version=0)
class Microsoft_Windows_FileHistory_Core_200_0(Etw):
    pattern = Struct(
        "HighLevelHr" / Int32ul,
        "LowLevelHr" / Int32ul,
        "ConfigFilePath" / WString
    )


@declare(guid=guid("b447b4db-7780-11e0-ada3-18a90531a85a"), event_id=201, version=0)
class Microsoft_Windows_FileHistory_Core_201_0(Etw):
    pattern = Struct(
        "Hr" / Int32ul,
        "ConfigFilePath" / WString
    )


@declare(guid=guid("b447b4db-7780-11e0-ada3-18a90531a85a"), event_id=202, version=0)
class Microsoft_Windows_FileHistory_Core_202_0(Etw):
    pattern = Struct(
        "Hr" / Int32ul,
        "ConfigFilePath" / WString
    )


@declare(guid=guid("b447b4db-7780-11e0-ada3-18a90531a85a"), event_id=203, version=0)
class Microsoft_Windows_FileHistory_Core_203_0(Etw):
    pattern = Struct(
        "Hr" / Int32ul,
        "ConfigFilePath" / WString
    )


@declare(guid=guid("b447b4db-7780-11e0-ada3-18a90531a85a"), event_id=204, version=0)
class Microsoft_Windows_FileHistory_Core_204_0(Etw):
    pattern = Struct(
        "Hr" / Int32ul,
        "ConfigFilePath" / WString
    )


@declare(guid=guid("b447b4db-7780-11e0-ada3-18a90531a85a"), event_id=205, version=0)
class Microsoft_Windows_FileHistory_Core_205_0(Etw):
    pattern = Struct(
        "Message" / WString
    )

