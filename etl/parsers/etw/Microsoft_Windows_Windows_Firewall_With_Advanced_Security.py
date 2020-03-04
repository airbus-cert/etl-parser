# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Windows Firewall With Advanced Security
GUID : d1bc9aff-2abf-4d71-9146-ecb2a986eb85
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2000, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2000_0(Etw):
    pattern = Struct(
        "CurrentProfile" / Int32ul,
        "SAIdleTime" / Int32ul,
        "PresharedKeyEncoding" / Int32ul,
        "IPSecExempt" / Int32ul,
        "CrlCheck" / Int32ul,
        "IPSecThroughNAT" / Int32ul,
        "PolicyVersionSupported" / Int32ul,
        "PolicyVersion" / Int32ul,
        "BinaryVersionSupported" / Int32ul,
        "DisableStatefulFTP" / Int32ul,
        "GroupPolicyApplied" / Int32ul,
        "RemoteMachineAuthorizationList" / WString,
        "RemoteUserAuthorizationList" / WString
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2001, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2001_0(Etw):
    pattern = Struct(
        "Profile" / Int32ul,
        "OpMode" / Int32ul,
        "DisableStealthMode" / Int32ul,
        "BlockAllInbound" / Int32ul,
        "DisableUnicastResponseToMultiCastBroadCast" / Int32ul,
        "LogDroppedPackets" / Int32ul,
        "LogSuccessfulConnections" / Int32ul,
        "LogIgnoredRules" / Int32ul,
        "DisableInboundNotifications" / Int32ul,
        "AllowUserPrefMergeForApps" / Int32ul,
        "AllowUserPrefMergeForGlobalPorts" / Int32ul,
        "AllowLocalPolicyMerge" / Int32ul,
        "AllowIPSecPolicyMerge" / Int32ul,
        "DefaultOutboundAction" / Int32ul,
        "DefaultInboundAction" / Int32ul,
        "RemoteAdministrationEnabled" / Int32ul,
        "MaxLogFileSize" / Int32ul,
        "LogFilePath" / WString,
        "DisabledInterfacesSize" / Int32ul,
        "DisabledInterfaces" / Bytes(lambda this: this.DisabledInterfacesSize),
        "DisableStealthModeIPsecSecuredPacketExemption" / Int32ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2002, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2002_0(Etw):
    pattern = Struct(
        "SettingType" / Int32ul,
        "SettingValueSize" / Int32ul,
        "SettingValue" / Bytes(lambda this: this.SettingValueSize),
        "SettingValueDisplay" / WString,
        "Origin" / Int32ul,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2003, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2003_0(Etw):
    pattern = Struct(
        "Profiles" / Int32ul,
        "SettingType" / Int32ul,
        "SettingValueSize" / Int32ul,
        "SettingValue" / Bytes(lambda this: this.SettingValueSize),
        "SettingValueString" / WString,
        "Origin" / Int32ul,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2004, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2004_0(Etw):
    pattern = Struct(
        "RuleId" / WString,
        "RuleName" / WString,
        "Origin" / Int32ul,
        "ApplicationPath" / WString,
        "ServiceName" / WString,
        "Direction" / Int32ul,
        "Protocol" / Int16ul,
        "LocalPorts" / WString,
        "RemotePorts" / WString,
        "Action" / Int32ul,
        "Profiles" / Int32ul,
        "LocalAddresses" / WString,
        "RemoteAddresses" / WString,
        "RemoteMachineAuthorizationList" / WString,
        "RemoteUserAuthorizationList" / WString,
        "EmbeddedContext" / WString,
        "Flags" / Int16ul,
        "Active" / Int16ul,
        "EdgeTraversal" / Int16ul,
        "LooseSourceMapped" / Int16ul,
        "SecurityOptions" / Int16ul,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString,
        "SchemaVersion" / Int16ul,
        "RuleStatus" / Int32ul,
        "LocalOnlyMapped" / Int16ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2005, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2005_0(Etw):
    pattern = Struct(
        "RuleId" / WString,
        "RuleName" / WString,
        "Origin" / Int32ul,
        "ApplicationPath" / WString,
        "ServiceName" / WString,
        "Direction" / Int32ul,
        "Protocol" / Int16ul,
        "LocalPorts" / WString,
        "RemotePorts" / WString,
        "Action" / Int32ul,
        "Profiles" / Int32ul,
        "LocalAddresses" / WString,
        "RemoteAddresses" / WString,
        "RemoteMachineAuthorizationList" / WString,
        "RemoteUserAuthorizationList" / WString,
        "EmbeddedContext" / WString,
        "Flags" / Int16ul,
        "Active" / Int16ul,
        "EdgeTraversal" / Int16ul,
        "LooseSourceMapped" / Int16ul,
        "SecurityOptions" / Int16ul,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString,
        "SchemaVersion" / Int16ul,
        "RuleStatus" / Int32ul,
        "LocalOnlyMapped" / Int16ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2006, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2006_0(Etw):
    pattern = Struct(
        "RuleId" / WString,
        "RuleName" / WString,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2007, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2007_0(Etw):
    pattern = Struct(
        "RuleId" / WString,
        "RuleName" / WString,
        "Origin" / Int32ul,
        "ApplicationPath" / WString,
        "ServiceName" / WString,
        "Direction" / Int32ul,
        "Protocol" / Int16ul,
        "LocalPorts" / WString,
        "RemotePorts" / WString,
        "Action" / Int32ul,
        "Profiles" / Int32ul,
        "LocalAddresses" / WString,
        "RemoteAddresses" / WString,
        "RemoteMachineAuthorizationList" / WString,
        "RemoteUserAuthorizationList" / WString,
        "EmbeddedContext" / WString,
        "Flags" / Int16ul,
        "Active" / Int16ul,
        "EdgeTraversal" / Int16ul,
        "LooseSourceMapped" / Int16ul,
        "SecurityOptions" / Int16ul,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString,
        "SchemaVersion" / Int16ul,
        "RuleStatus" / Int32ul,
        "LocalOnlyMapped" / Int16ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2009, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2009_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2010, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2010_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceName" / WString,
        "OldProfile" / Int32ul,
        "NewProfile" / Int32ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2011, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2011_0(Etw):
    pattern = Struct(
        "ReasonCode" / Int32ul,
        "ApplicationPath" / WString,
        "IPVersion" / Int8ul,
        "Protocol" / Int16ul,
        "Port" / Int16ul,
        "ProcessId" / Int32ul,
        "ModifyingUser" / Sid
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2012, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2012_0(Etw):
    pattern = Struct(
        "RuleId" / WString,
        "RuleName" / WString,
        "Origin" / Int32ul,
        "Active" / Int16ul,
        "Protocol" / Int16ul,
        "Endpoint1Ports" / WString,
        "Endpoint2Ports" / WString,
        "LocalTunnelEndpointV4" / Int32ul,
        "RemoteTunnelEndpointV4" / Int32ul,
        "Phase1AuthSetId" / WString,
        "Phase2AuthSetId" / WString,
        "Phase2CryptoSetId" / WString,
        "Action" / Int32ul,
        "Profiles" / Int32ul,
        "Endpoint1" / WString,
        "Endpoint2" / WString,
        "MMParentRuleId" / WString,
        "EmbeddedContext" / WString,
        "Flags" / Int16ul,
        "IsDTM" / Int16ul,
        "ApplyAuthZ" / Int16ul,
        "BypassTunnelIfEncrypted" / Int16ul,
        "NoIPSecOnOutbound" / Int16ul,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString,
        "SchemaVersion" / Int16ul,
        "RuleStatus" / Int32ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2013, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2013_0(Etw):
    pattern = Struct(
        "RuleId" / WString,
        "RuleName" / WString,
        "Origin" / Int32ul,
        "Active" / Int16ul,
        "Protocol" / Int16ul,
        "Endpoint1Ports" / WString,
        "Endpoint2Ports" / WString,
        "LocalTunnelEndpointV4" / Int32ul,
        "RemoteTunnelEndpointV4" / Int32ul,
        "Phase1AuthSetId" / WString,
        "Phase2AuthSetId" / WString,
        "Phase2CryptoSetId" / WString,
        "Action" / Int32ul,
        "Profiles" / Int32ul,
        "Endpoint1" / WString,
        "Endpoint2" / WString,
        "MMParentRuleId" / WString,
        "EmbeddedContext" / WString,
        "Flags" / Int16ul,
        "IsDTM" / Int16ul,
        "ApplyAuthZ" / Int16ul,
        "BypassTunnelIfEncrypted" / Int16ul,
        "NoIPSecOnOutbound" / Int16ul,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString,
        "SchemaVersion" / Int16ul,
        "RuleStatus" / Int32ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2014, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2014_0(Etw):
    pattern = Struct(
        "RuleId" / WString,
        "RuleName" / WString,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2015, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2015_0(Etw):
    pattern = Struct(
        "RuleId" / WString,
        "RuleName" / WString,
        "Origin" / Int32ul,
        "Active" / Int16ul,
        "Protocol" / Int16ul,
        "Endpoint1Ports" / WString,
        "Endpoint2Ports" / WString,
        "LocalTunnelEndpointV4" / Int32ul,
        "RemoteTunnelEndpointV4" / Int32ul,
        "Phase1AuthSetId" / WString,
        "Phase2AuthSetId" / WString,
        "Phase2CryptoSetId" / WString,
        "Action" / Int32ul,
        "Profiles" / Int32ul,
        "Endpoint1" / WString,
        "Endpoint2" / WString,
        "MMParentRuleId" / WString,
        "EmbeddedContext" / WString,
        "Flags" / Int16ul,
        "IsDTM" / Int16ul,
        "ApplyAuthZ" / Int16ul,
        "BypassTunnelIfEncrypted" / Int16ul,
        "NoIPSecOnOutbound" / Int16ul,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString,
        "SchemaVersion" / Int16ul,
        "RuleStatus" / Int32ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2016, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2016_0(Etw):
    pattern = Struct(
        "RuleId" / WString,
        "RuleName" / WString,
        "Profiles" / Int32ul,
        "Endpoint1" / WString,
        "Endpoint2" / WString,
        "Phase1AuthSetId" / WString,
        "Phase1CryptoSetId" / WString,
        "Flags" / Int16ul,
        "Active" / Int16ul,
        "EmbeddedContext" / WString,
        "Origin" / Int32ul,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString,
        "SchemaVersion" / Int16ul,
        "RuleStatus" / Int32ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2017, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2017_0(Etw):
    pattern = Struct(
        "RuleId" / WString,
        "RuleName" / WString,
        "Profiles" / Int32ul,
        "Endpoint1" / WString,
        "Endpoint2" / WString,
        "Phase1AuthSetId" / WString,
        "Phase1CryptoSetId" / WString,
        "Flags" / Int16ul,
        "Active" / Int16ul,
        "EmbeddedContext" / WString,
        "Origin" / Int32ul,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString,
        "SchemaVersion" / Int16ul,
        "RuleStatus" / Int32ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2018, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2018_0(Etw):
    pattern = Struct(
        "RuleId" / WString,
        "RuleName" / WString,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2019, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2019_0(Etw):
    pattern = Struct(
        "RuleId" / WString,
        "RuleName" / WString,
        "Profiles" / Int32ul,
        "Endpoint1" / WString,
        "Endpoint2" / WString,
        "Phase1AuthSetId" / WString,
        "Phase1CryptoSetId" / WString,
        "Flags" / Int16ul,
        "Active" / Int16ul,
        "EmbeddedContext" / WString,
        "Origin" / Int32ul,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString,
        "SchemaVersion" / Int16ul,
        "RuleStatus" / Int32ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2020, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2020_0(Etw):
    pattern = Struct(
        "SetId" / WString,
        "SetName" / WString,
        "EmbeddedContext" / WString,
        "Origin" / Int32ul,
        "CryptoSetFlags" / Int32ul,
        "Flags" / Int16ul,
        "NumSuites" / Int32ul,
        "SuitesBinaryLength" / Int32ul,
        "CryptoSuites" / Bytes(lambda this: this.SuitesBinaryLength),
        "TimeOutMinutes" / Int32ul,
        "TimeOutSessions" / Int32ul,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString,
        "SchemaVersion" / Int16ul,
        "RuleStatus" / Int32ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2021, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2021_0(Etw):
    pattern = Struct(
        "SetId" / WString,
        "SetName" / WString,
        "EmbeddedContext" / WString,
        "Origin" / Int32ul,
        "CryptoSetFlags" / Int32ul,
        "Flags" / Int16ul,
        "NumSuites" / Int32ul,
        "SuitesBinaryLength" / Int32ul,
        "CryptoSuites" / Bytes(lambda this: this.SuitesBinaryLength),
        "TimeOutMinutes" / Int32ul,
        "TimeOutSessions" / Int32ul,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString,
        "SchemaVersion" / Int16ul,
        "RuleStatus" / Int32ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2022, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2022_0(Etw):
    pattern = Struct(
        "RuleId" / WString,
        "RuleName" / WString,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2023, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2023_0(Etw):
    pattern = Struct(
        "SetId" / WString,
        "SetName" / WString,
        "EmbeddedContext" / WString,
        "Origin" / Int32ul,
        "CryptoSetFlags" / Int32ul,
        "Flags" / Int16ul,
        "NumSuites" / Int32ul,
        "SuitesBinaryLength" / Int32ul,
        "CryptoSuites" / Bytes(lambda this: this.SuitesBinaryLength),
        "TimeOutMinutes" / Int32ul,
        "TimeOutSessions" / Int32ul,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString,
        "SchemaVersion" / Int16ul,
        "RuleStatus" / Int32ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2024, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2024_0(Etw):
    pattern = Struct(
        "SetId" / WString,
        "SetName" / WString,
        "EmbeddedContext" / WString,
        "Origin" / Int32ul,
        "CryptoSetFlags" / Int32ul,
        "Pfs" / Int32ul,
        "NumSuites" / Int32ul,
        "SuitesBinaryLength" / Int32ul,
        "CryptoSuites" / Bytes(lambda this: this.SuitesBinaryLength),
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString,
        "SchemaVersion" / Int16ul,
        "RuleStatus" / Int32ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2025, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2025_0(Etw):
    pattern = Struct(
        "SetId" / WString,
        "SetName" / WString,
        "EmbeddedContext" / WString,
        "Origin" / Int32ul,
        "CryptoSetFlags" / Int32ul,
        "Pfs" / Int32ul,
        "NumSuites" / Int32ul,
        "SuitesBinaryLength" / Int32ul,
        "CryptoSuites" / Bytes(lambda this: this.SuitesBinaryLength),
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString,
        "SchemaVersion" / Int16ul,
        "RuleStatus" / Int32ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2026, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2026_0(Etw):
    pattern = Struct(
        "RuleId" / WString,
        "RuleName" / WString,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2027, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2027_0(Etw):
    pattern = Struct(
        "SetId" / WString,
        "SetName" / WString,
        "EmbeddedContext" / WString,
        "Origin" / Int32ul,
        "CryptoSetFlags" / Int32ul,
        "Pfs" / Int32ul,
        "NumSuites" / Int32ul,
        "SuitesBinaryLength" / Int32ul,
        "CryptoSuites" / Bytes(lambda this: this.SuitesBinaryLength),
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString,
        "SchemaVersion" / Int16ul,
        "RuleStatus" / Int32ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2028, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2028_0(Etw):
    pattern = Struct(
        "SetId" / WString,
        "SetName" / WString,
        "IPsecPhase" / Int32ul,
        "EmbeddedContext" / WString,
        "Origin" / Int32ul,
        "AuthSetFlags" / Int32ul,
        "NumSuites" / Int32ul,
        "SuitesBinaryLength" / Int32ul,
        "AuthenticationSuites" / Bytes(lambda this: this.SuitesBinaryLength),
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString,
        "SchemaVersion" / Int16ul,
        "RuleStatus" / Int32ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2029, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2029_0(Etw):
    pattern = Struct(
        "SetId" / WString,
        "SetName" / WString,
        "IPsecPhase" / Int32ul,
        "EmbeddedContext" / WString,
        "Origin" / Int32ul,
        "AuthSetFlags" / Int32ul,
        "NumSuites" / Int32ul,
        "SuitesBinaryLength" / Int32ul,
        "AuthenticationSuites" / Bytes(lambda this: this.SuitesBinaryLength),
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString,
        "SchemaVersion" / Int16ul,
        "RuleStatus" / Int32ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2030, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2030_0(Etw):
    pattern = Struct(
        "RuleId" / WString,
        "RuleName" / WString,
        "IPsecPhase" / Int32ul,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2031, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2031_0(Etw):
    pattern = Struct(
        "SetId" / WString,
        "SetName" / WString,
        "IPsecPhase" / Int32ul,
        "EmbeddedContext" / WString,
        "Origin" / Int32ul,
        "AuthSetFlags" / Int32ul,
        "NumSuites" / Int32ul,
        "SuitesBinaryLength" / Int32ul,
        "AuthenticationSuites" / Bytes(lambda this: this.SuitesBinaryLength),
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString,
        "SchemaVersion" / Int16ul,
        "RuleStatus" / Int32ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2032, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2032_0(Etw):
    pattern = Struct(
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2033, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2033_0(Etw):
    pattern = Struct(
        "StoreType" / Int32ul,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2034, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2034_0(Etw):
    pattern = Struct(
        "StoreType" / Int32ul,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2035, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2035_0(Etw):
    pattern = Struct(
        "StoreType" / Int32ul,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2036, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2036_0(Etw):
    pattern = Struct(
        "IPsecPhase" / Int32ul,
        "StoreType" / Int32ul,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2037, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2037_0(Etw):
    pattern = Struct(
        "IPsecPhase" / Int32ul,
        "StoreType" / Int32ul,
        "ModifyingUser" / Sid,
        "ModifyingApplication" / WString
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2038, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2038_0(Etw):
    pattern = Struct(
        "ID" / WString,
        "Name" / WString,
        "Reason" / WString,
        "RuleStatus" / Int32ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2039, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2039_0(Etw):
    pattern = Struct(
        "ChangeType" / Int32ul,
        "AllProxies" / WString,
        "AllDomainProxies" / WString,
        "GPConfiguredDomainProxies" / WString,
        "GPConfiguredLocalProxies" / WString,
        "AllDANat64Proxies" / WString,
        "GPIsAuthoritative" / Int32ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2040, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2040_0(Etw):
    pattern = Struct(
        "ChangeType" / Int32ul,
        "AllDomainProxies" / WString,
        "GPConfiguredDomainSubnets" / WString,
        "AllDANat64DomainSubnets" / WString,
        "GPIsAuthoritative" / Int32ul
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2041, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2041_0(Etw):
    pattern = Struct(
        "ChangeType" / Int32ul,
        "Capability" / Int32ul,
        "Profile" / Int32ul,
        "IPRangeDefinition" / WString
    )


@declare(guid=guid("d1bc9aff-2abf-4d71-9146-ecb2a986eb85"), event_id=2042, version=0)
class Microsoft_Windows_Windows_Firewall_With_Advanced_Security_2042_0(Etw):
    pattern = Struct(
        "SettingType" / Int32ul,
        "ErrorCode" / Int32sl
    )

