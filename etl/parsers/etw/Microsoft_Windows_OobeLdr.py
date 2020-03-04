# -*- coding: utf-8 -*-
"""
Microsoft-Windows-OobeLdr
GUID : 75ebc33e-8670-4eb6-b535-3b9d6bb222fd
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("75ebc33e-8670-4eb6-b535-3b9d6bb222fd"), event_id=1001, version=0)
class Microsoft_Windows_OobeLdr_1001_0(Etw):
    pattern = Struct(
        "CommandLine" / WString
    )


@declare(guid=guid("75ebc33e-8670-4eb6-b535-3b9d6bb222fd"), event_id=1002, version=0)
class Microsoft_Windows_OobeLdr_1002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("75ebc33e-8670-4eb6-b535-3b9d6bb222fd"), event_id=2001, version=0)
class Microsoft_Windows_OobeLdr_2001_0(Etw):
    pattern = Struct(
        "Pass" / WString
    )


@declare(guid=guid("75ebc33e-8670-4eb6-b535-3b9d6bb222fd"), event_id=2002, version=0)
class Microsoft_Windows_OobeLdr_2002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("75ebc33e-8670-4eb6-b535-3b9d6bb222fd"), event_id=2003, version=0)
class Microsoft_Windows_OobeLdr_2003_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("75ebc33e-8670-4eb6-b535-3b9d6bb222fd"), event_id=2004, version=0)
class Microsoft_Windows_OobeLdr_2004_0(Etw):
    pattern = Struct(
        "Pass" / WString,
        "FilePath" / WString
    )


@declare(guid=guid("75ebc33e-8670-4eb6-b535-3b9d6bb222fd"), event_id=3002, version=0)
class Microsoft_Windows_OobeLdr_3002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )

