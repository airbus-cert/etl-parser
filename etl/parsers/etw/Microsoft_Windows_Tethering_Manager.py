# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Tethering-Manager
GUID : cc311f1f-623c-4ca4-ba44-a458016555e8
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("cc311f1f-623c-4ca4-ba44-a458016555e8"), event_id=1000, version=0)
class Microsoft_Windows_Tethering_Manager_1000_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("cc311f1f-623c-4ca4-ba44-a458016555e8"), event_id=1002, version=0)
class Microsoft_Windows_Tethering_Manager_1002_0(Etw):
    pattern = Struct(
        "TetheringStartResult" / Int32ul,
        "EntitlementCheckCompletionTime" / Int32ul,
        "MbConnectCompletionTime" / Int32ul,
        "ApStartCompletionTime" / Int32ul,
        "IcsStartCompletionTime" / Int32ul
    )


@declare(guid=guid("cc311f1f-623c-4ca4-ba44-a458016555e8"), event_id=1004, version=0)
class Microsoft_Windows_Tethering_Manager_1004_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "CompletedTime" / Int32ul
    )


@declare(guid=guid("cc311f1f-623c-4ca4-ba44-a458016555e8"), event_id=1005, version=0)
class Microsoft_Windows_Tethering_Manager_1005_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "CompletedTime" / Int32ul
    )


@declare(guid=guid("cc311f1f-623c-4ca4-ba44-a458016555e8"), event_id=1006, version=0)
class Microsoft_Windows_Tethering_Manager_1006_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "CompletedTime" / Int32ul
    )


@declare(guid=guid("cc311f1f-623c-4ca4-ba44-a458016555e8"), event_id=1007, version=0)
class Microsoft_Windows_Tethering_Manager_1007_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "CompletedTime" / Int32ul
    )

