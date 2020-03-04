# -*- coding: utf-8 -*-
"""
Microsoft-Windows-RemoteApp and Desktop Connections
GUID : 1b8b402d-78dc-46fb-bf71-46e64aedf165
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1000, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1000_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FeedURL" / WString,
        "ErrorCode" / Int32ul,
        "ErrorCodeAdditional" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1001, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1001_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FeedURL" / WString,
        "ErrorCode" / Int32ul,
        "ErrorCodeAdditional" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1002, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1002_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FeedURL" / WString,
        "ErrorCode" / Int32ul,
        "ErrorCodeAdditional" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1003, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1003_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FeedURL" / WString,
        "ErrorCode" / Int32ul,
        "ErrorCodeAdditional" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1004, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1004_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FeedURL" / WString,
        "ErrorCode" / Int32ul,
        "ErrorCodeAdditional" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1005, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1005_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FeedURL" / WString,
        "ErrorCode" / Int32ul,
        "ErrorCodeAdditional" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1006, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1006_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FeedURL" / WString,
        "ErrorCode" / Int32ul,
        "ErrorCodeAdditional" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1007, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1007_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FeedURL" / WString,
        "ErrorCode" / Int32ul,
        "ErrorCodeAdditional" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1008, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1008_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FeedURL" / WString,
        "ErrorCode" / Int32ul,
        "ErrorCodeAdditional" / Int32ul,
        "NumResourcesAvailable" / Int32ul,
        "NumResourcesDownloaded" / Int32ul,
        "NumResourcesNotDownloaded" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1009, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1009_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FeedURL" / WString,
        "ErrorCode" / Int32ul,
        "ErrorCodeAdditional" / Int32ul,
        "NumResourcesAvailable" / Int32ul,
        "NumResourcesDownloaded" / Int32ul,
        "NumResourcesNotDownloaded" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1010, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1010_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FeedURL" / WString,
        "ErrorCode" / Int32ul,
        "ErrorCodeAdditional" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1011, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1011_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FeedURL" / WString,
        "ErrorCode" / Int32ul,
        "ErrorCodeAdditional" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1012, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1012_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FeedURL" / WString,
        "ErrorCode" / Int32ul,
        "ErrorCodeAdditional" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1013, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1013_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FeedURL" / WString,
        "ErrorCode" / Int32ul,
        "ErrorCodeAdditional" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1014, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1014_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FeedURL" / WString,
        "ErrorCode" / Int32ul,
        "ErrorCodeAdditional" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1015, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1015_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FeedURL" / WString,
        "ErrorCode" / Int32ul,
        "ErrorCodeAdditional" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1016, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1016_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FeedURL" / WString,
        "ErrorCode" / Int32ul,
        "ErrorCodeAdditional" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1017, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1017_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FeedURL" / WString,
        "ErrorCode" / Int32ul,
        "ErrorCodeAdditional" / Int32ul,
        "ResourceURL" / WString
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1018, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1018_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FeedURL" / WString,
        "ErrorCode" / Int32ul,
        "ErrorCodeAdditional" / Int32ul,
        "ResourceURL" / WString
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1019, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1019_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FeedURL" / WString
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1020, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1020_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FeedURL" / WString
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1021, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1021_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "String2" / WString
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1022, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1022_0(Etw):
    pattern = Struct(
        "Hint" / WString,
        "FeedURL" / WString
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1023, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1023_0(Etw):
    pattern = Struct(
        "Hint" / WString,
        "FeedURL" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1024, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1024_0(Etw):
    pattern = Struct(
        "Hint" / WString,
        "FeedURL" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1025, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1025_0(Etw):
    pattern = Struct(
        "ResourceName" / WString,
        "ConnectionName" / WString,
        "ConnectionURL" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1026, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1026_0(Etw):
    pattern = Struct(
        "User" / WString
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1027, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1027_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "ConnectionName" / WString
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1028, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1028_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "ConnectionName" / WString
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1029, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1029_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "ConnectionName" / WString
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1030, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1030_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "ConnectionName" / WString
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1031, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1031_0(Etw):
    pattern = Struct(
        "ConnectionName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1032, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1032_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "ConnectionName" / WString
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1033, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1033_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "ConnectionName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1034, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1034_0(Etw):
    pattern = Struct(
        "ConnectionId" / Int32ul,
        "ConnectionName" / WString
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1035, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1035_0(Etw):
    pattern = Struct(
        "ConnectionName" / WString
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1036, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1036_0(Etw):
    pattern = Struct(
        "ConnectionName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1037, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1037_0(Etw):
    pattern = Struct(
        "ConnectionId" / Int32ul,
        "ConnectionName" / WString
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1038, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1038_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "ConnectionName" / WString
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1039, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1039_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "ConnectionName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1040, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1040_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "ConnectionName" / WString
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1041, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1041_0(Etw):
    pattern = Struct(
        "RemoteAppName" / WString,
        "ConnectionName" / WString,
        "Reason" / WString
    )


@declare(guid=guid("1b8b402d-78dc-46fb-bf71-46e64aedf165"), event_id=1042, version=0)
class Microsoft_Windows_RemoteApp_and_Desktop_Connections_1042_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "ConnectionName" / WString,
        "ErrorCode" / Int32ul
    )

