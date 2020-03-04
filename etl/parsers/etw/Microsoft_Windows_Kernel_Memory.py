# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-Memory
GUID : d1d93ef7-e1f2-4f45-9943-03d245fe6c00
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d1d93ef7-e1f2-4f45-9943-03d245fe6c00"), event_id=1, version=1)
class Microsoft_Windows_Kernel_Memory_1_1(Etw):
    pattern = Struct(
        "PriorityLevels" / Int8ul,
        "ZeroPageCount" / Int64ul,
        "FreePageCount" / Int64ul,
        "ModifiedPageCount" / Int64ul,
        "ModifiedNoWritePageCount" / Int64ul,
        "BadPageCount" / Int64ul,
        "StandbyPageCounts" / Int64ul,
        "RepurposedPageCounts" / Int64ul,
        "ModifiedPageCountPageFile" / Int64ul,
        "PagedPoolPageCount" / Int64ul,
        "NonPagedPoolPageCount" / Int64ul,
        "MdlPageCount" / Int64ul,
        "CommitPageCount" / Int64ul
    )


@declare(guid=guid("d1d93ef7-e1f2-4f45-9943-03d245fe6c00"), event_id=2, version=0)
class Microsoft_Windows_Kernel_Memory_2_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "WSCommitInfo" / CString
    )


@declare(guid=guid("d1d93ef7-e1f2-4f45-9943-03d245fe6c00"), event_id=2, version=1)
class Microsoft_Windows_Kernel_Memory_2_1(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "WSCommitInfo" / CString
    )


@declare(guid=guid("d1d93ef7-e1f2-4f45-9943-03d245fe6c00"), event_id=2, version=2)
class Microsoft_Windows_Kernel_Memory_2_2(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "WSCommitInfo" / CString
    )


@declare(guid=guid("d1d93ef7-e1f2-4f45-9943-03d245fe6c00"), event_id=3, version=0)
class Microsoft_Windows_Kernel_Memory_3_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "SessionWSCommitInfo" / CString
    )


@declare(guid=guid("d1d93ef7-e1f2-4f45-9943-03d245fe6c00"), event_id=3, version=1)
class Microsoft_Windows_Kernel_Memory_3_1(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "SessionWSCommitInfo" / CString
    )


@declare(guid=guid("d1d93ef7-e1f2-4f45-9943-03d245fe6c00"), event_id=3, version=2)
class Microsoft_Windows_Kernel_Memory_3_2(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "SessionWSCommitInfo" / CString
    )


@declare(guid=guid("d1d93ef7-e1f2-4f45-9943-03d245fe6c00"), event_id=4, version=0)
class Microsoft_Windows_Kernel_Memory_4_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul
    )


@declare(guid=guid("d1d93ef7-e1f2-4f45-9943-03d245fe6c00"), event_id=4, version=1)
class Microsoft_Windows_Kernel_Memory_4_1(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("d1d93ef7-e1f2-4f45-9943-03d245fe6c00"), event_id=5, version=0)
class Microsoft_Windows_Kernel_Memory_5_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "Status" / Int32ul,
        "PagesProcessed" / Int32ul
    )


@declare(guid=guid("d1d93ef7-e1f2-4f45-9943-03d245fe6c00"), event_id=5, version=1)
class Microsoft_Windows_Kernel_Memory_5_1(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "Status" / Int32ul,
        "PagesProcessed" / Int64ul,
        "WriteCombinePagesProcessed" / Int64ul,
        "UncachedPagesProcessed" / Int64ul,
        "CleanPagesProcessed" / Int64ul
    )


@declare(guid=guid("d1d93ef7-e1f2-4f45-9943-03d245fe6c00"), event_id=6, version=0)
class Microsoft_Windows_Kernel_Memory_6_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul
    )


@declare(guid=guid("d1d93ef7-e1f2-4f45-9943-03d245fe6c00"), event_id=6, version=1)
class Microsoft_Windows_Kernel_Memory_6_1(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("d1d93ef7-e1f2-4f45-9943-03d245fe6c00"), event_id=7, version=0)
class Microsoft_Windows_Kernel_Memory_7_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("d1d93ef7-e1f2-4f45-9943-03d245fe6c00"), event_id=8, version=0)
class Microsoft_Windows_Kernel_Memory_8_0(Etw):
    pattern = Struct(
        "AcgFlag" / Int32ul
    )


@declare(guid=guid("d1d93ef7-e1f2-4f45-9943-03d245fe6c00"), event_id=9, version=0)
class Microsoft_Windows_Kernel_Memory_9_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("d1d93ef7-e1f2-4f45-9943-03d245fe6c00"), event_id=10, version=0)
class Microsoft_Windows_Kernel_Memory_10_0(Etw):
    pattern = Struct(
        "DurationInMicroseconds" / Int64ul,
        "TotalBytes" / Int64ul,
        "LowAddress" / Int64ul,
        "HighAddress" / Int64ul,
        "SkipBytes" / Int64ul,
        "MemoryDescriptorList" / Int64ul,
        "IdealNode" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("d1d93ef7-e1f2-4f45-9943-03d245fe6c00"), event_id=11, version=0)
class Microsoft_Windows_Kernel_Memory_11_0(Etw):
    pattern = Struct(
        "DurationInMicroseconds" / Int64ul,
        "TotalBytes" / Int64ul,
        "LowAddress" / Int64ul,
        "HighAddress" / Int64ul,
        "Boundary" / Int64ul,
        "PhysicalAddress" / Int64ul,
        "MappedAddress" / Int64ul,
        "AllocatedFromPool" / Int8ul,
        "ProtectionMask" / Int32ul,
        "PreferredNode" / Int32ul
    )


@declare(guid=guid("d1d93ef7-e1f2-4f45-9943-03d245fe6c00"), event_id=12, version=0)
class Microsoft_Windows_Kernel_Memory_12_0(Etw):
    pattern = Struct(
        "PartitionId" / Int32ul,
        "Count" / Int32ul,
        "MemoryNodeInfo" / Int8sl
    )

