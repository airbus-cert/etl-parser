# -*- coding: utf-8 -*-
"""
Microsoft-AppV-ServiceLog
GUID : 9cc69d1c-7917-4acd-8066-6bf8b63e551b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9cc69d1c-7917-4acd-8066-6bf8b63e551b"), event_id=1, version=0)
class Microsoft_AppV_ServiceLog_1_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("9cc69d1c-7917-4acd-8066-6bf8b63e551b"), event_id=2, version=0)
class Microsoft_AppV_ServiceLog_2_0(Etw):
    pattern = Struct(
        "WString1" / WString
    )


@declare(guid=guid("9cc69d1c-7917-4acd-8066-6bf8b63e551b"), event_id=3, version=0)
class Microsoft_AppV_ServiceLog_3_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / WString,
        "Line" / Int32ul
    )

