# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SMBWitnessClient
GUID : 32254f6c-aa33-46f0-a5e3-1cbcc74bf683
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=1, version=0)
class Microsoft_Windows_SMBWitnessClient_1_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=2, version=0)
class Microsoft_Windows_SMBWitnessClient_2_0(Etw):
    pattern = Struct(
        "NetName" / WString,
        "ShareName" / WString,
        "WitnessServerIP" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=3, version=0)
class Microsoft_Windows_SMBWitnessClient_3_0(Etw):
    pattern = Struct(
        "WitnessServerIP" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=4, version=0)
class Microsoft_Windows_SMBWitnessClient_4_0(Etw):
    pattern = Struct(
        "WitnessServerIP" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=5, version=0)
class Microsoft_Windows_SMBWitnessClient_5_0(Etw):
    pattern = Struct(
        "WitnessServerIP" / WString,
        "NetName" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=6, version=0)
class Microsoft_Windows_SMBWitnessClient_6_0(Etw):
    pattern = Struct(
        "NetName" / WString,
        "ErrorCode" / Int32ul,
        "Sleep" / Int32ul
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=7, version=0)
class Microsoft_Windows_SMBWitnessClient_7_0(Etw):
    pattern = Struct(
        "WitnessServerIP" / WString,
        "NetName" / WString,
        "FileServerIP" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=8, version=0)
class Microsoft_Windows_SMBWitnessClient_8_0(Etw):
    pattern = Struct(
        "WitnessServerIP" / WString,
        "NetName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=9, version=0)
class Microsoft_Windows_SMBWitnessClient_9_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "WitnessServerIP" / WString,
        "NetName" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=10, version=0)
class Microsoft_Windows_SMBWitnessClient_10_0(Etw):
    pattern = Struct(
        "NotificationType" / Int32ul,
        "NetName" / WString,
        "WitnessServerIP" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=11, version=0)
class Microsoft_Windows_SMBWitnessClient_11_0(Etw):
    pattern = Struct(
        "NetName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=12, version=0)
class Microsoft_Windows_SMBWitnessClient_12_0(Etw):
    pattern = Struct(
        "NetName" / WString,
        "WitnessServerIP" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=13, version=0)
class Microsoft_Windows_SMBWitnessClient_13_0(Etw):
    pattern = Struct(
        "NetName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=14, version=0)
class Microsoft_Windows_SMBWitnessClient_14_0(Etw):
    pattern = Struct(
        "NetName" / WString,
        "ShareName" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=15, version=0)
class Microsoft_Windows_SMBWitnessClient_15_0(Etw):
    pattern = Struct(
        "WitnessServerIP" / WString,
        "NetName" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=16, version=0)
class Microsoft_Windows_SMBWitnessClient_16_0(Etw):
    pattern = Struct(
        "WitnessServerIP" / WString,
        "NetName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=17, version=0)
class Microsoft_Windows_SMBWitnessClient_17_0(Etw):
    pattern = Struct(
        "WitnessServer" / WString,
        "NetName" / WString,
        "IPAddress" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=18, version=0)
class Microsoft_Windows_SMBWitnessClient_18_0(Etw):
    pattern = Struct(
        "WitnessServer" / WString,
        "NetName" / WString,
        "ShareName" / WString,
        "IPAddress" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=19, version=0)
class Microsoft_Windows_SMBWitnessClient_19_0(Etw):
    pattern = Struct(
        "NetName" / WString,
        "WitnessServerIP" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=20, version=0)
class Microsoft_Windows_SMBWitnessClient_20_0(Etw):
    pattern = Struct(
        "NetName" / WString,
        "ShareName" / WString,
        "WitnessServerIP" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=21, version=0)
class Microsoft_Windows_SMBWitnessClient_21_0(Etw):
    pattern = Struct(
        "NetName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=22, version=0)
class Microsoft_Windows_SMBWitnessClient_22_0(Etw):
    pattern = Struct(
        "NetName" / WString,
        "ShareName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=23, version=0)
class Microsoft_Windows_SMBWitnessClient_23_0(Etw):
    pattern = Struct(
        "NetName" / WString,
        "ShareName" / WString,
        "WitnessServer" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=24, version=0)
class Microsoft_Windows_SMBWitnessClient_24_0(Etw):
    pattern = Struct(
        "NetName" / WString,
        "ShareName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=25, version=0)
class Microsoft_Windows_SMBWitnessClient_25_0(Etw):
    pattern = Struct(
        "NetName" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=26, version=0)
class Microsoft_Windows_SMBWitnessClient_26_0(Etw):
    pattern = Struct(
        "NetName" / WString,
        "ShareName" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=27, version=0)
class Microsoft_Windows_SMBWitnessClient_27_0(Etw):
    pattern = Struct(
        "WitnessServerIP" / WString,
        "NetName" / WString,
        "ShareName" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=28, version=0)
class Microsoft_Windows_SMBWitnessClient_28_0(Etw):
    pattern = Struct(
        "NetName" / WString,
        "ShareName" / WString,
        "ErrorCode" / Int32ul,
        "Sleep" / Int32ul
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=29, version=0)
class Microsoft_Windows_SMBWitnessClient_29_0(Etw):
    pattern = Struct(
        "WitnessServerIP" / WString,
        "NetName" / WString,
        "ShareName" / WString,
        "FileServerIP" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=30, version=0)
class Microsoft_Windows_SMBWitnessClient_30_0(Etw):
    pattern = Struct(
        "WitnessServerIP" / WString,
        "NetName" / WString,
        "ShareName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=31, version=0)
class Microsoft_Windows_SMBWitnessClient_31_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "WitnessServerIP" / WString,
        "NetName" / WString,
        "ShareName" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=32, version=0)
class Microsoft_Windows_SMBWitnessClient_32_0(Etw):
    pattern = Struct(
        "NotificationType" / Int32ul,
        "NetName" / WString,
        "ShareName" / WString,
        "WitnessServerIP" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=33, version=0)
class Microsoft_Windows_SMBWitnessClient_33_0(Etw):
    pattern = Struct(
        "NetName" / WString,
        "ShareName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=34, version=0)
class Microsoft_Windows_SMBWitnessClient_34_0(Etw):
    pattern = Struct(
        "NetName" / WString,
        "ShareName" / WString,
        "WitnessServerIP" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=35, version=0)
class Microsoft_Windows_SMBWitnessClient_35_0(Etw):
    pattern = Struct(
        "NetName" / WString,
        "ShareName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=36, version=0)
class Microsoft_Windows_SMBWitnessClient_36_0(Etw):
    pattern = Struct(
        "WitnessServerIP" / WString,
        "NetName" / WString,
        "ShareName" / WString
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=37, version=0)
class Microsoft_Windows_SMBWitnessClient_37_0(Etw):
    pattern = Struct(
        "WitnessServerIP" / WString,
        "NetName" / WString,
        "ShareName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=38, version=0)
class Microsoft_Windows_SMBWitnessClient_38_0(Etw):
    pattern = Struct(
        "NetName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=39, version=0)
class Microsoft_Windows_SMBWitnessClient_39_0(Etw):
    pattern = Struct(
        "NetName" / WString,
        "ShareName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=40, version=0)
class Microsoft_Windows_SMBWitnessClient_40_0(Etw):
    pattern = Struct(
        "NetName" / WString,
        "ShareName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=41, version=0)
class Microsoft_Windows_SMBWitnessClient_41_0(Etw):
    pattern = Struct(
        "WitnessServerIP" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("32254f6c-aa33-46f0-a5e3-1cbcc74bf683"), event_id=42, version=0)
class Microsoft_Windows_SMBWitnessClient_42_0(Etw):
    pattern = Struct(
        "WitnessServerIP" / WString,
        "Error" / Int32ul
    )

