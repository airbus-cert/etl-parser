# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TerminalServices-ClientActiveXCore
GUID : 28aa95bb-d444-4719-a36f-40462168127e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=225, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_225_0(Etw):
    pattern = Struct(
        "StateTransitionName" / WString,
        "PreviousState" / Int32ul,
        "PreviousStateName" / WString,
        "NewState" / Int32ul,
        "NewStateName" / WString,
        "Event" / Int32ul,
        "EventName" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=226, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_226_0(Etw):
    pattern = Struct(
        "StateTransitionName" / WString,
        "PreviousState" / Int32ul,
        "PreviousStateName" / WString,
        "NewState" / Int32ul,
        "NewStateName" / WString,
        "Event" / Int32ul,
        "EventName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=227, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_227_0(Etw):
    pattern = Struct(
        "StateTransitionName" / WString,
        "ChannelID" / Int32ul,
        "ChannelName" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1000, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1000_0(Etw):
    pattern = Struct(
        "Function" / WString,
        "Line" / WString,
        "DebugMessage" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1001, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1001_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString,
        "CustomLevel" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1003, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1003_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / Int32ul,
        "CustomLevel" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1004, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1004_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / Int32ul,
        "CustomLevel" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1005, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1005_0(Etw):
    pattern = Struct(
        "TraceMessage" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1006, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1006_0(Etw):
    pattern = Struct(
        "TraceMessage" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1007, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1007_0(Etw):
    pattern = Struct(
        "TraceMessage" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1008, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1008_0(Etw):
    pattern = Struct(
        "TraceMessage" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1009, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1009_0(Etw):
    pattern = Struct(
        "TraceMessage" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1010, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1010_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString,
        "CustomLevel" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1012, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1012_0(Etw):
    pattern = Struct(
        "TraceMessage" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1013, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1013_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / Int32ul,
        "CustomLevel" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1014, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1014_0(Etw):
    pattern = Struct(
        "TraceMessage" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1015, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1015_0(Etw):
    pattern = Struct(
        "TraceMessage" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1016, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1016_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString,
        "CustomLevel" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1017, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1017_0(Etw):
    pattern = Struct(
        "TraceMessage" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1018, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1018_0(Etw):
    pattern = Struct(
        "TraceMessage" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1019, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1019_0(Etw):
    pattern = Struct(
        "TraceMessage" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1020, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1020_0(Etw):
    pattern = Struct(
        "TraceMessage" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1021, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1021_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / Int32ul,
        "CustomLevel" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1022, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1022_0(Etw):
    pattern = Struct(
        "TraceMessage" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1023, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1023_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString,
        "CustomLevel" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1024, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1024_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString,
        "CustomLevel" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1026, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1026_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / Int32ul,
        "CustomLevel" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1027, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1027_0(Etw):
    pattern = Struct(
        "DomainName" / WString,
        "SessionId" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1028, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1028_0(Etw):
    pattern = Struct(
        "TraceMessage" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1029, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1029_0(Etw):
    pattern = Struct(
        "TraceMessage" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1030, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1030_0(Etw):
    pattern = Struct(
        "BuildBranch" / WString,
        "BuildDate" / WString,
        "BuildTime" / WString,
        "BuildVersion" / WString,
        "ArchAndFlavour" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1031, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1031_0(Etw):
    pattern = Struct(
        "TraceMessage" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1032, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1032_0(Etw):
    pattern = Struct(
        "ErrorCode" / WString,
        "ErrorDescription" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1033, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1033_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "CustomLevel" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1034, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1034_0(Etw):
    pattern = Struct(
        "ErrorCode" / WString,
        "ErrorDescription" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1100, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1100_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString,
        "CustomLevel" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1101, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1101_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString,
        "CustomLevel" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1102, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1102_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString,
        "CustomLevel" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1104, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1104_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / Int32ul,
        "CustomLevel" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1106, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1106_0(Etw):
    pattern = Struct(
        "Code" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1107, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1107_0(Etw):
    pattern = Struct(
        "ComponentName" / WString,
        "Message" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1205, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1205_0(Etw):
    pattern = Struct(
        "Event" / WString,
        "TenantId" / WString,
        "TotalTimeWithoutAdal" / Int32ul,
        "AdalTime" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1206, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1206_0(Etw):
    pattern = Struct(
        "Event" / WString,
        "TenantId" / WString,
        "TotalTimeWithoutAdal" / Int32ul,
        "AdalTime" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1207, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1207_0(Etw):
    pattern = Struct(
        "BuildBranch" / WString,
        "BuildDate" / WString,
        "BuildTime" / WString,
        "BuildVersion" / WString,
        "ArchAndFlavour" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1208, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1208_0(Etw):
    pattern = Struct(
        "TotalTimeWithoutAdal" / Int32ul,
        "AdalTime" / Int32ul,
        "NumberOfFeeds" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1209, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1209_0(Etw):
    pattern = Struct(
        "TotalTimeWithoutAdal" / Int32ul,
        "AdalTime" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1210, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1210_0(Etw):
    pattern = Struct(
        "TenantId" / WString,
        "ResourceIndex" / Int32ul,
        "ResourceType" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1211, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1211_0(Etw):
    pattern = Struct(
        "TotalTimeWithoutAdal" / Int32ul,
        "AdalTime" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1212, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1212_0(Etw):
    pattern = Struct(
        "TotalTimeWithoutAdal" / Int32ul,
        "AdalTime" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1214, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1214_0(Etw):
    pattern = Struct(
        "UserNameHash" / WString,
        "TimeZoneBias" / Int32sl,
        "TimeZoneName" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1215, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1215_0(Etw):
    pattern = Struct(
        "refreshTime" / Int32ul,
        "numberOfFeeds" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1216, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1216_0(Etw):
    pattern = Struct(
        "ErrorCode" / WString,
        "ErrorDescription" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1227, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1227_0(Etw):
    pattern = Struct(
        "RadcClientType" / WString,
        "RadcClientStage" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1228, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1228_0(Etw):
    pattern = Struct(
        "RadcClientStage" / WString,
        "RadcHttpEvent" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1229, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1229_0(Etw):
    pattern = Struct(
        "RadcClientStage" / WString,
        "RadcHttpEvent" / WString,
        "Code" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1230, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1230_0(Etw):
    pattern = Struct(
        "RadcClientStage" / WString,
        "RadcHttpEvent" / WString,
        "Code" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1401, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1401_0(Etw):
    pattern = Struct(
        "Version" / Int32ul,
        "ClientMode" / Int32ul,
        "AvcEnabled" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1404, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1404_0(Etw):
    pattern = Struct(
        "Component" / WString,
        "Function" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1501, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1501_0(Etw):
    pattern = Struct(
        "TraceMessage" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1502, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1502_0(Etw):
    pattern = Struct(
        "TraceMessage" / WString
    )


@declare(guid=guid("28aa95bb-d444-4719-a36f-40462168127e"), event_id=1503, version=0)
class Microsoft_Windows_TerminalServices_ClientActiveXCore_1503_0(Etw):
    pattern = Struct(
        "TraceMessage" / WString
    )

