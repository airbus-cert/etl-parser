# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ActionQueue
GUID : 0dd4d48e-2bbf-452f-a7ec-ba3dba8407ae
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("0dd4d48e-2bbf-452f-a7ec-ba3dba8407ae"), event_id=1001, version=0)
class Microsoft_Windows_ActionQueue_1001_0(Etw):
    pattern = Struct(
        "QueueFile" / WString
    )


@declare(guid=guid("0dd4d48e-2bbf-452f-a7ec-ba3dba8407ae"), event_id=1002, version=0)
class Microsoft_Windows_ActionQueue_1002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("0dd4d48e-2bbf-452f-a7ec-ba3dba8407ae"), event_id=2001, version=0)
class Microsoft_Windows_ActionQueue_2001_0(Etw):
    pattern = Struct(
        "ExecutableName" / CString,
        "Arguments" / CString,
        "Identity" / CString,
        "Pass" / CString
    )


@declare(guid=guid("0dd4d48e-2bbf-452f-a7ec-ba3dba8407ae"), event_id=2002, version=0)
class Microsoft_Windows_ActionQueue_2002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )

