# -*- coding: utf-8 -*-
"""
Microsoft-Windows-RPC-Events
GUID : f4aed7c7-a898-4627-b053-44a7caa12fcd
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f4aed7c7-a898-4627-b053-44a7caa12fcd"), event_id=2, version=0)
class Microsoft_Windows_RPC_Events_2_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "ProcessId" / Int32ul,
        "RPCProtocolSequence" / WString,
        "InterfaceGUID" / Guid
    )


@declare(guid=guid("f4aed7c7-a898-4627-b053-44a7caa12fcd"), event_id=3, version=0)
class Microsoft_Windows_RPC_Events_3_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "ProcessId" / Int32ul,
        "RPCProtocolSequence" / WString,
        "InterfaceGUID" / Guid
    )


@declare(guid=guid("f4aed7c7-a898-4627-b053-44a7caa12fcd"), event_id=4, version=0)
class Microsoft_Windows_RPC_Events_4_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("f4aed7c7-a898-4627-b053-44a7caa12fcd"), event_id=5, version=0)
class Microsoft_Windows_RPC_Events_5_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "ProcessId" / Int32ul,
        "RPCProtocolSequence" / WString,
        "InterfaceGUID" / Guid
    )


@declare(guid=guid("f4aed7c7-a898-4627-b053-44a7caa12fcd"), event_id=6, version=0)
class Microsoft_Windows_RPC_Events_6_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "ProcessId" / Int32ul,
        "RPCProtocolSequence" / WString
    )


@declare(guid=guid("f4aed7c7-a898-4627-b053-44a7caa12fcd"), event_id=7, version=0)
class Microsoft_Windows_RPC_Events_7_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "ProcessId" / Int32ul,
        "RPCProtocolSequence" / WString,
        "InterfaceGUID" / Guid
    )


@declare(guid=guid("f4aed7c7-a898-4627-b053-44a7caa12fcd"), event_id=8, version=0)
class Microsoft_Windows_RPC_Events_8_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "ProcessId" / Int32ul,
        "RPCProtocolSequence" / WString,
        "RPCEndpoint" / WString,
        "InterfaceGUID" / Guid,
        "RPCStatus" / Int32ul
    )


@declare(guid=guid("f4aed7c7-a898-4627-b053-44a7caa12fcd"), event_id=9, version=0)
class Microsoft_Windows_RPC_Events_9_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "ProcessId" / WString
    )


@declare(guid=guid("f4aed7c7-a898-4627-b053-44a7caa12fcd"), event_id=10, version=0)
class Microsoft_Windows_RPC_Events_10_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "ProcessId" / WString,
        "ExpectedInterfaceID" / WString,
        "ReceivedInterfaceID" / WString
    )


@declare(guid=guid("f4aed7c7-a898-4627-b053-44a7caa12fcd"), event_id=11, version=0)
class Microsoft_Windows_RPC_Events_11_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "ProcessId" / WString,
        "InterfaceId" / Guid,
        "Method" / Int32sl
    )

