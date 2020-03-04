# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WMPDMCUI
GUID : 3f9e07bd-0e26-4241-a5a5-28cafa150a75
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3f9e07bd-0e26-4241-a5a5-28cafa150a75"), event_id=2001, version=0)
class Microsoft_Windows_WMPDMCUI_2001_0(Etw):
    pattern = Struct(
        "result" / Int32sl
    )


@declare(guid=guid("3f9e07bd-0e26-4241-a5a5-28cafa150a75"), event_id=2003, version=0)
class Microsoft_Windows_WMPDMCUI_2003_0(Etw):
    pattern = Struct(
        "result" / Int32sl
    )


@declare(guid=guid("3f9e07bd-0e26-4241-a5a5-28cafa150a75"), event_id=2005, version=0)
class Microsoft_Windows_WMPDMCUI_2005_0(Etw):
    pattern = Struct(
        "result" / Int32sl
    )


@declare(guid=guid("3f9e07bd-0e26-4241-a5a5-28cafa150a75"), event_id=2007, version=0)
class Microsoft_Windows_WMPDMCUI_2007_0(Etw):
    pattern = Struct(
        "result" / Int32sl
    )


@declare(guid=guid("3f9e07bd-0e26-4241-a5a5-28cafa150a75"), event_id=2009, version=0)
class Microsoft_Windows_WMPDMCUI_2009_0(Etw):
    pattern = Struct(
        "result" / Int32sl
    )


@declare(guid=guid("3f9e07bd-0e26-4241-a5a5-28cafa150a75"), event_id=2011, version=0)
class Microsoft_Windows_WMPDMCUI_2011_0(Etw):
    pattern = Struct(
        "result" / Int32sl
    )


@declare(guid=guid("3f9e07bd-0e26-4241-a5a5-28cafa150a75"), event_id=2012, version=0)
class Microsoft_Windows_WMPDMCUI_2012_0(Etw):
    pattern = Struct(
        "UDN" / WString
    )


@declare(guid=guid("3f9e07bd-0e26-4241-a5a5-28cafa150a75"), event_id=2013, version=0)
class Microsoft_Windows_WMPDMCUI_2013_0(Etw):
    pattern = Struct(
        "UDN" / WString
    )


@declare(guid=guid("3f9e07bd-0e26-4241-a5a5-28cafa150a75"), event_id=2014, version=0)
class Microsoft_Windows_WMPDMCUI_2014_0(Etw):
    pattern = Struct(
        "UDN" / WString
    )


@declare(guid=guid("3f9e07bd-0e26-4241-a5a5-28cafa150a75"), event_id=2015, version=0)
class Microsoft_Windows_WMPDMCUI_2015_0(Etw):
    pattern = Struct(
        "UDN" / WString
    )


@declare(guid=guid("3f9e07bd-0e26-4241-a5a5-28cafa150a75"), event_id=2016, version=0)
class Microsoft_Windows_WMPDMCUI_2016_0(Etw):
    pattern = Struct(
        "UDN" / WString
    )


@declare(guid=guid("3f9e07bd-0e26-4241-a5a5-28cafa150a75"), event_id=2017, version=0)
class Microsoft_Windows_WMPDMCUI_2017_0(Etw):
    pattern = Struct(
        "UDN" / WString,
        "fRenderAlreadyExists" / Int8ul,
        "result" / Int32sl,
        "failureReason" / Int32sl
    )


@declare(guid=guid("3f9e07bd-0e26-4241-a5a5-28cafa150a75"), event_id=2020, version=0)
class Microsoft_Windows_WMPDMCUI_2020_0(Etw):
    pattern = Struct(
        "result" / Int32sl,
        "failureReason" / Int32sl
    )


@declare(guid=guid("3f9e07bd-0e26-4241-a5a5-28cafa150a75"), event_id=2021, version=0)
class Microsoft_Windows_WMPDMCUI_2021_0(Etw):
    pattern = Struct(
        "UDN" / WString
    )


@declare(guid=guid("3f9e07bd-0e26-4241-a5a5-28cafa150a75"), event_id=2022, version=0)
class Microsoft_Windows_WMPDMCUI_2022_0(Etw):
    pattern = Struct(
        "UDN" / WString,
        "result" / Int32sl
    )


@declare(guid=guid("3f9e07bd-0e26-4241-a5a5-28cafa150a75"), event_id=2023, version=0)
class Microsoft_Windows_WMPDMCUI_2023_0(Etw):
    pattern = Struct(
        "UDN" / WString,
        "URI" / WString
    )


@declare(guid=guid("3f9e07bd-0e26-4241-a5a5-28cafa150a75"), event_id=2024, version=0)
class Microsoft_Windows_WMPDMCUI_2024_0(Etw):
    pattern = Struct(
        "UDN" / WString,
        "URI" / WString,
        "result" / Int32sl
    )


@declare(guid=guid("3f9e07bd-0e26-4241-a5a5-28cafa150a75"), event_id=2025, version=0)
class Microsoft_Windows_WMPDMCUI_2025_0(Etw):
    pattern = Struct(
        "UDN" / WString
    )


@declare(guid=guid("3f9e07bd-0e26-4241-a5a5-28cafa150a75"), event_id=2026, version=0)
class Microsoft_Windows_WMPDMCUI_2026_0(Etw):
    pattern = Struct(
        "UDN" / WString,
        "result" / Int32sl
    )

