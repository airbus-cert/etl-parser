# -*- coding: utf-8 -*-
"""
Microsoft-Windows-OLEACC
GUID : 19d2c934-ee9b-49e5-aaeb-9cce721d2c65
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("19d2c934-ee9b-49e5-aaeb-9cce721d2c65"), event_id=1, version=0)
class Microsoft_Windows_OLEACC_1_0(Etw):
    pattern = Struct(
        "Method" / WString,
        "Hresult" / Int32ul,
        "Details" / WString,
        "SourceHwnd" / WString,
        "Provider" / WString
    )


@declare(guid=guid("19d2c934-ee9b-49e5-aaeb-9cce721d2c65"), event_id=2, version=0)
class Microsoft_Windows_OLEACC_2_0(Etw):
    pattern = Struct(
        "MethodIndex" / Int32ul,
        "Object" / Int64ul,
        "Parameter" / Int32sl
    )


@declare(guid=guid("19d2c934-ee9b-49e5-aaeb-9cce721d2c65"), event_id=3, version=0)
class Microsoft_Windows_OLEACC_3_0(Etw):
    pattern = Struct(
        "MethodIndex" / Int32ul,
        "Object" / Int64ul,
        "Parameter" / Int32sl
    )

