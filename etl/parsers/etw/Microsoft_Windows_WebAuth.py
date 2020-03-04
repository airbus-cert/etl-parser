# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WebAuth
GUID : db6972b6-dddf-4820-84b1-2ed6ac0b96e5
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1000, version=0)
class Microsoft_Windows_WebAuth_1000_0(Etw):
    pattern = Struct(
        "StartUrl" / WString,
        "TerminateUrl" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1001, version=0)
class Microsoft_Windows_WebAuth_1001_0(Etw):
    pattern = Struct(
        "StartUrl" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1002, version=0)
class Microsoft_Windows_WebAuth_1002_0(Etw):
    pattern = Struct(
        "Url" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1003, version=0)
class Microsoft_Windows_WebAuth_1003_0(Etw):
    pattern = Struct(
        "Url" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1010, version=0)
class Microsoft_Windows_WebAuth_1010_0(Etw):
    pattern = Struct(
        "Url" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1011, version=0)
class Microsoft_Windows_WebAuth_1011_0(Etw):
    pattern = Struct(
        "Url" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1020, version=0)
class Microsoft_Windows_WebAuth_1020_0(Etw):
    pattern = Struct(
        "RedirectedUrl" / WString,
        "OriginalUrl" / WString,
        "HttpStatusCode" / Int32ul
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1021, version=0)
class Microsoft_Windows_WebAuth_1021_0(Etw):
    pattern = Struct(
        "Url" / WString,
        "ReferrerUrl" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1022, version=0)
class Microsoft_Windows_WebAuth_1022_0(Etw):
    pattern = Struct(
        "Url" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1023, version=0)
class Microsoft_Windows_WebAuth_1023_0(Etw):
    pattern = Struct(
        "Url" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1024, version=0)
class Microsoft_Windows_WebAuth_1024_0(Etw):
    pattern = Struct(
        "Url" / WString,
        "ReferrerUrl" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1040, version=0)
class Microsoft_Windows_WebAuth_1040_0(Etw):
    pattern = Struct(
        "Url" / WString,
        "TerminateUrl" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1041, version=0)
class Microsoft_Windows_WebAuth_1041_0(Etw):
    pattern = Struct(
        "Title" / WString,
        "Url" / WString,
        "TerminateUrl" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1043, version=0)
class Microsoft_Windows_WebAuth_1043_0(Etw):
    pattern = Struct(
        "Post" / WString,
        "Url" / WString,
        "TerminateUrl" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1050, version=0)
class Microsoft_Windows_WebAuth_1050_0(Etw):
    pattern = Struct(
        "Url" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1051, version=0)
class Microsoft_Windows_WebAuth_1051_0(Etw):
    pattern = Struct(
        "Url" / WString,
        "HttpStatusCode" / Int32ul
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1100, version=0)
class Microsoft_Windows_WebAuth_1100_0(Etw):
    pattern = Struct(
        "Problem" / Int32ul
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1101, version=0)
class Microsoft_Windows_WebAuth_1101_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1200, version=0)
class Microsoft_Windows_WebAuth_1200_0(Etw):
    pattern = Struct(
        "Action" / Int32ul,
        "Url" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1201, version=0)
class Microsoft_Windows_WebAuth_1201_0(Etw):
    pattern = Struct(
        "Action" / Int32ul,
        "Url" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1202, version=0)
class Microsoft_Windows_WebAuth_1202_0(Etw):
    pattern = Struct(
        "Action" / Int32ul,
        "Url" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1203, version=0)
class Microsoft_Windows_WebAuth_1203_0(Etw):
    pattern = Struct(
        "Url" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1204, version=0)
class Microsoft_Windows_WebAuth_1204_0(Etw):
    pattern = Struct(
        "Url" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1205, version=0)
class Microsoft_Windows_WebAuth_1205_0(Etw):
    pattern = Struct(
        "Url" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1206, version=0)
class Microsoft_Windows_WebAuth_1206_0(Etw):
    pattern = Struct(
        "Url" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1300, version=0)
class Microsoft_Windows_WebAuth_1300_0(Etw):
    pattern = Struct(
        "Clsid" / Guid,
        "Url" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1301, version=0)
class Microsoft_Windows_WebAuth_1301_0(Etw):
    pattern = Struct(
        "Clsid" / Guid,
        "Url" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1310, version=0)
class Microsoft_Windows_WebAuth_1310_0(Etw):
    pattern = Struct(
        "Clsid" / Guid,
        "Url" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1311, version=0)
class Microsoft_Windows_WebAuth_1311_0(Etw):
    pattern = Struct(
        "Clsid" / Guid,
        "Url" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1400, version=0)
class Microsoft_Windows_WebAuth_1400_0(Etw):
    pattern = Struct(
        "Content" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1401, version=0)
class Microsoft_Windows_WebAuth_1401_0(Etw):
    pattern = Struct(
        "Url" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1402, version=0)
class Microsoft_Windows_WebAuth_1402_0(Etw):
    pattern = Struct(
        "Content" / WString,
        "ConvertedValue" / Int32ul
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1403, version=0)
class Microsoft_Windows_WebAuth_1403_0(Etw):
    pattern = Struct(
        "Content" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1404, version=0)
class Microsoft_Windows_WebAuth_1404_0(Etw):
    pattern = Struct(
        "Url" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1405, version=0)
class Microsoft_Windows_WebAuth_1405_0(Etw):
    pattern = Struct(
        "Url" / WString
    )


@declare(guid=guid("db6972b6-dddf-4820-84b1-2ed6ac0b96e5"), event_id=1406, version=0)
class Microsoft_Windows_WebAuth_1406_0(Etw):
    pattern = Struct(
        "Url" / WString,
        "StatusCode" / Int32ul
    )

