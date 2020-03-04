# -*- coding: utf-8 -*-
"""
Microsoft-Windows-RPC
GUID : 6ad52b32-d609-4be9-ae07-ce8dae937e39
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6ad52b32-d609-4be9-ae07-ce8dae937e39"), event_id=1, version=1)
class Microsoft_Windows_RPC_1_1(Etw):
    pattern = Struct(
        "ImageName" / WString,
        "ComputerName" / WString,
        "ProcessID" / Int32ul,
        "TimeStamp" / SystemTime,
        "GeneratingComponent" / Int32ul,
        "Status" / Int32ul,
        "DetectionLocation" / Int16ul,
        "Flags" / Int16ul,
        "NumberOfParameters" / Int16ul,
        "Params" / Int64ul
    )


@declare(guid=guid("6ad52b32-d609-4be9-ae07-ce8dae937e39"), event_id=2, version=1)
class Microsoft_Windows_RPC_2_1(Etw):
    pattern = Struct(
        "ImangeName" / WString,
        "InterfaceUuid" / Guid,
        "FilterKey" / Guid
    )


@declare(guid=guid("6ad52b32-d609-4be9-ae07-ce8dae937e39"), event_id=3, version=1)
class Microsoft_Windows_RPC_3_1(Etw):
    pattern = Struct(
        "ImageName" / WString,
        "DetectionLocation" / Int16ul,
        "Status" / Int32ul,
        "AdditionalData1" / Int32ul,
        "AdditionalData2" / Int32ul
    )


@declare(guid=guid("6ad52b32-d609-4be9-ae07-ce8dae937e39"), event_id=4, version=1)
class Microsoft_Windows_RPC_4_1(Etw):
    pattern = Struct(
        "Subject" / Int8ul,
        "Verb" / Int8ul,
        "SubjectPointer" / Int64ul,
        "ObjectPointer" / Int64ul,
        "DataPointer" / Int64ul
    )


@declare(guid=guid("6ad52b32-d609-4be9-ae07-ce8dae937e39"), event_id=5, version=1)
class Microsoft_Windows_RPC_5_1(Etw):
    pattern = Struct(
        "InterfaceUuid" / Guid,
        "ProcNum" / Int32ul,
        "Protocol" / Int32ul,
        "NetworkAddress" / WString,
        "Endpoint" / WString,
        "Options" / WString,
        "AuthenticationLevel" / Int32ul,
        "AuthenticationService" / Int32ul,
        "ImpersonationLevel" / Int32ul
    )


@declare(guid=guid("6ad52b32-d609-4be9-ae07-ce8dae937e39"), event_id=6, version=1)
class Microsoft_Windows_RPC_6_1(Etw):
    pattern = Struct(
        "InterfaceUuid" / Guid,
        "ProcNum" / Int32ul,
        "Protocol" / Int32ul,
        "NetworkAddress" / WString,
        "Endpoint" / WString,
        "Options" / WString,
        "AuthenticationLevel" / Int32ul,
        "AuthenticationService" / Int32ul,
        "ImpersonationLevel" / Int32ul
    )


@declare(guid=guid("6ad52b32-d609-4be9-ae07-ce8dae937e39"), event_id=7, version=1)
class Microsoft_Windows_RPC_7_1(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("6ad52b32-d609-4be9-ae07-ce8dae937e39"), event_id=8, version=1)
class Microsoft_Windows_RPC_8_1(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("6ad52b32-d609-4be9-ae07-ce8dae937e39"), event_id=9, version=1)
class Microsoft_Windows_RPC_9_1(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("6ad52b32-d609-4be9-ae07-ce8dae937e39"), event_id=10, version=1)
class Microsoft_Windows_RPC_10_1(Etw):
    pattern = Struct(
        "SubjectPointer" / Int64ul,
        "FragmentSize" / Int32ul,
        "Fragment" / Bytes(lambda this: this.FragmentSize)
    )


@declare(guid=guid("6ad52b32-d609-4be9-ae07-ce8dae937e39"), event_id=11, version=1)
class Microsoft_Windows_RPC_11_1(Etw):
    pattern = Struct(
        "SubjectPointer" / Int64ul,
        "FragmentSize" / Int32ul,
        "Fragment" / Bytes(lambda this: this.FragmentSize)
    )


@declare(guid=guid("6ad52b32-d609-4be9-ae07-ce8dae937e39"), event_id=12, version=1)
class Microsoft_Windows_RPC_12_1(Etw):
    pattern = Struct(
        "ObjectType" / Int32ul,
        "Operation" / Int32ul,
        "Address" / Int64ul,
        "Data" / Int64ul
    )


@declare(guid=guid("6ad52b32-d609-4be9-ae07-ce8dae937e39"), event_id=13, version=1)
class Microsoft_Windows_RPC_13_1(Etw):
    pattern = Struct(
        "ObjectType" / Int32ul,
        "Operation" / Int32ul,
        "Address" / Int64ul,
        "Data" / Int64ul
    )


@declare(guid=guid("6ad52b32-d609-4be9-ae07-ce8dae937e39"), event_id=14, version=1)
class Microsoft_Windows_RPC_14_1(Etw):
    pattern = Struct(
        "InterfaceUuid" / Guid,
        "TypeMgrUuid" / Guid,
        "Flags" / Int32ul,
        "MaxCalls" / Int32ul,
        "SDSize" / Int32ul,
        "SD" / Bytes(lambda this: this.SDSize)
    )


@declare(guid=guid("6ad52b32-d609-4be9-ae07-ce8dae937e39"), event_id=15, version=1)
class Microsoft_Windows_RPC_15_1(Etw):
    pattern = Struct(
        "InterfaceUuid" / Guid,
        "TypeMgrUuid" / Guid,
        "Flags" / Int32ul,
        "MaxCalls" / Int32ul
    )


@declare(guid=guid("6ad52b32-d609-4be9-ae07-ce8dae937e39"), event_id=16, version=1)
class Microsoft_Windows_RPC_16_1(Etw):
    pattern = Struct(
        "Protocol" / WString,
        "Endpoint" / WString,
        "NetworkAddress" / WString,
        "PendingQueueSize" / Int32ul,
        "EndpointFlags" / Int32ul,
        "NicFlags" / Int32ul
    )

