# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Security-Auditing
GUID : 54849625-5478-4994-a5ba-3e3b0328c30d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4610, version=0)
class Microsoft_Windows_Security_Auditing_4610_0(Etw):
    pattern = Struct(
        "AuthenticationPackageName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4611, version=0)
class Microsoft_Windows_Security_Auditing_4611_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "LogonProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4612, version=0)
class Microsoft_Windows_Security_Auditing_4612_0(Etw):
    pattern = Struct(
        "AuditsDiscarded" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4614, version=0)
class Microsoft_Windows_Security_Auditing_4614_0(Etw):
    pattern = Struct(
        "NotificationPackageName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4615, version=0)
class Microsoft_Windows_Security_Auditing_4615_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "InvalidCallName" / WString,
        "ServerPortName" / WString,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4616, version=0)
class Microsoft_Windows_Security_Auditing_4616_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PreviousDate" / WString,
        "PreviousTime" / WString,
        "NewDate" / WString,
        "NewTime" / WString,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4616, version=1)
class Microsoft_Windows_Security_Auditing_4616_1(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PreviousTime" / Int64ul,
        "NewTime" / Int64ul,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4618, version=0)
class Microsoft_Windows_Security_Auditing_4618_0(Etw):
    pattern = Struct(
        "EventId" / Int32ul,
        "ComputerName" / WString,
        "TargetUserSid" / Sid,
        "TargetUserName" / WString,
        "TargetUserDomain" / WString,
        "TargetLogonId" / Int64ul,
        "EventCount" / Int32ul,
        "Duration" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4621, version=0)
class Microsoft_Windows_Security_Auditing_4621_0(Etw):
    pattern = Struct(
        "CrashOnAuditFailValue" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4622, version=0)
class Microsoft_Windows_Security_Auditing_4622_0(Etw):
    pattern = Struct(
        "SecurityPackageName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4624, version=0)
class Microsoft_Windows_Security_Auditing_4624_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TargetUserSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetLogonId" / Int64ul,
        "LogonType" / Int32ul,
        "LogonProcessName" / WString,
        "AuthenticationPackageName" / WString,
        "WorkstationName" / WString,
        "LogonGuid" / Guid,
        "TransmittedServices" / WString,
        "LmPackageName" / WString,
        "KeyLength" / Int32ul,
        "ProcessId" / Int64ul,
        "ProcessName" / WString,
        "IpAddress" / WString,
        "IpPort" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4624, version=1)
class Microsoft_Windows_Security_Auditing_4624_1(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TargetUserSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetLogonId" / Int64ul,
        "LogonType" / Int32ul,
        "LogonProcessName" / WString,
        "AuthenticationPackageName" / WString,
        "WorkstationName" / WString,
        "LogonGuid" / Guid,
        "TransmittedServices" / WString,
        "LmPackageName" / WString,
        "KeyLength" / Int32ul,
        "ProcessId" / Int64ul,
        "ProcessName" / WString,
        "IpAddress" / WString,
        "IpPort" / WString,
        "ImpersonationLevel" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4624, version=2)
class Microsoft_Windows_Security_Auditing_4624_2(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TargetUserSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetLogonId" / Int64ul,
        "LogonType" / Int32ul,
        "LogonProcessName" / WString,
        "AuthenticationPackageName" / WString,
        "WorkstationName" / WString,
        "LogonGuid" / Guid,
        "TransmittedServices" / WString,
        "LmPackageName" / WString,
        "KeyLength" / Int32ul,
        "ProcessId" / Int64ul,
        "ProcessName" / WString,
        "IpAddress" / WString,
        "IpPort" / WString,
        "ImpersonationLevel" / WString,
        "RestrictedAdminMode" / WString,
        "TargetOutboundUserName" / WString,
        "TargetOutboundDomainName" / WString,
        "VirtualAccount" / WString,
        "TargetLinkedLogonId" / Int64ul,
        "ElevatedToken" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4625, version=0)
class Microsoft_Windows_Security_Auditing_4625_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TargetUserSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "Status" / Int32ul,
        "FailureReason" / WString,
        "SubStatus" / Int32ul,
        "LogonType" / Int32ul,
        "LogonProcessName" / WString,
        "AuthenticationPackageName" / WString,
        "WorkstationName" / WString,
        "TransmittedServices" / WString,
        "LmPackageName" / WString,
        "KeyLength" / Int32ul,
        "ProcessId" / Int64ul,
        "ProcessName" / WString,
        "IpAddress" / WString,
        "IpPort" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4626, version=0)
class Microsoft_Windows_Security_Auditing_4626_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TargetUserSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetLogonId" / Int64ul,
        "LogonType" / Int32ul,
        "EventIdx" / Int32ul,
        "EventCountTotal" / Int32ul,
        "UserClaims" / WString,
        "DeviceClaims" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4627, version=0)
class Microsoft_Windows_Security_Auditing_4627_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TargetUserSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetLogonId" / Int64ul,
        "LogonType" / Int32ul,
        "EventIdx" / Int32ul,
        "EventCountTotal" / Int32ul,
        "GroupMembership" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4634, version=0)
class Microsoft_Windows_Security_Auditing_4634_0(Etw):
    pattern = Struct(
        "TargetUserSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetLogonId" / Int64ul,
        "LogonType" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4646, version=0)
class Microsoft_Windows_Security_Auditing_4646_0(Etw):
    pattern = Struct(
        "notification" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4647, version=0)
class Microsoft_Windows_Security_Auditing_4647_0(Etw):
    pattern = Struct(
        "TargetUserSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4648, version=0)
class Microsoft_Windows_Security_Auditing_4648_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "LogonGuid" / Guid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetLogonGuid" / Guid,
        "TargetServerName" / WString,
        "TargetInfo" / WString,
        "ProcessId" / Int64ul,
        "ProcessName" / WString,
        "IpAddress" / WString,
        "IpPort" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4649, version=0)
class Microsoft_Windows_Security_Auditing_4649_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "RequestType" / WString,
        "LogonProcessName" / WString,
        "AuthenticationPackage" / WString,
        "WorkstationName" / WString,
        "TransmittedServices" / WString,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4650, version=0)
class Microsoft_Windows_Security_Auditing_4650_0(Etw):
    pattern = Struct(
        "LocalMMPrincipalName" / WString,
        "RemoteMMPrincipalName" / WString,
        "LocalAddress" / WString,
        "LocalKeyModPort" / Int32ul,
        "RemoteAddress" / WString,
        "RemoteKeyModPort" / Int32ul,
        "KeyModName" / WString,
        "MMAuthMethod" / WString,
        "MMCipherAlg" / WString,
        "MMIntegrityAlg" / WString,
        "DHGroup" / WString,
        "MMLifetime" / Int32ul,
        "QMLimit" / Int32ul,
        "Role" / WString,
        "MMImpersonationState" / WString,
        "MMFilterID" / Int64ul,
        "MMSAID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4651, version=0)
class Microsoft_Windows_Security_Auditing_4651_0(Etw):
    pattern = Struct(
        "LocalMMPrincipalName" / WString,
        "LocalMMCertHash" / WString,
        "LocalMMIssuingCA" / WString,
        "LocalMMRootCA" / WString,
        "RemoteMMPrincipalName" / WString,
        "RemoteMMCertHash" / WString,
        "RemoteMMIssuingCA" / WString,
        "RemoteMMRootCA" / WString,
        "LocalAddress" / WString,
        "LocalKeyModPort" / Int32ul,
        "RemoteAddress" / WString,
        "RemoteKeyModPort" / Int32ul,
        "KeyModName" / WString,
        "MMAuthMethod" / WString,
        "MMCipherAlg" / WString,
        "MMIntegrityAlg" / WString,
        "DHGroup" / WString,
        "MMLifetime" / Int32ul,
        "QMLimit" / Int32ul,
        "Role" / WString,
        "MMImpersonationState" / WString,
        "MMFilterID" / Int64ul,
        "MMSAID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4652, version=0)
class Microsoft_Windows_Security_Auditing_4652_0(Etw):
    pattern = Struct(
        "LocalMMPrincipalName" / WString,
        "LocalMMCertHash" / WString,
        "LocalMMIssuingCA" / WString,
        "LocalMMRootCA" / WString,
        "RemoteMMPrincipalName" / WString,
        "RemoteMMCertHash" / WString,
        "RemoteMMIssuingCA" / WString,
        "RemoteMMRootCA" / WString,
        "LocalAddress" / WString,
        "LocalKeyModPort" / Int32ul,
        "RemoteAddress" / WString,
        "RemoteKeyModPort" / Int32ul,
        "KeyModName" / WString,
        "FailurePoint" / WString,
        "FailureReason" / WString,
        "MMAuthMethod" / WString,
        "State" / WString,
        "Role" / WString,
        "MMImpersonationState" / WString,
        "MMFilterID" / Int64ul,
        "InitiatorCookie" / WString,
        "ResponderCookie" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4653, version=0)
class Microsoft_Windows_Security_Auditing_4653_0(Etw):
    pattern = Struct(
        "LocalMMPrincipalName" / WString,
        "RemoteMMPrincipalName" / WString,
        "LocalAddress" / WString,
        "LocalKeyModPort" / Int32ul,
        "RemoteAddress" / WString,
        "RemoteKeyModPort" / Int32ul,
        "KeyModName" / WString,
        "FailurePoint" / WString,
        "FailureReason" / WString,
        "MMAuthMethod" / WString,
        "State" / WString,
        "Role" / WString,
        "MMImpersonationState" / WString,
        "MMFilterID" / Int64ul,
        "InitiatorCookie" / WString,
        "ResponderCookie" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4654, version=0)
class Microsoft_Windows_Security_Auditing_4654_0(Etw):
    pattern = Struct(
        "LocalAddress" / WString,
        "LocalAddressMask" / WString,
        "LocalPort" / Int32ul,
        "LocalTunnelEndpoint" / WString,
        "RemoteAddress" / WString,
        "RemoteAddressMask" / WString,
        "RemotePort" / Int32ul,
        "RemoteTunnelEndpoint" / WString,
        "Protocol" / Int32ul,
        "RemotePrivateAddress" / WString,
        "KeyModName" / WString,
        "FailurePoint" / WString,
        "FailureReason" / WString,
        "Mode" / WString,
        "State" / WString,
        "Role" / WString,
        "MessageID" / Int32ul,
        "QMFilterID" / Int64ul,
        "MMSAID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4654, version=1)
class Microsoft_Windows_Security_Auditing_4654_1(Etw):
    pattern = Struct(
        "LocalAddress" / WString,
        "LocalAddressMask" / WString,
        "LocalPort" / Int32ul,
        "LocalTunnelEndpoint" / WString,
        "RemoteAddress" / WString,
        "RemoteAddressMask" / WString,
        "RemotePort" / Int32ul,
        "RemoteTunnelEndpoint" / WString,
        "Protocol" / Int32ul,
        "RemotePrivateAddress" / WString,
        "KeyModName" / WString,
        "FailurePoint" / WString,
        "FailureReason" / WString,
        "Mode" / WString,
        "State" / WString,
        "Role" / WString,
        "MessageID" / Int32ul,
        "QMFilterID" / Int64ul,
        "MMSAID" / Int64ul,
        "TunnelId" / Int64ul,
        "TrafficSelectorId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4655, version=0)
class Microsoft_Windows_Security_Auditing_4655_0(Etw):
    pattern = Struct(
        "LocalAddress" / WString,
        "RemoteAddress" / WString,
        "KeyModName" / WString,
        "MMSAID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4656, version=0)
class Microsoft_Windows_Security_Auditing_4656_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectServer" / WString,
        "ObjectType" / WString,
        "ObjectName" / WString,
        "HandleId" / Int64ul,
        "TransactionId" / Guid,
        "AccessList" / WString,
        "AccessMask" / Int32ul,
        "PrivilegeList" / WString,
        "RestrictedSidCount" / Int32ul,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4656, version=1)
class Microsoft_Windows_Security_Auditing_4656_1(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectServer" / WString,
        "ObjectType" / WString,
        "ObjectName" / WString,
        "HandleId" / Int64ul,
        "TransactionId" / Guid,
        "AccessList" / WString,
        "AccessReason" / WString,
        "AccessMask" / Int32ul,
        "PrivilegeList" / WString,
        "RestrictedSidCount" / Int32ul,
        "ProcessId" / Int64ul,
        "ProcessName" / WString,
        "ResourceAttributes" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4657, version=0)
class Microsoft_Windows_Security_Auditing_4657_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectName" / WString,
        "ObjectValueName" / WString,
        "HandleId" / Int64ul,
        "OperationType" / WString,
        "OldValueType" / WString,
        "OldValue" / WString,
        "NewValueType" / WString,
        "NewValue" / WString,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4658, version=0)
class Microsoft_Windows_Security_Auditing_4658_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectServer" / WString,
        "HandleId" / Int64ul,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4659, version=0)
class Microsoft_Windows_Security_Auditing_4659_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectServer" / WString,
        "ObjectType" / WString,
        "ObjectName" / WString,
        "HandleId" / Int64ul,
        "TransactionId" / Guid,
        "AccessList" / WString,
        "AccessMask" / Int32ul,
        "PrivilegeList" / WString,
        "ProcessId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4660, version=0)
class Microsoft_Windows_Security_Auditing_4660_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectServer" / WString,
        "HandleId" / Int64ul,
        "ProcessId" / Int64ul,
        "ProcessName" / WString,
        "TransactionId" / Guid
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4661, version=0)
class Microsoft_Windows_Security_Auditing_4661_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectServer" / WString,
        "ObjectType" / WString,
        "ObjectName" / WString,
        "HandleId" / Int64ul,
        "TransactionId" / Guid,
        "AccessList" / WString,
        "AccessMask" / Int32ul,
        "PrivilegeList" / WString,
        "Properties" / WString,
        "RestrictedSidCount" / Int32ul,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4661, version=1)
class Microsoft_Windows_Security_Auditing_4661_1(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectServer" / WString,
        "ObjectType" / WString,
        "ObjectName" / WString,
        "HandleId" / Int64ul,
        "TransactionId" / Guid,
        "AccessList" / WString,
        "AccessReason" / WString,
        "AccessMask" / Int32ul,
        "PrivilegeList" / WString,
        "Properties" / WString,
        "RestrictedSidCount" / Int32ul,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4662, version=0)
class Microsoft_Windows_Security_Auditing_4662_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectServer" / WString,
        "ObjectType" / WString,
        "ObjectName" / WString,
        "OperationType" / WString,
        "HandleId" / Int64ul,
        "AccessList" / WString,
        "AccessMask" / Int32ul,
        "Properties" / WString,
        "AdditionalInfo" / WString,
        "AdditionalInfo2" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4663, version=0)
class Microsoft_Windows_Security_Auditing_4663_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectServer" / WString,
        "ObjectType" / WString,
        "ObjectName" / WString,
        "HandleId" / Int64ul,
        "AccessList" / WString,
        "AccessMask" / Int32ul,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4663, version=1)
