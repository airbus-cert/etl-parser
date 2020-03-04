# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Networking-RealTimeCommunication
GUID : 1e39b4ce-d1e6-46ce-b65b-5ab05d6cc266
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("1e39b4ce-d1e6-46ce-b65b-5ab05d6cc266"), event_id=1000, version=0)
class Microsoft_Windows_Networking_RealTimeCommunication_1000_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ChannelId" / WString,
        "StatusDescription" / WString,
        "hresult" / Int32sl
    )


@declare(guid=guid("1e39b4ce-d1e6-46ce-b65b-5ab05d6cc266"), event_id=1001, version=0)
class Microsoft_Windows_Networking_RealTimeCommunication_1001_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ChannelId" / WString,
        "StatusDescription" / WString,
        "ChannelStatus" / Int32ul
    )


@declare(guid=guid("1e39b4ce-d1e6-46ce-b65b-5ab05d6cc266"), event_id=1002, version=0)
class Microsoft_Windows_Networking_RealTimeCommunication_1002_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "Object" / Int64ul,
        "ChannelId" / WString,
        "RequestedResourceType" / Int32ul,
        "ServerKeepaliveIntervalInMinutes" / Int32ul,
        "KeepaliveTriggerId" / Guid,
        "PushNotificationTriggerId" / Guid
    )


@declare(guid=guid("1e39b4ce-d1e6-46ce-b65b-5ab05d6cc266"), event_id=1003, version=0)
class Microsoft_Windows_Networking_RealTimeCommunication_1003_0(Etw):
    pattern = Struct(
        "ResetReason" / Int32ul,
        "HardwareSlotReset" / Int32ul,
        "SoftwareSlotReset" / Int32ul
    )

