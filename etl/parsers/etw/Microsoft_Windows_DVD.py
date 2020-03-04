# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DVD
GUID : e18d0fca-9515-4232-98e4-89e456d8551b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e18d0fca-9515-4232-98e4-89e456d8551b"), event_id=1, version=0)
class Microsoft_Windows_DVD_1_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamID" / Int32sl,
        "StreamType" / Int32sl,
        "IsRunning" / Int32sl,
        "rtTimestamp" / Int64sl,
        "rtNow" / Int64sl,
        "rtAhead" / Int64sl,
        "SyncPoint" / Int32sl,
        "TimeDisc" / Int32sl,
        "Length" / Int32sl
    )


@declare(guid=guid("e18d0fca-9515-4232-98e4-89e456d8551b"), event_id=2, version=0)
class Microsoft_Windows_DVD_2_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("e18d0fca-9515-4232-98e4-89e456d8551b"), event_id=3, version=0)
class Microsoft_Windows_DVD_3_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("e18d0fca-9515-4232-98e4-89e456d8551b"), event_id=5, version=0)
class Microsoft_Windows_DVD_5_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Duration" / Int32sl
    )


@declare(guid=guid("e18d0fca-9515-4232-98e4-89e456d8551b"), event_id=6, version=0)
class Microsoft_Windows_DVD_6_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Duration" / Int32sl
    )


@declare(guid=guid("e18d0fca-9515-4232-98e4-89e456d8551b"), event_id=7, version=0)
class Microsoft_Windows_DVD_7_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HaveRun" / Int32sl,
        "IsRunning" / Int32sl,
        "UsedGetTime" / Int32sl,
        "SetTimeToNow" / Int32sl,
        "CellTimeDisc" / Int32sl,
        "rtNow" / Int64sl,
        "rtTime0" / Int64sl,
        "rtNow_Time0" / Int64sl,
        "VOBULen" / Int64sl
    )


@declare(guid=guid("e18d0fca-9515-4232-98e4-89e456d8551b"), event_id=8, version=0)
class Microsoft_Windows_DVD_8_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Duration" / Int32sl,
        "MaxLatency" / Int32sl
    )


@declare(guid=guid("e18d0fca-9515-4232-98e4-89e456d8551b"), event_id=9, version=0)
class Microsoft_Windows_DVD_9_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("e18d0fca-9515-4232-98e4-89e456d8551b"), event_id=10, version=0)
class Microsoft_Windows_DVD_10_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HandleMask" / Int32sl
    )


@declare(guid=guid("e18d0fca-9515-4232-98e4-89e456d8551b"), event_id=11, version=0)
class Microsoft_Windows_DVD_11_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "WakeIndex" / Int32sl,
        "LastError" / Int32sl,
        "IOIndex" / Int32sl,
        "ExtraEventInfo" / Int32sl
    )


@declare(guid=guid("e18d0fca-9515-4232-98e4-89e456d8551b"), event_id=12, version=0)
class Microsoft_Windows_DVD_12_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Type" / Int32sl,
        "Param1" / Int32sl,
        "Param2" / Int32sl
    )


@declare(guid=guid("e18d0fca-9515-4232-98e4-89e456d8551b"), event_id=13, version=0)
class Microsoft_Windows_DVD_13_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Domain" / Int32sl,
        "VTSN" / Int32sl
    )


@declare(guid=guid("e18d0fca-9515-4232-98e4-89e456d8551b"), event_id=14, version=0)
class Microsoft_Windows_DVD_14_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Param1" / Int32sl,
        "Param2" / Int32sl
    )


@declare(guid=guid("e18d0fca-9515-4232-98e4-89e456d8551b"), event_id=15, version=0)
class Microsoft_Windows_DVD_15_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("e18d0fca-9515-4232-98e4-89e456d8551b"), event_id=16, version=0)
class Microsoft_Windows_DVD_16_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("e18d0fca-9515-4232-98e4-89e456d8551b"), event_id=17, version=0)
class Microsoft_Windows_DVD_17_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Filename" / WString
    )


@declare(guid=guid("e18d0fca-9515-4232-98e4-89e456d8551b"), event_id=18, version=0)
class Microsoft_Windows_DVD_18_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "hr" / Int32sl
    )


@declare(guid=guid("e18d0fca-9515-4232-98e4-89e456d8551b"), event_id=19, version=0)
class Microsoft_Windows_DVD_19_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("e18d0fca-9515-4232-98e4-89e456d8551b"), event_id=20, version=0)
class Microsoft_Windows_DVD_20_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )

