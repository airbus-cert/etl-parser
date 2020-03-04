# -*- coding: utf-8 -*-
"""
Microsoft-Windows-CoreSystem-InitMachineConfig
GUID : 0b886108-1899-4d3a-9c0d-42d8fc4b9108
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("0b886108-1899-4d3a-9c0d-42d8fc4b9108"), event_id=1, version=0)
class Microsoft_Windows_CoreSystem_InitMachineConfig_1_0(Etw):
    pattern = Struct(
        "evtErrorId" / Int64ul,
        "evtHiveNameLength" / Int16ul,
        "evtHiveName" / Bytes(lambda this: this.evtHiveNameLength),
        "evtStatus" / Int32ul,
        "evtAdditionalInfo" / Int64ul
    )


@declare(guid=guid("0b886108-1899-4d3a-9c0d-42d8fc4b9108"), event_id=2, version=0)
class Microsoft_Windows_CoreSystem_InitMachineConfig_2_0(Etw):
    pattern = Struct(
        "evtHiveNameLength" / Int16ul,
        "evtHiveName" / Bytes(lambda this: this.evtHiveNameLength)
    )


@declare(guid=guid("0b886108-1899-4d3a-9c0d-42d8fc4b9108"), event_id=3, version=0)
class Microsoft_Windows_CoreSystem_InitMachineConfig_3_0(Etw):
    pattern = Struct(
        "evtStatus" / Int32ul
    )


@declare(guid=guid("0b886108-1899-4d3a-9c0d-42d8fc4b9108"), event_id=4, version=0)
class Microsoft_Windows_CoreSystem_InitMachineConfig_4_0(Etw):
    pattern = Struct(
        "evtStatus" / Int32ul
    )

