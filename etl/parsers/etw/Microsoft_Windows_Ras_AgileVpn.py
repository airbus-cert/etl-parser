# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Ras-AgileVpn
GUID : b5325cd6-438e-4ec1-aa46-14f46f2570e4
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b5325cd6-438e-4ec1-aa46-14f46f2570e4"), event_id=2100, version=0)
class Microsoft_Windows_Ras_AgileVpn_2100_0(Etw):
    pattern = Struct(
        "DebugString" / CString
    )


@declare(guid=guid("b5325cd6-438e-4ec1-aa46-14f46f2570e4"), event_id=2101, version=0)
class Microsoft_Windows_Ras_AgileVpn_2101_0(Etw):
    pattern = Struct(
        "DebugString" / CString
    )


@declare(guid=guid("b5325cd6-438e-4ec1-aa46-14f46f2570e4"), event_id=2102, version=0)
class Microsoft_Windows_Ras_AgileVpn_2102_0(Etw):
    pattern = Struct(
        "DebugString" / CString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / CString,
        "PortNo" / CString
    )


@declare(guid=guid("b5325cd6-438e-4ec1-aa46-14f46f2570e4"), event_id=2103, version=0)
class Microsoft_Windows_Ras_AgileVpn_2103_0(Etw):
    pattern = Struct(
        "DebugString" / CString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / CString,
        "PortNo" / CString
    )


@declare(guid=guid("b5325cd6-438e-4ec1-aa46-14f46f2570e4"), event_id=3100, version=0)
class Microsoft_Windows_Ras_AgileVpn_3100_0(Etw):
    pattern = Struct(
        "DebugString" / CString
    )


@declare(guid=guid("b5325cd6-438e-4ec1-aa46-14f46f2570e4"), event_id=3101, version=0)
class Microsoft_Windows_Ras_AgileVpn_3101_0(Etw):
    pattern = Struct(
        "DebugString" / CString
    )


@declare(guid=guid("b5325cd6-438e-4ec1-aa46-14f46f2570e4"), event_id=3102, version=0)
class Microsoft_Windows_Ras_AgileVpn_3102_0(Etw):
    pattern = Struct(
        "DebugString" / CString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / CString,
        "PortNo" / CString
    )


@declare(guid=guid("b5325cd6-438e-4ec1-aa46-14f46f2570e4"), event_id=3103, version=0)
class Microsoft_Windows_Ras_AgileVpn_3103_0(Etw):
    pattern = Struct(
        "DebugString" / CString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / CString,
        "PortNo" / CString
    )


@declare(guid=guid("b5325cd6-438e-4ec1-aa46-14f46f2570e4"), event_id=3104, version=0)
class Microsoft_Windows_Ras_AgileVpn_3104_0(Etw):
    pattern = Struct(
        "DebugString" / CString,
        "DebugParam" / Int64ul
    )


@declare(guid=guid("b5325cd6-438e-4ec1-aa46-14f46f2570e4"), event_id=3105, version=0)
class Microsoft_Windows_Ras_AgileVpn_3105_0(Etw):
    pattern = Struct(
        "DebugString" / CString,
        "DebugParam" / Int64ul
    )


@declare(guid=guid("b5325cd6-438e-4ec1-aa46-14f46f2570e4"), event_id=3106, version=0)
class Microsoft_Windows_Ras_AgileVpn_3106_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "IpAddress" / WString
    )


@declare(guid=guid("b5325cd6-438e-4ec1-aa46-14f46f2570e4"), event_id=3201, version=0)
class Microsoft_Windows_Ras_AgileVpn_3201_0(Etw):
    pattern = Struct(
        "NumberOfPackets" / Int32ul,
        "SrcAddress" / CString,
        "DestAddress" / CString,
        "SrcPort" / Int32ul,
        "DestPort" / Int32ul,
        "NextProtocol" / Int32ul
    )


@declare(guid=guid("b5325cd6-438e-4ec1-aa46-14f46f2570e4"), event_id=3202, version=0)
class Microsoft_Windows_Ras_AgileVpn_3202_0(Etw):
    pattern = Struct(
        "DropReason" / CString,
        "NumberOfPackets" / Int32ul,
        "SrcAddress" / CString,
        "DestAddress" / CString,
        "SrcPort" / Int32ul,
        "DestPort" / Int32ul,
        "NextProtocol" / Int32ul
    )


@declare(guid=guid("b5325cd6-438e-4ec1-aa46-14f46f2570e4"), event_id=3203, version=0)
class Microsoft_Windows_Ras_AgileVpn_3203_0(Etw):
    pattern = Struct(
        "AddressFamily" / Int32ul,
        "StartPort" / Int32ul,
        "EndPort" / Int32ul,
        "ProtocolID" / Int32ul,
        "StartAddress" / CString,
        "EndAddress" / CString
    )


@declare(guid=guid("b5325cd6-438e-4ec1-aa46-14f46f2570e4"), event_id=3204, version=0)
class Microsoft_Windows_Ras_AgileVpn_3204_0(Etw):
    pattern = Struct(
        "TSID" / Int64ul,
        "fDelete" / Int32ul
    )


@declare(guid=guid("b5325cd6-438e-4ec1-aa46-14f46f2570e4"), event_id=3205, version=0)
class Microsoft_Windows_Ras_AgileVpn_3205_0(Etw):
    pattern = Struct(
        "TunnelID" / Int64ul,
        "Status" / Int32ul
    )

