# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ThemeCPL
GUID : 61f044af-9104-4ca5-81ee-cb6c51bb01ab
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("61f044af-9104-4ca5-81ee-cb6c51bb01ab"), event_id=4, version=0)
class Microsoft_Windows_ThemeCPL_4_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("61f044af-9104-4ca5-81ee-cb6c51bb01ab"), event_id=8, version=0)
class Microsoft_Windows_ThemeCPL_8_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("61f044af-9104-4ca5-81ee-cb6c51bb01ab"), event_id=13, version=0)
class Microsoft_Windows_ThemeCPL_13_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("61f044af-9104-4ca5-81ee-cb6c51bb01ab"), event_id=14, version=0)
class Microsoft_Windows_ThemeCPL_14_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("61f044af-9104-4ca5-81ee-cb6c51bb01ab"), event_id=15, version=0)
class Microsoft_Windows_ThemeCPL_15_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("61f044af-9104-4ca5-81ee-cb6c51bb01ab"), event_id=16, version=0)
class Microsoft_Windows_ThemeCPL_16_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("61f044af-9104-4ca5-81ee-cb6c51bb01ab"), event_id=17, version=0)
class Microsoft_Windows_ThemeCPL_17_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("61f044af-9104-4ca5-81ee-cb6c51bb01ab"), event_id=24, version=0)
class Microsoft_Windows_ThemeCPL_24_0(Etw):
    pattern = Struct(
        "dwColorsChanged" / Int32ul
    )


@declare(guid=guid("61f044af-9104-4ca5-81ee-cb6c51bb01ab"), event_id=25, version=0)
class Microsoft_Windows_ThemeCPL_25_0(Etw):
    pattern = Struct(
        "dwColorsChanged" / Int32ul
    )


@declare(guid=guid("61f044af-9104-4ca5-81ee-cb6c51bb01ab"), event_id=26, version=0)
class Microsoft_Windows_ThemeCPL_26_0(Etw):
    pattern = Struct(
        "dwColorsChanged" / Int32ul
    )


@declare(guid=guid("61f044af-9104-4ca5-81ee-cb6c51bb01ab"), event_id=27, version=0)
class Microsoft_Windows_ThemeCPL_27_0(Etw):
    pattern = Struct(
        "dwColorsChanged" / Int32ul
    )

