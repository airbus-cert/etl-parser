# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-Audit-API-Calls
GUID : e02a841c-75a3-4fa7-afc8-ae09cf9b7f23
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e02a841c-75a3-4fa7-afc8-ae09cf9b7f23"), event_id=1, version=0)
class Microsoft_Windows_Kernel_Audit_API_Calls_1_0(Etw):
    pattern = Struct(
        "NotifyRoutineAddress" / Int64ul,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("e02a841c-75a3-4fa7-afc8-ae09cf9b7f23"), event_id=2, version=0)
class Microsoft_Windows_Kernel_Audit_API_Calls_2_0(Etw):
    pattern = Struct(
        "TargetProcessId" / Int32ul,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("e02a841c-75a3-4fa7-afc8-ae09cf9b7f23"), event_id=3, version=0)
class Microsoft_Windows_Kernel_Audit_API_Calls_3_0(Etw):
    pattern = Struct(
        "LinkSourceName" / WString,
        "LinkTargetName" / WString,
        "DesiredAccess" / Int32ul,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("e02a841c-75a3-4fa7-afc8-ae09cf9b7f23"), event_id=4, version=0)
class Microsoft_Windows_Kernel_Audit_API_Calls_4_0(Etw):
    pattern = Struct(
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("e02a841c-75a3-4fa7-afc8-ae09cf9b7f23"), event_id=5, version=0)
class Microsoft_Windows_Kernel_Audit_API_Calls_5_0(Etw):
    pattern = Struct(
        "TargetProcessId" / Int32ul,
        "DesiredAccess" / Int32ul,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("e02a841c-75a3-4fa7-afc8-ae09cf9b7f23"), event_id=6, version=0)
class Microsoft_Windows_Kernel_Audit_API_Calls_6_0(Etw):
    pattern = Struct(
        "TargetProcessId" / Int32ul,
        "TargetThreatId" / Int32ul,
        "DesiredAccess" / Int32ul,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("e02a841c-75a3-4fa7-afc8-ae09cf9b7f23"), event_id=7, version=0)
class Microsoft_Windows_Kernel_Audit_API_Calls_7_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("e02a841c-75a3-4fa7-afc8-ae09cf9b7f23"), event_id=8, version=0)
class Microsoft_Windows_Kernel_Audit_API_Calls_8_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "ReturnCode" / Int32ul
    )

