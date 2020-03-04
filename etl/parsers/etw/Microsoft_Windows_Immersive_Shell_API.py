# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Immersive-Shell-API
GUID : 5f0e257f-c224-43e5-9555-2adcb8540a58
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5f0e257f-c224-43e5-9555-2adcb8540a58"), event_id=2041, version=0)
class Microsoft_Windows_Immersive_Shell_API_2041_0(Etw):
    pattern = Struct(
        "QuiesceBool" / Int32ul
    )


@declare(guid=guid("5f0e257f-c224-43e5-9555-2adcb8540a58"), event_id=2042, version=0)
class Microsoft_Windows_Immersive_Shell_API_2042_0(Etw):
    pattern = Struct(
        "BlockUnblockBool" / Int32ul,
        "ThreadId" / Int32ul
    )


@declare(guid=guid("5f0e257f-c224-43e5-9555-2adcb8540a58"), event_id=2044, version=0)
class Microsoft_Windows_Immersive_Shell_API_2044_0(Etw):
    pattern = Struct(
        "ThreadId" / Int32ul
    )


@declare(guid=guid("5f0e257f-c224-43e5-9555-2adcb8540a58"), event_id=2045, version=0)
class Microsoft_Windows_Immersive_Shell_API_2045_0(Etw):
    pattern = Struct(
        "IsMainView" / Int32ul,
        "Pid" / Int32ul,
        "ThreadId" / Int32ul
    )


@declare(guid=guid("5f0e257f-c224-43e5-9555-2adcb8540a58"), event_id=2102, version=0)
class Microsoft_Windows_Immersive_Shell_API_2102_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("5f0e257f-c224-43e5-9555-2adcb8540a58"), event_id=2106, version=0)
class Microsoft_Windows_Immersive_Shell_API_2106_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("5f0e257f-c224-43e5-9555-2adcb8540a58"), event_id=6201, version=0)
class Microsoft_Windows_Immersive_Shell_API_6201_0(Etw):
    pattern = Struct(
        "AppID" / WString
    )


@declare(guid=guid("5f0e257f-c224-43e5-9555-2adcb8540a58"), event_id=6203, version=0)
class Microsoft_Windows_Immersive_Shell_API_6203_0(Etw):
    pattern = Struct(
        "HWND" / Int32ul,
        "AppID" / WString
    )

