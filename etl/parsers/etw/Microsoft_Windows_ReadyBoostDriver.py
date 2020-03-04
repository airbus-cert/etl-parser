# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ReadyBoostDriver
GUID : 2a274310-42d5-4019-b816-e4b8c7abe95c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=1, version=2)
class Microsoft_Windows_ReadyBoostDriver_1_2(Etw):
    pattern = Struct(
        "ByteOffset" / Int64ul,
        "Irp" / Int64ul,
        "ByteLength" / Int32ul,
        "Flags" / Int32ul,
        "FileKey" / Int64ul,
        "StoreId" / Int16ul,
        "VolumeId" / Int16ul
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=2, version=1)
class Microsoft_Windows_ReadyBoostDriver_2_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=3, version=2)
class Microsoft_Windows_ReadyBoostDriver_3_2(Etw):
    pattern = Struct(
        "DataKey" / Int64ul,
        "DataMgr" / Int64ul,
        "StoreOffset" / Int32ul,
        "CompressedSize" / Int16ul,
        "Flags" / Int16ul
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=4, version=1)
class Microsoft_Windows_ReadyBoostDriver_4_1(Etw):
    pattern = Struct(
        "DataKey" / Int64ul,
        "DataMgr" / Int64ul,
        "StoreOffset" / Int32ul
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=6, version=1)
class Microsoft_Windows_ReadyBoostDriver_6_1(Etw):
    pattern = Struct(
        "StoreKey" / Int64ul
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=8, version=1)
class Microsoft_Windows_ReadyBoostDriver_8_1(Etw):
    pattern = Struct(
        "VolumeId" / Int16ul,
        "VolumeNameLength" / Int16ul,
        "VolumePath" / Bytes(lambda this: this.VolumeNameLength)
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=9, version=1)
class Microsoft_Windows_ReadyBoostDriver_9_1(Etw):
    pattern = Struct(
        "VolumeId" / Int16ul,
        "VolumeNameLength" / Int16ul,
        "VolumePath" / Bytes(lambda this: this.VolumeNameLength)
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=10, version=1)
class Microsoft_Windows_ReadyBoostDriver_10_1(Etw):
    pattern = Struct(
        "VolumeId" / Int16ul,
        "VolumeNameLength" / Int16ul,
        "VolumePath" / Bytes(lambda this: this.VolumeNameLength)
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=11, version=1)
class Microsoft_Windows_ReadyBoostDriver_11_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Reason" / Int16ul,
        "Flags" / Int16ul
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=12, version=2)
class Microsoft_Windows_ReadyBoostDriver_12_2(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "ByteOffset" / Int64ul,
        "FileKey" / Int64ul,
        "ProcessKey" / Int64ul,
        "ByteLength" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=13, version=1)
class Microsoft_Windows_ReadyBoostDriver_13_1(Etw):
    pattern = Struct(
        "DataMgr" / Int64ul,
        "VirtualAddress" / Int64ul,
        "PhysicalAddress" / Int64ul,
        "Size" / Int16ul,
        "FileBacked" / Int8ul,
        "CorruptionType" / Int8ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=14, version=1)
class Microsoft_Windows_ReadyBoostDriver_14_1(Etw):
    pattern = Struct(
        "DataKey" / Int64ul,
        "DataMgr" / Int64ul,
        "StoreOffset" / Int32ul,
        "CompressedSize" / Int16ul,
        "Flags" / Int16ul
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=15, version=2)
class Microsoft_Windows_ReadyBoostDriver_15_2(Etw):
    pattern = Struct(
        "DataMgr" / Int64ul,
        "RegionIndex" / Int32ul,
        "Status" / Int32ul,
        "SpaceUsed" / Int16ul,
        "LastAccessTime" / Int16ul
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=16, version=2)
class Microsoft_Windows_ReadyBoostDriver_16_2(Etw):
    pattern = Struct(
        "DataMgr" / Int64ul,
        "RegionIndex" / Int32ul,
        "Status" / Int32ul,
        "SpaceUsed" / Int16ul,
        "LastAccessTime" / Int16ul
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=17, version=1)
class Microsoft_Windows_ReadyBoostDriver_17_1(Etw):
    pattern = Struct(
        "FailReason" / Int32ul,
        "FailStatus" / Int32ul,
        "ObjectPathLength" / Int16ul,
        "ObjectPath" / Bytes(lambda this: this.ObjectPathLength)
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=18, version=1)
class Microsoft_Windows_ReadyBoostDriver_18_1(Etw):
    pattern = Struct(
        "UserActive" / Int8ul
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=19, version=1)
class Microsoft_Windows_ReadyBoostDriver_19_1(Etw):
    pattern = Struct(
        "StoreKey" / Int64ul,
        "Size" / Int32ul,
        "Data" / Bytes(lambda this: this.Size)
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=20, version=1)
class Microsoft_Windows_ReadyBoostDriver_20_1(Etw):
    pattern = Struct(
        "Size" / Int32ul,
        "Data" / Bytes(lambda this: this.Size)
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=21, version=1)
class Microsoft_Windows_ReadyBoostDriver_21_1(Etw):
    pattern = Struct(
        "StoreKey" / Int64ul,
        "Param" / Int64ul
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=22, version=1)
class Microsoft_Windows_ReadyBoostDriver_22_1(Etw):
    pattern = Struct(
        "DataMgr" / Int64ul,
        "RegionIndex" / Int32ul,
        "Status" / Int32ul,
        "SpaceUsed" / Int16ul,
        "LastAccessTime" / Int16ul
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=23, version=1)
class Microsoft_Windows_ReadyBoostDriver_23_1(Etw):
    pattern = Struct(
        "DataMgr" / Int64ul,
        "RegionIndex" / Int32ul,
        "Status" / Int32ul,
        "SpaceUsed" / Int16ul,
        "LastAccessTime" / Int16ul
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=24, version=1)
class Microsoft_Windows_ReadyBoostDriver_24_1(Etw):
    pattern = Struct(
        "DataMgr" / Int64ul,
        "RegionIndex" / Int32ul,
        "Status" / Int32ul,
        "SpaceUsed" / Int16ul,
        "LastAccessTime" / Int16ul
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=25, version=1)
class Microsoft_Windows_ReadyBoostDriver_25_1(Etw):
    pattern = Struct(
        "DataMgr" / Int64ul,
        "RegionIndex" / Int32ul,
        "Status" / Int32ul,
        "SpaceUsed" / Int16ul,
        "LastAccessTime" / Int16ul
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=26, version=1)
class Microsoft_Windows_ReadyBoostDriver_26_1(Etw):
    pattern = Struct(
        "DataKey" / Int64ul,
        "LengthInBytes" / Int64ul
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=27, version=1)
class Microsoft_Windows_ReadyBoostDriver_27_1(Etw):
    pattern = Struct(
        "Reason" / Int8ul,
        "FailStatus" / Int32ul,
        "DeviceDescLength" / Int16ul,
        "DeviceDescription" / Bytes(lambda this: this.DeviceDescLength),
        "ObjectPathLength" / Int16ul,
        "ObjectPath" / Bytes(lambda this: this.ObjectPathLength)
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=28, version=1)
class Microsoft_Windows_ReadyBoostDriver_28_1(Etw):
    pattern = Struct(
        "Size" / Int32ul,
        "Data" / Bytes(lambda this: this.Size)
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=29, version=0)
class Microsoft_Windows_ReadyBoostDriver_29_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=30, version=1)
class Microsoft_Windows_ReadyBoostDriver_30_1(Etw):
    pattern = Struct(
        "Key" / Int64ul,
        "Operation" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=31, version=1)
class Microsoft_Windows_ReadyBoostDriver_31_1(Etw):
    pattern = Struct(
        "VolumeOffset" / Int64ul,
        "Length" / Int32ul,
        "Read" / Int8ul,
        "Priority" / Int16ul,
        "PartialBmpHit" / Int8ul
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=32, version=0)
class Microsoft_Windows_ReadyBoostDriver_32_0(Etw):
    pattern = Struct(
        "Key" / Int64ul
    )


@declare(guid=guid("2a274310-42d5-4019-b816-e4b8c7abe95c"), event_id=33, version=0)
class Microsoft_Windows_ReadyBoostDriver_33_0(Etw):
    pattern = Struct(
        "Key" / Int64ul,
        "Flags" / Int32ul
    )

