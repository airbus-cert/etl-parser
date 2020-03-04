# -*- coding: utf-8 -*-
"""
Microsoft-Windows-PersistentMemory-PmemDisk
GUID : 0fa2ee03-1feb-5057-3bb3-eb25521b8482
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=1, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_1_0(Etw):
    pattern = Struct(
        "StartAddress" / Int64ul,
        "Size" / Int64ul
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=2, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_2_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "DeviceNumber" / Int32ul,
        "RequestDuration" / Int64ul,
        "Irp" / Int64ul,
        "IsWrite" / Int8ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=3, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_3_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "DeviceNumber" / Int32ul,
        "RequestDuration" / Int64ul,
        "Irp" / Int64ul,
        "IsWrite" / Int8ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=101, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_101_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "IRPMJ" / Int8ul,
        "LengthOfTransfer" / Int64ul,
        "LBA" / Int64ul
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=102, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_102_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "IRPMJ" / Int8ul,
        "LengthOfTransfer" / Int64ul,
        "LBA" / Int64ul
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=103, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_103_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "IRPMJ" / Int8ul,
        "LengthOfTransfer" / Int64ul,
        "LBA" / Int64ul
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=104, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_104_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "IRPMJ" / Int8ul,
        "LengthOfTransfer" / Int64ul,
        "LBA" / Int64ul
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=105, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_105_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "NTStatus" / Int32ul
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=106, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_106_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "MajorFunction" / Int32ul,
        "MinorFunction" / Int32ul,
        "Parameter" / Int32ul
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=107, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_107_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=108, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_108_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "MinorFunction" / Int32ul,
        "Type" / Int32ul,
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=109, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_109_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=202, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_202_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "Reason" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=203, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_203_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=204, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_204_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=205, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_205_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=206, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_206_0(Etw):
    pattern = Struct(
        "LogicalPersistentMemoryDiskGuid" / Guid,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "PhysicalNvdimmGuid" / Guid,
        "NfitHandle" / Int32ul,
        "NvdimmHealthStatus" / Int32ul
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=207, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_207_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=209, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_209_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=211, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_211_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=212, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_212_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=213, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_213_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=214, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_214_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=215, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_215_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "Message" / CString
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=300, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_300_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=301, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_301_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=302, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_302_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid
    )


@declare(guid=guid("0fa2ee03-1feb-5057-3bb3-eb25521b8482"), event_id=900, version=0)
class Microsoft_Windows_PersistentMemory_PmemDisk_900_0(Etw):
    pattern = Struct(
        "PersistentMemoryDiskGuid" / Guid,
        "Message" / CString
    )

