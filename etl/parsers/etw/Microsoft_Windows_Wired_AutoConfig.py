# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Wired-AutoConfig
GUID : b92cf7fd-dc10-4c6b-a72d-1613bf25e597
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=13021, version=0)
class Microsoft_Windows_Wired_AutoConfig_13021_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=13022, version=0)
class Microsoft_Windows_Wired_AutoConfig_13022_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "InterfaceGuid" / Guid,
        "RequestedFields" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=13031, version=0)
class Microsoft_Windows_Wired_AutoConfig_13031_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=13032, version=0)
class Microsoft_Windows_Wired_AutoConfig_13032_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=13033, version=0)
class Microsoft_Windows_Wired_AutoConfig_13033_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "Reason" / Int32ul,
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=15500, version=0)
class Microsoft_Windows_Wired_AutoConfig_15500_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=15501, version=0)
class Microsoft_Windows_Wired_AutoConfig_15501_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=15502, version=0)
class Microsoft_Windows_Wired_AutoConfig_15502_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "ProfileType" / Int32ul,
        "ProfileContent" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=15503, version=0)
class Microsoft_Windows_Wired_AutoConfig_15503_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "ConnectionID" / Int64ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=15504, version=0)
class Microsoft_Windows_Wired_AutoConfig_15504_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "ConnectionID" / Int64ul,
        "RestartReason" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=15505, version=0)
class Microsoft_Windows_Wired_AutoConfig_15505_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "SwitchMAC" / WString,
        "LocalMAC" / WString,
        "ConnectionID" / Int64ul,
        "Identity" / WString,
        "User" / WString,
        "Domain" / WString,
        "ReasonCode" / Int32ul,
        "ReasonText" / WString,
        "ErrorCode" / Int32ul,
        "ExplicitCredentials" / Int8ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=15506, version=0)
class Microsoft_Windows_Wired_AutoConfig_15506_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "ReasonCode" / WString,
        "BlockingTime" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=15507, version=0)
class Microsoft_Windows_Wired_AutoConfig_15507_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=15508, version=0)
class Microsoft_Windows_Wired_AutoConfig_15508_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "NdisPortControlState" / Int32ul,
        "NdisPortAuthState" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=15509, version=0)
class Microsoft_Windows_Wired_AutoConfig_15509_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "AdapterState" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=15510, version=0)
class Microsoft_Windows_Wired_AutoConfig_15510_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / WString,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=15513, version=0)
class Microsoft_Windows_Wired_AutoConfig_15513_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / WString,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=15514, version=0)
class Microsoft_Windows_Wired_AutoConfig_15514_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "SwitchMAC" / WString,
        "LocalMAC" / WString,
        "ConnectionID" / Int64ul,
        "Identity" / WString,
        "User" / WString,
        "Domain" / WString,
        "ReasonCode" / Int32ul,
        "ReasonText" / WString,
        "ErrorCode" / Int32ul,
        "ExplicitCredentials" / Int8ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20001, version=0)
class Microsoft_Windows_Wired_AutoConfig_20001_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20002, version=0)
class Microsoft_Windows_Wired_AutoConfig_20002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20003, version=0)
class Microsoft_Windows_Wired_AutoConfig_20003_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20004, version=0)
class Microsoft_Windows_Wired_AutoConfig_20004_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20005, version=0)
class Microsoft_Windows_Wired_AutoConfig_20005_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20006, version=0)
class Microsoft_Windows_Wired_AutoConfig_20006_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20007, version=0)
class Microsoft_Windows_Wired_AutoConfig_20007_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20008, version=0)
class Microsoft_Windows_Wired_AutoConfig_20008_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20009, version=0)
class Microsoft_Windows_Wired_AutoConfig_20009_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20010, version=0)
class Microsoft_Windows_Wired_AutoConfig_20010_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20011, version=0)
class Microsoft_Windows_Wired_AutoConfig_20011_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20012, version=0)
class Microsoft_Windows_Wired_AutoConfig_20012_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20013, version=0)
class Microsoft_Windows_Wired_AutoConfig_20013_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20014, version=0)
class Microsoft_Windows_Wired_AutoConfig_20014_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20015, version=0)
class Microsoft_Windows_Wired_AutoConfig_20015_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20016, version=0)
class Microsoft_Windows_Wired_AutoConfig_20016_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20017, version=0)
class Microsoft_Windows_Wired_AutoConfig_20017_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20018, version=0)
class Microsoft_Windows_Wired_AutoConfig_20018_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20019, version=0)
class Microsoft_Windows_Wired_AutoConfig_20019_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ProfileName" / WString,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20020, version=0)
class Microsoft_Windows_Wired_AutoConfig_20020_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ProfileName" / WString,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20021, version=0)
class Microsoft_Windows_Wired_AutoConfig_20021_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ProfileName" / WString,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20022, version=0)
class Microsoft_Windows_Wired_AutoConfig_20022_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ProfileName" / WString,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20024, version=0)
class Microsoft_Windows_Wired_AutoConfig_20024_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ProfileName" / WString,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20025, version=0)
class Microsoft_Windows_Wired_AutoConfig_20025_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "ProfileName" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20026, version=0)
class Microsoft_Windows_Wired_AutoConfig_20026_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ProfileName" / WString,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20028, version=0)
class Microsoft_Windows_Wired_AutoConfig_20028_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ProfileName" / WString,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20029, version=0)
class Microsoft_Windows_Wired_AutoConfig_20029_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ProfileName" / WString,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20030, version=0)
class Microsoft_Windows_Wired_AutoConfig_20030_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "ProfileName" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20031, version=0)
class Microsoft_Windows_Wired_AutoConfig_20031_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "ProfileName" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20032, version=0)
class Microsoft_Windows_Wired_AutoConfig_20032_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ProfileName" / WString,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20033, version=0)
class Microsoft_Windows_Wired_AutoConfig_20033_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ProfileName" / WString,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20034, version=0)
class Microsoft_Windows_Wired_AutoConfig_20034_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ProfileName" / WString,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20035, version=0)
class Microsoft_Windows_Wired_AutoConfig_20035_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "ProfileName" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20036, version=0)
class Microsoft_Windows_Wired_AutoConfig_20036_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20037, version=0)
class Microsoft_Windows_Wired_AutoConfig_20037_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "Profile" / WString,
        "Start" / Int32ul,
        "Stop" / Int32ul,
        "Duration" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=20038, version=0)
class Microsoft_Windows_Wired_AutoConfig_20038_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21001, version=0)
class Microsoft_Windows_Wired_AutoConfig_21001_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceContext" / Int64ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21002, version=0)
class Microsoft_Windows_Wired_AutoConfig_21002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceContext" / Int64ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21003, version=0)
class Microsoft_Windows_Wired_AutoConfig_21003_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceContext" / Int64ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21004, version=0)
class Microsoft_Windows_Wired_AutoConfig_21004_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceContext" / Int64ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21005, version=0)
class Microsoft_Windows_Wired_AutoConfig_21005_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceContext" / Int64ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21006, version=0)
class Microsoft_Windows_Wired_AutoConfig_21006_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "InterfaceContext" / Int64ul,
        "PacketContext" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21007, version=0)
class Microsoft_Windows_Wired_AutoConfig_21007_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "InterfaceContext" / Int64ul,
        "PacketContext" / Int64ul,
        "Type" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21008, version=0)
class Microsoft_Windows_Wired_AutoConfig_21008_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "InterfaceContext" / Int64ul,
        "PacketContext" / Int64ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21009, version=0)
class Microsoft_Windows_Wired_AutoConfig_21009_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "InterfaceContext" / Int64ul,
        "PacketContext" / Int64ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21010, version=0)
class Microsoft_Windows_Wired_AutoConfig_21010_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "InterfaceContext" / Int64ul,
        "PacketContext" / Int64ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21011, version=0)
class Microsoft_Windows_Wired_AutoConfig_21011_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "InterfaceContext" / Int64ul,
        "PacketContext" / Int64ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21012, version=0)
class Microsoft_Windows_Wired_AutoConfig_21012_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21013, version=0)
class Microsoft_Windows_Wired_AutoConfig_21013_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21014, version=0)
class Microsoft_Windows_Wired_AutoConfig_21014_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21015, version=0)
class Microsoft_Windows_Wired_AutoConfig_21015_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21016, version=0)
class Microsoft_Windows_Wired_AutoConfig_21016_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21017, version=0)
class Microsoft_Windows_Wired_AutoConfig_21017_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21018, version=0)
class Microsoft_Windows_Wired_AutoConfig_21018_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21019, version=0)
class Microsoft_Windows_Wired_AutoConfig_21019_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21020, version=0)
class Microsoft_Windows_Wired_AutoConfig_21020_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21021, version=0)
class Microsoft_Windows_Wired_AutoConfig_21021_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21022, version=0)
class Microsoft_Windows_Wired_AutoConfig_21022_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21023, version=0)
class Microsoft_Windows_Wired_AutoConfig_21023_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "EventId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21024, version=0)
class Microsoft_Windows_Wired_AutoConfig_21024_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "EventId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21025, version=0)
class Microsoft_Windows_Wired_AutoConfig_21025_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21026, version=0)
class Microsoft_Windows_Wired_AutoConfig_21026_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21027, version=0)
class Microsoft_Windows_Wired_AutoConfig_21027_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21028, version=0)
class Microsoft_Windows_Wired_AutoConfig_21028_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21029, version=0)
class Microsoft_Windows_Wired_AutoConfig_21029_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21030, version=0)
class Microsoft_Windows_Wired_AutoConfig_21030_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21031, version=0)
class Microsoft_Windows_Wired_AutoConfig_21031_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21032, version=0)
class Microsoft_Windows_Wired_AutoConfig_21032_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21033, version=0)
class Microsoft_Windows_Wired_AutoConfig_21033_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "EventId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21034, version=0)
class Microsoft_Windows_Wired_AutoConfig_21034_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "EventId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21035, version=0)
class Microsoft_Windows_Wired_AutoConfig_21035_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "EventId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21036, version=0)
class Microsoft_Windows_Wired_AutoConfig_21036_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21037, version=0)
class Microsoft_Windows_Wired_AutoConfig_21037_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21038, version=0)
class Microsoft_Windows_Wired_AutoConfig_21038_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21039, version=0)
class Microsoft_Windows_Wired_AutoConfig_21039_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21040, version=0)
class Microsoft_Windows_Wired_AutoConfig_21040_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21041, version=0)
class Microsoft_Windows_Wired_AutoConfig_21041_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21042, version=0)
class Microsoft_Windows_Wired_AutoConfig_21042_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("b92cf7fd-dc10-4c6b-a72d-1613bf25e597"), event_id=21043, version=0)
class Microsoft_Windows_Wired_AutoConfig_21043_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )

