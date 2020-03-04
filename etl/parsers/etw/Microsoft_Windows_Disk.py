# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Disk
GUID : 6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=1, version=1)
class Microsoft_Windows_Disk_1_1(Etw):
    pattern = Struct(
        "ReadCacheEnabled" / Int8ul,
        "WriteCacheEnabled" / Int8ul,
        "ReadRetentionPriority" / Int8ul,
        "WriteRetentionPriority" / Int8ul,
        "PrefetchScalar" / Int8ul,
        "DisablePrefetchTransferLength" / Int16ul,
        "Minimum" / Int16ul,
        "Maximum" / Int16ul,
        "MaximumBlocks" / Int16ul,
        "DeviceNumber" / Int32ul
    )


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=201, version=1)
class Microsoft_Windows_Disk_201_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "RequestDuration" / Int64ul,
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "SrbStatus" / Int8ul
    )


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=202, version=1)
class Microsoft_Windows_Disk_202_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransfer" / Int64ul,
        "LBA" / Int64ul
    )


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=203, version=1)
class Microsoft_Windows_Disk_203_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransfer" / Int64ul,
        "LBA" / Int64ul
    )


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=204, version=1)
class Microsoft_Windows_Disk_204_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransfer" / Int64ul,
        "LBA" / Int64ul
    )


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=205, version=1)
class Microsoft_Windows_Disk_205_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransfer" / Int64ul,
        "LBA" / Int64ul
    )


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=206, version=1)
class Microsoft_Windows_Disk_206_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransfer" / Int64ul,
        "LBA" / Int64ul
    )


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=207, version=1)
class Microsoft_Windows_Disk_207_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransfer" / Int64ul,
        "LBA" / Int64ul
    )


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=208, version=1)
class Microsoft_Windows_Disk_208_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "NTStatus" / Int32ul,
        "SrbStatus" / Int8ul,
        "ScsiStatus" / Int8ul,
        "SenseKey" / Int8ul,
        "AddSense" / Int8ul,
        "AddSenseQ" / Int8ul
    )


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=209, version=1)
class Microsoft_Windows_Disk_209_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "CurrentRetryCount" / Int32ul
    )


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=210, version=1)
class Microsoft_Windows_Disk_210_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul
    )


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=211, version=1)
class Microsoft_Windows_Disk_211_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "NTStatus" / Int32ul,
        "SrbStatus" / Int8ul,
        "ScsiStatus" / Int8ul,
        "SenseKey" / Int8ul,
        "AddSense" / Int8ul,
        "AddSenseQ" / Int8ul
    )


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=212, version=1)
class Microsoft_Windows_Disk_212_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "MajorFunction" / Int32ul,
        "MinorFunction" / Int32ul,
        "Parameter" / Int32ul
    )


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=213, version=1)
class Microsoft_Windows_Disk_213_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "MajorFunction" / Int32ul,
        "MinorFunction" / Int32ul,
        "Parameter" / Int32ul
    )


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=214, version=1)
class Microsoft_Windows_Disk_214_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=215, version=1)
class Microsoft_Windows_Disk_215_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "MinorFunction" / Int32ul,
        "Type" / Int8ul,
        "OldState" / Int32ul,
        "NewState" / Int32ul,
        "Action" / Int32ul,
        "PowerStateContext" / Int32ul
    )


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=216, version=1)
class Microsoft_Windows_Disk_216_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=217, version=1)
class Microsoft_Windows_Disk_217_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "MinorFunction" / Int32ul,
        "Type" / Int32ul,
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=218, version=1)
class Microsoft_Windows_Disk_218_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=219, version=1)
class Microsoft_Windows_Disk_219_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "NumberOfChildren" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=220, version=1)
class Microsoft_Windows_Disk_220_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "QueueTag" / Int32ul,
        "Operation" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("6b4db0bc-9a3d-467d-81b9-a84c6f2f3d40"), event_id=221, version=1)
class Microsoft_Windows_Disk_221_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "MajorFunction" / Int32ul,
        "MinorFunction" / Int32ul,
        "Parameter" / Int32ul
    )

