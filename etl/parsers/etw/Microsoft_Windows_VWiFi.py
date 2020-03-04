# -*- coding: utf-8 -*-
"""
Microsoft-Windows-VWiFi
GUID : 314b2b0d-81ee-4474-b6e0-c2aaec0ddbde
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("314b2b0d-81ee-4474-b6e0-c2aaec0ddbde"), event_id=25001, version=0)
class Microsoft_Windows_VWiFi_25001_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "FriendlyName" / WString
    )


@declare(guid=guid("314b2b0d-81ee-4474-b6e0-c2aaec0ddbde"), event_id=25002, version=0)
class Microsoft_Windows_VWiFi_25002_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "FriendlyName" / WString
    )


@declare(guid=guid("314b2b0d-81ee-4474-b6e0-c2aaec0ddbde"), event_id=25003, version=0)
class Microsoft_Windows_VWiFi_25003_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "FriendlyName" / WString,
        "VIfGuid" / Guid
    )


@declare(guid=guid("314b2b0d-81ee-4474-b6e0-c2aaec0ddbde"), event_id=25004, version=0)
class Microsoft_Windows_VWiFi_25004_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "FriendlyName" / WString,
        "VIfGuid" / Guid
    )

