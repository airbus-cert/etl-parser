# -*- coding: utf-8 -*-
"""
Microsoft-Windows-stobject
GUID : 86133982-63d7-4741-928e-ef1349b80219
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("86133982-63d7-4741-928e-ef1349b80219"), event_id=142, version=0)
class Microsoft_Windows_stobject_142_0(Etw):
    pattern = Struct(
        "BatteryDrainRate" / Int32sl,
        "CurrentBatteryPercent" / Int32ul,
        "TimeSinceLastLogged" / Int32ul,
        "FullChargeCapacity" / Int32ul,
        "ChargeCapacityRatio" / Int32ul,
        "BatteryDrainInfoFlags" / Int32ul
    )


@declare(guid=guid("86133982-63d7-4741-928e-ef1349b80219"), event_id=302, version=0)
class Microsoft_Windows_stobject_302_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("86133982-63d7-4741-928e-ef1349b80219"), event_id=303, version=0)
class Microsoft_Windows_stobject_303_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("86133982-63d7-4741-928e-ef1349b80219"), event_id=304, version=0)
class Microsoft_Windows_stobject_304_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )

