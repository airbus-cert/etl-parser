# -*- coding: utf-8 -*-
"""
Microsoft-User Experience Virtualization-Agent Driver
GUID : de29cf61-5ee6-43ff-9aac-959c4e13cc6c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("de29cf61-5ee6-43ff-9aac-959c4e13cc6c"), event_id=0, version=0)
class Microsoft_User_Experience_Virtualization_Agent_Driver_0_0(Etw):
    pattern = Struct(
        "P1AnsiString" / CString
    )


@declare(guid=guid("de29cf61-5ee6-43ff-9aac-959c4e13cc6c"), event_id=1, version=0)
class Microsoft_User_Experience_Virtualization_Agent_Driver_1_0(Etw):
    pattern = Struct(
        "P1AnsiString" / CString
    )


@declare(guid=guid("de29cf61-5ee6-43ff-9aac-959c4e13cc6c"), event_id=2, version=0)
class Microsoft_User_Experience_Virtualization_Agent_Driver_2_0(Etw):
    pattern = Struct(
        "P1AnsiString" / CString
    )


@declare(guid=guid("de29cf61-5ee6-43ff-9aac-959c4e13cc6c"), event_id=3, version=0)
class Microsoft_User_Experience_Virtualization_Agent_Driver_3_0(Etw):
    pattern = Struct(
        "P1AnsiString" / CString
    )


@declare(guid=guid("de29cf61-5ee6-43ff-9aac-959c4e13cc6c"), event_id=4, version=0)
class Microsoft_User_Experience_Virtualization_Agent_Driver_4_0(Etw):
    pattern = Struct(
        "P1AnsiString" / CString
    )


@declare(guid=guid("de29cf61-5ee6-43ff-9aac-959c4e13cc6c"), event_id=5, version=0)
class Microsoft_User_Experience_Virtualization_Agent_Driver_5_0(Etw):
    pattern = Struct(
        "P1AnsiString" / CString
    )


@declare(guid=guid("de29cf61-5ee6-43ff-9aac-959c4e13cc6c"), event_id=102, version=0)
class Microsoft_User_Experience_Virtualization_Agent_Driver_102_0(Etw):
    pattern = Struct(
        "P1String" / WString,
        "P2Ulong" / Int64ul
    )


@declare(guid=guid("de29cf61-5ee6-43ff-9aac-959c4e13cc6c"), event_id=103, version=0)
class Microsoft_User_Experience_Virtualization_Agent_Driver_103_0(Etw):
    pattern = Struct(
        "P1String" / WString,
        "P2ErrorCode" / Int32ul
    )


@declare(guid=guid("de29cf61-5ee6-43ff-9aac-959c4e13cc6c"), event_id=104, version=0)
class Microsoft_User_Experience_Virtualization_Agent_Driver_104_0(Etw):
    pattern = Struct(
        "P1String" / WString,
        "P2ErrorCode" / Int32ul
    )


@declare(guid=guid("de29cf61-5ee6-43ff-9aac-959c4e13cc6c"), event_id=105, version=0)
class Microsoft_User_Experience_Virtualization_Agent_Driver_105_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("de29cf61-5ee6-43ff-9aac-959c4e13cc6c"), event_id=106, version=0)
class Microsoft_User_Experience_Virtualization_Agent_Driver_106_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("de29cf61-5ee6-43ff-9aac-959c4e13cc6c"), event_id=107, version=0)
class Microsoft_User_Experience_Virtualization_Agent_Driver_107_0(Etw):
    pattern = Struct(
        "P1String" / WString,
        "P2ErrorCode" / Int32ul
    )


@declare(guid=guid("de29cf61-5ee6-43ff-9aac-959c4e13cc6c"), event_id=108, version=0)
class Microsoft_User_Experience_Virtualization_Agent_Driver_108_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("de29cf61-5ee6-43ff-9aac-959c4e13cc6c"), event_id=109, version=0)
class Microsoft_User_Experience_Virtualization_Agent_Driver_109_0(Etw):
    pattern = Struct(
        "P1Length" / Int16ul,
        "P2UnicodeBuffer" / Bytes(lambda this: this.P1Length),
        "P3ProcessId" / Int32ul
    )

