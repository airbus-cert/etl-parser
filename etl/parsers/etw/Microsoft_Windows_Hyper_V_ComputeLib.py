# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Hyper-V-ComputeLib
GUID : af7fd3a7-b248-460c-a9f5-fec39ef8468c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("af7fd3a7-b248-460c-a9f5-fec39ef8468c"), event_id=100, version=0)
class Microsoft_Windows_Hyper_V_ComputeLib_100_0(Etw):
    pattern = Struct(
        "TraceData" / WString,
        "VmName" / WString,
        "VmId" / WString,
        "StackFrameCount" / Int32ul,
        "StackFrame" / Int64ul,
        "ModuleCount" / Int32ul,
        "Module" / Int32sl
    )


@declare(guid=guid("af7fd3a7-b248-460c-a9f5-fec39ef8468c"), event_id=101, version=0)
class Microsoft_Windows_Hyper_V_ComputeLib_101_0(Etw):
    pattern = Struct(
        "TraceData" / WString,
        "VmName" / WString,
        "VmId" / WString,
        "StackFrameCount" / Int32ul,
        "StackFrame" / Int64ul,
        "ModuleCount" / Int32ul,
        "Module" / Int32sl
    )


@declare(guid=guid("af7fd3a7-b248-460c-a9f5-fec39ef8468c"), event_id=102, version=0)
class Microsoft_Windows_Hyper_V_ComputeLib_102_0(Etw):
    pattern = Struct(
        "TraceData" / WString,
        "VmName" / WString,
        "VmId" / WString,
        "StackFrameCount" / Int32ul,
        "StackFrame" / Int64ul,
        "ModuleCount" / Int32ul,
        "Module" / Int32sl
    )


@declare(guid=guid("af7fd3a7-b248-460c-a9f5-fec39ef8468c"), event_id=103, version=0)
class Microsoft_Windows_Hyper_V_ComputeLib_103_0(Etw):
    pattern = Struct(
        "TraceData" / WString,
        "VmName" / WString,
        "VmId" / WString,
        "StackFrameCount" / Int32ul,
        "StackFrame" / Int64ul,
        "ModuleCount" / Int32ul,
        "Module" / Int32sl
    )


@declare(guid=guid("af7fd3a7-b248-460c-a9f5-fec39ef8468c"), event_id=1000, version=0)
class Microsoft_Windows_Hyper_V_ComputeLib_1000_0(Etw):
    pattern = Struct(
        "Id" / WString,
        "ErrorMessage" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("af7fd3a7-b248-460c-a9f5-fec39ef8468c"), event_id=1001, version=0)
class Microsoft_Windows_Hyper_V_ComputeLib_1001_0(Etw):
    pattern = Struct(
        "Id" / WString,
        "ErrorMessage" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("af7fd3a7-b248-460c-a9f5-fec39ef8468c"), event_id=1002, version=0)
class Microsoft_Windows_Hyper_V_ComputeLib_1002_0(Etw):
    pattern = Struct(
        "Id" / WString,
        "ErrorMessage" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("af7fd3a7-b248-460c-a9f5-fec39ef8468c"), event_id=1003, version=0)
class Microsoft_Windows_Hyper_V_ComputeLib_1003_0(Etw):
    pattern = Struct(
        "Id" / WString,
        "ErrorMessage" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("af7fd3a7-b248-460c-a9f5-fec39ef8468c"), event_id=1004, version=0)
class Microsoft_Windows_Hyper_V_ComputeLib_1004_0(Etw):
    pattern = Struct(
        "Id" / WString,
        "ErrorMessage" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("af7fd3a7-b248-460c-a9f5-fec39ef8468c"), event_id=1005, version=0)
class Microsoft_Windows_Hyper_V_ComputeLib_1005_0(Etw):
    pattern = Struct(
        "Id" / WString,
        "ErrorMessage" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("af7fd3a7-b248-460c-a9f5-fec39ef8468c"), event_id=1006, version=0)
class Microsoft_Windows_Hyper_V_ComputeLib_1006_0(Etw):
    pattern = Struct(
        "Id" / WString,
        "ErrorMessage" / WString,
        "ErrorCode" / WString
    )

