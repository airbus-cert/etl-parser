# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TerminalServices-LocalSessionManager
GUID : 5d896912-022d-40aa-a3a8-4fa5515c76d7
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=2, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_2_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=3, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_3_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=4, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_4_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=5, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_5_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=6, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_6_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=7, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_7_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=8, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_8_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=9, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_9_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=16, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_16_0(Etw):
    pattern = Struct(
        "Param1" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=17, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_17_0(Etw):
    pattern = Struct(
        "Param1" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=19, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_19_0(Etw):
    pattern = Struct(
        "Param1" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=20, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_20_0(Etw):
    pattern = Struct(
        "messageName" / WString,
        "errorCode" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=21, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_21_0(Etw):
    pattern = Struct(
        "User" / WString,
        "SessionID" / Int32ul,
        "Address" / WString
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=22, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_22_0(Etw):
    pattern = Struct(
        "User" / WString,
        "SessionID" / Int32ul,
        "Address" / WString
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=23, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_23_0(Etw):
    pattern = Struct(
        "User" / WString,
        "SessionID" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=24, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_24_0(Etw):
    pattern = Struct(
        "User" / WString,
        "SessionID" / Int32ul,
        "Address" / WString
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=25, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_25_0(Etw):
    pattern = Struct(
        "User" / WString,
        "SessionID" / Int32ul,
        "Address" / WString
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=32, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_32_0(Etw):
    pattern = Struct(
        "messageName" / WString
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=33, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_33_0(Etw):
    pattern = Struct(
        "messageName" / WString,
        "errorCode" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=35, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_35_0(Etw):
    pattern = Struct(
        "Param1" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=36, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_36_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "State" / Int32ul,
        "StateName" / WString,
        "Event" / Int32ul,
        "EventName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=37, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_37_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "State" / Int32ul,
        "StateName" / WString,
        "Event" / Int32ul,
        "EventName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=38, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_38_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "PreviousState" / Int32ul,
        "PreviousStateName" / WString,
        "NewState" / Int32ul,
        "NewStateName" / WString,
        "Event" / Int32ul,
        "EventName" / WString
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=39, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_39_0(Etw):
    pattern = Struct(
        "TargetSession" / Int32ul,
        "Source" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=40, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_40_0(Etw):
    pattern = Struct(
        "Session" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=41, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_41_0(Etw):
    pattern = Struct(
        "User" / WString,
        "SessionID" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=42, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_42_0(Etw):
    pattern = Struct(
        "User" / WString,
        "SessionID" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=43, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_43_0(Etw):
    pattern = Struct(
        "Session" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=44, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_44_0(Etw):
    pattern = Struct(
        "Session" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=45, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_45_0(Etw):
    pattern = Struct(
        "Session" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=48, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_48_0(Etw):
    pattern = Struct(
        "Session" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=49, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_49_0(Etw):
    pattern = Struct(
        "Session" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=50, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_50_0(Etw):
    pattern = Struct(
        "Session" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=51, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_51_0(Etw):
    pattern = Struct(
        "Session" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=52, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_52_0(Etw):
    pattern = Struct(
        "Session" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=53, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_53_0(Etw):
    pattern = Struct(
        "Session" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=57, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_57_0(Etw):
    pattern = Struct(
        "SessionID" / Int32ul,
        "InitCmdPid" / Int32ul,
        "Win32kPid" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=58, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_58_0(Etw):
    pattern = Struct(
        "SessionID" / Int32ul,
        "InitCmdPid" / Int32ul,
        "Win32kPid" / Int32ul,
        "InitCmdName" / WString
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=59, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_59_0(Etw):
    pattern = Struct(
        "Function" / WString,
        "CallerImageName" / WString,
        "SessionId" / Int32ul,
        "ClientProcessId" / Int32ul
    )


@declare(guid=guid("5d896912-022d-40aa-a3a8-4fa5515c76d7"), event_id=60, version=0)
class Microsoft_Windows_TerminalServices_LocalSessionManager_60_0(Etw):
    pattern = Struct(
        "SessionID" / Int32ul
    )

