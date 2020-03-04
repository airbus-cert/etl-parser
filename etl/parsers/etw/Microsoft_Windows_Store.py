# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Store
GUID : 9c2a37f3-e5fd-5cae-bcd1-43dafeee1ff0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9c2a37f3-e5fd-5cae-bcd1-43dafeee1ff0"), event_id=8000, version=0)
class Microsoft_Windows_Store_8000_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "ModuleName" / WString,
        "BuildName" / WString
    )


@declare(guid=guid("9c2a37f3-e5fd-5cae-bcd1-43dafeee1ff0"), event_id=8001, version=0)
class Microsoft_Windows_Store_8001_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("9c2a37f3-e5fd-5cae-bcd1-43dafeee1ff0"), event_id=8002, version=0)
class Microsoft_Windows_Store_8002_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("9c2a37f3-e5fd-5cae-bcd1-43dafeee1ff0"), event_id=8003, version=0)
class Microsoft_Windows_Store_8003_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("9c2a37f3-e5fd-5cae-bcd1-43dafeee1ff0"), event_id=8010, version=0)
class Microsoft_Windows_Store_8010_0(Etw):
    pattern = Struct(
        "StateMachine" / Int64ul,
        "ThreadID" / Int32ul,
        "StateMachineName" / WString,
        "EventName" / CString
    )


@declare(guid=guid("9c2a37f3-e5fd-5cae-bcd1-43dafeee1ff0"), event_id=8011, version=0)
class Microsoft_Windows_Store_8011_0(Etw):
    pattern = Struct(
        "StateMachine" / Int64ul,
        "ThreadID" / Int32ul,
        "StateMachineName" / WString,
        "EventName" / CString,
        "CurrentState" / WString
    )


@declare(guid=guid("9c2a37f3-e5fd-5cae-bcd1-43dafeee1ff0"), event_id=8012, version=0)
class Microsoft_Windows_Store_8012_0(Etw):
    pattern = Struct(
        "StateMachine" / Int64ul,
        "ThreadID" / Int32ul,
        "CurrentState" / WString,
        "NewState" / WString,
        "StateMachineName" / WString
    )


@declare(guid=guid("9c2a37f3-e5fd-5cae-bcd1-43dafeee1ff0"), event_id=8013, version=0)
class Microsoft_Windows_Store_8013_0(Etw):
    pattern = Struct(
        "StateMachine" / Int64ul,
        "ThreadID" / Int32ul,
        "StateMachineName" / WString,
        "CurrentState" / WString
    )


@declare(guid=guid("9c2a37f3-e5fd-5cae-bcd1-43dafeee1ff0"), event_id=8014, version=0)
class Microsoft_Windows_Store_8014_0(Etw):
    pattern = Struct(
        "StateMachine" / Int64ul,
        "ThreadID" / Int32ul,
        "StateMachineName" / WString,
        "CurrentState" / WString
    )

