# -*- coding: utf-8 -*-
"""
Microsoft-Windows-IPxlatCfg
GUID : 3e5ac668-af52-4c15-b99b-a3e7a6616ebd
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3e5ac668-af52-4c15-b99b-a3e7a6616ebd"), event_id=1001, version=0)
class Microsoft_Windows_IPxlatCfg_1001_0(Etw):
    pattern = Struct(
        "ErrorString" / CString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3e5ac668-af52-4c15-b99b-a3e7a6616ebd"), event_id=1002, version=0)
class Microsoft_Windows_IPxlatCfg_1002_0(Etw):
    pattern = Struct(
        "ErrorString" / CString,
        "ErrorCode" / Int32ul,
        "InterfaceLuid" / Int64ul
    )


@declare(guid=guid("3e5ac668-af52-4c15-b99b-a3e7a6616ebd"), event_id=1003, version=0)
class Microsoft_Windows_IPxlatCfg_1003_0(Etw):
    pattern = Struct(
        "InfoString" / CString
    )


@declare(guid=guid("3e5ac668-af52-4c15-b99b-a3e7a6616ebd"), event_id=1005, version=0)
class Microsoft_Windows_IPxlatCfg_1005_0(Etw):
    pattern = Struct(
        "IPv4Address" / Int32ul,
        "IPv4Prefix" / Int32ul
    )


@declare(guid=guid("3e5ac668-af52-4c15-b99b-a3e7a6616ebd"), event_id=1006, version=0)
class Microsoft_Windows_IPxlatCfg_1006_0(Etw):
    pattern = Struct(
        "InfoString" / CString,
        "InterfaceLuid" / Int64ul
    )


@declare(guid=guid("3e5ac668-af52-4c15-b99b-a3e7a6616ebd"), event_id=1007, version=0)
class Microsoft_Windows_IPxlatCfg_1007_0(Etw):
    pattern = Struct(
        "InterfaceLuid" / Int64ul,
        "PrefixLength" / Int32ul
    )


@declare(guid=guid("3e5ac668-af52-4c15-b99b-a3e7a6616ebd"), event_id=1008, version=0)
class Microsoft_Windows_IPxlatCfg_1008_0(Etw):
    pattern = Struct(
        "InterfaceLuid" / Int64ul,
        "IPv4Address" / Int32ul
    )


@declare(guid=guid("3e5ac668-af52-4c15-b99b-a3e7a6616ebd"), event_id=1009, version=0)
class Microsoft_Windows_IPxlatCfg_1009_0(Etw):
    pattern = Struct(
        "InterfaceLuid" / Int64ul
    )


@declare(guid=guid("3e5ac668-af52-4c15-b99b-a3e7a6616ebd"), event_id=1010, version=0)
class Microsoft_Windows_IPxlatCfg_1010_0(Etw):
    pattern = Struct(
        "InterfaceLuid" / Int64ul
    )


@declare(guid=guid("3e5ac668-af52-4c15-b99b-a3e7a6616ebd"), event_id=1011, version=0)
class Microsoft_Windows_IPxlatCfg_1011_0(Etw):
    pattern = Struct(
        "InfoString" / CString,
        "MTU" / Int32ul
    )


@declare(guid=guid("3e5ac668-af52-4c15-b99b-a3e7a6616ebd"), event_id=1101, version=0)
class Microsoft_Windows_IPxlatCfg_1101_0(Etw):
    pattern = Struct(
        "InterfaceLuid" / Int64ul,
        "Metric" / Int32ul,
        "RemotePrefixLength" / Int32ul,
        "LocalPrefixLength" / Int32ul
    )


@declare(guid=guid("3e5ac668-af52-4c15-b99b-a3e7a6616ebd"), event_id=1102, version=0)
class Microsoft_Windows_IPxlatCfg_1102_0(Etw):
    pattern = Struct(
        "InterfaceLuid" / Int64ul,
        "Metric" / Int32ul,
        "RemotePrefixLength" / Int32ul,
        "LocalPrefixLength" / Int32ul
    )


@declare(guid=guid("3e5ac668-af52-4c15-b99b-a3e7a6616ebd"), event_id=1103, version=0)
class Microsoft_Windows_IPxlatCfg_1103_0(Etw):
    pattern = Struct(
        "InterfaceLuid" / Int64ul,
        "PrefixLength" / Int32ul
    )

