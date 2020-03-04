# -*- coding: utf-8 -*-
"""
Microsoft-Windows-PushNotifications-Platform
GUID : 88cd9180-4491-4640-b571-e3bee2527943
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1, version=0)
class Microsoft_Windows_PushNotifications_Platform_1_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "FunctionName" / WString,
        "LineNumber" / Int32sl,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=7, version=0)
class Microsoft_Windows_PushNotifications_Platform_7_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Privilege" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=8, version=0)
class Microsoft_Windows_PushNotifications_Platform_8_0(Etw):
    pattern = Struct(
        "NewPrivilege" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=9, version=0)
class Microsoft_Windows_PushNotifications_Platform_9_0(Etw):
    pattern = Struct(
        "ResultedPrivilege" / Int32ul,
        "Error" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=12, version=0)
class Microsoft_Windows_PushNotifications_Platform_12_0(Etw):
    pattern = Struct(
        "CountApplication" / Int16ul,
        "MaximumApplication" / Int16ul,
        "OldMaximumApplication" / Int16ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=13, version=0)
class Microsoft_Windows_PushNotifications_Platform_13_0(Etw):
    pattern = Struct(
        "NewMaximumApplication" / Int16ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=15, version=0)
class Microsoft_Windows_PushNotifications_Platform_15_0(Etw):
    pattern = Struct(
        "CountApplication" / Int16ul,
        "CountAllocated" / Int16ul,
        "MaximumApplication" / Int16ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=19, version=0)
class Microsoft_Windows_PushNotifications_Platform_19_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "FunctionName" / WString,
        "LineNumber" / Int32sl,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=20, version=0)
class Microsoft_Windows_PushNotifications_Platform_20_0(Etw):
    pattern = Struct(
        "FilePath" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=21, version=0)
class Microsoft_Windows_PushNotifications_Platform_21_0(Etw):
    pattern = Struct(
        "CountInboxApps" / Int32ul,
        "CountPreinstallApps" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=23, version=0)
class Microsoft_Windows_PushNotifications_Platform_23_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "Uri" / WString,
        "WpnRecurrence" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=26, version=0)
class Microsoft_Windows_PushNotifications_Platform_26_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "InstanceId" / Int64ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=27, version=0)
class Microsoft_Windows_PushNotifications_Platform_27_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "InstanceId" / Int64ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=28, version=0)
class Microsoft_Windows_PushNotifications_Platform_28_0(Etw):
    pattern = Struct(
        "MessageCode" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=31, version=0)
class Microsoft_Windows_PushNotifications_Platform_31_0(Etw):
    pattern = Struct(
        "TotalSize" / Int64ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=35, version=0)
class Microsoft_Windows_PushNotifications_Platform_35_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=36, version=0)
class Microsoft_Windows_PushNotifications_Platform_36_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=37, version=0)
class Microsoft_Windows_PushNotifications_Platform_37_0(Etw):
    pattern = Struct(
        "ChannelsExist" / Int8ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=38, version=0)
class Microsoft_Windows_PushNotifications_Platform_38_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=39, version=0)
class Microsoft_Windows_PushNotifications_Platform_39_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=40, version=0)
class Microsoft_Windows_PushNotifications_Platform_40_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl,
        "PdcType" / Int32ul,
        "PdcScenario" / Int32ul,
        "PdcNetRefCount" / Int64sl,
        "PdcPlatRefCount" / Int64sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=41, version=0)
class Microsoft_Windows_PushNotifications_Platform_41_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl,
        "PdcType" / Int32ul,
        "PdcNetRefCount" / Int64sl,
        "PdcPlatRefCount" / Int64sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=42, version=0)
class Microsoft_Windows_PushNotifications_Platform_42_0(Etw):
    pattern = Struct(
        "GroupPolicyValue" / Int8ul,
        "MDMPolicyValue" / Int8ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1000, version=0)
class Microsoft_Windows_PushNotifications_Platform_1000_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "Enabled" / Int8ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1001, version=0)
class Microsoft_Windows_PushNotifications_Platform_1001_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "Flags" / Int32ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1002, version=0)
class Microsoft_Windows_PushNotifications_Platform_1002_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "Flags" / Int32ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1005, version=0)
class Microsoft_Windows_PushNotifications_Platform_1005_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1006, version=0)
class Microsoft_Windows_PushNotifications_Platform_1006_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "Properties" / Int32ul,
        "Cookie" / Int32ul,
        "TransactionId" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1007, version=0)
class Microsoft_Windows_PushNotifications_Platform_1007_0(Etw):
    pattern = Struct(
        "TransactionId" / Int32sl,
        "ChannelId" / WString,
        "ChannelUri" / WString,
        "Expiry" / Double
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1008, version=0)
class Microsoft_Windows_PushNotifications_Platform_1008_0(Etw):
    pattern = Struct(
        "ChannelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1010, version=0)
class Microsoft_Windows_PushNotifications_Platform_1010_0(Etw):
    pattern = Struct(
        "NotificationType" / Int32ul,
        "ChannelId" / WString,
        "AppUserModelId" / WString,
        "TrackingId" / Int32ul,
        "MessageId" / Int64ul,
        "Timestamp" / Double,
        "Expiry" / Double,
        "Tag" / WString,
        "Group" / WString,
        "Action" / Int32ul,
        "OfflineCacheCount" / Int32ul,
        "CacheRollover" / Int8ul,
        "OfflineBundleId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1011, version=0)
class Microsoft_Windows_PushNotifications_Platform_1011_0(Etw):
    pattern = Struct(
        "ChannelId" / WString,
        "PackageFullName" / WString,
        "Properties" / Int32ul,
        "Cookie" / Int32ul,
        "TransactionId" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1012, version=0)
class Microsoft_Windows_PushNotifications_Platform_1012_0(Etw):
    pattern = Struct(
        "BatchingState" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1013, version=0)
class Microsoft_Windows_PushNotifications_Platform_1013_0(Etw):
    pattern = Struct(
        "ChannelId" / WString,
        "NotificationType" / Int32ul,
        "Enabled" / Int8ul,
        "AppUserModelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1014, version=0)
class Microsoft_Windows_PushNotifications_Platform_1014_0(Etw):
    pattern = Struct(
        "DisplayStatus" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1015, version=0)
class Microsoft_Windows_PushNotifications_Platform_1015_0(Etw):
    pattern = Struct(
        "NotificationType" / Int32ul,
        "Enabled" / Int8ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1016, version=0)
class Microsoft_Windows_PushNotifications_Platform_1016_0(Etw):
    pattern = Struct(
        "NetworkCost" / Int32ul,
        "Costly" / Int8ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1017, version=0)
class Microsoft_Windows_PushNotifications_Platform_1017_0(Etw):
    pattern = Struct(
        "DateSource" / Int32ul,
        "BillingCycle" / Int64ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1019, version=0)
class Microsoft_Windows_PushNotifications_Platform_1019_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1021, version=0)
class Microsoft_Windows_PushNotifications_Platform_1021_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1023, version=0)
class Microsoft_Windows_PushNotifications_Platform_1023_0(Etw):
    pattern = Struct(
        "WorkItemName" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1024, version=0)
class Microsoft_Windows_PushNotifications_Platform_1024_0(Etw):
    pattern = Struct(
        "WasConnected" / Int8ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1025, version=0)
class Microsoft_Windows_PushNotifications_Platform_1025_0(Etw):
    pattern = Struct(
        "PowerEventType" / WString,
        "IsEnabled" / Int8ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1100, version=0)
class Microsoft_Windows_PushNotifications_Platform_1100_0(Etw):
    pattern = Struct(
        "UserId" / Int64ul,
        "UserType" / Int32ul,
        "FeatureSet" / CString,
        "AuthType" / CString,
        "AuthPayloadSize" / Int32ul,
        "AuthPayload" / Bytes(lambda this: this.AuthPayloadSize),
        "BindPayloadSize" / Int32ul,
        "BindPayload" / Bytes(lambda this: this.BindPayloadSize)
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1101, version=0)
class Microsoft_Windows_PushNotifications_Platform_1101_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1102, version=0)
class Microsoft_Windows_PushNotifications_Platform_1102_0(Etw):
    pattern = Struct(
        "TransactionId" / Int32sl,
        "ChannelId" / CString,
        "PackageFullName" / CString,
        "Properties" / Int32ul,
        "CommandSize" / Int32ul,
        "Command" / Bytes(lambda this: this.CommandSize),
        "Namespace" / CString,
        "ContextId" / Int64ul,
        "PayloadSize" / Int32ul,
        "Payload" / Bytes(lambda this: this.PayloadSize),
        "UserId" / Int64ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1103, version=0)
class Microsoft_Windows_PushNotifications_Platform_1103_0(Etw):
    pattern = Struct(
        "TransactionId" / Int32sl,
        "TrID" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1104, version=0)
class Microsoft_Windows_PushNotifications_Platform_1104_0(Etw):
    pattern = Struct(
        "ChannelId" / CString,
        "CommandSize" / Int32ul,
        "Command" / Bytes(lambda this: this.CommandSize),
        "Namespace" / CString,
        "ContextId" / Int64ul,
        "PayloadSize" / Int32ul,
        "Payload" / Bytes(lambda this: this.PayloadSize),
        "UserId" / Int64ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1105, version=0)
class Microsoft_Windows_PushNotifications_Platform_1105_0(Etw):
    pattern = Struct(
        "ChannelId" / CString,
        "NotificationType" / Int32ul,
        "Enabled" / Int8ul,
        "CommandSize" / Int32ul,
        "Command" / Bytes(lambda this: this.CommandSize),
        "Namespace" / CString,
        "ContextId" / Int64ul,
        "PayloadSize" / Int32ul,
        "Payload" / Bytes(lambda this: this.PayloadSize),
        "UserId" / Int64ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1106, version=0)
class Microsoft_Windows_PushNotifications_Platform_1106_0(Etw):
    pattern = Struct(
        "BatchingState" / Int32ul,
        "CommandSize" / Int32ul,
        "Command" / Bytes(lambda this: this.CommandSize),
        "Namespace" / CString,
        "ContextId" / Int64ul,
        "PayloadSize" / Int32ul,
        "Payload" / Bytes(lambda this: this.PayloadSize)
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1107, version=0)
class Microsoft_Windows_PushNotifications_Platform_1107_0(Etw):
    pattern = Struct(
        "TrID" / Int32ul,
        "Error" / Int32ul,
        "ContextId" / Int64ul,
        "UserId" / Int64ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1108, version=0)
class Microsoft_Windows_PushNotifications_Platform_1108_0(Etw):
    pattern = Struct(
        "Namespace" / CString,
        "UserId" / CString,
        "PayloadSize" / Int32ul,
        "MsgId" / Int64ul,
        "Ack" / Int8ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1110, version=0)
class Microsoft_Windows_PushNotifications_Platform_1110_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1112, version=0)
class Microsoft_Windows_PushNotifications_Platform_1112_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1113, version=0)
class Microsoft_Windows_PushNotifications_Platform_1113_0(Etw):
    pattern = Struct(
        "DeviceId" / CString,
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1114, version=0)
class Microsoft_Windows_PushNotifications_Platform_1114_0(Etw):
    pattern = Struct(
        "NotificationType" / Int32ul,
        "Enabled" / Int8ul,
        "CommandSize" / Int32ul,
        "Command" / Bytes(lambda this: this.CommandSize),
        "Namespace" / CString,
        "ContextId" / Int64ul,
        "PayloadSize" / Int32ul,
        "Payload" / Bytes(lambda this: this.PayloadSize),
        "UserId" / Int64ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1115, version=0)
class Microsoft_Windows_PushNotifications_Platform_1115_0(Etw):
    pattern = Struct(
        "MsgId" / Int64ul,
        "CommandSize" / Int32ul,
        "Command" / Bytes(lambda this: this.CommandSize),
        "Namespace" / CString,
        "PayloadSize" / Int32ul,
        "Payload" / Bytes(lambda this: this.PayloadSize)
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1116, version=0)
class Microsoft_Windows_PushNotifications_Platform_1116_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1117, version=0)
class Microsoft_Windows_PushNotifications_Platform_1117_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1118, version=0)
class Microsoft_Windows_PushNotifications_Platform_1118_0(Etw):
    pattern = Struct(
        "Nonce" / CString,
        "Response" / CString,
        "CommandSize" / Int32ul,
        "Command" / Bytes(lambda this: this.CommandSize),
        "Namespace" / CString,
        "ContextId" / Int64ul,
        "PayloadSize" / Int32ul,
        "Payload" / Bytes(lambda this: this.PayloadSize)
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1201, version=0)
class Microsoft_Windows_PushNotifications_Platform_1201_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1202, version=0)
class Microsoft_Windows_PushNotifications_Platform_1202_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1203, version=0)
class Microsoft_Windows_PushNotifications_Platform_1203_0(Etw):
    pattern = Struct(
        "CommandTrid" / Int32ul,
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1204, version=0)
class Microsoft_Windows_PushNotifications_Platform_1204_0(Etw):
    pattern = Struct(
        "CommandTrid" / Int32ul,
        "ConnectionType" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1205, version=0)
class Microsoft_Windows_PushNotifications_Platform_1205_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1206, version=0)
class Microsoft_Windows_PushNotifications_Platform_1206_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1207, version=0)
class Microsoft_Windows_PushNotifications_Platform_1207_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul,
        "HostName" / CString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1208, version=0)
class Microsoft_Windows_PushNotifications_Platform_1208_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1211, version=0)
class Microsoft_Windows_PushNotifications_Platform_1211_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul,
        "HostName" / CString,
        "Port" / Int16ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1212, version=0)
class Microsoft_Windows_PushNotifications_Platform_1212_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul,
        "HostName" / CString,
        "Port" / Int16ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1213, version=0)
class Microsoft_Windows_PushNotifications_Platform_1213_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1214, version=0)
class Microsoft_Windows_PushNotifications_Platform_1214_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul,
        "HostName" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1215, version=0)
class Microsoft_Windows_PushNotifications_Platform_1215_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1216, version=0)
class Microsoft_Windows_PushNotifications_Platform_1216_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1217, version=0)
class Microsoft_Windows_PushNotifications_Platform_1217_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1218, version=0)
class Microsoft_Windows_PushNotifications_Platform_1218_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1219, version=0)
class Microsoft_Windows_PushNotifications_Platform_1219_0(Etw):
    pattern = Struct(
        "Bytes" / Int32ul,
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1220, version=0)
class Microsoft_Windows_PushNotifications_Platform_1220_0(Etw):
    pattern = Struct(
        "Bytes" / Int32ul,
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1223, version=0)
class Microsoft_Windows_PushNotifications_Platform_1223_0(Etw):
    pattern = Struct(
        "Verb" / CString,
        "TrID" / Int32ul,
        "Namespace" / CString,
        "CorrelationVector" / CString,
        "Bytes" / Int32ul,
        "Payload" / Bytes(lambda this: this.Bytes),
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1224, version=0)
class Microsoft_Windows_PushNotifications_Platform_1224_0(Etw):
    pattern = Struct(
        "Bytes" / Int32ul,
        "Payload" / Bytes(lambda this: this.Bytes),
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1225, version=0)
class Microsoft_Windows_PushNotifications_Platform_1225_0(Etw):
    pattern = Struct(
        "Verb" / CString,
        "TrID" / Int32ul,
        "Namespace" / CString,
        "CorrelationVector" / CString,
        "Bytes" / Int32ul,
        "Payload" / Bytes(lambda this: this.Bytes),
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1226, version=0)
class Microsoft_Windows_PushNotifications_Platform_1226_0(Etw):
    pattern = Struct(
        "Bytes" / Int32ul,
        "Payload" / Bytes(lambda this: this.Bytes),
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1227, version=0)
class Microsoft_Windows_PushNotifications_Platform_1227_0(Etw):
    pattern = Struct(
        "Verb" / CString,
        "TrID" / Int32ul,
        "Namespace" / CString,
        "CorrelationVector" / CString,
        "Bytes" / Int32ul,
        "Payload" / Bytes(lambda this: this.Bytes),
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1228, version=0)
class Microsoft_Windows_PushNotifications_Platform_1228_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1229, version=0)
class Microsoft_Windows_PushNotifications_Platform_1229_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1230, version=0)
class Microsoft_Windows_PushNotifications_Platform_1230_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1231, version=0)
class Microsoft_Windows_PushNotifications_Platform_1231_0(Etw):
    pattern = Struct(
        "ServerKaHint" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1232, version=0)
class Microsoft_Windows_PushNotifications_Platform_1232_0(Etw):
    pattern = Struct(
        "KaValueType" / Int32ul,
        "KaValue" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1233, version=0)
class Microsoft_Windows_PushNotifications_Platform_1233_0(Etw):
    pattern = Struct(
        "SessionId" / CString,
        "SecondsSinceLastSentPacket" / Int64ul,
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1234, version=0)
class Microsoft_Windows_PushNotifications_Platform_1234_0(Etw):
    pattern = Struct(
        "ProtocolType" / Int32ul,
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1235, version=0)
class Microsoft_Windows_PushNotifications_Platform_1235_0(Etw):
    pattern = Struct(
        "IdleSucceededInterval" / Int32ul,
        "IdleFailedInterval" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1236, version=0)
class Microsoft_Windows_PushNotifications_Platform_1236_0(Etw):
    pattern = Struct(
        "IdleSucceededCount" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1237, version=0)
class Microsoft_Windows_PushNotifications_Platform_1237_0(Etw):
    pattern = Struct(
        "IdleFailedInterval" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1239, version=0)
class Microsoft_Windows_PushNotifications_Platform_1239_0(Etw):
    pattern = Struct(
        "KaValueType" / Int32ul,
        "KaValue" / Int32ul,
        "KaMinLimit" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1241, version=0)
class Microsoft_Windows_PushNotifications_Platform_1241_0(Etw):
    pattern = Struct(
        "ProtocolType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1242, version=0)
class Microsoft_Windows_PushNotifications_Platform_1242_0(Etw):
    pattern = Struct(
        "PowerManagementType" / Int32ul,
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1243, version=0)
class Microsoft_Windows_PushNotifications_Platform_1243_0(Etw):
    pattern = Struct(
        "PowerManagementType" / Int32ul,
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1244, version=0)
class Microsoft_Windows_PushNotifications_Platform_1244_0(Etw):
    pattern = Struct(
        "HostName" / WString,
        "Port" / Int16ul,
        "ProxyHostName" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1245, version=0)
class Microsoft_Windows_PushNotifications_Platform_1245_0(Etw):
    pattern = Struct(
        "HostName" / WString,
        "Port" / Int16ul,
        "ProxyHostName" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1247, version=0)
class Microsoft_Windows_PushNotifications_Platform_1247_0(Etw):
    pattern = Struct(
        "ControlChannelTriggerStatus" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1248, version=0)
class Microsoft_Windows_PushNotifications_Platform_1248_0(Etw):
    pattern = Struct(
        "HostName" / WString,
        "Port" / Int16ul,
        "ProxyHostName" / WString,
        "HttpStatus" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1251, version=0)
class Microsoft_Windows_PushNotifications_Platform_1251_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1254, version=0)
class Microsoft_Windows_PushNotifications_Platform_1254_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul,
        "OldIndex" / Int32ul,
        "OldAddressFamily" / Int32ul,
        "NewIndex" / Int32ul,
        "NewAddressFamily" / Int32ul,
        "NewPhysicalMediumType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1255, version=0)
class Microsoft_Windows_PushNotifications_Platform_1255_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1256, version=0)
class Microsoft_Windows_PushNotifications_Platform_1256_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1257, version=0)
class Microsoft_Windows_PushNotifications_Platform_1257_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1258, version=0)
class Microsoft_Windows_PushNotifications_Platform_1258_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul,
        "SocketError" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1261, version=0)
class Microsoft_Windows_PushNotifications_Platform_1261_0(Etw):
    pattern = Struct(
        "DeviceId" / CString,
        "UserId" / Int64ul,
        "UserType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1262, version=0)
class Microsoft_Windows_PushNotifications_Platform_1262_0(Etw):
    pattern = Struct(
        "DeviceId" / CString,
        "UserId" / Int64ul,
        "UserType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1263, version=0)
class Microsoft_Windows_PushNotifications_Platform_1263_0(Etw):
    pattern = Struct(
        "DeviceId" / CString,
        "OldUserId" / Int64ul,
        "OldUserType" / Int32ul,
        "NewUserId" / Int64ul,
        "NewUserType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1264, version=0)
class Microsoft_Windows_PushNotifications_Platform_1264_0(Etw):
    pattern = Struct(
        "DeviceId" / CString,
        "UserId" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1265, version=0)
class Microsoft_Windows_PushNotifications_Platform_1265_0(Etw):
    pattern = Struct(
        "DeviceId" / CString,
        "UserId" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1266, version=0)
class Microsoft_Windows_PushNotifications_Platform_1266_0(Etw):
    pattern = Struct(
        "DeviceId" / CString,
        "OldUserId" / Int64ul,
        "NewUserId" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1267, version=0)
class Microsoft_Windows_PushNotifications_Platform_1267_0(Etw):
    pattern = Struct(
        "Verb" / CString,
        "TrID" / Int32ul,
        "Namespace" / CString,
        "CorrelationVector" / CString,
        "Bytes" / Int32ul,
        "Payload" / Bytes(lambda this: this.Bytes),
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1268, version=0)
class Microsoft_Windows_PushNotifications_Platform_1268_0(Etw):
    pattern = Struct(
        "Verb" / CString,
        "TrID" / Int32ul,
        "Namespace" / CString,
        "CorrelationVector" / CString,
        "Bytes" / Int32ul,
        "Payload" / Bytes(lambda this: this.Bytes),
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1302, version=0)
class Microsoft_Windows_PushNotifications_Platform_1302_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl,
        "InitCount" / Int64sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1303, version=0)
class Microsoft_Windows_PushNotifications_Platform_1303_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl,
        "InitCount" / Int64sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1304, version=0)
class Microsoft_Windows_PushNotifications_Platform_1304_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl,
        "InitCount" / Int64sl,
        "PdcReason" / Int64sl,
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1305, version=0)
class Microsoft_Windows_PushNotifications_Platform_1305_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl,
        "InitCount" / Int64sl,
        "PdcReason" / Int64sl,
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1306, version=0)
class Microsoft_Windows_PushNotifications_Platform_1306_0(Etw):
    pattern = Struct(
        "DeviceId" / CString,
        "State" / Int64sl,
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1307, version=0)
class Microsoft_Windows_PushNotifications_Platform_1307_0(Etw):
    pattern = Struct(
        "ConnectorId" / Int32ul,
        "State" / Int64sl,
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1308, version=0)
class Microsoft_Windows_PushNotifications_Platform_1308_0(Etw):
    pattern = Struct(
        "ConnectorId" / Int32ul,
        "ConnectionType" / Int32ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1309, version=0)
class Microsoft_Windows_PushNotifications_Platform_1309_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1310, version=0)
class Microsoft_Windows_PushNotifications_Platform_1310_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul,
        "OldIndex" / Int32ul,
        "OldAddressFamily" / Int32ul,
        "NewIndex" / Int32ul,
        "NewAddressFamily" / Int32ul,
        "NewPhysicalMediumType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1311, version=0)
class Microsoft_Windows_PushNotifications_Platform_1311_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul,
        "OldIndex" / Int32ul,
        "OldAddressFamily" / Int32ul,
        "NewIndex" / Int32ul,
        "NewAddressFamily" / Int32ul,
        "NewPhysicalMediumType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1312, version=0)
class Microsoft_Windows_PushNotifications_Platform_1312_0(Etw):
    pattern = Struct(
        "TriggerValue" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1313, version=0)
class Microsoft_Windows_PushNotifications_Platform_1313_0(Etw):
    pattern = Struct(
        "TriggerValue" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1314, version=0)
class Microsoft_Windows_PushNotifications_Platform_1314_0(Etw):
    pattern = Struct(
        "TriggerValue" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=1315, version=0)
class Microsoft_Windows_PushNotifications_Platform_1315_0(Etw):
    pattern = Struct(
        "TriggerValue" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2000, version=0)
class Microsoft_Windows_PushNotifications_Platform_2000_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2001, version=0)
class Microsoft_Windows_PushNotifications_Platform_2001_0(Etw):
    pattern = Struct(
        "ChannelId" / WString,
        "AppUserModelId" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2002, version=0)
class Microsoft_Windows_PushNotifications_Platform_2002_0(Etw):
    pattern = Struct(
        "ChannelId" / WString,
        "AppUserModelId" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2003, version=0)
class Microsoft_Windows_PushNotifications_Platform_2003_0(Etw):
    pattern = Struct(
        "ChannelId" / WString,
        "AppUserModelId" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2004, version=0)
class Microsoft_Windows_PushNotifications_Platform_2004_0(Etw):
    pattern = Struct(
        "ChannelId" / WString,
        "AppUserModelId" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2005, version=0)
class Microsoft_Windows_PushNotifications_Platform_2005_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2006, version=0)
class Microsoft_Windows_PushNotifications_Platform_2006_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2007, version=0)
class Microsoft_Windows_PushNotifications_Platform_2007_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2008, version=0)
class Microsoft_Windows_PushNotifications_Platform_2008_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "NotificationType" / WString,
        "TrackingId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2009, version=0)
class Microsoft_Windows_PushNotifications_Platform_2009_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "NotificationType" / WString,
        "TrackingId" / Int32ul,
        "NotificationSource" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2010, version=0)
class Microsoft_Windows_PushNotifications_Platform_2010_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2011, version=0)
class Microsoft_Windows_PushNotifications_Platform_2011_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2012, version=0)
class Microsoft_Windows_PushNotifications_Platform_2012_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "TrackingId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2013, version=0)
class Microsoft_Windows_PushNotifications_Platform_2013_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2014, version=0)
class Microsoft_Windows_PushNotifications_Platform_2014_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "Tag" / WString,
        "Group" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2015, version=0)
class Microsoft_Windows_PushNotifications_Platform_2015_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2016, version=0)
class Microsoft_Windows_PushNotifications_Platform_2016_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2025, version=0)
class Microsoft_Windows_PushNotifications_Platform_2025_0(Etw):
    pattern = Struct(
        "TrackingId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2026, version=0)
class Microsoft_Windows_PushNotifications_Platform_2026_0(Etw):
    pattern = Struct(
        "TrackingId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2027, version=0)
class Microsoft_Windows_PushNotifications_Platform_2027_0(Etw):
    pattern = Struct(
        "TrackingId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2028, version=0)
class Microsoft_Windows_PushNotifications_Platform_2028_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "AppUserModelID" / WString,
        "TimerId" / Guid,
        "Duetime" / Int64ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2029, version=0)
class Microsoft_Windows_PushNotifications_Platform_2029_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "AppUserModelID" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2030, version=0)
class Microsoft_Windows_PushNotifications_Platform_2030_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "TimerId" / Guid,
        "Duetime" / Int64ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2031, version=0)
class Microsoft_Windows_PushNotifications_Platform_2031_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "EventId" / Guid
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2032, version=0)
class Microsoft_Windows_PushNotifications_Platform_2032_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "EventId" / Guid
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2033, version=0)
class Microsoft_Windows_PushNotifications_Platform_2033_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "EventId" / Guid,
        "NotificationId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2034, version=0)
class Microsoft_Windows_PushNotifications_Platform_2034_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2035, version=0)
class Microsoft_Windows_PushNotifications_Platform_2035_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "AppUserModelID" / WString,
        "TimerId" / Guid,
        "Duetime" / Int64ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2036, version=0)
class Microsoft_Windows_PushNotifications_Platform_2036_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "AppUserModelID" / WString,
        "TimerId" / Guid
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2037, version=0)
class Microsoft_Windows_PushNotifications_Platform_2037_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "TimerId" / Guid,
        "Duetime" / Int64ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2038, version=0)
class Microsoft_Windows_PushNotifications_Platform_2038_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "TimerId" / Guid,
        "Duetime" / Int64ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2039, version=0)
class Microsoft_Windows_PushNotifications_Platform_2039_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "AppUserModelID" / WString,
        "NotificationType" / Int32ul,
        "TimerId" / Guid,
        "URL" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2040, version=0)
class Microsoft_Windows_PushNotifications_Platform_2040_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "AppUserModelID" / WString,
        "NotificationType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2041, version=0)
class Microsoft_Windows_PushNotifications_Platform_2041_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "NotificationType" / Int32ul,
        "TimerId" / Guid
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2042, version=0)
class Microsoft_Windows_PushNotifications_Platform_2042_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "NotificationType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2043, version=0)
class Microsoft_Windows_PushNotifications_Platform_2043_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "NotificationType" / Int32ul,
        "URL" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2044, version=0)
class Microsoft_Windows_PushNotifications_Platform_2044_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "NotificationType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2045, version=0)
class Microsoft_Windows_PushNotifications_Platform_2045_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "NotificationType" / Int32ul,
        "URL" / WString,
        "Error" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2046, version=0)
class Microsoft_Windows_PushNotifications_Platform_2046_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2047, version=0)
class Microsoft_Windows_PushNotifications_Platform_2047_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2048, version=0)
class Microsoft_Windows_PushNotifications_Platform_2048_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "EventId" / Guid,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2049, version=0)
class Microsoft_Windows_PushNotifications_Platform_2049_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "NotificationType" / Int32ul,
        "URL" / WString,
        "HttpStatusCode" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2050, version=0)
class Microsoft_Windows_PushNotifications_Platform_2050_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "NotificationType" / Int32ul,
        "URL" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2051, version=0)
class Microsoft_Windows_PushNotifications_Platform_2051_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "NotificationType" / Int32ul,
        "URL" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2052, version=0)
class Microsoft_Windows_PushNotifications_Platform_2052_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "NotificationType" / Int32ul,
        "URL" / WString,
        "Error" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2053, version=0)
class Microsoft_Windows_PushNotifications_Platform_2053_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "NotificationType" / Int32ul,
        "URL" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2100, version=0)
class Microsoft_Windows_PushNotifications_Platform_2100_0(Etw):
    pattern = Struct(
        "ChannelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2101, version=0)
class Microsoft_Windows_PushNotifications_Platform_2101_0(Etw):
    pattern = Struct(
        "TrackingId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2102, version=0)
class Microsoft_Windows_PushNotifications_Platform_2102_0(Etw):
    pattern = Struct(
        "RequestFlags" / Int32ul,
        "TrackingId" / Int32ul,
        "NotificationType" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2103, version=0)
class Microsoft_Windows_PushNotifications_Platform_2103_0(Etw):
    pattern = Struct(
        "RequestFlags" / Int32ul,
        "TrackingId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2104, version=0)
class Microsoft_Windows_PushNotifications_Platform_2104_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "TrackingId" / Int32ul,
        "NotificationType" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2105, version=0)
class Microsoft_Windows_PushNotifications_Platform_2105_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "TrackingId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2106, version=0)
class Microsoft_Windows_PushNotifications_Platform_2106_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "TrackingId" / Int32ul,
        "NotificationType" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2107, version=0)
class Microsoft_Windows_PushNotifications_Platform_2107_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "TrackingId" / Int32ul,
        "NotificationType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2108, version=0)
class Microsoft_Windows_PushNotifications_Platform_2108_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "TrackingId" / Int32ul,
        "NotificationType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2109, version=0)
class Microsoft_Windows_PushNotifications_Platform_2109_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "NotificationType" / Int32ul,
        "Size" / Int64ul,
        "NetworkType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2110, version=0)
class Microsoft_Windows_PushNotifications_Platform_2110_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "TrackingId" / Int32ul,
        "NotificationType" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2111, version=0)
class Microsoft_Windows_PushNotifications_Platform_2111_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "NotificationType" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2112, version=0)
class Microsoft_Windows_PushNotifications_Platform_2112_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "TrackingId" / Int32ul,
        "NotificationType" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2150, version=0)
class Microsoft_Windows_PushNotifications_Platform_2150_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "SettingType" / Int32ul,
        "Enabled" / Int8ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2151, version=0)
class Microsoft_Windows_PushNotifications_Platform_2151_0(Etw):
    pattern = Struct(
        "Enabled" / Int8ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2152, version=0)
class Microsoft_Windows_PushNotifications_Platform_2152_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "SettingType" / Int32ul,
        "Enabled" / Int8ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2153, version=0)
class Microsoft_Windows_PushNotifications_Platform_2153_0(Etw):
    pattern = Struct(
        "SettingType" / Int32ul,
        "Enabled" / Int8ul,
        "PolicyLevel" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2154, version=0)
class Microsoft_Windows_PushNotifications_Platform_2154_0(Etw):
    pattern = Struct(
        "SettingType" / Int32ul,
        "Enabled" / Int8ul,
        "PolicyLevel" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2155, version=0)
class Microsoft_Windows_PushNotifications_Platform_2155_0(Etw):
    pattern = Struct(
        "SettingType" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2156, version=0)
class Microsoft_Windows_PushNotifications_Platform_2156_0(Etw):
    pattern = Struct(
        "SettingType" / Int32ul,
        "Cookie" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2157, version=0)
class Microsoft_Windows_PushNotifications_Platform_2157_0(Etw):
    pattern = Struct(
        "Cookie" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2159, version=0)
class Microsoft_Windows_PushNotifications_Platform_2159_0(Etw):
    pattern = Struct(
        "SettingsValue" / Int64ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2160, version=0)
class Microsoft_Windows_PushNotifications_Platform_2160_0(Etw):
    pattern = Struct(
        "SettingsValue" / Int64ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2161, version=0)
class Microsoft_Windows_PushNotifications_Platform_2161_0(Etw):
    pattern = Struct(
        "SettingsValue" / Int64ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2163, version=0)
class Microsoft_Windows_PushNotifications_Platform_2163_0(Etw):
    pattern = Struct(
        "SettingType" / Int32ul,
        "PackageFamilyName" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2165, version=0)
class Microsoft_Windows_PushNotifications_Platform_2165_0(Etw):
    pattern = Struct(
        "Enabled" / Int8ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2166, version=0)
class Microsoft_Windows_PushNotifications_Platform_2166_0(Etw):
    pattern = Struct(
        "WakeupTime" / Int64ul,
        "IsValid" / Int8ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2167, version=0)
class Microsoft_Windows_PushNotifications_Platform_2167_0(Etw):
    pattern = Struct(
        "WakeupTime" / Int64ul,
        "IsValid" / Int8ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2169, version=0)
class Microsoft_Windows_PushNotifications_Platform_2169_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2170, version=0)
class Microsoft_Windows_PushNotifications_Platform_2170_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "CollectionId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2200, version=0)
class Microsoft_Windows_PushNotifications_Platform_2200_0(Etw):
    pattern = Struct(
        "RequestFlags" / Int32ul,
        "AppUserModelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2201, version=0)
class Microsoft_Windows_PushNotifications_Platform_2201_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2202, version=0)
class Microsoft_Windows_PushNotifications_Platform_2202_0(Etw):
    pattern = Struct(
        "TrackingId" / Int32ul,
        "NotificationType" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2203, version=0)
class Microsoft_Windows_PushNotifications_Platform_2203_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "TrackingId" / Int32ul,
        "NotificationType" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2250, version=0)
class Microsoft_Windows_PushNotifications_Platform_2250_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2300, version=0)
class Microsoft_Windows_PushNotifications_Platform_2300_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "PackageRelativeApplicationId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2301, version=0)
class Microsoft_Windows_PushNotifications_Platform_2301_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "PackageRelativeApplicationId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2400, version=0)
class Microsoft_Windows_PushNotifications_Platform_2400_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "AppUserModelId" / WString,
        "Capabilities" / Int32ul,
        "WNFEventNameLength" / Int32ul,
        "WNFEventName" / Bytes(lambda this: this.WNFEventNameLength)
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2401, version=0)
class Microsoft_Windows_PushNotifications_Platform_2401_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2402, version=0)
class Microsoft_Windows_PushNotifications_Platform_2402_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2403, version=0)
class Microsoft_Windows_PushNotifications_Platform_2403_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2404, version=0)
class Microsoft_Windows_PushNotifications_Platform_2404_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "PhoneVoipAgentId" / Guid
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2405, version=0)
class Microsoft_Windows_PushNotifications_Platform_2405_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2406, version=0)
class Microsoft_Windows_PushNotifications_Platform_2406_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "AppUserModelId" / WString,
        "ChannelName" / WString,
        "ServiceName" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2407, version=0)
class Microsoft_Windows_PushNotifications_Platform_2407_0(Etw):
    pattern = Struct(
        "ChannelId" / WString,
        "NotificationType" / WString,
        "TrackingId" / Int32ul,
        "AppUserModelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2408, version=0)
class Microsoft_Windows_PushNotifications_Platform_2408_0(Etw):
    pattern = Struct(
        "ChannelId" / WString,
        "NotificationType" / WString,
        "TrackingId" / Int32ul,
        "AppUserModelId" / WString,
        "PhoneVoipAgentId" / Guid
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2409, version=0)
class Microsoft_Windows_PushNotifications_Platform_2409_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2410, version=0)
class Microsoft_Windows_PushNotifications_Platform_2410_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2411, version=0)
class Microsoft_Windows_PushNotifications_Platform_2411_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2412, version=0)
class Microsoft_Windows_PushNotifications_Platform_2412_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "IsConnected" / Int8ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2413, version=0)
class Microsoft_Windows_PushNotifications_Platform_2413_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "AppUserModelId" / WString,
        "AppSettings" / Int32ul,
        "AppType" / Int32ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2414, version=0)
class Microsoft_Windows_PushNotifications_Platform_2414_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "AppUserModelId" / WString,
        "AppSettings" / Int32ul,
        "AppType" / Int32ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=2415, version=0)
class Microsoft_Windows_PushNotifications_Platform_2415_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3000, version=0)
class Microsoft_Windows_PushNotifications_Platform_3000_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3001, version=0)
class Microsoft_Windows_PushNotifications_Platform_3001_0(Etw):
    pattern = Struct(
        "Endpoint" / Int64ul,
        "SessionId" / Int32ul,
        "Error" / Int32sl,
        "ProcessName" / WString,
        "QueuedTileCloses" / Int32sl,
        "QueuedTileCleanups" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3002, version=0)
class Microsoft_Windows_PushNotifications_Platform_3002_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3003, version=0)
class Microsoft_Windows_PushNotifications_Platform_3003_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Count" / Int32ul,
        "Error" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3004, version=0)
class Microsoft_Windows_PushNotifications_Platform_3004_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3005, version=0)
class Microsoft_Windows_PushNotifications_Platform_3005_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Error" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3006, version=0)
class Microsoft_Windows_PushNotifications_Platform_3006_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ProcessName" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3007, version=0)
class Microsoft_Windows_PushNotifications_Platform_3007_0(Etw):
    pattern = Struct(
        "Endpoint" / Int64ul,
        "SessionId" / Int32ul,
        "Error" / Int32sl,
        "ProcessName" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3008, version=0)
class Microsoft_Windows_PushNotifications_Platform_3008_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3009, version=0)
class Microsoft_Windows_PushNotifications_Platform_3009_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Error" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3012, version=0)
class Microsoft_Windows_PushNotifications_Platform_3012_0(Etw):
    pattern = Struct(
        "TrackingId" / Int32sl,
        "AppUserModelId" / WString,
        "SessionId" / Int32ul,
        "MessageId" / Guid
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3013, version=0)
class Microsoft_Windows_PushNotifications_Platform_3013_0(Etw):
    pattern = Struct(
        "NotificationType" / WString,
        "TrackingId" / Int32sl,
        "AppUserModelId" / WString,
        "SessionId" / Int32ul,
        "MessageId" / Guid,
        "ErrorCode" / Int32sl,
        "SessionErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3014, version=0)
class Microsoft_Windows_PushNotifications_Platform_3014_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3015, version=0)
class Microsoft_Windows_PushNotifications_Platform_3015_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "NotificationId" / Int32ul,
        "QueueIndex" / Int16ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3016, version=0)
class Microsoft_Windows_PushNotifications_Platform_3016_0(Etw):
    pattern = Struct(
        "OverridedNotificationId" / Int32ul,
        "OverridingNotificationId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3017, version=0)
class Microsoft_Windows_PushNotifications_Platform_3017_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "SessionMask" / Int32ul,
        "Flag" / Int16ul,
        "UpdateIndex" / Int16ul,
        "KeystoneNotificationId" / Int32ul,
        "KeystoneFlag" / Int16ul,
        "Appspace" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3018, version=0)
class Microsoft_Windows_PushNotifications_Platform_3018_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "TrackingId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3019, version=0)
class Microsoft_Windows_PushNotifications_Platform_3019_0(Etw):
    pattern = Struct(
        "RequestId" / Int32ul,
        "RequestCountInHighPriority" / Int32ul,
        "RequestCountInMedPriority" / Int32ul,
        "RequestCountInLowPriority" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3020, version=0)
class Microsoft_Windows_PushNotifications_Platform_3020_0(Etw):
    pattern = Struct(
        "RequestId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3021, version=0)
class Microsoft_Windows_PushNotifications_Platform_3021_0(Etw):
    pattern = Struct(
        "PriorityIndex" / Int32ul,
        "AppUserModelId" / WString,
        "NotificationId" / Int32ul,
        "URLCount" / Int32ul,
        "Flag" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3022, version=0)
class Microsoft_Windows_PushNotifications_Platform_3022_0(Etw):
    pattern = Struct(
        "ResourceId" / Int32ul,
        "URL" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3023, version=0)
class Microsoft_Windows_PushNotifications_Platform_3023_0(Etw):
    pattern = Struct(
        "NotificationId" / Int32ul,
        "ResourceId" / Int32ul,
        "LocalPath" / WString,
        "ErrorCode" / Int32sl,
        "Flag" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3024, version=0)
class Microsoft_Windows_PushNotifications_Platform_3024_0(Etw):
    pattern = Struct(
        "NotificationId" / Int32ul,
        "Flag" / Int32ul,
        "Count" / Int32ul,
        "URLComplete" / Int8ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3025, version=0)
class Microsoft_Windows_PushNotifications_Platform_3025_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "NotificationId" / Int32ul,
        "URLCount" / Int32ul,
        "Flag" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3026, version=0)
class Microsoft_Windows_PushNotifications_Platform_3026_0(Etw):
    pattern = Struct(
        "ResourceId" / Int32ul,
        "URL" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3027, version=0)
class Microsoft_Windows_PushNotifications_Platform_3027_0(Etw):
    pattern = Struct(
        "SlotIndex" / Int32ul,
        "NotificationId" / Int32ul,
        "BITSPriority" / Int32ul,
        "IsTile" / Int8ul,
        "URL" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3028, version=0)
class Microsoft_Windows_PushNotifications_Platform_3028_0(Etw):
    pattern = Struct(
        "NotificationId" / Int32ul,
        "IsTile" / Int8ul,
        "Path" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3029, version=0)
class Microsoft_Windows_PushNotifications_Platform_3029_0(Etw):
    pattern = Struct(
        "NotificationId" / Int32ul,
        "IsTile" / Int8ul,
        "ErrorCode" / Int32sl,
        "URL" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3036, version=0)
class Microsoft_Windows_PushNotifications_Platform_3036_0(Etw):
    pattern = Struct(
        "IDM_Enabled" / Int8ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3037, version=0)
class Microsoft_Windows_PushNotifications_Platform_3037_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Count" / Int32ul,
        "UpdateControl" / Int8sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3038, version=0)
class Microsoft_Windows_PushNotifications_Platform_3038_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "RequestControl" / CString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3040, version=0)
class Microsoft_Windows_PushNotifications_Platform_3040_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3041, version=0)
class Microsoft_Windows_PushNotifications_Platform_3041_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3042, version=0)
class Microsoft_Windows_PushNotifications_Platform_3042_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3043, version=0)
class Microsoft_Windows_PushNotifications_Platform_3043_0(Etw):
    pattern = Struct(
        "NewNotificationId" / Int64ul,
        "OldNotificationId" / Int64ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3044, version=0)
class Microsoft_Windows_PushNotifications_Platform_3044_0(Etw):
    pattern = Struct(
        "NewNotificationId" / Int64ul,
        "OldNotificationId" / Int64ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3047, version=0)
class Microsoft_Windows_PushNotifications_Platform_3047_0(Etw):
    pattern = Struct(
        "NewNotificationId" / Int64ul,
        "OldNotificationId" / Int64ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3048, version=0)
class Microsoft_Windows_PushNotifications_Platform_3048_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "TrackingId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3049, version=0)
class Microsoft_Windows_PushNotifications_Platform_3049_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3050, version=0)
class Microsoft_Windows_PushNotifications_Platform_3050_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "NotificationId" / Int32ul,
        "QueueIndex" / Int16ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3051, version=0)
class Microsoft_Windows_PushNotifications_Platform_3051_0(Etw):
    pattern = Struct(
        "OverridedNotificationId" / Int32ul,
        "OverridingNotificationId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3052, version=0)
class Microsoft_Windows_PushNotifications_Platform_3052_0(Etw):
    pattern = Struct(
        "TrackingId" / Int32sl,
        "AppUserModelId" / WString,
        "SessionId" / Int32ul,
        "MessageId" / Guid
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3053, version=0)
class Microsoft_Windows_PushNotifications_Platform_3053_0(Etw):
    pattern = Struct(
        "NotificationType" / WString,
        "TrackingId" / Int32sl,
        "AppUserModelId" / WString,
        "SessionId" / Int32ul,
        "MessageId" / Guid
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3054, version=0)
class Microsoft_Windows_PushNotifications_Platform_3054_0(Etw):
    pattern = Struct(
        "TrackingId" / Int32sl,
        "AppUserModelId" / WString,
        "SessionId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3055, version=0)
class Microsoft_Windows_PushNotifications_Platform_3055_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3056, version=0)
class Microsoft_Windows_PushNotifications_Platform_3056_0(Etw):
    pattern = Struct(
        "NotificationType" / Int32ul,
        "AppUserModelId" / WString,
        "SessionId" / Int32ul,
        "ErrorCode" / Int32sl,
        "SessionErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3057, version=0)
class Microsoft_Windows_PushNotifications_Platform_3057_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3058, version=0)
class Microsoft_Windows_PushNotifications_Platform_3058_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3104, version=0)
class Microsoft_Windows_PushNotifications_Platform_3104_0(Etw):
    pattern = Struct(
        "TrackingId" / Int32ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3107, version=0)
class Microsoft_Windows_PushNotifications_Platform_3107_0(Etw):
    pattern = Struct(
        "ChannelId" / WString,
        "NotificationType" / WString,
        "TrackingId" / Int32ul,
        "AppUserModelId" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3110, version=0)
class Microsoft_Windows_PushNotifications_Platform_3110_0(Etw):
    pattern = Struct(
        "IsFwdToCdpEnabled" / Int8ul,
        "IsMirrorMasterSwitchEnabled" / Int8ul,
        "MirroringEnabled" / Int8ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3113, version=0)
class Microsoft_Windows_PushNotifications_Platform_3113_0(Etw):
    pattern = Struct(
        "IsFwdToCdpEnabled" / Int8ul,
        "IsMirrorMasterSwitchEnabled" / Int8ul,
        "IsGPEnabled" / Int8ul
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3123, version=0)
class Microsoft_Windows_PushNotifications_Platform_3123_0(Etw):
    pattern = Struct(
        "TrackingId" / Int32ul,
        "AppUserModelId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3124, version=0)
class Microsoft_Windows_PushNotifications_Platform_3124_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3125, version=0)
class Microsoft_Windows_PushNotifications_Platform_3125_0(Etw):
    pattern = Struct(
        "VerboseLog" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3138, version=0)
class Microsoft_Windows_PushNotifications_Platform_3138_0(Etw):
    pattern = Struct(
        "VerboseLog" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3139, version=0)
class Microsoft_Windows_PushNotifications_Platform_3139_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3140, version=0)
class Microsoft_Windows_PushNotifications_Platform_3140_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3141, version=0)
class Microsoft_Windows_PushNotifications_Platform_3141_0(Etw):
    pattern = Struct(
        "MatchOnNotificationId" / Int8ul,
        "NotificationId" / Int32ul,
        "ActivityId" / WString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3145, version=0)
class Microsoft_Windows_PushNotifications_Platform_3145_0(Etw):
    pattern = Struct(
        "Error" / Int32sl,
        "Message" / CString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3146, version=0)
class Microsoft_Windows_PushNotifications_Platform_3146_0(Etw):
    pattern = Struct(
        "Error" / Int32sl,
        "Message" / CString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3147, version=0)
class Microsoft_Windows_PushNotifications_Platform_3147_0(Etw):
    pattern = Struct(
        "Error" / Int32sl,
        "Message" / CString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=3148, version=0)
class Microsoft_Windows_PushNotifications_Platform_3148_0(Etw):
    pattern = Struct(
        "Error" / Int32sl,
        "Message" / CString
    )


@declare(guid=guid("88cd9180-4491-4640-b571-e3bee2527943"), event_id=10000, version=0)
class Microsoft_Windows_PushNotifications_Platform_10000_0(Etw):
    pattern = Struct(
        "debugString" / WString
    )

