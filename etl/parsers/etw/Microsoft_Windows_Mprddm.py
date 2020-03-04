# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Mprddm
GUID : 3a5bef13-d0f7-4e7f-9ec8-5e707df711d0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3a5bef13-d0f7-4e7f-9ec8-5e707df711d0"), event_id=0, version=0)
class Microsoft_Windows_Mprddm_0_0(Etw):
    pattern = Struct(
        "debugString" / WString
    )


@declare(guid=guid("3a5bef13-d0f7-4e7f-9ec8-5e707df711d0"), event_id=1, version=0)
class Microsoft_Windows_Mprddm_1_0(Etw):
    pattern = Struct(
        "connectionID" / Int64ul,
        "userName" / WString,
        "remoteIPv4Address" / WString,
        "remoteIPv6Address" / WString,
        "ispAddress" / WString,
        "deviceType" / Int32ul,
        "tunnelType" / WString,
        "portName" / WString,
        "authenticationProtocol" / Int32ul,
        "authenticationData" / Int32ul,
        "eapTypeId" / Int32ul,
        "embeddedEapTypeId" / Int32ul,
        "quarantineState" / Int32ul,
        "connectionStartTime" / Int64ul,
        "isS2SConnection" / Int32ul,
        "routingDomainId" / Guid
    )


@declare(guid=guid("3a5bef13-d0f7-4e7f-9ec8-5e707df711d0"), event_id=2, version=0)
class Microsoft_Windows_Mprddm_2_0(Etw):
    pattern = Struct(
        "connectionID" / Int64ul,
        "userName" / WString,
        "remoteIPv4Address" / WString,
        "remoteIPv6Address" / WString,
        "ispAddress" / WString,
        "portName" / WString,
        "bytesIn" / Int64ul,
        "bytesOut" / Int64ul,
        "disconnectTime" / Int64ul,
        "isS2SConnection" / Int32ul
    )

