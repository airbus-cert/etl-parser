# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Windeploy
GUID : 75ebc33e-c8ae-4f93-9ca1-683a53e20cb6
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("75ebc33e-c8ae-4f93-9ca1-683a53e20cb6"), event_id=1001, version=0)
class Microsoft_Windows_Windeploy_1001_0(Etw):
    pattern = Struct(
        "CommandLine" / WString
    )


@declare(guid=guid("75ebc33e-c8ae-4f93-9ca1-683a53e20cb6"), event_id=1002, version=0)
class Microsoft_Windows_Windeploy_1002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("75ebc33e-c8ae-4f93-9ca1-683a53e20cb6"), event_id=2001, version=0)
class Microsoft_Windows_Windeploy_2001_0(Etw):
    pattern = Struct(
        "CommandLine" / WString
    )


@declare(guid=guid("75ebc33e-c8ae-4f93-9ca1-683a53e20cb6"), event_id=2002, version=0)
class Microsoft_Windows_Windeploy_2002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("75ebc33e-c8ae-4f93-9ca1-683a53e20cb6"), event_id=2003, version=0)
class Microsoft_Windows_Windeploy_2003_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("75ebc33e-c8ae-4f93-9ca1-683a53e20cb6"), event_id=3001, version=0)
class Microsoft_Windows_Windeploy_3001_0(Etw):
    pattern = Struct(
        "CommandLine" / WString
    )


@declare(guid=guid("75ebc33e-c8ae-4f93-9ca1-683a53e20cb6"), event_id=3002, version=0)
class Microsoft_Windows_Windeploy_3002_0(Etw):
    pattern = Struct(
        "Command" / WString,
        "ExitCode" / Int32ul
    )


@declare(guid=guid("75ebc33e-c8ae-4f93-9ca1-683a53e20cb6"), event_id=3003, version=0)
class Microsoft_Windows_Windeploy_3003_0(Etw):
    pattern = Struct(
        "Command" / WString,
        "ExitCode" / Int32ul
    )

