# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Tethering-Station
GUID : 585cab4f-9351-436e-9d99-dc4b41a20de0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("585cab4f-9351-436e-9d99-dc4b41a20de0"), event_id=1001, version=0)
class Microsoft_Windows_Tethering_Station_1001_0(Etw):
    pattern = Struct(
        "WlanInterfaceGuid" / Guid
    )


@declare(guid=guid("585cab4f-9351-436e-9d99-dc4b41a20de0"), event_id=1002, version=0)
class Microsoft_Windows_Tethering_Station_1002_0(Etw):
    pattern = Struct(
        "WlanInterfaceGuid" / Guid,
        "Scenario" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("585cab4f-9351-436e-9d99-dc4b41a20de0"), event_id=1003, version=0)
class Microsoft_Windows_Tethering_Station_1003_0(Etw):
    pattern = Struct(
        "WlanInterfaceGuid" / Guid
    )

