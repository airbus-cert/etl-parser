# -*- coding: utf-8 -*-
"""
Microsoft-Windows-exFAT-SQM
GUID : 494e7a3d-8db9-4ec4-b43e-2844af6e38d6
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("494e7a3d-8db9-4ec4-b43e-2844af6e38d6"), event_id=3, version=0)
class Microsoft_Windows_exFAT_SQM_3_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmSid" / Sid,
        "SqmWindowsSessionId" / Int32ul,
        "SqmSessionFlags" / Int32ul
    )


@declare(guid=guid("494e7a3d-8db9-4ec4-b43e-2844af6e38d6"), event_id=4, version=0)
class Microsoft_Windows_exFAT_SQM_4_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid
    )


@declare(guid=guid("494e7a3d-8db9-4ec4-b43e-2844af6e38d6"), event_id=5, version=0)
class Microsoft_Windows_exFAT_SQM_5_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("494e7a3d-8db9-4ec4-b43e-2844af6e38d6"), event_id=6, version=0)
class Microsoft_Windows_exFAT_SQM_6_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("494e7a3d-8db9-4ec4-b43e-2844af6e38d6"), event_id=7, version=0)
class Microsoft_Windows_exFAT_SQM_7_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("494e7a3d-8db9-4ec4-b43e-2844af6e38d6"), event_id=8, version=0)
class Microsoft_Windows_exFAT_SQM_8_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("494e7a3d-8db9-4ec4-b43e-2844af6e38d6"), event_id=9, version=0)
class Microsoft_Windows_exFAT_SQM_9_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("494e7a3d-8db9-4ec4-b43e-2844af6e38d6"), event_id=10, version=0)
class Microsoft_Windows_exFAT_SQM_10_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmStringDatapointValue" / WString
    )


@declare(guid=guid("494e7a3d-8db9-4ec4-b43e-2844af6e38d6"), event_id=11, version=0)
class Microsoft_Windows_exFAT_SQM_11_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("494e7a3d-8db9-4ec4-b43e-2844af6e38d6"), event_id=16, version=0)
class Microsoft_Windows_exFAT_SQM_16_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmProcessHashValue" / Int32ul,
        "SqmDWORD64DatapointValue" / Int64ul
    )


@declare(guid=guid("494e7a3d-8db9-4ec4-b43e-2844af6e38d6"), event_id=17, version=0)
class Microsoft_Windows_exFAT_SQM_17_0(Etw):
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

