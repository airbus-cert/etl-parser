# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DotNETRuntime
GUID : e13c0d23-ccbc-4e12-931b-d9cc2eee27e4
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=1, version=0)
class Microsoft_Windows_DotNETRuntime_1_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=1, version=1)
class Microsoft_Windows_DotNETRuntime_1_1(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "Depth" / Int32ul,
        "Reason" / Int32ul,
        "Type" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=1, version=2)
class Microsoft_Windows_DotNETRuntime_1_2(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "Depth" / Int32ul,
        "Reason" / Int32ul,
        "Type" / Int32ul,
        "ClrInstanceID" / Int16ul,
        "ClientSequenceNumber" / Int64ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=2, version=0)
class Microsoft_Windows_DotNETRuntime_2_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "Depth" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=2, version=1)
class Microsoft_Windows_DotNETRuntime_2_1(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "Depth" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=3, version=1)
class Microsoft_Windows_DotNETRuntime_3_1(Etw):
    pattern = Struct(
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=4, version=0)
class Microsoft_Windows_DotNETRuntime_4_0(Etw):
    pattern = Struct(
        "GenerationSize0" / Int64ul,
        "TotalPromotedSize0" / Int64ul,
        "GenerationSize1" / Int64ul,
        "TotalPromotedSize1" / Int64ul,
        "GenerationSize2" / Int64ul,
        "TotalPromotedSize2" / Int64ul,
        "GenerationSize3" / Int64ul,
        "TotalPromotedSize3" / Int64ul,
        "FinalizationPromotedSize" / Int64ul,
        "FinalizationPromotedCount" / Int64ul,
        "PinnedObjectCount" / Int32ul,
        "SinkBlockCount" / Int32ul,
        "GCHandleCount" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=4, version=1)
class Microsoft_Windows_DotNETRuntime_4_1(Etw):
    pattern = Struct(
        "GenerationSize0" / Int64ul,
        "TotalPromotedSize0" / Int64ul,
        "GenerationSize1" / Int64ul,
        "TotalPromotedSize1" / Int64ul,
        "GenerationSize2" / Int64ul,
        "TotalPromotedSize2" / Int64ul,
        "GenerationSize3" / Int64ul,
        "TotalPromotedSize3" / Int64ul,
        "FinalizationPromotedSize" / Int64ul,
        "FinalizationPromotedCount" / Int64ul,
        "PinnedObjectCount" / Int32ul,
        "SinkBlockCount" / Int32ul,
        "GCHandleCount" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=5, version=0)
class Microsoft_Windows_DotNETRuntime_5_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "Size" / Int64ul,
        "Type" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=5, version=1)
class Microsoft_Windows_DotNETRuntime_5_1(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "Size" / Int64ul,
        "Type" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=6, version=0)
class Microsoft_Windows_DotNETRuntime_6_0(Etw):
    pattern = Struct(
        "Address" / Int64ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=6, version=1)
class Microsoft_Windows_DotNETRuntime_6_1(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=7, version=1)
class Microsoft_Windows_DotNETRuntime_7_1(Etw):
    pattern = Struct(
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=8, version=1)
class Microsoft_Windows_DotNETRuntime_8_1(Etw):
    pattern = Struct(
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=9, version=0)
class Microsoft_Windows_DotNETRuntime_9_0(Etw):
    pattern = Struct(
        "Reason" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=9, version=1)
class Microsoft_Windows_DotNETRuntime_9_1(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Count" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=10, version=0)
class Microsoft_Windows_DotNETRuntime_10_0(Etw):
    pattern = Struct(
        "AllocationAmount" / Int32ul,
        "AllocationKind" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=10, version=1)
class Microsoft_Windows_DotNETRuntime_10_1(Etw):
    pattern = Struct(
        "AllocationAmount" / Int32ul,
        "AllocationKind" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=10, version=2)
class Microsoft_Windows_DotNETRuntime_10_2(Etw):
    pattern = Struct(
        "AllocationAmount" / Int32ul,
        "AllocationKind" / Int32ul,
        "ClrInstanceID" / Int16ul,
        "AllocationAmount64" / Int64ul,
        "TypeID" / Int64ul,
        "TypeName" / WString,
        "HeapIndex" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=10, version=3)
class Microsoft_Windows_DotNETRuntime_10_3(Etw):
    pattern = Struct(
        "AllocationAmount" / Int32ul,
        "AllocationKind" / Int32ul,
        "ClrInstanceID" / Int16ul,
        "AllocationAmount64" / Int64ul,
        "TypeID" / Int64ul,
        "TypeName" / WString,
        "HeapIndex" / Int32ul,
        "Address" / Int64ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=11, version=1)
class Microsoft_Windows_DotNETRuntime_11_1(Etw):
    pattern = Struct(
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=12, version=1)
class Microsoft_Windows_DotNETRuntime_12_1(Etw):
    pattern = Struct(
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=13, version=0)
class Microsoft_Windows_DotNETRuntime_13_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=13, version=1)
class Microsoft_Windows_DotNETRuntime_13_1(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=14, version=1)
class Microsoft_Windows_DotNETRuntime_14_1(Etw):
    pattern = Struct(
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=15, version=0)
class Microsoft_Windows_DotNETRuntime_15_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "ClrInstanceID" / Int16ul,
        "Values" / Int8sl
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=16, version=0)
class Microsoft_Windows_DotNETRuntime_16_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Count" / Int32ul,
        "ClrInstanceID" / Int16ul,
        "Values" / Int8ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=17, version=0)
class Microsoft_Windows_DotNETRuntime_17_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Count" / Int32ul,
        "ClrInstanceID" / Int16ul,
        "Values" / Int8ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=18, version=0)
class Microsoft_Windows_DotNETRuntime_18_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Count" / Int32ul,
        "ClrInstanceID" / Int16ul,
        "Values" / Int8ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=19, version=0)
class Microsoft_Windows_DotNETRuntime_19_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Count" / Int32ul,
        "ClrInstanceID" / Int16ul,
        "Values" / Int8ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=20, version=0)
class Microsoft_Windows_DotNETRuntime_20_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "TypeID" / Int64ul,
        "ObjectCountForTypeSample" / Int32ul,
        "TotalSizeForTypeSample" / Int64ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=21, version=0)
class Microsoft_Windows_DotNETRuntime_21_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Count" / Int32ul,
        "ClrInstanceID" / Int16ul,
        "Values" / Int8ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=22, version=0)
class Microsoft_Windows_DotNETRuntime_22_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Count" / Int32ul,
        "ClrInstanceID" / Int16ul,
        "Values" / Int8ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=23, version=0)
class Microsoft_Windows_DotNETRuntime_23_0(Etw):
    pattern = Struct(
        "Generation" / Int8ul,
        "RangeStart" / Int64ul,
        "RangeUsedLength" / Int64ul,
        "RangeReservedLength" / Int64ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=25, version=0)
class Microsoft_Windows_DotNETRuntime_25_0(Etw):
    pattern = Struct(
        "HeapNum" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=26, version=0)
class Microsoft_Windows_DotNETRuntime_26_0(Etw):
    pattern = Struct(
        "HeapNum" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=27, version=0)
class Microsoft_Windows_DotNETRuntime_27_0(Etw):
    pattern = Struct(
        "HeapNum" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=28, version=0)
class Microsoft_Windows_DotNETRuntime_28_0(Etw):
    pattern = Struct(
        "HeapNum" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=29, version=0)
class Microsoft_Windows_DotNETRuntime_29_0(Etw):
    pattern = Struct(
        "TypeID" / Int64ul,
        "ObjectID" / Int64ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=30, version=0)
class Microsoft_Windows_DotNETRuntime_30_0(Etw):
    pattern = Struct(
        "HandleID" / Int64ul,
        "ObjectID" / Int64ul,
        "Kind" / Int32ul,
        "Generation" / Int32ul,
        "AppDomainID" / Int64ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=31, version=0)
class Microsoft_Windows_DotNETRuntime_31_0(Etw):
    pattern = Struct(
        "HandleID" / Int64ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=32, version=0)
class Microsoft_Windows_DotNETRuntime_32_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "TypeID" / Int64ul,
        "ObjectCountForTypeSample" / Int32ul,
        "TotalSizeForTypeSample" / Int64ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=33, version=0)
class Microsoft_Windows_DotNETRuntime_33_0(Etw):
    pattern = Struct(
        "HandleID" / Int64ul,
        "ObjectID" / Int64ul,
        "ObjectSize" / Int64ul,
        "TypeName" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=35, version=0)
class Microsoft_Windows_DotNETRuntime_35_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=36, version=0)
class Microsoft_Windows_DotNETRuntime_36_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "ClrInstanceID" / Int16ul,
        "Values" / Int8sl
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=37, version=0)
class Microsoft_Windows_DotNETRuntime_37_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "ClrInstanceID" / Int16ul,
        "Values" / Int8sl
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=38, version=0)
class Microsoft_Windows_DotNETRuntime_38_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "AppDomainID" / Int64ul,
        "ClrInstanceID" / Int16ul,
        "Values" / Int8ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=39, version=0)
class Microsoft_Windows_DotNETRuntime_39_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "DataSize" / Int32ul,
        "Data" / Bytes(lambda this: this.DataSize),
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=40, version=0)
class Microsoft_Windows_DotNETRuntime_40_0(Etw):
    pattern = Struct(
        "WorkerThreadCount" / Int32ul,
        "RetiredWorkerThreads" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=41, version=0)
class Microsoft_Windows_DotNETRuntime_41_0(Etw):
    pattern = Struct(
        "WorkerThreadCount" / Int32ul,
        "RetiredWorkerThreads" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=42, version=0)
class Microsoft_Windows_DotNETRuntime_42_0(Etw):
    pattern = Struct(
        "WorkerThreadCount" / Int32ul,
        "RetiredWorkerThreads" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=43, version=0)
class Microsoft_Windows_DotNETRuntime_43_0(Etw):
    pattern = Struct(
        "WorkerThreadCount" / Int32ul,
        "RetiredWorkerThreads" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=44, version=0)
class Microsoft_Windows_DotNETRuntime_44_0(Etw):
    pattern = Struct(
        "IOThreadCount" / Int32ul,
        "RetiredIOThreads" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=44, version=1)
class Microsoft_Windows_DotNETRuntime_44_1(Etw):
    pattern = Struct(
        "IOThreadCount" / Int32ul,
        "RetiredIOThreads" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=45, version=0)
class Microsoft_Windows_DotNETRuntime_45_0(Etw):
    pattern = Struct(
        "IOThreadCount" / Int32ul,
        "RetiredIOThreads" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=45, version=1)
class Microsoft_Windows_DotNETRuntime_45_1(Etw):
    pattern = Struct(
        "IOThreadCount" / Int32ul,
        "RetiredIOThreads" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=46, version=0)
class Microsoft_Windows_DotNETRuntime_46_0(Etw):
    pattern = Struct(
        "IOThreadCount" / Int32ul,
        "RetiredIOThreads" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=46, version=1)
class Microsoft_Windows_DotNETRuntime_46_1(Etw):
    pattern = Struct(
        "IOThreadCount" / Int32ul,
        "RetiredIOThreads" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=47, version=0)
class Microsoft_Windows_DotNETRuntime_47_0(Etw):
    pattern = Struct(
        "IOThreadCount" / Int32ul,
        "RetiredIOThreads" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=47, version=1)
class Microsoft_Windows_DotNETRuntime_47_1(Etw):
    pattern = Struct(
        "IOThreadCount" / Int32ul,
        "RetiredIOThreads" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=48, version=0)
class Microsoft_Windows_DotNETRuntime_48_0(Etw):
    pattern = Struct(
        "ClrThreadID" / Int32ul,
        "CpuUtilization" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=49, version=0)
class Microsoft_Windows_DotNETRuntime_49_0(Etw):
    pattern = Struct(
        "ClrThreadID" / Int32ul,
        "CpuUtilization" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=50, version=0)
class Microsoft_Windows_DotNETRuntime_50_0(Etw):
    pattern = Struct(
        "ActiveWorkerThreadCount" / Int32ul,
        "RetiredWorkerThreadCount" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=51, version=0)
class Microsoft_Windows_DotNETRuntime_51_0(Etw):
    pattern = Struct(
        "ActiveWorkerThreadCount" / Int32ul,
        "RetiredWorkerThreadCount" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=52, version=0)
class Microsoft_Windows_DotNETRuntime_52_0(Etw):
    pattern = Struct(
        "ActiveWorkerThreadCount" / Int32ul,
        "RetiredWorkerThreadCount" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=53, version=0)
class Microsoft_Windows_DotNETRuntime_53_0(Etw):
    pattern = Struct(
        "ActiveWorkerThreadCount" / Int32ul,
        "RetiredWorkerThreadCount" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=54, version=0)
class Microsoft_Windows_DotNETRuntime_54_0(Etw):
    pattern = Struct(
        "Throughput" / Double,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=55, version=0)
class Microsoft_Windows_DotNETRuntime_55_0(Etw):
    pattern = Struct(
        "AverageThroughput" / Double,
        "NewWorkerThreadCount" / Int32ul,
        "Reason" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=56, version=0)
