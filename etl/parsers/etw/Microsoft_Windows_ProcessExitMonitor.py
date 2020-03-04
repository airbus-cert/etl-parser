# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ProcessExitMonitor
GUID : fd771d53-8492-4057-8e35-8c02813af49b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("fd771d53-8492-4057-8e35-8c02813af49b"), event_id=3000, version=0)
class Microsoft_Windows_ProcessExitMonitor_3000_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("fd771d53-8492-4057-8e35-8c02813af49b"), event_id=3001, version=0)
class Microsoft_Windows_ProcessExitMonitor_3001_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )

