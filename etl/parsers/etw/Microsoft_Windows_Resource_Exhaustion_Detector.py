# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Resource-Exhaustion-Detector
GUID : 9988748e-c2e8-4054-85f6-0c3e1cad2470
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9988748e-c2e8-4054-85f6-0c3e1cad2470"), event_id=1003, version=0)
class Microsoft_Windows_Resource_Exhaustion_Detector_1003_0(Etw):
    pattern = Struct(
        "SystemCommitLimit" / Int64ul,
        "SystemCommitCharge" / Int64ul
    )


@declare(guid=guid("9988748e-c2e8-4054-85f6-0c3e1cad2470"), event_id=1005, version=0)
class Microsoft_Windows_Resource_Exhaustion_Detector_1005_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("9988748e-c2e8-4054-85f6-0c3e1cad2470"), event_id=1006, version=0)
class Microsoft_Windows_Resource_Exhaustion_Detector_1006_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("9988748e-c2e8-4054-85f6-0c3e1cad2470"), event_id=1007, version=0)
class Microsoft_Windows_Resource_Exhaustion_Detector_1007_0(Etw):
    pattern = Struct(
        "RequestSize" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("9988748e-c2e8-4054-85f6-0c3e1cad2470"), event_id=1008, version=0)
class Microsoft_Windows_Resource_Exhaustion_Detector_1008_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("9988748e-c2e8-4054-85f6-0c3e1cad2470"), event_id=2004, version=0)
class Microsoft_Windows_Resource_Exhaustion_Detector_2004_0(Etw):
    pattern = Struct(
        "SystemCommitLimit" / Int64ul,
        "SystemCommitCharge" / Int64ul,
        "ProcessCommitCharge" / Int64ul,
        "PagedPoolUsage" / Int64ul,
        "PhysicalMemorySize" / Int64ul,
        "PhysicalMemoryUsage" / Int64ul,
        "NonPagedPoolUsage" / Int64ul,
        "TotalProcesses" / Int32ul,
        "PagedPoolTag_1" / WString,
        "PagedPoolUsed_1" / Int64ul,
        "PagedPoolTag_2" / WString,
        "PagedPoolUsed_2" / Int64ul,
        "PagedPoolTag_3" / WString,
        "PagedPoolUsed_3" / Int64ul,
        "NonPagedPoolTag_1" / WString,
        "NonPagedPoolUsed_1" / Int64ul,
        "NonPagedPoolTag_2" / WString,
        "NonPagedPoolUsed_2" / Int64ul,
        "NonPagedPoolTag_3" / WString,
        "NonPagedPoolUsed_3" / Int64ul,
        "Process_1_Name" / WString,
        "Process_1_ID" / Int32ul,
        "Process_1_CreationTime" / Int64ul,
        "Process_1_CommitCharge" / Int64ul,
        "Process_1_HandleCount" / Int32ul,
        "Process_1_Version" / WString,
        "Process_1_TypeInfo" / Int32ul,
        "Process_2_Name" / WString,
        "Process_2_ID" / Int32ul,
        "Process_2_CreationTime" / Int64ul,
        "Process_2_CommitCharge" / Int64ul,
        "Process_2_HandleCount" / Int32ul,
        "Process_2_Version" / WString,
        "Process_2_TypeInfo" / Int32ul,
        "Process_3_Name" / WString,
        "Process_3_ID" / Int32ul,
        "Process_3_CreationTime" / Int64ul,
        "Process_3_CommitCharge" / Int64ul,
        "Process_3_HandleCount" / Int32ul,
        "Process_3_Version" / WString,
        "Process_3_TypeInfo" / Int32ul,
        "Process_4_Name" / WString,
        "Process_4_ID" / Int32ul,
        "Process_4_CreationTime" / Int64ul,
        "Process_4_CommitCharge" / Int64ul,
        "Process_4_HandleCount" / Int32ul,
        "Process_4_Version" / WString,
        "Process_4_TypeInfo" / Int32ul,
        "Process_5_Name" / WString,
        "Process_5_ID" / Int32ul,
        "Process_5_CreationTime" / Int64ul,
        "Process_5_CommitCharge" / Int64ul,
        "Process_5_HandleCount" / Int32ul,
        "Process_5_Version" / WString,
        "Process_5_TypeInfo" / Int32ul,
        "Process_6_Name" / WString,
        "Process_6_ID" / Int32ul,
        "Process_6_CreationTime" / Int64ul,
        "Process_6_CommitCharge" / Int64ul,
        "Process_6_HandleCount" / Int32ul,
        "Process_6_Version" / WString,
        "Process_6_TypeInfo" / Int32ul,
        "EventGenerationTime" / Int64ul
    )

