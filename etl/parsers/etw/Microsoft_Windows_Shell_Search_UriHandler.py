# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Shell-Search-UriHandler
GUID : 606c6fe0-a9dc-4a9d-bdea-830aff6716e7
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("606c6fe0-a9dc-4a9d-bdea-830aff6716e7"), event_id=101, version=0)
class Microsoft_Windows_Shell_Search_UriHandler_101_0(Etw):
    pattern = Struct(
        "Uri" / WString
    )


@declare(guid=guid("606c6fe0-a9dc-4a9d-bdea-830aff6716e7"), event_id=102, version=0)
class Microsoft_Windows_Shell_Search_UriHandler_102_0(Etw):
    pattern = Struct(
        "Uri" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("606c6fe0-a9dc-4a9d-bdea-830aff6716e7"), event_id=201, version=0)
class Microsoft_Windows_Shell_Search_UriHandler_201_0(Etw):
    pattern = Struct(
        "Uri" / WString
    )


@declare(guid=guid("606c6fe0-a9dc-4a9d-bdea-830aff6716e7"), event_id=202, version=0)
class Microsoft_Windows_Shell_Search_UriHandler_202_0(Etw):
    pattern = Struct(
        "Scheme" / WString
    )


@declare(guid=guid("606c6fe0-a9dc-4a9d-bdea-830aff6716e7"), event_id=203, version=0)
class Microsoft_Windows_Shell_Search_UriHandler_203_0(Etw):
    pattern = Struct(
        "SearchView" / WString
    )


@declare(guid=guid("606c6fe0-a9dc-4a9d-bdea-830aff6716e7"), event_id=204, version=0)
class Microsoft_Windows_Shell_Search_UriHandler_204_0(Etw):
    pattern = Struct(
        "Uri" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("606c6fe0-a9dc-4a9d-bdea-830aff6716e7"), event_id=301, version=0)
class Microsoft_Windows_Shell_Search_UriHandler_301_0(Etw):
    pattern = Struct(
        "Parameter" / WString
    )


@declare(guid=guid("606c6fe0-a9dc-4a9d-bdea-830aff6716e7"), event_id=302, version=0)
class Microsoft_Windows_Shell_Search_UriHandler_302_0(Etw):
    pattern = Struct(
        "Parameter" / WString,
        "ParameterValue" / WString
    )


@declare(guid=guid("606c6fe0-a9dc-4a9d-bdea-830aff6716e7"), event_id=303, version=0)
class Microsoft_Windows_Shell_Search_UriHandler_303_0(Etw):
    pattern = Struct(
        "Parameter" / WString,
        "ParameterValue" / WString
    )


@declare(guid=guid("606c6fe0-a9dc-4a9d-bdea-830aff6716e7"), event_id=304, version=0)
class Microsoft_Windows_Shell_Search_UriHandler_304_0(Etw):
    pattern = Struct(
        "Parameter" / WString,
        "Value" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("606c6fe0-a9dc-4a9d-bdea-830aff6716e7"), event_id=305, version=0)
class Microsoft_Windows_Shell_Search_UriHandler_305_0(Etw):
    pattern = Struct(
        "Parameter" / WString,
        "OldValue" / WString,
        "NewValue" / WString
    )


@declare(guid=guid("606c6fe0-a9dc-4a9d-bdea-830aff6716e7"), event_id=306, version=0)
class Microsoft_Windows_Shell_Search_UriHandler_306_0(Etw):
    pattern = Struct(
        "Parameter" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("606c6fe0-a9dc-4a9d-bdea-830aff6716e7"), event_id=402, version=0)
class Microsoft_Windows_Shell_Search_UriHandler_402_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )

