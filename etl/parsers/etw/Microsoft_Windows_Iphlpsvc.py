# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Iphlpsvc
GUID : 66a5c15c-4f8e-4044-bf6e-71d896038977
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("66a5c15c-4f8e-4044-bf6e-71d896038977"), event_id=4001, version=0)
class Microsoft_Windows_Iphlpsvc_4001_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "TeredoReasonCode" / Int32ul
    )


@declare(guid=guid("66a5c15c-4f8e-4044-bf6e-71d896038977"), event_id=4002, version=0)
class Microsoft_Windows_Iphlpsvc_4002_0(Etw):
    pattern = Struct(
        "Interface" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("66a5c15c-4f8e-4044-bf6e-71d896038977"), event_id=4003, version=0)
class Microsoft_Windows_Iphlpsvc_4003_0(Etw):
    pattern = Struct(
        "ServerName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("66a5c15c-4f8e-4044-bf6e-71d896038977"), event_id=4004, version=0)
class Microsoft_Windows_Iphlpsvc_4004_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("66a5c15c-4f8e-4044-bf6e-71d896038977"), event_id=4100, version=0)
class Microsoft_Windows_Iphlpsvc_4100_0(Etw):
    pattern = Struct(
        "IsatapRouter" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("66a5c15c-4f8e-4044-bf6e-71d896038977"), event_id=4200, version=0)
class Microsoft_Windows_Iphlpsvc_4200_0(Etw):
    pattern = Struct(
        "ProtocolType" / Int32ul,
        "Interface" / WString,
        "Address" / WString
    )


@declare(guid=guid("66a5c15c-4f8e-4044-bf6e-71d896038977"), event_id=4201, version=0)
class Microsoft_Windows_Iphlpsvc_4201_0(Etw):
    pattern = Struct(
        "ProtocolType" / Int32ul,
        "Interface" / WString
    )


@declare(guid=guid("66a5c15c-4f8e-4044-bf6e-71d896038977"), event_id=4202, version=0)
class Microsoft_Windows_Iphlpsvc_4202_0(Etw):
    pattern = Struct(
        "ProtocolType" / Int32ul,
        "Interface" / WString,
        "UpdateType" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("66a5c15c-4f8e-4044-bf6e-71d896038977"), event_id=4300, version=0)
class Microsoft_Windows_Iphlpsvc_4300_0(Etw):
    pattern = Struct(
        "ServerUrl" / WString
    )


@declare(guid=guid("66a5c15c-4f8e-4044-bf6e-71d896038977"), event_id=4302, version=0)
class Microsoft_Windows_Iphlpsvc_4302_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "IpHTTPSReasonCode" / Int32ul
    )


@declare(guid=guid("66a5c15c-4f8e-4044-bf6e-71d896038977"), event_id=4303, version=0)
class Microsoft_Windows_Iphlpsvc_4303_0(Etw):
    pattern = Struct(
        "ClientMachineName" / WString,
        "TunnelSourceIP" / WString,
        "RemoteIP" / WString
    )


@declare(guid=guid("66a5c15c-4f8e-4044-bf6e-71d896038977"), event_id=4304, version=0)
class Microsoft_Windows_Iphlpsvc_4304_0(Etw):
    pattern = Struct(
        "ClientMachineName" / WString,
        "TunnelSourceIP" / WString,
        "RemoteIP" / WString
    )


@declare(guid=guid("66a5c15c-4f8e-4044-bf6e-71d896038977"), event_id=4400, version=0)
class Microsoft_Windows_Iphlpsvc_4400_0(Etw):
    pattern = Struct(
        "AddrLength" / Int32ul,
        "ClientIP" / Bytes(lambda this: this.AddrLength),
        "QuestionName" / WString,
        "TranslatedIPv4Address" / Int32ul
    )


@declare(guid=guid("66a5c15c-4f8e-4044-bf6e-71d896038977"), event_id=4500, version=0)
class Microsoft_Windows_Iphlpsvc_4500_0(Etw):
    pattern = Struct(
        "SiteName" / WString
    )


@declare(guid=guid("66a5c15c-4f8e-4044-bf6e-71d896038977"), event_id=4501, version=0)
class Microsoft_Windows_Iphlpsvc_4501_0(Etw):
    pattern = Struct(
        "SiteName" / WString
    )