class Microsoft_Windows_Security_Auditing_4663_1(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectServer" / WString,
        "ObjectType" / WString,
        "ObjectName" / WString,
        "HandleId" / Int64ul,
        "AccessList" / WString,
        "AccessMask" / Int32ul,
        "ProcessId" / Int64ul,
        "ProcessName" / WString,
        "ResourceAttributes" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4664, version=0)
class Microsoft_Windows_Security_Auditing_4664_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "FileName" / WString,
        "LinkName" / WString,
        "TransactionId" / Guid
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4665, version=0)
class Microsoft_Windows_Security_Auditing_4665_0(Etw):
    pattern = Struct(
        "AppName" / WString,
        "AppInstance" / Int64ul,
        "ClientName" / WString,
        "ClientDomain" / WString,
        "ClientLogonId" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4666, version=0)
class Microsoft_Windows_Security_Auditing_4666_0(Etw):
    pattern = Struct(
        "AppName" / WString,
        "AppInstance" / Int64ul,
        "ObjectName" / WString,
        "ScopeName" / WString,
        "ClientName" / WString,
        "ClientDomain" / WString,
        "ClientLogonId" / Int64ul,
        "Role" / WString,
        "Group" / WString,
        "OperationName" / WString,
        "OperationId" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4667, version=0)
class Microsoft_Windows_Security_Auditing_4667_0(Etw):
    pattern = Struct(
        "AppName" / WString,
        "AppInstance" / Int64ul,
        "ClientName" / WString,
        "ClientDomain" / WString,
        "ClientLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4668, version=0)
class Microsoft_Windows_Security_Auditing_4668_0(Etw):
    pattern = Struct(
        "AppName" / WString,
        "AppInstance" / Int64ul,
        "ClientName" / WString,
        "ClientDomain" / WString,
        "ClientLogonId" / Int64ul,
        "StoreUrl" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4670, version=0)
class Microsoft_Windows_Security_Auditing_4670_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectServer" / WString,
        "ObjectType" / WString,
        "ObjectName" / WString,
        "HandleId" / Int64ul,
        "OldSd" / WString,
        "NewSd" / WString,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4671, version=0)
class Microsoft_Windows_Security_Auditing_4671_0(Etw):
    pattern = Struct(
        "CallerUserSid" / Sid,
        "CallerUserName" / WString,
        "CallerDomainName" / WString,
        "CallerLogonId" / Int64ul,
        "Ordinal" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4672, version=0)
class Microsoft_Windows_Security_Auditing_4672_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4673, version=0)
class Microsoft_Windows_Security_Auditing_4673_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectServer" / WString,
        "Service" / WString,
        "PrivilegeList" / WString,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4674, version=0)
class Microsoft_Windows_Security_Auditing_4674_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectServer" / WString,
        "ObjectType" / WString,
        "ObjectName" / WString,
        "HandleId" / Int64ul,
        "AccessMask" / WString,
        "PrivilegeList" / WString,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4675, version=0)
class Microsoft_Windows_Security_Auditing_4675_0(Etw):
    pattern = Struct(
        "TargetUserSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TdoDirection" / Int32ul,
        "TdoAttributes" / Int32ul,
        "TdoType" / Int32ul,
        "TdoSid" / Sid,
        "SidList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4688, version=0)
class Microsoft_Windows_Security_Auditing_4688_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "NewProcessId" / Int64ul,
        "NewProcessName" / WString,
        "TokenElevationType" / WString,
        "ProcessId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4688, version=1)
class Microsoft_Windows_Security_Auditing_4688_1(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "NewProcessId" / Int64ul,
        "NewProcessName" / WString,
        "TokenElevationType" / WString,
        "ProcessId" / Int64ul,
        "CommandLine" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4688, version=2)
class Microsoft_Windows_Security_Auditing_4688_2(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "NewProcessId" / Int64ul,
        "NewProcessName" / WString,
        "TokenElevationType" / WString,
        "ProcessId" / Int64ul,
        "CommandLine" / WString,
        "TargetUserSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetLogonId" / Int64ul,
        "ParentProcessName" / WString,
        "MandatoryLabel" / Sid
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4689, version=0)
class Microsoft_Windows_Security_Auditing_4689_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "Status" / Int32ul,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4690, version=0)
class Microsoft_Windows_Security_Auditing_4690_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "SourceHandleId" / Int64ul,
        "SourceProcessId" / Int64ul,
        "TargetHandleId" / Int64ul,
        "TargetProcessId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4691, version=0)
class Microsoft_Windows_Security_Auditing_4691_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectType" / WString,
        "ObjectName" / WString,
        "AccessList" / WString,
        "AccessMask" / Int32ul,
        "ProcessId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4692, version=0)
class Microsoft_Windows_Security_Auditing_4692_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "MasterKeyId" / WString,
        "RecoveryServer" / WString,
        "RecoveryKeyId" / WString,
        "FailureReason" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4693, version=0)
class Microsoft_Windows_Security_Auditing_4693_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "MasterKeyId" / WString,
        "RecoveryReason" / Int32ul,
        "RecoveryServer" / WString,
        "RecoveryKeyId" / WString,
        "FailureId" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4694, version=0)
class Microsoft_Windows_Security_Auditing_4694_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "DataDescription" / WString,
        "MasterKeyId" / WString,
        "ProtectedDataFlags" / Int32ul,
        "CryptoAlgorithms" / WString,
        "FailureReason" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4695, version=0)
class Microsoft_Windows_Security_Auditing_4695_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "DataDescription" / WString,
        "MasterKeyId" / WString,
        "ProtectedDataFlags" / Int32ul,
        "CryptoAlgorithms" / WString,
        "FailureReason" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4696, version=0)
class Microsoft_Windows_Security_Auditing_4696_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TargetUserSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetLogonId" / Int64ul,
        "TargetProcessId" / Int64ul,
        "TargetProcessName" / WString,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4697, version=0)
class Microsoft_Windows_Security_Auditing_4697_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ServiceName" / WString,
        "ServiceFileName" / WString,
        "ServiceType" / Int32ul,
        "ServiceStartType" / Int32ul,
        "ServiceAccount" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4698, version=0)
class Microsoft_Windows_Security_Auditing_4698_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TaskName" / WString,
        "TaskContent" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4699, version=0)
class Microsoft_Windows_Security_Auditing_4699_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TaskName" / WString,
        "TaskContent" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4700, version=0)
class Microsoft_Windows_Security_Auditing_4700_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TaskName" / WString,
        "TaskContent" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4701, version=0)
class Microsoft_Windows_Security_Auditing_4701_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TaskName" / WString,
        "TaskContent" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4702, version=0)
class Microsoft_Windows_Security_Auditing_4702_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TaskName" / WString,
        "TaskContentNew" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4703, version=0)
class Microsoft_Windows_Security_Auditing_4703_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TargetUserSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetLogonId" / Int64ul,
        "ProcessName" / WString,
        "ProcessId" / Int64ul,
        "EnabledPrivilegeList" / WString,
        "DisabledPrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4704, version=0)
class Microsoft_Windows_Security_Auditing_4704_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TargetSid" / Sid,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4705, version=0)
class Microsoft_Windows_Security_Auditing_4705_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TargetSid" / Sid,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4706, version=0)
class Microsoft_Windows_Security_Auditing_4706_0(Etw):
    pattern = Struct(
        "DomainName" / WString,
        "DomainSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TdoType" / Int32ul,
        "TdoDirection" / Int32ul,
        "TdoAttributes" / Int32ul,
        "SidFilteringEnabled" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4707, version=0)
class Microsoft_Windows_Security_Auditing_4707_0(Etw):
    pattern = Struct(
        "DomainName" / WString,
        "DomainSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4709, version=0)
class Microsoft_Windows_Security_Auditing_4709_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4710, version=0)
class Microsoft_Windows_Security_Auditing_4710_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4711, version=0)
class Microsoft_Windows_Security_Auditing_4711_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4712, version=0)
class Microsoft_Windows_Security_Auditing_4712_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4713, version=0)
class Microsoft_Windows_Security_Auditing_4713_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "KerberosPolicyChange" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4714, version=0)
class Microsoft_Windows_Security_Auditing_4714_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "EfsPolicyChange" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4715, version=0)
class Microsoft_Windows_Security_Auditing_4715_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "OldSd" / WString,
        "NewSd" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4716, version=0)
class Microsoft_Windows_Security_Auditing_4716_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "DomainName" / WString,
        "DomainSid" / Sid,
        "TdoType" / Int32ul,
        "TdoDirection" / Int32ul,
        "TdoAttributes" / Int32ul,
        "SidFilteringEnabled" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4717, version=0)
class Microsoft_Windows_Security_Auditing_4717_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TargetSid" / Sid,
        "AccessGranted" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4718, version=0)
class Microsoft_Windows_Security_Auditing_4718_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TargetSid" / Sid,
        "AccessRemoved" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4719, version=0)
class Microsoft_Windows_Security_Auditing_4719_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "CategoryId" / WString,
        "SubcategoryId" / WString,
        "SubcategoryGuid" / Guid,
        "AuditPolicyChanges" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4720, version=0)
class Microsoft_Windows_Security_Auditing_4720_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SamAccountName" / WString,
        "DisplayName" / WString,
        "UserPrincipalName" / WString,
        "HomeDirectory" / WString,
        "HomePath" / WString,
        "ScriptPath" / WString,
        "ProfilePath" / WString,
        "UserWorkstations" / WString,
        "PasswordLastSet" / WString,
        "AccountExpires" / WString,
        "PrimaryGroupId" / WString,
        "AllowedToDelegateTo" / WString,
        "OldUacValue" / WString,
        "NewUacValue" / WString,
        "UserAccountControl" / WString,
        "UserParameters" / WString,
        "SidHistory" / WString,
        "LogonHours" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4722, version=0)
class Microsoft_Windows_Security_Auditing_4722_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4723, version=0)
class Microsoft_Windows_Security_Auditing_4723_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4724, version=0)
class Microsoft_Windows_Security_Auditing_4724_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4725, version=0)
class Microsoft_Windows_Security_Auditing_4725_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4726, version=0)
class Microsoft_Windows_Security_Auditing_4726_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4727, version=0)
class Microsoft_Windows_Security_Auditing_4727_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SamAccountName" / WString,
        "SidHistory" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4728, version=0)
class Microsoft_Windows_Security_Auditing_4728_0(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4728, version=1)
class Microsoft_Windows_Security_Auditing_4728_1(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "MembershipExpirationTime" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4729, version=0)
class Microsoft_Windows_Security_Auditing_4729_0(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4730, version=0)
class Microsoft_Windows_Security_Auditing_4730_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4731, version=0)
class Microsoft_Windows_Security_Auditing_4731_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SamAccountName" / WString,
        "SidHistory" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4732, version=0)
class Microsoft_Windows_Security_Auditing_4732_0(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4732, version=1)
class Microsoft_Windows_Security_Auditing_4732_1(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "MembershipExpirationTime" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4733, version=0)
class Microsoft_Windows_Security_Auditing_4733_0(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4734, version=0)
class Microsoft_Windows_Security_Auditing_4734_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4735, version=0)
class Microsoft_Windows_Security_Auditing_4735_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SamAccountName" / WString,
        "SidHistory" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4737, version=0)
class Microsoft_Windows_Security_Auditing_4737_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SamAccountName" / WString,
        "SidHistory" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4738, version=0)
class Microsoft_Windows_Security_Auditing_4738_0(Etw):
    pattern = Struct(
        "Dummy" / WString,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SamAccountName" / WString,
        "DisplayName" / WString,
        "UserPrincipalName" / WString,
        "HomeDirectory" / WString,
        "HomePath" / WString,
        "ScriptPath" / WString,
        "ProfilePath" / WString,
        "UserWorkstations" / WString,
        "PasswordLastSet" / WString,
        "AccountExpires" / WString,
        "PrimaryGroupId" / WString,
        "AllowedToDelegateTo" / WString,
        "OldUacValue" / WString,
        "NewUacValue" / WString,
        "UserAccountControl" / WString,
        "UserParameters" / WString,
        "SidHistory" / WString,
        "LogonHours" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4739, version=0)
class Microsoft_Windows_Security_Auditing_4739_0(Etw):
    pattern = Struct(
        "DomainPolicyChanged" / WString,
        "DomainName" / WString,
        "DomainSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "MinPasswordAge" / WString,
        "MaxPasswordAge" / WString,
        "ForceLogoff" / WString,
        "LockoutThreshold" / WString,
        "LockoutObservationWindow" / WString,
        "LockoutDuration" / WString,
        "PasswordProperties" / WString,
        "MinPasswordLength" / WString,
        "PasswordHistoryLength" / WString,
        "MachineAccountQuota" / WString,
        "MixedDomainMode" / WString,
        "DomainBehaviorVersion" / WString,
        "OemInformation" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4740, version=0)
class Microsoft_Windows_Security_Auditing_4740_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4741, version=0)
class Microsoft_Windows_Security_Auditing_4741_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SamAccountName" / WString,
        "DisplayName" / WString,
        "UserPrincipalName" / WString,
        "HomeDirectory" / WString,
        "HomePath" / WString,
        "ScriptPath" / WString,
        "ProfilePath" / WString,
        "UserWorkstations" / WString,
        "PasswordLastSet" / WString,
        "AccountExpires" / WString,
        "PrimaryGroupId" / WString,
        "AllowedToDelegateTo" / WString,
        "OldUacValue" / WString,
        "NewUacValue" / WString,
        "UserAccountControl" / WString,
        "UserParameters" / WString,
        "SidHistory" / WString,
        "LogonHours" / WString,
        "DnsHostName" / WString,
        "ServicePrincipalNames" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4742, version=0)
class Microsoft_Windows_Security_Auditing_4742_0(Etw):
    pattern = Struct(
        "ComputerAccountChange" / WString,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SamAccountName" / WString,
        "DisplayName" / WString,
        "UserPrincipalName" / WString,
        "HomeDirectory" / WString,
        "HomePath" / WString,
        "ScriptPath" / WString,
        "ProfilePath" / WString,
        "UserWorkstations" / WString,
        "PasswordLastSet" / WString,
        "AccountExpires" / WString,
        "PrimaryGroupId" / WString,
        "AllowedToDelegateTo" / WString,
        "OldUacValue" / WString,
        "NewUacValue" / WString,
        "UserAccountControl" / WString,
        "UserParameters" / WString,
        "SidHistory" / WString,
        "LogonHours" / WString,
        "DnsHostName" / WString,
        "ServicePrincipalNames" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4743, version=0)
class Microsoft_Windows_Security_Auditing_4743_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4744, version=0)
class Microsoft_Windows_Security_Auditing_4744_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SamAccountName" / WString,
        "SidHistory" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4745, version=0)
class Microsoft_Windows_Security_Auditing_4745_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SamAccountName" / WString,
        "SidHistory" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4746, version=0)
