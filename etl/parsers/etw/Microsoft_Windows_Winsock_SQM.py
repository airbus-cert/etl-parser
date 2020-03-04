# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Winsock-SQM
GUID : 093da50c-0bb9-4d7d-b95c-3bb9fcda5ee8
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("093da50c-0bb9-4d7d-b95c-3bb9fcda5ee8"), event_id=5, version=0)
class Microsoft_Windows_Winsock_SQM_5_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("093da50c-0bb9-4d7d-b95c-3bb9fcda5ee8"), event_id=10, version=0)
class Microsoft_Windows_Winsock_SQM_10_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmStringDatapointValue" / WString
    )


@declare(guid=guid("093da50c-0bb9-4d7d-b95c-3bb9fcda5ee8"), event_id=11, version=0)
class Microsoft_Windows_Winsock_SQM_11_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )

