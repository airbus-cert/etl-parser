# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Iphlpsvc-Trace
GUID : 6600e712-c3b6-44a2-8a48-935c511f28c8
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4051, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4051_0(Etw):
    pattern = Struct(
        "IpAddrLength" / Int32ul,
        "ServiceType" / Int32ul,
        "TeredoPacketType" / Int32ul,
        "SourceIPAddress" / Bytes(lambda this: this.IpAddrLength),
        "DestinationIPAddress" / Bytes(lambda this: this.IpAddrLength)
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4052, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4052_0(Etw):
    pattern = Struct(
        "IpAddrLength" / Int32ul,
        "ReceivedTeredoPacketType" / Int32ul,
        "SourceIPAddress" / Bytes(lambda this: this.IpAddrLength),
        "SentTeredoPacketType" / Int32ul,
        "DestinationIPAddress" / Bytes(lambda this: this.IpAddrLength)
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4053, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4053_0(Etw):
    pattern = Struct(
        "IpAddrLength" / Int32ul,
        "ServiceType" / Int32ul,
        "ReceivedTeredoPacketType" / Int32ul,
        "MappedTeredoPacketType" / Int32ul,
        "SourceIPAddress" / Bytes(lambda this: this.IpAddrLength),
        "DestinationIPAddress" / Bytes(lambda this: this.IpAddrLength),
        "TargetIPAddress" / Bytes(lambda this: this.IpAddrLength)
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4054, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4054_0(Etw):
    pattern = Struct(
        "TeredoProtocolState" / Int32ul,
        "BadorInvalidPacket" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4055, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4055_0(Etw):
    pattern = Struct(
        "PreviousTeredoProtocolState" / Int32ul,
        "CurrentTeredoProtocolState" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4056, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4056_0(Etw):
    pattern = Struct(
        "TeredoPacketType" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4057, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4057_0(Etw):
    pattern = Struct(
        "IpAddrV4Length" / Int32ul,
        "IpAddrV6Length" / Int32ul,
        "SourceIpv6Address" / Bytes(lambda this: this.IpAddrV6Length),
        "DestinationIPv6Address" / Bytes(lambda this: this.IpAddrV6Length),
        "SourceIPv4Address" / Int32ul,
        "DestinationIPv4Address" / Int32ul,
        "SourcePort" / Int16ul,
        "DestinationPort" / Int16ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4058, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4058_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4059, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4059_0(Etw):
    pattern = Struct(
        "BadorInvalidPacket" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4060, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4060_0(Etw):
    pattern = Struct(
        "SockAddrLength" / Int32ul,
        "ServiceType" / Int32ul,
        "MappingType" / Int32ul,
        "SocketAddress" / Bytes(lambda this: this.SockAddrLength)
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4061, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4061_0(Etw):
    pattern = Struct(
        "AddrLength" / Int32ul,
        "PrimaryorSecondary" / WString,
        "DestinationAddress" / Bytes(lambda this: this.AddrLength)
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4062, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4062_0(Etw):
    pattern = Struct(
        "AddrLength" / Int32ul,
        "ServiceType" / Int32ul,
        "TeredoPacketType" / Int32ul,
        "SourceIpv6Address" / Bytes(lambda this: this.AddrLength)
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4063, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4063_0(Etw):
    pattern = Struct(
        "IpAddrLength" / Int32ul,
        "ServiceType" / Int32ul,
        "ReceivedTeredoPacketType" / Int32ul,
        "MappedTeredoPacketType" / Int32ul,
        "DestinationIPAddress" / Bytes(lambda this: this.IpAddrLength)
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4064, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4064_0(Etw):
    pattern = Struct(
        "AddrLength" / Int32ul,
        "ServiceType" / Int32ul,
        "ReceivedTeredoPacketType" / Int32ul,
        "MappedTeredoPacketType" / Int32ul,
        "DestinationIPAddress" / Bytes(lambda this: this.AddrLength)
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4065, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4065_0(Etw):
    pattern = Struct(
        "AddrLength" / Int32ul,
        "PrimaryorSecondary" / WString,
        "SocketAddress" / Bytes(lambda this: this.AddrLength)
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4066, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4066_0(Etw):
    pattern = Struct(
        "AddrLength" / Int32ul,
        "ServiceType" / Int32ul,
        "TeredoPacketType" / Int32ul,
        "SourceIpv6Address" / Bytes(lambda this: this.AddrLength),
        "DestinationIPAddress" / Bytes(lambda this: this.AddrLength),
        "TargetIPAddress" / Bytes(lambda this: this.AddrLength)
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4067, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4067_0(Etw):
    pattern = Struct(
        "AddrLength" / Int32ul,
        "ServiceType" / Int32ul,
        "TeredoPacketType" / Int32ul,
        "DestinationAddress" / Bytes(lambda this: this.AddrLength)
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4150, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4150_0(Etw):
    pattern = Struct(
        "ProtocolType" / Int32ul,
        "Interface" / WString,
        "InterfaceState" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4151, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4151_0(Etw):
    pattern = Struct(
        "AddrLength" / Int32ul,
        "Interface" / WString,
        "CurrentIPv4Address" / Int32ul,
        "NewIPv4Address" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4153, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4153_0(Etw):
    pattern = Struct(
        "AddrLength" / Int32ul,
        "ProtocolType" / Int32ul,
        "DestinationIPv4Address" / Int32ul,
        "Interface" / WString,
        "SourceIPv4Address" / Int32ul,
        "NextHopIPv4Address" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4154, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4154_0(Etw):
    pattern = Struct(
        "AddrLength" / Int32ul,
        "ProtocolType" / Int32ul,
        "InterfaceName" / WString,
        "RouterIPv4Address" / Int32ul,
        "Reachable" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4155, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4155_0(Etw):
    pattern = Struct(
        "AddrLength" / Int32ul,
        "InterfaceName" / WString,
        "RouterName" / WString,
        "Resolved" / Int32ul,
        "RouterIPv4Address" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4157, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4157_0(Etw):
    pattern = Struct(
        "ProtocolType" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4158, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4158_0(Etw):
    pattern = Struct(
        "ProtocolType" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4159, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4159_0(Etw):
    pattern = Struct(
        "ProtocolType" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4160, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4160_0(Etw):
    pattern = Struct(
        "ProtocolType" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4161, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4161_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4162, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4162_0(Etw):
    pattern = Struct(
        "AddrLength" / Int32ul,
        "ProtocolType" / Int32ul,
        "AddedorDeleted" / Int32ul,
        "IPv4Address" / Int32ul,
        "InterfaceName" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4163, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4163_0(Etw):
    pattern = Struct(
        "AddrLength" / Int32ul,
        "IPAddress" / Bytes(lambda this: this.AddrLength),
        "PrefixLen" / Int64ul,
        "InterfaceAlias" / WString,
        "Metric" / Int32ul,
        "PreferredLifetime" / Int32ul,
        "ValidLifeTime" / Int32ul,
        "Publish" / Int8ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4164, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4164_0(Etw):
    pattern = Struct(
        "InterfaceAlias" / WString,
        "IcsPrivateInterface" / Int8ul,
        "AdvertiseDefaultRoute" / Int8ul,
        "Advertises" / Int8ul,
        "Forwards" / Int8ul,
        "Status" / Int64ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4165, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4165_0(Etw):
    pattern = Struct(
        "NewRoutingState" / Int32ul,
        "OldRoutingState" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4166, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4166_0(Etw):
    pattern = Struct(
        "InterfaceAlias" / WString,
        "IPAddress" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4167, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4167_0(Etw):
    pattern = Struct(
        "ProtocolType" / Int32ul,
        "CompartmentId" / Int32ul,
        "HaveGlobalIpv6Address" / Int8ul,
        "ICSEnabled" / Int8ul,
        "GlobalIPv4AddressCount" / Int64ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4168, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4168_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int64ul,
        "CompartmentId" / Int32ul,
        "RoutingState" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4169, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4169_0(Etw):
    pattern = Struct(
        "AddrLength" / Int32ul,
        "InterfaceAlias" / WString,
        "IPAddress" / Bytes(lambda this: this.AddrLength),
        "Lifetime" / Int64ul,
        "PrefixConf" / Int64ul,
        "SuffixConf" / Int64ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4170, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4170_0(Etw):
    pattern = Struct(
        "ProtocolCallback" / Int32ul,
        "ProtocolType" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4171, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4171_0(Etw):
    pattern = Struct(
        "TeredoReasonCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4172, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4172_0(Etw):
    pattern = Struct(
        "TeredoReasonCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4173, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4173_0(Etw):
    pattern = Struct(
        "WindowsErrorCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4174, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4174_0(Etw):
    pattern = Struct(
        "IsatapRouter" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4175, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4175_0(Etw):
    pattern = Struct(
        "NetworkType" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4176, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4176_0(Etw):
    pattern = Struct(
        "SourceIPv4Address" / Int32ul,
        "SourcePort" / Int16ul,
        "UpperValue" / Int16ul,
        "LowerValue" / Int16ul,
        "PortPredicted" / Int16ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4177, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4177_0(Etw):
    pattern = Struct(
        "Action" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4178, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4178_0(Etw):
    pattern = Struct(
        "Action" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4179, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4179_0(Etw):
    pattern = Struct(
        "Action" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=4180, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_4180_0(Etw):
    pattern = Struct(
        "Action" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5000, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5000_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "InterfaceType" / Int32ul,
        "RegistryState" / Int32ul,
        "CurrentState" / Int32ul,
        "URL" / WString,
        "AuthenticationMode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5001, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5001_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5002, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5002_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5003, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5003_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "CertificateCN" / WString,
        "Preference" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5004, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5004_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5005, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5005_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5006, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5006_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5007, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5007_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5008, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5008_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5009, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5009_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5010, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5010_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5011, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5011_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5012, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5012_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5013, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5013_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5014, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5014_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5015, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5015_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "Address" / WString,
        "Added" / Int8ul,
        "LimitedConnectivity" / Int8ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5016, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5016_0(Etw):
    pattern = Struct(
        "GlobalIpv6AddressCount" / Int32ul,
        "Ipv4Connectivity" / Int8ul,
        "Ipv6Connectivity" / Int8ul,
        "CorpConnectivity" / Int8ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5017, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5017_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "Address" / WString,
        "Added" / Int8ul,
        "LimitedConnectivity" / Int8ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5018, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5018_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5019, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5019_0(Etw):
    pattern = Struct(
        "DueTime" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5020, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5020_0(Etw):
    pattern = Struct(
        "DueTime" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5021, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5021_0(Etw):
    pattern = Struct(
        "NetworkGuid" / Guid,
        "Added" / Int8ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5022, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5022_0(Etw):
    pattern = Struct(
        "CurrentTeredoProtocolState" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5023, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5023_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5024, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5024_0(Etw):
    pattern = Struct(
        "PacketType" / Int32ul,
        "TargetAddress" / WString,
        "Prefix" / WString,
        "DefaultRouter" / Int8ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5026, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5026_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5027, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5027_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5028, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5028_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5029, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5029_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5030, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5030_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5031, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5031_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5032, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5032_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5033, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5033_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5034, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5034_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5035, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5035_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5036, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5036_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "Address" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5037, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5037_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "Address" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5038, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5038_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "Address" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5039, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5039_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "Address" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5040, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5040_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5041, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5041_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5042, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5042_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5043, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5043_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5044, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5044_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5045, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5045_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "DestinationAddress" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5046, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5046_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "DestinationAddress" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5047, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5047_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5048, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5048_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5049, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5049_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5050, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5050_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5051, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5051_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5052, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5052_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5053, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5053_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5054, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5054_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5055, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5055_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5061, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5061_0(Etw):
    pattern = Struct(
        "WmiNotificationType" / Int32ul,
        "InterfaceName" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5063, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5063_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5064, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5064_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5065, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5065_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "ProxyAccessType" / Int32ul,
        "Proxy" / WString,
        "ProxyBypass" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5066, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5066_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5067, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5067_0(Etw):
    pattern = Struct(
        "ClientContext" / Int64ul,
        "TargetAddress" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5068, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5068_0(Etw):
    pattern = Struct(
        "Value" / Int64ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5069, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5069_0(Etw):
    pattern = Struct(
        "Action" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5100, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5100_0(Etw):
    pattern = Struct(
        "AddrLength" / Int32ul,
        "ClientIP" / Bytes(lambda this: this.AddrLength),
        "QuestionName" / WString,
        "QueryReceiveInterface" / WString,
        "QuerySendInterface" / WString,
        "DnsStatus" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5101, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5101_0(Etw):
    pattern = Struct(
        "AddrLength" / Int32ul,
        "ClientIP" / Bytes(lambda this: this.AddrLength),
        "QuestionName" / WString,
        "QueryReceiveInterface" / WString,
        "QuerySendInterface" / WString,
        "DnsStatus" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5102, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5102_0(Etw):
    pattern = Struct(
        "AddrLength" / Int32ul,
        "ClientIP" / Bytes(lambda this: this.AddrLength),
        "QuestionName" / WString,
        "TranslatedIPv4Address" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5104, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5104_0(Etw):
    pattern = Struct(
        "AddrLength" / Int32ul,
        "ClientIP" / Bytes(lambda this: this.AddrLength),
        "QuestionName" / WString,
        "IPv4Address" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.AddrLength)
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5105, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5105_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5106, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5106_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5107, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5107_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5108, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5108_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5109, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5109_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5110, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5110_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5111, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5111_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "Object2" / Int64ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5112, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5112_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5113, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5113_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5114, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5114_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5115, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5115_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5116, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5116_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5117, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5117_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5118, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5118_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5119, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5119_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5120, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5120_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5121, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5121_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5122, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5122_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5123, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5123_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5124, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5124_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5125, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5125_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5126, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5126_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5127, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5127_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5128, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5128_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5129, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5129_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5130, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5130_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5131, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5131_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5132, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5132_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5133, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5133_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5401, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5401_0(Etw):
    pattern = Struct(
        "Reason" / WString,
        "Event" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5402, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5402_0(Etw):
    pattern = Struct(
        "Reason" / WString,
        "Event" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5403, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5403_0(Etw):
    pattern = Struct(
        "Action" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5404, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5404_0(Etw):
    pattern = Struct(
        "Action" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5501, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5501_0(Etw):
    pattern = Struct(
        "SiteSelectionMethod" / Int32ul,
        "SiteName" / WString,
        "IphttpsProfileName" / WString,
        "TeredoServerIp" / Int32ul,
        "AddrLength" / Int32ul,
        "SiteIpv6Address" / Bytes(lambda this: this.AddrLength),
        "AdSiteName" / WString,
        "CorporateRanges" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5502, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5502_0(Etw):
    pattern = Struct(
        "AdSiteName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5503, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5503_0(Etw):
    pattern = Struct(
        "AddrLength" / Int32ul,
        "Prefix" / Bytes(lambda this: this.AddrLength),
        "PrefixLength" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5504, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5504_0(Etw):
    pattern = Struct(
        "IphttpsProfileName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5505, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5505_0(Etw):
    pattern = Struct(
        "TeredoServerIp" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5506, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5506_0(Etw):
    pattern = Struct(
        "SiteName" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5508, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5508_0(Etw):
    pattern = Struct(
        "SortingSiteName" / WString,
        "SortingMetric" / Int32ul,
        "AddressFamily" / Int32ul,
        "ProbingSiteName" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5509, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5509_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5510, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5510_0(Etw):
    pattern = Struct(
        "Action" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5511, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5511_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5512, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5512_0(Etw):
    pattern = Struct(
        "AddrLength" / Int32ul,
        "Prefix" / Bytes(lambda this: this.AddrLength)
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5513, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5513_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5514, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5514_0(Etw):
    pattern = Struct(
        "SiteUrl" / WString,
        "Timestamp" / Int64ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5515, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5515_0(Etw):
    pattern = Struct(
        "SiteUrl" / WString,
        "ErrorCode" / Int32ul,
        "Timestamp" / Int64ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5516, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5516_0(Etw):
    pattern = Struct(
        "Action" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5517, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5517_0(Etw):
    pattern = Struct(
        "SiteUrl" / WString,
        "ErrorCode" / Int32ul,
        "HttpStatus" / Int32ul,
        "Timestamp" / Int64ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5518, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5518_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Message" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5519, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5519_0(Etw):
    pattern = Struct(
        "Action" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5550, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5550_0(Etw):
    pattern = Struct(
        "Action" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5600, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5600_0(Etw):
    pattern = Struct(
        "Action" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5607, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5607_0(Etw):
    pattern = Struct(
        "SiteName" / WString,
        "Delay" / Int64ul
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5650, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5650_0(Etw):
    pattern = Struct(
        "Action" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5651, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5651_0(Etw):
    pattern = Struct(
        "Action" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5652, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5652_0(Etw):
    pattern = Struct(
        "Action" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5653, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5653_0(Etw):
    pattern = Struct(
        "Action" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5654, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5654_0(Etw):
    pattern = Struct(
        "Action" / WString
    )


@declare(guid=guid("6600e712-c3b6-44a2-8a48-935c511f28c8"), event_id=5655, version=0)
class Microsoft_Windows_Iphlpsvc_Trace_5655_0(Etw):
    pattern = Struct(
        "Action" / WString
    )

