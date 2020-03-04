# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ApplicationExperience-Cache
GUID : 6d8a3a60-40af-445a-98ca-99359e500146
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6d8a3a60-40af-445a-98ca-99359e500146"), event_id=3, version=0)
class Microsoft_Windows_ApplicationExperience_Cache_3_0(Etw):
    pattern = Struct(
        "OperationalMessage" / CString
    )


@declare(guid=guid("6d8a3a60-40af-445a-98ca-99359e500146"), event_id=4, version=0)
class Microsoft_Windows_ApplicationExperience_Cache_4_0(Etw):
    pattern = Struct(
        "InfoMessage" / CString
    )


@declare(guid=guid("6d8a3a60-40af-445a-98ca-99359e500146"), event_id=5, version=0)
class Microsoft_Windows_ApplicationExperience_Cache_5_0(Etw):
    pattern = Struct(
        "DebugMessage" / CString
    )


@declare(guid=guid("6d8a3a60-40af-445a-98ca-99359e500146"), event_id=6, version=0)
class Microsoft_Windows_ApplicationExperience_Cache_6_0(Etw):
    pattern = Struct(
        "Matches" / Int8ul,
        "CheckerName" / WString,
        "AttributeName" / WString,
        "AttributeExpectedValue" / CString
    )


@declare(guid=guid("6d8a3a60-40af-445a-98ca-99359e500146"), event_id=7, version=0)
class Microsoft_Windows_ApplicationExperience_Cache_7_0(Etw):
    pattern = Struct(
        "Matches" / Int8ul,
        "CheckerName" / WString,
        "AttributeName" / WString,
        "AttributeExpectedValue" / WString
    )


@declare(guid=guid("6d8a3a60-40af-445a-98ca-99359e500146"), event_id=8, version=0)
class Microsoft_Windows_ApplicationExperience_Cache_8_0(Etw):
    pattern = Struct(
        "Matches" / Int8ul,
        "CheckerName" / WString,
        "AttributeName" / WString,
        "AttributeExpectedValue" / Int32ul
    )


@declare(guid=guid("6d8a3a60-40af-445a-98ca-99359e500146"), event_id=9, version=0)
class Microsoft_Windows_ApplicationExperience_Cache_9_0(Etw):
    pattern = Struct(
        "Matches" / Int8ul,
        "CheckerName" / WString,
        "AttributeName" / WString,
        "AttributeExpectedValue" / Int64ul
    )

