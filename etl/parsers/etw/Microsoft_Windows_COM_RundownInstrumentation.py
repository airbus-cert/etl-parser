# -*- coding: utf-8 -*-
"""
Microsoft-Windows-COM-RundownInstrumentation
GUID : 2957313d-fcaa-5d4a-2f69-32ce5f0ac44e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=1, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_1_0(Etw):
    pattern = Struct(
        "OID" / Int64ul,
        "IID" / Guid,
        "IPID" / Guid,
        "IsFastRundown" / Int8ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=2, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_2_0(Etw):
    pattern = Struct(
        "OID" / Int64ul,
        "IID" / Guid,
        "IPID" / Guid,
        "ProxyManagerIUnknown" / Int64ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=3, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_3_0(Etw):
    pattern = Struct(
        "OID" / Int64ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=4, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_4_0(Etw):
    pattern = Struct(
        "OID" / Int64ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=5, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_5_0(Etw):
    pattern = Struct(
        "OID" / Int64ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=6, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_6_0(Etw):
    pattern = Struct(
        "OID" / Int64ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=7, version=1)
class Microsoft_Windows_COM_RundownInstrumentation_7_1(Etw):
    pattern = Struct(
        "OID" / Int64ul,
        "TargetInterface" / Guid,
        "TargetMethod" / Int32ul,
        "IPID" / Guid,
        "ProxyManagerIUnknown" / Int64ul,
        "ImplementedInterface1" / Guid,
        "ImplementedInterface2" / Guid,
        "ImplementedInterface3" / Guid
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=8, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_8_0(Etw):
    pattern = Struct(
        "OID" / Int64ul,
        "TargetInterface" / Guid,
        "TargetMethod" / Int32ul,
        "IPID" / Guid,
        "ProxyManagerIUnknown" / Int64ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=9, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_9_0(Etw):
    pattern = Struct(
        "OID" / Int64ul,
        "Flags" / Int32ul,
        "HRESULT" / Int32sl
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=10, version=1)
class Microsoft_Windows_COM_RundownInstrumentation_10_1(Etw):
    pattern = Struct(
        "OID" / Int64ul,
        "ClientProcessId" / Int32ul,
        "WhereDetected" / Int32ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=11, version=1)
class Microsoft_Windows_COM_RundownInstrumentation_11_1(Etw):
    pattern = Struct(
        "OID" / Int64ul,
        "ClientProcessId" / Int32ul,
        "TokenModifiedLuid" / Int64ul,
        "SetIdIfKnown" / Int64ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=12, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_12_0(Etw):
    pattern = Struct(
        "OID" / Int64ul,
        "ClientProcessId" / Int32ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=13, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_13_0(Etw):
    pattern = Struct(
        "OID" / Int64ul,
        "ClientProcessId" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=14, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_14_0(Etw):
    pattern = Struct(
        "OID" / Int64ul,
        "ClientProcessId" / Int32ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=15, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_15_0(Etw):
    pattern = Struct(
        "OID" / Int64ul,
        "ClientProcessId" / Int32ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=16, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_16_0(Etw):
    pattern = Struct(
        "OID" / Int64ul,
        "TokenModifiedLuid" / Int64ul,
        "SetId" / Int64ul,
        "CurrentSequenceNumber" / Int16ul,
        "LastSequenceNumber" / Int16ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=17, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_17_0(Etw):
    pattern = Struct(
        "OID" / Int64ul,
        "TokenModifiedLuid" / Int64ul,
        "SetId" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=18, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_18_0(Etw):
    pattern = Struct(
        "OID" / Int64ul,
        "TokenModifiedLuid" / Int64ul,
        "SetId" / Int64ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=19, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_19_0(Etw):
    pattern = Struct(
        "OID" / Int64ul,
        "TokenModifiedLuid" / Int64ul,
        "SetIdIfKnown" / Int64ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=20, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_20_0(Etw):
    pattern = Struct(
        "OID" / Int64ul,
        "TokenModifiedLuid" / Int64ul,
        "SetId" / Int64ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=21, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_21_0(Etw):
    pattern = Struct(
        "OID" / Int64ul,
        "WhereIssued" / Int32ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=22, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_22_0(Etw):
    pattern = Struct(
        "OID" / Int64ul,
        "DisconnectionType" / Int32ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=23, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_23_0(Etw):
    pattern = Struct(
        "OID" / Int64ul,
        "DisconnectionType" / Int32ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=24, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_24_0(Etw):
    pattern = Struct(
        "OID" / Int64ul,
        "ClientProcessId" / Int32ul
    )


@declare(guid=guid("2957313d-fcaa-5d4a-2f69-32ce5f0ac44e"), event_id=25, version=0)
class Microsoft_Windows_COM_RundownInstrumentation_25_0(Etw):
    pattern = Struct(
        "OID" / Int64ul,
        "ClientProcessId" / Int32ul,
        "TokenModifiedLuid" / Int64ul,
        "SetIdIfKnown" / Int64ul,
        "Reason" / Int32ul
    )

