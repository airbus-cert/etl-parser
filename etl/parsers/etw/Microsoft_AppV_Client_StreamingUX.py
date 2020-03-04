# -*- coding: utf-8 -*-
"""
Microsoft-AppV-Client-StreamingUX
GUID : 28cb46c7-4003-4e50-8bd9-442086762d12
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=1, version=1)
class Microsoft_AppV_Client_StreamingUX_1_1(Etw):
    pattern = Struct(
        "astring" / WString,
        "uint64" / Int64ul
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=2, version=1)
class Microsoft_AppV_Client_StreamingUX_2_1(Etw):
    pattern = Struct(
        "astring" / WString,
        "uint64" / Int64ul
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=3, version=1)
class Microsoft_AppV_Client_StreamingUX_3_1(Etw):
    pattern = Struct(
        "unint64" / Int64ul
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=4, version=1)
class Microsoft_AppV_Client_StreamingUX_4_1(Etw):
    pattern = Struct(
        "unint64" / Int64ul,
        "uint642" / Int64ul
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=5, version=1)
class Microsoft_AppV_Client_StreamingUX_5_1(Etw):
    pattern = Struct(
        "astring" / WString
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=6, version=1)
class Microsoft_AppV_Client_StreamingUX_6_1(Etw):
    pattern = Struct(
        "astring" / WString
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=20, version=1)
class Microsoft_AppV_Client_StreamingUX_20_1(Etw):
    pattern = Struct(
        "unint64" / Int64ul
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=21, version=1)
class Microsoft_AppV_Client_StreamingUX_21_1(Etw):
    pattern = Struct(
        "unint64" / Int64ul
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=40, version=1)
class Microsoft_AppV_Client_StreamingUX_40_1(Etw):
    pattern = Struct(
        "unint64" / Int64ul
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=41, version=1)
class Microsoft_AppV_Client_StreamingUX_41_1(Etw):
    pattern = Struct(
        "unint64" / Int64ul
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=42, version=1)
class Microsoft_AppV_Client_StreamingUX_42_1(Etw):
    pattern = Struct(
        "astring" / WString,
        "uint64" / Int64ul
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=43, version=1)
class Microsoft_AppV_Client_StreamingUX_43_1(Etw):
    pattern = Struct(
        "unint64" / Int64ul
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=44, version=1)
class Microsoft_AppV_Client_StreamingUX_44_1(Etw):
    pattern = Struct(
        "unint64" / Int64ul
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=45, version=1)
class Microsoft_AppV_Client_StreamingUX_45_1(Etw):
    pattern = Struct(
        "unint64" / Int64ul
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=60, version=1)
class Microsoft_AppV_Client_StreamingUX_60_1(Etw):
    pattern = Struct(
        "packageId" / Guid,
        "versionId" / Guid
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=61, version=1)
class Microsoft_AppV_Client_StreamingUX_61_1(Etw):
    pattern = Struct(
        "packageId" / Guid,
        "versionId" / Guid,
        "percentageComplete" / Int64ul
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=80, version=1)
class Microsoft_AppV_Client_StreamingUX_80_1(Etw):
    pattern = Struct(
        "unint64" / Int64ul
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=101, version=1)
class Microsoft_AppV_Client_StreamingUX_101_1(Etw):
    pattern = Struct(
        "uint32" / Int32ul
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=102, version=1)
class Microsoft_AppV_Client_StreamingUX_102_1(Etw):
    pattern = Struct(
        "astring" / WString
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=120, version=1)
class Microsoft_AppV_Client_StreamingUX_120_1(Etw):
    pattern = Struct(
        "unint64" / Int64ul
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=121, version=1)
class Microsoft_AppV_Client_StreamingUX_121_1(Etw):
    pattern = Struct(
        "unint64" / Int64ul
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=122, version=1)
class Microsoft_AppV_Client_StreamingUX_122_1(Etw):
    pattern = Struct(
        "unint64" / Int64ul
    )


@declare(guid=guid("28cb46c7-4003-4e50-8bd9-442086762d12"), event_id=150, version=1)
class Microsoft_AppV_Client_StreamingUX_150_1(Etw):
    pattern = Struct(
        "server" / WString,
        "global" / Int8ul,
        "packageTotal" / Int32ul,
        "packageSucceeded" / Int32ul,
        "packageFailed" / Int32ul,
        "groupTotal" / Int32ul,
        "groupSucceeded" / Int32ul,
        "groupFailed" / Int32ul
    )