class Microsoft_Windows_Security_Auditing_4746_0(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4746, version=1)
class Microsoft_Windows_Security_Auditing_4746_1(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "MembershipExpirationTime" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4747, version=0)
class Microsoft_Windows_Security_Auditing_4747_0(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4748, version=0)
class Microsoft_Windows_Security_Auditing_4748_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4749, version=0)
class Microsoft_Windows_Security_Auditing_4749_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SamAccountName" / WString,
        "SidHistory" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4750, version=0)
class Microsoft_Windows_Security_Auditing_4750_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SamAccountName" / WString,
        "SidHistory" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4751, version=0)
class Microsoft_Windows_Security_Auditing_4751_0(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4751, version=1)
class Microsoft_Windows_Security_Auditing_4751_1(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "MembershipExpirationTime" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4752, version=0)
class Microsoft_Windows_Security_Auditing_4752_0(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4753, version=0)
class Microsoft_Windows_Security_Auditing_4753_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4754, version=0)
class Microsoft_Windows_Security_Auditing_4754_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SamAccountName" / WString,
        "SidHistory" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4755, version=0)
class Microsoft_Windows_Security_Auditing_4755_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SamAccountName" / WString,
        "SidHistory" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4756, version=0)
class Microsoft_Windows_Security_Auditing_4756_0(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4756, version=1)
class Microsoft_Windows_Security_Auditing_4756_1(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "MembershipExpirationTime" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4757, version=0)
class Microsoft_Windows_Security_Auditing_4757_0(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4758, version=0)
class Microsoft_Windows_Security_Auditing_4758_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4759, version=0)
class Microsoft_Windows_Security_Auditing_4759_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SamAccountName" / WString,
        "SidHistory" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4760, version=0)
class Microsoft_Windows_Security_Auditing_4760_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SamAccountName" / WString,
        "SidHistory" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4761, version=0)
class Microsoft_Windows_Security_Auditing_4761_0(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4761, version=1)
class Microsoft_Windows_Security_Auditing_4761_1(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "MembershipExpirationTime" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4762, version=0)
class Microsoft_Windows_Security_Auditing_4762_0(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4763, version=0)
class Microsoft_Windows_Security_Auditing_4763_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4764, version=0)
class Microsoft_Windows_Security_Auditing_4764_0(Etw):
    pattern = Struct(
        "GroupTypeChange" / WString,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4765, version=0)
class Microsoft_Windows_Security_Auditing_4765_0(Etw):
    pattern = Struct(
        "SourceUserName" / WString,
        "SourceSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SidList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4766, version=0)
class Microsoft_Windows_Security_Auditing_4766_0(Etw):
    pattern = Struct(
        "SourceUserName" / WString,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / WString,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / WString,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4767, version=0)
class Microsoft_Windows_Security_Auditing_4767_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4768, version=0)
class Microsoft_Windows_Security_Auditing_4768_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "ServiceName" / WString,
        "ServiceSid" / Sid,
        "TicketOptions" / Int32ul,
        "Status" / Int32ul,
        "TicketEncryptionType" / Int32ul,
        "PreAuthType" / WString,
        "IpAddress" / WString,
        "IpPort" / WString,
        "CertIssuerName" / WString,
        "CertSerialNumber" / WString,
        "CertThumbprint" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4769, version=0)
class Microsoft_Windows_Security_Auditing_4769_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "ServiceName" / WString,
        "ServiceSid" / Sid,
        "TicketOptions" / Int32ul,
        "TicketEncryptionType" / Int32ul,
        "IpAddress" / WString,
        "IpPort" / WString,
        "Status" / Int32ul,
        "LogonGuid" / Guid,
        "TransmittedServices" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4770, version=0)
class Microsoft_Windows_Security_Auditing_4770_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "ServiceName" / WString,
        "ServiceSid" / Sid,
        "TicketOptions" / Int32ul,
        "TicketEncryptionType" / Int32ul,
        "IpAddress" / WString,
        "IpPort" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4771, version=0)
class Microsoft_Windows_Security_Auditing_4771_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetSid" / Sid,
        "ServiceName" / WString,
        "TicketOptions" / Int32ul,
        "Status" / Int32ul,
        "PreAuthType" / WString,
        "IpAddress" / WString,
        "IpPort" / WString,
        "CertIssuerName" / WString,
        "CertSerialNumber" / WString,
        "CertThumbprint" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4772, version=0)
class Microsoft_Windows_Security_Auditing_4772_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "ServiceName" / WString,
        "TicketOptions" / WString,
        "FailureCode" / WString,
        "IpAddress" / WString,
        "IpPort" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4773, version=0)
class Microsoft_Windows_Security_Auditing_4773_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "ServiceName" / WString,
        "TicketOptions" / WString,
        "FailureCode" / WString,
        "IpAddress" / WString,
        "IpPort" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4774, version=0)
class Microsoft_Windows_Security_Auditing_4774_0(Etw):
    pattern = Struct(
        "MappingBy" / WString,
        "ClientUserName" / WString,
        "MappedName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4775, version=0)
class Microsoft_Windows_Security_Auditing_4775_0(Etw):
    pattern = Struct(
        "ClientUserName" / WString,
        "MappingBy" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4776, version=0)
class Microsoft_Windows_Security_Auditing_4776_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "TargetUserName" / WString,
        "Workstation" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4777, version=0)
class Microsoft_Windows_Security_Auditing_4777_0(Etw):
    pattern = Struct(
        "ClientUserName" / WString,
        "TargetUserName" / WString,
        "Workstation" / WString,
        "Status" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4778, version=0)
class Microsoft_Windows_Security_Auditing_4778_0(Etw):
    pattern = Struct(
        "AccountName" / WString,
        "AccountDomain" / WString,
        "LogonID" / Int64ul,
        "SessionName" / WString,
        "ClientName" / WString,
        "ClientAddress" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4779, version=0)
class Microsoft_Windows_Security_Auditing_4779_0(Etw):
    pattern = Struct(
        "AccountName" / WString,
        "AccountDomain" / WString,
        "LogonID" / Int64ul,
        "SessionName" / WString,
        "ClientName" / WString,
        "ClientAddress" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4780, version=0)
class Microsoft_Windows_Security_Auditing_4780_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4781, version=0)
class Microsoft_Windows_Security_Auditing_4781_0(Etw):
    pattern = Struct(
        "OldTargetUserName" / WString,
        "NewTargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4782, version=0)
class Microsoft_Windows_Security_Auditing_4782_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4783, version=0)
class Microsoft_Windows_Security_Auditing_4783_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SamAccountName" / WString,
        "SidHistory" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4784, version=0)
class Microsoft_Windows_Security_Auditing_4784_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SamAccountName" / WString,
        "SidHistory" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4785, version=0)
class Microsoft_Windows_Security_Auditing_4785_0(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4785, version=1)
class Microsoft_Windows_Security_Auditing_4785_1(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "MembershipExpirationTime" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4786, version=0)
class Microsoft_Windows_Security_Auditing_4786_0(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4787, version=0)
class Microsoft_Windows_Security_Auditing_4787_0(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4788, version=0)
class Microsoft_Windows_Security_Auditing_4788_0(Etw):
    pattern = Struct(
        "MemberName" / WString,
        "MemberSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4789, version=0)
class Microsoft_Windows_Security_Auditing_4789_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4790, version=0)
class Microsoft_Windows_Security_Auditing_4790_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SamAccountName" / WString,
        "SidHistory" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4791, version=0)
class Microsoft_Windows_Security_Auditing_4791_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SamAccountName" / WString,
        "SidHistory" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4792, version=0)
class Microsoft_Windows_Security_Auditing_4792_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4793, version=0)
class Microsoft_Windows_Security_Auditing_4793_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "Workstation" / WString,
        "TargetUserName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4794, version=0)
class Microsoft_Windows_Security_Auditing_4794_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "Workstation" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4797, version=0)
class Microsoft_Windows_Security_Auditing_4797_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "Workstation" / WString,
        "TargetUserName" / WString,
        "TargetDomainName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4798, version=0)
class Microsoft_Windows_Security_Auditing_4798_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "CallerProcessId" / Int64ul,
        "CallerProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4799, version=0)
class Microsoft_Windows_Security_Auditing_4799_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "CallerProcessId" / Int64ul,
        "CallerProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4800, version=0)
class Microsoft_Windows_Security_Auditing_4800_0(Etw):
    pattern = Struct(
        "TargetUserSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetLogonId" / Int64ul,
        "SessionId" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4801, version=0)
class Microsoft_Windows_Security_Auditing_4801_0(Etw):
    pattern = Struct(
        "TargetUserSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetLogonId" / Int64ul,
        "SessionId" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4802, version=0)
class Microsoft_Windows_Security_Auditing_4802_0(Etw):
    pattern = Struct(
        "TargetUserSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetLogonId" / Int64ul,
        "SessionId" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4803, version=0)
class Microsoft_Windows_Security_Auditing_4803_0(Etw):
    pattern = Struct(
        "TargetUserSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetLogonId" / Int64ul,
        "SessionId" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4816, version=0)
class Microsoft_Windows_Security_Auditing_4816_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4816, version=1)
class Microsoft_Windows_Security_Auditing_4816_1(Etw):
    pattern = Struct(
        "PeerName" / WString,
        "ProtocolSequence" / WString,
        "SecurityError" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4817, version=0)
class Microsoft_Windows_Security_Auditing_4817_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectServer" / WString,
        "ObjectType" / WString,
        "ObjectName" / WString,
        "OldSd" / WString,
        "NewSd" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4818, version=0)
class Microsoft_Windows_Security_Auditing_4818_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectServer" / WString,
        "ObjectType" / WString,
        "ObjectName" / WString,
        "HandleId" / Int64ul,
        "ProcessId" / Int64ul,
        "ProcessName" / WString,
        "AccessReason" / WString,
        "StagingReason" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4819, version=0)
class Microsoft_Windows_Security_Auditing_4819_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectServer" / WString,
        "ObjectType" / WString,
        "AddedCAPs" / WString,
        "DeletedCAPs" / WString,
        "ModifiedCAPs" / WString,
        "AsIsCAPs" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4820, version=0)
class Microsoft_Windows_Security_Auditing_4820_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "DeviceName" / WString,
        "ServiceName" / WString,
        "ServiceSid" / Sid,
        "TicketOptions" / Int32ul,
        "Status" / Int32ul,
        "TicketEncryptionType" / Int32ul,
        "PreAuthType" / WString,
        "IpAddress" / WString,
        "IpPort" / WString,
        "CertIssuerName" / WString,
        "CertSerialNumber" / WString,
        "CertThumbprint" / WString,
        "SiloName" / WString,
        "PolicyName" / WString,
        "TGTLifetime" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4821, version=0)
class Microsoft_Windows_Security_Auditing_4821_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "DeviceName" / WString,
        "ServiceName" / WString,
        "ServiceSid" / Sid,
        "TicketOptions" / Int32ul,
        "TicketEncryptionType" / Int32ul,
        "IpAddress" / WString,
        "IpPort" / WString,
        "Status" / Int32ul,
        "LogonGuid" / Guid,
        "TransitedServices" / WString,
        "SiloName" / WString,
        "PolicyName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4822, version=0)
class Microsoft_Windows_Security_Auditing_4822_0(Etw):
    pattern = Struct(
        "AccountName" / WString,
        "DeviceName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4823, version=0)
class Microsoft_Windows_Security_Auditing_4823_0(Etw):
    pattern = Struct(
        "AccountName" / WString,
        "DeviceName" / WString,
        "Status" / Int32ul,
        "SiloName" / WString,
        "PolicyName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4824, version=0)
class Microsoft_Windows_Security_Auditing_4824_0(Etw):
    pattern = Struct(
        "TargetUserName" / WString,
        "TargetSid" / Sid,
        "ServiceName" / WString,
        "TicketOptions" / Int32ul,
        "Status" / Int32ul,
        "PreAuthType" / WString,
        "IpAddress" / WString,
        "IpPort" / WString,
        "CertIssuerName" / WString,
        "CertSerialNumber" / WString,
        "CertThumbprint" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4825, version=0)
class Microsoft_Windows_Security_Auditing_4825_0(Etw):
    pattern = Struct(
        "AccountName" / WString,
        "AccountDomain" / WString,
        "LogonID" / Int64ul,
        "ClientAddress" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4826, version=0)
class Microsoft_Windows_Security_Auditing_4826_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "LoadOptions" / WString,
        "AdvancedOptions" / WString,
        "ConfigAccessPolicy" / WString,
        "RemoteEventLogging" / WString,
        "KernelDebug" / WString,
        "VsmLaunchType" / WString,
        "TestSigning" / WString,
        "FlightSigning" / WString,
        "DisableIntegrityChecks" / WString,
        "HypervisorLoadOptions" / WString,
        "HypervisorLaunchType" / WString,
        "HypervisorDebug" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4830, version=0)
class Microsoft_Windows_Security_Auditing_4830_0(Etw):
    pattern = Struct(
        "SourceUserName" / WString,
        "SourceSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PrivilegeList" / WString,
        "SidList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4864, version=0)
class Microsoft_Windows_Security_Auditing_4864_0(Etw):
    pattern = Struct(
        "CollisionTargetType" / Int32ul,
        "CollisionTargetName" / WString,
        "ForestRoot" / WString,
        "TopLevelName" / WString,
        "DnsName" / WString,
        "NetbiosName" / WString,
        "DomainSid" / Sid,
        "Flags" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4865, version=0)
class Microsoft_Windows_Security_Auditing_4865_0(Etw):
    pattern = Struct(
        "ForestRoot" / WString,
        "ForestRootSid" / Sid,
        "OperationId" / Int64ul,
        "EntryType" / Int32ul,
        "Flags" / Int32ul,
        "TopLevelName" / WString,
        "DnsName" / WString,
        "NetbiosName" / WString,
        "DomainSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4866, version=0)
class Microsoft_Windows_Security_Auditing_4866_0(Etw):
    pattern = Struct(
        "ForestRoot" / WString,
        "ForestRootSid" / Sid,
        "OperationId" / Int64ul,
        "EntryType" / Int32ul,
        "Flags" / Int32ul,
        "TopLevelName" / WString,
        "DnsName" / WString,
        "NetbiosName" / WString,
        "DomainSid" / Sid,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4867, version=0)
class Microsoft_Windows_Security_Auditing_4867_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ForestRoot" / WString,
        "ForestRootSid" / Sid,
        "OperationId" / Int64ul,
        "EntryType" / Int32ul,
        "Flags" / Int32ul,
        "TopLevelName" / WString,
        "DnsName" / WString,
        "NetbiosName" / WString,
        "DomainSid" / Sid
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4868, version=0)
class Microsoft_Windows_Security_Auditing_4868_0(Etw):
    pattern = Struct(
        "RequestId" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4869, version=0)
class Microsoft_Windows_Security_Auditing_4869_0(Etw):
    pattern = Struct(
        "RequestId" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4870, version=0)
class Microsoft_Windows_Security_Auditing_4870_0(Etw):
    pattern = Struct(
        "CertificateSerialNumber" / WString,
        "RevocationReason" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4871, version=0)
class Microsoft_Windows_Security_Auditing_4871_0(Etw):
    pattern = Struct(
        "NextUpdate" / WString,
        "NextPublishForBaseCRL" / WString,
        "NextPublishForDeltaCRL" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4872, version=0)
class Microsoft_Windows_Security_Auditing_4872_0(Etw):
    pattern = Struct(
        "IsBaseCRL" / WString,
        "CRLNumber" / WString,
        "KeyContainer" / WString,
        "NextPublish" / WString,
        "PublishURLs" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4873, version=0)
class Microsoft_Windows_Security_Auditing_4873_0(Etw):
    pattern = Struct(
        "RequestId" / WString,
        "ExtensionName" / WString,
        "ExtensionDataType" / WString,
        "ExtensionPolicyFlags" / WString,
        "ExtensionData" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4874, version=0)
class Microsoft_Windows_Security_Auditing_4874_0(Etw):
    pattern = Struct(
        "RequestId" / WString,
        "Attributes" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4875, version=0)
class Microsoft_Windows_Security_Auditing_4875_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4876, version=0)
class Microsoft_Windows_Security_Auditing_4876_0(Etw):
    pattern = Struct(
        "BackupType" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4877, version=0)
class Microsoft_Windows_Security_Auditing_4877_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4880, version=0)
class Microsoft_Windows_Security_Auditing_4880_0(Etw):
    pattern = Struct(
        "CertificateDatabaseHash" / WString,
        "PrivateKeyUsageCount" / WString,
        "CACertificateHash" / WString,
        "CAPublicKeyHash" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4881, version=0)
class Microsoft_Windows_Security_Auditing_4881_0(Etw):
    pattern = Struct(
        "CertificateDatabaseHash" / WString,
        "PrivateKeyUsageCount" / WString,
        "CACertificateHash" / WString,
        "CAPublicKeyHash" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4882, version=0)
class Microsoft_Windows_Security_Auditing_4882_0(Etw):
    pattern = Struct(
        "SecuritySettings" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4883, version=0)
class Microsoft_Windows_Security_Auditing_4883_0(Etw):
    pattern = Struct(
        "RequestId" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4884, version=0)
class Microsoft_Windows_Security_Auditing_4884_0(Etw):
    pattern = Struct(
        "Certificate" / WString,
        "RequestId" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4885, version=0)
class Microsoft_Windows_Security_Auditing_4885_0(Etw):
    pattern = Struct(
        "AuditFilter" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4886, version=0)
class Microsoft_Windows_Security_Auditing_4886_0(Etw):
    pattern = Struct(
        "RequestId" / WString,
        "Requester" / WString,
        "Attributes" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4887, version=0)
class Microsoft_Windows_Security_Auditing_4887_0(Etw):
    pattern = Struct(
        "RequestId" / WString,
        "Requester" / WString,
        "Attributes" / WString,
        "Disposition" / WString,
        "SubjectKeyIdentifier" / WString,
        "Subject" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4888, version=0)
class Microsoft_Windows_Security_Auditing_4888_0(Etw):
    pattern = Struct(
        "RequestId" / WString,
        "Requester" / WString,
        "Attributes" / WString,
        "Disposition" / WString,
        "SubjectKeyIdentifier" / WString,
        "Subject" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4889, version=0)
class Microsoft_Windows_Security_Auditing_4889_0(Etw):
    pattern = Struct(
        "RequestId" / WString,
        "Requester" / WString,
        "Attributes" / WString,
        "Disposition" / WString,
        "SubjectKeyIdentifier" / WString,
        "Subject" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4890, version=0)
class Microsoft_Windows_Security_Auditing_4890_0(Etw):
    pattern = Struct(
        "EnableRestrictedPermissions" / WString,
        "RestrictedPermissions" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4891, version=0)
class Microsoft_Windows_Security_Auditing_4891_0(Etw):
    pattern = Struct(
        "Node" / WString,
        "Entry" / WString,
        "Value" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4892, version=0)
class Microsoft_Windows_Security_Auditing_4892_0(Etw):
    pattern = Struct(
        "PropertyName" / WString,
        "PropertyIndex" / WString,
        "PropertyType" / WString,
        "PropertyValue" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4893, version=0)
class Microsoft_Windows_Security_Auditing_4893_0(Etw):
    pattern = Struct(
        "RequestId" / WString,
        "Requester" / WString,
        "KRAHashes" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4894, version=0)
class Microsoft_Windows_Security_Auditing_4894_0(Etw):
    pattern = Struct(
        "RequestId" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4895, version=0)
class Microsoft_Windows_Security_Auditing_4895_0(Etw):
    pattern = Struct(
        "CertificateHash" / WString,
        "ValidFrom" / WString,
        "ValidTo" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4896, version=0)
class Microsoft_Windows_Security_Auditing_4896_0(Etw):
    pattern = Struct(
        "TableId" / WString,
        "Filter" / WString,
        "RowsDeleted" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4897, version=0)
class Microsoft_Windows_Security_Auditing_4897_0(Etw):
    pattern = Struct(
        "RoleSeparationEnabled" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4898, version=0)
class Microsoft_Windows_Security_Auditing_4898_0(Etw):
    pattern = Struct(
        "TemplateInternalName" / WString,
        "TemplateVersion" / WString,
        "TemplateSchemaVersion" / WString,
        "TemplateOID" / WString,
        "TemplateDSObjectFQDN" / WString,
        "DCDNSName" / WString,
        "TemplateContent" / WString,
        "SecurityDescriptor" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4899, version=0)
class Microsoft_Windows_Security_Auditing_4899_0(Etw):
    pattern = Struct(
        "TemplateInternalName" / WString,
        "TemplateVersion" / WString,
        "TemplateSchemaVersion" / WString,
        "TemplateOID" / WString,
        "TemplateDSObjectFQDN" / WString,
        "DCDNSName" / WString,
        "NewTemplateContent" / WString,
        "OldTemplateContent" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4900, version=0)
class Microsoft_Windows_Security_Auditing_4900_0(Etw):
    pattern = Struct(
        "TemplateInternalName" / WString,
        "TemplateVersion" / WString,
        "TemplateSchemaVersion" / WString,
        "TemplateOID" / WString,
        "TemplateDSObjectFQDN" / WString,
        "DCDNSName" / WString,
        "NewTemplateContent" / WString,
        "NewSecurityDescriptor" / WString,
        "OldTemplateContent" / WString,
        "OldSecurityDescriptor" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4902, version=0)
class Microsoft_Windows_Security_Auditing_4902_0(Etw):
    pattern = Struct(
        "PuaCount" / Int32ul,
        "PuaPolicyId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4904, version=0)
class Microsoft_Windows_Security_Auditing_4904_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "AuditSourceName" / WString,
        "EventSourceId" / Int64ul,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4905, version=0)
class Microsoft_Windows_Security_Auditing_4905_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "AuditSourceName" / WString,
        "EventSourceId" / Int64ul,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4906, version=0)
class Microsoft_Windows_Security_Auditing_4906_0(Etw):
    pattern = Struct(
        "CrashOnAuditFailValue" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4907, version=0)
class Microsoft_Windows_Security_Auditing_4907_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectServer" / WString,
        "ObjectType" / WString,
        "ObjectName" / WString,
        "HandleId" / Int64ul,
        "OldSd" / WString,
        "NewSd" / WString,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4908, version=0)
class Microsoft_Windows_Security_Auditing_4908_0(Etw):
    pattern = Struct(
        "SidList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4909, version=0)
class Microsoft_Windows_Security_Auditing_4909_0(Etw):
    pattern = Struct(
        "OldBlockedOrdinals" / WString,
        "NewBlockedOrdinals" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4910, version=0)
class Microsoft_Windows_Security_Auditing_4910_0(Etw):
    pattern = Struct(
        "OldIgnoreDefaultSettings" / Int32ul,
        "NewIgnoreDefaultSettings" / Int32ul,
        "OldIgnoreLocalSettings" / Int32ul,
        "NewIgnoreLocalSettings" / Int32ul,
        "OldBlockedOrdinals" / WString,
        "NewBlockedOrdinals" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4911, version=0)
class Microsoft_Windows_Security_Auditing_4911_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectServer" / WString,
        "ObjectType" / WString,
        "ObjectName" / WString,
        "HandleId" / Int64ul,
        "OldSd" / WString,
        "NewSd" / WString,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4912, version=0)
class Microsoft_Windows_Security_Auditing_4912_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TargetUserSid" / Sid,
        "CategoryId" / WString,
        "SubcategoryId" / WString,
        "SubcategoryGuid" / Guid,
        "AuditPolicyChanges" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4913, version=0)
class Microsoft_Windows_Security_Auditing_4913_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectServer" / WString,
        "ObjectType" / WString,
        "ObjectName" / WString,
        "HandleId" / Int64ul,
        "OldSd" / WString,
        "NewSd" / WString,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4928, version=0)
class Microsoft_Windows_Security_Auditing_4928_0(Etw):
    pattern = Struct(
        "DestinationDRA" / WString,
        "SourceDRA" / WString,
        "SourceAddr" / WString,
        "NamingContext" / WString,
        "Options" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4928, version=1)
class Microsoft_Windows_Security_Auditing_4928_1(Etw):
    pattern = Struct(
        "DestinationDRA" / WString,
        "SourceDRA" / WString,
        "SourceAddr" / WString,
        "NamingContext" / WString,
        "Options" / Int64ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4929, version=0)
class Microsoft_Windows_Security_Auditing_4929_0(Etw):
    pattern = Struct(
        "DestinationDRA" / WString,
        "SourceDRA" / WString,
        "SourceAddr" / WString,
        "NamingContext" / WString,
        "Options" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4929, version=1)
class Microsoft_Windows_Security_Auditing_4929_1(Etw):
    pattern = Struct(
        "DestinationDRA" / WString,
        "SourceDRA" / WString,
        "SourceAddr" / WString,
        "NamingContext" / WString,
        "Options" / Int64ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4930, version=0)
class Microsoft_Windows_Security_Auditing_4930_0(Etw):
    pattern = Struct(
        "DestinationDRA" / WString,
        "SourceDRA" / WString,
        "SourceAddr" / WString,
        "NamingContext" / WString,
        "Options" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4930, version=1)
class Microsoft_Windows_Security_Auditing_4930_1(Etw):
    pattern = Struct(
        "DestinationDRA" / WString,
        "SourceDRA" / WString,
        "SourceAddr" / WString,
        "NamingContext" / WString,
        "Options" / Int64ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4931, version=0)
class Microsoft_Windows_Security_Auditing_4931_0(Etw):
    pattern = Struct(
        "DestinationDRA" / WString,
        "SourceDRA" / WString,
        "SourceAddr" / WString,
        "NamingContext" / WString,
        "Options" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4931, version=1)
class Microsoft_Windows_Security_Auditing_4931_1(Etw):
    pattern = Struct(
        "DestinationDRA" / WString,
        "SourceDRA" / WString,
        "SourceAddr" / WString,
        "NamingContext" / WString,
        "Options" / Int64ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4932, version=0)
class Microsoft_Windows_Security_Auditing_4932_0(Etw):
    pattern = Struct(
        "DestinationDRA" / WString,
        "SourceDRA" / WString,
        "NamingContext" / WString,
        "Options" / Int32ul,
        "SessionID" / Int32ul,
        "StartUSN" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4932, version=1)
class Microsoft_Windows_Security_Auditing_4932_1(Etw):
    pattern = Struct(
        "DestinationDRA" / WString,
        "SourceDRA" / WString,
        "NamingContext" / WString,
        "Options" / Int64ul,
        "SessionID" / Int32ul,
        "StartUSN" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4933, version=0)
class Microsoft_Windows_Security_Auditing_4933_0(Etw):
    pattern = Struct(
        "DestinationDRA" / WString,
        "SourceDRA" / WString,
        "NamingContext" / WString,
        "Options" / Int32ul,
        "SessionID" / Int32ul,
        "EndUSN" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4933, version=1)
class Microsoft_Windows_Security_Auditing_4933_1(Etw):
    pattern = Struct(
        "DestinationDRA" / WString,
        "SourceDRA" / WString,
        "NamingContext" / WString,
        "Options" / Int64ul,
        "SessionID" / Int32ul,
        "EndUSN" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4934, version=0)
class Microsoft_Windows_Security_Auditing_4934_0(Etw):
    pattern = Struct(
        "SessionID" / Int32ul,
        "Object" / WString,
        "Attribute" / WString,
        "TypeOfChange" / Int32ul,
        "NewValue" / WString,
        "USN" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4935, version=0)
class Microsoft_Windows_Security_Auditing_4935_0(Etw):
    pattern = Struct(
        "ReplicationEvent" / Int32ul,
        "AuditStatusCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4936, version=0)
class Microsoft_Windows_Security_Auditing_4936_0(Etw):
    pattern = Struct(
        "ReplicationEvent" / Int32ul,
        "AuditStatusCode" / Int32ul,
        "ReplicationStatusCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4937, version=0)
class Microsoft_Windows_Security_Auditing_4937_0(Etw):
    pattern = Struct(
        "DestinationDRA" / WString,
        "SourceDRA" / WString,
        "Object" / WString,
        "Options" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4937, version=1)
class Microsoft_Windows_Security_Auditing_4937_1(Etw):
    pattern = Struct(
        "DestinationDRA" / WString,
        "SourceDRA" / WString,
        "Object" / WString,
        "Options" / Int64ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4944, version=0)
class Microsoft_Windows_Security_Auditing_4944_0(Etw):
    pattern = Struct(
        "GroupPolicyApplied" / WString,
        "Profile" / WString,
        "OperationMode" / WString,
        "RemoteAdminEnabled" / WString,
        "MulticastFlowsEnabled" / WString,
        "LogDroppedPacketsEnabled" / WString,
        "LogSuccessfulConnectionsEnabled" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4945, version=0)
class Microsoft_Windows_Security_Auditing_4945_0(Etw):
    pattern = Struct(
        "ProfileUsed" / WString,
        "RuleId" / WString,
        "RuleName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4946, version=0)
class Microsoft_Windows_Security_Auditing_4946_0(Etw):
    pattern = Struct(
        "ProfileChanged" / WString,
        "RuleId" / WString,
        "RuleName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4947, version=0)
class Microsoft_Windows_Security_Auditing_4947_0(Etw):
    pattern = Struct(
        "ProfileChanged" / WString,
        "RuleId" / WString,
        "RuleName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4948, version=0)
class Microsoft_Windows_Security_Auditing_4948_0(Etw):
    pattern = Struct(
        "ProfileChanged" / WString,
        "RuleId" / WString,
        "RuleName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4950, version=0)
class Microsoft_Windows_Security_Auditing_4950_0(Etw):
    pattern = Struct(
        "ProfileChanged" / WString,
        "SettingType" / WString,
        "SettingValue" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4951, version=0)
class Microsoft_Windows_Security_Auditing_4951_0(Etw):
    pattern = Struct(
        "Profile" / WString,
        "RuleId" / WString,
        "RuleName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4952, version=0)
class Microsoft_Windows_Security_Auditing_4952_0(Etw):
    pattern = Struct(
        "Profile" / WString,
        "RuleId" / WString,
        "RuleName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4953, version=0)
class Microsoft_Windows_Security_Auditing_4953_0(Etw):
    pattern = Struct(
        "Profile" / WString,
        "ReasonForRejection" / WString,
        "RuleId" / WString,
        "RuleName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4956, version=0)
class Microsoft_Windows_Security_Auditing_4956_0(Etw):
    pattern = Struct(
        "ActiveProfile" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4957, version=0)
class Microsoft_Windows_Security_Auditing_4957_0(Etw):
    pattern = Struct(
        "RuleId" / WString,
        "RuleName" / WString,
        "RuleAttr" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4958, version=0)
class Microsoft_Windows_Security_Auditing_4958_0(Etw):
    pattern = Struct(
        "RuleId" / WString,
        "RuleName" / WString,
        "Error" / WString,
        "Reason" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4960, version=0)
class Microsoft_Windows_Security_Auditing_4960_0(Etw):
    pattern = Struct(
        "RemoteAddress" / WString,
        "SPI" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4961, version=0)
class Microsoft_Windows_Security_Auditing_4961_0(Etw):
    pattern = Struct(
        "RemoteAddress" / WString,
        "SPI" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4962, version=0)
class Microsoft_Windows_Security_Auditing_4962_0(Etw):
    pattern = Struct(
        "RemoteAddress" / WString,
        "SPI" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4963, version=0)
class Microsoft_Windows_Security_Auditing_4963_0(Etw):
    pattern = Struct(
        "RemoteAddress" / WString,
        "SPI" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4964, version=0)
class Microsoft_Windows_Security_Auditing_4964_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "LogonGuid" / Guid,
        "TargetUserSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetLogonId" / Int64ul,
        "TargetLogonGuid" / Guid,
        "SidList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4965, version=0)
class Microsoft_Windows_Security_Auditing_4965_0(Etw):
    pattern = Struct(
        "RemoteAddress" / WString,
        "SPI" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4976, version=0)
class Microsoft_Windows_Security_Auditing_4976_0(Etw):
    pattern = Struct(
        "LocalAddress" / WString,
        "RemoteAddress" / WString,
        "KeyModName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4977, version=0)
class Microsoft_Windows_Security_Auditing_4977_0(Etw):
    pattern = Struct(
        "LocalAddress" / WString,
        "RemoteAddress" / WString,
        "KeyModName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4978, version=0)
class Microsoft_Windows_Security_Auditing_4978_0(Etw):
    pattern = Struct(
        "LocalAddress" / WString,
        "RemoteAddress" / WString,
        "KeyModName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4979, version=0)
class Microsoft_Windows_Security_Auditing_4979_0(Etw):
    pattern = Struct(
        "LocalMMPrincipalName" / WString,
        "RemoteMMPrincipalName" / WString,
        "LocalAddress" / WString,
        "LocalKeyModPort" / Int32ul,
        "RemoteAddress" / WString,
        "RemoteKeyModPort" / Int32ul,
        "MMAuthMethod" / WString,
        "MMCipherAlg" / WString,
        "MMIntegrityAlg" / WString,
        "DHGroup" / WString,
        "MMLifetime" / Int32ul,
        "QMLimit" / Int32ul,
        "Role" / WString,
        "MMImpersonationState" / WString,
        "MMFilterID" / Int64ul,
        "MMSAID" / Int64ul,
        "LocalEMPrincipalName" / WString,
        "RemoteEMPrincipalName" / WString,
        "EMAuthMethod" / WString,
        "EMImpersonationState" / WString,
        "QMFilterID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4980, version=0)
class Microsoft_Windows_Security_Auditing_4980_0(Etw):
    pattern = Struct(
        "LocalMMPrincipalName" / WString,
        "RemoteMMPrincipalName" / WString,
        "LocalAddress" / WString,
        "LocalKeyModPort" / Int32ul,
        "RemoteAddress" / WString,
        "RemoteKeyModPort" / Int32ul,
        "MMAuthMethod" / WString,
        "MMCipherAlg" / WString,
        "MMIntegrityAlg" / WString,
        "DHGroup" / WString,
        "MMLifetime" / Int32ul,
        "QMLimit" / Int32ul,
        "Role" / WString,
        "MMImpersonationState" / WString,
        "MMFilterID" / Int64ul,
        "MMSAID" / Int64ul,
        "LocalEMPrincipalName" / WString,
        "LocalEMCertHash" / WString,
        "LocalEMIssuingCA" / WString,
        "LocalEMRootCA" / WString,
        "RemoteEMPrincipalName" / WString,
        "RemoteEMCertHash" / WString,
        "RemoteEMIssuingCA" / WString,
        "RemoteEMRootCA" / WString,
        "EMImpersonationState" / WString,
        "QMFilterID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4981, version=0)
class Microsoft_Windows_Security_Auditing_4981_0(Etw):
    pattern = Struct(
        "LocalMMPrincipalName" / WString,
        "LocalMMCertHash" / WString,
        "LocalMMIssuingCA" / WString,
        "LocalMMRootCA" / WString,
        "RemoteMMPrincipalName" / WString,
        "RemoteMMCertHash" / WString,
        "RemoteMMIssuingCA" / WString,
        "RemoteMMRootCA" / WString,
        "LocalAddress" / WString,
        "LocalKeyModPort" / Int32ul,
        "RemoteAddress" / WString,
        "RemoteKeyModPort" / Int32ul,
        "MMCipherAlg" / WString,
        "MMIntegrityAlg" / WString,
        "DHGroup" / WString,
        "MMLifetime" / Int32ul,
        "QMLimit" / Int32ul,
        "Role" / WString,
        "MMImpersonationState" / WString,
        "MMFilterID" / Int64ul,
        "MMSAID" / Int64ul,
        "LocalEMPrincipalName" / WString,
        "RemoteEMPrincipalName" / WString,
        "EMAuthMethod" / WString,
        "EMImpersonationState" / WString,
        "QMFilterID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4982, version=0)
class Microsoft_Windows_Security_Auditing_4982_0(Etw):
    pattern = Struct(
        "LocalMMPrincipalName" / WString,
        "LocalMMCertHash" / WString,
        "LocalMMIssuingCA" / WString,
        "LocalMMRootCA" / WString,
        "RemoteMMPrincipalName" / WString,
        "RemoteMMCertHash" / WString,
        "RemoteMMIssuingCA" / WString,
        "RemoteMMRootCA" / WString,
        "LocalKeyModPort" / Int32ul,
        "RemoteAddress" / WString,
        "RemoteKeyModPort" / Int32ul,
        "MMCipherAlg" / WString,
        "MMIntegrityAlg" / WString,
        "DHGroup" / WString,
        "MMLifetime" / Int32ul,
        "QMLimit" / Int32ul,
        "Role" / WString,
        "MMImpersonationState" / WString,
        "MMFilterID" / Int64ul,
        "MMSAID" / Int64ul,
        "LocalEMPrincipalName" / WString,
        "LocalEMCertHash" / WString,
        "LocalEMIssuingCA" / WString,
        "LocalEMRootCA" / WString,
        "RemoteEMPrincipalName" / WString,
        "RemoteEMCertHash" / WString,
        "RemoteEMIssuingCA" / WString,
        "RemoteEMRootCA" / WString,
        "EMImpersonationState" / WString,
        "QMFilterID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4983, version=0)
class Microsoft_Windows_Security_Auditing_4983_0(Etw):
    pattern = Struct(
        "LocalEMPrincipalName" / WString,
        "LocalEMCertHash" / WString,
        "LocalEMIssuingCA" / WString,
        "LocalEMRootCA" / WString,
        "RemoteEMPrincipalName" / WString,
        "RemoteEMCertHash" / WString,
        "RemoteEMIssuingCA" / WString,
        "RemoteEMRootCA" / WString,
        "LocalAddress" / WString,
        "LocalKeyModPort" / Int32ul,
        "RemoteAddress" / WString,
        "RemoteKeyModPort" / Int32ul,
        "FailurePoint" / WString,
        "FailureReason" / WString,
        "State" / WString,
        "Role" / WString,
        "EMImpersonationState" / WString,
        "QMFilterID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4984, version=0)
class Microsoft_Windows_Security_Auditing_4984_0(Etw):
    pattern = Struct(
        "LocalEMPrincipalName" / WString,
        "RemoteEMPrincipalName" / WString,
        "LocalAddress" / WString,
        "LocalKeyModPort" / Int32ul,
        "RemoteAddress" / WString,
        "RemoteKeyModPort" / Int32ul,
        "FailurePoint" / WString,
        "FailureReason" / WString,
        "EMAuthMethod" / WString,
        "State" / WString,
        "Role" / WString,
        "EMImpersonationState" / WString,
        "QMFilterID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=4985, version=0)
class Microsoft_Windows_Security_Auditing_4985_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TransactionId" / Guid,
        "NewState" / Int32ul,
        "ResourceManager" / Guid,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5027, version=0)
class Microsoft_Windows_Security_Auditing_5027_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5028, version=0)
class Microsoft_Windows_Security_Auditing_5028_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5029, version=0)
class Microsoft_Windows_Security_Auditing_5029_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5030, version=0)
class Microsoft_Windows_Security_Auditing_5030_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5031, version=0)
class Microsoft_Windows_Security_Auditing_5031_0(Etw):
    pattern = Struct(
        "Profiles" / WString,
        "Application" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5032, version=0)
class Microsoft_Windows_Security_Auditing_5032_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5035, version=0)
class Microsoft_Windows_Security_Auditing_5035_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5037, version=0)
class Microsoft_Windows_Security_Auditing_5037_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5038, version=0)
class Microsoft_Windows_Security_Auditing_5038_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5039, version=0)
class Microsoft_Windows_Security_Auditing_5039_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectPath" / WString,
        "ObjectVirtualPath" / WString,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5040, version=0)
class Microsoft_Windows_Security_Auditing_5040_0(Etw):
    pattern = Struct(
        "ProfileChanged" / WString,
        "AuthenticationSetId" / WString,
        "AuthenticationSetName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5041, version=0)
class Microsoft_Windows_Security_Auditing_5041_0(Etw):
    pattern = Struct(
        "ProfileChanged" / WString,
        "AuthenticationSetId" / WString,
        "AuthenticationSetName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5042, version=0)
class Microsoft_Windows_Security_Auditing_5042_0(Etw):
    pattern = Struct(
        "ProfileChanged" / WString,
        "AuthenticationSetId" / WString,
        "AuthenticationSetName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5043, version=0)
class Microsoft_Windows_Security_Auditing_5043_0(Etw):
    pattern = Struct(
        "ProfileChanged" / WString,
        "ConnectionSecurityRuleId" / WString,
        "ConnectionSecurityRuleName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5044, version=0)
class Microsoft_Windows_Security_Auditing_5044_0(Etw):
    pattern = Struct(
        "ProfileChanged" / WString,
        "ConnectionSecurityRuleId" / WString,
        "ConnectionSecurityRuleName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5045, version=0)
class Microsoft_Windows_Security_Auditing_5045_0(Etw):
    pattern = Struct(
        "ProfileChanged" / WString,
        "ConnectionSecurityRuleId" / WString,
        "ConnectionSecurityRuleName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5046, version=0)
class Microsoft_Windows_Security_Auditing_5046_0(Etw):
    pattern = Struct(
        "ProfileChanged" / WString,
        "CryptographicSetId" / WString,
        "CryptographicSetName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5047, version=0)
class Microsoft_Windows_Security_Auditing_5047_0(Etw):
    pattern = Struct(
        "ProfileChanged" / WString,
        "CryptographicSetId" / WString,
        "CryptographicSetName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5048, version=0)
class Microsoft_Windows_Security_Auditing_5048_0(Etw):
    pattern = Struct(
        "ProfileChanged" / WString,
        "CryptographicSetId" / WString,
        "CryptographicSetName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5049, version=0)
class Microsoft_Windows_Security_Auditing_5049_0(Etw):
    pattern = Struct(
        "ProfileChanged" / WString,
        "IpSecSecurityAssociationId" / WString,
        "IpSecSecurityAssociationName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5050, version=0)
class Microsoft_Windows_Security_Auditing_5050_0(Etw):
    pattern = Struct(
        "CallerProcessName" / WString,
        "ProcessId" / Int32ul,
        "Publisher" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5051, version=0)
class Microsoft_Windows_Security_Auditing_5051_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "FileName" / WString,
        "VirtualFileName" / WString,
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5056, version=0)
class Microsoft_Windows_Security_Auditing_5056_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "Module" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5057, version=0)
class Microsoft_Windows_Security_Auditing_5057_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ProviderName" / WString,
        "AlgorithmName" / WString,
        "Reason" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5058, version=0)
class Microsoft_Windows_Security_Auditing_5058_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ProviderName" / WString,
        "AlgorithmName" / WString,
        "KeyName" / WString,
        "KeyType" / WString,
        "KeyFilePath" / WString,
        "Operation" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5058, version=1)
class Microsoft_Windows_Security_Auditing_5058_1(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ClientProcessId" / Int32ul,
        "ClientCreationTime" / Int64ul,
        "ProviderName" / WString,
        "AlgorithmName" / WString,
        "KeyName" / WString,
        "KeyType" / WString,
        "KeyFilePath" / WString,
        "Operation" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5059, version=0)
class Microsoft_Windows_Security_Auditing_5059_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ProviderName" / WString,
        "AlgorithmName" / WString,
        "KeyName" / WString,
        "KeyType" / WString,
        "Operation" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5059, version=1)
class Microsoft_Windows_Security_Auditing_5059_1(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ClientProcessId" / Int32ul,
        "ClientCreationTime" / Int64ul,
        "ProviderName" / WString,
        "AlgorithmName" / WString,
        "KeyName" / WString,
        "KeyType" / WString,
        "Operation" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5060, version=0)
class Microsoft_Windows_Security_Auditing_5060_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ProviderName" / WString,
        "AlgorithmName" / WString,
        "KeyName" / WString,
        "KeyType" / WString,
        "Reason" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5061, version=0)
class Microsoft_Windows_Security_Auditing_5061_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ProviderName" / WString,
        "AlgorithmName" / WString,
        "KeyName" / WString,
        "KeyType" / WString,
        "Operation" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5062, version=0)
class Microsoft_Windows_Security_Auditing_5062_0(Etw):
    pattern = Struct(
        "Module" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5063, version=0)
class Microsoft_Windows_Security_Auditing_5063_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ProviderName" / WString,
        "ModuleName" / WString,
        "Operation" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5064, version=0)
class Microsoft_Windows_Security_Auditing_5064_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "Scope" / WString,
        "ContextName" / WString,
        "Operation" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5065, version=0)
class Microsoft_Windows_Security_Auditing_5065_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "Scope" / WString,
        "ContextName" / WString,
        "OldValue" / Int32ul,
        "NewValue" / Int32ul,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5066, version=0)
class Microsoft_Windows_Security_Auditing_5066_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "Scope" / WString,
        "ContextName" / WString,
        "InterfaceId" / WString,
        "FunctionName" / WString,
        "Position" / Int32ul,
        "Operation" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5067, version=0)
class Microsoft_Windows_Security_Auditing_5067_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "Scope" / WString,
        "ContextName" / WString,
        "InterfaceId" / WString,
        "FunctionName" / WString,
        "OldValue" / Int32ul,
        "NewValue" / Int32ul,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5068, version=0)
class Microsoft_Windows_Security_Auditing_5068_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "Scope" / WString,
        "ContextName" / WString,
        "InterfaceId" / WString,
        "FunctionName" / WString,
        "ProviderName" / WString,
        "Position" / Int32ul,
        "Operation" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5069, version=0)
class Microsoft_Windows_Security_Auditing_5069_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "Scope" / WString,
        "ContextName" / WString,
        "InterfaceId" / WString,
        "FunctionName" / WString,
        "PropertyName" / WString,
        "Operation" / WString,
        "Value" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5070, version=0)
class Microsoft_Windows_Security_Auditing_5070_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "Scope" / WString,
        "ContextName" / WString,
        "InterfaceId" / WString,
        "FunctionName" / WString,
        "PropertyName" / WString,
        "OldValue" / WString,
        "NewValue" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5071, version=0)
class Microsoft_Windows_Security_Auditing_5071_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "SecurityDescriptor" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5122, version=0)
class Microsoft_Windows_Security_Auditing_5122_0(Etw):
    pattern = Struct(
        "CAConfigurationId" / WString,
        "NewValue" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5123, version=0)
class Microsoft_Windows_Security_Auditing_5123_0(Etw):
    pattern = Struct(
        "PropertyName" / WString,
        "NewValue" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5124, version=0)
class Microsoft_Windows_Security_Auditing_5124_0(Etw):
    pattern = Struct(
        "NewSecuritySettings" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5125, version=0)
class Microsoft_Windows_Security_Auditing_5125_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5125, version=1)
class Microsoft_Windows_Security_Auditing_5125_1(Etw):
    pattern = Struct(
        "SerialNumber" / WString,
        "CAName" / WString,
        "Status" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5126, version=0)
class Microsoft_Windows_Security_Auditing_5126_0(Etw):
    pattern = Struct(
        "CAConfigurationId" / WString,
        "NewSigningCertificateHash" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5127, version=0)
class Microsoft_Windows_Security_Auditing_5127_0(Etw):
    pattern = Struct(
        "CAConfigurationId" / WString,
        "BaseCRLNumber" / WString,
        "BaseCRLThisUpdate" / WString,
        "BaseCRLHash" / WString,
        "DeltaCRLNumber" / WString,
        "DeltaCRLIndicator" / WString,
        "DeltaCRLThisUpdate" / WString,
        "DeltaCRLHash" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5136, version=0)
class Microsoft_Windows_Security_Auditing_5136_0(Etw):
    pattern = Struct(
        "OpCorrelationID" / Guid,
        "AppCorrelationID" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "DSName" / WString,
        "DSType" / WString,
        "ObjectDN" / WString,
        "ObjectGUID" / Guid,
        "ObjectClass" / WString,
        "AttributeLDAPDisplayName" / WString,
        "AttributeSyntaxOID" / WString,
        "AttributeValue" / WString,
        "OperationType" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5137, version=0)
class Microsoft_Windows_Security_Auditing_5137_0(Etw):
    pattern = Struct(
        "OpCorrelationID" / Guid,
        "AppCorrelationID" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "DSName" / WString,
        "DSType" / WString,
        "ObjectDN" / WString,
        "ObjectGUID" / Guid,
        "ObjectClass" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5138, version=0)
class Microsoft_Windows_Security_Auditing_5138_0(Etw):
    pattern = Struct(
        "OpCorrelationID" / Guid,
        "AppCorrelationID" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "DSName" / WString,
        "DSType" / WString,
        "OldObjectDN" / WString,
        "NewObjectDN" / WString,
        "ObjectGUID" / Guid,
        "ObjectClass" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5139, version=0)
class Microsoft_Windows_Security_Auditing_5139_0(Etw):
    pattern = Struct(
        "OpCorrelationID" / Guid,
        "AppCorrelationID" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "DSName" / WString,
        "DSType" / WString,
        "OldObjectDN" / WString,
        "NewObjectDN" / WString,
        "ObjectGUID" / Guid,
        "ObjectClass" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5140, version=0)
class Microsoft_Windows_Security_Auditing_5140_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "IpAddress" / WString,
        "IpPort" / WString,
        "ShareName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5140, version=1)
class Microsoft_Windows_Security_Auditing_5140_1(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectType" / WString,
        "IpAddress" / WString,
        "IpPort" / WString,
        "ShareName" / WString,
        "ShareLocalPath" / WString,
        "AccessMask" / Int32ul,
        "AccessList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5141, version=0)
class Microsoft_Windows_Security_Auditing_5141_0(Etw):
    pattern = Struct(
        "OpCorrelationID" / Guid,
        "AppCorrelationID" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "DSName" / WString,
        "DSType" / WString,
        "ObjectDN" / WString,
        "ObjectGUID" / Guid,
        "ObjectClass" / WString,
        "TreeDelete" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5142, version=0)
class Microsoft_Windows_Security_Auditing_5142_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ShareName" / WString,
        "ShareLocalPath" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5143, version=0)
class Microsoft_Windows_Security_Auditing_5143_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectType" / WString,
        "ShareName" / WString,
        "ShareLocalPath" / WString,
        "OldRemark" / WString,
        "NewRemark" / WString,
        "OldMaxUsers" / Int32ul,
        "NewMaxUsers" / Int32ul,
        "OldShareFlags" / Int32ul,
        "NewShareFlags" / Int32ul,
        "OldSD" / WString,
        "NewSD" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5144, version=0)
class Microsoft_Windows_Security_Auditing_5144_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ShareName" / WString,
        "ShareLocalPath" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5145, version=0)
class Microsoft_Windows_Security_Auditing_5145_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectType" / WString,
        "IpAddress" / WString,
        "IpPort" / WString,
        "ShareName" / WString,
        "ShareLocalPath" / WString,
        "RelativeTargetName" / WString,
        "AccessMask" / Int32ul,
        "AccessList" / WString,
        "AccessReason" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5146, version=0)
class Microsoft_Windows_Security_Auditing_5146_0(Etw):
    pattern = Struct(
        "Direction" / WString,
        "SourceAddress" / WString,
        "DestAddress" / WString,
        "EtherType" / Int32ul,
        "VlanTag" / Int32ul,
        "vSwitchID" / WString,
        "SourcevSwitchPort" / Int32ul,
        "DestinationvSwitchPort" / Int32ul,
        "FilterRTID" / Int64ul,
        "LayerName" / WString,
        "LayerRTID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5147, version=0)
class Microsoft_Windows_Security_Auditing_5147_0(Etw):
    pattern = Struct(
        "Direction" / WString,
        "SourceAddress" / WString,
        "DestAddress" / WString,
        "EtherType" / Int32ul,
        "VlanTag" / Int32ul,
        "vSwitchID" / WString,
        "SourcevSwitchPort" / Int32ul,
        "DestinationvSwitchPort" / Int32ul,
        "FilterRTID" / Int64ul,
        "LayerName" / WString,
        "LayerRTID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5148, version=0)
class Microsoft_Windows_Security_Auditing_5148_0(Etw):
    pattern = Struct(
        "Type" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5149, version=0)
class Microsoft_Windows_Security_Auditing_5149_0(Etw):
    pattern = Struct(
        "Type" / WString,
        "PacketsDiscarded" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5150, version=0)
class Microsoft_Windows_Security_Auditing_5150_0(Etw):
    pattern = Struct(
        "Direction" / WString,
        "SourceAddress" / WString,
        "DestAddress" / WString,
        "EtherType" / Int32ul,
        "MediaType" / Int32ul,
        "InterfaceType" / Int32ul,
        "VlanTag" / Int32ul,
        "FilterRTID" / Int64ul,
        "LayerName" / WString,
        "LayerRTID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5151, version=0)
class Microsoft_Windows_Security_Auditing_5151_0(Etw):
    pattern = Struct(
        "Direction" / WString,
        "SourceAddress" / WString,
        "DestAddress" / WString,
        "EtherType" / Int32ul,
        "MediaType" / Int32ul,
        "InterfaceType" / Int32ul,
        "VlanTag" / Int32ul,
        "FilterRTID" / Int64ul,
        "LayerName" / WString,
        "LayerRTID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5152, version=0)
class Microsoft_Windows_Security_Auditing_5152_0(Etw):
    pattern = Struct(
        "ProcessId" / Int64ul,
        "Application" / WString,
        "Direction" / WString,
        "SourceAddress" / WString,
        "SourcePort" / WString,
        "DestAddress" / WString,
        "DestPort" / WString,
        "Protocol" / Int32ul,
        "FilterRTID" / Int64ul,
        "LayerName" / WString,
        "LayerRTID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5153, version=0)
class Microsoft_Windows_Security_Auditing_5153_0(Etw):
    pattern = Struct(
        "ProcessId" / Int64ul,
        "Application" / WString,
        "Direction" / WString,
        "SourceAddress" / WString,
        "SourcePort" / WString,
        "DestAddress" / WString,
        "DestPort" / WString,
        "Protocol" / Int32ul,
        "FilterRTID" / Int64ul,
        "LayerName" / WString,
        "LayerRTID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5154, version=0)
class Microsoft_Windows_Security_Auditing_5154_0(Etw):
    pattern = Struct(
        "ProcessId" / Int64ul,
        "Application" / WString,
        "SourceAddress" / WString,
        "SourcePort" / WString,
        "Protocol" / Int32ul,
        "FilterRTID" / Int64ul,
        "LayerName" / WString,
        "LayerRTID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5155, version=0)
class Microsoft_Windows_Security_Auditing_5155_0(Etw):
    pattern = Struct(
        "ProcessId" / Int64ul,
        "Application" / WString,
        "SourceAddress" / WString,
        "SourcePort" / WString,
        "Protocol" / Int32ul,
        "FilterRTID" / Int64ul,
        "LayerName" / WString,
        "LayerRTID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5156, version=0)
class Microsoft_Windows_Security_Auditing_5156_0(Etw):
    pattern = Struct(
        "ProcessID" / Int64ul,
        "Application" / WString,
        "Direction" / WString,
        "SourceAddress" / WString,
        "SourcePort" / WString,
        "DestAddress" / WString,
        "DestPort" / WString,
        "Protocol" / Int32ul,
        "FilterRTID" / Int64ul,
        "LayerName" / WString,
        "LayerRTID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5156, version=1)
class Microsoft_Windows_Security_Auditing_5156_1(Etw):
    pattern = Struct(
        "ProcessID" / Int64ul,
        "Application" / WString,
        "Direction" / WString,
        "SourceAddress" / WString,
        "SourcePort" / WString,
        "DestAddress" / WString,
        "DestPort" / WString,
        "Protocol" / Int32ul,
        "FilterRTID" / Int64ul,
        "LayerName" / WString,
        "LayerRTID" / Int64ul,
        "RemoteUserID" / Sid,
        "RemoteMachineID" / Sid
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5157, version=0)
class Microsoft_Windows_Security_Auditing_5157_0(Etw):
    pattern = Struct(
        "ProcessID" / Int64ul,
        "Application" / WString,
        "Direction" / WString,
        "SourceAddress" / WString,
        "SourcePort" / WString,
        "DestAddress" / WString,
        "DestPort" / WString,
        "Protocol" / Int32ul,
        "FilterRTID" / Int64ul,
        "LayerName" / WString,
        "LayerRTID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5157, version=1)
class Microsoft_Windows_Security_Auditing_5157_1(Etw):
    pattern = Struct(
        "ProcessID" / Int64ul,
        "Application" / WString,
        "Direction" / WString,
        "SourceAddress" / WString,
        "SourcePort" / WString,
        "DestAddress" / WString,
        "DestPort" / WString,
        "Protocol" / Int32ul,
        "FilterRTID" / Int64ul,
        "LayerName" / WString,
        "LayerRTID" / Int64ul,
        "RemoteUserID" / Sid,
        "RemoteMachineID" / Sid
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5158, version=0)
class Microsoft_Windows_Security_Auditing_5158_0(Etw):
    pattern = Struct(
        "ProcessId" / Int64ul,
        "Application" / WString,
        "SourceAddress" / WString,
        "SourcePort" / WString,
        "Protocol" / Int32ul,
        "FilterRTID" / Int64ul,
        "LayerName" / WString,
        "LayerRTID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5159, version=0)
class Microsoft_Windows_Security_Auditing_5159_0(Etw):
    pattern = Struct(
        "ProcessId" / Int64ul,
        "Application" / WString,
        "SourceAddress" / WString,
        "SourcePort" / WString,
        "Protocol" / Int32ul,
        "FilterRTID" / Int64ul,
        "LayerName" / WString,
        "LayerRTID" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5168, version=0)
class Microsoft_Windows_Security_Auditing_5168_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "SpnName" / WString,
        "ErrorCode" / Int32ul,
        "ServerNames" / WString,
        "ConfiguredNames" / WString,
        "IpAddresses" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5169, version=0)
class Microsoft_Windows_Security_Auditing_5169_0(Etw):
    pattern = Struct(
        "OpCorrelationID" / Guid,
        "AppCorrelationID" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "DSName" / WString,
        "DSType" / WString,
        "ObjectDN" / WString,
        "ObjectGUID" / Guid,
        "ObjectClass" / WString,
        "AttributeLDAPDisplayName" / WString,
        "AttributeSyntaxOID" / WString,
        "AttributeValue" / WString,
        "ExpirationTime" / Int64ul,
        "OperationType" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5170, version=0)
class Microsoft_Windows_Security_Auditing_5170_0(Etw):
    pattern = Struct(
        "OpCorrelationID" / Guid,
        "AppCorrelationID" / WString,
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "DSName" / WString,
        "DSType" / WString,
        "ObjectDN" / WString,
        "ObjectGUID" / Guid,
        "ObjectClass" / WString,
        "AttributeLDAPDisplayName" / WString,
        "AttributeSyntaxOID" / WString,
        "AttributeValue" / WString,
        "ExpirationTime" / Int64ul,
        "OperationType" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5376, version=0)
class Microsoft_Windows_Security_Auditing_5376_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5376, version=1)
class Microsoft_Windows_Security_Auditing_5376_1(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "BackupFileName" / WString,
        "ProcessCreationTime" / Int64ul,
        "ClientProcessId" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5377, version=0)
class Microsoft_Windows_Security_Auditing_5377_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5377, version=1)
class Microsoft_Windows_Security_Auditing_5377_1(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "BackupFileName" / WString,
        "ProcessCreationTime" / Int64ul,
        "ClientProcessId" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5378, version=0)
class Microsoft_Windows_Security_Auditing_5378_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "Package" / WString,
        "UserUPN" / WString,
        "TargetServer" / WString,
        "CredType" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5379, version=0)
class Microsoft_Windows_Security_Auditing_5379_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "TargetName" / WString,
        "Type" / Int32ul,
        "CountOfCredentialsReturned" / Int32ul,
        "ReadOperation" / WString,
        "ReturnCode" / Int32ul,
        "ProcessCreationTime" / Int64ul,
        "ClientProcessId" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5380, version=0)
class Microsoft_Windows_Security_Auditing_5380_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "SearchString" / WString,
        "SchemaFriendlyName" / WString,
        "Schema" / Guid,
        "CountOfCredentialsReturned" / Int32ul,
        "ProcessCreationTime" / Int64ul,
        "ClientProcessId" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5381, version=0)
class Microsoft_Windows_Security_Auditing_5381_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "Flags" / Int32ul,
        "CountOfCredentialsReturned" / Int32ul,
        "ProcessCreationTime" / Int64ul,
        "ClientProcessId" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5382, version=0)
class Microsoft_Windows_Security_Auditing_5382_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "SchemaFriendlyName" / WString,
        "Schema" / Guid,
        "Resource" / WString,
        "Identity" / WString,
        "PackageSid" / WString,
        "Flags" / Int32ul,
        "ReturnCode" / Int32ul,
        "ProcessCreationTime" / Int64ul,
        "ClientProcessId" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5440, version=0)
class Microsoft_Windows_Security_Auditing_5440_0(Etw):
    pattern = Struct(
        "ProviderKey" / Guid,
        "ProviderName" / WString,
        "CalloutKey" / Guid,
        "CalloutName" / WString,
        "CalloutType" / WString,
        "CalloutId" / Int32ul,
        "LayerKey" / Guid,
        "LayerName" / WString,
        "LayerId" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5441, version=0)
class Microsoft_Windows_Security_Auditing_5441_0(Etw):
    pattern = Struct(
        "ProviderKey" / Guid,
        "ProviderName" / WString,
        "FilterKey" / Guid,
        "FilterName" / WString,
        "FilterType" / WString,
        "FilterId" / Int64ul,
        "LayerKey" / Guid,
        "LayerName" / WString,
        "LayerId" / Int32ul,
        "Weight" / Int64ul,
        "Conditions" / WString,
        "Action" / WString,
        "CalloutKey" / Guid,
        "CalloutName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5442, version=0)
class Microsoft_Windows_Security_Auditing_5442_0(Etw):
    pattern = Struct(
        "ProviderKey" / Guid,
        "ProviderName" / WString,
        "ProviderType" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5443, version=0)
class Microsoft_Windows_Security_Auditing_5443_0(Etw):
    pattern = Struct(
        "ProviderKey" / Guid,
        "ProviderName" / WString,
        "ProviderContextKey" / Guid,
        "ProviderContextName" / WString,
        "ProviderContextType" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5444, version=0)
class Microsoft_Windows_Security_Auditing_5444_0(Etw):
    pattern = Struct(
        "ProviderKey" / Guid,
        "ProviderName" / WString,
        "SubLayerKey" / Guid,
        "SubLayerName" / WString,
        "SubLayerType" / WString,
        "Weight" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5446, version=0)
class Microsoft_Windows_Security_Auditing_5446_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "UserSid" / Sid,
        "UserName" / WString,
        "ProviderKey" / Guid,
        "ProviderName" / WString,
        "ChangeType" / WString,
        "CalloutKey" / Guid,
        "CalloutName" / WString,
        "CalloutType" / WString,
        "CalloutId" / Int32ul,
        "LayerKey" / Guid,
        "LayerName" / WString,
        "LayerId" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5447, version=0)
class Microsoft_Windows_Security_Auditing_5447_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "UserSid" / Sid,
        "UserName" / WString,
        "ProviderKey" / Guid,
        "ProviderName" / WString,
        "ChangeType" / WString,
        "FilterKey" / Guid,
        "FilterName" / WString,
        "FilterType" / WString,
        "FilterId" / Int64ul,
        "LayerKey" / Guid,
        "LayerName" / WString,
        "LayerId" / Int32ul,
        "Weight" / Int64ul,
        "Conditions" / WString,
        "Action" / WString,
        "CalloutKey" / Guid,
        "CalloutName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5448, version=0)
class Microsoft_Windows_Security_Auditing_5448_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "UserSid" / Sid,
        "UserName" / WString,
        "ChangeType" / WString,
        "ProviderKey" / Guid,
        "ProviderName" / WString,
        "ProviderType" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5449, version=0)
class Microsoft_Windows_Security_Auditing_5449_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "UserSid" / Sid,
        "UserName" / WString,
        "ProviderKey" / Guid,
        "ProviderName" / WString,
        "ChangeType" / WString,
        "ProviderContextKey" / Guid,
        "ProviderContextName" / WString,
        "ProviderContextType" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5450, version=0)
class Microsoft_Windows_Security_Auditing_5450_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "UserSid" / Sid,
        "UserName" / WString,
        "ProviderKey" / Guid,
        "ProviderName" / WString,
        "ChangeType" / WString,
        "SubLayerKey" / Guid,
        "SubLayerName" / WString,
        "SubLayerType" / WString,
        "Weight" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5451, version=0)
class Microsoft_Windows_Security_Auditing_5451_0(Etw):
    pattern = Struct(
        "LocalAddress" / WString,
        "LocalAddressMask" / WString,
        "LocalPort" / Int32ul,
        "LocalTunnelEndpoint" / WString,
        "RemoteAddress" / WString,
        "RemoteAddressMask" / WString,
        "RemotePort" / Int32ul,
        "PeerPrivateAddress" / WString,
        "RemoteTunnelEndpoint" / WString,
        "IpProtocol" / Int32ul,
        "KeyingModuleName" / WString,
        "AhAuthType" / WString,
        "EspAuthType" / WString,
        "CipherType" / WString,
        "LifetimeSeconds" / Int32ul,
        "LifetimeKilobytes" / Int32ul,
        "LifetimePackets" / Int32ul,
        "Mode" / WString,
        "Role" / WString,
        "TransportFilterId" / Int64ul,
        "MainModeSaId" / Int64ul,
        "QuickModeSaId" / Int64ul,
        "InboundSpi" / Int64ul,
        "OutboundSpi" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5451, version=1)
class Microsoft_Windows_Security_Auditing_5451_1(Etw):
    pattern = Struct(
        "LocalAddress" / WString,
        "LocalAddressMask" / WString,
        "LocalPort" / Int32ul,
        "LocalTunnelEndpoint" / WString,
        "RemoteAddress" / WString,
        "RemoteAddressMask" / WString,
        "RemotePort" / Int32ul,
        "PeerPrivateAddress" / WString,
        "RemoteTunnelEndpoint" / WString,
        "IpProtocol" / Int32ul,
        "KeyingModuleName" / WString,
        "AhAuthType" / WString,
        "EspAuthType" / WString,
        "CipherType" / WString,
        "LifetimeSeconds" / Int32ul,
        "LifetimeKilobytes" / Int32ul,
        "LifetimePackets" / Int32ul,
        "Mode" / WString,
        "Role" / WString,
        "TransportFilterId" / Int64ul,
        "MainModeSaId" / Int64ul,
        "QuickModeSaId" / Int64ul,
        "InboundSpi" / Int64ul,
        "OutboundSpi" / Int64ul,
        "TunnelId" / Int64ul,
        "TrafficSelectorId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5452, version=0)
class Microsoft_Windows_Security_Auditing_5452_0(Etw):
    pattern = Struct(
        "LocalAddress" / WString,
        "LocalPort" / Int32ul,
        "LocalTunnelEndpoint" / WString,
        "RemoteAddress" / WString,
        "RemotePort" / Int32ul,
        "RemoteTunnelEndpoint" / WString,
        "IpProtocol" / Int32ul,
        "QuickModeSaId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5452, version=1)
class Microsoft_Windows_Security_Auditing_5452_1(Etw):
    pattern = Struct(
        "LocalAddress" / WString,
        "LocalAddressMask" / WString,
        "LocalPort" / Int32ul,
        "LocalTunnelEndpoint" / WString,
        "RemoteAddress" / WString,
        "RemoteAddressMask" / WString,
        "RemotePort" / Int32ul,
        "RemoteTunnelEndpoint" / WString,
        "IpProtocol" / Int32ul,
        "QuickModeSaId" / Int64ul,
        "TunnelId" / Int64ul,
        "TrafficSelectorId" / Int64ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5456, version=0)
class Microsoft_Windows_Security_Auditing_5456_0(Etw):
    pattern = Struct(
        "Policy" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5457, version=0)
class Microsoft_Windows_Security_Auditing_5457_0(Etw):
    pattern = Struct(
        "Policy" / WString,
        "Error" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5458, version=0)
class Microsoft_Windows_Security_Auditing_5458_0(Etw):
    pattern = Struct(
        "Policy" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5459, version=0)
class Microsoft_Windows_Security_Auditing_5459_0(Etw):
    pattern = Struct(
        "Policy" / WString,
        "Error" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5460, version=0)
class Microsoft_Windows_Security_Auditing_5460_0(Etw):
    pattern = Struct(
        "Policy" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5461, version=0)
class Microsoft_Windows_Security_Auditing_5461_0(Etw):
    pattern = Struct(
        "Policy" / WString,
        "Error" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5462, version=0)
class Microsoft_Windows_Security_Auditing_5462_0(Etw):
    pattern = Struct(
        "Policy" / WString,
        "Error" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5471, version=0)
class Microsoft_Windows_Security_Auditing_5471_0(Etw):
    pattern = Struct(
        "Policy" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5472, version=0)
class Microsoft_Windows_Security_Auditing_5472_0(Etw):
    pattern = Struct(
        "Policy" / WString,
        "Error" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5473, version=0)
class Microsoft_Windows_Security_Auditing_5473_0(Etw):
    pattern = Struct(
        "Policy" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5474, version=0)
class Microsoft_Windows_Security_Auditing_5474_0(Etw):
    pattern = Struct(
        "Policy" / WString,
        "Error" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5477, version=0)
class Microsoft_Windows_Security_Auditing_5477_0(Etw):
    pattern = Struct(
        "QuickModeFilter" / WString,
        "Error" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5483, version=0)
class Microsoft_Windows_Security_Auditing_5483_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5484, version=0)
class Microsoft_Windows_Security_Auditing_5484_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5632, version=0)
class Microsoft_Windows_Security_Auditing_5632_0(Etw):
    pattern = Struct(
        "SSID" / WString,
        "Identity" / WString,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PeerMac" / WString,
        "LocalMac" / WString,
        "IntfGuid" / Guid,
        "ReasonCode" / Int32ul,
        "ReasonText" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5632, version=1)
class Microsoft_Windows_Security_Auditing_5632_1(Etw):
    pattern = Struct(
        "SSID" / WString,
        "Identity" / WString,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "PeerMac" / WString,
        "LocalMac" / WString,
        "IntfGuid" / Guid,
        "ReasonCode" / Int32ul,
        "ReasonText" / WString,
        "ErrorCode" / Int32ul,
        "EAPReasonCode" / Int32ul,
        "EapRootCauseString" / WString,
        "EAPErrorCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5633, version=0)
class Microsoft_Windows_Security_Auditing_5633_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "Identity" / WString,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ReasonCode" / Int32ul,
        "ReasonText" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5712, version=0)
class Microsoft_Windows_Security_Auditing_5712_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessName" / WString,
        "RemoteIpAddress" / WString,
        "RemotePort" / WString,
        "InterfaceUuid" / Guid,
        "ProtocolSequence" / WString,
        "AuthenticationService" / Int32ul,
        "AuthenticationLevel" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5888, version=0)
class Microsoft_Windows_Security_Auditing_5888_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectUserDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectCollectionName" / WString,
        "ObjectIdentifyingProperties" / WString,
        "ModifiedObjectProperties" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5889, version=0)
class Microsoft_Windows_Security_Auditing_5889_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectUserDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectCollectionName" / WString,
        "ObjectIdentifyingProperties" / WString,
        "ObjectProperties" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=5890, version=0)
class Microsoft_Windows_Security_Auditing_5890_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectUserDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ObjectCollectionName" / WString,
        "ObjectIdentifyingProperties" / WString,
        "ObjectProperties" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6144, version=0)
class Microsoft_Windows_Security_Auditing_6144_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "GPOList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6145, version=0)
class Microsoft_Windows_Security_Auditing_6145_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "GPOList" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6272, version=0)
class Microsoft_Windows_Security_Auditing_6272_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "FullyQualifiedSubjectUserName" / WString,
        "SubjectMachineSID" / Sid,
        "SubjectMachineName" / WString,
        "FullyQualifiedSubjectMachineName" / WString,
        "MachineInventory" / WString,
        "CalledStationID" / WString,
        "CallingStationID" / WString,
        "NASIPv4Address" / WString,
        "NASIPv6Address" / WString,
        "NASIdentifier" / WString,
        "NASPortType" / WString,
        "NASPort" / WString,
        "ClientName" / WString,
        "ClientIPAddress" / WString,
        "ProxyPolicyName" / WString,
        "NetworkPolicyName" / WString,
        "AuthenticationProvider" / WString,
        "AuthenticationServer" / WString,
        "AuthenticationType" / WString,
        "EAPType" / WString,
        "AccountSessionIdentifier" / WString,
        "QuarantineState" / WString,
        "QuarantineSessionIdentifier" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6272, version=1)
class Microsoft_Windows_Security_Auditing_6272_1(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "FullyQualifiedSubjectUserName" / WString,
        "SubjectMachineSID" / Sid,
        "SubjectMachineName" / WString,
        "FullyQualifiedSubjectMachineName" / WString,
        "MachineInventory" / WString,
        "CalledStationID" / WString,
        "CallingStationID" / WString,
        "NASIPv4Address" / WString,
        "NASIPv6Address" / WString,
        "NASIdentifier" / WString,
        "NASPortType" / WString,
        "NASPort" / WString,
        "ClientName" / WString,
        "ClientIPAddress" / WString,
        "ProxyPolicyName" / WString,
        "NetworkPolicyName" / WString,
        "AuthenticationProvider" / WString,
        "AuthenticationServer" / WString,
        "AuthenticationType" / WString,
        "EAPType" / WString,
        "AccountSessionIdentifier" / WString,
        "QuarantineState" / WString,
        "QuarantineSessionIdentifier" / WString,
        "LoggingResult" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6272, version=2)
class Microsoft_Windows_Security_Auditing_6272_2(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "FullyQualifiedSubjectUserName" / WString,
        "SubjectMachineSID" / Sid,
        "SubjectMachineName" / WString,
        "FullyQualifiedSubjectMachineName" / WString,
        "CalledStationID" / WString,
        "CallingStationID" / WString,
        "NASIPv4Address" / WString,
        "NASIPv6Address" / WString,
        "NASIdentifier" / WString,
        "NASPortType" / WString,
        "NASPort" / WString,
        "ClientName" / WString,
        "ClientIPAddress" / WString,
        "ProxyPolicyName" / WString,
        "NetworkPolicyName" / WString,
        "AuthenticationProvider" / WString,
        "AuthenticationServer" / WString,
        "AuthenticationType" / WString,
        "EAPType" / WString,
        "AccountSessionIdentifier" / WString,
        "LoggingResult" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6273, version=0)
class Microsoft_Windows_Security_Auditing_6273_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "FullyQualifiedSubjectUserName" / WString,
        "SubjectMachineSID" / Sid,
        "SubjectMachineName" / WString,
        "FullyQualifiedSubjectMachineName" / WString,
        "MachineInventory" / WString,
        "CalledStationID" / WString,
        "CallingStationID" / WString,
        "NASIPv4Address" / WString,
        "NASIPv6Address" / WString,
        "NASIdentifier" / WString,
        "NASPortType" / WString,
        "NASPort" / WString,
        "ClientName" / WString,
        "ClientIPAddress" / WString,
        "ProxyPolicyName" / WString,
        "NetworkPolicyName" / WString,
        "AuthenticationProvider" / WString,
        "AuthenticationServer" / WString,
        "AuthenticationType" / WString,
        "EAPType" / WString,
        "AccountSessionIdentifier" / WString,
        "ReasonCode" / WString,
        "Reason" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6273, version=1)
class Microsoft_Windows_Security_Auditing_6273_1(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "FullyQualifiedSubjectUserName" / WString,
        "SubjectMachineSID" / Sid,
        "SubjectMachineName" / WString,
        "FullyQualifiedSubjectMachineName" / WString,
        "MachineInventory" / WString,
        "CalledStationID" / WString,
        "CallingStationID" / WString,
        "NASIPv4Address" / WString,
        "NASIPv6Address" / WString,
        "NASIdentifier" / WString,
        "NASPortType" / WString,
        "NASPort" / WString,
        "ClientName" / WString,
        "ClientIPAddress" / WString,
        "ProxyPolicyName" / WString,
        "NetworkPolicyName" / WString,
        "AuthenticationProvider" / WString,
        "AuthenticationServer" / WString,
        "AuthenticationType" / WString,
        "EAPType" / WString,
        "AccountSessionIdentifier" / WString,
        "ReasonCode" / WString,
        "Reason" / WString,
        "LoggingResult" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6273, version=2)
class Microsoft_Windows_Security_Auditing_6273_2(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "FullyQualifiedSubjectUserName" / WString,
        "SubjectMachineSID" / Sid,
        "SubjectMachineName" / WString,
        "FullyQualifiedSubjectMachineName" / WString,
        "CalledStationID" / WString,
        "CallingStationID" / WString,
        "NASIPv4Address" / WString,
        "NASIPv6Address" / WString,
        "NASIdentifier" / WString,
        "NASPortType" / WString,
        "NASPort" / WString,
        "ClientName" / WString,
        "ClientIPAddress" / WString,
        "ProxyPolicyName" / WString,
        "NetworkPolicyName" / WString,
        "AuthenticationProvider" / WString,
        "AuthenticationServer" / WString,
        "AuthenticationType" / WString,
        "EAPType" / WString,
        "AccountSessionIdentifier" / WString,
        "ReasonCode" / WString,
        "Reason" / WString,
        "LoggingResult" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6274, version=0)
class Microsoft_Windows_Security_Auditing_6274_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "FullyQualifiedSubjectUserName" / WString,
        "SubjectMachineSID" / Sid,
        "SubjectMachineName" / WString,
        "FullyQualifiedSubjectMachineName" / WString,
        "MachineInventory" / WString,
        "CalledStationID" / WString,
        "CallingStationID" / WString,
        "NASIPv4Address" / WString,
        "NASIPv6Address" / WString,
        "NASIdentifier" / WString,
        "NASPortType" / WString,
        "NASPort" / WString,
        "ClientName" / WString,
        "ClientIPAddress" / WString,
        "ProxyPolicyName" / WString,
        "NetworkPolicyName" / WString,
        "AuthenticationProvider" / WString,
        "AuthenticationServer" / WString,
        "AuthenticationType" / WString,
        "EAPType" / WString,
        "AccountSessionIdentifier" / WString,
        "ReasonCode" / WString,
        "Reason" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6274, version=1)
class Microsoft_Windows_Security_Auditing_6274_1(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "FullyQualifiedSubjectUserName" / WString,
        "SubjectMachineSID" / Sid,
        "SubjectMachineName" / WString,
        "FullyQualifiedSubjectMachineName" / WString,
        "CalledStationID" / WString,
        "CallingStationID" / WString,
        "NASIPv4Address" / WString,
        "NASIPv6Address" / WString,
        "NASIdentifier" / WString,
        "NASPortType" / WString,
        "NASPort" / WString,
        "ClientName" / WString,
        "ClientIPAddress" / WString,
        "ProxyPolicyName" / WString,
        "NetworkPolicyName" / WString,
        "AuthenticationProvider" / WString,
        "AuthenticationServer" / WString,
        "AuthenticationType" / WString,
        "EAPType" / WString,
        "AccountSessionIdentifier" / WString,
        "ReasonCode" / WString,
        "Reason" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6275, version=0)
class Microsoft_Windows_Security_Auditing_6275_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "FullyQualifiedSubjectUserName" / WString,
        "SubjectMachineSID" / Sid,
        "SubjectMachineName" / WString,
        "FullyQualifiedSubjectMachineName" / WString,
        "MachineInventory" / WString,
        "CalledStationID" / WString,
        "CallingStationID" / WString,
        "NASIPv4Address" / WString,
        "NASIPv6Address" / WString,
        "NASIdentifier" / WString,
        "NASPortType" / WString,
        "NASPort" / WString,
        "ClientName" / WString,
        "ClientIPAddress" / WString,
        "ProxyPolicyName" / WString,
        "NetworkPolicyName" / WString,
        "AuthenticationProvider" / WString,
        "AuthenticationServer" / WString,
        "AuthenticationType" / WString,
        "EAPType" / WString,
        "AccountSessionIdentifier" / WString,
        "ReasonCode" / WString,
        "Reason" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6275, version=1)
class Microsoft_Windows_Security_Auditing_6275_1(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "FullyQualifiedSubjectUserName" / WString,
        "SubjectMachineSID" / Sid,
        "SubjectMachineName" / WString,
        "FullyQualifiedSubjectMachineName" / WString,
        "CalledStationID" / WString,
        "CallingStationID" / WString,
        "NASIPv4Address" / WString,
        "NASIPv6Address" / WString,
        "NASIdentifier" / WString,
        "NASPortType" / WString,
        "NASPort" / WString,
        "ClientName" / WString,
        "ClientIPAddress" / WString,
        "ProxyPolicyName" / WString,
        "NetworkPolicyName" / WString,
        "AuthenticationProvider" / WString,
        "AuthenticationServer" / WString,
        "AuthenticationType" / WString,
        "EAPType" / WString,
        "AccountSessionIdentifier" / WString,
        "ReasonCode" / WString,
        "Reason" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6276, version=0)
class Microsoft_Windows_Security_Auditing_6276_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "FullyQualifiedSubjectUserName" / WString,
        "SubjectMachineSID" / Sid,
        "SubjectMachineName" / WString,
        "FullyQualifiedSubjectMachineName" / WString,
        "MachineInventory" / WString,
        "CalledStationID" / WString,
        "CallingStationID" / WString,
        "NASIPv4Address" / WString,
        "NASIPv6Address" / WString,
        "NASIdentifier" / WString,
        "NASPortType" / WString,
        "NASPort" / WString,
        "ClientName" / WString,
        "ClientIPAddress" / WString,
        "ProxyPolicyName" / WString,
        "NetworkPolicyName" / WString,
        "AuthenticationProvider" / WString,
        "AuthenticationServer" / WString,
        "AuthenticationType" / WString,
        "EAPType" / WString,
        "AccountSessionIdentifier" / WString,
        "QuarantineState" / WString,
        "ExtendedQuarantineState" / WString,
        "QuarantineSessionID" / WString,
        "QuarantineHelpURL" / WString,
        "QuarantineSystemHealthResult" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6277, version=0)
class Microsoft_Windows_Security_Auditing_6277_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "FullyQualifiedSubjectUserName" / WString,
        "SubjectMachineSID" / Sid,
        "SubjectMachineName" / WString,
        "FullyQualifiedSubjectMachineName" / WString,
        "MachineInventory" / WString,
        "CalledStationID" / WString,
        "CallingStationID" / WString,
        "NASIPv4Address" / WString,
        "NASIPv6Address" / WString,
        "NASIdentifier" / WString,
        "NASPortType" / WString,
        "NASPort" / WString,
        "ClientName" / WString,
        "ClientIPAddress" / WString,
        "ProxyPolicyName" / WString,
        "NetworkPolicyName" / WString,
        "AuthenticationProvider" / WString,
        "AuthenticationServer" / WString,
        "AuthenticationType" / WString,
        "EAPType" / WString,
        "AccountSessionIdentifier" / WString,
        "QuarantineState" / WString,
        "ExtendedQuarantineState" / WString,
        "QuarantineSessionID" / WString,
        "QuarantineHelpURL" / WString,
        "QuarantineSystemHealthResult" / WString,
        "QuarantineGraceTime" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6278, version=0)
class Microsoft_Windows_Security_Auditing_6278_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "FullyQualifiedSubjectUserName" / WString,
        "SubjectMachineSID" / Sid,
        "SubjectMachineName" / WString,
        "FullyQualifiedSubjectMachineName" / WString,
        "MachineInventory" / WString,
        "CalledStationID" / WString,
        "CallingStationID" / WString,
        "NASIPv4Address" / WString,
        "NASIPv6Address" / WString,
        "NASIdentifier" / WString,
        "NASPortType" / WString,
        "NASPort" / WString,
        "ClientName" / WString,
        "ClientIPAddress" / WString,
        "ProxyPolicyName" / WString,
        "NetworkPolicyName" / WString,
        "AuthenticationProvider" / WString,
        "AuthenticationServer" / WString,
        "AuthenticationType" / WString,
        "EAPType" / WString,
        "AccountSessionIdentifier" / WString,
        "QuarantineState" / WString,
        "ExtendedQuarantineState" / WString,
        "QuarantineSessionID" / WString,
        "QuarantineHelpURL" / WString,
        "QuarantineSystemHealthResult" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6279, version=0)
class Microsoft_Windows_Security_Auditing_6279_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "FullyQualifiedSubjectUserName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6280, version=0)
class Microsoft_Windows_Security_Auditing_6280_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "FullyQualifiedSubjectUserName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6281, version=0)
class Microsoft_Windows_Security_Auditing_6281_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6400, version=0)
class Microsoft_Windows_Security_Auditing_6400_0(Etw):
    pattern = Struct(
        "ClientIPAddress" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6401, version=0)
class Microsoft_Windows_Security_Auditing_6401_0(Etw):
    pattern = Struct(
        "ClientIPAddress" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6402, version=0)
class Microsoft_Windows_Security_Auditing_6402_0(Etw):
    pattern = Struct(
        "ClientIPAddress" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6403, version=0)
class Microsoft_Windows_Security_Auditing_6403_0(Etw):
    pattern = Struct(
        "HostedCacheName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6404, version=0)
class Microsoft_Windows_Security_Auditing_6404_0(Etw):
    pattern = Struct(
        "HostedCacheName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6405, version=0)
class Microsoft_Windows_Security_Auditing_6405_0(Etw):
    pattern = Struct(
        "EventId" / Int32ul,
        "Count" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6406, version=0)
class Microsoft_Windows_Security_Auditing_6406_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "Categories" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6407, version=0)
class Microsoft_Windows_Security_Auditing_6407_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6408, version=0)
class Microsoft_Windows_Security_Auditing_6408_0(Etw):
    pattern = Struct(
        "ProductName" / WString,
        "Categories" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6409, version=0)
class Microsoft_Windows_Security_Auditing_6409_0(Etw):
    pattern = Struct(
        "GUID" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6410, version=0)
class Microsoft_Windows_Security_Auditing_6410_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6416, version=0)
class Microsoft_Windows_Security_Auditing_6416_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "ClassId" / Guid,
        "VendorIds" / WString,
        "CompatibleIds" / WString,
        "LocationInformation" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6416, version=1)
class Microsoft_Windows_Security_Auditing_6416_1(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "DeviceId" / WString,
        "DeviceDescription" / WString,
        "ClassId" / Guid,
        "ClassName" / WString,
        "VendorIds" / WString,
        "CompatibleIds" / WString,
        "LocationInformation" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6417, version=0)
class Microsoft_Windows_Security_Auditing_6417_0(Etw):
    pattern = Struct(
        "ProcessId" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6418, version=0)
class Microsoft_Windows_Security_Auditing_6418_0(Etw):
    pattern = Struct(
        "ProcessId" / Int64ul,
        "ProcessName" / WString,
        "FatalCode" / Int32ul
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6419, version=0)
class Microsoft_Windows_Security_Auditing_6419_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "DeviceId" / WString,
        "DeviceDescription" / WString,
        "ClassId" / Guid,
        "ClassName" / WString,
        "HardwareIds" / WString,
        "CompatibleIds" / WString,
        "LocationInformation" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6420, version=0)
class Microsoft_Windows_Security_Auditing_6420_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "DeviceId" / WString,
        "DeviceDescription" / WString,
        "ClassId" / Guid,
        "ClassName" / WString,
        "HardwareIds" / WString,
        "CompatibleIds" / WString,
        "LocationInformation" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6421, version=0)
class Microsoft_Windows_Security_Auditing_6421_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "DeviceId" / WString,
        "DeviceDescription" / WString,
        "ClassId" / Guid,
        "ClassName" / WString,
        "HardwareIds" / WString,
        "CompatibleIds" / WString,
        "LocationInformation" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6422, version=0)
class Microsoft_Windows_Security_Auditing_6422_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "DeviceId" / WString,
        "DeviceDescription" / WString,
        "ClassId" / Guid,
        "ClassName" / WString,
        "HardwareIds" / WString,
        "CompatibleIds" / WString,
        "LocationInformation" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6423, version=0)
class Microsoft_Windows_Security_Auditing_6423_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "DeviceId" / WString,
        "DeviceDescription" / WString,
        "ClassId" / Guid,
        "ClassName" / WString,
        "HardwareIds" / WString,
        "CompatibleIds" / WString,
        "LocationInformation" / WString
    )


@declare(guid=guid("54849625-5478-4994-a5ba-3e3b0328c30d"), event_id=6424, version=0)
class Microsoft_Windows_Security_Auditing_6424_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul,
        "DeviceId" / WString,
        "DeviceDescription" / WString,
        "ClassId" / Guid,
        "ClassName" / WString,
        "HardwareIds" / WString,
        "CompatibleIds" / WString,
        "LocationInformation" / WString
    )

