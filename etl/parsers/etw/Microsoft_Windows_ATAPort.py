# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ATAPort
GUID : cb587ad1-cc35-4ef1-ad93-36cc82a2d319
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=0, version=0)
class Microsoft_Windows_ATAPort_0_0(Etw):
    pattern = Struct(
        "SCSIAddressSize" / Int32ul,
        "PortNumber" / Int8ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "DeviceType" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=1, version=0)
class Microsoft_Windows_ATAPort_1_0(Etw):
    pattern = Struct(
        "SCSIAddressSize" / Int32ul,
        "PortNumber" / Int8ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "DeviceType" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=100, version=0)
class Microsoft_Windows_ATAPort_100_0(Etw):
    pattern = Struct(
        "SCSIAddressSize" / Int32ul,
        "PortNumber" / Int8ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "DeviceType" / Int32ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=101, version=0)
class Microsoft_Windows_ATAPort_101_0(Etw):
    pattern = Struct(
        "SCSIAddressSize" / Int32ul,
        "PortNumber" / Int8ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "DeviceType" / Int32ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=102, version=0)
class Microsoft_Windows_ATAPort_102_0(Etw):
    pattern = Struct(
        "SCSIAddressSize" / Int32ul,
        "PortNumber" / Int8ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "DMAtoPIO" / Int8ul,
        "StepDownInDMAModes" / Int8ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=103, version=0)
class Microsoft_Windows_ATAPort_103_0(Etw):
    pattern = Struct(
        "DeviceAddress" / Int32ul,
        "RequestSequence" / Int32ul,
        "QueueTime" / Int64ul,
        "DeviceTime" / Int64ul,
        "MasterIRP" / Int64ul,
        "ActiveRequestCount" / Int32ul,
        "IRBFunction" / Int16ul,
        "DeviceCommand" / Int8ul,
        "IRBStatus" / Int8ul,
        "ATAStatus" / Int8ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=104, version=0)
class Microsoft_Windows_ATAPort_104_0(Etw):
    pattern = Struct(
        "DeviceAddress" / Int32ul,
        "RequestSequence" / Int32ul,
        "QueueTime" / Int64ul,
        "DeviceTime" / Int64ul,
        "MasterIRP" / Int64ul,
        "ActiveRequestCount" / Int32ul,
        "IRBFunction" / Int16ul,
        "DeviceCommand" / Int8ul,
        "IRBStatus" / Int8ul,
        "ATAStatus" / Int8ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=105, version=0)
class Microsoft_Windows_ATAPort_105_0(Etw):
    pattern = Struct(
        "DeviceAddress" / Int32ul,
        "RequestSequence" / Int32ul,
        "QueueTime" / Int64ul,
        "DeviceTime" / Int64ul,
        "MasterIRP" / Int64ul,
        "ActiveRequestCount" / Int32ul,
        "IRBFunction" / Int16ul,
        "DeviceCommand" / Int8ul,
        "IRBStatus" / Int8ul,
        "ATAStatus" / Int8ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=106, version=0)
class Microsoft_Windows_ATAPort_106_0(Etw):
    pattern = Struct(
        "SCSIAddressSize" / Int32ul,
        "PortNumber" / Int8ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "DeviceType" / Int32ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=107, version=0)
class Microsoft_Windows_ATAPort_107_0(Etw):
    pattern = Struct(
        "SCSIAddressSize" / Int32ul,
        "PortNumber" / Int8ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "DeviceType" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=108, version=0)
class Microsoft_Windows_ATAPort_108_0(Etw):
    pattern = Struct(
        "SCSIAddressSize" / Int32ul,
        "PortNumber" / Int8ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "DeviceType" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=109, version=0)
class Microsoft_Windows_ATAPort_109_0(Etw):
    pattern = Struct(
        "SCSIAddressSize" / Int32ul,
        "PortNumber" / Int8ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "DeviceType" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=110, version=0)
class Microsoft_Windows_ATAPort_110_0(Etw):
    pattern = Struct(
        "SCSIAddressSize" / Int32ul,
        "PortNumber" / Int8ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "DeviceType" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=113, version=0)
class Microsoft_Windows_ATAPort_113_0(Etw):
    pattern = Struct(
        "SCSIAddressSize" / Int32ul,
        "PortNumber" / Int8ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "DeviceType" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=113, version=1)
class Microsoft_Windows_ATAPort_113_1(Etw):
    pattern = Struct(
        "PortNumber" / Int8ul,
        "BusNumber" / Int8ul,
        "TargetId" / Int8ul,
        "LUN" / Int8ul,
        "FailureReason" / Int32ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=114, version=0)
class Microsoft_Windows_ATAPort_114_0(Etw):
    pattern = Struct(
        "SCSIAddressSize" / Int32ul,
        "PortNumber" / Int8ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "DeviceType" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=114, version=1)
class Microsoft_Windows_ATAPort_114_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "TransferModeChangeType" / Int8ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=200, version=1)
class Microsoft_Windows_ATAPort_200_1(Etw):
    pattern = Struct(
        "RequestDurationin100ns" / Int64ul,
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "SrbStatus" / Int8ul,
        "OriginalIrp" / Int64ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=201, version=1)
class Microsoft_Windows_ATAPort_201_1(Etw):
    pattern = Struct(
        "RequestDurationin100ns" / Int64ul,
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "SrbStatus" / Int8ul,
        "OriginalIrp" / Int64ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=202, version=1)
class Microsoft_Windows_ATAPort_202_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransferinbytes" / Int64ul,
        "LBA" / Int64ul,
        "OriginalIrp" / Int64ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=203, version=1)
class Microsoft_Windows_ATAPort_203_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransferinbytes" / Int64ul,
        "LBA" / Int64ul,
        "OriginalIrp" / Int64ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=204, version=1)
class Microsoft_Windows_ATAPort_204_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransferinbytes" / Int64ul,
        "LBA" / Int64ul,
        "OriginalIrp" / Int64ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=205, version=1)
class Microsoft_Windows_ATAPort_205_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransferinbytes" / Int64ul,
        "LBA" / Int64ul,
        "OriginalIrp" / Int64ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=206, version=1)
class Microsoft_Windows_ATAPort_206_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransferinbytes" / Int64ul,
        "LBA" / Int64ul,
        "OriginalIrp" / Int64ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=207, version=1)
class Microsoft_Windows_ATAPort_207_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransferinbytes" / Int64ul,
        "LBA" / Int64ul,
        "OriginalIrp" / Int64ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=208, version=1)
class Microsoft_Windows_ATAPort_208_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "NTStatus" / Int32ul,
        "SrbStatus" / Int8ul,
        "ScsiStatus" / Int8ul,
        "SenseKey" / Int8ul,
        "AddSense" / Int8ul,
        "AddSenseQ" / Int8ul,
        "OriginalIrp" / Int64ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=209, version=1)
class Microsoft_Windows_ATAPort_209_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "CurrentRetryCount" / Int32ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=210, version=1)
class Microsoft_Windows_ATAPort_210_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=211, version=1)
class Microsoft_Windows_ATAPort_211_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "NTStatus" / Int32ul,
        "SrbStatus" / Int8ul,
        "ScsiStatus" / Int8ul,
        "SenseKey" / Int8ul,
        "AddSense" / Int8ul,
        "AddSenseQ" / Int8ul,
        "OriginalIrp" / Int64ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=212, version=1)
class Microsoft_Windows_ATAPort_212_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "MajorFunction" / Int32ul,
        "MinorFunction" / Int32ul,
        "Parameter" / Int32ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=213, version=1)
class Microsoft_Windows_ATAPort_213_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "MajorFunction" / Int32ul,
        "MinorFunction" / Int32ul,
        "Parameter" / Int32ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=214, version=1)
class Microsoft_Windows_ATAPort_214_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=215, version=1)
class Microsoft_Windows_ATAPort_215_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "MinorFunction" / Int32ul,
        "Type" / Int8ul,
        "OldState" / Int32ul,
        "NewState" / Int32ul,
        "Action" / Int32ul,
        "PowerStateContext" / Int32ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=216, version=1)
class Microsoft_Windows_ATAPort_216_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=217, version=1)
class Microsoft_Windows_ATAPort_217_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "MinorFunction" / Int32ul,
        "Type" / Int32ul,
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=218, version=1)
class Microsoft_Windows_ATAPort_218_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=219, version=1)
class Microsoft_Windows_ATAPort_219_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "NumberOfChildren" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=220, version=1)
class Microsoft_Windows_ATAPort_220_1(Etw):
    pattern = Struct(
        "QueueTag" / Int32ul,
        "Operation" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("cb587ad1-cc35-4ef1-ad93-36cc82a2d319"), event_id=221, version=1)
class Microsoft_Windows_ATAPort_221_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "MajorFunction" / Int32ul,
        "MinorFunction" / Int32ul,
        "Parameter" / Int32ul
    )

