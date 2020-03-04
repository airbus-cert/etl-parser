# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Partition
GUID : 412bdff2-a8c4-470d-8f33-63fe0d8c20e2
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("412bdff2-a8c4-470d-8f33-63fe0d8c20e2"), event_id=1001, version=0)
class Microsoft_Windows_Partition_1001_0(Etw):
    pattern = Struct(
        "DiskNumber" / Int32ul,
        "ControlCode" / Int32ul
    )


@declare(guid=guid("412bdff2-a8c4-470d-8f33-63fe0d8c20e2"), event_id=1002, version=0)
class Microsoft_Windows_Partition_1002_0(Etw):
    pattern = Struct(
        "DiskNumber" / Int32ul,
        "ControlCode" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("412bdff2-a8c4-470d-8f33-63fe0d8c20e2"), event_id=1003, version=0)
class Microsoft_Windows_Partition_1003_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "IncrementEnergy" / Int64ul,
        "SrvTime" / Int64ul,
        "EndByteOffset" / Int64ul,
        "IoSize" / Int32ul,
        "LastIdleState" / Int8ul,
        "IsRandom" / Int8ul
    )


@declare(guid=guid("412bdff2-a8c4-470d-8f33-63fe0d8c20e2"), event_id=1004, version=0)
class Microsoft_Windows_Partition_1004_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "IncrementEnergy" / Int64ul,
        "IdleTime" / Int64ul,
        "LastIdleState" / Int8ul
    )


@declare(guid=guid("412bdff2-a8c4-470d-8f33-63fe0d8c20e2"), event_id=1005, version=0)
class Microsoft_Windows_Partition_1005_0(Etw):
    pattern = Struct(
        "LocalLastCompTime" / Int64ul,
        "SharedLastCompTime" / Int64ul,
        "CompTime" / Int64ul
    )


@declare(guid=guid("412bdff2-a8c4-470d-8f33-63fe0d8c20e2"), event_id=1006, version=0)
class Microsoft_Windows_Partition_1006_0(Etw):
    pattern = Struct(
        "Version" / Int32ul,
        "DiskNumber" / Int32ul,
        "Flags" / Int32ul,
        "Characteristics" / Int32ul,
        "IsSystemCritical" / Int8ul,
        "PagingCount" / Int32ul,
        "HibernationCount" / Int32ul,
        "DumpCount" / Int32ul,
        "BytesPerSector" / Int32ul,
        "Capacity" / Int64ul,
        "BusType" / Int32ul,
        "Manufacturer" / WString,
        "Model" / WString,
        "Revision" / WString,
        "SerialNumber" / WString,
        "Location" / WString,
        "ParentId" / WString,
        "IoctlSupport" / Int64ul,
        "IdFlags" / Int32ul,
        "DiskId" / Guid,
        "AdapterId" / Guid,
        "RegistryId" / Guid,
        "PoolId" / Guid,
        "FirmwareSupportsUpgrade" / Int8ul,
        "FirmwareSlotCount" / Int8ul,
        "StorageIdCount" / Int32ul,
        "StorageIdCodeSet" / Int32ul,
        "StorageIdType" / Int32ul,
        "StorageIdAssociation" / Int32ul,
        "StorageIdBytes" / Int32ul,
        "StorageId" / Bytes(lambda this: this.StorageIdBytes),
        "WriteCacheType" / Int32ul,
        "WriteCacheEnabled" / Int32ul,
        "WriteCacheChangeable" / Int32ul,
        "WriteThroughSupported" / Int32ul,
        "FlushCacheSupported" / Int8ul,
        "IsPowerProtected" / Int8ul,
        "NVCacheEnabled" / Int8ul,
        "BytesPerLogicalSector" / Int32ul,
        "BytesPerPhysicalSector" / Int32ul,
        "BytesOffsetForSectorAlignment" / Int32ul,
        "IncursSeekPenalty" / Int8ul,
        "IsTrimSupported" / Int8ul,
        "IsThinProvisioned" / Int8ul,
        "OptimalUnmapGranularity" / Int64ul,
        "UnmapAlignment" / Int64ul,
        "NumberOfLogicalCopies" / Int32ul,
        "NumberOfPhysicalCopies" / Int32ul,
        "FaultTolerance" / Int32ul,
        "NumberOfColumns" / Int32ul,
        "InterleaveBytes" / Int32ul,
        "HybridSupported" / Int8ul,
        "HybridCacheBytes" / Int64ul,
        "AdapterMaximumTransferBytes" / Int32ul,
        "AdapterMaximumTransferPages" / Int32ul,
        "AdapterAlignmentMask" / Int32ul,
        "AdapterSerialNumber" / WString,
        "PortDriver" / Int32ul,
        "UserRemovalPolicy" / Int8ul,
        "PartitionStyle" / Int32ul,
        "PartitionCount" / Int32ul,
        "PartitionTableBytes" / Int32ul,
        "PartitionTable" / Bytes(lambda this: this.PartitionTableBytes),
        "MbrBytes" / Int32ul,
        "Mbr" / Bytes(lambda this: this.MbrBytes),
        "Vbr0Bytes" / Int32ul,
        "Vbr0" / Bytes(lambda this: this.Vbr0Bytes),
        "Vbr1Bytes" / Int32ul,
        "Vbr1" / Bytes(lambda this: this.Vbr1Bytes),
        "Vbr2Bytes" / Int32ul,
        "Vbr2" / Bytes(lambda this: this.Vbr2Bytes),
        "Vbr3Size" / Int32ul,
        "Vbr3" / Bytes(lambda this: this.Vbr3Size)
    )

