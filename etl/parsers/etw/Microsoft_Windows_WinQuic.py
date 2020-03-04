# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WinQuic
GUID : 2bcfefe5-5026-536b-1686-b249cb49cae3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("2bcfefe5-5026-536b-1686-b249cb49cae3"), event_id=1, version=0)
class Microsoft_Windows_WinQuic_1_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "IsServer" / Int32ul
    )


@declare(guid=guid("2bcfefe5-5026-536b-1686-b249cb49cae3"), event_id=2, version=0)
class Microsoft_Windows_WinQuic_2_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul
    )


@declare(guid=guid("2bcfefe5-5026-536b-1686-b249cb49cae3"), event_id=3, version=0)
class Microsoft_Windows_WinQuic_3_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul
    )


@declare(guid=guid("2bcfefe5-5026-536b-1686-b249cb49cae3"), event_id=4, version=0)
class Microsoft_Windows_WinQuic_4_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "State" / Int32ul
    )


@declare(guid=guid("2bcfefe5-5026-536b-1686-b249cb49cae3"), event_id=5, version=0)
class Microsoft_Windows_WinQuic_5_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "Type" / Int32ul
    )


@declare(guid=guid("2bcfefe5-5026-536b-1686-b249cb49cae3"), event_id=6, version=0)
class Microsoft_Windows_WinQuic_6_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "Type" / Int32ul
    )


@declare(guid=guid("2bcfefe5-5026-536b-1686-b249cb49cae3"), event_id=7, version=0)
class Microsoft_Windows_WinQuic_7_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "Type" / Int32ul
    )


@declare(guid=guid("2bcfefe5-5026-536b-1686-b249cb49cae3"), event_id=100, version=0)
class Microsoft_Windows_WinQuic_100_0(Etw):
    pattern = Struct(
        "Stream" / Int64ul,
        "Connection" / Int64ul,
        "ID" / Int64ul
    )


@declare(guid=guid("2bcfefe5-5026-536b-1686-b249cb49cae3"), event_id=101, version=0)
class Microsoft_Windows_WinQuic_101_0(Etw):
    pattern = Struct(
        "Stream" / Int64ul
    )


@declare(guid=guid("2bcfefe5-5026-536b-1686-b249cb49cae3"), event_id=1000, version=0)
class Microsoft_Windows_WinQuic_1000_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "BytesSent" / Int64ul,
        "BytesInFlight" / Int32ul,
        "BytesInFlightMax" / Int32ul,
        "CongestionWindow" / Int32ul,
        "SlowStartThreshold" / Int32ul,
        "IsInRecovery" / Int32ul,
        "ConnectionFlowControl" / Int64ul,
        "StreamFlowControl" / Int64ul,
        "IdealBytes" / Int64ul,
        "PostedBytes" / Int64ul,
        "SmoothedRtt" / Int32ul
    )


@declare(guid=guid("2bcfefe5-5026-536b-1686-b249cb49cae3"), event_id=1001, version=0)
class Microsoft_Windows_WinQuic_1001_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "Reason" / CString
    )


@declare(guid=guid("2bcfefe5-5026-536b-1686-b249cb49cae3"), event_id=1002, version=0)
class Microsoft_Windows_WinQuic_1002_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "Reason" / CString
    )


@declare(guid=guid("2bcfefe5-5026-536b-1686-b249cb49cae3"), event_id=1003, version=0)
class Microsoft_Windows_WinQuic_1003_0(Etw):
    pattern = Struct(
        "Stream" / Int64ul,
        "Reason" / CString
    )


@declare(guid=guid("2bcfefe5-5026-536b-1686-b249cb49cae3"), event_id=1004, version=0)
class Microsoft_Windows_WinQuic_1004_0(Etw):
    pattern = Struct(
        "Stream" / Int64ul,
        "Reason" / CString
    )


@declare(guid=guid("2bcfefe5-5026-536b-1686-b249cb49cae3"), event_id=1005, version=0)
class Microsoft_Windows_WinQuic_1005_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "SlowStartThreshold" / Int32ul,
        "K" / Int32ul,
        "WindowMax" / Int32ul,
        "WindowLastMax" / Int32ul
    )


@declare(guid=guid("2bcfefe5-5026-536b-1686-b249cb49cae3"), event_id=1006, version=0)
class Microsoft_Windows_WinQuic_1006_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul
    )

