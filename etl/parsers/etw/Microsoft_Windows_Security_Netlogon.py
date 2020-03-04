# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Security-Netlogon
GUID : e5ba83f6-07d0-46b1-8bc7-7e669a1d31dc
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e5ba83f6-07d0-46b1-8bc7-7e669a1d31dc"), event_id=4004, version=0)
class Microsoft_Windows_Security_Netlogon_4004_0(Etw):
    pattern = Struct(
        "SChannelName" / WString,
        "UserName" / WString,
        "DomainName" / WString,
        "WorkstationName" / WString,
        "SChannelType" / Int32ul
    )


@declare(guid=guid("e5ba83f6-07d0-46b1-8bc7-7e669a1d31dc"), event_id=4005, version=0)
class Microsoft_Windows_Security_Netlogon_4005_0(Etw):
    pattern = Struct(
        "SChannelName" / WString,
        "UserName" / WString,
        "DomainName" / WString,
        "WorkstationName" / WString,
        "SChannelType" / Int32ul
    )


@declare(guid=guid("e5ba83f6-07d0-46b1-8bc7-7e669a1d31dc"), event_id=4006, version=0)
class Microsoft_Windows_Security_Netlogon_4006_0(Etw):
    pattern = Struct(
        "SChannelName" / WString,
        "UserName" / WString,
        "DomainName" / WString,
        "WorkstationName" / WString,
        "SChannelType" / Int32ul
    )


@declare(guid=guid("e5ba83f6-07d0-46b1-8bc7-7e669a1d31dc"), event_id=8004, version=0)
class Microsoft_Windows_Security_Netlogon_8004_0(Etw):
    pattern = Struct(
        "SChannelName" / WString,
        "UserName" / WString,
        "DomainName" / WString,
        "WorkstationName" / WString,
        "SChannelType" / Int32ul
    )


@declare(guid=guid("e5ba83f6-07d0-46b1-8bc7-7e669a1d31dc"), event_id=8005, version=0)
class Microsoft_Windows_Security_Netlogon_8005_0(Etw):
    pattern = Struct(
        "SChannelName" / WString,
        "UserName" / WString,
        "DomainName" / WString,
        "WorkstationName" / WString,
        "SChannelType" / Int32ul
    )


@declare(guid=guid("e5ba83f6-07d0-46b1-8bc7-7e669a1d31dc"), event_id=8006, version=0)
class Microsoft_Windows_Security_Netlogon_8006_0(Etw):
    pattern = Struct(
        "SChannelName" / WString,
        "UserName" / WString,
        "DomainName" / WString,
        "WorkstationName" / WString,
        "SChannelType" / Int32ul
    )


@declare(guid=guid("e5ba83f6-07d0-46b1-8bc7-7e669a1d31dc"), event_id=9000, version=0)
class Microsoft_Windows_Security_Netlogon_9000_0(Etw):
    pattern = Struct(
        "AccountName" / WString,
        "AccountDomain" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("e5ba83f6-07d0-46b1-8bc7-7e669a1d31dc"), event_id=9001, version=0)
class Microsoft_Windows_Security_Netlogon_9001_0(Etw):
    pattern = Struct(
        "Account" / WString
    )


@declare(guid=guid("e5ba83f6-07d0-46b1-8bc7-7e669a1d31dc"), event_id=9002, version=0)
class Microsoft_Windows_Security_Netlogon_9002_0(Etw):
    pattern = Struct(
        "Account" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("e5ba83f6-07d0-46b1-8bc7-7e669a1d31dc"), event_id=9003, version=0)
class Microsoft_Windows_Security_Netlogon_9003_0(Etw):
    pattern = Struct(
        "Account" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("e5ba83f6-07d0-46b1-8bc7-7e669a1d31dc"), event_id=9004, version=0)
class Microsoft_Windows_Security_Netlogon_9004_0(Etw):
    pattern = Struct(
        "RequestsRejected" / Int32ul
    )

