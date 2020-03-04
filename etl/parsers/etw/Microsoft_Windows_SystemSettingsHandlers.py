# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SystemSettingsHandlers
GUID : fbbd52e1-df97-529d-4b67-53f67da99a98
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("fbbd52e1-df97-529d-4b67-53f67da99a98"), event_id=100, version=0)
class Microsoft_Windows_SystemSettingsHandlers_100_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("fbbd52e1-df97-529d-4b67-53f67da99a98"), event_id=101, version=0)
class Microsoft_Windows_SystemSettingsHandlers_101_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Pfn" / WString,
        "Arguments" / WString
    )


@declare(guid=guid("fbbd52e1-df97-529d-4b67-53f67da99a98"), event_id=102, version=0)
class Microsoft_Windows_SystemSettingsHandlers_102_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Pfns" / WString
    )


@declare(guid=guid("fbbd52e1-df97-529d-4b67-53f67da99a98"), event_id=103, version=0)
class Microsoft_Windows_SystemSettingsHandlers_103_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("fbbd52e1-df97-529d-4b67-53f67da99a98"), event_id=200, version=0)
class Microsoft_Windows_SystemSettingsHandlers_200_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("fbbd52e1-df97-529d-4b67-53f67da99a98"), event_id=201, version=0)
class Microsoft_Windows_SystemSettingsHandlers_201_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Pfn" / WString,
        "Arguments" / WString
    )


@declare(guid=guid("fbbd52e1-df97-529d-4b67-53f67da99a98"), event_id=202, version=0)
class Microsoft_Windows_SystemSettingsHandlers_202_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Pfns" / WString
    )

