# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MemoryDiagnostics-Schedule
GUID : 73e9c9de-a148-41f7-b1db-4da051fdc327
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("73e9c9de-a148-41f7-b1db-4da051fdc327"), event_id=1001, version=0)
class Microsoft_Windows_MemoryDiagnostics_Schedule_1001_0(Etw):
    pattern = Struct(
        "LaunchType" / WString,
        "ScheduleType" / WString
    )


@declare(guid=guid("73e9c9de-a148-41f7-b1db-4da051fdc327"), event_id=1002, version=0)
class Microsoft_Windows_MemoryDiagnostics_Schedule_1002_0(Etw):
    pattern = Struct(
        "LaunchType" / WString,
        "ScheduleType" / WString
    )


@declare(guid=guid("73e9c9de-a148-41f7-b1db-4da051fdc327"), event_id=1003, version=0)
class Microsoft_Windows_MemoryDiagnostics_Schedule_1003_0(Etw):
    pattern = Struct(
        "LaunchType" / WString,
        "ScheduleType" / WString,
        "ErrorCode" / Int32ul
    )

