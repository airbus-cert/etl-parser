# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ThemeUI
GUID : 869fb599-80aa-485d-bca7-db18d72b7219
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("869fb599-80aa-485d-bca7-db18d72b7219"), event_id=0, version=0)
class Microsoft_Windows_ThemeUI_0_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("869fb599-80aa-485d-bca7-db18d72b7219"), event_id=1, version=0)
class Microsoft_Windows_ThemeUI_1_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("869fb599-80aa-485d-bca7-db18d72b7219"), event_id=2, version=0)
class Microsoft_Windows_ThemeUI_2_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("869fb599-80aa-485d-bca7-db18d72b7219"), event_id=3, version=0)
class Microsoft_Windows_ThemeUI_3_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("869fb599-80aa-485d-bca7-db18d72b7219"), event_id=6, version=0)
class Microsoft_Windows_ThemeUI_6_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("869fb599-80aa-485d-bca7-db18d72b7219"), event_id=7, version=0)
class Microsoft_Windows_ThemeUI_7_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("869fb599-80aa-485d-bca7-db18d72b7219"), event_id=9, version=0)
class Microsoft_Windows_ThemeUI_9_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("869fb599-80aa-485d-bca7-db18d72b7219"), event_id=13, version=0)
class Microsoft_Windows_ThemeUI_13_0(Etw):
    pattern = Struct(
        "type" / Int32ul,
        "pszBackgroundFile" / WString
    )


@declare(guid=guid("869fb599-80aa-485d-bca7-db18d72b7219"), event_id=14, version=0)
class Microsoft_Windows_ThemeUI_14_0(Etw):
    pattern = Struct(
        "type" / Int32ul,
        "dwColor" / Int32ul
    )

