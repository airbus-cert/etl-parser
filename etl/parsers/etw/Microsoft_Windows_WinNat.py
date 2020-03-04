# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WinNat
GUID : 66c07ecd-6667-43fc-93f8-05cf07f446ec
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1001, version=0)
class Microsoft_Windows_WinNat_1001_0(Etw):
    pattern = Struct(
        "InternalAddrLen" / Int32ul,
        "InternalSrcAddr" / Bytes(lambda this: this.InternalAddrLen),
        "InternalDstAddr" / Bytes(lambda this: this.InternalAddrLen),
        "ExternalAddrLen" / Int32ul,
        "ExternalSrcAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "ExternalDstAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "TransportProtocol" / Int32ul,
        "Lifetime" / Int32ul,
        "TcpSessionState" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1001, version=1)
class Microsoft_Windows_WinNat_1001_1(Etw):
    pattern = Struct(
        "InternalAddrLen" / Int32ul,
        "InternalSrcAddr" / Bytes(lambda this: this.InternalAddrLen),
        "InternalDstAddr" / Bytes(lambda this: this.InternalAddrLen),
        "ExternalAddrLen" / Int32ul,
        "ExternalSrcAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "ExternalDstAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "TransportProtocol" / Int32ul,
        "Lifetime" / Int32ul,
        "TcpSessionState" / Int32ul,
        "InternalCompartmentId" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1002, version=0)
class Microsoft_Windows_WinNat_1002_0(Etw):
    pattern = Struct(
        "InternalAddrLen" / Int32ul,
        "InternalSrcAddr" / Bytes(lambda this: this.InternalAddrLen),
        "InternalDstAddr" / Bytes(lambda this: this.InternalAddrLen),
        "ExternalAddrLen" / Int32ul,
        "ExternalSrcAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "ExternalDstAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "TransportProtocol" / Int32ul,
        "Lifetime" / Int32ul,
        "TcpSessionState" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1002, version=1)
class Microsoft_Windows_WinNat_1002_1(Etw):
    pattern = Struct(
        "InternalAddrLen" / Int32ul,
        "InternalSrcAddr" / Bytes(lambda this: this.InternalAddrLen),
        "InternalDstAddr" / Bytes(lambda this: this.InternalAddrLen),
        "ExternalAddrLen" / Int32ul,
        "ExternalSrcAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "ExternalDstAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "TransportProtocol" / Int32ul,
        "Lifetime" / Int32ul,
        "TcpSessionState" / Int32ul,
        "InternalCompartmentId" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1003, version=0)
class Microsoft_Windows_WinNat_1003_0(Etw):
    pattern = Struct(
        "InternalAddrLen" / Int32ul,
        "InternalSrcAddr" / Bytes(lambda this: this.InternalAddrLen),
        "InternalDstAddr" / Bytes(lambda this: this.InternalAddrLen),
        "ExternalAddrLen" / Int32ul,
        "ExternalSrcAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "ExternalDstAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "TransportProtocol" / Int32ul,
        "Lifetime" / Int32ul,
        "TcpSessionState" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1003, version=1)
class Microsoft_Windows_WinNat_1003_1(Etw):
    pattern = Struct(
        "InternalAddrLen" / Int32ul,
        "InternalSrcAddr" / Bytes(lambda this: this.InternalAddrLen),
        "InternalDstAddr" / Bytes(lambda this: this.InternalAddrLen),
        "ExternalAddrLen" / Int32ul,
        "ExternalSrcAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "ExternalDstAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "TransportProtocol" / Int32ul,
        "Lifetime" / Int32ul,
        "TcpSessionState" / Int32ul,
        "InternalCompartmentId" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1004, version=0)
class Microsoft_Windows_WinNat_1004_0(Etw):
    pattern = Struct(
        "InternalAddrLen" / Int32ul,
        "InternalSrcAddr" / Bytes(lambda this: this.InternalAddrLen),
        "InternalDstAddr" / Bytes(lambda this: this.InternalAddrLen),
        "ExternalAddrLen" / Int32ul,
        "ExternalSrcAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "ExternalDstAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "TransportProtocol" / Int32ul,
        "Lifetime" / Int32ul,
        "TcpSessionState" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1004, version=1)
class Microsoft_Windows_WinNat_1004_1(Etw):
    pattern = Struct(
        "InternalAddrLen" / Int32ul,
        "InternalSrcAddr" / Bytes(lambda this: this.InternalAddrLen),
        "InternalDstAddr" / Bytes(lambda this: this.InternalAddrLen),
        "ExternalAddrLen" / Int32ul,
        "ExternalSrcAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "ExternalDstAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "TransportProtocol" / Int32ul,
        "Lifetime" / Int32ul,
        "TcpSessionState" / Int32ul,
        "InternalCompartmentId" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1005, version=0)
class Microsoft_Windows_WinNat_1005_0(Etw):
    pattern = Struct(
        "InternalAddrLen" / Int32ul,
        "InternalSrcAddr" / Bytes(lambda this: this.InternalAddrLen),
        "InternalDstAddr" / Bytes(lambda this: this.InternalAddrLen),
        "ExternalAddrLen" / Int32ul,
        "ExternalSrcAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "ExternalDstAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "TransportProtocol" / Int32ul,
        "Lifetime" / Int32ul,
        "TcpSessionState" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1005, version=1)
class Microsoft_Windows_WinNat_1005_1(Etw):
    pattern = Struct(
        "InternalAddrLen" / Int32ul,
        "InternalSrcAddr" / Bytes(lambda this: this.InternalAddrLen),
        "InternalDstAddr" / Bytes(lambda this: this.InternalAddrLen),
        "ExternalAddrLen" / Int32ul,
        "ExternalSrcAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "ExternalDstAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "TransportProtocol" / Int32ul,
        "Lifetime" / Int32ul,
        "TcpSessionState" / Int32ul,
        "InternalCompartmentId" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1006, version=0)
class Microsoft_Windows_WinNat_1006_0(Etw):
    pattern = Struct(
        "InternalAddrLen" / Int32ul,
        "InternalAddr" / Bytes(lambda this: this.InternalAddrLen),
        "ExternalAddrLen" / Int32ul,
        "ExternalAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "TransportProtocol" / Int32ul,
        "SessionCount" / Int32ul,
        "Configured" / Int8ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1006, version=1)
class Microsoft_Windows_WinNat_1006_1(Etw):
    pattern = Struct(
        "InternalAddrLen" / Int32ul,
        "InternalAddr" / Bytes(lambda this: this.InternalAddrLen),
        "ExternalAddrLen" / Int32ul,
        "ExternalAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "TransportProtocol" / Int32ul,
        "SessionCount" / Int32ul,
        "Configured" / Int8ul,
        "InternalCompartmentId" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1007, version=0)
class Microsoft_Windows_WinNat_1007_0(Etw):
    pattern = Struct(
        "InternalAddrLen" / Int32ul,
        "InternalAddr" / Bytes(lambda this: this.InternalAddrLen),
        "ExternalAddrLen" / Int32ul,
        "ExternalAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "TransportProtocol" / Int32ul,
        "SessionCount" / Int32ul,
        "Configured" / Int8ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1007, version=1)
class Microsoft_Windows_WinNat_1007_1(Etw):
    pattern = Struct(
        "InternalAddrLen" / Int32ul,
        "InternalAddr" / Bytes(lambda this: this.InternalAddrLen),
        "ExternalAddrLen" / Int32ul,
        "ExternalAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "TransportProtocol" / Int32ul,
        "SessionCount" / Int32ul,
        "Configured" / Int8ul,
        "InternalCompartmentId" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1008, version=0)
class Microsoft_Windows_WinNat_1008_0(Etw):
    pattern = Struct(
        "InternalAddrLen" / Int32ul,
        "InternalAddr" / Bytes(lambda this: this.InternalAddrLen),
        "ExternalAddrLen" / Int32ul,
        "ExternalAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "TransportProtocol" / Int32ul,
        "SessionCount" / Int32ul,
        "Configured" / Int8ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1008, version=1)
class Microsoft_Windows_WinNat_1008_1(Etw):
    pattern = Struct(
        "InternalAddrLen" / Int32ul,
        "InternalAddr" / Bytes(lambda this: this.InternalAddrLen),
        "ExternalAddrLen" / Int32ul,
        "ExternalAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "TransportProtocol" / Int32ul,
        "SessionCount" / Int32ul,
        "Configured" / Int8ul,
        "InternalCompartmentId" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1009, version=0)
class Microsoft_Windows_WinNat_1009_0(Etw):
    pattern = Struct(
        "IncomingAddrLen" / Int32ul,
        "IncomingSrcAddr" / Bytes(lambda this: this.IncomingAddrLen),
        "IncomingDstAddr" / Bytes(lambda this: this.IncomingAddrLen),
        "TranslatedAddrLen" / Int32ul,
        "TranslatedSrcAddr" / Bytes(lambda this: this.TranslatedAddrLen),
        "TranslatedDstAddr" / Bytes(lambda this: this.TranslatedAddrLen),
        "Identification" / Int32ul,
        "TransportProtocol" / Int32ul,
        "Status" / Int32ul,
        "IcmpType" / Int32ul,
        "IcmpCode" / Int32ul,
        "IcmpPayload" / Int8ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1010, version=0)
class Microsoft_Windows_WinNat_1010_0(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "UdpIdleSessionTimeout" / Int32ul,
        "TcpTransientConnectionTimeout" / Int32ul,
        "TcpEstablishedConnectionTimeout" / Int32ul,
        "IcmpQueryTimeout" / Int32ul,
        "TcpFilteringBehavior" / Int32ul,
        "UdpFilteringBehavior" / Int32ul,
        "UdpInboundRefresh" / Int8ul,
        "Enabled" / Int8ul,
        "Status" / Int32ul,
        "Action" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1011, version=0)
class Microsoft_Windows_WinNat_1011_0(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "InternalPrefixAddrLength" / Int32ul,
        "InternalSrcPrefix" / Bytes(lambda this: this.InternalPrefixAddrLength),
        "InternalSrcPrefixLength" / Int32ul,
        "InternaDstlPrefix" / Bytes(lambda this: this.InternalPrefixAddrLength),
        "InternalDstPrefixLength" / Int32ul,
        "IPv4Prefix" / Int32ul,
        "IPv4PrefixLength" / Int32ul,
        "Nat64" / Int8ul,
        "InterfaceLuid" / Int64ul,
        "FilterId" / Int64ul,
        "Action" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1012, version=0)
class Microsoft_Windows_WinNat_1012_0(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "InternalPrefixAddrLength" / Int32ul,
        "InternalSrcPrefix" / Bytes(lambda this: this.InternalPrefixAddrLength),
        "InternalSrcPrefixLength" / Int32ul,
        "InternaDstlPrefix" / Bytes(lambda this: this.InternalPrefixAddrLength),
        "InternalDstPrefixLength" / Int32ul,
        "IPv4Prefix" / Int32ul,
        "IPv4PrefixLength" / Int32ul,
        "Nat64" / Int8ul,
        "InterfaceLuid" / Int64ul,
        "FilterId" / Int64ul,
        "Action" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1013, version=0)
class Microsoft_Windows_WinNat_1013_0(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "Address" / Int32ul,
        "StartingPort" / Int16ul,
        "EndingPort" / Int16ul,
        "InterfaceLuid" / Int64ul,
        "Action" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1014, version=0)
class Microsoft_Windows_WinNat_1014_0(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "Address" / Int32ul,
        "StartingPort" / Int16ul,
        "EndingPort" / Int16ul,
        "InterfaceLuid" / Int64ul,
        "Action" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1015, version=0)
class Microsoft_Windows_WinNat_1015_0(Etw):
    pattern = Struct(
        "InternalAddrLen" / Int32ul,
        "InternalAddr" / Bytes(lambda this: this.InternalAddrLen),
        "ExternalAddrLen" / Int32ul,
        "ExternalAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "TransportProtocol" / Int32ul,
        "Action" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1016, version=0)
class Microsoft_Windows_WinNat_1016_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1017, version=0)
class Microsoft_Windows_WinNat_1017_0(Etw):
    pattern = Struct(
        "InternalAddrLen" / Int32ul,
        "InternalSrcAddr" / Bytes(lambda this: this.InternalAddrLen),
        "InternalDstAddr" / Bytes(lambda this: this.InternalAddrLen),
        "ExternalAddrLen" / Int32ul,
        "ExternalSrcAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "ExternalDstAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "TransportProtocol" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1018, version=0)
class Microsoft_Windows_WinNat_1018_0(Etw):
    pattern = Struct(
        "InternalAddrLen" / Int32ul,
        "InternalSrcAddr" / Bytes(lambda this: this.InternalAddrLen),
        "InternalDstAddr" / Bytes(lambda this: this.InternalAddrLen),
        "ExternalAddrLen" / Int32ul,
        "ExternalSrcAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "ExternalDstAddr" / Bytes(lambda this: this.ExternalAddrLen),
        "TransportProtocol" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1019, version=0)
class Microsoft_Windows_WinNat_1019_0(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "InternalRoutingDomainId" / Guid,
        "ExternalIPInterfaceAddressPrefixLength" / Int32ul,
        "ExternalIPInterfaceAddressPrefix" / Int32ul,
        "CompartmentId" / Int32ul,
        "ExternalInterfaceIndex" / Int32ul,
        "UdpIdleSessionTimeout" / Int32ul,
        "TcpTransientConnectionTimeout" / Int32ul,
        "TcpEstablishedConnectionTimeout" / Int32ul,
        "IcmpQueryTimeout" / Int32ul,
        "TcpFilteringBehavior" / Int32ul,
        "UdpFilteringBehavior" / Int32ul,
        "UdpInboundRefresh" / Int8ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1019, version=1)
class Microsoft_Windows_WinNat_1019_1(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "InternalRoutingDomainId" / Guid,
        "PrefixLength" / Int32ul,
        "AddressPrefix" / Int32ul,
        "CompartmentId" / Int32ul,
        "ExternalInterfaceIndex" / Int32ul,
        "UdpIdleSessionTimeout" / Int32ul,
        "TcpTransientConnectionTimeout" / Int32ul,
        "TcpEstablishedConnectionTimeout" / Int32ul,
        "IcmpQueryTimeout" / Int32ul,
        "TcpFilteringBehavior" / Int32ul,
        "UdpFilteringBehavior" / Int32ul,
        "UdpInboundRefresh" / Int8ul,
        "InstanceType" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1020, version=0)
class Microsoft_Windows_WinNat_1020_0(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "InternalRoutingDomainId" / Guid,
        "ExternalIPInterfaceAddressPrefixLength" / Int32ul,
        "ExternalIPInterfaceAddressPrefix" / Int32ul,
        "CompartmentId" / Int32ul,
        "ExternalInterfaceIndex" / Int32ul,
        "UdpIdleSessionTimeout" / Int32ul,
        "TcpTransientConnectionTimeout" / Int32ul,
        "TcpEstablishedConnectionTimeout" / Int32ul,
        "IcmpQueryTimeout" / Int32ul,
        "TcpFilteringBehavior" / Int32ul,
        "UdpFilteringBehavior" / Int32ul,
        "UdpInboundRefresh" / Int8ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1021, version=0)
class Microsoft_Windows_WinNat_1021_0(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "InternalRoutingDomainId" / Guid,
        "ExternalIPInterfaceAddressPrefixLength" / Int32ul,
        "ExternalIPInterfaceAddressPrefix" / Int32ul,
        "CompartmentId" / Int32ul,
        "ExternalInterfaceIndex" / Int32ul,
        "UdpIdleSessionTimeout" / Int32ul,
        "TcpTransientConnectionTimeout" / Int32ul,
        "TcpEstablishedConnectionTimeout" / Int32ul,
        "IcmpQueryTimeout" / Int32ul,
        "TcpFilteringBehavior" / Int32ul,
        "UdpFilteringBehavior" / Int32ul,
        "UdpInboundRefresh" / Int8ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1022, version=0)
class Microsoft_Windows_WinNat_1022_0(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "InternalRoutingDomainId" / Guid,
        "ExternalIPInterfaceAddressPrefixLength" / Int32ul,
        "ExternalIPInterfaceAddressPrefix" / Int32ul,
        "CompartmentId" / Int32ul,
        "ExternalInterfaceIndex" / Int32ul,
        "UdpIdleSessionTimeout" / Int32ul,
        "TcpTransientConnectionTimeout" / Int32ul,
        "TcpEstablishedConnectionTimeout" / Int32ul,
        "IcmpQueryTimeout" / Int32ul,
        "TcpFilteringBehavior" / Int32ul,
        "UdpFilteringBehavior" / Int32ul,
        "UdpInboundRefresh" / Int8ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1023, version=0)
class Microsoft_Windows_WinNat_1023_0(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "InternalRoutingDomainId" / Guid,
        "ExternalIPInterfaceAddressPrefixLength" / Int32ul,
        "ExternalIPInterfaceAddressPrefix" / Int32ul,
        "CompartmentId" / Int32ul,
        "ExternalInterfaceIndex" / Int32ul,
        "UdpIdleSessionTimeout" / Int32ul,
        "TcpTransientConnectionTimeout" / Int32ul,
        "TcpEstablishedConnectionTimeout" / Int32ul,
        "IcmpQueryTimeout" / Int32ul,
        "TcpFilteringBehavior" / Int32ul,
        "UdpFilteringBehavior" / Int32ul,
        "UdpInboundRefresh" / Int8ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1023, version=1)
class Microsoft_Windows_WinNat_1023_1(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "InternalRoutingDomainId" / Guid,
        "PrefixLength" / Int32ul,
        "AddressPrefix" / Int32ul,
        "CompartmentId" / Int32ul,
        "ExternalInterfaceIndex" / Int32ul,
        "UdpIdleSessionTimeout" / Int32ul,
        "TcpTransientConnectionTimeout" / Int32ul,
        "TcpEstablishedConnectionTimeout" / Int32ul,
        "IcmpQueryTimeout" / Int32ul,
        "TcpFilteringBehavior" / Int32ul,
        "UdpFilteringBehavior" / Int32ul,
        "UdpInboundRefresh" / Int8ul,
        "InstanceType" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1024, version=0)
class Microsoft_Windows_WinNat_1024_0(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "AddressLength" / Int32ul,
        "IPAddress" / Bytes(lambda this: this.AddressLength),
        "PortStart" / Int16ul,
        "PortEnd" / Int16ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1025, version=0)
class Microsoft_Windows_WinNat_1025_0(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "AddressLength" / Int32ul,
        "IPAddress" / Bytes(lambda this: this.AddressLength),
        "PortStart" / Int16ul,
        "PortEnd" / Int16ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1026, version=0)
class Microsoft_Windows_WinNat_1026_0(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "AddressLength" / Int32ul,
        "IPAddress" / Bytes(lambda this: this.AddressLength),
        "PortStart" / Int16ul,
        "PortEnd" / Int16ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1027, version=0)
class Microsoft_Windows_WinNat_1027_0(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "TransportProtocol" / Int32ul,
        "MappingType" / Int32ul,
        "AddressLength" / Int32ul,
        "ExternalTransportAddress" / Bytes(lambda this: this.AddressLength),
        "InternalTransportAddress" / Bytes(lambda this: this.AddressLength),
        "InternalRoutingDomainId" / Guid,
        "CompartmentId" / Int32ul,
        "RemoteAddressPrefix" / Bytes(lambda this: this.AddressLength),
        "RemoteAddressPrefixLength" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1028, version=0)
class Microsoft_Windows_WinNat_1028_0(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "TransportProtocol" / Int32ul,
        "MappingType" / Int32ul,
        "AddressLength" / Int32ul,
        "ExternalTransportAddress" / Bytes(lambda this: this.AddressLength),
        "InternalTransportAddress" / Bytes(lambda this: this.AddressLength),
        "InternalRoutingDomainId" / Guid,
        "CompartmentId" / Int32ul,
        "RemoteAddressPrefix" / Bytes(lambda this: this.AddressLength),
        "RemoteAddressPrefixLength" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1029, version=0)
class Microsoft_Windows_WinNat_1029_0(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "TransportProtocol" / Int32ul,
        "MappingType" / Int32ul,
        "AddressLength" / Int32ul,
        "ExternalTransportAddress" / Bytes(lambda this: this.AddressLength),
        "InternalTransportAddress" / Bytes(lambda this: this.AddressLength),
        "InternalRoutingDomainId" / Guid,
        "CompartmentId" / Int32ul,
        "RemoteAddressPrefix" / Bytes(lambda this: this.AddressLength),
        "RemoteAddressPrefixLength" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1030, version=0)
class Microsoft_Windows_WinNat_1030_0(Etw):
    pattern = Struct(
        "ActionReason" / Int32ul,
        "ArrivalCompartmentId" / Int32ul,
        "ArrivalInterfaceIndex" / Int32ul,
        "ArrivalNetwork" / Int32ul,
        "TransportProtocol" / Int32ul,
        "ForwardCompartmentId" / Int32ul,
        "ForwardInterfaceIndex" / Int32ul,
        "PacketLength" / Int32ul,
        "ContinuousLength" / Int32ul,
        "CapturedIPHeaderLength" / Int32ul,
        "CapturedTransportHeaderLength" / Int32ul,
        "ICMPErrorTransportProtocol" / Int32ul,
        "ICMPErrorCapturedIPHeaderLength" / Int32ul,
        "ICMPErrorCapturedTransportHeaderLength" / Int32ul,
        "IPHeader" / Bytes(lambda this: this.CapturedIPHeaderLength),
        "TransportHeader" / Bytes(lambda this: this.CapturedTransportHeaderLength),
        "ICMPErrorIPHeader" / Bytes(lambda this: this.ICMPErrorCapturedIPHeaderLength),
        "ICMPErrorTransportHeader" / Bytes(lambda this: this.ICMPErrorCapturedTransportHeaderLength)
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1031, version=0)
class Microsoft_Windows_WinNat_1031_0(Etw):
    pattern = Struct(
        "CompartmentId" / Int32ul,
        "InterfaceIndex" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1032, version=0)
class Microsoft_Windows_WinNat_1032_0(Etw):
    pattern = Struct(
        "CompartmentId" / Int32ul,
        "InterfaceIndex" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1033, version=0)
class Microsoft_Windows_WinNat_1033_0(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "TransportProtocol" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1034, version=0)
class Microsoft_Windows_WinNat_1034_0(Etw):
    pattern = Struct(
        "ActionReason" / Int32ul,
        "ArrivalCompartmentId" / Int32ul,
        "ArrivalInterfaceIndex" / Int32ul,
        "ArrivalNetwork" / Int32ul,
        "TransportProtocol" / Int32ul,
        "ForwardCompartmentId" / Int32ul,
        "ForwardInterfaceIndex" / Int32ul,
        "PacketLength" / Int32ul,
        "ContinuousLength" / Int32ul,
        "CapturedIPHeaderLength" / Int32ul,
        "CapturedTransportHeaderLength" / Int32ul,
        "ICMPErrorTransportProtocol" / Int32ul,
        "ICMPErrorCapturedIPHeaderLength" / Int32ul,
        "ICMPErrorCapturedTransportHeaderLength" / Int32ul,
        "IPHeader" / Bytes(lambda this: this.CapturedIPHeaderLength),
        "TransportHeader" / Bytes(lambda this: this.CapturedTransportHeaderLength),
        "ICMPErrorIPHeader" / Bytes(lambda this: this.ICMPErrorCapturedIPHeaderLength),
        "ICMPErrorTransportHeader" / Bytes(lambda this: this.ICMPErrorCapturedTransportHeaderLength)
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1035, version=0)
class Microsoft_Windows_WinNat_1035_0(Etw):
    pattern = Struct(
        "ActionReason" / Int32ul,
        "ArrivalCompartmentId" / Int32ul,
        "ArrivalInterfaceIndex" / Int32ul,
        "ArrivalNetwork" / Int32ul,
        "TransportProtocol" / Int32ul,
        "ForwardCompartmentId" / Int32ul,
        "ForwardInterfaceIndex" / Int32ul,
        "PacketLength" / Int32ul,
        "ContinuousLength" / Int32ul,
        "CapturedIPHeaderLength" / Int32ul,
        "CapturedTransportHeaderLength" / Int32ul,
        "ICMPErrorTransportProtocol" / Int32ul,
        "ICMPErrorCapturedIPHeaderLength" / Int32ul,
        "ICMPErrorCapturedTransportHeaderLength" / Int32ul,
        "IPHeader" / Bytes(lambda this: this.CapturedIPHeaderLength),
        "TransportHeader" / Bytes(lambda this: this.CapturedTransportHeaderLength),
        "ICMPErrorIPHeader" / Bytes(lambda this: this.ICMPErrorCapturedIPHeaderLength),
        "ICMPErrorTransportHeader" / Bytes(lambda this: this.ICMPErrorCapturedTransportHeaderLength)
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1036, version=0)
class Microsoft_Windows_WinNat_1036_0(Etw):
    pattern = Struct(
        "ErrorID" / Int32ul,
        "ErrorContext" / WString,
        "ErrorMisc" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1037, version=0)
