# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-StoreMgr
GUID : a6ad76e3-867a-4635-91b3-4904ba6374d7
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a6ad76e3-867a-4635-91b3-4904ba6374d7"), event_id=1, version=2)
class Microsoft_Windows_Kernel_StoreMgr_1_2(Etw):
    pattern = Struct(
        "DataKey" / Int32ul,
        "DataMgr" / Int64ul,
        "StoreOffset" / Int32ul,
        "CompressedSize" / Int16ul,
        "Flags" / Int16ul
    )


@declare(guid=guid("a6ad76e3-867a-4635-91b3-4904ba6374d7"), event_id=2, version=1)
class Microsoft_Windows_Kernel_StoreMgr_2_1(Etw):
    pattern = Struct(
        "DataKey" / Int32ul,
        "DataMgr" / Int64ul,
        "StoreOffset" / Int32ul
    )


@declare(guid=guid("a6ad76e3-867a-4635-91b3-4904ba6374d7"), event_id=3, version=3)
class Microsoft_Windows_Kernel_StoreMgr_3_3(Etw):
    pattern = Struct(
        "StoreKey" / Int64ul,
        "StoreFileKey" / Int64ul,
        "UserDataMgr" / Int64ul,
        "MetadataMgr" / Int64ul,
        "RegionSize" / Int32ul,
        "RegionCount" / Int32ul,
        "BlockSize" / Int32ul,
        "SectorSize" / Int32ul,
        "EncryptionStrength" / Int32ul,
        "StoreType" / Int16ul,
        "StoreId" / Int16ul,
        "BlocksStored" / Int32ul,
        "RegionsInUse" / Int32ul,
        "TotalSpaceUsed" / Int32ul,
        "Flags" / Int32ul,
        "MetaRegionCount" / Int32ul,
        "MetaRegionsInUse" / Int32ul,
        "MetaRegionsSpaceUsed" / Int32ul,
        "StoreTime" / Int32ul
    )


@declare(guid=guid("a6ad76e3-867a-4635-91b3-4904ba6374d7"), event_id=4, version=1)
class Microsoft_Windows_Kernel_StoreMgr_4_1(Etw):
    pattern = Struct(
        "StoreKey" / Int64ul
    )


@declare(guid=guid("a6ad76e3-867a-4635-91b3-4904ba6374d7"), event_id=5, version=3)
class Microsoft_Windows_Kernel_StoreMgr_5_3(Etw):
    pattern = Struct(
        "StoreKey" / Int64ul,
        "StoreFileKey" / Int64ul,
        "UserDataMgr" / Int64ul,
        "MetadataMgr" / Int64ul,
        "RegionSize" / Int32ul,
        "RegionCount" / Int32ul,
        "BlockSize" / Int32ul,
        "SectorSize" / Int32ul,
        "EncryptionStrength" / Int32ul,
        "StoreType" / Int16ul,
        "StoreId" / Int16ul,
        "BlocksStored" / Int32ul,
        "RegionsInUse" / Int32ul,
        "TotalSpaceUsed" / Int32ul,
        "Flags" / Int32ul,
        "MetaRegionCount" / Int32ul,
        "MetaRegionsInUse" / Int32ul,
        "MetaRegionsSpaceUsed" / Int32ul,
        "StoreTime" / Int32ul
    )


@declare(guid=guid("a6ad76e3-867a-4635-91b3-4904ba6374d7"), event_id=6, version=1)
class Microsoft_Windows_Kernel_StoreMgr_6_1(Etw):
    pattern = Struct(
        "DataMgr" / Int64ul,
        "VirtualAddress" / Int64ul,
        "PhysicalAddress" / Int64ul,
        "Size" / Int16ul,
        "FileBacked" / Int8ul,
        "CorruptionType" / Int8ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("a6ad76e3-867a-4635-91b3-4904ba6374d7"), event_id=7, version=1)
class Microsoft_Windows_Kernel_StoreMgr_7_1(Etw):
    pattern = Struct(
        "DataKey" / Int32ul,
        "DataMgr" / Int64ul,
        "StoreOffset" / Int32ul,
        "CompressedSize" / Int16ul,
        "Flags" / Int16ul
    )


@declare(guid=guid("a6ad76e3-867a-4635-91b3-4904ba6374d7"), event_id=8, version=2)
class Microsoft_Windows_Kernel_StoreMgr_8_2(Etw):
    pattern = Struct(
        "DataMgr" / Int64ul,
        "RegionIndex" / Int32ul,
        "Status" / Int32ul,
        "SpaceUsed" / Int16ul,
        "LastAccessTime" / Int16ul
    )


@declare(guid=guid("a6ad76e3-867a-4635-91b3-4904ba6374d7"), event_id=9, version=2)
class Microsoft_Windows_Kernel_StoreMgr_9_2(Etw):
    pattern = Struct(
        "DataMgr" / Int64ul,
        "RegionIndex" / Int32ul,
        "Status" / Int32ul,
        "SpaceUsed" / Int16ul,
        "LastAccessTime" / Int16ul
    )


@declare(guid=guid("a6ad76e3-867a-4635-91b3-4904ba6374d7"), event_id=10, version=1)
class Microsoft_Windows_Kernel_StoreMgr_10_1(Etw):
    pattern = Struct(
        "FailReason" / Int32ul,
        "FailStatus" / Int32ul,
        "ObjectPathLength" / Int16ul,
        "ObjectPath" / Bytes(lambda this: this.ObjectPathLength)
    )


@declare(guid=guid("a6ad76e3-867a-4635-91b3-4904ba6374d7"), event_id=11, version=1)
class Microsoft_Windows_Kernel_StoreMgr_11_1(Etw):
    pattern = Struct(
        "StoreKey" / Int64ul,
        "Size" / Int32ul,
        "Data" / Bytes(lambda this: this.Size)
    )


@declare(guid=guid("a6ad76e3-867a-4635-91b3-4904ba6374d7"), event_id=12, version=1)
class Microsoft_Windows_Kernel_StoreMgr_12_1(Etw):
    pattern = Struct(
        "Size" / Int32ul,
        "Data" / Bytes(lambda this: this.Size)
    )


@declare(guid=guid("a6ad76e3-867a-4635-91b3-4904ba6374d7"), event_id=13, version=1)
class Microsoft_Windows_Kernel_StoreMgr_13_1(Etw):
    pattern = Struct(
        "StoreKey" / Int64ul,
        "Param" / Int64ul
    )


@declare(guid=guid("a6ad76e3-867a-4635-91b3-4904ba6374d7"), event_id=14, version=1)
class Microsoft_Windows_Kernel_StoreMgr_14_1(Etw):
    pattern = Struct(
        "DataMgr" / Int64ul,
        "RegionIndex" / Int32ul,
        "Status" / Int32ul,
        "SpaceUsed" / Int16ul,
        "LastAccessTime" / Int16ul
    )


@declare(guid=guid("a6ad76e3-867a-4635-91b3-4904ba6374d7"), event_id=15, version=1)
class Microsoft_Windows_Kernel_StoreMgr_15_1(Etw):
    pattern = Struct(
        "DataMgr" / Int64ul,
        "RegionIndex" / Int32ul,
        "Status" / Int32ul,
        "SpaceUsed" / Int16ul,
        "LastAccessTime" / Int16ul
    )


@declare(guid=guid("a6ad76e3-867a-4635-91b3-4904ba6374d7"), event_id=16, version=1)
class Microsoft_Windows_Kernel_StoreMgr_16_1(Etw):
    pattern = Struct(
        "DataMgr" / Int64ul,
        "RegionIndex" / Int32ul,
        "Status" / Int32ul,
        "SpaceUsed" / Int16ul,
        "LastAccessTime" / Int16ul
    )


@declare(guid=guid("a6ad76e3-867a-4635-91b3-4904ba6374d7"), event_id=17, version=1)
class Microsoft_Windows_Kernel_StoreMgr_17_1(Etw):
    pattern = Struct(
        "DataMgr" / Int64ul,
        "RegionIndex" / Int32ul,
        "Status" / Int32ul,
        "SpaceUsed" / Int16ul,
        "LastAccessTime" / Int16ul
    )


@declare(guid=guid("a6ad76e3-867a-4635-91b3-4904ba6374d7"), event_id=18, version=1)
class Microsoft_Windows_Kernel_StoreMgr_18_1(Etw):
    pattern = Struct(
        "Reason" / Int8ul,
        "FailStatus" / Int32ul,
        "DeviceDescLength" / Int16ul,
        "DeviceDescription" / Bytes(lambda this: this.DeviceDescLength),
        "ObjectPathLength" / Int16ul,
        "ObjectPath" / Bytes(lambda this: this.ObjectPathLength)
    )


@declare(guid=guid("a6ad76e3-867a-4635-91b3-4904ba6374d7"), event_id=19, version=0)
class Microsoft_Windows_Kernel_StoreMgr_19_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )

