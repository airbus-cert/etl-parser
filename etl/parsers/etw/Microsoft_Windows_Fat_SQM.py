# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Fat-SQM
GUID : 3e59a529-b0b3-4a11-8129-9ffe6bb46eb9
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3e59a529-b0b3-4a11-8129-9ffe6bb46eb9"), event_id=3, version=0)
class Microsoft_Windows_Fat_SQM_3_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmSid" / Sid,
        "SqmWindowsSessionId" / Int32ul,
        "SqmSessionFlags" / Int32ul
    )


@declare(guid=guid("3e59a529-b0b3-4a11-8129-9ffe6bb46eb9"), event_id=4, version=0)
class Microsoft_Windows_Fat_SQM_4_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid
    )


@declare(guid=guid("3e59a529-b0b3-4a11-8129-9ffe6bb46eb9"), event_id=5, version=0)
class Microsoft_Windows_Fat_SQM_5_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("3e59a529-b0b3-4a11-8129-9ffe6bb46eb9"), event_id=6, version=0)
class Microsoft_Windows_Fat_SQM_6_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("3e59a529-b0b3-4a11-8129-9ffe6bb46eb9"), event_id=7, version=0)
class Microsoft_Windows_Fat_SQM_7_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("3e59a529-b0b3-4a11-8129-9ffe6bb46eb9"), event_id=8, version=0)
class Microsoft_Windows_Fat_SQM_8_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("3e59a529-b0b3-4a11-8129-9ffe6bb46eb9"), event_id=9, version=0)
class Microsoft_Windows_Fat_SQM_9_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("3e59a529-b0b3-4a11-8129-9ffe6bb46eb9"), event_id=10, version=0)
class Microsoft_Windows_Fat_SQM_10_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmStringDatapointValue" / WString
    )


@declare(guid=guid("3e59a529-b0b3-4a11-8129-9ffe6bb46eb9"), event_id=11, version=0)
class Microsoft_Windows_Fat_SQM_11_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("3e59a529-b0b3-4a11-8129-9ffe6bb46eb9"), event_id=16, version=0)
class Microsoft_Windows_Fat_SQM_16_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmProcessHashValue" / Int32ul,
        "SqmDWORD64DatapointValue" / Int64ul
    )


@declare(guid=guid("3e59a529-b0b3-4a11-8129-9ffe6bb46eb9"), event_id=17, version=0)
class Microsoft_Windows_Fat_SQM_17_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmProcessHashValue" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamEntriesSize" / Int32ul,
        "SqmStreamEntries" / Bytes(lambda this: this.SqmStreamEntriesSize),
        "SqmStreamFlags" / Int32ul
    )

