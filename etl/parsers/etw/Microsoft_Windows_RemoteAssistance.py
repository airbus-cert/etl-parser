# -*- coding: utf-8 -*-
"""
Microsoft-Windows-RemoteAssistance
GUID : 5b0a651a-8807-45cc-9656-7579815b6af0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=1, version=0)
class Microsoft_Windows_RemoteAssistance_1_0(Etw):
    pattern = Struct(
        "FuncName" / WString
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=2, version=0)
class Microsoft_Windows_RemoteAssistance_2_0(Etw):
    pattern = Struct(
        "FuncName" / WString
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=3, version=0)
class Microsoft_Windows_RemoteAssistance_3_0(Etw):
    pattern = Struct(
        "file" / WString,
        "line" / Int32ul,
        "function" / WString,
        "error" / Int32ul
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=4, version=0)
class Microsoft_Windows_RemoteAssistance_4_0(Etw):
    pattern = Struct(
        "file" / WString,
        "line" / Int32ul,
        "function" / WString,
        "error" / Int32ul
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=5, version=0)
class Microsoft_Windows_RemoteAssistance_5_0(Etw):
    pattern = Struct(
        "file" / WString,
        "line" / Int32ul,
        "Condition" / WString
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=6, version=0)
class Microsoft_Windows_RemoteAssistance_6_0(Etw):
    pattern = Struct(
        "file" / WString,
        "line" / Int32ul,
        "Condition" / Int32ul
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=7, version=0)
class Microsoft_Windows_RemoteAssistance_7_0(Etw):
    pattern = Struct(
        "line" / Int32ul,
        "File" / WString
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=8, version=0)
class Microsoft_Windows_RemoteAssistance_8_0(Etw):
    pattern = Struct(
        "line" / Int32ul,
        "File" / WString
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=9, version=0)
class Microsoft_Windows_RemoteAssistance_9_0(Etw):
    pattern = Struct(
        "FuncName" / WString
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=13, version=0)
class Microsoft_Windows_RemoteAssistance_13_0(Etw):
    pattern = Struct(
        "FuncName" / WString
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=17, version=1)
class Microsoft_Windows_RemoteAssistance_17_1(Etw):
    pattern = Struct(
        "FuncName" / WString
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=25, version=0)
class Microsoft_Windows_RemoteAssistance_25_0(Etw):
    pattern = Struct(
        "Code" / Int32ul
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=29, version=0)
class Microsoft_Windows_RemoteAssistance_29_0(Etw):
    pattern = Struct(
        "FuncName" / WString
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=33, version=0)
class Microsoft_Windows_RemoteAssistance_33_0(Etw):
    pattern = Struct(
        "FuncName" / WString
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=34, version=0)
class Microsoft_Windows_RemoteAssistance_34_0(Etw):
    pattern = Struct(
        "FuncName" / WString
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=35, version=0)
class Microsoft_Windows_RemoteAssistance_35_0(Etw):
    pattern = Struct(
        "FuncName" / WString
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=36, version=0)
class Microsoft_Windows_RemoteAssistance_36_0(Etw):
    pattern = Struct(
        "FuncName" / WString
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=37, version=0)
class Microsoft_Windows_RemoteAssistance_37_0(Etw):
    pattern = Struct(
        "FuncName" / WString
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=38, version=0)
class Microsoft_Windows_RemoteAssistance_38_0(Etw):
    pattern = Struct(
        "FuncName" / WString
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=39, version=0)
class Microsoft_Windows_RemoteAssistance_39_0(Etw):
    pattern = Struct(
        "FuncName" / WString
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=42, version=0)
class Microsoft_Windows_RemoteAssistance_42_0(Etw):
    pattern = Struct(
        "FuncName" / WString
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=43, version=0)
class Microsoft_Windows_RemoteAssistance_43_0(Etw):
    pattern = Struct(
        "Code" / Int32ul
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=44, version=0)
class Microsoft_Windows_RemoteAssistance_44_0(Etw):
    pattern = Struct(
        "FuncName" / WString
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=45, version=0)
class Microsoft_Windows_RemoteAssistance_45_0(Etw):
    pattern = Struct(
        "FuncName" / WString
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=46, version=0)
class Microsoft_Windows_RemoteAssistance_46_0(Etw):
    pattern = Struct(
        "FuncName" / WString
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=47, version=0)
class Microsoft_Windows_RemoteAssistance_47_0(Etw):
    pattern = Struct(
        "FuncName" / WString
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=100, version=0)
class Microsoft_Windows_RemoteAssistance_100_0(Etw):
    pattern = Struct(
        "Code" / Int32ul
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=101, version=0)
class Microsoft_Windows_RemoteAssistance_101_0(Etw):
    pattern = Struct(
        "Code" / Int32ul
    )


@declare(guid=guid("5b0a651a-8807-45cc-9656-7579815b6af0"), event_id=102, version=0)
class Microsoft_Windows_RemoteAssistance_102_0(Etw):
    pattern = Struct(
        "FuncName" / WString
    )