class Microsoft_Windows_DotNETRuntime_56_0(Etw):
    pattern = Struct(
        "Duration" / Double,
        "Throughput" / Double,
        "ThreadWave" / Double,
        "ThroughputWave" / Double,
        "ThroughputErrorEstimate" / Double,
        "AverageThroughputErrorEstimate" / Double,
        "ThroughputRatio" / Double,
        "Confidence" / Double,
        "NewControlSetting" / Double,
        "NewThreadWaveMagnitude" / Int16ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=57, version=0)
class Microsoft_Windows_DotNETRuntime_57_0(Etw):
    pattern = Struct(
        "ActiveWorkerThreadCount" / Int32ul,
        "RetiredWorkerThreadCount" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=60, version=0)
class Microsoft_Windows_DotNETRuntime_60_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=61, version=0)
class Microsoft_Windows_DotNETRuntime_61_0(Etw):
    pattern = Struct(
        "WorkID" / Int64ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=62, version=0)
class Microsoft_Windows_DotNETRuntime_62_0(Etw):
    pattern = Struct(
        "WorkID" / Int64ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=63, version=0)
class Microsoft_Windows_DotNETRuntime_63_0(Etw):
    pattern = Struct(
        "NativeOverlapped" / Int64ul,
        "Overlapped" / Int64ul,
        "MultiDequeues" / Int8ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=64, version=0)
class Microsoft_Windows_DotNETRuntime_64_0(Etw):
    pattern = Struct(
        "NativeOverlapped" / Int64ul,
        "Overlapped" / Int64ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=65, version=0)
class Microsoft_Windows_DotNETRuntime_65_0(Etw):
    pattern = Struct(
        "NativeOverlapped" / Int64ul,
        "Overlapped" / Int64ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=70, version=0)
class Microsoft_Windows_DotNETRuntime_70_0(Etw):
    pattern = Struct(
        "ID" / Int64ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=71, version=0)
class Microsoft_Windows_DotNETRuntime_71_0(Etw):
    pattern = Struct(
        "ID" / Int64ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=80, version=1)
class Microsoft_Windows_DotNETRuntime_80_1(Etw):
    pattern = Struct(
        "ExceptionType" / WString,
        "ExceptionMessage" / WString,
        "ExceptionEIP" / Int64ul,
        "ExceptionHRESULT" / Int32ul,
        "ExceptionFlags" / Int16ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=81, version=1)
class Microsoft_Windows_DotNETRuntime_81_1(Etw):
    pattern = Struct(
        "ContentionFlags" / Int8ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=82, version=0)
class Microsoft_Windows_DotNETRuntime_82_0(Etw):
    pattern = Struct(
        "ClrInstanceID" / Int16ul,
        "Reserved1" / Int8ul,
        "Reserved2" / Int8ul,
        "FrameCount" / Int32ul,
        "Stack" / Int64ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=83, version=0)
class Microsoft_Windows_DotNETRuntime_83_0(Etw):
    pattern = Struct(
        "AppDomainID" / Int64ul,
        "Allocated" / Int64ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=84, version=0)
class Microsoft_Windows_DotNETRuntime_84_0(Etw):
    pattern = Struct(
        "AppDomainID" / Int64ul,
        "Survived" / Int64ul,
        "ProcessSurvived" / Int64ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=85, version=0)
class Microsoft_Windows_DotNETRuntime_85_0(Etw):
    pattern = Struct(
        "ManagedThreadID" / Int64ul,
        "AppDomainID" / Int64ul,
        "Flags" / Int32ul,
        "ManagedThreadIndex" / Int32ul,
        "OSThreadID" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=86, version=0)
class Microsoft_Windows_DotNETRuntime_86_0(Etw):
    pattern = Struct(
        "ManagedThreadID" / Int64ul,
        "AppDomainID" / Int64ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=87, version=0)
class Microsoft_Windows_DotNETRuntime_87_0(Etw):
    pattern = Struct(
        "ManagedThreadID" / Int64ul,
        "AppDomainID" / Int64ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=88, version=0)
class Microsoft_Windows_DotNETRuntime_88_0(Etw):
    pattern = Struct(
        "ClrInstanceID" / Int16ul,
        "ModuleID" / Int64ul,
        "StubMethodID" / Int64ul,
        "StubFlags" / Int32ul,
        "ManagedInteropMethodToken" / Int32ul,
        "ManagedInteropMethodNamespace" / WString,
        "ManagedInteropMethodName" / WString,
        "ManagedInteropMethodSignature" / WString,
        "NativeMethodSignature" / WString,
        "StubMethodSignature" / WString,
        "StubMethodILCode" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=89, version=0)
class Microsoft_Windows_DotNETRuntime_89_0(Etw):
    pattern = Struct(
        "ClrInstanceID" / Int16ul,
        "ModuleID" / Int64ul,
        "StubMethodID" / Int64ul,
        "ManagedInteropMethodToken" / Int32ul,
        "ManagedInteropMethodNamespace" / WString,
        "ManagedInteropMethodName" / WString,
        "ManagedInteropMethodSignature" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=91, version=0)
class Microsoft_Windows_DotNETRuntime_91_0(Etw):
    pattern = Struct(
        "ContentionFlags" / Int8ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=137, version=0)
class Microsoft_Windows_DotNETRuntime_137_0(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=138, version=0)
class Microsoft_Windows_DotNETRuntime_138_0(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=139, version=0)
class Microsoft_Windows_DotNETRuntime_139_0(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "MethodNamespace" / WString,
        "MethodName" / WString,
        "MethodSignature" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=140, version=0)
class Microsoft_Windows_DotNETRuntime_140_0(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "MethodNamespace" / WString,
        "MethodName" / WString,
        "MethodSignature" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=141, version=0)
class Microsoft_Windows_DotNETRuntime_141_0(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=141, version=1)
class Microsoft_Windows_DotNETRuntime_141_1(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=141, version=2)
class Microsoft_Windows_DotNETRuntime_141_2(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "ClrInstanceID" / Int16ul,
        "ReJITID" / Int64ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=142, version=0)
class Microsoft_Windows_DotNETRuntime_142_0(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=142, version=1)
class Microsoft_Windows_DotNETRuntime_142_1(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=142, version=2)
class Microsoft_Windows_DotNETRuntime_142_2(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "ClrInstanceID" / Int16ul,
        "ReJITID" / Int64ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=143, version=0)
class Microsoft_Windows_DotNETRuntime_143_0(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "MethodNamespace" / WString,
        "MethodName" / WString,
        "MethodSignature" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=143, version=1)
class Microsoft_Windows_DotNETRuntime_143_1(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "MethodNamespace" / WString,
        "MethodName" / WString,
        "MethodSignature" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=143, version=2)
class Microsoft_Windows_DotNETRuntime_143_2(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "MethodNamespace" / WString,
        "MethodName" / WString,
        "MethodSignature" / WString,
        "ClrInstanceID" / Int16ul,
        "ReJITID" / Int64ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=144, version=0)
class Microsoft_Windows_DotNETRuntime_144_0(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "MethodNamespace" / WString,
        "MethodName" / WString,
        "MethodSignature" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=144, version=1)
class Microsoft_Windows_DotNETRuntime_144_1(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "MethodNamespace" / WString,
        "MethodName" / WString,
        "MethodSignature" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=144, version=2)
class Microsoft_Windows_DotNETRuntime_144_2(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "MethodNamespace" / WString,
        "MethodName" / WString,
        "MethodSignature" / WString,
        "ClrInstanceID" / Int16ul,
        "ReJITID" / Int64ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=145, version=0)
class Microsoft_Windows_DotNETRuntime_145_0(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodToken" / Int32ul,
        "MethodILSize" / Int32ul,
        "MethodNamespace" / WString,
        "MethodName" / WString,
        "MethodSignature" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=145, version=1)
class Microsoft_Windows_DotNETRuntime_145_1(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodToken" / Int32ul,
        "MethodILSize" / Int32ul,
        "MethodNamespace" / WString,
        "MethodName" / WString,
        "MethodSignature" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=149, version=0)
class Microsoft_Windows_DotNETRuntime_149_0(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "AssemblyID" / Int64ul,
        "ModuleFlags" / Int32ul,
        "Reserved1" / Int32ul,
        "ModuleILPath" / WString,
        "ModuleNativePath" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=150, version=0)
class Microsoft_Windows_DotNETRuntime_150_0(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "AssemblyID" / Int64ul,
        "ModuleFlags" / Int32ul,
        "Reserved1" / Int32ul,
        "ModuleILPath" / WString,
        "ModuleNativePath" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=151, version=0)
class Microsoft_Windows_DotNETRuntime_151_0(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "AssemblyID" / Int64ul,
        "AppDomainID" / Int64ul,
        "ModuleFlags" / Int32ul,
        "Reserved1" / Int32ul,
        "ModuleILPath" / WString,
        "ModuleNativePath" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=151, version=1)
class Microsoft_Windows_DotNETRuntime_151_1(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "AssemblyID" / Int64ul,
        "AppDomainID" / Int64ul,
        "ModuleFlags" / Int32ul,
        "Reserved1" / Int32ul,
        "ModuleILPath" / WString,
        "ModuleNativePath" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=152, version=0)
class Microsoft_Windows_DotNETRuntime_152_0(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "AssemblyID" / Int64ul,
        "ModuleFlags" / Int32ul,
        "Reserved1" / Int32ul,
        "ModuleILPath" / WString,
        "ModuleNativePath" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=152, version=1)
class Microsoft_Windows_DotNETRuntime_152_1(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "AssemblyID" / Int64ul,
        "ModuleFlags" / Int32ul,
        "Reserved1" / Int32ul,
        "ModuleILPath" / WString,
        "ModuleNativePath" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=152, version=2)
class Microsoft_Windows_DotNETRuntime_152_2(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "AssemblyID" / Int64ul,
        "ModuleFlags" / Int32ul,
        "Reserved1" / Int32ul,
        "ModuleILPath" / WString,
        "ModuleNativePath" / WString,
        "ClrInstanceID" / Int16ul,
        "ManagedPdbSignature" / Guid,
        "ManagedPdbAge" / Int32ul,
        "ManagedPdbBuildPath" / WString,
        "NativePdbSignature" / Guid,
        "NativePdbAge" / Int32ul,
        "NativePdbBuildPath" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=153, version=0)
class Microsoft_Windows_DotNETRuntime_153_0(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "AssemblyID" / Int64ul,
        "ModuleFlags" / Int32ul,
        "Reserved1" / Int32ul,
        "ModuleILPath" / WString,
        "ModuleNativePath" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=153, version=1)
class Microsoft_Windows_DotNETRuntime_153_1(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "AssemblyID" / Int64ul,
        "ModuleFlags" / Int32ul,
        "Reserved1" / Int32ul,
        "ModuleILPath" / WString,
        "ModuleNativePath" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=153, version=2)
class Microsoft_Windows_DotNETRuntime_153_2(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "AssemblyID" / Int64ul,
        "ModuleFlags" / Int32ul,
        "Reserved1" / Int32ul,
        "ModuleILPath" / WString,
        "ModuleNativePath" / WString,
        "ClrInstanceID" / Int16ul,
        "ManagedPdbSignature" / Guid,
        "ManagedPdbAge" / Int32ul,
        "ManagedPdbBuildPath" / WString,
        "NativePdbSignature" / Guid,
        "NativePdbAge" / Int32ul,
        "NativePdbBuildPath" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=154, version=0)
class Microsoft_Windows_DotNETRuntime_154_0(Etw):
    pattern = Struct(
        "AssemblyID" / Int64ul,
        "AppDomainID" / Int64ul,
        "AssemblyFlags" / Int32ul,
        "FullyQualifiedAssemblyName" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=154, version=1)
class Microsoft_Windows_DotNETRuntime_154_1(Etw):
    pattern = Struct(
        "AssemblyID" / Int64ul,
        "AppDomainID" / Int64ul,
        "BindingID" / Int64ul,
        "AssemblyFlags" / Int32ul,
        "FullyQualifiedAssemblyName" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=155, version=0)
class Microsoft_Windows_DotNETRuntime_155_0(Etw):
    pattern = Struct(
        "AssemblyID" / Int64ul,
        "AppDomainID" / Int64ul,
        "AssemblyFlags" / Int32ul,
        "FullyQualifiedAssemblyName" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=155, version=1)
class Microsoft_Windows_DotNETRuntime_155_1(Etw):
    pattern = Struct(
        "AssemblyID" / Int64ul,
        "AppDomainID" / Int64ul,
        "BindingID" / Int64ul,
        "AssemblyFlags" / Int32ul,
        "FullyQualifiedAssemblyName" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=156, version=0)
class Microsoft_Windows_DotNETRuntime_156_0(Etw):
    pattern = Struct(
        "AppDomainID" / Int64ul,
        "AppDomainFlags" / Int32ul,
        "AppDomainName" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=156, version=1)
class Microsoft_Windows_DotNETRuntime_156_1(Etw):
    pattern = Struct(
        "AppDomainID" / Int64ul,
        "AppDomainFlags" / Int32ul,
        "AppDomainName" / WString,
        "AppDomainIndex" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=157, version=0)
class Microsoft_Windows_DotNETRuntime_157_0(Etw):
    pattern = Struct(
        "AppDomainID" / Int64ul,
        "AppDomainFlags" / Int32ul,
        "AppDomainName" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=157, version=1)
class Microsoft_Windows_DotNETRuntime_157_1(Etw):
    pattern = Struct(
        "AppDomainID" / Int64ul,
        "AppDomainFlags" / Int32ul,
        "AppDomainName" / WString,
        "AppDomainIndex" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=158, version=0)
class Microsoft_Windows_DotNETRuntime_158_0(Etw):
    pattern = Struct(
        "ClrInstanceID" / Int16ul,
        "ModuleID" / Int64ul,
        "RangeBegin" / Int32ul,
        "RangeSize" / Int32ul,
        "RangeType" / Int8ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=181, version=0)
class Microsoft_Windows_DotNETRuntime_181_0(Etw):
    pattern = Struct(
        "VerificationFlags" / Int32ul,
        "ErrorCode" / Int32ul,
        "FullyQualifiedAssemblyName" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=181, version=1)
class Microsoft_Windows_DotNETRuntime_181_1(Etw):
    pattern = Struct(
        "VerificationFlags" / Int32ul,
        "ErrorCode" / Int32ul,
        "FullyQualifiedAssemblyName" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=182, version=0)
class Microsoft_Windows_DotNETRuntime_182_0(Etw):
    pattern = Struct(
        "VerificationFlags" / Int32ul,
        "ErrorCode" / Int32ul,
        "FullyQualifiedAssemblyName" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=182, version=1)
class Microsoft_Windows_DotNETRuntime_182_1(Etw):
    pattern = Struct(
        "VerificationFlags" / Int32ul,
        "ErrorCode" / Int32ul,
        "FullyQualifiedAssemblyName" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=183, version=0)
class Microsoft_Windows_DotNETRuntime_183_0(Etw):
    pattern = Struct(
        "VerificationFlags" / Int32ul,
        "ErrorCode" / Int32ul,
        "ModulePath" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=183, version=1)
class Microsoft_Windows_DotNETRuntime_183_1(Etw):
    pattern = Struct(
        "VerificationFlags" / Int32ul,
        "ErrorCode" / Int32ul,
        "ModulePath" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=184, version=0)
class Microsoft_Windows_DotNETRuntime_184_0(Etw):
    pattern = Struct(
        "VerificationFlags" / Int32ul,
        "ErrorCode" / Int32ul,
        "ModulePath" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=184, version=1)
class Microsoft_Windows_DotNETRuntime_184_1(Etw):
    pattern = Struct(
        "VerificationFlags" / Int32ul,
        "ErrorCode" / Int32ul,
        "ModulePath" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=185, version=0)
class Microsoft_Windows_DotNETRuntime_185_0(Etw):
    pattern = Struct(
        "MethodBeingCompiledNamespace" / WString,
        "MethodBeingCompiledName" / WString,
        "MethodBeingCompiledNameSignature" / WString,
        "InlinerNamespace" / WString,
        "InlinerName" / WString,
        "InlinerNameSignature" / WString,
        "InlineeNamespace" / WString,
        "InlineeName" / WString,
        "InlineeNameSignature" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=186, version=0)
class Microsoft_Windows_DotNETRuntime_186_0(Etw):
    pattern = Struct(
        "MethodBeingCompiledNamespace" / WString,
        "MethodBeingCompiledName" / WString,
        "MethodBeingCompiledNameSignature" / WString,
        "InlinerNamespace" / WString,
        "InlinerName" / WString,
        "InlinerNameSignature" / WString,
        "InlineeNamespace" / WString,
        "InlineeName" / WString,
        "InlineeNameSignature" / WString,
        "FailAlways" / Int8ul,
        "FailReason" / CString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=187, version=0)
class Microsoft_Windows_DotNETRuntime_187_0(Etw):
    pattern = Struct(
        "ClrInstanceID" / Int16ul,
        "Sku" / Int16ul,
        "BclMajorVersion" / Int16ul,
        "BclMinorVersion" / Int16ul,
        "BclBuildNumber" / Int16ul,
        "BclQfeNumber" / Int16ul,
        "VMMajorVersion" / Int16ul,
        "VMMinorVersion" / Int16ul,
        "VMBuildNumber" / Int16ul,
        "VMQfeNumber" / Int16ul,
        "StartupFlags" / Int32ul,
        "StartupMode" / Int8ul,
        "CommandLine" / WString,
        "ComObjectGuid" / Guid,
        "RuntimeDllPath" / WString
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=188, version=0)
class Microsoft_Windows_DotNETRuntime_188_0(Etw):
    pattern = Struct(
        "MethodBeingCompiledNamespace" / WString,
        "MethodBeingCompiledName" / WString,
        "MethodBeingCompiledNameSignature" / WString,
        "CallerNamespace" / WString,
        "CallerName" / WString,
        "CallerNameSignature" / WString,
        "CalleeNamespace" / WString,
        "CalleeName" / WString,
        "CalleeNameSignature" / WString,
        "TailPrefix" / Int8ul,
        "TailCallType" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=189, version=0)
class Microsoft_Windows_DotNETRuntime_189_0(Etw):
    pattern = Struct(
        "MethodBeingCompiledNamespace" / WString,
        "MethodBeingCompiledName" / WString,
        "MethodBeingCompiledNameSignature" / WString,
        "CallerNamespace" / WString,
        "CallerName" / WString,
        "CallerNameSignature" / WString,
        "CalleeNamespace" / WString,
        "CalleeName" / WString,
        "CalleeNameSignature" / WString,
        "TailPrefix" / Int8ul,
        "FailReason" / CString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=190, version=0)
class Microsoft_Windows_DotNETRuntime_190_0(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ReJITID" / Int64ul,
        "MethodExtent" / Int8ul,
        "CountOfMapEntries" / Int16ul,
        "ILOffsets" / Int32ul,
        "NativeOffsets" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=200, version=0)
class Microsoft_Windows_DotNETRuntime_200_0(Etw):
    pattern = Struct(
        "BytesAllocated" / Int64ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=201, version=0)
class Microsoft_Windows_DotNETRuntime_201_0(Etw):
    pattern = Struct(
        "BytesFreed" / Int64ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=202, version=0)
class Microsoft_Windows_DotNETRuntime_202_0(Etw):
    pattern = Struct(
        "HeapNum" / Int32ul,
        "ClrInstanceID" / Int16ul,
        "Type" / Int32ul,
        "Bytes" / Int64ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=203, version=2)
class Microsoft_Windows_DotNETRuntime_203_2(Etw):
    pattern = Struct(
        "Heap" / Int32ul,
        "JoinTime" / Int32ul,
        "JoinType" / Int32ul,
        "ClrInstanceID" / Int16ul,
        "JoinID" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=204, version=3)
class Microsoft_Windows_DotNETRuntime_204_3(Etw):
    pattern = Struct(
        "ClrInstanceID" / Int16ul,
        "FreeListAllocated" / Int64ul,
        "FreeListRejected" / Int64ul,
        "EndOfSegAllocated" / Int64ul,
        "CondemnedAllocated" / Int64ul,
        "PinnedAllocated" / Int64ul,
        "PinnedAllocatedAdvance" / Int64ul,
        "RunningFreeListEfficiency" / Int32ul,
        "CondemnReasons0" / Int32ul,
        "CondemnReasons1" / Int32ul,
        "CompactMechanisms" / Int32ul,
        "ExpandMechanisms" / Int32ul,
        "HeapIndex" / Int32ul,
        "ExtraGen0Commit" / Int64ul,
        "Count" / Int32ul,
        "Values" / Int64ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=205, version=2)
class Microsoft_Windows_DotNETRuntime_205_2(Etw):
    pattern = Struct(
        "FinalYoungestDesired" / Int64ul,
        "NumHeaps" / Int32sl,
        "CondemnedGeneration" / Int32ul,
        "Gen0ReductionCount" / Int32ul,
        "Reason" / Int32ul,
        "GlobalMechanisms" / Int32ul,
        "ClrInstanceID" / Int16ul,
        "PauseMode" / Int32ul,
        "MemoryPressure" / Int32ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=206, version=0)
class Microsoft_Windows_DotNETRuntime_206_0(Etw):
    pattern = Struct(
        "GCName" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=250, version=0)
class Microsoft_Windows_DotNETRuntime_250_0(Etw):
    pattern = Struct(
        "EntryEIP" / Int64ul,
        "MethodID" / Int64ul,
        "MethodName" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=252, version=0)
class Microsoft_Windows_DotNETRuntime_252_0(Etw):
    pattern = Struct(
        "EntryEIP" / Int64ul,
        "MethodID" / Int64ul,
        "MethodName" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("e13c0d23-ccbc-4e12-931b-d9cc2eee27e4"), event_id=254, version=0)
class Microsoft_Windows_DotNETRuntime_254_0(Etw):
    pattern = Struct(
        "EntryEIP" / Int64ul,
        "MethodID" / Int64ul,
        "MethodName" / WString,
        "ClrInstanceID" / Int16ul
    )

