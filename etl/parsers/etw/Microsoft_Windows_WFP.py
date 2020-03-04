# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WFP
GUID : 0c478c5b-0351-41b1-8c58-4a6737da32e3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1001, version=0)
class Microsoft_Windows_WFP_1001_0(Etw):
    pattern = Struct(
        "Timestamp" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "ScopeId" / Int32ul,
        "AppId" / WString,
        "UserSID" / Sid,
        "ReauthReason" / Int32ul,
        "OriginalProfile" / Int32ul,
        "CurrentProfile" / Int32ul,
        "PacketDirection" / Int32ul,
        "Loopback" / Int8ul,
        "FilterId" / Int64ul,
        "LayerId" / Int16ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1001, version=1)
class Microsoft_Windows_WFP_1001_1(Etw):
    pattern = Struct(
        "Timestamp" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "ScopeId" / Int32ul,
        "AppId" / WString,
        "UserSID" / Sid,
        "ReauthReason" / Int32ul,
        "OriginalProfile" / Int32ul,
        "CurrentProfile" / Int32ul,
        "PacketDirection" / Int32ul,
        "Loopback" / Int8ul,
        "FilterId" / Int64ul,
        "LayerId" / Int16ul,
        "vSwitchId" / WString,
        "SourcevSwitchPort" / Int32ul,
        "DestinationvSwitchPort" / Int32ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1001, version=2)
class Microsoft_Windows_WFP_1001_2(Etw):
    pattern = Struct(
        "Timestamp" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "ScopeId" / Int32ul,
        "AppId" / WString,
        "UserSID" / Sid,
        "ReauthReason" / Int32ul,
        "OriginalProfile" / Int32ul,
        "CurrentProfile" / Int32ul,
        "PacketDirection" / Int32ul,
        "Loopback" / Int8ul,
        "FilterId" / Int64ul,
        "LayerId" / Int16ul,
        "vSwitchId" / WString,
        "SourcevSwitchPort" / Int32ul,
        "DestinationvSwitchPort" / Int32ul,
        "EnterpriseId" / WString,
        "PolicyFlags" / Int64ul,
        "EffectiveName" / WString
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1003, version=0)
class Microsoft_Windows_WFP_1003_0(Etw):
    pattern = Struct(
        "Timestamp" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "ScopeId" / Int32ul,
        "AppId" / WString,
        "UserSID" / Sid,
        "FailureStatus" / Int32ul,
        "Direction" / Int32ul,
        "SPI" / Int32ul,
        "FilterId" / Int64ul,
        "LayerId" / Int16ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1005, version=0)
class Microsoft_Windows_WFP_1005_0(Etw):
    pattern = Struct(
        "Timestamp" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "ScopeId" / Int32ul,
        "AppId" / WString,
        "UserSID" / Sid,
        "LocalSpn" / WString,
        "PeerSpn" / WString,
        "LocalGroupSidCount" / Int32ul,
        "LocalGroupSidLength" / Int32ul,
        "LocalGroupSids" / WString,
        "RemoteGroupSidCount" / Int32ul,
        "RemoteGroupSidLength" / Int32ul,
        "RemoteGroupSids" / WString,
        "FailureErrorCode" / Int32ul,
        "FailurePoint" / Int32ul,
        "Flags" / Int32ul,
        "KeyingModuleType" / Int32ul,
        "MmState" / Int32ul,
        "SaRole" / Int32ul,
        "MMAuthMethod" / Int32ul,
        "MMId" / Int64ul,
        "MMFilterId" / Int64ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1005, version=1)
class Microsoft_Windows_WFP_1005_1(Etw):
    pattern = Struct(
        "Timestamp" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "ScopeId" / Int32ul,
        "AppId" / WString,
        "UserSID" / Sid,
        "LocalSpn" / WString,
        "PeerSpn" / WString,
        "LocalGroupSidCount" / Int32ul,
        "LocalGroupSidLength" / Int32ul,
        "LocalGroupSids" / WString,
        "RemoteGroupSidCount" / Int32ul,
        "RemoteGroupSidLength" / Int32ul,
        "RemoteGroupSids" / WString,
        "FailureErrorCode" / Int32ul,
        "FailurePoint" / Int32ul,
        "Flags" / Int32ul,
        "KeyingModuleType" / Int32ul,
        "MmState" / Int32ul,
        "SaRole" / Int32ul,
        "MMAuthMethod" / Int32ul,
        "MMId" / Int64ul,
        "MMFilterId" / Int64ul,
        "ProviderContextKey" / Guid
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1007, version=0)
class Microsoft_Windows_WFP_1007_0(Etw):
    pattern = Struct(
        "Timestamp" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "ScopeId" / Int32ul,
        "AppId" / WString,
        "UserSID" / Sid,
        "FailureErrorCode" / Int32ul,
        "FailurePoint" / Int32ul,
        "KeyingModuleType" / Int32ul,
        "QMState" / Int32ul,
        "SaRole" / Int32ul,
        "SaTrafficType" / Int32ul,
        "QMFilterId" / Int64ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1007, version=1)
class Microsoft_Windows_WFP_1007_1(Etw):
    pattern = Struct(
        "Timestamp" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "ScopeId" / Int32ul,
        "AppId" / WString,
        "UserSID" / Sid,
        "FailureErrorCode" / Int32ul,
        "FailurePoint" / Int32ul,
        "KeyingModuleType" / Int32ul,
        "QMState" / Int32ul,
        "SaRole" / Int32ul,
        "SaTrafficType" / Int32ul,
        "QMFilterId" / Int64ul,
        "MMSaLuid" / Int64ul,
        "MMProviderContextKey" / Guid
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1009, version=0)
class Microsoft_Windows_WFP_1009_0(Etw):
    pattern = Struct(
        "Timestamp" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "ScopeId" / Int32ul,
        "AppId" / WString,
        "UserSID" / Sid,
        "LocalSpn" / WString,
        "PeerSpn" / WString,
        "LocalGroupSidCount" / Int32ul,
        "LocalGroupSidLength" / Int32ul,
        "LocalGroupSids" / WString,
        "RemoteGroupSidCount" / Int32ul,
        "RemoteGroupSidLength" / Int32ul,
        "RemoteGroupSids" / WString,
        "FailureErrorCode" / Int32ul,
        "FailurePoint" / Int32ul,
        "Flags" / Int32ul,
        "EMState" / Int32ul,
        "SaRole" / Int32ul,
        "EMAuthMethod" / Int32ul,
        "MMId" / Int64ul,
        "QMFilterId" / Int64ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1011, version=0)
class Microsoft_Windows_WFP_1011_0(Etw):
    pattern = Struct(
        "Timestamp" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "ScopeId" / Int32ul,
        "AppId" / WString,
        "UserSID" / Sid,
        "InternetHostAddress" / Int32ul,
        "CorpnetHostAddress" / Int32ul,
        "FailureStatus" / Int32ul,
        "Direction" / Int32ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1013, version=0)
class Microsoft_Windows_WFP_1013_0(Etw):
    pattern = Struct(
        "MainModeLocalAddressLength" / Int32ul,
        "MainModeLocalAddress" / Bytes(lambda this: this.MainModeLocalAddressLength),
        "MainModePeerAddressLength" / Int32ul,
        "MainModePeerAddress" / Bytes(lambda this: this.MainModePeerAddressLength),
        "KeyingModule" / Int32ul,
        "SaLuid" / Int64ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1013, version=1)
class Microsoft_Windows_WFP_1013_1(Etw):
    pattern = Struct(
        "MainModeLocalAddressLength" / Int32ul,
        "MainModeLocalAddress" / Bytes(lambda this: this.MainModeLocalAddressLength),
        "MainModePeerAddressLength" / Int32ul,
        "MainModePeerAddress" / Bytes(lambda this: this.MainModePeerAddressLength),
        "KeyingModule" / Int32ul,
        "SaLuid" / Int64ul,
        "ICookie" / Int64ul,
        "RCookie" / Int64ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1014, version=0)
class Microsoft_Windows_WFP_1014_0(Etw):
    pattern = Struct(
        "LocalSpn" / WString,
        "PeerSpn" / WString,
        "MainModeLocalAddressLength" / Int32ul,
        "MainModeLocalAddress" / Bytes(lambda this: this.MainModeLocalAddressLength),
        "MainModePeerAddressLength" / Int32ul,
        "MainModePeerAddress" / Bytes(lambda this: this.MainModePeerAddressLength),
        "KeyingModule" / Int32ul,
        "AuthenticationMethodType" / Int32ul,
        "EncryptionAlgorithm" / Int32ul,
        "AuthenticationAlgorithm" / Int32ul,
        "DiffieHellmanGroup" / Int32ul,
        "LifetimeMinutes" / Int32ul,
        "QMLimit" / Int32ul,
        "Role" / Int32ul,
        "Impersonation" / Int32ul,
        "MMFilterId" / Int64ul,
        "SaLuid" / Int64ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1015, version=0)
class Microsoft_Windows_WFP_1015_0(Etw):
    pattern = Struct(
        "LocalCertDnSubject" / WString,
        "LocalCertShaThumbprintLength" / Int32ul,
        "LocalCertShaThumbprint" / Bytes(lambda this: this.LocalCertShaThumbprintLength),
        "LocalCertDnIssuer" / WString,
        "LocalCertDnRoot" / WString,
        "PeerCertDnSubject" / WString,
        "PeerCertShaThumbprintLength" / Int32ul,
        "PeerCertShaThumbprint" / Bytes(lambda this: this.PeerCertShaThumbprintLength),
        "PeerCertDnIssuer" / WString,
        "PeerCertDnRoot" / WString,
        "MainModeLocalAddressLength" / Int32ul,
        "MainModeLocalAddress" / Bytes(lambda this: this.MainModeLocalAddressLength),
        "MainModePeerAddressLength" / Int32ul,
        "MainModePeerAddress" / Bytes(lambda this: this.MainModePeerAddressLength),
        "KeyingModule" / Int32ul,
        "AuthenticationMethodType" / Int32ul,
        "EncryptionAlgorithm" / Int32ul,
        "AuthenticationAlgorithm" / Int32ul,
        "DiffieHellmanGroup" / Int32ul,
        "LifetimeMinutes" / Int32ul,
        "QMLimit" / Int32ul,
        "Role" / Int32ul,
        "Impersonation" / Int32ul,
        "MMFilterId" / Int64ul,
        "SaLuid" / Int64ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1016, version=0)
class Microsoft_Windows_WFP_1016_0(Etw):
    pattern = Struct(
        "LocalCertDnSubject" / WString,
        "LocalCertShaThumbprintLength" / Int32ul,
        "LocalCertShaThumbprint" / Bytes(lambda this: this.LocalCertShaThumbprintLength),
        "LocalCertDnIssuer" / WString,
        "LocalCertDnRoot" / WString,
        "PeerCertDnSubject" / WString,
        "PeerCertShaThumbprintLength" / Int32ul,
        "PeerCertShaThumbprint" / Bytes(lambda this: this.PeerCertShaThumbprintLength),
        "PeerCertDnIssuer" / WString,
        "PeerCertDnRoot" / WString,
        "MainModeLocalAddressLength" / Int32ul,
        "MainModeLocalAddress" / Bytes(lambda this: this.MainModeLocalAddressLength),
        "MainModePeerAddressLength" / Int32ul,
        "MainModePeerAddress" / Bytes(lambda this: this.MainModePeerAddressLength),
        "EncryptionAlgorithm" / Int32ul,
        "AuthenticationAlgorithm" / Int32ul,
        "DiffieHellmanGroup" / Int32ul,
        "LifetimeMinutes" / Int32ul,
        "QMLimit" / Int32ul,
        "Role" / Int32ul,
        "Impersonation" / Int32ul,
        "MMFilterId" / Int64ul,
        "SaLuid" / Int64ul,
        "LocalUmCertDnSubject" / WString,
        "LocalUmCertShaThumbprintLength" / Int32ul,
        "LocalUmCertShaThumbprint" / Bytes(lambda this: this.LocalUmCertShaThumbprintLength),
        "LocalUmCertDnIssuer" / WString,
        "LocalUmCertDnRoot" / WString,
        "PeerUmCertDnSubject" / WString,
        "PeerUmCertShaThumbprintLength" / Int32ul,
        "PeerUmCertShaThumbprint" / Bytes(lambda this: this.PeerUmCertShaThumbprintLength),
        "PeerUmCertDnIssuer" / WString,
        "PeerUmCertDnRoot" / WString,
        "UMImpersonation" / Int32ul,
        "QMFilterId" / Int64ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1017, version=0)
class Microsoft_Windows_WFP_1017_0(Etw):
    pattern = Struct(
        "LocalCertDnSubject" / WString,
        "LocalCertShaThumbprintLength" / Int32ul,
        "LocalCertShaThumbprint" / Bytes(lambda this: this.LocalCertShaThumbprintLength),
        "LocalCertDnIssuer" / WString,
        "LocalCertDnRoot" / WString,
        "PeerCertDnSubject" / WString,
        "PeerCertShaThumbprintLength" / Int32ul,
        "PeerCertShaThumbprint" / Bytes(lambda this: this.PeerCertShaThumbprintLength),
        "PeerCertDnIssuer" / WString,
        "PeerCertDnRoot" / WString,
        "MainModeLocalAddressLength" / Int32ul,
        "MainModeLocalAddress" / Bytes(lambda this: this.MainModeLocalAddressLength),
        "MainModePeerAddressLength" / Int32ul,
        "MainModePeerAddress" / Bytes(lambda this: this.MainModePeerAddressLength),
        "EncryptionAlgorithm" / Int32ul,
        "AuthenticationAlgorithm" / Int32ul,
        "DiffieHellmanGroup" / Int32ul,
        "LifetimeMinutes" / Int32ul,
        "QMLimit" / Int32ul,
        "Role" / Int32ul,
        "Impersonation" / Int32ul,
        "MMFilterId" / Int64ul,
        "SaLuid" / Int64ul,
        "UMLocalSPN" / WString,
        "UMPeerSPN" / WString,
        "UMAuthenticationMethodType" / Int32ul,
        "UMImpersonation" / Int32ul,
        "QMFilterId" / Int64ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1018, version=0)
class Microsoft_Windows_WFP_1018_0(Etw):
    pattern = Struct(
        "LocalSPN" / WString,
        "PeerSPN" / WString,
        "MainModeLocalAddressLength" / Int32ul,
        "MainModeLocalAddress" / Bytes(lambda this: this.MainModeLocalAddressLength),
        "MainModePeerAddressLength" / Int32ul,
        "MainModePeerAddress" / Bytes(lambda this: this.MainModePeerAddressLength),
        "AuthenticationMethodType" / Int32ul,
        "EncryptionAlgorithm" / Int32ul,
        "AuthenticationAlgorithm" / Int32ul,
        "DiffieHellmanGroup" / Int32ul,
        "LifetimeMinutes" / Int32ul,
        "QMLimit" / Int32ul,
        "Role" / Int32ul,
        "Impersonation" / Int32ul,
        "MMFilterId" / Int64ul,
        "SaLuid" / Int64ul,
        "LocalUmCertDnSubject" / WString,
        "LocalUmCertShaThumbprintLength" / Int32ul,
        "LocalUmCertShaThumbprint" / Bytes(lambda this: this.LocalUmCertShaThumbprintLength),
        "LocalUmCertDnIssuer" / WString,
        "LocalUmCertDnRoot" / WString,
        "PeerUmCertDnSubject" / WString,
        "PeerUmCertShaThumbprintLength" / Int32ul,
        "PeerUmCertShaThumbprint" / Bytes(lambda this: this.PeerUmCertShaThumbprintLength),
        "PeerUmCertDnIssuer" / WString,
        "PeerUmCertDnRoot" / WString,
        "UMImpersonation" / Int32ul,
        "QMFilterId" / Int64ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1019, version=0)
class Microsoft_Windows_WFP_1019_0(Etw):
    pattern = Struct(
        "LocalSpn" / WString,
        "PeerSpn" / WString,
        "MainModeLocalAddressLength" / Int32ul,
        "MainModeLocalAddress" / Bytes(lambda this: this.MainModeLocalAddressLength),
        "MainModePeerAddressLength" / Int32ul,
        "MainModePeerAddress" / Bytes(lambda this: this.MainModePeerAddressLength),
        "AuthenticationMethodType" / Int32ul,
        "EncryptionAlgorithm" / Int32ul,
        "AuthenticationAlgorithm" / Int32ul,
        "DiffieHellmanGroup" / Int32ul,
        "LifetimeMinutes" / Int32ul,
        "QMLimit" / Int32ul,
        "Role" / Int32ul,
        "Impersonation" / Int32ul,
        "MMFilterId" / Int64ul,
        "SaLuid" / Int64ul,
        "UMLocalSPN" / WString,
        "UMPeerSPN" / WString,
        "UMAuthenticationMethodType" / Int32ul,
        "UMImpersonation" / Int32ul,
        "QMFilterId" / Int64ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1023, version=0)
class Microsoft_Windows_WFP_1023_0(Etw):
    pattern = Struct(
        "KeyingModule" / CString,
        "AcquireContext" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Mode" / WString,
        "FilterId" / Int64ul,
        "IPProtocol" / Int32ul,
        "InterfaceLuid" / Int64ul,
        "ProfileId" / Int32ul,
        "LocalUdpEncapPort" / Int16ul,
        "RemoteUdpEncapPort" / Int16ul,
        "MMTargetName" / WString,
        "EMTargetName" / WString,
        "NumTokens" / Int32ul,
        "Token1Type" / WString,
        "Token1Principal" / WString,
        "Token1Mode" / WString,
        "Token1" / Int64ul,
        "Token2Type" / WString,
        "Token2Principal" / WString,
        "Token2Mode" / WString,
        "Token2" / Int64ul,
        "Token3Type" / WString,
        "Token3Principal" / WString,
        "Token3Mode" / WString,
        "Token3" / Int64ul,
        "Token4Type" / WString,
        "Token4Principal" / WString,
        "Token4Mode" / WString,
        "Token4" / Int64ul,
        "VirtualIfTunnelId" / Int64ul,
        "TrafficSelectorId" / Int64ul,
        "Flags" / Int32ul,
        "RekeySPI" / Int32ul,
        "OrigVirtualIfTunnelId" / Int64ul,
        "PacketLocalAddressLength" / Int32ul,
        "PacketLocalAddress" / Bytes(lambda this: this.PacketLocalAddressLength),
        "PacketRemoteAddressLength" / Int32ul,
        "PacketRemoteAddress" / Bytes(lambda this: this.PacketRemoteAddressLength),
        "PacketIPProtocol" / Int32ul,
        "PacketInterfaceLuid" / Int64ul,
        "PacketProfileId" / Int32ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1024, version=0)
class Microsoft_Windows_WFP_1024_0(Etw):
    pattern = Struct(
        "ICookie" / CString,
        "RCookie" / CString,
        "ExchangeType" / CString,
        "Length" / Int32ul,
        "NextPayload" / CString,
        "Flags" / Int8ul,
        "MessageID" / Int32ul,
        "LocalAddress" / WString,
        "LocalPort" / Int32ul,
        "LocalProtocol" / Int32ul,
        "RemoteAddress" / WString,
        "RemotePort" / Int32ul,
        "RemoteProtocol" / Int32ul,
        "InterfaceLuid" / Int64ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1025, version=0)
class Microsoft_Windows_WFP_1025_0(Etw):
    pattern = Struct(
        "ICookie" / CString,
        "RCookie" / CString,
        "ExchangeType" / CString,
        "Length" / Int32ul,
        "NextPayload" / CString,
        "Flags" / Int8ul,
        "MessageID" / Int32ul,
        "LocalAddress" / WString,
        "LocalPort" / Int32ul,
        "LocalProtocol" / Int32ul,
        "RemoteAddress" / WString,
        "RemotePort" / Int32ul,
        "RemoteProtocol" / Int32ul,
        "InterfaceLuid" / Int64ul,
        "ProfileId" / Int32ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1026, version=0)
class Microsoft_Windows_WFP_1026_0(Etw):
    pattern = Struct(
        "Function" / CString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1027, version=0)
class Microsoft_Windows_WFP_1027_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "LocalAddressMask" / WString,
        "LocalTunnelEndpointLength" / Int32ul,
        "LocalTunnelEndpoint" / Bytes(lambda this: this.LocalTunnelEndpointLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "RemoteAddressMask" / WString,
        "RemoteTunnelEndpointLength" / Int32ul,
        "RemoteTunnelEndpoint" / Bytes(lambda this: this.RemoteTunnelEndpointLength),
        "IPProtocol" / Int32ul,
        "QMSaLuid" / Int64ul,
        "VirtualIFTunnelId" / Int64ul,
        "VirtualIFTrafficSelectorId" / Int64ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1027, version=1)
class Microsoft_Windows_WFP_1027_1(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "LocalAddressMask" / WString,
        "LocalTunnelEndpointLength" / Int32ul,
        "LocalTunnelEndpoint" / Bytes(lambda this: this.LocalTunnelEndpointLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "RemoteAddressMask" / WString,
        "RemoteTunnelEndpointLength" / Int32ul,
        "RemoteTunnelEndpoint" / Bytes(lambda this: this.RemoteTunnelEndpointLength),
        "IPProtocol" / Int32ul,
        "QMSaLuid" / Int64ul,
        "VirtualIFTunnelId" / Int64ul,
        "VirtualIFTrafficSelectorId" / Int64ul,
        "InboundSPI" / Int32ul,
        "OutboundSPI" / Int32ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1028, version=0)
class Microsoft_Windows_WFP_1028_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "LocalAddressMask" / WString,
        "LocalTunnelEndpointLength" / Int32ul,
        "LocalTunnelEndpoint" / Bytes(lambda this: this.LocalTunnelEndpointLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "RemoteAddressMask" / WString,
        "RemoteTunnelEndpointLength" / Int32ul,
        "RemoteTunnelEndpoint" / Bytes(lambda this: this.RemoteTunnelEndpointLength),
        "IPProtocol" / Int32ul,
        "KeyingModuleName" / Int8ul,
        "AHAuthType" / Int8ul,
        "ESPAuthType" / Int8ul,
        "ESPCipherType" / Int8ul,
        "LifetimeSeconds" / Int32ul,
        "LifetimeKilobytes" / Int32ul,
        "LifetimePackets" / Int32ul,
        "Mode" / Int8ul,
        "Role" / Int8ul,
        "TransportFilterId" / Int64ul,
        "MMSaLuid" / Int64ul,
        "QMSaLuid" / Int64ul,
        "InboundSPI" / Int32ul,
        "OutboundSPI" / Int32ul,
        "VirtualIFTunnelId" / Int64ul,
        "VirtualIFTrafficSelectorId" / Int64ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1028, version=1)
class Microsoft_Windows_WFP_1028_1(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "LocalAddressMask" / WString,
        "LocalTunnelEndpointLength" / Int32ul,
        "LocalTunnelEndpoint" / Bytes(lambda this: this.LocalTunnelEndpointLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "RemoteAddressMask" / WString,
        "RemoteTunnelEndpointLength" / Int32ul,
        "RemoteTunnelEndpoint" / Bytes(lambda this: this.RemoteTunnelEndpointLength),
        "IPProtocol" / Int32ul,
        "KeyingModuleName" / Int8ul,
        "AHAuthType" / Int8ul,
        "ESPAuthType" / Int8ul,
        "ESPCipherType" / Int8ul,
        "LifetimeSeconds" / Int32ul,
        "LifetimeKilobytes" / Int32ul,
        "LifetimePackets" / Int32ul,
        "Mode" / Int8ul,
        "Role" / Int8ul,
        "TransportFilterId" / Int64ul,
        "MMSaLuid" / Int64ul,
        "QMSaLuid" / Int64ul,
        "InboundSPI" / Int32ul,
        "OutboundSPI" / Int32ul,
        "VirtualIFTunnelId" / Int64ul,
        "VirtualIFTrafficSelectorId" / Int64ul,
        "RekeySPI" / Int32ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1029, version=0)
class Microsoft_Windows_WFP_1029_0(Etw):
    pattern = Struct(
        "Timestamp" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "EtherType" / Int16ul,
        "MediaType" / Int32ul,
        "InterfaceType" / Int32ul,
        "VlanTag" / Int16ul,
        "FilterId" / Int64ul,
        "LayerId" / Int16ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1029, version=1)
class Microsoft_Windows_WFP_1029_1(Etw):
    pattern = Struct(
        "Timestamp" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "EtherType" / Int16ul,
        "MediaType" / Int32ul,
        "InterfaceType" / Int32ul,
        "VlanTag" / Int16ul,
        "FilterId" / Int64ul,
        "LayerId" / Int16ul,
        "vSwitchId" / WString,
        "SourcevSwitchPort" / Int32ul,
        "DestinationvSwitchPort" / Int32ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1030, version=0)
class Microsoft_Windows_WFP_1030_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "TxnTimeInMSec" / Int32ul,
        "CommitTimeInMSec" / Int32ul,
        "WatchdogTimeoutInMSec" / Int32ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1031, version=0)
class Microsoft_Windows_WFP_1031_0(Etw):
    pattern = Struct(
        "Counter" / Int32ul,
        "FilePath" / WString
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1032, version=0)
class Microsoft_Windows_WFP_1032_0(Etw):
    pattern = Struct(
        "Counter" / Int32ul,
        "FilePath" / WString
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1033, version=0)
class Microsoft_Windows_WFP_1033_0(Etw):
    pattern = Struct(
        "Counter" / Int32ul,
        "AppSID" / Sid
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1034, version=0)
class Microsoft_Windows_WFP_1034_0(Etw):
    pattern = Struct(
        "Counter" / Int32ul,
        "AppSID" / Sid
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1035, version=0)
class Microsoft_Windows_WFP_1035_0(Etw):
    pattern = Struct(
        "Counter" / Int32ul,
        "SecurityDescriptor" / WString
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1036, version=0)
class Microsoft_Windows_WFP_1036_0(Etw):
    pattern = Struct(
        "Counter" / Int32ul,
        "SecurityDescriptor" / WString
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1037, version=0)
class Microsoft_Windows_WFP_1037_0(Etw):
    pattern = Struct(
        "Counter" / Int32ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1038, version=0)
class Microsoft_Windows_WFP_1038_0(Etw):
    pattern = Struct(
        "Counter" / Int32ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1039, version=0)
class Microsoft_Windows_WFP_1039_0(Etw):
    pattern = Struct(
        "Counter" / Int32ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "IPProtocol" / Int32ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1040, version=0)
class Microsoft_Windows_WFP_1040_0(Etw):
    pattern = Struct(
        "Counter" / Int32ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "IPProtocol" / Int32ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1041, version=0)
class Microsoft_Windows_WFP_1041_0(Etw):
    pattern = Struct(
        "Counter" / Int32ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1043, version=0)
class Microsoft_Windows_WFP_1043_0(Etw):
    pattern = Struct(
        "MainModeLocalAddressLength" / Int32ul,
        "MainModeLocalAddress" / Bytes(lambda this: this.MainModeLocalAddressLength),
        "MainModePeerAddressLength" / Int32ul,
        "MainModePeerAddress" / Bytes(lambda this: this.MainModePeerAddressLength),
        "KeyingModule" / Int32ul,
        "AuthenticationMethodType" / Int32ul,
        "EncryptionAlgorithm" / Int32ul,
        "AuthenticationAlgorithm" / Int32ul,
        "DiffieHellmanGroup" / Int32ul,
        "LifetimeMinutes" / Int32ul,
        "QMLimit" / Int32ul,
        "Role" / Int32ul,
        "Impersonation" / Int32ul,
        "MMFilterId" / Int64ul,
        "SaLuid" / Int64ul,
        "ProviderContextKey" / Guid,
        "VirtualIfTunnelId" / Int64ul,
        "ICookie" / Int64ul,
        "RCookie" / Int64ul
    )


@declare(guid=guid("0c478c5b-0351-41b1-8c58-4a6737da32e3"), event_id=1044, version=0)
class Microsoft_Windows_WFP_1044_0(Etw):
    pattern = Struct(
        "Timestamp" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "ScopeId" / Int32ul,
        "AppId" / WString,
        "UserSID" / Sid,
        "SPI" / Int32ul
    )

