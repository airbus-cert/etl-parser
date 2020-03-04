# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Speech-UserExperience
GUID : 13480a22-d79f-4334-9d32-aa239398ad3c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("13480a22-d79f-4334-9d32-aa239398ad3c"), event_id=68, version=0)
class Microsoft_Windows_Speech_UserExperience_68_0(Etw):
    pattern = Struct(
        "State" / Int32ul
    )


@declare(guid=guid("13480a22-d79f-4334-9d32-aa239398ad3c"), event_id=69, version=0)
class Microsoft_Windows_Speech_UserExperience_69_0(Etw):
    pattern = Struct(
        "State" / Int32ul
    )


@declare(guid=guid("13480a22-d79f-4334-9d32-aa239398ad3c"), event_id=123, version=0)
class Microsoft_Windows_Speech_UserExperience_123_0(Etw):
    pattern = Struct(
        "ElementsExamined" / Int32ul,
        "ElementsAdded" / Int32ul,
        "CrossProcCalls" / Int32ul
    )


@declare(guid=guid("13480a22-d79f-4334-9d32-aa239398ad3c"), event_id=141, version=0)
class Microsoft_Windows_Speech_UserExperience_141_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "Index" / Int32ul,
        "Item" / WString
    )

