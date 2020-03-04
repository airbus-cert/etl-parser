# -*- coding: utf-8 -*-
"""
Microsoft-Windows-NCSI
GUID : 314de49f-ce63-4779-ba2b-d616f6963a88
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=2001, version=0)
class Microsoft_Windows_NCSI_2001_0(Etw):
    pattern = Struct(
        "CorpCheckDisabledReason" / Int8ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=2003, version=0)
class Microsoft_Windows_NCSI_2003_0(Etw):
    pattern = Struct(
        "CorpCheckDisabledReason" / Int8ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4001, version=0)
class Microsoft_Windows_NCSI_4001_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "CurrentOrNextState" / Int8ul,
        "IfLuid" / Int64ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4002, version=0)
class Microsoft_Windows_NCSI_4002_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "CurrentOrNextState" / Int8ul,
        "IfLuid" / Int64ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4003, version=0)
class Microsoft_Windows_NCSI_4003_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "CurrentOrNextState" / Int8ul,
        "IfLuid" / Int64ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4004, version=0)
class Microsoft_Windows_NCSI_4004_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "CurrentOrNextState" / Int8ul,
        "IfLuid" / Int64ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4005, version=0)
class Microsoft_Windows_NCSI_4005_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "CurrentOrNextState" / Int8ul,
        "IfLuid" / Int64ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4006, version=0)
class Microsoft_Windows_NCSI_4006_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "CurrentOrNextState" / Int8ul,
        "IfLuid" / Int64ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4007, version=0)
class Microsoft_Windows_NCSI_4007_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "CurrentOrNextState" / Int8ul,
        "IfLuid" / Int64ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4008, version=0)
class Microsoft_Windows_NCSI_4008_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "CurrentOrNextState" / Int8ul,
        "IfLuid" / Int64ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4009, version=0)
class Microsoft_Windows_NCSI_4009_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "CurrentOrNextState" / Int8ul,
        "IfLuid" / Int64ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4010, version=0)
class Microsoft_Windows_NCSI_4010_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "CurrentOrNextState" / Int8ul,
        "IfLuid" / Int64ul,
        "CorporateLocation" / Int8ul,
        "CorporateLocationMetadata" / Int32ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4012, version=0)
class Microsoft_Windows_NCSI_4012_0(Etw):
    pattern = Struct(
        "IfLuid" / Int64ul,
        "InterfaceGuid" / Guid,
        "ProbeHost" / WString,
        "ProbePath" / WString,
        "ErrorCode" / Int32ul,
        "ErrorString" / WString,
        "RetryInterval" / Int32ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4013, version=0)
class Microsoft_Windows_NCSI_4013_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ForceWeb" / Int8ul,
        "UseProxyCache" / Int8ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4014, version=0)
class Microsoft_Windows_NCSI_4014_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "Succeeded" / Int8ul,
        "UsedDnsProbe" / Int8ul,
        "UsedProxy" / Int8ul,
        "ContentComparison" / Int8ul,
        "WebCompleted" / Int8ul,
        "WebRedirected" / Int8ul,
        "LocalErrorOccured" / Int8ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4015, version=0)
class Microsoft_Windows_NCSI_4015_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "Family" / Int32ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4016, version=0)
class Microsoft_Windows_NCSI_4016_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "Family" / Int32ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4017, version=0)
class Microsoft_Windows_NCSI_4017_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "Family" / Int32ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4018, version=0)
class Microsoft_Windows_NCSI_4018_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "Family" / Int32ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4019, version=0)
class Microsoft_Windows_NCSI_4019_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4020, version=0)
class Microsoft_Windows_NCSI_4020_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "Succeeded" / Int8ul,
        "LocalErrorOccured" / Int8ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4021, version=0)
class Microsoft_Windows_NCSI_4021_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4022, version=0)
class Microsoft_Windows_NCSI_4022_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4023, version=0)
class Microsoft_Windows_NCSI_4023_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4024, version=0)
class Microsoft_Windows_NCSI_4024_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4026, version=0)
class Microsoft_Windows_NCSI_4026_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Source" / Int8ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4027, version=0)
class Microsoft_Windows_NCSI_4027_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "Family" / Int32ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4029, version=0)
class Microsoft_Windows_NCSI_4029_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "IfLuid" / Int64ul,
        "Family" / Int32ul,
        "SuspectStateReason" / Int8ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4030, version=0)
class Microsoft_Windows_NCSI_4030_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "IfLuid" / Int64ul,
        "Family" / Int32ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4031, version=0)
class Microsoft_Windows_NCSI_4031_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "IfLuid" / Int64ul,
        "Family" / Int32ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4032, version=0)
class Microsoft_Windows_NCSI_4032_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "IfLuid" / Int64ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4033, version=0)
class Microsoft_Windows_NCSI_4033_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "IfLuid" / Int64ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4034, version=0)
class Microsoft_Windows_NCSI_4034_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "IfLuid" / Int64ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4035, version=0)
class Microsoft_Windows_NCSI_4035_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4036, version=0)
class Microsoft_Windows_NCSI_4036_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4037, version=0)
class Microsoft_Windows_NCSI_4037_0(Etw):
    pattern = Struct(
        "IfLuid" / Int64ul,
        "Family" / Int32ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4038, version=0)
class Microsoft_Windows_NCSI_4038_0(Etw):
    pattern = Struct(
        "IfLuid" / Int64ul,
        "Family" / Int32ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4039, version=0)
class Microsoft_Windows_NCSI_4039_0(Etw):
    pattern = Struct(
        "IfLuid" / Int64ul,
        "Family" / Int32ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4040, version=0)
class Microsoft_Windows_NCSI_4040_0(Etw):
    pattern = Struct(
        "ConnectedInterfaceGuid" / Guid,
        "IfLuid" / Int64ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4041, version=0)
class Microsoft_Windows_NCSI_4041_0(Etw):
    pattern = Struct(
        "DisconnectedInterfaceGuid" / Guid,
        "IfLuid" / Int64ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4042, version=0)
class Microsoft_Windows_NCSI_4042_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "IfLuid" / Int64ul,
        "Family" / Int32ul,
        "Capability" / Int32ul,
        "CapabilityChangeReason" / Int32ul,
        "PreviousCapability" / Int32ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4043, version=0)
class Microsoft_Windows_NCSI_4043_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "IfLuid" / Int64ul,
        "Family" / Int32ul,
        "ProxiedCapability" / Int32ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4044, version=0)
class Microsoft_Windows_NCSI_4044_0(Etw):
    pattern = Struct(
        "ShouldPassivePollRun" / Int8ul,
        "WasPassivePollRunning" / Int8ul,
        "IsPassivePollAllowed" / Int8ul,
        "ClientPresent" / Int8ul,
        "UserPresent" / Int8ul,
        "NetworkQuietMode" / Int8ul,
        "DeadUserPollCount" / Int32ul,
        "DeadNetPollCountV4" / Int32ul,
        "DeadNetPollCountV6" / Int32ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4045, version=0)
class Microsoft_Windows_NCSI_4045_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "IfLuid" / Int64ul,
        "Family" / Int32ul,
        "NetReady" / Int8ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4046, version=0)
class Microsoft_Windows_NCSI_4046_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "IfLuid" / Int64ul,
        "Family" / Int32ul,
        "HasCorporateConnectivity" / Int8ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4047, version=0)
class Microsoft_Windows_NCSI_4047_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "IfLuid" / Int64ul,
        "Family" / Int32ul,
        "IpAddressLength" / Int32ul,
        "IpAddress" / Bytes(lambda this: this.IpAddressLength),
        "MacAddressLength" / Int32ul,
        "MacAddress" / Bytes(lambda this: this.MacAddressLength),
        "KnownProxyless" / Int8ul,
        "KnownHotspot" / Int8ul,
        "KnownOppInternet" / Int8ul,
        "KnownProxiedOppInternet" / Int8ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4048, version=0)
class Microsoft_Windows_NCSI_4048_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "IfLuid" / Int64ul,
        "Family" / Int32ul,
        "HasNextHopToInternet" / Int8ul,
        "NextHopAddressLength" / Int32ul,
        "NextHopAddress" / Bytes(lambda this: this.NextHopAddressLength)
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4049, version=0)
class Microsoft_Windows_NCSI_4049_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "IfLuid" / Int64ul,
        "Family" / Int32ul,
        "HasPreferredAddress" / Int8ul,
        "AddressSuffixOrigins" / Int32ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4050, version=0)
class Microsoft_Windows_NCSI_4050_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "IfLuid" / Int64ul,
        "Family" / Int32ul,
        "HasPreferredGlobalAddress" / Int8ul,
        "AddressSuffixOrigins" / Int32ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4051, version=0)
class Microsoft_Windows_NCSI_4051_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "IfLuid" / Int64ul,
        "Family" / Int32ul,
        "ActiveProbeResultCode" / Int32ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4052, version=0)
class Microsoft_Windows_NCSI_4052_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "IfLuid" / Int64ul,
        "HasPreferredGlobalAddressIPv4" / Int8ul,
        "HasPreferredGlobalAddressIPv6" / Int8ul,
        "InternetCapabilityIPv4" / Int8ul,
        "InternetCapabilityIPv6" / Int8ul,
        "InternetTestIPv4" / Int8ul,
        "InternetTestIPv6" / Int8ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4053, version=0)
class Microsoft_Windows_NCSI_4053_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "Family" / Int32ul
    )


@declare(guid=guid("314de49f-ce63-4779-ba2b-d616f6963a88"), event_id=4054, version=0)
class Microsoft_Windows_NCSI_4054_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "Family" / Int32ul
    )

