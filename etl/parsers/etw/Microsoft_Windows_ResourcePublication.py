# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ResourcePublication
GUID : 74c2135f-cc76-45c3-879a-ef3bb1eeaf86
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("74c2135f-cc76-45c3-879a-ef3bb1eeaf86"), event_id=100, version=0)
class Microsoft_Windows_ResourcePublication_100_0(Etw):
    pattern = Struct(
        "Argument" / WString
    )


@declare(guid=guid("74c2135f-cc76-45c3-879a-ef3bb1eeaf86"), event_id=101, version=0)
class Microsoft_Windows_ResourcePublication_101_0(Etw):
    pattern = Struct(
        "Argument" / WString
    )


@declare(guid=guid("74c2135f-cc76-45c3-879a-ef3bb1eeaf86"), event_id=102, version=0)
class Microsoft_Windows_ResourcePublication_102_0(Etw):
    pattern = Struct(
        "Argument" / WString
    )


@declare(guid=guid("74c2135f-cc76-45c3-879a-ef3bb1eeaf86"), event_id=103, version=0)
class Microsoft_Windows_ResourcePublication_103_0(Etw):
    pattern = Struct(
        "Argument" / WString
    )


@declare(guid=guid("74c2135f-cc76-45c3-879a-ef3bb1eeaf86"), event_id=104, version=0)
class Microsoft_Windows_ResourcePublication_104_0(Etw):
    pattern = Struct(
        "Argument" / WString
    )


@declare(guid=guid("74c2135f-cc76-45c3-879a-ef3bb1eeaf86"), event_id=1000, version=0)
class Microsoft_Windows_ResourcePublication_1000_0(Etw):
    pattern = Struct(
        "Argument" / WString
    )


@declare(guid=guid("74c2135f-cc76-45c3-879a-ef3bb1eeaf86"), event_id=1001, version=0)
class Microsoft_Windows_ResourcePublication_1001_0(Etw):
    pattern = Struct(
        "Argument" / WString
    )


@declare(guid=guid("74c2135f-cc76-45c3-879a-ef3bb1eeaf86"), event_id=1002, version=0)
class Microsoft_Windows_ResourcePublication_1002_0(Etw):
    pattern = Struct(
        "Argument" / WString
    )


@declare(guid=guid("74c2135f-cc76-45c3-879a-ef3bb1eeaf86"), event_id=1003, version=0)
class Microsoft_Windows_ResourcePublication_1003_0(Etw):
    pattern = Struct(
        "Function" / WString,
        "HRESULT" / Int32ul,
        "Line" / Int32ul,
        "Filename" / CString
    )


@declare(guid=guid("74c2135f-cc76-45c3-879a-ef3bb1eeaf86"), event_id=1004, version=0)
class Microsoft_Windows_ResourcePublication_1004_0(Etw):
    pattern = Struct(
        "Argument" / WString
    )

