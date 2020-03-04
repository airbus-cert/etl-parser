# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DateTimeControlPanel
GUID : 741fc222-44ed-4ba7-98e3-f405b2d2c4b4
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("741fc222-44ed-4ba7-98e3-f405b2d2c4b4"), event_id=1001, version=0)
class Microsoft_Windows_DateTimeControlPanel_1001_0(Etw):
    pattern = Struct(
        "TimeZoneKey" / WString,
        "TimeZoneDisplay" / WString,
        "TimeZoneMUIDisplay" / WString
    )


@declare(guid=guid("741fc222-44ed-4ba7-98e3-f405b2d2c4b4"), event_id=1002, version=0)
class Microsoft_Windows_DateTimeControlPanel_1002_0(Etw):
    pattern = Struct(
        "TimeZoneKey" / WString,
        "SubKey" / WString
    )


@declare(guid=guid("741fc222-44ed-4ba7-98e3-f405b2d2c4b4"), event_id=1003, version=0)
class Microsoft_Windows_DateTimeControlPanel_1003_0(Etw):
    pattern = Struct(
        "wYear" / Int16ul,
        "wMonth" / Int16ul,
        "wDayOfWeek" / Int16ul,
        "wDay" / Int16ul,
        "wHour" / Int16ul,
        "wMinute" / Int16ul,
        "wSecond" / Int16ul,
        "wMilliseconds" / Int16ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("741fc222-44ed-4ba7-98e3-f405b2d2c4b4"), event_id=1004, version=0)
class Microsoft_Windows_DateTimeControlPanel_1004_0(Etw):
    pattern = Struct(
        "Bias" / Int32sl,
        "StandardName" / WString,
        "SystemDatewYear" / Int16ul,
        "SystemDatewMonth" / Int16ul,
        "SystemDatewDayOfWeek" / Int16ul,
        "SystemDatewDay" / Int16ul,
        "SystemDatewHour" / Int16ul,
        "SystemDatewMinute" / Int16ul,
        "SystemDatewSecond" / Int16ul,
        "SystemDatewMilliseconds" / Int16ul,
        "StandardBias" / Int32sl,
        "DaylightName" / WString,
        "DaylightDatewYear" / Int16ul,
        "DaylightDatewMonth" / Int16ul,
        "DaylightDatewDayOfWeek" / Int16ul,
        "DaylightDatewDay" / Int16ul,
        "DaylightDatewHour" / Int16ul,
        "DaylightDatewMinute" / Int16ul,
        "DaylightDatewSecond" / Int16ul,
        "DaylightDatewMilliseconds" / Int16ul,
        "DaylightBias" / Int32sl,
        "TimeZoneKeyName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("741fc222-44ed-4ba7-98e3-f405b2d2c4b4"), event_id=1004, version=1)
class Microsoft_Windows_DateTimeControlPanel_1004_1(Etw):
    pattern = Struct(
        "TimeZone" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("741fc222-44ed-4ba7-98e3-f405b2d2c4b4"), event_id=1005, version=0)
class Microsoft_Windows_DateTimeControlPanel_1005_0(Etw):
    pattern = Struct(
        "TimeZone" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("741fc222-44ed-4ba7-98e3-f405b2d2c4b4"), event_id=1006, version=0)
class Microsoft_Windows_DateTimeControlPanel_1006_0(Etw):
    pattern = Struct(
        "TimeZone" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("741fc222-44ed-4ba7-98e3-f405b2d2c4b4"), event_id=1007, version=0)
class Microsoft_Windows_DateTimeControlPanel_1007_0(Etw):
    pattern = Struct(
        "TimeZone" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("741fc222-44ed-4ba7-98e3-f405b2d2c4b4"), event_id=20000, version=0)
class Microsoft_Windows_DateTimeControlPanel_20000_0(Etw):
    pattern = Struct(
        "wYear" / Int16ul,
        "wMonth" / Int16ul,
        "wDayOfWeek" / Int16ul,
        "wDay" / Int16ul,
        "wHour" / Int16ul,
        "wMinute" / Int16ul,
        "wSecond" / Int16ul,
        "wMilliseconds" / Int16ul
    )


@declare(guid=guid("741fc222-44ed-4ba7-98e3-f405b2d2c4b4"), event_id=20001, version=0)
class Microsoft_Windows_DateTimeControlPanel_20001_0(Etw):
    pattern = Struct(
        "TimeZone" / WString
    )


@declare(guid=guid("741fc222-44ed-4ba7-98e3-f405b2d2c4b4"), event_id=30001, version=0)
class Microsoft_Windows_DateTimeControlPanel_30001_0(Etw):
    pattern = Struct(
        "wYear" / Int16ul,
        "wMonth" / Int16ul,
        "wDayOfWeek" / Int16ul,
        "wDay" / Int16ul,
        "wHour" / Int16ul,
        "wMinute" / Int16ul,
        "wSecond" / Int16ul,
        "wMilliseconds" / Int16ul
    )


@declare(guid=guid("741fc222-44ed-4ba7-98e3-f405b2d2c4b4"), event_id=30002, version=0)
class Microsoft_Windows_DateTimeControlPanel_30002_0(Etw):
    pattern = Struct(
        "Bias" / Int32sl,
        "StandardName" / WString,
        "SystemDatewYear" / Int16ul,
        "SystemDatewMonth" / Int16ul,
        "SystemDatewDayOfWeek" / Int16ul,
        "SystemDatewDay" / Int16ul,
        "SystemDatewHour" / Int16ul,
        "SystemDatewMinute" / Int16ul,
        "SystemDatewSecond" / Int16ul,
        "SystemDatewMilliseconds" / Int16ul,
        "StandardBias" / Int32sl,
        "DaylightName" / WString,
        "DaylightDatewYear" / Int16ul,
        "DaylightDatewMonth" / Int16ul,
        "DaylightDatewDayOfWeek" / Int16ul,
        "DaylightDatewDay" / Int16ul,
        "DaylightDatewHour" / Int16ul,
        "DaylightDatewMinute" / Int16ul,
        "DaylightDatewSecond" / Int16ul,
        "DaylightDatewMilliseconds" / Int16ul,
        "DaylightBias" / Int32sl,
        "TimeZoneKeyName" / WString
    )

