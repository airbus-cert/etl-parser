# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Network-Setup
GUID : a111f1c2-5923-47c0-9a68-d0bafb577901
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a111f1c2-5923-47c0-9a68-d0bafb577901"), event_id=102, version=0)
class Microsoft_Windows_Network_Setup_102_0(Etw):
    pattern = Struct(
        "Code" / Int32sl
    )


@declare(guid=guid("a111f1c2-5923-47c0-9a68-d0bafb577901"), event_id=200, version=0)
class Microsoft_Windows_Network_Setup_200_0(Etw):
    pattern = Struct(
        "TransactionGuid" / Guid,
        "EnvironmentType" / Int32ul
    )


@declare(guid=guid("a111f1c2-5923-47c0-9a68-d0bafb577901"), event_id=201, version=0)
class Microsoft_Windows_Network_Setup_201_0(Etw):
    pattern = Struct(
        "TransactionGuid" / Guid
    )


@declare(guid=guid("a111f1c2-5923-47c0-9a68-d0bafb577901"), event_id=202, version=0)
class Microsoft_Windows_Network_Setup_202_0(Etw):
    pattern = Struct(
        "TransactionGuid" / Guid
    )


@declare(guid=guid("a111f1c2-5923-47c0-9a68-d0bafb577901"), event_id=203, version=0)
class Microsoft_Windows_Network_Setup_203_0(Etw):
    pattern = Struct(
        "TransactionGuid" / Guid
    )


@declare(guid=guid("a111f1c2-5923-47c0-9a68-d0bafb577901"), event_id=204, version=0)
class Microsoft_Windows_Network_Setup_204_0(Etw):
    pattern = Struct(
        "TransactionGuid" / Guid
    )


@declare(guid=guid("a111f1c2-5923-47c0-9a68-d0bafb577901"), event_id=205, version=0)
class Microsoft_Windows_Network_Setup_205_0(Etw):
    pattern = Struct(
        "TransactionGuid" / Guid
    )


@declare(guid=guid("a111f1c2-5923-47c0-9a68-d0bafb577901"), event_id=300, version=0)
class Microsoft_Windows_Network_Setup_300_0(Etw):
    pattern = Struct(
        "TransactionGuid" / Guid,
        "Api" / Int32ul
    )


@declare(guid=guid("a111f1c2-5923-47c0-9a68-d0bafb577901"), event_id=301, version=0)
class Microsoft_Windows_Network_Setup_301_0(Etw):
    pattern = Struct(
        "TransactionGuid" / Guid,
        "Api" / Int32ul,
        "Code" / Int32sl
    )


@declare(guid=guid("a111f1c2-5923-47c0-9a68-d0bafb577901"), event_id=400, version=0)
class Microsoft_Windows_Network_Setup_400_0(Etw):
    pattern = Struct(
        "TransactionGuid" / Guid,
        "PluginId" / Int32ul,
        "PluginName" / WString,
        "Api" / Int32ul
    )


@declare(guid=guid("a111f1c2-5923-47c0-9a68-d0bafb577901"), event_id=401, version=0)
class Microsoft_Windows_Network_Setup_401_0(Etw):
    pattern = Struct(
        "TransactionGuid" / Guid,
        "Output" / Int32ul,
        "Code" / Int32sl
    )


@declare(guid=guid("a111f1c2-5923-47c0-9a68-d0bafb577901"), event_id=500, version=0)
class Microsoft_Windows_Network_Setup_500_0(Etw):
    pattern = Struct(
        "TransactionGuid" / Guid,
        "OperationType" / Int32ul,
        "ObjectType" / Int32ul,
        "ObjectId" / Guid,
        "PropertyBufferSize" / Int16ul,
        "PropertyBuffer" / Bytes(lambda this: this.PropertyBufferSize)
    )


@declare(guid=guid("a111f1c2-5923-47c0-9a68-d0bafb577901"), event_id=501, version=0)
class Microsoft_Windows_Network_Setup_501_0(Etw):
    pattern = Struct(
        "TransactionGuid" / Guid,
        "Code" / Int32sl
    )


@declare(guid=guid("a111f1c2-5923-47c0-9a68-d0bafb577901"), event_id=600, version=0)
class Microsoft_Windows_Network_Setup_600_0(Etw):
    pattern = Struct(
        "Api" / Int32ul
    )


@declare(guid=guid("a111f1c2-5923-47c0-9a68-d0bafb577901"), event_id=601, version=0)
class Microsoft_Windows_Network_Setup_601_0(Etw):
    pattern = Struct(
        "Code" / Int32sl
    )


@declare(guid=guid("a111f1c2-5923-47c0-9a68-d0bafb577901"), event_id=700, version=0)
class Microsoft_Windows_Network_Setup_700_0(Etw):
    pattern = Struct(
        "TransactionGuid" / Guid,
        "ComponentId" / WString,
        "Api" / Int32ul,
        "Parameter1" / Int32ul,
        "Parameter2" / WString
    )


@declare(guid=guid("a111f1c2-5923-47c0-9a68-d0bafb577901"), event_id=701, version=0)
class Microsoft_Windows_Network_Setup_701_0(Etw):
    pattern = Struct(
        "Code" / Int32sl
    )


@declare(guid=guid("a111f1c2-5923-47c0-9a68-d0bafb577901"), event_id=702, version=0)
class Microsoft_Windows_Network_Setup_702_0(Etw):
    pattern = Struct(
        "Code" / Int32sl
    )

