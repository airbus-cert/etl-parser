# -*- coding: utf-8 -*-
"""
Intel-Thunderbolt-Service
GUID : 8c2ec332-c0e1-4a25-b152-8e869fc649d7
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("8c2ec332-c0e1-4a25-b152-8e869fc649d7"), event_id=1, version=1)
class Intel_Thunderbolt_Service_1_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "File" / WString,
        "Function" / WString,
        "Line" / Int32ul
    )


@declare(guid=guid("8c2ec332-c0e1-4a25-b152-8e869fc649d7"), event_id=2, version=1)
class Intel_Thunderbolt_Service_2_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "File" / WString,
        "Function" / WString,
        "Line" / Int32ul
    )


@declare(guid=guid("8c2ec332-c0e1-4a25-b152-8e869fc649d7"), event_id=3, version=1)
class Intel_Thunderbolt_Service_3_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "File" / WString,
        "Function" / WString,
        "Line" / Int32ul
    )


@declare(guid=guid("8c2ec332-c0e1-4a25-b152-8e869fc649d7"), event_id=4, version=1)
class Intel_Thunderbolt_Service_4_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "File" / WString,
        "Function" / WString,
        "Line" / Int32ul
    )


@declare(guid=guid("8c2ec332-c0e1-4a25-b152-8e869fc649d7"), event_id=5, version=1)
class Intel_Thunderbolt_Service_5_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "File" / WString,
        "Function" / WString,
        "Line" / Int32ul
    )


@declare(guid=guid("8c2ec332-c0e1-4a25-b152-8e869fc649d7"), event_id=6, version=1)
class Intel_Thunderbolt_Service_6_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "File" / WString,
        "Function" / WString,
        "Line" / Int32ul
    )

