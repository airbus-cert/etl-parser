# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Search-Core
GUID : 49c2c27c-fe2d-40bf-8c4e-c3fb518037e7
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=17, version=0)
class Microsoft_Windows_Search_Core_17_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=18, version=1)
class Microsoft_Windows_Search_Core_18_1(Etw):
    pattern = Struct(
        "UsesFilter" / Int8ul,
        "UsesPropertyHandler" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=19, version=0)
class Microsoft_Windows_Search_Core_19_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Path" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=21, version=0)
class Microsoft_Windows_Search_Core_21_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Path" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=24, version=0)
class Microsoft_Windows_Search_Core_24_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=26, version=0)
class Microsoft_Windows_Search_Core_26_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=32, version=0)
class Microsoft_Windows_Search_Core_32_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=42, version=0)
class Microsoft_Windows_Search_Core_42_0(Etw):
    pattern = Struct(
        "ITrans" / Int64ul,
        "ResID" / Int32ul,
        "Status" / Int32ul,
        "Type" / Int32ul,
        "Flags" / Int32ul,
        "InternalFlags" / Int32ul,
        "CrawlNumber" / Int32ul,
        "CrawlType" / Int32ul,
        "Extra1" / Int32ul,
        "Extra2" / Int32ul,
        "Extra3" / Int32ul,
        "Path" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=43, version=0)
class Microsoft_Windows_Search_Core_43_0(Etw):
    pattern = Struct(
        "ITrans" / Int64ul,
        "ResID" / Int32ul,
        "Status" / Int32ul,
        "Type" / Int32ul,
        "Flags" / Int32ul,
        "InternalFlags" / Int32ul,
        "CrawlNumber" / Int32ul,
        "CrawlType" / Int32ul,
        "Extra1" / Int32ul,
        "Extra2" / Int32ul,
        "Extra3" / Int32ul,
        "Path" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=44, version=0)
class Microsoft_Windows_Search_Core_44_0(Etw):
    pattern = Struct(
        "Value" / Int64ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=46, version=0)
class Microsoft_Windows_Search_Core_46_0(Etw):
    pattern = Struct(
        "ITrans" / Int64ul,
        "ResID" / Int32ul,
        "Status" / Int32ul,
        "Type" / Int32ul,
        "Flags" / Int32ul,
        "InternalFlags" / Int32ul,
        "CrawlNumber" / Int32ul,
        "CrawlType" / Int32ul,
        "Extra1" / Int32ul,
        "Extra2" / Int32ul,
        "Extra3" / Int32ul,
        "Path" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=47, version=0)
class Microsoft_Windows_Search_Core_47_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=48, version=0)
class Microsoft_Windows_Search_Core_48_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=49, version=0)
class Microsoft_Windows_Search_Core_49_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=50, version=0)
class Microsoft_Windows_Search_Core_50_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=50, version=1)
class Microsoft_Windows_Search_Core_50_1(Etw):
    pattern = Struct(
        "QueryText" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=51, version=0)
class Microsoft_Windows_Search_Core_51_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=51, version=1)
class Microsoft_Windows_Search_Core_51_1(Etw):
    pattern = Struct(
        "QueryText" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=52, version=0)
class Microsoft_Windows_Search_Core_52_0(Etw):
    pattern = Struct(
        "ITrans" / Int64ul,
        "ResID" / Int32ul,
        "Status" / Int32ul,
        "Type" / Int32ul,
        "Flags" / Int32ul,
        "InternalFlags" / Int32ul,
        "CrawlNumber" / Int32ul,
        "CrawlType" / Int32ul,
        "Extra1" / Int32ul,
        "Extra2" / Int32ul,
        "Extra3" / Int32ul,
        "Path" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=53, version=0)
class Microsoft_Windows_Search_Core_53_0(Etw):
    pattern = Struct(
        "Value" / Int64ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=54, version=0)
class Microsoft_Windows_Search_Core_54_0(Etw):
    pattern = Struct(
        "Value" / Int64ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=54, version=1)
class Microsoft_Windows_Search_Core_54_1(Etw):
    pattern = Struct(
        "Level" / Int32ul,
        "Type" / Int64ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=55, version=0)
class Microsoft_Windows_Search_Core_55_0(Etw):
    pattern = Struct(
        "Value" / Int64ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=55, version=1)
class Microsoft_Windows_Search_Core_55_1(Etw):
    pattern = Struct(
        "Level" / Int32ul,
        "Type" / Int64ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=56, version=0)
class Microsoft_Windows_Search_Core_56_0(Etw):
    pattern = Struct(
        "ITrans" / Int64ul,
        "ResID" / Int32ul,
        "Status" / Int32ul,
        "Type" / Int32ul,
        "Flags" / Int32ul,
        "InternalFlags" / Int32ul,
        "CrawlNumber" / Int32ul,
        "CrawlType" / Int32ul,
        "Extra1" / Int32ul,
        "Extra2" / Int32ul,
        "Extra3" / Int32ul,
        "Path" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=57, version=0)
class Microsoft_Windows_Search_Core_57_0(Etw):
    pattern = Struct(
        "Rowset" / Int64ul,
        "Chapter" / Int64ul,
        "RowsToSkip" / Int64sl,
        "RowsRequested" / Int64sl,
        "RowsReturned" / Int64ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=58, version=0)
class Microsoft_Windows_Search_Core_58_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=59, version=0)
class Microsoft_Windows_Search_Core_59_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=60, version=0)
class Microsoft_Windows_Search_Core_60_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=61, version=0)
class Microsoft_Windows_Search_Core_61_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=62, version=0)
class Microsoft_Windows_Search_Core_62_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=63, version=0)
class Microsoft_Windows_Search_Core_63_0(Etw):
    pattern = Struct(
        "WaitHint" / Int32ul,
        "State" / Int32ul,
        "CheckPoint" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=64, version=0)
class Microsoft_Windows_Search_Core_64_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=65, version=0)
class Microsoft_Windows_Search_Core_65_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=66, version=0)
class Microsoft_Windows_Search_Core_66_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=67, version=0)
class Microsoft_Windows_Search_Core_67_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=68, version=0)
class Microsoft_Windows_Search_Core_68_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=69, version=0)
class Microsoft_Windows_Search_Core_69_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=70, version=0)
class Microsoft_Windows_Search_Core_70_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=71, version=0)
class Microsoft_Windows_Search_Core_71_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=74, version=0)
class Microsoft_Windows_Search_Core_74_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=75, version=0)
class Microsoft_Windows_Search_Core_75_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=76, version=0)
class Microsoft_Windows_Search_Core_76_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=77, version=0)
class Microsoft_Windows_Search_Core_77_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "hrReason" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=78, version=0)
class Microsoft_Windows_Search_Core_78_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "hrReason" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=79, version=1)
class Microsoft_Windows_Search_Core_79_1(Etw):
    pattern = Struct(
        "ProjectPtr" / Int64ul,
        "Status" / Int32ul,
        "hrReason" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=80, version=0)
class Microsoft_Windows_Search_Core_80_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=81, version=0)
class Microsoft_Windows_Search_Core_81_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=83, version=0)
class Microsoft_Windows_Search_Core_83_0(Etw):
    pattern = Struct(
        "IsCompact" / Int8ul,
        "CacheCapacity" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=84, version=0)
class Microsoft_Windows_Search_Core_84_0(Etw):
    pattern = Struct(
        "MaxWID" / Int32ul,
        "SDID" / Int32ul,
        "IsCompact" / Int8ul,
        "CacheCapacity" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=85, version=0)
class Microsoft_Windows_Search_Core_85_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=86, version=0)
class Microsoft_Windows_Search_Core_86_0(Etw):
    pattern = Struct(
        "MemAvail" / Int32ul,
        "MemTreshold" / Int32ul,
        "IsLow" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=87, version=0)
class Microsoft_Windows_Search_Core_87_0(Etw):
    pattern = Struct(
        "ACLineStatus" / Int8ul,
        "BackOffOnBattery" / Int8ul,
        "IsBackOffNeeded" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=88, version=0)
class Microsoft_Windows_Search_Core_88_0(Etw):
    pattern = Struct(
        "ACLineStatus" / Int8ul,
        "BatteryFlag" / Int8ul,
        "BatteryLifePercent" / Int8ul,
        "LowBatteryThreshold" / Int32ul,
        "IsLow" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=89, version=0)
class Microsoft_Windows_Search_Core_89_0(Etw):
    pattern = Struct(
        "DiskAvail" / Double,
        "LowDiskThreshold" / Int32ul,
        "IsLow" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=90, version=0)
class Microsoft_Windows_Search_Core_90_0(Etw):
    pattern = Struct(
        "Interval" / Int32ul,
        "IsUserActive" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=91, version=0)
class Microsoft_Windows_Search_Core_91_0(Etw):
    pattern = Struct(
        "Idle" / Double,
        "MaxIdle" / Int32ul,
        "IsHigh" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=92, version=0)
class Microsoft_Windows_Search_Core_92_0(Etw):
    pattern = Struct(
        "IORate" / Int32ul,
        "HighIOThreshold" / Int32ul,
        "IsHigh" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=93, version=0)
class Microsoft_Windows_Search_Core_93_0(Etw):
    pattern = Struct(
        "NotificationRate" / Int32ul,
        "HighNotificationThreshold" / Int32ul,
        "IsHigh" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=94, version=0)
class Microsoft_Windows_Search_Core_94_0(Etw):
    pattern = Struct(
        "PendingNotifications" / Int32ul,
        "NotificationsForceAtMost" / Int32ul,
        "NotificationsForced" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=95, version=0)
class Microsoft_Windows_Search_Core_95_0(Etw):
    pattern = Struct(
        "LastIndexNewItemReason" / Int32ul,
        "IndexNewItemReason" / Int32ul,
        "BackoffReason" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=96, version=0)
class Microsoft_Windows_Search_Core_96_0(Etw):
    pattern = Struct(
        "BackoffReason" / Int32ul,
        "IndexNewItemReason" / Int32ul,
        "AllReasons" / Int32ul,
        "FeatureDisabled" / Int32ul,
        "PowerSetting" / Int32ul,
        "BackoffRecoveryIsON" / Int8ul,
        "ProcessNotifications" / Int8ul,
        "BackOffOnPendingNotifications" / Int8ul,
        "PendingHiPriNotifications" / Int32ul,
        "BackOffOnPowerSetting" / Int8ul,
        "XPScreenSaverAndNoBattery" / Int8ul,
        "EnablePHBackoff" / Int8ul,
        "Merging" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=98, version=0)
class Microsoft_Windows_Search_Core_98_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "SID" / WString,
        "IsProcessWow64" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=99, version=0)
class Microsoft_Windows_Search_Core_99_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "SID" / WString,
        "IsProcessWow64" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=100, version=0)
class Microsoft_Windows_Search_Core_100_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "SID" / WString,
        "IsProcessWow64" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=101, version=0)
class Microsoft_Windows_Search_Core_101_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "SID" / WString,
        "IsProcessWow64" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=102, version=0)
class Microsoft_Windows_Search_Core_102_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "SID" / WString,
        "IsProcessWow64" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=103, version=0)
class Microsoft_Windows_Search_Core_103_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "SID" / WString,
        "IsProcessWow64" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=104, version=0)
class Microsoft_Windows_Search_Core_104_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "SID" / WString,
        "IsProcessWow64" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=105, version=0)
class Microsoft_Windows_Search_Core_105_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "SID" / WString,
        "IsProcessWow64" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=106, version=0)
class Microsoft_Windows_Search_Core_106_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "SID" / WString,
        "IsProcessWow64" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=107, version=0)
class Microsoft_Windows_Search_Core_107_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "SID" / WString,
        "IsProcessWow64" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=108, version=0)
class Microsoft_Windows_Search_Core_108_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "SID" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=109, version=0)
class Microsoft_Windows_Search_Core_109_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "SID" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=110, version=0)
class Microsoft_Windows_Search_Core_110_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "SID" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=112, version=0)
class Microsoft_Windows_Search_Core_112_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=113, version=0)
class Microsoft_Windows_Search_Core_113_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=114, version=0)
class Microsoft_Windows_Search_Core_114_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=115, version=0)
class Microsoft_Windows_Search_Core_115_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=122, version=0)
class Microsoft_Windows_Search_Core_122_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=123, version=0)
class Microsoft_Windows_Search_Core_123_0(Etw):
    pattern = Struct(
        "OldPath" / WString,
        "NewPath" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=124, version=0)
class Microsoft_Windows_Search_Core_124_0(Etw):
    pattern = Struct(
        "OldPath" / WString,
        "NewPath" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=125, version=0)
class Microsoft_Windows_Search_Core_125_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=126, version=0)
class Microsoft_Windows_Search_Core_126_0(Etw):
    pattern = Struct(
        "Value" / WString,
        "OldPrefix" / WString,
        "NewPrefix" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=127, version=0)
class Microsoft_Windows_Search_Core_127_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=128, version=0)
class Microsoft_Windows_Search_Core_128_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=129, version=0)
class Microsoft_Windows_Search_Core_129_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=130, version=0)
class Microsoft_Windows_Search_Core_130_0(Etw):
    pattern = Struct(
        "NoRun" / Int8ul,
        "SystemSetupOver" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=132, version=0)
class Microsoft_Windows_Search_Core_132_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=134, version=0)
class Microsoft_Windows_Search_Core_134_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=136, version=0)
class Microsoft_Windows_Search_Core_136_0(Etw):
    pattern = Struct(
        "NoRun" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=137, version=0)
class Microsoft_Windows_Search_Core_137_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=140, version=0)
class Microsoft_Windows_Search_Core_140_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=141, version=0)
class Microsoft_Windows_Search_Core_141_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=143, version=0)
class Microsoft_Windows_Search_Core_143_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "Message" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=145, version=0)
class Microsoft_Windows_Search_Core_145_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=147, version=0)
class Microsoft_Windows_Search_Core_147_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=148, version=0)
class Microsoft_Windows_Search_Core_148_0(Etw):
    pattern = Struct(
        "CrawlNo" / Int32ul,
        "CrawlType" / Int32ul,
        "FileName" / WString,
        "IsCatalogLevel" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=149, version=0)
class Microsoft_Windows_Search_Core_149_0(Etw):
    pattern = Struct(
        "CrawlNo" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=150, version=0)
class Microsoft_Windows_Search_Core_150_0(Etw):
    pattern = Struct(
        "CrawlNo" / Int32ul,
        "CrawlType" / Int32ul,
        "FileName" / WString,
        "IsCatalogLevel" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=151, version=0)
class Microsoft_Windows_Search_Core_151_0(Etw):
    pattern = Struct(
        "CrawlNo" / Int32ul,
        "StartPageName" / WString,
        "StartPageRefID" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=152, version=0)
class Microsoft_Windows_Search_Core_152_0(Etw):
    pattern = Struct(
        "CrawlNo" / Int32ul,
        "StartPageName" / WString,
        "StartPageRefID" / Int32ul,
        "CrawlIsInProgress" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=153, version=0)
class Microsoft_Windows_Search_Core_153_0(Etw):
    pattern = Struct(
        "CrawlNo" / Int32ul,
        "IsDone" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=154, version=0)
class Microsoft_Windows_Search_Core_154_0(Etw):
    pattern = Struct(
        "CrawlNo" / Int32ul,
        "CrawlType" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=155, version=0)
class Microsoft_Windows_Search_Core_155_0(Etw):
    pattern = Struct(
        "CrawlNo" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=156, version=0)
class Microsoft_Windows_Search_Core_156_0(Etw):
    pattern = Struct(
        "CrawlNo" / Int32ul,
        "URL" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=157, version=0)
class Microsoft_Windows_Search_Core_157_0(Etw):
    pattern = Struct(
        "CrawlNo" / Int32ul,
        "URL" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=159, version=0)
class Microsoft_Windows_Search_Core_159_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=160, version=0)
class Microsoft_Windows_Search_Core_160_0(Etw):
    pattern = Struct(
        "hrCode" / Int32ul,
        "URL" / WString,
        "TransactionType" / Int32ul,
        "StartAddressId" / Int32ul,
        "CrawlNo" / Int32ul,
        "DocId" / Int32ul,
        "hrTransactionError" / Int32ul,
        "Description" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=161, version=0)
class Microsoft_Windows_Search_Core_161_0(Etw):
    pattern = Struct(
        "hrCode" / Int32ul,
        "URL" / WString,
        "TransactionType" / Int32ul,
        "StartAddressId" / Int32ul,
        "CrawlNo" / Int32ul,
        "DocId" / Int32ul,
        "hrTransactionError" / Int32ul,
        "Description" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=162, version=0)
class Microsoft_Windows_Search_Core_162_0(Etw):
    pattern = Struct(
        "Resource" / Int64ul,
        "ChangeAdvice" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=163, version=0)
class Microsoft_Windows_Search_Core_163_0(Etw):
    pattern = Struct(
        "Resource" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=164, version=0)
class Microsoft_Windows_Search_Core_164_0(Etw):
    pattern = Struct(
        "Resource" / Int64ul,
        "TransactionURL" / WString,
        "TransactionType" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=170, version=0)
class Microsoft_Windows_Search_Core_170_0(Etw):
    pattern = Struct(
        "ITrans" / Int64ul,
        "ResID" / Int32ul,
        "Status" / Int32ul,
        "Type" / Int32ul,
        "Flags" / Int32ul,
        "InternalFlags" / Int32ul,
        "CrawlNumber" / Int32ul,
        "CrawlType" / Int32ul,
        "Extra1" / Int32ul,
        "Extra2" / Int32ul,
        "Extra3" / Int32ul,
        "Path" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=171, version=1)
class Microsoft_Windows_Search_Core_171_1(Etw):
    pattern = Struct(
        "ITrans" / Int64ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=172, version=1)
class Microsoft_Windows_Search_Core_172_1(Etw):
    pattern = Struct(
        "ITrans" / Int64ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=173, version=1)
class Microsoft_Windows_Search_Core_173_1(Etw):
    pattern = Struct(
        "ITrans" / Int64ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=174, version=1)
class Microsoft_Windows_Search_Core_174_1(Etw):
    pattern = Struct(
        "ITrans" / Int64ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=175, version=1)
class Microsoft_Windows_Search_Core_175_1(Etw):
    pattern = Struct(
        "ITrans" / Int64ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=176, version=1)
class Microsoft_Windows_Search_Core_176_1(Etw):
    pattern = Struct(
        "ITrans" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=177, version=1)
class Microsoft_Windows_Search_Core_177_1(Etw):
    pattern = Struct(
        "ITrans" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=178, version=1)
class Microsoft_Windows_Search_Core_178_1(Etw):
    pattern = Struct(
        "ITrans" / Int64ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=179, version=1)
class Microsoft_Windows_Search_Core_179_1(Etw):
    pattern = Struct(
        "ITrans" / Int64ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=185, version=0)
class Microsoft_Windows_Search_Core_185_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=186, version=0)
class Microsoft_Windows_Search_Core_186_0(Etw):
    pattern = Struct(
        "ElementCount" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=187, version=0)
class Microsoft_Windows_Search_Core_187_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "ElementCount" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=188, version=0)
class Microsoft_Windows_Search_Core_188_0(Etw):
    pattern = Struct(
        "SearchRootURL" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=190, version=0)
class Microsoft_Windows_Search_Core_190_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=196, version=0)
class Microsoft_Windows_Search_Core_196_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=198, version=0)
class Microsoft_Windows_Search_Core_198_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=199, version=0)
class Microsoft_Windows_Search_Core_199_0(Etw):
    pattern = Struct(
        "ScopeRuleURL" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=201, version=0)
class Microsoft_Windows_Search_Core_201_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=204, version=0)
class Microsoft_Windows_Search_Core_204_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=205, version=0)
class Microsoft_Windows_Search_Core_205_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "IsIncluded" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=206, version=0)
class Microsoft_Windows_Search_Core_206_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "IsInclude" / Int8ul,
        "FollowFlags" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=207, version=0)
class Microsoft_Windows_Search_Core_207_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=208, version=0)
class Microsoft_Windows_Search_Core_208_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "IsInclude" / Int8ul,
        "IsDefault" / Int8ul,
        "OverrideChildren" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=209, version=0)
class Microsoft_Windows_Search_Core_209_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=210, version=0)
class Microsoft_Windows_Search_Core_210_0(Etw):
    pattern = Struct(
        "SearchRootURL" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=211, version=0)
class Microsoft_Windows_Search_Core_211_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=212, version=0)
class Microsoft_Windows_Search_Core_212_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "IsInclude" / Int8ul,
        "OverrideChildren" / Int8ul,
        "FollowFlags" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=213, version=0)
class Microsoft_Windows_Search_Core_213_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=215, version=0)
class Microsoft_Windows_Search_Core_215_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=217, version=0)
class Microsoft_Windows_Search_Core_217_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=218, version=0)
class Microsoft_Windows_Search_Core_218_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=219, version=0)
class Microsoft_Windows_Search_Core_219_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "ScopeId" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=220, version=0)
class Microsoft_Windows_Search_Core_220_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=221, version=0)
class Microsoft_Windows_Search_Core_221_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "HasChildRule" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=222, version=0)
class Microsoft_Windows_Search_Core_222_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=223, version=0)
class Microsoft_Windows_Search_Core_223_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "HasParentRule" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=224, version=0)
class Microsoft_Windows_Search_Core_224_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=225, version=0)
class Microsoft_Windows_Search_Core_225_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "IsIncluded" / Int8ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=226, version=0)
class Microsoft_Windows_Search_Core_226_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=227, version=0)
class Microsoft_Windows_Search_Core_227_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=228, version=0)
class Microsoft_Windows_Search_Core_228_0(Etw):
    pattern = Struct(
        "SearchRootURL" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=229, version=0)
class Microsoft_Windows_Search_Core_229_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=230, version=0)
class Microsoft_Windows_Search_Core_230_0(Etw):
    pattern = Struct(
        "ScopeRuleURL" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=231, version=0)
class Microsoft_Windows_Search_Core_231_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=233, version=0)
class Microsoft_Windows_Search_Core_233_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=235, version=0)
class Microsoft_Windows_Search_Core_235_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=236, version=0)
class Microsoft_Windows_Search_Core_236_0(Etw):
    pattern = Struct(
        "SearchRootURL" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=237, version=0)
class Microsoft_Windows_Search_Core_237_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "SearchRootURL" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=238, version=0)
class Microsoft_Windows_Search_Core_238_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=239, version=0)
class Microsoft_Windows_Search_Core_239_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=240, version=0)
class Microsoft_Windows_Search_Core_240_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "Value" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=241, version=0)
class Microsoft_Windows_Search_Core_241_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=242, version=0)
class Microsoft_Windows_Search_Core_242_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "Value" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=243, version=0)
class Microsoft_Windows_Search_Core_243_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "Value" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=244, version=0)
class Microsoft_Windows_Search_Core_244_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "Value" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=245, version=0)
class Microsoft_Windows_Search_Core_245_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "Value" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=246, version=0)
class Microsoft_Windows_Search_Core_246_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=247, version=0)
class Microsoft_Windows_Search_Core_247_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=248, version=0)
class Microsoft_Windows_Search_Core_248_0(Etw):
    pattern = Struct(
        "Value" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=249, version=0)
class Microsoft_Windows_Search_Core_249_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=250, version=0)
class Microsoft_Windows_Search_Core_250_0(Etw):
    pattern = Struct(
        "Value" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=251, version=0)
class Microsoft_Windows_Search_Core_251_0(Etw):
    pattern = Struct(
        "Value" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=252, version=0)
class Microsoft_Windows_Search_Core_252_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=253, version=0)
class Microsoft_Windows_Search_Core_253_0(Etw):
    pattern = Struct(
        "Value" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=254, version=0)
class Microsoft_Windows_Search_Core_254_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "Value" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=255, version=0)
class Microsoft_Windows_Search_Core_255_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "Value" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=256, version=0)
class Microsoft_Windows_Search_Core_256_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "Value" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=257, version=0)
class Microsoft_Windows_Search_Core_257_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=259, version=0)
class Microsoft_Windows_Search_Core_259_0(Etw):
    pattern = Struct(
        "Resource" / Int64ul,
        "TransactionURL" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=260, version=0)
class Microsoft_Windows_Search_Core_260_0(Etw):
    pattern = Struct(
        "WorkId" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=261, version=0)
class Microsoft_Windows_Search_Core_261_0(Etw):
    pattern = Struct(
        "WorkId" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=262, version=0)
class Microsoft_Windows_Search_Core_262_0(Etw):
    pattern = Struct(
        "WorkId" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=263, version=0)
class Microsoft_Windows_Search_Core_263_0(Etw):
    pattern = Struct(
        "WorkId" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=264, version=0)
class Microsoft_Windows_Search_Core_264_0(Etw):
    pattern = Struct(
        "WorkId" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=265, version=0)
class Microsoft_Windows_Search_Core_265_0(Etw):
    pattern = Struct(
        "NumWID" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=266, version=0)
class Microsoft_Windows_Search_Core_266_0(Etw):
    pattern = Struct(
        "GathererCodeLocation" / Int32ul,
        "TransactionsInFile" / Int32ul,
        "TransactionsInMemory" / Int32ul,
        "TransactionQueueLength" / Int32ul,
        "TransactionsInFileNotifications" / Int32ul,
        "TransactionsInMemoryNotifications" / Int32ul,
        "TransactionQueueLengthNotifications" / Int32ul,
        "TransactionsHighLimit" / Int32ul,
        "TransactionsLowLimitPerCrawl" / Int32ul,
        "TransactionsHighLimitPerCrawl" / Int32ul,
        "TransactionsInIncrementalQueue" / Int32ul,
        "TransactionsInNotificationQueue" / Int32ul,
        "TansactionsInNotificationHighPriorityQueue" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=271, version=0)
class Microsoft_Windows_Search_Core_271_0(Etw):
    pattern = Struct(
        "Qid" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=272, version=0)
class Microsoft_Windows_Search_Core_272_0(Etw):
    pattern = Struct(
        "ObjectWid" / Int32ul,
        "KeyPid" / Int32ul,
        "GroupPids" / WString,
        "KeyStr" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=273, version=0)
class Microsoft_Windows_Search_Core_273_0(Etw):
    pattern = Struct(
        "ObjectWid" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=274, version=0)
class Microsoft_Windows_Search_Core_274_0(Etw):
    pattern = Struct(
        "ObjectWid" / Int32ul,
        "KeyStartPid" / Int32ul,
        "GroupPids" / WString,
        "KeyEndStr" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=275, version=0)
class Microsoft_Windows_Search_Core_275_0(Etw):
    pattern = Struct(
        "ObjectWid" / Int32ul,
        "StackCount" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=276, version=0)
class Microsoft_Windows_Search_Core_276_0(Etw):
    pattern = Struct(
        "ObjectWid" / Int32ul,
        "UseQueryPerfOpt" / Int8ul,
        "Restarted" / Int8ul,
        "IndexIds" / WString,
        "TotalSizeInPages" / Int32ul,
        "MaxWid" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=277, version=0)
class Microsoft_Windows_Search_Core_277_0(Etw):
    pattern = Struct(
        "ObjectWid" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=278, version=0)
class Microsoft_Windows_Search_Core_278_0(Etw):
    pattern = Struct(
        "WordListId" / Int64ul,
        "KeyTargetPid" / Int32ul,
        "KeyTargetStr" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=279, version=0)
class Microsoft_Windows_Search_Core_279_0(Etw):
    pattern = Struct(
        "WordListId" / Int64ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=280, version=0)
class Microsoft_Windows_Search_Core_280_0(Etw):
    pattern = Struct(
        "WordListId" / Int64ul,
        "KeyStartPid" / Int32ul,
        "GroupPids" / WString,
        "KeyEndStr" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=281, version=0)
class Microsoft_Windows_Search_Core_281_0(Etw):
    pattern = Struct(
        "WordListId" / Int64ul,
        "StackCount" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=282, version=0)
class Microsoft_Windows_Search_Core_282_0(Etw):
    pattern = Struct(
        "Qid" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=283, version=0)
class Microsoft_Windows_Search_Core_283_0(Etw):
    pattern = Struct(
        "Qid" / Int32ul,
        "BytesSent" / Int32ul,
        "MessageId" / Int32sl
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=284, version=0)
class Microsoft_Windows_Search_Core_284_0(Etw):
    pattern = Struct(
        "Qid" / Int32ul,
        "BytesReceived" / Int32ul,
        "MessageId" / Int32sl
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=285, version=0)
class Microsoft_Windows_Search_Core_285_0(Etw):
    pattern = Struct(
        "BytesSent" / Int32ul,
        "MessageId" / Int32sl
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=286, version=0)
class Microsoft_Windows_Search_Core_286_0(Etw):
    pattern = Struct(
        "BytesReceived" / Int32ul,
        "MessageId" / Int32sl
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=287, version=0)
class Microsoft_Windows_Search_Core_287_0(Etw):
    pattern = Struct(
        "Qid" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=288, version=0)
class Microsoft_Windows_Search_Core_288_0(Etw):
    pattern = Struct(
        "Qid" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=289, version=0)
class Microsoft_Windows_Search_Core_289_0(Etw):
    pattern = Struct(
        "Rowset" / Int64ul,
        "Chapter" / Int64ul,
        "RowsRequested" / Int64sl,
        "RowSeekMethod" / Int32sl,
        "RowsToSkip" / Int64sl,
        "RowOffset" / Int32sl,
        "Bookmark" / Int32ul,
        "Bookmarks" / WString,
        "Numerator" / Int32ul,
        "Denominator" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=290, version=0)
class Microsoft_Windows_Search_Core_290_0(Etw):
    pattern = Struct(
        "Rowset" / Int64ul,
        "RowsReturned" / Int64sl,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=291, version=0)
class Microsoft_Windows_Search_Core_291_0(Etw):
    pattern = Struct(
        "Qid" / Int32ul,
        "WidStart" / Int32ul,
        "Chapter" / Int32ul,
        "Depth" / Int32ul,
        "RowOffset" / Int64sl,
        "RequestedRows" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=292, version=0)
class Microsoft_Windows_Search_Core_292_0(Etw):
    pattern = Struct(
        "Qid" / Int32ul,
        "RowsTransferred" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=293, version=0)
class Microsoft_Windows_Search_Core_293_0(Etw):
    pattern = Struct(
        "fmtid" / Guid,
        "pid" / Int32ul,
        "TextPrefix" / WString,
        "TextLength" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=294, version=0)
class Microsoft_Windows_Search_Core_294_0(Etw):
    pattern = Struct(
        "LocaleID" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=295, version=0)
class Microsoft_Windows_Search_Core_295_0(Etw):
    pattern = Struct(
        "LocaleName" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=296, version=0)
class Microsoft_Windows_Search_Core_296_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=297, version=0)
class Microsoft_Windows_Search_Core_297_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=298, version=0)
class Microsoft_Windows_Search_Core_298_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=300, version=0)
class Microsoft_Windows_Search_Core_300_0(Etw):
    pattern = Struct(
        "Qid" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=301, version=0)
class Microsoft_Windows_Search_Core_301_0(Etw):
    pattern = Struct(
        "Qid" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=302, version=0)
class Microsoft_Windows_Search_Core_302_0(Etw):
    pattern = Struct(
        "CBID" / Int64ul,
        "DocCount" / Int32ul,
        "BytesAvailable" / Int64ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=303, version=0)
class Microsoft_Windows_Search_Core_303_0(Etw):
    pattern = Struct(
        "CBID" / Int64ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=304, version=0)
class Microsoft_Windows_Search_Core_304_0(Etw):
    pattern = Struct(
        "Scheduled" / Int8ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=305, version=0)
class Microsoft_Windows_Search_Core_305_0(Etw):
    pattern = Struct(
        "AvailableCBCount" / Int32ul,
        "DirtyCBCount" / Int32ul,
        "InUseCBCount" / Int32ul,
        "PublishedCBCount" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=306, version=0)
class Microsoft_Windows_Search_Core_306_0(Etw):
    pattern = Struct(
        "DocID" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=307, version=0)
class Microsoft_Windows_Search_Core_307_0(Etw):
    pattern = Struct(
        "DocID" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=308, version=0)
class Microsoft_Windows_Search_Core_308_0(Etw):
    pattern = Struct(
        "DocID" / Int32ul,
        "BytesAvailable" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=309, version=0)
class Microsoft_Windows_Search_Core_309_0(Etw):
    pattern = Struct(
        "DocID" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=310, version=0)
class Microsoft_Windows_Search_Core_310_0(Etw):
    pattern = Struct(
        "DocID" / Int32ul,
        "CBID" / Int64ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=311, version=0)
class Microsoft_Windows_Search_Core_311_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=312, version=0)
class Microsoft_Windows_Search_Core_312_0(Etw):
    pattern = Struct(
        "DocID" / Int32ul,
        "PropID" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=313, version=0)
class Microsoft_Windows_Search_Core_313_0(Etw):
    pattern = Struct(
        "IsCompact" / Int8ul,
        "CacheCapacity" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=314, version=0)
class Microsoft_Windows_Search_Core_314_0(Etw):
    pattern = Struct(
        "NumWID" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=315, version=0)
class Microsoft_Windows_Search_Core_315_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=316, version=0)
class Microsoft_Windows_Search_Core_316_0(Etw):
    pattern = Struct(
        "MaxWID" / Int32ul,
        "Scope" / Int32ul,
        "IsCompact" / Int8ul,
        "CacheCapacity" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=317, version=0)
class Microsoft_Windows_Search_Core_317_0(Etw):
    pattern = Struct(
        "RequestID" / Int64ul,
        "Priority" / Int32ul,
        "Indexed" / Int32ul,
        "OutstandingAdds" / Int32ul,
        "OutstandingModifies" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=318, version=0)
class Microsoft_Windows_Search_Core_318_0(Etw):
    pattern = Struct(
        "RequestID" / Int64ul,
        "Priority" / Int32ul,
        "Indexed" / Int32ul,
        "OutstandingAdds" / Int32ul,
        "OutstandingModifies" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=319, version=0)
class Microsoft_Windows_Search_Core_319_0(Etw):
    pattern = Struct(
        "RequestID" / Int64ul,
        "Priority" / Int32ul,
        "Indexed" / Int32ul,
        "OutstandingAdds" / Int32ul,
        "OutstandingModifies" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=320, version=0)
class Microsoft_Windows_Search_Core_320_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "Value" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=321, version=0)
class Microsoft_Windows_Search_Core_321_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "URL" / WString,
        "DocID" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=322, version=0)
class Microsoft_Windows_Search_Core_322_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=323, version=0)
class Microsoft_Windows_Search_Core_323_0(Etw):
    pattern = Struct(
        "Hr" / Int32ul,
        "Info" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=324, version=0)
class Microsoft_Windows_Search_Core_324_0(Etw):
    pattern = Struct(
        "DocID" / Int32ul,
        "URL" / WString,
        "Info" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=325, version=0)
class Microsoft_Windows_Search_Core_325_0(Etw):
    pattern = Struct(
        "Hr" / Int32ul,
        "DocID" / Int32ul,
        "URL" / WString,
        "Info" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=326, version=0)
class Microsoft_Windows_Search_Core_326_0(Etw):
    pattern = Struct(
        "Volume" / WString,
        "DesiredPosition" / Int64sl,
        "CurrentPosition" / Int64sl,
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=328, version=0)
class Microsoft_Windows_Search_Core_328_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=329, version=0)
class Microsoft_Windows_Search_Core_329_0(Etw):
    pattern = Struct(
        "Locale" / Int32ul,
        "IdxName" / CString,
        "IsShadow" / Int8ul,
        "ColumnType" / Int64ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=330, version=0)
class Microsoft_Windows_Search_Core_330_0(Etw):
    pattern = Struct(
        "Locale" / Int32ul,
        "IdxName" / CString,
        "IsShadow" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=331, version=0)
class Microsoft_Windows_Search_Core_331_0(Etw):
    pattern = Struct(
        "SeekType" / WString,
        "ColumnType" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=332, version=0)
class Microsoft_Windows_Search_Core_332_0(Etw):
    pattern = Struct(
        "SeekType" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=333, version=0)
class Microsoft_Windows_Search_Core_333_0(Etw):
    pattern = Struct(
        "HasStartVariant" / Int8ul,
        "HasEndVariant" / Int8ul,
        "ExcludeStartVariant" / Int8ul,
        "ExcludeEndVariant" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=334, version=0)
class Microsoft_Windows_Search_Core_334_0(Etw):
    pattern = Struct(
        "RangeSet" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=335, version=0)
class Microsoft_Windows_Search_Core_335_0(Etw):
    pattern = Struct(
        "Qid" / Int32ul,
        "Cursor" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=336, version=0)
class Microsoft_Windows_Search_Core_336_0(Etw):
    pattern = Struct(
        "WhereID" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=337, version=0)
class Microsoft_Windows_Search_Core_337_0(Etw):
    pattern = Struct(
        "Qid" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=338, version=0)
class Microsoft_Windows_Search_Core_338_0(Etw):
    pattern = Struct(
        "Qid" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=339, version=0)
class Microsoft_Windows_Search_Core_339_0(Etw):
    pattern = Struct(
        "Locale" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=340, version=0)
class Microsoft_Windows_Search_Core_340_0(Etw):
    pattern = Struct(
        "Locale" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=341, version=0)
class Microsoft_Windows_Search_Core_341_0(Etw):
    pattern = Struct(
        "Locale" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=342, version=0)
class Microsoft_Windows_Search_Core_342_0(Etw):
    pattern = Struct(
        "Locale" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=343, version=0)
class Microsoft_Windows_Search_Core_343_0(Etw):
    pattern = Struct(
        "Locale" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=344, version=0)
class Microsoft_Windows_Search_Core_344_0(Etw):
    pattern = Struct(
        "Locale" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=345, version=0)
class Microsoft_Windows_Search_Core_345_0(Etw):
    pattern = Struct(
        "Locale" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=346, version=0)
class Microsoft_Windows_Search_Core_346_0(Etw):
    pattern = Struct(
        "Locale" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=347, version=0)
class Microsoft_Windows_Search_Core_347_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "Message" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=348, version=0)
class Microsoft_Windows_Search_Core_348_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "Message" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=349, version=0)
class Microsoft_Windows_Search_Core_349_0(Etw):
    pattern = Struct(
        "fmtid" / Guid,
        "pid" / Int32ul,
        "LocaleID" / Int32ul,
        "LocaleSource" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=350, version=0)
class Microsoft_Windows_Search_Core_350_0(Etw):
    pattern = Struct(
        "Locale" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=351, version=0)
class Microsoft_Windows_Search_Core_351_0(Etw):
    pattern = Struct(
        "LocaleID" / Int32ul,
        "IncrementCallID" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=352, version=0)
class Microsoft_Windows_Search_Core_352_0(Etw):
    pattern = Struct(
        "LocaleOriginal" / Int32ul,
        "LocaleSubstitute" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=353, version=0)
class Microsoft_Windows_Search_Core_353_0(Etw):
    pattern = Struct(
        "LocaleID" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=354, version=0)
class Microsoft_Windows_Search_Core_354_0(Etw):
    pattern = Struct(
        "Data" / CString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=355, version=0)
class Microsoft_Windows_Search_Core_355_0(Etw):
    pattern = Struct(
        "Data" / CString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=356, version=0)
class Microsoft_Windows_Search_Core_356_0(Etw):
    pattern = Struct(
        "TextLength" / Int32ul,
        "TopLCID" / Int32ul,
        "TopScore" / Int32ul,
        "SecondLCID" / Int32ul,
        "SecondScore" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=358, version=0)
class Microsoft_Windows_Search_Core_358_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=360, version=0)
class Microsoft_Windows_Search_Core_360_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=362, version=0)
class Microsoft_Windows_Search_Core_362_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=365, version=0)
class Microsoft_Windows_Search_Core_365_0(Etw):
    pattern = Struct(
        "ScopeId" / Int32ul,
        "EventId" / Guid,
        "PackageFamilyName" / WString,
        "Path" / WString,
        "Result" / Int32ul,
        "SuccessEvent" / Int8ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=366, version=0)
class Microsoft_Windows_Search_Core_366_0(Etw):
    pattern = Struct(
        "ScopeId" / Int32ul
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=367, version=0)
class Microsoft_Windows_Search_Core_367_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "PackageFamilyName" / WString,
        "EventId" / Guid,
        "Count" / Int32ul,
        "Paths" / WString
    )


@declare(guid=guid("49c2c27c-fe2d-40bf-8c4e-c3fb518037e7"), event_id=369, version=0)
class Microsoft_Windows_Search_Core_369_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "PackageFamilyName" / WString,
        "EventId" / Guid
    )

