# -*- coding: utf-8 -*-
"""
Intel-SST-BUS
GUID : b28427d2-a745-43ba-8aec-ffe3b94f97d3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b28427d2-a745-43ba-8aec-ffe3b94f97d3"), event_id=1, version=1)
class Intel_SST_BUS_1_1(Etw):
    pattern = Struct(
        "status" / Int32ul
    )


@declare(guid=guid("b28427d2-a745-43ba-8aec-ffe3b94f97d3"), event_id=3, version=1)
class Intel_SST_BUS_3_1(Etw):
    pattern = Struct(
        "status" / Int32ul
    )


@declare(guid=guid("b28427d2-a745-43ba-8aec-ffe3b94f97d3"), event_id=4, version=1)
class Intel_SST_BUS_4_1(Etw):
    pattern = Struct(
        "WDFDevice" / Int64ul,
        "DeviceState" / Int32ul
    )


@declare(guid=guid("b28427d2-a745-43ba-8aec-ffe3b94f97d3"), event_id=6, version=1)
class Intel_SST_BUS_6_1(Etw):
    pattern = Struct(
        "WDFDevice" / Int64ul,
        "DeviceState" / Int32ul
    )


@declare(guid=guid("b28427d2-a745-43ba-8aec-ffe3b94f97d3"), event_id=8, version=1)
class Intel_SST_BUS_8_1(Etw):
    pattern = Struct(
        "WDFDevice" / Int64ul,
        "DeviceState" / Int32ul
    )


@declare(guid=guid("b28427d2-a745-43ba-8aec-ffe3b94f97d3"), event_id=10, version=1)
class Intel_SST_BUS_10_1(Etw):
    pattern = Struct(
        "WDFDevice" / Int64ul,
        "DeviceState" / Int32ul
    )


@declare(guid=guid("b28427d2-a745-43ba-8aec-ffe3b94f97d3"), event_id=12, version=1)
class Intel_SST_BUS_12_1(Etw):
    pattern = Struct(
        "device" / Int64ul
    )


@declare(guid=guid("b28427d2-a745-43ba-8aec-ffe3b94f97d3"), event_id=14, version=1)
class Intel_SST_BUS_14_1(Etw):
    pattern = Struct(
        "device" / Int64ul
    )


@declare(guid=guid("b28427d2-a745-43ba-8aec-ffe3b94f97d3"), event_id=16, version=1)
class Intel_SST_BUS_16_1(Etw):
    pattern = Struct(
        "device" / Int64ul
    )


@declare(guid=guid("b28427d2-a745-43ba-8aec-ffe3b94f97d3"), event_id=18, version=1)
class Intel_SST_BUS_18_1(Etw):
    pattern = Struct(
        "device" / Int64ul
    )


@declare(guid=guid("b28427d2-a745-43ba-8aec-ffe3b94f97d3"), event_id=23, version=1)
class Intel_SST_BUS_23_1(Etw):
    pattern = Struct(
        "intStatusAndControl" / Int32ul,
        "InterruptStatus" / Int32ul,
        "RIRBStatus" / Int32ul,
        "CORBStatus" / Int32ul,
        "dspStatus" / Int32ul,
        "stateSTS" / Int16ul
    )


@declare(guid=guid("b28427d2-a745-43ba-8aec-ffe3b94f97d3"), event_id=401, version=1)
class Intel_SST_BUS_401_1(Etw):
    pattern = Struct(
        "status" / Int32ul,
        "lineNo" / Int32ul
    )


@declare(guid=guid("b28427d2-a745-43ba-8aec-ffe3b94f97d3"), event_id=402, version=0)
class Intel_SST_BUS_402_0(Etw):
    pattern = Struct(
        "status" / Int32ul,
        "lineNo" / Int32ul
    )

