# -*- coding: utf-8 -*-
"""
Microsoft-Windows-BranchCache
GUID : 7eafcf79-06a7-460b-8a55-bd0a0c9248aa
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=4, version=0)
class Microsoft_Windows_BranchCache_4_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=5, version=0)
class Microsoft_Windows_BranchCache_5_0(Etw):
    pattern = Struct(
        "SubKey" / WString,
        "ValueName" / WString,
        "SettingType" / Int32ul,
        "UInt32" / Int32ul,
        "UInt64" / Int64ul,
        "String" / WString,
        "BinaryLength" / Int32ul,
        "Binary" / Bytes(lambda this: this.BinaryLength)
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=11, version=0)
class Microsoft_Windows_BranchCache_11_0(Etw):
    pattern = Struct(
        "CacheSize" / Int32ul
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=12, version=0)
class Microsoft_Windows_BranchCache_12_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=13, version=0)
class Microsoft_Windows_BranchCache_13_0(Etw):
    pattern = Struct(
        "cbContentId" / Int16ul,
        "ContentId" / Bytes(lambda this: this.cbContentId),
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=14, version=0)
class Microsoft_Windows_BranchCache_14_0(Etw):
    pattern = Struct(
        "cbSegmentId" / Int32ul,
        "SegmentId" / Bytes(lambda this: this.cbSegmentId),
        "BlockId" / Int32ul,
        "PeerAddress" / WString,
        "MessageType" / Int32ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=15, version=0)
class Microsoft_Windows_BranchCache_15_0(Etw):
    pattern = Struct(
        "cbSegmentId" / Int32ul,
        "SegmentId" / Bytes(lambda this: this.cbSegmentId),
        "BlockId" / Int32ul,
        "HostedCacheAddress" / WString,
        "MessageType" / Int32ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=16, version=0)
class Microsoft_Windows_BranchCache_16_0(Etw):
    pattern = Struct(
        "PeerAddress" / WString,
        "MinutesOfQuarantine" / Int32ul
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=17, version=0)
class Microsoft_Windows_BranchCache_17_0(Etw):
    pattern = Struct(
        "FromAddress" / WString,
        "MessageType" / Int32ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=18, version=0)
class Microsoft_Windows_BranchCache_18_0(Etw):
    pattern = Struct(
        "PeerAddress" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=19, version=0)
class Microsoft_Windows_BranchCache_19_0(Etw):
    pattern = Struct(
        "HostedCacheLocation" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=20, version=0)
class Microsoft_Windows_BranchCache_20_0(Etw):
    pattern = Struct(
        "HostedCacheLocation" / WString
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=21, version=0)
class Microsoft_Windows_BranchCache_21_0(Etw):
    pattern = Struct(
        "EventId" / Int32ul,
        "Count" / Int32ul
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=24, version=0)
class Microsoft_Windows_BranchCache_24_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "SubCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=25, version=0)
class Microsoft_Windows_BranchCache_25_0(Etw):
    pattern = Struct(
        "Timestamp" / SystemTime
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=26, version=0)
class Microsoft_Windows_BranchCache_26_0(Etw):
    pattern = Struct(
        "Timestamp" / SystemTime
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=27, version=0)
class Microsoft_Windows_BranchCache_27_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=29, version=0)
class Microsoft_Windows_BranchCache_29_0(Etw):
    pattern = Struct(
        "Port" / Int32ul
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=30, version=0)
class Microsoft_Windows_BranchCache_30_0(Etw):
    pattern = Struct(
        "CachePath" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=31, version=0)
class Microsoft_Windows_BranchCache_31_0(Etw):
    pattern = Struct(
        "cbSegmentId" / Int32ul,
        "SegmentId" / Bytes(lambda this: this.cbSegmentId),
        "BlockId" / Int32ul,
        "ClientAddress" / WString,
        "MessageType" / Int32ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=32, version=0)
class Microsoft_Windows_BranchCache_32_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "ConfiguredSize" / Int64ul,
        "ActualSize" / Int64ul
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=33, version=0)
class Microsoft_Windows_BranchCache_33_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "ConfiguredSize" / Int64ul,
        "ActualSize" / Int64ul
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=34, version=0)
class Microsoft_Windows_BranchCache_34_0(Etw):
    pattern = Struct(
        "ServerDNSName" / WString,
        "SiteName" / WString,
        "ExpiryTime" / SystemTime,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=35, version=0)
class Microsoft_Windows_BranchCache_35_0(Etw):
    pattern = Struct(
        "GUID" / WString,
        "ServerDNSName" / WString,
        "SiteName" / WString,
        "ExpiryTime" / SystemTime,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=36, version=0)
class Microsoft_Windows_BranchCache_36_0(Etw):
    pattern = Struct(
        "GUID" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=37, version=0)
class Microsoft_Windows_BranchCache_37_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=38, version=0)
class Microsoft_Windows_BranchCache_38_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=39, version=0)
class Microsoft_Windows_BranchCache_39_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "ConfiguredSize" / Int64ul,
        "ActualSize" / Int64ul
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=40, version=0)
class Microsoft_Windows_BranchCache_40_0(Etw):
    pattern = Struct(
        "HCClientAddress" / WString,
        "CurrentUploads" / Int32ul,
        "MaxUploads" / Int32ul
    )


@declare(guid=guid("7eafcf79-06a7-460b-8a55-bd0a0c9248aa"), event_id=41, version=0)
class Microsoft_Windows_BranchCache_41_0(Etw):
    pattern = Struct(
        "ListenPort" / Int16ul
    )

