# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SetupQueue
GUID : a615acb9-d5a4-4738-b561-1df301d207f8
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a615acb9-d5a4-4738-b561-1df301d207f8"), event_id=1001, version=0)
class Microsoft_Windows_SetupQueue_1001_0(Etw):
    pattern = Struct(
        "Command" / WString
    )


@declare(guid=guid("a615acb9-d5a4-4738-b561-1df301d207f8"), event_id=1002, version=0)
class Microsoft_Windows_SetupQueue_1002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a615acb9-d5a4-4738-b561-1df301d207f8"), event_id=1003, version=0)
class Microsoft_Windows_SetupQueue_1003_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )

