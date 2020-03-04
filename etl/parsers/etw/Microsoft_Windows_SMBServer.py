# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SMBServer
GUID : d48ce617-33a2-4bc3-a5c7-11aa4f29619e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1, version=2)
class Microsoft_Windows_SMBServer_1_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsRequested" / Int16ul,
        "Flags" / Int32ul,
        "SecurityMode" / Int16ul,
        "Capabilities" / Int32ul,
        "DialectCount" / Int16ul,
        "Dialects" / Int16ul,
        "ClientGuid" / Guid,
        "ConnectionGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=2, version=2)
class Microsoft_Windows_SMBServer_2_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsRequested" / Int16ul,
        "Flags" / Int32ul,
        "VcNumber" / Int8ul,
        "SecurityMode" / Int8ul,
        "Capabilities" / Int32ul,
        "Channel" / Int32ul,
        "PreviousSessionId" / Int64ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=3, version=2)
class Microsoft_Windows_SMBServer_3_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsRequested" / Int16ul,
        "Flags" / Int32ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=4, version=2)
class Microsoft_Windows_SMBServer_4_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsRequested" / Int16ul,
        "Flags" / Int32ul,
        "PathLength" / Int16ul,
        "Path" / Bytes(lambda this: this.PathLength),
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=5, version=2)
class Microsoft_Windows_SMBServer_5_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsRequested" / Int16ul,
        "Flags" / Int32ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=6, version=2)
class Microsoft_Windows_SMBServer_6_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsRequested" / Int16ul,
        "Flags" / Int32ul,
        "ConnectionGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=7, version=2)
class Microsoft_Windows_SMBServer_7_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsRequested" / Int16ul,
        "Flags" / Int32ul,
        "ConnectionGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=8, version=2)
class Microsoft_Windows_SMBServer_8_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsRequested" / Int16ul,
        "Flags" / Int32ul,
        "SecurityFlags" / Int8ul,
        "RequestedOplockLevel" / Int8ul,
        "ImpersonationLevel" / Int32ul,
        "CreateFlags" / Int64ul,
        "RootDirectoryFid" / Int64ul,
        "DesiredAccess" / Int32sl,
        "FileAttributes" / Int32sl,
        "ShareAccess" / Int32sl,
        "CreateDisposition" / Int32sl,
        "CreateOptions" / Int32sl,
        "NameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.NameLength),
        "CreateContextsCount" / Int32ul,
        "LeaseKey" / Guid,
        "LeaseLevel" / Int32ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=9, version=2)
class Microsoft_Windows_SMBServer_9_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsRequested" / Int16ul,
        "Flags" / Int32ul,
        "CloseFlags" / Int16ul,
        "FileId" / Int64ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=10, version=2)
class Microsoft_Windows_SMBServer_10_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsRequested" / Int16ul,
        "Flags" / Int32ul,
        "FileId" / Int64ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=11, version=2)
class Microsoft_Windows_SMBServer_11_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsRequested" / Int16ul,
        "Flags" / Int32ul,
        "Length" / Int32ul,
        "Offset" / Int64ul,
        "FileId" / Int64ul,
        "MinimumCount" / Int32ul,
        "Channel" / Int32ul,
        "RemainingBytes" / Int32ul,
        "ReadChannelInfoOffset" / Int16ul,
        "ReadChannelInfoLength" / Int16ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=12, version=2)
class Microsoft_Windows_SMBServer_12_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsRequested" / Int16ul,
        "Flags" / Int32ul,
        "Length" / Int32ul,
        "Offset" / Int64ul,
        "FileId" / Int64ul,
        "Channel" / Int32ul,
        "RemainingBytes" / Int32ul,
        "WriteChannelInfoOffset" / Int16ul,
        "WriteChannelInfoLength" / Int16ul,
        "WriteFlags" / Int32ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=13, version=2)
class Microsoft_Windows_SMBServer_13_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsRequested" / Int16ul,
        "Flags" / Int32ul,
        "OplockLevel" / Int8ul,
        "FileId" / Int64ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=14, version=2)
class Microsoft_Windows_SMBServer_14_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsRequested" / Int16ul,
        "Flags" / Int32ul,
        "LeaseFlags" / Int32ul,
        "CurrentLeaseState" / Int32ul,
        "NewLeaseState" / Int32ul,
        "BreakReason" / Int32ul,
        "AccessMaskHint" / Int32ul,
        "ShareMaskHint" / Int32ul,
        "LeaseKey" / Guid,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=15, version=2)
class Microsoft_Windows_SMBServer_15_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsRequested" / Int16ul,
        "Flags" / Int32ul,
        "LeaseFlags" / Int32ul,
        "LeaseState" / Int32ul,
        "LeaseDuration" / Int64sl,
        "LeaseKey" / Guid,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=16, version=2)
class Microsoft_Windows_SMBServer_16_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsRequested" / Int16ul,
        "Flags" / Int32ul,
        "FileId" / Int64ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid,
        "LockCount" / Int16ul,
        "Locks" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=17, version=2)
class Microsoft_Windows_SMBServer_17_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsRequested" / Int16ul,
        "Flags" / Int32ul,
        "FileId" / Int64ul,
        "ControlCode" / Int32ul,
        "IoctlFlags" / Int32ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=18, version=2)
class Microsoft_Windows_SMBServer_18_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsRequested" / Int16ul,
        "Flags" / Int32ul,
        "FileInformationClass" / Int8ul,
        "QueryDirectoryFlags" / Int8ul,
        "FileIndex" / Int32ul,
        "FileId" / Int64ul,
        "OutputBufferLength" / Int32ul,
        "NameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.NameLength),
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=19, version=2)
class Microsoft_Windows_SMBServer_19_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsRequested" / Int16ul,
        "Flags" / Int32ul,
        "ChangeNotifyFlags" / Int16ul,
        "FileId" / Int64ul,
        "OutputBufferLength" / Int32ul,
        "CompletionFilter" / Int32ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=20, version=2)
class Microsoft_Windows_SMBServer_20_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsRequested" / Int16ul,
        "Flags" / Int32ul,
        "InfoType" / Int8ul,
        "InfoClass" / Int8ul,
        "OutputBufferLength" / Int32ul,
        "SecurityInformation" / Int32ul,
        "QueryInfoFlags" / Int32ul,
        "FileId" / Int64ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=21, version=2)
class Microsoft_Windows_SMBServer_21_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsRequested" / Int16ul,
        "Flags" / Int32ul,
        "InfoType" / Int8ul,
        "InfoClass" / Int8ul,
        "SecurityInformation" / Int32ul,
        "FileId" / Int64ul,
        "OutputBufferLength" / Int32ul,
        "OutputBuffer" / Bytes(lambda this: this.OutputBufferLength),
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=101, version=2)
class Microsoft_Windows_SMBServer_101_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessingHits" / Int32ul,
        "ProcessingCycles" / Int64ul,
        "QueueHits" / Int32ul,
        "QueueCycles" / Int64ul,
        "FileSystemFastHits" / Int32ul,
        "FileSystemFastCycles" / Int64ul,
        "FileSystemSlowHits" / Int32ul,
        "FileSystemSlowCycles" / Int64ul,
        "TransportFastHits" / Int32ul,
        "TransportFastCycles" / Int64ul,
        "TransportSlowHits" / Int32ul,
        "TransportSlowCycles" / Int64ul,
        "SecurityHits" / Int32ul,
        "SecurityCycles" / Int64ul,
        "SecurityMode" / Int16ul,
        "DialectRevision" / Int16ul,
        "Capabilities" / Int32ul,
        "MaxTransactSize" / Int32ul,
        "MaxReadSize" / Int32ul,
        "MaxWriteSize" / Int32ul,
        "SystemTime" / Int64ul,
        "ConnectionGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=102, version=2)
class Microsoft_Windows_SMBServer_102_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessingHits" / Int32ul,
        "ProcessingCycles" / Int64ul,
        "QueueHits" / Int32ul,
        "QueueCycles" / Int64ul,
        "FileSystemFastHits" / Int32ul,
        "FileSystemFastCycles" / Int64ul,
        "FileSystemSlowHits" / Int32ul,
        "FileSystemSlowCycles" / Int64ul,
        "TransportFastHits" / Int32ul,
        "TransportFastCycles" / Int64ul,
        "TransportSlowHits" / Int32ul,
        "TransportSlowCycles" / Int64ul,
        "SecurityHits" / Int32ul,
        "SecurityCycles" / Int64ul,
        "SessionFlags" / Int16ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=103, version=2)
class Microsoft_Windows_SMBServer_103_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessingHits" / Int32ul,
        "ProcessingCycles" / Int64ul,
        "QueueHits" / Int32ul,
        "QueueCycles" / Int64ul,
        "FileSystemFastHits" / Int32ul,
        "FileSystemFastCycles" / Int64ul,
        "FileSystemSlowHits" / Int32ul,
        "FileSystemSlowCycles" / Int64ul,
        "TransportFastHits" / Int32ul,
        "TransportFastCycles" / Int64ul,
        "TransportSlowHits" / Int32ul,
        "TransportSlowCycles" / Int64ul,
        "SecurityHits" / Int32ul,
        "SecurityCycles" / Int64ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=104, version=2)
class Microsoft_Windows_SMBServer_104_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessingHits" / Int32ul,
        "ProcessingCycles" / Int64ul,
        "QueueHits" / Int32ul,
        "QueueCycles" / Int64ul,
        "FileSystemFastHits" / Int32ul,
        "FileSystemFastCycles" / Int64ul,
        "FileSystemSlowHits" / Int32ul,
        "FileSystemSlowCycles" / Int64ul,
        "TransportFastHits" / Int32ul,
        "TransportFastCycles" / Int64ul,
        "TransportSlowHits" / Int32ul,
        "TransportSlowCycles" / Int64ul,
        "SecurityHits" / Int32ul,
        "SecurityCycles" / Int64ul,
        "ShareType" / Int8ul,
        "ShareFlags" / Int32ul,
        "Capabilities" / Int32ul,
        "MaximalAccess" / Int32ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=105, version=2)
class Microsoft_Windows_SMBServer_105_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessingHits" / Int32ul,
        "ProcessingCycles" / Int64ul,
        "QueueHits" / Int32ul,
        "QueueCycles" / Int64ul,
        "FileSystemFastHits" / Int32ul,
        "FileSystemFastCycles" / Int64ul,
        "FileSystemSlowHits" / Int32ul,
        "FileSystemSlowCycles" / Int64ul,
        "TransportFastHits" / Int32ul,
        "TransportFastCycles" / Int64ul,
        "TransportSlowHits" / Int32ul,
        "TransportSlowCycles" / Int64ul,
        "SecurityHits" / Int32ul,
        "SecurityCycles" / Int64ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=106, version=2)
class Microsoft_Windows_SMBServer_106_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessingHits" / Int32ul,
        "ProcessingCycles" / Int64ul,
        "QueueHits" / Int32ul,
        "QueueCycles" / Int64ul,
        "FileSystemFastHits" / Int32ul,
        "FileSystemFastCycles" / Int64ul,
        "FileSystemSlowHits" / Int32ul,
        "FileSystemSlowCycles" / Int64ul,
        "TransportFastHits" / Int32ul,
        "TransportFastCycles" / Int64ul,
        "TransportSlowHits" / Int32ul,
        "TransportSlowCycles" / Int64ul,
        "SecurityHits" / Int32ul,
        "SecurityCycles" / Int64ul,
        "ConnectionGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=108, version=2)
class Microsoft_Windows_SMBServer_108_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessingHits" / Int32ul,
        "ProcessingCycles" / Int64ul,
        "QueueHits" / Int32ul,
        "QueueCycles" / Int64ul,
        "FileSystemFastHits" / Int32ul,
        "FileSystemFastCycles" / Int64ul,
        "FileSystemSlowHits" / Int32ul,
        "FileSystemSlowCycles" / Int64ul,
        "TransportFastHits" / Int32ul,
        "TransportFastCycles" / Int64ul,
        "TransportSlowHits" / Int32ul,
        "TransportSlowCycles" / Int64ul,
        "SecurityHits" / Int32ul,
        "SecurityCycles" / Int64ul,
        "OplockLevel" / Int8ul,
        "CreateAction" / Int32ul,
        "CreationTime" / Int64ul,
        "LastAccessTime" / Int64ul,
        "LastWriteTime" / Int64ul,
        "LastChangeTime" / Int64ul,
        "AllocationSize" / Int64ul,
        "EndOfFile" / Int64ul,
        "FileAttributes" / Int32ul,
        "FileId" / Int64ul,
        "CreateContextsCount" / Int32ul,
        "LeaseKey" / Guid,
        "LeaseLevel" / Int32ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=109, version=2)
class Microsoft_Windows_SMBServer_109_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessingHits" / Int32ul,
        "ProcessingCycles" / Int64ul,
        "QueueHits" / Int32ul,
        "QueueCycles" / Int64ul,
        "FileSystemFastHits" / Int32ul,
        "FileSystemFastCycles" / Int64ul,
        "FileSystemSlowHits" / Int32ul,
        "FileSystemSlowCycles" / Int64ul,
        "TransportFastHits" / Int32ul,
        "TransportFastCycles" / Int64ul,
        "TransportSlowHits" / Int32ul,
        "TransportSlowCycles" / Int64ul,
        "SecurityHits" / Int32ul,
        "SecurityCycles" / Int64ul,
        "CloseFlags" / Int16ul,
        "CreationTime" / Int64ul,
        "LastAccessTime" / Int64ul,
        "LastWriteTime" / Int64ul,
        "ChangeTime" / Int64ul,
        "AllocationSize" / Int64ul,
        "EndOfFile" / Int64ul,
        "FileAttributes" / Int32ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=110, version=2)
class Microsoft_Windows_SMBServer_110_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessingHits" / Int32ul,
        "ProcessingCycles" / Int64ul,
        "QueueHits" / Int32ul,
        "QueueCycles" / Int64ul,
        "FileSystemFastHits" / Int32ul,
        "FileSystemFastCycles" / Int64ul,
        "FileSystemSlowHits" / Int32ul,
        "FileSystemSlowCycles" / Int64ul,
        "TransportFastHits" / Int32ul,
        "TransportFastCycles" / Int64ul,
        "TransportSlowHits" / Int32ul,
        "TransportSlowCycles" / Int64ul,
        "SecurityHits" / Int32ul,
        "SecurityCycles" / Int64ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=111, version=2)
class Microsoft_Windows_SMBServer_111_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessingHits" / Int32ul,
        "ProcessingCycles" / Int64ul,
        "QueueHits" / Int32ul,
        "QueueCycles" / Int64ul,
        "FileSystemFastHits" / Int32ul,
        "FileSystemFastCycles" / Int64ul,
        "FileSystemSlowHits" / Int32ul,
        "FileSystemSlowCycles" / Int64ul,
        "TransportFastHits" / Int32ul,
        "TransportFastCycles" / Int64ul,
        "TransportSlowHits" / Int32ul,
        "TransportSlowCycles" / Int64ul,
        "SecurityHits" / Int32ul,
        "SecurityCycles" / Int64ul,
        "LengthRead" / Int32ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=112, version=2)
class Microsoft_Windows_SMBServer_112_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessingHits" / Int32ul,
        "ProcessingCycles" / Int64ul,
        "QueueHits" / Int32ul,
        "QueueCycles" / Int64ul,
        "FileSystemFastHits" / Int32ul,
        "FileSystemFastCycles" / Int64ul,
        "FileSystemSlowHits" / Int32ul,
        "FileSystemSlowCycles" / Int64ul,
        "TransportFastHits" / Int32ul,
        "TransportFastCycles" / Int64ul,
        "TransportSlowHits" / Int32ul,
        "TransportSlowCycles" / Int64ul,
        "SecurityHits" / Int32ul,
        "SecurityCycles" / Int64ul,
        "LengthWritten" / Int32ul,
        "Remaining" / Int32ul,
        "WriteChannelInfoOffset" / Int16ul,
        "WriteChannelInfoLength" / Int16ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=113, version=2)
class Microsoft_Windows_SMBServer_113_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessingHits" / Int32ul,
        "ProcessingCycles" / Int64ul,
        "QueueHits" / Int32ul,
        "QueueCycles" / Int64ul,
        "FileSystemFastHits" / Int32ul,
        "FileSystemFastCycles" / Int64ul,
        "FileSystemSlowHits" / Int32ul,
        "FileSystemSlowCycles" / Int64ul,
        "TransportFastHits" / Int32ul,
        "TransportFastCycles" / Int64ul,
        "TransportSlowHits" / Int32ul,
        "TransportSlowCycles" / Int64ul,
        "SecurityHits" / Int32ul,
        "SecurityCycles" / Int64ul,
        "OplockLevel" / Int8ul,
        "FileId" / Int64ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=115, version=2)
class Microsoft_Windows_SMBServer_115_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessingHits" / Int32ul,
        "ProcessingCycles" / Int64ul,
        "QueueHits" / Int32ul,
        "QueueCycles" / Int64ul,
        "FileSystemFastHits" / Int32ul,
        "FileSystemFastCycles" / Int64ul,
        "FileSystemSlowHits" / Int32ul,
        "FileSystemSlowCycles" / Int64ul,
        "TransportFastHits" / Int32ul,
        "TransportFastCycles" / Int64ul,
        "TransportSlowHits" / Int32ul,
        "TransportSlowCycles" / Int64ul,
        "SecurityHits" / Int32ul,
        "SecurityCycles" / Int64ul,
        "LeaseFlags" / Int32ul,
        "LeaseState" / Int32ul,
        "LeaseDuration" / Int64sl,
        "LeaseKey" / Guid,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=116, version=2)
class Microsoft_Windows_SMBServer_116_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessingHits" / Int32ul,
        "ProcessingCycles" / Int64ul,
        "QueueHits" / Int32ul,
        "QueueCycles" / Int64ul,
        "FileSystemFastHits" / Int32ul,
        "FileSystemFastCycles" / Int64ul,
        "FileSystemSlowHits" / Int32ul,
        "FileSystemSlowCycles" / Int64ul,
        "TransportFastHits" / Int32ul,
        "TransportFastCycles" / Int64ul,
        "TransportSlowHits" / Int32ul,
        "TransportSlowCycles" / Int64ul,
        "SecurityHits" / Int32ul,
        "SecurityCycles" / Int64ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=117, version=2)
class Microsoft_Windows_SMBServer_117_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessingHits" / Int32ul,
        "ProcessingCycles" / Int64ul,
        "QueueHits" / Int32ul,
        "QueueCycles" / Int64ul,
        "FileSystemFastHits" / Int32ul,
        "FileSystemFastCycles" / Int64ul,
        "FileSystemSlowHits" / Int32ul,
        "FileSystemSlowCycles" / Int64ul,
        "TransportFastHits" / Int32ul,
        "TransportFastCycles" / Int64ul,
        "TransportSlowHits" / Int32ul,
        "TransportSlowCycles" / Int64ul,
        "SecurityHits" / Int32ul,
        "SecurityCycles" / Int64ul,
        "ControlCode" / Int32ul,
        "IoctlFlags" / Int32ul,
        "FileId" / Int64ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=118, version=2)
class Microsoft_Windows_SMBServer_118_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessingHits" / Int32ul,
        "ProcessingCycles" / Int64ul,
        "QueueHits" / Int32ul,
        "QueueCycles" / Int64ul,
        "FileSystemFastHits" / Int32ul,
        "FileSystemFastCycles" / Int64ul,
        "FileSystemSlowHits" / Int32ul,
        "FileSystemSlowCycles" / Int64ul,
        "TransportFastHits" / Int32ul,
        "TransportFastCycles" / Int64ul,
        "TransportSlowHits" / Int32ul,
        "TransportSlowCycles" / Int64ul,
        "SecurityHits" / Int32ul,
        "SecurityCycles" / Int64ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=119, version=2)
class Microsoft_Windows_SMBServer_119_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessingHits" / Int32ul,
        "ProcessingCycles" / Int64ul,
        "QueueHits" / Int32ul,
        "QueueCycles" / Int64ul,
        "FileSystemFastHits" / Int32ul,
        "FileSystemFastCycles" / Int64ul,
        "FileSystemSlowHits" / Int32ul,
        "FileSystemSlowCycles" / Int64ul,
        "TransportFastHits" / Int32ul,
        "TransportFastCycles" / Int64ul,
        "TransportSlowHits" / Int32ul,
        "TransportSlowCycles" / Int64ul,
        "SecurityHits" / Int32ul,
        "SecurityCycles" / Int64ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=120, version=2)
class Microsoft_Windows_SMBServer_120_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessingHits" / Int32ul,
        "ProcessingCycles" / Int64ul,
        "QueueHits" / Int32ul,
        "QueueCycles" / Int64ul,
        "FileSystemFastHits" / Int32ul,
        "FileSystemFastCycles" / Int64ul,
        "FileSystemSlowHits" / Int32ul,
        "FileSystemSlowCycles" / Int64ul,
        "TransportFastHits" / Int32ul,
        "TransportFastCycles" / Int64ul,
        "TransportSlowHits" / Int32ul,
        "TransportSlowCycles" / Int64ul,
        "SecurityHits" / Int32ul,
        "SecurityCycles" / Int64ul,
        "OutputBufferLength" / Int32ul,
        "OutputBuffer" / Bytes(lambda this: this.OutputBufferLength),
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=121, version=2)
class Microsoft_Windows_SMBServer_121_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessingHits" / Int32ul,
        "ProcessingCycles" / Int64ul,
        "QueueHits" / Int32ul,
        "QueueCycles" / Int64ul,
        "FileSystemFastHits" / Int32ul,
        "FileSystemFastCycles" / Int64ul,
        "FileSystemSlowHits" / Int32ul,
        "FileSystemSlowCycles" / Int64ul,
        "TransportFastHits" / Int32ul,
        "TransportFastCycles" / Int64ul,
        "TransportSlowHits" / Int32ul,
        "TransportSlowCycles" / Int64ul,
        "SecurityHits" / Int32ul,
        "SecurityCycles" / Int64ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=122, version=2)
class Microsoft_Windows_SMBServer_122_2(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "ProcessId" / Int32ul,
        "TreeId" / Int32ul,
        "MessageId" / Int64ul,
        "MasterMessageId" / Int64ul,
        "Command" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int32ul,
        "Status" / Int32ul,
        "ProcessingHits" / Int32ul,
        "ProcessingCycles" / Int64ul,
        "QueueHits" / Int32ul,
        "QueueCycles" / Int64ul,
        "FileSystemFastHits" / Int32ul,
        "FileSystemFastCycles" / Int64ul,
        "FileSystemSlowHits" / Int32ul,
        "FileSystemSlowCycles" / Int64ul,
        "TransportFastHits" / Int32ul,
        "TransportFastCycles" / Int64ul,
        "TransportSlowHits" / Int32ul,
        "TransportSlowCycles" / Int64ul,
        "SecurityHits" / Int32ul,
        "SecurityCycles" / Int64ul,
        "ConnectionGUID" / Guid,
        "SessionGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "FileGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=200, version=0)
class Microsoft_Windows_SMBServer_200_0(Etw):
    pattern = Struct(
        "ComponentId" / Int32ul,
        "LineNumber" / Int32ul,
        "FunctionNameLength" / Int16ul,
        "FunctionName" / Bytes(lambda this: this.FunctionNameLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=201, version=0)
class Microsoft_Windows_SMBServer_201_0(Etw):
    pattern = Struct(
        "WorkItem" / Int64ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=202, version=0)
class Microsoft_Windows_SMBServer_202_0(Etw):
    pattern = Struct(
        "WorkItem" / Int64ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=500, version=0)
class Microsoft_Windows_SMBServer_500_0(Etw):
    pattern = Struct(
        "ConnectionGUID" / Guid,
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength),
        "TransportLength" / Int32ul,
        "TransportName" / Bytes(lambda this: this.TransportLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=501, version=0)
class Microsoft_Windows_SMBServer_501_0(Etw):
    pattern = Struct(
        "ConnectionGUID" / Guid,
        "Flags" / Int32ul,
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength),
        "TransportLength" / Int32ul,
        "TransportName" / Bytes(lambda this: this.TransportLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=502, version=0)
class Microsoft_Windows_SMBServer_502_0(Etw):
    pattern = Struct(
        "ConnectionGUID" / Guid,
        "Reason" / Int32ul,
        "Status" / Int32ul,
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength),
        "TransportLength" / Int32ul,
        "TransportName" / Bytes(lambda this: this.TransportLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=550, version=0)
class Microsoft_Windows_SMBServer_550_0(Etw):
    pattern = Struct(
        "SessionGUID" / Guid,
        "ConnectionGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=551, version=0)
class Microsoft_Windows_SMBServer_551_0(Etw):
    pattern = Struct(
        "SessionGUID" / Guid,
        "ConnectionGUID" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=551, version=1)
class Microsoft_Windows_SMBServer_551_1(Etw):
    pattern = Struct(
        "SessionGUID" / Guid,
        "ConnectionGUID" / Guid,
        "Status" / Int32ul,
        "TranslatedStatus" / Int32ul,
        "ClientAddressLength" / Int32ul,
        "ClientAddress" / Bytes(lambda this: this.ClientAddressLength),
        "SessionId" / Int64ul,
        "UserNameLength" / Int16ul,
        "UserName" / Bytes(lambda this: this.UserNameLength),
        "ClientNameLength" / Int16ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=551, version=2)
class Microsoft_Windows_SMBServer_551_2(Etw):
    pattern = Struct(
        "SessionGUID" / Guid,
        "ConnectionGUID" / Guid,
        "Status" / Int32ul,
        "TranslatedStatus" / Int32ul,
        "ClientAddressLength" / Int32ul,
        "ClientAddress" / Bytes(lambda this: this.ClientAddressLength),
        "SessionId" / Int64ul,
        "UserNameLength" / Int16ul,
        "UserName" / Bytes(lambda this: this.UserNameLength),
        "ClientNameLength" / Int16ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength),
        "SPN" / WString,
        "SPNValidationPolicy" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=552, version=0)
class Microsoft_Windows_SMBServer_552_0(Etw):
    pattern = Struct(
        "SessionGUID" / Guid,
        "ConnectionGUID" / Guid,
        "UserNameLength" / Int16ul,
        "UserName" / Bytes(lambda this: this.UserNameLength),
        "DomainNameLength" / Int16ul,
        "DomainName" / Bytes(lambda this: this.DomainNameLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=553, version=0)
class Microsoft_Windows_SMBServer_553_0(Etw):
    pattern = Struct(
        "SessionGUID" / Guid,
        "ConnectionGUID" / Guid,
        "BindingSessionGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=554, version=0)
class Microsoft_Windows_SMBServer_554_0(Etw):
    pattern = Struct(
        "SessionGUID" / Guid,
        "Reason" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=555, version=0)
class Microsoft_Windows_SMBServer_555_0(Etw):
    pattern = Struct(
        "SessionGUID" / Guid,
        "InvalidateSession" / Int8ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=600, version=0)
class Microsoft_Windows_SMBServer_600_0(Etw):
    pattern = Struct(
        "TreeConnectGUID" / Guid,
        "SessionGUID" / Guid,
        "ConnectionGUID" / Guid,
        "ShareGUID" / Guid,
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "ScopeNameLength" / Int16ul,
        "ScopeName" / Bytes(lambda this: this.ScopeNameLength),
        "ShareProperties" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=601, version=0)
class Microsoft_Windows_SMBServer_601_0(Etw):
    pattern = Struct(
        "TreeConnectGUID" / Guid,
        "SessionGUID" / Guid,
        "ConnectionGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=602, version=0)
class Microsoft_Windows_SMBServer_602_0(Etw):
    pattern = Struct(
        "TreeConnectGUID" / Guid,
        "SessionGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=603, version=0)
class Microsoft_Windows_SMBServer_603_0(Etw):
    pattern = Struct(
        "SessionGUID" / Guid,
        "ConnectionGUID" / Guid,
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "ScopeNameLength" / Int16ul,
        "ScopeName" / Bytes(lambda this: this.ScopeNameLength),
        "Status" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=650, version=0)
class Microsoft_Windows_SMBServer_650_0(Etw):
    pattern = Struct(
        "OpenGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "SessionGUID" / Guid,
        "ConnectionGUID" / Guid,
        "ShareGUID" / Guid,
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "LeaseId" / Guid,
        "DesiredAccess" / Int32ul,
        "SharingMode" / Int32ul,
        "CreateOptions" / Int32ul,
        "FileAttributes" / Int32ul,
        "IsReplay" / Int8ul,
        "IsResume" / Int8ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=651, version=0)
class Microsoft_Windows_SMBServer_651_0(Etw):
    pattern = Struct(
        "OpenGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=652, version=0)
class Microsoft_Windows_SMBServer_652_0(Etw):
    pattern = Struct(
        "OpenGUID" / Guid,
        "TreeConnectGUID" / Guid,
        "SessionGUID" / Guid,
        "ConnectionGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=653, version=0)
class Microsoft_Windows_SMBServer_653_0(Etw):
    pattern = Struct(
        "OpenGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=654, version=0)
class Microsoft_Windows_SMBServer_654_0(Etw):
    pattern = Struct(
        "OpenGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=655, version=0)
class Microsoft_Windows_SMBServer_655_0(Etw):
    pattern = Struct(
        "OpenGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=656, version=0)
class Microsoft_Windows_SMBServer_656_0(Etw):
    pattern = Struct(
        "OpenGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=657, version=0)
class Microsoft_Windows_SMBServer_657_0(Etw):
    pattern = Struct(
        "OpenGUID" / Guid,
        "AppInstanceGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=658, version=0)
class Microsoft_Windows_SMBServer_658_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "UserNameLength" / Int16ul,
        "UserName" / Bytes(lambda this: this.UserNameLength),
        "ComputerNameLength" / Int16ul,
        "ComputerName" / Bytes(lambda this: this.ComputerNameLength),
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=700, version=0)
class Microsoft_Windows_SMBServer_700_0(Etw):
    pattern = Struct(
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "PathNameLength" / Int16ul,
        "PathName" / Bytes(lambda this: this.PathNameLength),
        "CSCState" / Int32ul,
        "ClusterShareType" / Int32ul,
        "ShareProperties" / Int32ul,
        "CaTimeOut" / Int32ul,
        "ShareState" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=701, version=0)
class Microsoft_Windows_SMBServer_701_0(Etw):
    pattern = Struct(
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "PathNameLength" / Int16ul,
        "PathName" / Bytes(lambda this: this.PathNameLength),
        "CSCState" / Int32ul,
        "ClusterShareType" / Int32ul,
        "ShareProperties" / Int32ul,
        "CaTimeOut" / Int32ul,
        "ShareState" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=702, version=0)
class Microsoft_Windows_SMBServer_702_0(Etw):
    pattern = Struct(
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1000, version=0)
class Microsoft_Windows_SMBServer_1000_0(Etw):
    pattern = Struct(
        "UserNameLength" / Int16ul,
        "UserName" / Bytes(lambda this: this.UserNameLength),
        "DomainNameLength" / Int16ul,
        "DomainName" / Bytes(lambda this: this.DomainNameLength),
        "Status" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1001, version=0)
class Microsoft_Windows_SMBServer_1001_0(Etw):
    pattern = Struct(
        "ClientNameLength" / Int16ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength),
        "LogEventCount" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1002, version=0)
class Microsoft_Windows_SMBServer_1002_0(Etw):
    pattern = Struct(
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1003, version=0)
class Microsoft_Windows_SMBServer_1003_0(Etw):
    pattern = Struct(
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "ClientNameLength" / Int16ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength),
        "UserNameLength" / Int16ul,
        "UserName" / Bytes(lambda this: this.UserNameLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1003, version=1)
class Microsoft_Windows_SMBServer_1003_1(Etw):
    pattern = Struct(
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "ClientNameLength" / Int16ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength),
        "UserNameLength" / Int16ul,
        "UserName" / Bytes(lambda this: this.UserNameLength),
        "ClientAddressLength" / Int32ul,
        "ClientAddress" / Bytes(lambda this: this.ClientAddressLength),
        "SessionID" / Int64ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1004, version=0)
class Microsoft_Windows_SMBServer_1004_0(Etw):
    pattern = Struct(
        "ClientNameLength" / Int16ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength),
        "UserNameLength" / Int16ul,
        "UserName" / Bytes(lambda this: this.UserNameLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1004, version=1)
class Microsoft_Windows_SMBServer_1004_1(Etw):
    pattern = Struct(
        "ClientNameLength" / Int16ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength),
        "UserNameLength" / Int16ul,
        "UserName" / Bytes(lambda this: this.UserNameLength),
        "ClientAddressLength" / Int32ul,
        "ClientAddress" / Bytes(lambda this: this.ClientAddressLength),
        "SessionID" / Int64ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1005, version=0)
class Microsoft_Windows_SMBServer_1005_0(Etw):
    pattern = Struct(
        "ClientNameLength" / Int16ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength),
        "UserNameLength" / Int16ul,
        "UserName" / Bytes(lambda this: this.UserNameLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1005, version=1)
class Microsoft_Windows_SMBServer_1005_1(Etw):
    pattern = Struct(
        "ClientNameLength" / Int16ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength),
        "UserNameLength" / Int16ul,
        "UserName" / Bytes(lambda this: this.UserNameLength),
        "ClientAddressLength" / Int32ul,
        "ClientAddress" / Bytes(lambda this: this.ClientAddressLength),
        "ExpectedDialect" / Int32ul,
        "ExpectedCapabilities" / Int32ul,
        "ExpectedSecurityMode" / Int32ul,
        "ReceivedDialect" / Int32ul,
        "ReceivedCapabilities" / Int32ul,
        "ReceivedSecurityMode" / Int32ul,
        "SessionID" / Int64ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1005, version=2)
class Microsoft_Windows_SMBServer_1005_2(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "TranslatedStatus" / Int32ul,
        "ClientNameLength" / Int16ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength),
        "UserNameLength" / Int16ul,
        "UserName" / Bytes(lambda this: this.UserNameLength),
        "ClientAddressLength" / Int32ul,
        "ClientAddress" / Bytes(lambda this: this.ClientAddressLength),
        "SessionID" / Int64ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1006, version=0)
class Microsoft_Windows_SMBServer_1006_0(Etw):
    pattern = Struct(
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "SharePathLength" / Int16ul,
        "SharePath" / Bytes(lambda this: this.SharePathLength),
        "ClientAddressLength" / Int32ul,
        "ClientAddress" / Bytes(lambda this: this.ClientAddressLength),
        "UserNameLength" / Int16ul,
        "UserName" / Bytes(lambda this: this.UserNameLength),
        "ClientNameLength" / Int16ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength),
        "MappedAccess" / Int32ul,
        "GrantedAccess" / Int32ul,
        "ShareSecurityDescriptorLength" / Int32ul,
        "ShareSecurityDescriptor" / Bytes(lambda this: this.ShareSecurityDescriptorLength),
        "Status" / Int32ul,
        "TranslatedStatus" / Int32ul,
        "SessionID" / Int64ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1007, version=0)
class Microsoft_Windows_SMBServer_1007_0(Etw):
    pattern = Struct(
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "SharePathLength" / Int16ul,
        "SharePath" / Bytes(lambda this: this.SharePathLength),
        "ClientAddressLength" / Int32ul,
        "ClientAddress" / Bytes(lambda this: this.ClientAddressLength),
        "ClientNameLength" / Int16ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1009, version=0)
class Microsoft_Windows_SMBServer_1009_0(Etw):
    pattern = Struct(
        "ClientAddressLength" / Int32ul,
        "ClientAddress" / Bytes(lambda this: this.ClientAddressLength),
        "ClientNameLength" / Int16ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength),
        "SessionId" / Int64ul,
        "SessionGUID" / Guid,
        "ConnectionGUID" / Guid
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1010, version=0)
class Microsoft_Windows_SMBServer_1010_0(Etw):
    pattern = Struct(
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "DomainNameLength" / Int16ul,
        "DomainName" / Bytes(lambda this: this.DomainNameLength),
        "TransportNameLength" / Int16ul,
        "TransportName" / Bytes(lambda this: this.TransportNameLength),
        "TransportFlags" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1011, version=0)
class Microsoft_Windows_SMBServer_1011_0(Etw):
    pattern = Struct(
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "DomainNameLength" / Int16ul,
        "DomainName" / Bytes(lambda this: this.DomainNameLength),
        "TransportNameLength" / Int16ul,
        "TransportName" / Bytes(lambda this: this.TransportNameLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1012, version=0)
class Microsoft_Windows_SMBServer_1012_0(Etw):
    pattern = Struct(
        "ChangeType" / Int32ul,
        "NetNameLength" / Int16ul,
        "NetName" / Bytes(lambda this: this.NetNameLength),
        "Flags" / Int32ul,
        "InterfaceIndex" / Int32ul,
        "Capability" / Int32ul,
        "LinkSpeed" / Int64ul,
        "ClientAddressLength" / Int16ul,
        "ClientAddress" / Bytes(lambda this: this.ClientAddressLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1013, version=0)
class Microsoft_Windows_SMBServer_1013_0(Etw):
    pattern = Struct(
        "EndpointNameLength" / Int16ul,
        "EndpointName" / Bytes(lambda this: this.EndpointNameLength),
        "TransportNameLength" / Int16ul,
        "TransportName" / Bytes(lambda this: this.TransportNameLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1014, version=0)
class Microsoft_Windows_SMBServer_1014_0(Etw):
    pattern = Struct(
        "EndpointNameLength" / Int16ul,
        "EndpointName" / Bytes(lambda this: this.EndpointNameLength),
        "TransportNameLength" / Int16ul,
        "TransportName" / Bytes(lambda this: this.TransportNameLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1015, version=0)
class Microsoft_Windows_SMBServer_1015_0(Etw):
    pattern = Struct(
        "ClientNameLength" / Int16ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength),
        "ClientAddressLength" / Int16ul,
        "ClientAddress" / Bytes(lambda this: this.ClientAddressLength),
        "Status" / Int32ul,
        "TranslatedStatus" / Int32ul,
        "SessionID" / Int64ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1016, version=0)
class Microsoft_Windows_SMBServer_1016_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "TranslatedStatus" / Int32ul,
        "RKFStatus" / Int32ul,
        "TranslatedRKFStatus" / Int32ul,
        "ConnectionGUID" / Guid,
        "ClientNameLength" / Int16ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength),
        "ClientAddressLength" / Int16ul,
        "ClientAddress" / Bytes(lambda this: this.ClientAddressLength),
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "UserNameLength" / Int16ul,
        "UserName" / Bytes(lambda this: this.UserNameLength),
        "SessionId" / Int64ul,
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "DurableHandle" / Int8ul,
        "ResilientHandle" / Int8ul,
        "PersistentHandle" / Int8ul,
        "ResumeKey" / Guid,
        "Reason" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1017, version=0)
class Microsoft_Windows_SMBServer_1017_0(Etw):
    pattern = Struct(
        "DurableHandle" / Int8ul,
        "ResilientHandle" / Int8ul,
        "PersistentFID" / Int64ul,
        "VolatileFID" / Int64ul,
        "ResumeKey" / Guid,
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1018, version=0)
class Microsoft_Windows_SMBServer_1018_0(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "Status" / Int32ul,
        "TranslatedStatus" / Int32ul,
        "TaskStatus" / Int32ul,
        "TranslatedTaskStatus" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1019, version=0)
class Microsoft_Windows_SMBServer_1019_0(Etw):
    pattern = Struct(
        "ResumeKey" / Guid,
        "Status" / Int32ul,
        "TranslatedStatus" / Int32ul,
        "TaskStatus" / Int32ul,
        "TranslatedTaskStatus" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1020, version=0)
class Microsoft_Windows_SMBServer_1020_0(Etw):
    pattern = Struct(
        "Command" / Int32ul,
        "SessionGuid" / Guid,
        "SessionId" / Int64ul,
        "ConnectionGuid" / Guid,
        "UserNameLength" / Int16ul,
        "UserName" / Bytes(lambda this: this.UserNameLength),
        "ClientNameLength" / Int16ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength),
        "ClientAddressLength" / Int16ul,
        "ClientAddress" / Bytes(lambda this: this.ClientAddressLength),
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "DurationInMilliseconds" / Int64ul,
        "ThresholdInMilliseconds" / Int64ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1020, version=1)
class Microsoft_Windows_SMBServer_1020_1(Etw):
    pattern = Struct(
        "Command" / Int32ul,
        "SessionGuid" / Guid,
        "SessionId" / Int64ul,
        "ConnectionGuid" / Guid,
        "UserNameLength" / Int16ul,
        "UserName" / Bytes(lambda this: this.UserNameLength),
        "ClientNameLength" / Int16ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength),
        "ClientAddressLength" / Int16ul,
        "ClientAddress" / Bytes(lambda this: this.ClientAddressLength),
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "DurationInMilliseconds" / Int64ul,
        "ThresholdInMilliseconds" / Int64ul,
        "CtlCode" / Int32ul,
        "SubCode" / Int32ul,
        "TunneledControl" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1021, version=0)
class Microsoft_Windows_SMBServer_1021_0(Etw):
    pattern = Struct(
        "ConfiguredLmCompatibilityLevel" / Int32ul,
        "DefaultLmCompatibilityLevel" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1028, version=0)
class Microsoft_Windows_SMBServer_1028_0(Etw):
    pattern = Struct(
        "NewDialect" / Int16ul,
        "OldDialect" / Int16ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1029, version=0)
class Microsoft_Windows_SMBServer_1029_0(Etw):
    pattern = Struct(
        "CipherSuiteOrder" / WString
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1030, version=0)
class Microsoft_Windows_SMBServer_1030_0(Etw):
    pattern = Struct(
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "IsRead" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1031, version=0)
class Microsoft_Windows_SMBServer_1031_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1032, version=0)
class Microsoft_Windows_SMBServer_1032_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1033, version=0)
class Microsoft_Windows_SMBServer_1033_0(Etw):
    pattern = Struct(
        "NotificationType" / Int32ul,
        "InterfaceNameLength" / Int16ul,
        "InterfaceName" / Bytes(lambda this: this.InterfaceNameLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1034, version=0)
class Microsoft_Windows_SMBServer_1034_0(Etw):
    pattern = Struct(
        "FailureType" / Int32ul,
        "InterfaceIndex" / Int32ul,
        "Error" / Int32ul,
        "DeviceNameLength" / Int16ul,
        "DeviceName" / Bytes(lambda this: this.DeviceNameLength),
        "ExtraInformation" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1035, version=0)
class Microsoft_Windows_SMBServer_1035_0(Etw):
    pattern = Struct(
        "EndpointState" / Int32ul,
        "InterfaceIndex" / Int32ul,
        "TransportNameLength" / Int16ul,
        "TransportName" / Bytes(lambda this: this.TransportNameLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1036, version=0)
class Microsoft_Windows_SMBServer_1036_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1037, version=0)
class Microsoft_Windows_SMBServer_1037_0(Etw):
    pattern = Struct(
        "FailureType" / Int32ul,
        "InterfaceIndex" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1038, version=0)
class Microsoft_Windows_SMBServer_1038_0(Etw):
    pattern = Struct(
        "FailureType" / Int32ul,
        "DeviceNameLength" / Int16ul,
        "DeviceName" / Bytes(lambda this: this.DeviceNameLength),
        "Error" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1039, version=0)
class Microsoft_Windows_SMBServer_1039_0(Etw):
    pattern = Struct(
        "NotificationType" / Int32ul,
        "InterfaceIndex" / Int32ul,
        "NdkOperationalState" / Int16ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1040, version=0)
class Microsoft_Windows_SMBServer_1040_0(Etw):
    pattern = Struct(
        "NotificationType" / Int32ul,
        "InterfaceIndex" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1041, version=0)
class Microsoft_Windows_SMBServer_1041_0(Etw):
    pattern = Struct(
        "FailureType" / Int32ul,
        "RegistryValueNameLength" / Int32ul,
        "RegistryValueName" / Bytes(lambda this: this.RegistryValueNameLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1043, version=0)
class Microsoft_Windows_SMBServer_1043_0(Etw):
    pattern = Struct(
        "CloseOperationDurationInMillieconds" / Int64ul,
        "TransportNameLength" / Int32ul,
        "TransportName" / Bytes(lambda this: this.TransportNameLength),
        "EndpointShutdown" / Int8ul,
        "EndpointRemoved" / Int8ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1800, version=0)
class Microsoft_Windows_SMBServer_1800_0(Etw):
    pattern = Struct(
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1801, version=0)
class Microsoft_Windows_SMBServer_1801_0(Etw):
    pattern = Struct(
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "Status" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1802, version=0)
class Microsoft_Windows_SMBServer_1802_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1803, version=0)
class Microsoft_Windows_SMBServer_1803_0(Etw):
    pattern = Struct(
        "DescriptorName" / WString
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1804, version=1)
class Microsoft_Windows_SMBServer_1804_1(Etw):
    pattern = Struct(
        "Days" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1900, version=0)
class Microsoft_Windows_SMBServer_1900_0(Etw):
    pattern = Struct(
        "IsTdiEnabled" / Int8ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1901, version=0)
class Microsoft_Windows_SMBServer_1901_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1902, version=0)
class Microsoft_Windows_SMBServer_1902_0(Etw):
    pattern = Struct(
        "AddressFamily" / Int32ul,
        "NetLuid" / Int64ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1903, version=0)
class Microsoft_Windows_SMBServer_1903_0(Etw):
    pattern = Struct(
        "AddressFamily" / Int32ul,
        "NetLuid" / Int64ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1904, version=0)
class Microsoft_Windows_SMBServer_1904_0(Etw):
    pattern = Struct(
        "NetLuid" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=1905, version=0)
class Microsoft_Windows_SMBServer_1905_0(Etw):
    pattern = Struct(
        "SessionId" / Int64ul,
        "InstanceId" / Int32ul,
        "Reason" / WString
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=2000, version=0)
class Microsoft_Windows_SMBServer_2000_0(Etw):
    pattern = Struct(
        "ReassembledEventID" / Int16ul,
        "FragmentSize" / Int32ul,
        "FragmentData" / Bytes(lambda this: this.FragmentSize)
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=3000, version=0)
class Microsoft_Windows_SMBServer_3000_0(Etw):
    pattern = Struct(
        "ClientName" / CString
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=3002, version=1)
class Microsoft_Windows_SMBServer_3002_1(Etw):
    pattern = Struct(
        "ClientName" / CString
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=3003, version=1)
class Microsoft_Windows_SMBServer_3003_1(Etw):
    pattern = Struct(
        "Days" / Int32ul
    )


@declare(guid=guid("d48ce617-33a2-4bc3-a5c7-11aa4f29619e"), event_id=40000, version=0)
class Microsoft_Windows_SMBServer_40000_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul,
        "PeerAddressLength" / Int32ul,
        "PeerAddress" / Bytes(lambda this: this.PeerAddressLength),
        "PacketSize" / Int32ul,
        "PacketData" / Bytes(lambda this: this.PacketSize)
    )