class Microsoft_Windows_WinNat_1037_0(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "InternalRoutingDomainId" / Guid,
        "ExternalIPInterfaceAddressPrefixLength" / Int32ul,
        "ExternalIPInterfaceAddressPrefix" / Int32ul,
        "CompartmentId" / Int32ul,
        "ExternalInterfaceIndex" / Int32ul,
        "UdpIdleSessionTimeout" / Int32ul,
        "TcpTransientConnectionTimeout" / Int32ul,
        "TcpEstablishedConnectionTimeout" / Int32ul,
        "IcmpQueryTimeout" / Int32ul,
        "TcpFilteringBehavior" / Int32ul,
        "UdpFilteringBehavior" / Int32ul,
        "UdpInboundRefresh" / Int8ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1037, version=1)
class Microsoft_Windows_WinNat_1037_1(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "InternalRoutingDomainId" / Guid,
        "PrefixLength" / Int32ul,
        "AddressPrefix" / Int32ul,
        "CompartmentId" / Int32ul,
        "ExternalInterfaceIndex" / Int32ul,
        "UdpIdleSessionTimeout" / Int32ul,
        "TcpTransientConnectionTimeout" / Int32ul,
        "TcpEstablishedConnectionTimeout" / Int32ul,
        "IcmpQueryTimeout" / Int32ul,
        "TcpFilteringBehavior" / Int32ul,
        "UdpFilteringBehavior" / Int32ul,
        "UdpInboundRefresh" / Int8ul,
        "InstanceType" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1038, version=0)
class Microsoft_Windows_WinNat_1038_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1039, version=0)
class Microsoft_Windows_WinNat_1039_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1040, version=0)
class Microsoft_Windows_WinNat_1040_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1041, version=0)
class Microsoft_Windows_WinNat_1041_0(Etw):
    pattern = Struct(
        "InterfaceLuid" / Int64ul,
        "FallbackIPv4Address" / Int32ul,
        "SyntheticIPv4Address" / Int32ul,
        "RemotePrefixLength" / Int32ul,
        "LocalPrefixLength" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1042, version=0)
class Microsoft_Windows_WinNat_1042_0(Etw):
    pattern = Struct(
        "InterfaceLuid" / Int64ul,
        "FallbackIPv4Address" / Int32ul,
        "SyntheticIPv4Address" / Int32ul,
        "RemotePrefixLength" / Int32ul,
        "LocalPrefixLength" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1043, version=0)
class Microsoft_Windows_WinNat_1043_0(Etw):
    pattern = Struct(
        "InterfaceLuid" / Int64ul,
        "FallbackIPv4Address" / Int32ul,
        "SyntheticIPv4Address" / Int32ul,
        "RemotePrefixLength" / Int32ul,
        "LocalPrefixLength" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1044, version=0)
class Microsoft_Windows_WinNat_1044_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1045, version=0)
class Microsoft_Windows_WinNat_1045_0(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "AddressLength" / Int32ul,
        "IPAddress" / Bytes(lambda this: this.AddressLength),
        "IfIndex" / Int32ul
    )


@declare(guid=guid("66c07ecd-6667-43fc-93f8-05cf07f446ec"), event_id=1046, version=0)
class Microsoft_Windows_WinNat_1046_0(Etw):
    pattern = Struct(
        "InstanceName" / WString,
        "AddressLength" / Int32ul,
        "IPAddress" / Bytes(lambda this: this.AddressLength),
        "IfIndex" / Int32ul
    )

