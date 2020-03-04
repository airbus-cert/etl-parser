# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Registry-SQM-Provider
GUID : 017ba13c-9a55-4f1f-8200-323055aac810
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("017ba13c-9a55-4f1f-8200-323055aac810"), event_id=5, version=0)
class Microsoft_Windows_Registry_SQM_Provider_5_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("017ba13c-9a55-4f1f-8200-323055aac810"), event_id=6, version=0)
class Microsoft_Windows_Registry_SQM_Provider_6_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("017ba13c-9a55-4f1f-8200-323055aac810"), event_id=7, version=0)
class Microsoft_Windows_Registry_SQM_Provider_7_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("017ba13c-9a55-4f1f-8200-323055aac810"), event_id=8, version=0)
class Microsoft_Windows_Registry_SQM_Provider_8_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("017ba13c-9a55-4f1f-8200-323055aac810"), event_id=9, version=0)
class Microsoft_Windows_Registry_SQM_Provider_9_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("017ba13c-9a55-4f1f-8200-323055aac810"), event_id=10, version=0)
class Microsoft_Windows_Registry_SQM_Provider_10_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmStringDatapointValue" / WString
    )


@declare(guid=guid("017ba13c-9a55-4f1f-8200-323055aac810"), event_id=11, version=0)
class Microsoft_Windows_Registry_SQM_Provider_11_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )

