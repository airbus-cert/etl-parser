# -*- coding: utf-8 -*-
"""
Microsoft-Windows-PushNotifications-Developer
GUID : 5cad3597-5fec-4c62-9ce1-9d7abc723d3a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5cad3597-5fec-4c62-9ce1-9d7abc723d3a"), event_id=1, version=0)
class Microsoft_Windows_PushNotifications_Developer_1_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "FunctionName" / WString,
        "LineNumber" / Int32sl,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("5cad3597-5fec-4c62-9ce1-9d7abc723d3a"), event_id=1000, version=0)
class Microsoft_Windows_PushNotifications_Developer_1000_0(Etw):
    pattern = Struct(
        "AppID" / WString
    )


@declare(guid=guid("5cad3597-5fec-4c62-9ce1-9d7abc723d3a"), event_id=1001, version=0)
class Microsoft_Windows_PushNotifications_Developer_1001_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "Channel" / WString
    )


@declare(guid=guid("5cad3597-5fec-4c62-9ce1-9d7abc723d3a"), event_id=1002, version=0)
class Microsoft_Windows_PushNotifications_Developer_1002_0(Etw):
    pattern = Struct(
        "Channel" / WString
    )


@declare(guid=guid("5cad3597-5fec-4c62-9ce1-9d7abc723d3a"), event_id=1100, version=0)
class Microsoft_Windows_PushNotifications_Developer_1100_0(Etw):
    pattern = Struct(
        "NotificationType" / Int32ul
    )


@declare(guid=guid("5cad3597-5fec-4c62-9ce1-9d7abc723d3a"), event_id=1101, version=0)
class Microsoft_Windows_PushNotifications_Developer_1101_0(Etw):
    pattern = Struct(
        "NotificationType" / Int32ul
    )


@declare(guid=guid("5cad3597-5fec-4c62-9ce1-9d7abc723d3a"), event_id=1102, version=0)
class Microsoft_Windows_PushNotifications_Developer_1102_0(Etw):
    pattern = Struct(
        "NotificationType" / Int32ul
    )


@declare(guid=guid("5cad3597-5fec-4c62-9ce1-9d7abc723d3a"), event_id=1103, version=0)
class Microsoft_Windows_PushNotifications_Developer_1103_0(Etw):
    pattern = Struct(
        "NotificationType" / Int32ul
    )


@declare(guid=guid("5cad3597-5fec-4c62-9ce1-9d7abc723d3a"), event_id=1104, version=0)
class Microsoft_Windows_PushNotifications_Developer_1104_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "NotificationType" / Int32ul
    )


@declare(guid=guid("5cad3597-5fec-4c62-9ce1-9d7abc723d3a"), event_id=1105, version=0)
class Microsoft_Windows_PushNotifications_Developer_1105_0(Etw):
    pattern = Struct(
        "AppID" / WString
    )


@declare(guid=guid("5cad3597-5fec-4c62-9ce1-9d7abc723d3a"), event_id=1106, version=0)
class Microsoft_Windows_PushNotifications_Developer_1106_0(Etw):
    pattern = Struct(
        "AppID" / WString
    )


@declare(guid=guid("5cad3597-5fec-4c62-9ce1-9d7abc723d3a"), event_id=1107, version=0)
class Microsoft_Windows_PushNotifications_Developer_1107_0(Etw):
    pattern = Struct(
        "AppID" / WString
    )


@declare(guid=guid("5cad3597-5fec-4c62-9ce1-9d7abc723d3a"), event_id=1118, version=0)
class Microsoft_Windows_PushNotifications_Developer_1118_0(Etw):
    pattern = Struct(
        "AppID" / WString
    )


@declare(guid=guid("5cad3597-5fec-4c62-9ce1-9d7abc723d3a"), event_id=1119, version=0)
class Microsoft_Windows_PushNotifications_Developer_1119_0(Etw):
    pattern = Struct(
        "AppID" / WString
    )


@declare(guid=guid("5cad3597-5fec-4c62-9ce1-9d7abc723d3a"), event_id=1120, version=0)
class Microsoft_Windows_PushNotifications_Developer_1120_0(Etw):
    pattern = Struct(
        "AppID" / WString
    )


@declare(guid=guid("5cad3597-5fec-4c62-9ce1-9d7abc723d3a"), event_id=1121, version=0)
class Microsoft_Windows_PushNotifications_Developer_1121_0(Etw):
    pattern = Struct(
        "AppID" / WString
    )


@declare(guid=guid("5cad3597-5fec-4c62-9ce1-9d7abc723d3a"), event_id=1122, version=0)
class Microsoft_Windows_PushNotifications_Developer_1122_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "IsConnected" / Int8ul
    )


@declare(guid=guid("5cad3597-5fec-4c62-9ce1-9d7abc723d3a"), event_id=1123, version=0)
class Microsoft_Windows_PushNotifications_Developer_1123_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "IsConnected" / Int8ul
    )


@declare(guid=guid("5cad3597-5fec-4c62-9ce1-9d7abc723d3a"), event_id=1124, version=0)
class Microsoft_Windows_PushNotifications_Developer_1124_0(Etw):
    pattern = Struct(
        "AppID" / WString
    )

