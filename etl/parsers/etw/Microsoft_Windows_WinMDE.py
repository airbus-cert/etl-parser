# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WinMDE
GUID : 77549803-7bb1-418b-a98e-f2e22f35a873
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("77549803-7bb1-418b-a98e-f2e22f35a873"), event_id=1, version=0)
class Microsoft_Windows_WinMDE_1_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("77549803-7bb1-418b-a98e-f2e22f35a873"), event_id=2, version=0)
class Microsoft_Windows_WinMDE_2_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("77549803-7bb1-418b-a98e-f2e22f35a873"), event_id=3, version=0)
class Microsoft_Windows_WinMDE_3_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("77549803-7bb1-418b-a98e-f2e22f35a873"), event_id=4, version=0)
class Microsoft_Windows_WinMDE_4_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Value" / Int32ul
    )


@declare(guid=guid("77549803-7bb1-418b-a98e-f2e22f35a873"), event_id=5, version=0)
class Microsoft_Windows_WinMDE_5_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Value" / Int32ul
    )


@declare(guid=guid("77549803-7bb1-418b-a98e-f2e22f35a873"), event_id=6, version=0)
class Microsoft_Windows_WinMDE_6_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamIndex" / Int32ul,
        "WorkQueueID" / Int32ul
    )


@declare(guid=guid("77549803-7bb1-418b-a98e-f2e22f35a873"), event_id=7, version=0)
class Microsoft_Windows_WinMDE_7_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("77549803-7bb1-418b-a98e-f2e22f35a873"), event_id=8, version=0)
class Microsoft_Windows_WinMDE_8_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )

