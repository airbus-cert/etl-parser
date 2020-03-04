# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Power-CAD
GUID : daba4d32-cc40-4266-bb95-c30344dbc680
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("daba4d32-cc40-4266-bb95-c30344dbc680"), event_id=100, version=0)
class Microsoft_Windows_Power_CAD_100_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("daba4d32-cc40-4266-bb95-c30344dbc680"), event_id=101, version=0)
class Microsoft_Windows_Power_CAD_101_0(Etw):
    pattern = Struct(
        "Function" / CString,
        "Line" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("daba4d32-cc40-4266-bb95-c30344dbc680"), event_id=201, version=0)
class Microsoft_Windows_Power_CAD_201_0(Etw):
    pattern = Struct(
        "PowerSourceId" / Int32ul,
        "MaxChargeCurrent" / Int32ul,
        "PowerSourceInformation" / Int32ul,
        "PowerSourceStatus" / Int32ul,
        "ChargerId" / Guid
    )


@declare(guid=guid("daba4d32-cc40-4266-bb95-c30344dbc680"), event_id=202, version=0)
class Microsoft_Windows_Power_CAD_202_0(Etw):
    pattern = Struct(
        "PowerSourceId" / Int32ul,
        "MaxChargeCurrent" / Int32ul,
        "PowerSourceInformation" / Int32ul,
        "PowerSourceStatus" / Int32ul,
        "ChargerId" / Guid
    )


@declare(guid=guid("daba4d32-cc40-4266-bb95-c30344dbc680"), event_id=203, version=0)
class Microsoft_Windows_Power_CAD_203_0(Etw):
    pattern = Struct(
        "PowerSourceId" / Int32ul,
        "MaxChargeCurrent" / Int32ul,
        "PowerSourceInformation" / Int32ul,
        "PowerSourceStatus" / Int32ul,
        "ChargerId" / Guid
    )


@declare(guid=guid("daba4d32-cc40-4266-bb95-c30344dbc680"), event_id=204, version=0)
class Microsoft_Windows_Power_CAD_204_0(Etw):
    pattern = Struct(
        "PowerSourceId" / Int32ul
    )


@declare(guid=guid("daba4d32-cc40-4266-bb95-c30344dbc680"), event_id=205, version=0)
class Microsoft_Windows_Power_CAD_205_0(Etw):
    pattern = Struct(
        "PowerSourceId" / Int32ul,
        "SourceOnline" / Int32ul
    )


@declare(guid=guid("daba4d32-cc40-4266-bb95-c30344dbc680"), event_id=206, version=0)
class Microsoft_Windows_Power_CAD_206_0(Etw):
    pattern = Struct(
        "Capacity" / Int32ul,
        "FullChargedCapacity" / Int32ul,
        "Voltage" / Int32ul,
        "Rate" / Int32sl
    )


@declare(guid=guid("daba4d32-cc40-4266-bb95-c30344dbc680"), event_id=207, version=0)
class Microsoft_Windows_Power_CAD_207_0(Etw):
    pattern = Struct(
        "Size" / Int32ul,
        "BatteryTag" / Int32ul,
        "InformationLevel" / Int32ul,
        "ChargingSourceType" / Int32ul,
        "VaData" / Int32ul
    )


@declare(guid=guid("daba4d32-cc40-4266-bb95-c30344dbc680"), event_id=208, version=0)
class Microsoft_Windows_Power_CAD_208_0(Etw):
    pattern = Struct(
        "BatteryTag" / Int32ul,
        "InformationLevel" / Int32ul,
        "ChargingSourceType" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("daba4d32-cc40-4266-bb95-c30344dbc680"), event_id=209, version=0)
class Microsoft_Windows_Power_CAD_209_0(Etw):
    pattern = Struct(
        "PowerSourceId" / Int32ul,
        "Version" / Int16ul,
        "Flags" / Int32ul,
        "MaxCurrent" / Int32ul,
        "Voltage" / Int32ul,
        "PortType" / Int32ul,
        "PortId" / Int64ul,
        "PowerSourceInformation" / Int32ul,
        "OemCharger" / Guid
    )


@declare(guid=guid("daba4d32-cc40-4266-bb95-c30344dbc680"), event_id=210, version=0)
class Microsoft_Windows_Power_CAD_210_0(Etw):
    pattern = Struct(
        "Size" / Int32ul,
        "BatteryTag" / Int32ul,
        "InformationLevel" / Int32ul,
        "ChargingSourceType" / Int32ul,
        "Reserved" / Int32ul,
        "Flags" / Int32ul,
        "MaxCurrent" / Int32ul,
        "Voltage" / Int32ul,
        "PortType" / Int32ul,
        "PortId" / Int64ul,
        "PowerSourceInformation" / Int64ul,
        "OemCharger" / Guid
    )

