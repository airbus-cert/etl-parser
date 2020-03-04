# -*- coding: utf-8 -*-
"""
Microsoft-Windows-RTWorkQueue-Extended
GUID : 83faaa86-63c8-4dd8-a2da-fbadddfc0655
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("83faaa86-63c8-4dd8-a2da-fbadddfc0655"), event_id=1, version=0)
class Microsoft_Windows_RTWorkQueue_Extended_1_0(Etw):
    pattern = Struct(
        "AsyncResult" / Int64ul,
        "AsyncResultVTable" / Int64ul
    )


@declare(guid=guid("83faaa86-63c8-4dd8-a2da-fbadddfc0655"), event_id=2, version=0)
class Microsoft_Windows_RTWorkQueue_Extended_2_0(Etw):
    pattern = Struct(
        "WorkQueueID" / Int32ul,
        "RefCount" / Int32ul
    )


@declare(guid=guid("83faaa86-63c8-4dd8-a2da-fbadddfc0655"), event_id=3, version=0)
class Microsoft_Windows_RTWorkQueue_Extended_3_0(Etw):
    pattern = Struct(
        "Platform" / Int64ul,
        "WorkQueueID" / Int32ul,
        "WorkPrivateIndex" / Int32ul
    )


@declare(guid=guid("83faaa86-63c8-4dd8-a2da-fbadddfc0655"), event_id=4, version=0)
class Microsoft_Windows_RTWorkQueue_Extended_4_0(Etw):
    pattern = Struct(
        "Platform" / Int64ul,
        "Callback" / Int64ul,
        "WorkQueueID" / Int32ul
    )


@declare(guid=guid("83faaa86-63c8-4dd8-a2da-fbadddfc0655"), event_id=5, version=0)
class Microsoft_Windows_RTWorkQueue_Extended_5_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("83faaa86-63c8-4dd8-a2da-fbadddfc0655"), event_id=6, version=0)
class Microsoft_Windows_RTWorkQueue_Extended_6_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("83faaa86-63c8-4dd8-a2da-fbadddfc0655"), event_id=7, version=0)
class Microsoft_Windows_RTWorkQueue_Extended_7_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Count" / Int32sl
    )


@declare(guid=guid("83faaa86-63c8-4dd8-a2da-fbadddfc0655"), event_id=8, version=0)
class Microsoft_Windows_RTWorkQueue_Extended_8_0(Etw):
    pattern = Struct(
        "WorkQueueID" / Int32ul
    )


@declare(guid=guid("83faaa86-63c8-4dd8-a2da-fbadddfc0655"), event_id=9, version=0)
class Microsoft_Windows_RTWorkQueue_Extended_9_0(Etw):
    pattern = Struct(
        "WorkQueueID" / Int32ul
    )


@declare(guid=guid("83faaa86-63c8-4dd8-a2da-fbadddfc0655"), event_id=10, version=0)
class Microsoft_Windows_RTWorkQueue_Extended_10_0(Etw):
    pattern = Struct(
        "handle" / Int64ul,
        "Mode" / Int32ul
    )


@declare(guid=guid("83faaa86-63c8-4dd8-a2da-fbadddfc0655"), event_id=11, version=0)
class Microsoft_Windows_RTWorkQueue_Extended_11_0(Etw):
    pattern = Struct(
        "handle" / Int64ul,
        "Mode" / Int32ul
    )


@declare(guid=guid("83faaa86-63c8-4dd8-a2da-fbadddfc0655"), event_id=12, version=0)
class Microsoft_Windows_RTWorkQueue_Extended_12_0(Etw):
    pattern = Struct(
        "WorkQueueID" / Int32ul
    )


@declare(guid=guid("83faaa86-63c8-4dd8-a2da-fbadddfc0655"), event_id=13, version=0)
class Microsoft_Windows_RTWorkQueue_Extended_13_0(Etw):
    pattern = Struct(
        "WorkQueueID" / Int32ul
    )


@declare(guid=guid("83faaa86-63c8-4dd8-a2da-fbadddfc0655"), event_id=14, version=0)
class Microsoft_Windows_RTWorkQueue_Extended_14_0(Etw):
    pattern = Struct(
        "workqueue" / Int64ul,
        "WorkQueueID" / Int32ul,
        "Mode" / Int32ul
    )


@declare(guid=guid("83faaa86-63c8-4dd8-a2da-fbadddfc0655"), event_id=15, version=0)
class Microsoft_Windows_RTWorkQueue_Extended_15_0(Etw):
    pattern = Struct(
        "workqueue" / Int64ul,
        "WorkQueueID" / Int32ul,
        "Mode" / Int32ul
    )


@declare(guid=guid("83faaa86-63c8-4dd8-a2da-fbadddfc0655"), event_id=16, version=0)
class Microsoft_Windows_RTWorkQueue_Extended_16_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "OldMode" / Int32ul,
        "NewMode" / Int32ul
    )


@declare(guid=guid("83faaa86-63c8-4dd8-a2da-fbadddfc0655"), event_id=17, version=0)
class Microsoft_Windows_RTWorkQueue_Extended_17_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "Mode" / Int32ul,
        "Delta" / Int32ul
    )


@declare(guid=guid("83faaa86-63c8-4dd8-a2da-fbadddfc0655"), event_id=18, version=0)
class Microsoft_Windows_RTWorkQueue_Extended_18_0(Etw):
    pattern = Struct(
        "workqueue" / Int64ul,
        "WorkQueueID" / Int32ul,
        "Resolution" / Int32ul
    )


@declare(guid=guid("83faaa86-63c8-4dd8-a2da-fbadddfc0655"), event_id=19, version=0)
class Microsoft_Windows_RTWorkQueue_Extended_19_0(Etw):
    pattern = Struct(
        "workqueue" / Int64ul,
        "WorkQueueID" / Int32ul,
        "Resolution" / Int32ul
    )

