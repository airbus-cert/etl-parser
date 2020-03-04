# -*- coding: utf-8 -*-
"""
Microsoft-Windows-User Profiles Service
GUID : 89b1e9f0-5aff-44a6-9b44-0a07a7ce5845
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1, version=0)
class Microsoft_Windows_User_Profiles_Service_1_0(Etw):
    pattern = Struct(
        "Session" / Int32ul
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=2, version=0)
class Microsoft_Windows_User_Profiles_Service_2_0(Etw):
    pattern = Struct(
        "Session" / Int32ul
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=3, version=0)
class Microsoft_Windows_User_Profiles_Service_3_0(Etw):
    pattern = Struct(
        "Session" / Int32ul
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=4, version=0)
class Microsoft_Windows_User_Profiles_Service_4_0(Etw):
    pattern = Struct(
        "Session" / Int32ul
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=5, version=0)
class Microsoft_Windows_User_Profiles_Service_5_0(Etw):
    pattern = Struct(
        "File" / WString,
        "Key" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=6, version=0)
class Microsoft_Windows_User_Profiles_Service_6_0(Etw):
    pattern = Struct(
        "Source" / WString,
        "Target" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=7, version=0)
class Microsoft_Windows_User_Profiles_Service_7_0(Etw):
    pattern = Struct(
        "Source" / WString,
        "Target" / WString,
        "Result" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=50, version=0)
class Microsoft_Windows_User_Profiles_Service_50_0(Etw):
    pattern = Struct(
        "UserSid" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=51, version=0)
class Microsoft_Windows_User_Profiles_Service_51_0(Etw):
    pattern = Struct(
        "UserSid" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=52, version=0)
class Microsoft_Windows_User_Profiles_Service_52_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=53, version=0)
class Microsoft_Windows_User_Profiles_Service_53_0(Etw):
    pattern = Struct(
        "File" / WString,
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=54, version=0)
class Microsoft_Windows_User_Profiles_Service_54_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=55, version=0)
class Microsoft_Windows_User_Profiles_Service_55_0(Etw):
    pattern = Struct(
        "File" / WString,
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=56, version=0)
class Microsoft_Windows_User_Profiles_Service_56_0(Etw):
    pattern = Struct(
        "File" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=58, version=0)
class Microsoft_Windows_User_Profiles_Service_58_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=60, version=0)
class Microsoft_Windows_User_Profiles_Service_60_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=62, version=0)
class Microsoft_Windows_User_Profiles_Service_62_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=63, version=0)
class Microsoft_Windows_User_Profiles_Service_63_0(Etw):
    pattern = Struct(
        "Result" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=64, version=0)
class Microsoft_Windows_User_Profiles_Service_64_0(Etw):
    pattern = Struct(
        "EnvIssue" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=65, version=0)
class Microsoft_Windows_User_Profiles_Service_65_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=66, version=0)
class Microsoft_Windows_User_Profiles_Service_66_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=67, version=0)
class Microsoft_Windows_User_Profiles_Service_67_0(Etw):
    pattern = Struct(
        "LogonType" / WString,
        "LocalPath" / WString,
        "ProfileType" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=68, version=0)
class Microsoft_Windows_User_Profiles_Service_68_0(Etw):
    pattern = Struct(
        "DownloadTime" / WString,
        "UploadTime" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=70, version=0)
class Microsoft_Windows_User_Profiles_Service_70_0(Etw):
    pattern = Struct(
        "Timeout" / Int32ul
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=71, version=0)
class Microsoft_Windows_User_Profiles_Service_71_0(Etw):
    pattern = Struct(
        "Timeout" / Int32ul
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=72, version=0)
class Microsoft_Windows_User_Profiles_Service_72_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1003, version=0)
class Microsoft_Windows_User_Profiles_Service_1003_0(Etw):
    pattern = Struct(
        "MeasuredLatency" / Int32ul,
        "LatencyThreshold" / Int32ul
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1004, version=0)
class Microsoft_Windows_User_Profiles_Service_1004_0(Etw):
    pattern = Struct(
        "MeasuredBandwidth" / Int32ul,
        "BandwidthThreshold" / Int32ul
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1005, version=0)
class Microsoft_Windows_User_Profiles_Service_1005_0(Etw):
    pattern = Struct(
        "ProfilePath" / WString,
        "AgeLimitInDays" / Int32ul
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1500, version=0)
class Microsoft_Windows_User_Profiles_Service_1500_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1501, version=0)
class Microsoft_Windows_User_Profiles_Service_1501_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1502, version=0)
class Microsoft_Windows_User_Profiles_Service_1502_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1503, version=0)
class Microsoft_Windows_User_Profiles_Service_1503_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1505, version=0)
class Microsoft_Windows_User_Profiles_Service_1505_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1506, version=0)
class Microsoft_Windows_User_Profiles_Service_1506_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1508, version=0)
class Microsoft_Windows_User_Profiles_Service_1508_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "File" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1509, version=0)
class Microsoft_Windows_User_Profiles_Service_1509_0(Etw):
    pattern = Struct(
        "File" / WString,
        "Status" / Int32ul,
        "MachineKeys" / WString,
        "UserKeys" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1512, version=0)
class Microsoft_Windows_User_Profiles_Service_1512_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1514, version=0)
class Microsoft_Windows_User_Profiles_Service_1514_0(Etw):
    pattern = Struct(
        "File" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1517, version=0)
class Microsoft_Windows_User_Profiles_Service_1517_0(Etw):
    pattern = Struct(
        "UserSid" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1519, version=0)
class Microsoft_Windows_User_Profiles_Service_1519_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1520, version=0)
class Microsoft_Windows_User_Profiles_Service_1520_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1521, version=0)
class Microsoft_Windows_User_Profiles_Service_1521_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1522, version=0)
class Microsoft_Windows_User_Profiles_Service_1522_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1523, version=0)
class Microsoft_Windows_User_Profiles_Service_1523_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1530, version=0)
class Microsoft_Windows_User_Profiles_Service_1530_0(Etw):
    pattern = Struct(
        "Detail" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1533, version=0)
class Microsoft_Windows_User_Profiles_Service_1533_0(Etw):
    pattern = Struct(
        "Folder" / WString,
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1534, version=0)
class Microsoft_Windows_User_Profiles_Service_1534_0(Etw):
    pattern = Struct(
        "Event" / WString,
        "Component" / WString,
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1535, version=0)
class Microsoft_Windows_User_Profiles_Service_1535_0(Etw):
    pattern = Struct(
        "Folder" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1536, version=0)
class Microsoft_Windows_User_Profiles_Service_1536_0(Etw):
    pattern = Struct(
        "Folder" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1537, version=0)
class Microsoft_Windows_User_Profiles_Service_1537_0(Etw):
    pattern = Struct(
        "Folder" / WString,
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1538, version=0)
class Microsoft_Windows_User_Profiles_Service_1538_0(Etw):
    pattern = Struct(
        "Folder" / WString,
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1539, version=0)
class Microsoft_Windows_User_Profiles_Service_1539_0(Etw):
    pattern = Struct(
        "Folder" / WString,
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1541, version=0)
class Microsoft_Windows_User_Profiles_Service_1541_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1542, version=0)
class Microsoft_Windows_User_Profiles_Service_1542_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1543, version=0)
class Microsoft_Windows_User_Profiles_Service_1543_0(Etw):
    pattern = Struct(
        "Folder" / WString
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1545, version=0)
class Microsoft_Windows_User_Profiles_Service_1545_0(Etw):
    pattern = Struct(
        "InterferingImageName" / WString,
        "InterferingPID" / Int32ul,
        "ProfsvcPID" / Int32ul
    )


@declare(guid=guid("89b1e9f0-5aff-44a6-9b44-0a07a7ce5845"), event_id=1552, version=0)
class Microsoft_Windows_User_Profiles_Service_1552_0(Etw):
    pattern = Struct(
        "InterferingImageName" / WString,
        "InterferingPID" / Int32ul,
        "ProfsvcPID" / Int32ul
    )

