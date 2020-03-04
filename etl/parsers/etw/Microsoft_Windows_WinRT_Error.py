# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WinRT-Error
GUID : a86f8471-c31d-4fbc-a035-665d06047b03
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a86f8471-c31d-4fbc-a035-665d06047b03"), event_id=1, version=0)
class Microsoft_Windows_WinRT_Error_1_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32sl,
        "ErrorMesage" / WString
    )


@declare(guid=guid("a86f8471-c31d-4fbc-a035-665d06047b03"), event_id=2, version=0)
class Microsoft_Windows_WinRT_Error_2_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32sl,
        "ErrorMesage" / WString,
        "LanguageErrorPointer" / Int64ul
    )


@declare(guid=guid("a86f8471-c31d-4fbc-a035-665d06047b03"), event_id=3, version=0)
class Microsoft_Windows_WinRT_Error_3_0(Etw):
    pattern = Struct(
        "OriginalHRESULT" / Int32sl,
        "NewHRESULT" / Int32sl,
        "ErrorMesage" / WString
    )

