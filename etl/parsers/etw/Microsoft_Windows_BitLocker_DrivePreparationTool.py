# -*- coding: utf-8 -*-
"""
Microsoft-Windows-BitLocker-DrivePreparationTool
GUID : 632f767e-0ec3-47b9-ba1c-a0e62a74728a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("632f767e-0ec3-47b9-ba1c-a0e62a74728a"), event_id=1, version=1)
class Microsoft_Windows_BitLocker_DrivePreparationTool_1_1(Etw):
    pattern = Struct(
        "MessageCode" / Int32ul,
        "MessageText" / WString
    )


@declare(guid=guid("632f767e-0ec3-47b9-ba1c-a0e62a74728a"), event_id=2, version=1)
class Microsoft_Windows_BitLocker_DrivePreparationTool_2_1(Etw):
    pattern = Struct(
        "MessageCode" / Int32ul,
        "MessageText" / WString
    )


@declare(guid=guid("632f767e-0ec3-47b9-ba1c-a0e62a74728a"), event_id=3, version=1)
class Microsoft_Windows_BitLocker_DrivePreparationTool_3_1(Etw):
    pattern = Struct(
        "MessageCode" / Int32ul,
        "MessageText" / WString
    )


@declare(guid=guid("632f767e-0ec3-47b9-ba1c-a0e62a74728a"), event_id=4, version=1)
class Microsoft_Windows_BitLocker_DrivePreparationTool_4_1(Etw):
    pattern = Struct(
        "MessageCode" / Int32ul,
        "MessageText" / WString
    )


@declare(guid=guid("632f767e-0ec3-47b9-ba1c-a0e62a74728a"), event_id=5, version=1)
class Microsoft_Windows_BitLocker_DrivePreparationTool_5_1(Etw):
    pattern = Struct(
        "MessageCode" / Int32ul,
        "MessageText" / WString
    )


@declare(guid=guid("632f767e-0ec3-47b9-ba1c-a0e62a74728a"), event_id=256, version=1)
class Microsoft_Windows_BitLocker_DrivePreparationTool_256_1(Etw):
    pattern = Struct(
        "MessageCode" / Int32ul,
        "MessageText" / WString
    )


@declare(guid=guid("632f767e-0ec3-47b9-ba1c-a0e62a74728a"), event_id=4096, version=1)
class Microsoft_Windows_BitLocker_DrivePreparationTool_4096_1(Etw):
    pattern = Struct(
        "Shrinkable" / Int8ul,
        "ContainsWinRE" / Int8ul,
        "VolumeName" / WString,
        "VolumeSize" / Int64ul,
        "VolumeFreeSpace" / Int64ul,
        "VolumeMaxShrinkSize" / Int64ul,
        "VolumeFlags" / Int32ul,
        "DriveLetter" / WString,
        "DiskNumber" / Int32ul,
        "PartitionNumber" / Int32ul
    )


@declare(guid=guid("632f767e-0ec3-47b9-ba1c-a0e62a74728a"), event_id=4097, version=1)
class Microsoft_Windows_BitLocker_DrivePreparationTool_4097_1(Etw):
    pattern = Struct(
        "DiskId" / Guid,
        "Type" / Int32ul,
        "Offset" / Int64ul,
        "Size" / Int64ul,
        "VolumeId" / Guid
    )


@declare(guid=guid("632f767e-0ec3-47b9-ba1c-a0e62a74728a"), event_id=4098, version=1)
class Microsoft_Windows_BitLocker_DrivePreparationTool_4098_1(Etw):
    pattern = Struct(
        "DiskId" / Guid,
        "Type" / Int32ul,
        "Offset" / Int64ul,
        "Size" / Int64ul,
        "VolumeId" / Guid
    )


@declare(guid=guid("632f767e-0ec3-47b9-ba1c-a0e62a74728a"), event_id=4099, version=1)
class Microsoft_Windows_BitLocker_DrivePreparationTool_4099_1(Etw):
    pattern = Struct(
        "RawCommandLine" / WString,
        "ShowUsage" / Int8ul,
        "DisplayDriveInfo" / Int8ul,
        "TargetDriveLetter" / WString,
        "TargetAction" / Int32ul,
        "NewSystemDriveLetter" / WString,
        "ShrinkSize" / Int64sl,
        "QuietMode" / Int8ul,
        "AutoRestart" / Int8ul
    )


@declare(guid=guid("632f767e-0ec3-47b9-ba1c-a0e62a74728a"), event_id=4100, version=1)
class Microsoft_Windows_BitLocker_DrivePreparationTool_4100_1(Etw):
    pattern = Struct(
        "VolumeName" / WString,
        "DriveLetter" / WString,
        "DiskNumber" / Int32ul,
        "PartitionNumber" / Int32ul,
        "ShrinkSize" / Int64ul,
        "NewDriveLetter" / WString
    )


@declare(guid=guid("632f767e-0ec3-47b9-ba1c-a0e62a74728a"), event_id=4101, version=1)
class Microsoft_Windows_BitLocker_DrivePreparationTool_4101_1(Etw):
    pattern = Struct(
        "ExtentOffset" / Int64ul,
        "NewPartitionSize" / Int64ul,
        "NewDriveLetter" / WString
    )


@declare(guid=guid("632f767e-0ec3-47b9-ba1c-a0e62a74728a"), event_id=4102, version=1)
class Microsoft_Windows_BitLocker_DrivePreparationTool_4102_1(Etw):
    pattern = Struct(
        "VolumeName" / WString,
        "DriveLetter" / WString,
        "DiskNumber" / Int32ul,
        "PartitionNumber" / Int32ul
    )


@declare(guid=guid("632f767e-0ec3-47b9-ba1c-a0e62a74728a"), event_id=4103, version=1)
class Microsoft_Windows_BitLocker_DrivePreparationTool_4103_1(Etw):
    pattern = Struct(
        "WinREVolumeName" / WString,
        "DriveLetter" / WString,
        "DiskNumber" / Int32ul,
        "PartitionNumber" / Int32ul
    )


@declare(guid=guid("632f767e-0ec3-47b9-ba1c-a0e62a74728a"), event_id=4104, version=1)
class Microsoft_Windows_BitLocker_DrivePreparationTool_4104_1(Etw):
    pattern = Struct(
        "MessageCode" / Int32ul,
        "MessageText" / WString,
        "VolumeName" / WString,
        "DriveLetter" / WString,
        "DiskNumber" / Int32ul,
        "PartitionNumber" / Int32ul
    )

