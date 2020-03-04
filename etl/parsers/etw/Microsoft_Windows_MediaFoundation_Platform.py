# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MediaFoundation-Platform
GUID : bc97b970-d001-482f-8745-b8d7d5759f99
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=1, version=0)
class Microsoft_Windows_MediaFoundation_Platform_1_0(Etw):
    pattern = Struct(
        "clsid" / Guid
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=2, version=0)
class Microsoft_Windows_MediaFoundation_Platform_2_0(Etw):
    pattern = Struct(
        "clsid" / Guid
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=3, version=0)
class Microsoft_Windows_MediaFoundation_Platform_3_0(Etw):
    pattern = Struct(
        "clsid" / Guid,
        "Disabled" / Int8ul
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=4, version=0)
class Microsoft_Windows_MediaFoundation_Platform_4_0(Etw):
    pattern = Struct(
        "clsid" / Guid,
        "Disabled" / Int8ul
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=5, version=0)
class Microsoft_Windows_MediaFoundation_Platform_5_0(Etw):
    pattern = Struct(
        "clsid" / Guid,
        "Selector" / WString
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=6, version=0)
class Microsoft_Windows_MediaFoundation_Platform_6_0(Etw):
    pattern = Struct(
        "clsid" / Guid,
        "Selector" / WString
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=7, version=0)
class Microsoft_Windows_MediaFoundation_Platform_7_0(Etw):
    pattern = Struct(
        "clsid" / Guid,
        "Selector" / WString
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=8, version=0)
class Microsoft_Windows_MediaFoundation_Platform_8_0(Etw):
    pattern = Struct(
        "clsid" / Guid,
        "Selector" / WString
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=9, version=0)
class Microsoft_Windows_MediaFoundation_Platform_9_0(Etw):
    pattern = Struct(
        "clsid" / Guid,
        "Selector" / WString
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=10, version=0)
class Microsoft_Windows_MediaFoundation_Platform_10_0(Etw):
    pattern = Struct(
        "Selector" / WString
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=11, version=0)
class Microsoft_Windows_MediaFoundation_Platform_11_0(Etw):
    pattern = Struct(
        "clsid" / Guid,
        "Disabled" / Int8ul
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=12, version=0)
class Microsoft_Windows_MediaFoundation_Platform_12_0(Etw):
    pattern = Struct(
        "clsid" / Guid,
        "Selector" / WString
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=13, version=0)
class Microsoft_Windows_MediaFoundation_Platform_13_0(Etw):
    pattern = Struct(
        "Selector" / WString
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=14, version=0)
class Microsoft_Windows_MediaFoundation_Platform_14_0(Etw):
    pattern = Struct(
        "clsid" / Guid,
        "Disabled" / Int8ul
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=15, version=0)
class Microsoft_Windows_MediaFoundation_Platform_15_0(Etw):
    pattern = Struct(
        "MFTName" / WString
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=16, version=0)
class Microsoft_Windows_MediaFoundation_Platform_16_0(Etw):
    pattern = Struct(
        "MFTName" / WString
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=17, version=0)
class Microsoft_Windows_MediaFoundation_Platform_17_0(Etw):
    pattern = Struct(
        "MFTName" / WString
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=18, version=0)
class Microsoft_Windows_MediaFoundation_Platform_18_0(Etw):
    pattern = Struct(
        "Category" / Guid
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=19, version=0)
class Microsoft_Windows_MediaFoundation_Platform_19_0(Etw):
    pattern = Struct(
        "LinkName" / WString,
        "FriendlyName" / WString
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=20, version=0)
class Microsoft_Windows_MediaFoundation_Platform_20_0(Etw):
    pattern = Struct(
        "Category" / Guid
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=21, version=0)
class Microsoft_Windows_MediaFoundation_Platform_21_0(Etw):
    pattern = Struct(
        "dwType" / Int32ul,
        "dwConfig" / Int32ul
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=100, version=0)
class Microsoft_Windows_MediaFoundation_Platform_100_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=102, version=0)
class Microsoft_Windows_MediaFoundation_Platform_102_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=103, version=0)
class Microsoft_Windows_MediaFoundation_Platform_103_0(Etw):
    pattern = Struct(
        "Type" / Int32sl,
        "KeyName" / WString,
        "lResult" / Int32sl
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=104, version=0)
class Microsoft_Windows_MediaFoundation_Platform_104_0(Etw):
    pattern = Struct(
        "Type" / Int32sl,
        "KeyName" / WString,
        "ValueName" / WString,
        "lResult" / Int32sl,
        "QuerySize" / Int8ul,
        "ValueDWORD" / Int32ul
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=105, version=0)
class Microsoft_Windows_MediaFoundation_Platform_105_0(Etw):
    pattern = Struct(
        "Type" / Int32sl,
        "KeyName" / WString,
        "ValueName" / WString,
        "lResult" / Int32sl,
        "QuerySize" / Int8ul,
        "ValueString" / WString
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=200, version=0)
class Microsoft_Windows_MediaFoundation_Platform_200_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "url" / WString,
        "hr" / Int32ul
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=201, version=0)
class Microsoft_Windows_MediaFoundation_Platform_201_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "clsid" / WString
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=202, version=0)
class Microsoft_Windows_MediaFoundation_Platform_202_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "clsid" / WString
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=203, version=0)
class Microsoft_Windows_MediaFoundation_Platform_203_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=204, version=0)
class Microsoft_Windows_MediaFoundation_Platform_204_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=205, version=0)
class Microsoft_Windows_MediaFoundation_Platform_205_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "url" / WString,
        "hr" / Int32ul
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=206, version=0)
class Microsoft_Windows_MediaFoundation_Platform_206_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "Line" / Int32sl,
        "hr" / Int32ul,
        "function" / CString
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=207, version=0)
class Microsoft_Windows_MediaFoundation_Platform_207_0(Etw):
    pattern = Struct(
        "stream" / Int64ul,
        "offset" / Int64sl,
        "length" / Int32sl,
        "buffer" / Int64ul
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=208, version=0)
class Microsoft_Windows_MediaFoundation_Platform_208_0(Etw):
    pattern = Struct(
        "stream" / Int64ul,
        "length" / Int32sl,
        "buffer" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=300, version=0)
class Microsoft_Windows_MediaFoundation_Platform_300_0(Etw):
    pattern = Struct(
        "flags" / Int32ul,
        "Category" / Guid,
        "inputType" / Guid,
        "inputSubtype" / Guid,
        "outputType" / Guid,
        "outputSubtype" / Guid
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=301, version=0)
class Microsoft_Windows_MediaFoundation_Platform_301_0(Etw):
    pattern = Struct(
        "clsid" / WString
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=302, version=0)
class Microsoft_Windows_MediaFoundation_Platform_302_0(Etw):
    pattern = Struct(
        "string" / WString
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=303, version=0)
class Microsoft_Windows_MediaFoundation_Platform_303_0(Etw):
    pattern = Struct(
        "string" / WString
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=304, version=0)
class Microsoft_Windows_MediaFoundation_Platform_304_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "localMFTs" / Int32ul,
        "hardwareMFTs" / Int32ul,
        "MFTs" / Int32ul
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=305, version=0)
class Microsoft_Windows_MediaFoundation_Platform_305_0(Etw):
    pattern = Struct(
        "flags" / Int32ul,
        "Category" / Guid,
        "inputType" / Guid,
        "inputSubtype" / Guid,
        "outputType" / Guid,
        "outputSubtype" / Guid,
        "luidSet" / Int8ul
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=306, version=0)
class Microsoft_Windows_MediaFoundation_Platform_306_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "numMFTs" / Int32ul,
        "adapterVendorId" / Int32ul,
        "adapterDeviceId" / Int32ul,
        "adapterSubSysId" / Int32ul,
        "adapterRevision" / Int32ul
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=2501, version=0)
class Microsoft_Windows_MediaFoundation_Platform_2501_0(Etw):
    pattern = Struct(
        "Merit" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=2502, version=0)
class Microsoft_Windows_MediaFoundation_Platform_2502_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=2503, version=0)
class Microsoft_Windows_MediaFoundation_Platform_2503_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=2504, version=0)
class Microsoft_Windows_MediaFoundation_Platform_2504_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("bc97b970-d001-482f-8745-b8d7d5759f99"), event_id=2505, version=0)
class Microsoft_Windows_MediaFoundation_Platform_2505_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )

