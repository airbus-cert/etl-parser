# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Program-Compatibility-Assistant
GUID : 4cb314df-c11f-47d7-9c04-65fb0051561b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4cb314df-c11f-47d7-9c04-65fb0051561b"), event_id=1, version=0)
class Microsoft_Windows_Program_Compatibility_Assistant_1_0(Etw):
    pattern = Struct(
        "ApplicationNameSize" / Int32ul,
        "ApplicationName" / WString,
        "CommandLineSize" / Int32ul,
        "CommandLine" / WString,
        "CurrentDirectorySize" / Int32ul,
        "CurrentDirectory" / WString,
        "DllNameSize" / Int32ul,
        "DllName" / WString,
        "InterfaceCLSID" / Guid,
        "SessionId" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("4cb314df-c11f-47d7-9c04-65fb0051561b"), event_id=3, version=0)
class Microsoft_Windows_Program_Compatibility_Assistant_3_0(Etw):
    pattern = Struct(
        "ApplicationNameSize" / Int32ul,
        "ApplicationName" / WString,
        "CommandLineSize" / Int32ul,
        "CommandLine" / WString,
        "CurrentDirectorySize" / Int32ul,
        "CurrentDirectory" / WString,
        "DllNameSize" / Int32ul,
        "DllName" / WString,
        "InterfaceCLSID" / Guid,
        "SessionId" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("4cb314df-c11f-47d7-9c04-65fb0051561b"), event_id=5, version=0)
class Microsoft_Windows_Program_Compatibility_Assistant_5_0(Etw):
    pattern = Struct(
        "ApplicationNameSize" / Int32ul,
        "ApplicationName" / WString,
        "CommandLineSize" / Int32ul,
        "CommandLine" / WString,
        "CurrentDirectorySize" / Int32ul,
        "CurrentDirectory" / WString,
        "DllNameSize" / Int32ul,
        "DllName" / WString,
        "InterfaceCLSID" / Guid,
        "SessionId" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("4cb314df-c11f-47d7-9c04-65fb0051561b"), event_id=8, version=0)
class Microsoft_Windows_Program_Compatibility_Assistant_8_0(Etw):
    pattern = Struct(
        "ApplicationNameSize" / Int32ul,
        "ApplicationName" / WString,
        "CommandLineSize" / Int32ul,
        "CommandLine" / WString,
        "CurrentDirectorySize" / Int32ul,
        "CurrentDirectory" / WString,
        "DllNameSize" / Int32ul,
        "DllName" / WString,
        "InterfaceCLSID" / Guid,
        "SessionId" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("4cb314df-c11f-47d7-9c04-65fb0051561b"), event_id=9, version=0)
class Microsoft_Windows_Program_Compatibility_Assistant_9_0(Etw):
    pattern = Struct(
        "ApplicationNameSize" / Int32ul,
        "ApplicationName" / WString,
        "CommandLineSize" / Int32ul,
        "CommandLine" / WString,
        "CurrentDirectorySize" / Int32ul,
        "CurrentDirectory" / WString,
        "DllNameSize" / Int32ul,
        "DllName" / WString,
        "InterfaceCLSID" / Guid,
        "SessionId" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("4cb314df-c11f-47d7-9c04-65fb0051561b"), event_id=10, version=0)
class Microsoft_Windows_Program_Compatibility_Assistant_10_0(Etw):
    pattern = Struct(
        "ApplicationNameSize" / Int32ul,
        "ApplicationName" / WString,
        "CommandLineSize" / Int32ul,
        "CommandLine" / WString,
        "CurrentDirectorySize" / Int32ul,
        "CurrentDirectory" / WString,
        "DllNameSize" / Int32ul,
        "DllName" / WString,
        "InterfaceCLSID" / Guid,
        "SessionId" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("4cb314df-c11f-47d7-9c04-65fb0051561b"), event_id=11, version=0)
class Microsoft_Windows_Program_Compatibility_Assistant_11_0(Etw):
    pattern = Struct(
        "DisplayNameSize" / Int32ul,
        "DisplayName" / WString,
        "FullImagePathSize" / Int32ul,
        "FullImagePath" / WString,
        "SessionId" / Int32ul
    )


@declare(guid=guid("4cb314df-c11f-47d7-9c04-65fb0051561b"), event_id=12, version=0)
class Microsoft_Windows_Program_Compatibility_Assistant_12_0(Etw):
    pattern = Struct(
        "ApplicationNameSize" / Int32ul,
        "ApplicationName" / WString,
        "CommandLineSize" / Int32ul,
        "CommandLine" / WString,
        "CurrentDirectorySize" / Int32ul,
        "CurrentDirectory" / WString,
        "DllNameSize" / Int32ul,
        "DllName" / WString,
        "InterfaceCLSID" / Guid,
        "SessionId" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("4cb314df-c11f-47d7-9c04-65fb0051561b"), event_id=14, version=0)
class Microsoft_Windows_Program_Compatibility_Assistant_14_0(Etw):
    pattern = Struct(
        "ApplicationNameSize" / Int32ul,
        "ApplicationName" / WString,
        "CommandLineSize" / Int32ul,
        "CommandLine" / WString,
        "CurrentDirectorySize" / Int32ul,
        "CurrentDirectory" / WString,
        "DllNameSize" / Int32ul,
        "DllName" / WString,
        "InterfaceCLSID" / Guid,
        "SessionId" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("4cb314df-c11f-47d7-9c04-65fb0051561b"), event_id=15, version=0)
class Microsoft_Windows_Program_Compatibility_Assistant_15_0(Etw):
    pattern = Struct(
        "TokenDataSize" / Int32ul,
        "TokenData" / Bytes(lambda this: this.TokenDataSize)
    )


@declare(guid=guid("4cb314df-c11f-47d7-9c04-65fb0051561b"), event_id=16, version=0)
class Microsoft_Windows_Program_Compatibility_Assistant_16_0(Etw):
    pattern = Struct(
        "ExePath" / WString,
        "ResolverMap" / Int64ul,
        "DialogType" / Int32ul
    )


@declare(guid=guid("4cb314df-c11f-47d7-9c04-65fb0051561b"), event_id=17, version=0)
class Microsoft_Windows_Program_Compatibility_Assistant_17_0(Etw):
    pattern = Struct(
        "ExePath" / WString,
        "ResolverName" / WString
    )


@declare(guid=guid("4cb314df-c11f-47d7-9c04-65fb0051561b"), event_id=30, version=0)
class Microsoft_Windows_Program_Compatibility_Assistant_30_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "ApplicationVersion" / WString,
        "ExecutablePath" / WString,
        "ScenarioId" / WString,
        "UserAction" / WString,
        "CompatibilityLayer" / WString
    )


@declare(guid=guid("4cb314df-c11f-47d7-9c04-65fb0051561b"), event_id=31, version=0)
class Microsoft_Windows_Program_Compatibility_Assistant_31_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "ApplicationVersion" / WString,
        "ExecutablePath" / WString,
        "ScenarioId" / WString,
        "UserAction" / WString,
        "CompatibilityLayer" / WString,
        "DeprecatedComponent" / WString
    )


@declare(guid=guid("4cb314df-c11f-47d7-9c04-65fb0051561b"), event_id=32, version=0)
class Microsoft_Windows_Program_Compatibility_Assistant_32_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "ServiceName" / WString,
        "PublisherName" / WString,
        "DriverPath" / WString,
        "DriverVersion" / WString
    )


@declare(guid=guid("4cb314df-c11f-47d7-9c04-65fb0051561b"), event_id=1200, version=0)
class Microsoft_Windows_Program_Compatibility_Assistant_1200_0(Etw):
    pattern = Struct(
        "TriggerID" / Int32ul,
        "ExtraDataSize" / Int32ul,
        "ExtraData" / Bytes(lambda this: this.ExtraDataSize)
    )


@declare(guid=guid("4cb314df-c11f-47d7-9c04-65fb0051561b"), event_id=1234, version=0)
class Microsoft_Windows_Program_Compatibility_Assistant_1234_0(Etw):
    pattern = Struct(
        "ApplicationID" / WString,
        "Uptime" / Int32ul
    )

