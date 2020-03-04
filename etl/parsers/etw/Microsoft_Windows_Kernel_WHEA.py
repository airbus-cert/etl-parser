# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-WHEA
GUID : 7b563579-53c8-44e7-8236-0f87b9fe6594
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=1, version=0)
class Microsoft_Windows_Kernel_WHEA_1_0(Etw):
    pattern = Struct(
        "Signature" / Int32ul,
        "Revision" / Int16ul,
        "Reserved1" / Int16ul,
        "Reserved2" / Int16ul,
        "SectionCount" / Int16ul,
        "Severity" / Int32ul,
        "ValidationBits" / Int32ul,
        "Length" / Int32ul,
        "Timestamp" / Int64ul,
        "PlatformId" / Guid,
        "PartitionId" / Guid,
        "CreatorId" / Guid,
        "NotifyType" / Guid,
        "RecordId" / Int64ul,
        "Flags" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=2, version=0)
class Microsoft_Windows_Kernel_WHEA_2_0(Etw):
    pattern = Struct(
        "Signature" / Int32ul,
        "Revision" / Int16ul,
        "Reserved1" / Int16ul,
        "Reserved2" / Int16ul,
        "SectionCount" / Int16ul,
        "Severity" / Int32ul,
        "ValidationBits" / Int32ul,
        "Length" / Int32ul,
        "Timestamp" / Int64ul,
        "PlatformId" / Guid,
        "PartitionId" / Guid,
        "CreatorId" / Guid,
        "NotifyType" / Guid,
        "RecordId" / Int64ul,
        "Flags" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=3, version=0)
class Microsoft_Windows_Kernel_WHEA_3_0(Etw):
    pattern = Struct(
        "Signature" / Int32ul,
        "Revision" / Int16ul,
        "Reserved1" / Int16ul,
        "Reserved2" / Int16ul,
        "SectionCount" / Int16ul,
        "Severity" / Int32ul,
        "ValidationBits" / Int32ul,
        "Length" / Int32ul,
        "Timestamp" / Int64ul,
        "PlatformId" / Guid,
        "PartitionId" / Guid,
        "CreatorId" / Guid,
        "NotifyType" / Guid,
        "RecordId" / Int64ul,
        "Flags" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=4, version=0)
class Microsoft_Windows_Kernel_WHEA_4_0(Etw):
    pattern = Struct(
        "Signature" / Int32ul,
        "Revision" / Int16ul,
        "Reserved1" / Int16ul,
        "Reserved2" / Int16ul,
        "SectionCount" / Int16ul,
        "Severity" / Int32ul,
        "ValidationBits" / Int32ul,
        "Length" / Int32ul,
        "Timestamp" / Int64ul,
        "PlatformId" / Guid,
        "PartitionId" / Guid,
        "CreatorId" / Guid,
        "NotifyType" / Guid,
        "RecordId" / Int64ul,
        "Flags" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=5, version=0)
class Microsoft_Windows_Kernel_WHEA_5_0(Etw):
    pattern = Struct(
        "ErrorSourceCount" / Int32ul,
        "ErrorRecordFormat" / Int32ul,
        "ErrorSourceTableLength" / Int32ul,
        "ErrorSourceTable" / Bytes(lambda this: this.ErrorSourceTableLength)
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=6, version=0)
class Microsoft_Windows_Kernel_WHEA_6_0(Etw):
    pattern = Struct(
        "TransactionType" / Int32ul,
        "Participation" / Int32ul,
        "RequestType" / Int32ul,
        "MemorIO" / Int32ul,
        "MemHierarchyLvl" / Int32ul,
        "Address" / Int64ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=7, version=0)
class Microsoft_Windows_Kernel_WHEA_7_0(Etw):
    pattern = Struct(
        "TransactionType" / Int32ul,
        "Participation" / Int32ul,
        "RequestType" / Int32ul,
        "MemorIO" / Int32ul,
        "MemHierarchyLvl" / Int32ul,
        "Address" / Int64ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=8, version=0)
class Microsoft_Windows_Kernel_WHEA_8_0(Etw):
    pattern = Struct(
        "TransactionType" / Int32ul,
        "Participation" / Int32ul,
        "RequestType" / Int32ul,
        "MemorIO" / Int32ul,
        "MemHierarchyLvl" / Int32ul,
        "Address" / Int64ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=9, version=0)
class Microsoft_Windows_Kernel_WHEA_9_0(Etw):
    pattern = Struct(
        "TransactionType" / Int32ul,
        "Participation" / Int32ul,
        "RequestType" / Int32ul,
        "MemorIO" / Int32ul,
        "MemHierarchyLvl" / Int32ul,
        "Address" / Int64ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=10, version=0)
class Microsoft_Windows_Kernel_WHEA_10_0(Etw):
    pattern = Struct(
        "TransactionType" / Int32ul,
        "Participation" / Int32ul,
        "RequestType" / Int32ul,
        "MemorIO" / Int32ul,
        "MemHierarchyLvl" / Int32ul,
        "Address" / Int64ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=11, version=0)
class Microsoft_Windows_Kernel_WHEA_11_0(Etw):
    pattern = Struct(
        "TransactionType" / Int32ul,
        "Participation" / Int32ul,
        "RequestType" / Int32ul,
        "MemorIO" / Int32ul,
        "MemHierarchyLvl" / Int32ul,
        "Address" / Int64ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=12, version=0)
class Microsoft_Windows_Kernel_WHEA_12_0(Etw):
    pattern = Struct(
        "TransactionType" / Int32ul,
        "Participation" / Int32ul,
        "RequestType" / Int32ul,
        "MemorIO" / Int32ul,
        "MemHierarchyLvl" / Int32ul,
        "Address" / Int64ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=13, version=0)
class Microsoft_Windows_Kernel_WHEA_13_0(Etw):
    pattern = Struct(
        "TransactionType" / Int32ul,
        "Participation" / Int32ul,
        "RequestType" / Int32ul,
        "MemorIO" / Int32ul,
        "MemHierarchyLvl" / Int32ul,
        "Address" / Int64ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=14, version=0)
class Microsoft_Windows_Kernel_WHEA_14_0(Etw):
    pattern = Struct(
        "TransactionType" / Int32ul,
        "Participation" / Int32ul,
        "RequestType" / Int32ul,
        "MemorIO" / Int32ul,
        "MemHierarchyLvl" / Int32ul,
        "Address" / Int64ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=15, version=0)
class Microsoft_Windows_Kernel_WHEA_15_0(Etw):
    pattern = Struct(
        "TransactionType" / Int32ul,
        "Participation" / Int32ul,
        "RequestType" / Int32ul,
        "MemorIO" / Int32ul,
        "MemHierarchyLvl" / Int32ul,
        "Address" / Int64ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=16, version=0)
class Microsoft_Windows_Kernel_WHEA_16_0(Etw):
    pattern = Struct(
        "TransactionType" / Int32ul,
        "Participation" / Int32ul,
        "RequestType" / Int32ul,
        "MemorIO" / Int32ul,
        "MemHierarchyLvl" / Int32ul,
        "Address" / Int64ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=17, version=0)
class Microsoft_Windows_Kernel_WHEA_17_0(Etw):
    pattern = Struct(
        "TransactionType" / Int32ul,
        "Participation" / Int32ul,
        "RequestType" / Int32ul,
        "MemorIO" / Int32ul,
        "MemHierarchyLvl" / Int32ul,
        "Address" / Int64ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=18, version=0)
class Microsoft_Windows_Kernel_WHEA_18_0(Etw):
    pattern = Struct(
        "SourceIdBus" / Int32ul,
        "SourceIdDev" / Int32ul,
        "SourceIdFun" / Int32ul,
        "UncorrectableErrorStatus" / Int32ul,
        "CorrectableErrorStatus" / Int32ul,
        "HeaderLog0" / Int32ul,
        "HeaderLog1" / Int32ul,
        "HeaderLog2" / Int32ul,
        "HeaderLog3" / Int32ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=19, version=0)
class Microsoft_Windows_Kernel_WHEA_19_0(Etw):
    pattern = Struct(
        "SourceIdBus" / Int32ul,
        "SourceIdDev" / Int32ul,
        "SourceIdFun" / Int32ul,
        "UncorrectableErrorStatus" / Int32ul,
        "CorrectableErrorStatus" / Int32ul,
        "HeaderLog0" / Int32ul,
        "HeaderLog1" / Int32ul,
        "HeaderLog2" / Int32ul,
        "HeaderLog3" / Int32ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=20, version=0)
class Microsoft_Windows_Kernel_WHEA_20_0(Etw):
    pattern = Struct(
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=31, version=0)
class Microsoft_Windows_Kernel_WHEA_31_0(Etw):
    pattern = Struct(
        "PhysicalAddress" / Int64ul,
        "Pending" / Int8ul,
        "PlatformDirected" / Int8ul,
        "Uncorrected" / Int8ul,
        "Persisted" / Int8ul
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=32, version=0)
class Microsoft_Windows_Kernel_WHEA_32_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmSid" / Sid,
        "SqmWindowsSessionId" / Int32ul,
        "SqmSessionFlags" / Int32ul
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=33, version=0)
class Microsoft_Windows_Kernel_WHEA_33_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=34, version=0)
class Microsoft_Windows_Kernel_WHEA_34_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=35, version=0)
class Microsoft_Windows_Kernel_WHEA_35_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=36, version=0)
class Microsoft_Windows_Kernel_WHEA_36_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=37, version=0)
class Microsoft_Windows_Kernel_WHEA_37_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=38, version=0)
class Microsoft_Windows_Kernel_WHEA_38_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=39, version=0)
class Microsoft_Windows_Kernel_WHEA_39_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmStringDatapointValue" / WString
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=40, version=0)
class Microsoft_Windows_Kernel_WHEA_40_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=41, version=0)
class Microsoft_Windows_Kernel_WHEA_41_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "ProcessName" / WString
    )


@declare(guid=guid("7b563579-53c8-44e7-8236-0f87b9fe6594"), event_id=42, version=0)
class Microsoft_Windows_Kernel_WHEA_42_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Owner" / Int32ul,
        "Id" / Int32ul,
        "Flags" / Int32ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )

