# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Eventlog
GUID : fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=20, version=0)
class Microsoft_Windows_Eventlog_20_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Path" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=21, version=0)
class Microsoft_Windows_Eventlog_21_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ChannelPath" / WString,
        "ConfigProperty" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=22, version=0)
class Microsoft_Windows_Eventlog_22_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Path" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=23, version=0)
class Microsoft_Windows_Eventlog_23_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Path" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=25, version=0)
class Microsoft_Windows_Eventlog_25_0(Etw):
    pattern = Struct(
        "ChannelPath" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=26, version=0)
class Microsoft_Windows_Eventlog_26_0(Etw):
    pattern = Struct(
        "ChannelPath" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=27, version=0)
class Microsoft_Windows_Eventlog_27_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ChannelPath" / WString,
        "NewLogFilePath" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=27, version=1)
class Microsoft_Windows_Eventlog_27_1(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ChannelPath" / WString,
        "FailedLogFilePath" / WString,
        "NewLogFilePath" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=28, version=0)
class Microsoft_Windows_Eventlog_28_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ChannelPath" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=29, version=0)
class Microsoft_Windows_Eventlog_29_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ChannelPath" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=30, version=0)
class Microsoft_Windows_Eventlog_30_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ChannelPath" / WString,
        "PublisherGuid" / Guid
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=31, version=0)
class Microsoft_Windows_Eventlog_31_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ChannelPath" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=40, version=0)
class Microsoft_Windows_Eventlog_40_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ChannelPath" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=100, version=0)
class Microsoft_Windows_Eventlog_100_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "EventID" / Int16ul,
        "PubID" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=102, version=0)
class Microsoft_Windows_Eventlog_102_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "EventID" / Int16ul,
        "PublisherName" / WString,
        "PublisherGuid" / Guid,
        "ProcessID" / Int32ul
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=103, version=0)
class Microsoft_Windows_Eventlog_103_0(Etw):
    pattern = Struct(
        "Reason" / Int8ul,
        "SessionName" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=104, version=0)
class Microsoft_Windows_Eventlog_104_0(Etw):
    pattern = Struct(
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "Channel" / WString,
        "BackupPath" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=105, version=0)
class Microsoft_Windows_Eventlog_105_0(Etw):
    pattern = Struct(
        "Channel" / WString,
        "BackupPath" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=106, version=0)
class Microsoft_Windows_Eventlog_106_0(Etw):
    pattern = Struct(
        "Channel" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=107, version=0)
class Microsoft_Windows_Eventlog_107_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ProviderName" / WString,
        "PublisherGuid" / Guid
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=108, version=0)
class Microsoft_Windows_Eventlog_108_0(Etw):
    pattern = Struct(
        "ShutdownTime" / SystemTime,
        "ActualMaxInterval" / Int32ul,
        "DiskPmDisabledMaxInterval" / Int32ul,
        "DiskPmEnabledFlag" / Int32ul,
        "DiskPmEnabledMaxInterval" / Int32ul,
        "TimestampForced" / Int32ul,
        "DiskPmPolicy" / Int32ul,
        "BiasValid" / Int32ul,
        "StartBias" / Int32ul
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=109, version=0)
class Microsoft_Windows_Eventlog_109_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "EventID" / Int16ul,
        "PublisherName" / WString,
        "PublisherGuid" / Guid,
        "ProcessID" / Int32ul,
        "EventName" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=110, version=0)
class Microsoft_Windows_Eventlog_110_0(Etw):
    pattern = Struct(
        "PublisherGuid" / Guid,
        "PublisherName" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=111, version=0)
class Microsoft_Windows_Eventlog_111_0(Etw):
    pattern = Struct(
        "PublisherGuid" / Guid,
        "PublisherName" / WString,
        "EventMetaDataCount" / Int32ul
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=112, version=0)
class Microsoft_Windows_Eventlog_112_0(Etw):
    pattern = Struct(
        "PublisherGuid" / Guid,
        "PublisherName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=200, version=0)
class Microsoft_Windows_Eventlog_200_0(Etw):
    pattern = Struct(
        "ChannelName" / WString,
        "ChannelType" / Int8ul,
        "Enabled" / Int8ul
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=201, version=0)
class Microsoft_Windows_Eventlog_201_0(Etw):
    pattern = Struct(
        "ChannelName" / WString,
        "Query" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=202, version=0)
class Microsoft_Windows_Eventlog_202_0(Etw):
    pattern = Struct(
        "ChannelName" / WString,
        "Query" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=203, version=0)
class Microsoft_Windows_Eventlog_203_0(Etw):
    pattern = Struct(
        "ModuleNameLen" / Int8ul,
        "ModuleName" / Bytes(lambda this: this.ModuleNameLen)
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=204, version=0)
class Microsoft_Windows_Eventlog_204_0(Etw):
    pattern = Struct(
        "ModuleNameLen" / Int8ul,
        "ModuleName" / Bytes(lambda this: this.ModuleNameLen)
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=205, version=1)
class Microsoft_Windows_Eventlog_205_1(Etw):
    pattern = Struct(
        "ModuleNameLen" / Int8ul,
        "ModuleName" / Bytes(lambda this: this.ModuleNameLen)
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=205, version=2)
class Microsoft_Windows_Eventlog_205_2(Etw):
    pattern = Struct(
        "ModuleNameLen" / Int8ul,
        "ModuleName" / Bytes(lambda this: this.ModuleNameLen)
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=1101, version=0)
class Microsoft_Windows_Eventlog_1101_0(Etw):
    pattern = Struct(
        "Reason" / Int8ul
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=1102, version=0)
class Microsoft_Windows_Eventlog_1102_0(Etw):
    pattern = Struct(
        "SubjectUserSid" / Sid,
        "SubjectUserName" / WString,
        "SubjectDomainName" / WString,
        "SubjectLogonId" / Int64ul
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=1103, version=0)
class Microsoft_Windows_Eventlog_1103_0(Etw):
    pattern = Struct(
        "PercentFull" / Int32ul
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=1105, version=0)
class Microsoft_Windows_Eventlog_1105_0(Etw):
    pattern = Struct(
        "Channel" / WString,
        "BackupPath" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=1106, version=0)
class Microsoft_Windows_Eventlog_1106_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=1107, version=0)
class Microsoft_Windows_Eventlog_1107_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "EventID" / Int16ul,
        "PublisherName" / WString,
        "PublisherGuid" / Guid,
        "ProcessID" / Int32ul
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=1108, version=0)
class Microsoft_Windows_Eventlog_1108_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "EventID" / Int16ul,
        "PubID" / WString
    )


@declare(guid=guid("fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148"), event_id=6000, version=0)
class Microsoft_Windows_Eventlog_6000_0(Etw):
    pattern = Struct(
        "Channel" / WString
    )

