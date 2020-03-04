# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SetupUGC
GUID : 75ebc33e-0870-49e5-bdce-9d7028279489
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("75ebc33e-0870-49e5-bdce-9d7028279489"), event_id=1001, version=0)
class Microsoft_Windows_SetupUGC_1001_0(Etw):
    pattern = Struct(
        "CommandLine" / WString
    )


@declare(guid=guid("75ebc33e-0870-49e5-bdce-9d7028279489"), event_id=1002, version=0)
class Microsoft_Windows_SetupUGC_1002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("75ebc33e-0870-49e5-bdce-9d7028279489"), event_id=2001, version=0)
class Microsoft_Windows_SetupUGC_2001_0(Etw):
    pattern = Struct(
        "Pass" / WString
    )


@declare(guid=guid("75ebc33e-0870-49e5-bdce-9d7028279489"), event_id=2002, version=0)
class Microsoft_Windows_SetupUGC_2002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("75ebc33e-0870-49e5-bdce-9d7028279489"), event_id=3001, version=0)
class Microsoft_Windows_SetupUGC_3001_0(Etw):
    pattern = Struct(
        "Processor" / WString
    )


@declare(guid=guid("75ebc33e-0870-49e5-bdce-9d7028279489"), event_id=3002, version=0)
class Microsoft_Windows_SetupUGC_3002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )

