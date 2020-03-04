# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Winsrv
GUID : 9d55b53d-449b-4824-a637-24f9d69aa02f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9d55b53d-449b-4824-a637-24f9d69aa02f"), event_id=10001, version=0)
class Microsoft_Windows_Winsrv_10001_0(Etw):
    pattern = Struct(
        "AppName" / WString,
        "ResponseTime" / Int32ul
    )


@declare(guid=guid("9d55b53d-449b-4824-a637-24f9d69aa02f"), event_id=10002, version=0)
class Microsoft_Windows_Winsrv_10002_0(Etw):
    pattern = Struct(
        "AppName" / WString
    )


@declare(guid=guid("9d55b53d-449b-4824-a637-24f9d69aa02f"), event_id=12001, version=0)
class Microsoft_Windows_Winsrv_12001_0(Etw):
    pattern = Struct(
        "ThreadId" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("9d55b53d-449b-4824-a637-24f9d69aa02f"), event_id=12001, version=1)
class Microsoft_Windows_Winsrv_12001_1(Etw):
    pattern = Struct(
        "ThreadId" / Int32ul,
        "Flags" / Int32ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("9d55b53d-449b-4824-a637-24f9d69aa02f"), event_id=12002, version=0)
class Microsoft_Windows_Winsrv_12002_0(Etw):
    pattern = Struct(
        "Command" / Int32ul
    )


@declare(guid=guid("9d55b53d-449b-4824-a637-24f9d69aa02f"), event_id=12002, version=1)
class Microsoft_Windows_Winsrv_12002_1(Etw):
    pattern = Struct(
        "Command" / Int32ul,
        "ThreadId" / Int32ul
    )


@declare(guid=guid("9d55b53d-449b-4824-a637-24f9d69aa02f"), event_id=12003, version=0)
class Microsoft_Windows_Winsrv_12003_0(Etw):
    pattern = Struct(
        "MessageId" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("9d55b53d-449b-4824-a637-24f9d69aa02f"), event_id=12003, version=1)
class Microsoft_Windows_Winsrv_12003_1(Etw):
    pattern = Struct(
        "MessageId" / Int32ul,
        "Flags" / Int32ul,
        "ThreadId" / Int32ul
    )


@declare(guid=guid("9d55b53d-449b-4824-a637-24f9d69aa02f"), event_id=12005, version=1)
class Microsoft_Windows_Winsrv_12005_1(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul
    )


@declare(guid=guid("9d55b53d-449b-4824-a637-24f9d69aa02f"), event_id=12006, version=1)
class Microsoft_Windows_Winsrv_12006_1(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "TerminateStatus" / Int32ul
    )


@declare(guid=guid("9d55b53d-449b-4824-a637-24f9d69aa02f"), event_id=12007, version=1)
class Microsoft_Windows_Winsrv_12007_1(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul
    )


@declare(guid=guid("9d55b53d-449b-4824-a637-24f9d69aa02f"), event_id=12008, version=0)
class Microsoft_Windows_Winsrv_12008_0(Etw):
    pattern = Struct(
        "WaitStatus" / Int32ul
    )


@declare(guid=guid("9d55b53d-449b-4824-a637-24f9d69aa02f"), event_id=12008, version=1)
class Microsoft_Windows_Winsrv_12008_1(Etw):
    pattern = Struct(
        "WaitStatus" / Int32ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("9d55b53d-449b-4824-a637-24f9d69aa02f"), event_id=12009, version=1)
class Microsoft_Windows_Winsrv_12009_1(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("9d55b53d-449b-4824-a637-24f9d69aa02f"), event_id=12010, version=1)
class Microsoft_Windows_Winsrv_12010_1(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("9d55b53d-449b-4824-a637-24f9d69aa02f"), event_id=12011, version=1)
class Microsoft_Windows_Winsrv_12011_1(Etw):
    pattern = Struct(
        "EventType" / Int32ul
    )


@declare(guid=guid("9d55b53d-449b-4824-a637-24f9d69aa02f"), event_id=12012, version=1)
class Microsoft_Windows_Winsrv_12012_1(Etw):
    pattern = Struct(
        "EventType" / Int32ul
    )

