# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WPD-MTPBT
GUID : 92ab58d3-f351-4af5-9c72-d52f36ee2c92
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("92ab58d3-f351-4af5-9c72-d52f36ee2c92"), event_id=100, version=0)
class Microsoft_Windows_WPD_MTPBT_100_0(Etw):
    pattern = Struct(
        "MTPBTPacketLength" / Int32ul,
        "MTPBTPacketData" / Bytes(lambda this: this.MTPBTPacketLength)
    )


@declare(guid=guid("92ab58d3-f351-4af5-9c72-d52f36ee2c92"), event_id=101, version=0)
class Microsoft_Windows_WPD_MTPBT_101_0(Etw):
    pattern = Struct(
        "MTPBTPacketLength" / Int32ul,
        "MTPBTPacketData" / Bytes(lambda this: this.MTPBTPacketLength)
    )


@declare(guid=guid("92ab58d3-f351-4af5-9c72-d52f36ee2c92"), event_id=102, version=0)
class Microsoft_Windows_WPD_MTPBT_102_0(Etw):
    pattern = Struct(
        "MTPBTPacketLength" / Int32ul,
        "MTPBTPacketData" / Bytes(lambda this: this.MTPBTPacketLength)
    )


@declare(guid=guid("92ab58d3-f351-4af5-9c72-d52f36ee2c92"), event_id=103, version=0)
class Microsoft_Windows_WPD_MTPBT_103_0(Etw):
    pattern = Struct(
        "MTPBTPacketLength" / Int32ul,
        "MTPBTPacketData" / Bytes(lambda this: this.MTPBTPacketLength)
    )


@declare(guid=guid("92ab58d3-f351-4af5-9c72-d52f36ee2c92"), event_id=104, version=0)
class Microsoft_Windows_WPD_MTPBT_104_0(Etw):
    pattern = Struct(
        "MTPBTPacketLength" / Int32ul,
        "MTPBTPacketType" / Int16ul,
        "MTPBTPacketSeqID" / Int16ul
    )


@declare(guid=guid("92ab58d3-f351-4af5-9c72-d52f36ee2c92"), event_id=105, version=0)
class Microsoft_Windows_WPD_MTPBT_105_0(Etw):
    pattern = Struct(
        "MTPBTEventLength" / Int32ul,
        "MTPBTEventData" / Bytes(lambda this: this.MTPBTEventLength)
    )


@declare(guid=guid("92ab58d3-f351-4af5-9c72-d52f36ee2c92"), event_id=106, version=0)
class Microsoft_Windows_WPD_MTPBT_106_0(Etw):
    pattern = Struct(
        "MTPBTPacketLength" / Int32ul,
        "MTPBTPacketType" / Int16ul,
        "MTPBTPacketSeqID" / Int16ul
    )


@declare(guid=guid("92ab58d3-f351-4af5-9c72-d52f36ee2c92"), event_id=107, version=0)
class Microsoft_Windows_WPD_MTPBT_107_0(Etw):
    pattern = Struct(
        "MTPBTPacketLength" / Int32ul,
        "MTPBTPacketType" / Int16ul,
        "MTPBTPacketSeqID" / Int16ul
    )

