# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WHEA-Logger
GUID : c26c4f3c-3f66-4e99-8f8a-39405cfed220
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=1, version=0)
class Microsoft_Windows_WHEA_Logger_1_0(Etw):
    pattern = Struct(
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=2, version=0)
class Microsoft_Windows_WHEA_Logger_2_0(Etw):
    pattern = Struct(
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=3, version=0)
class Microsoft_Windows_WHEA_Logger_3_0(Etw):
    pattern = Struct(
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=16, version=0)
class Microsoft_Windows_WHEA_Logger_16_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "FRUId" / Guid,
        "FRUText" / CString,
        "ValidBits" / Int64ul,
        "PortType" / Int32ul,
        "Version" / Int32ul,
        "Command" / Int32ul,
        "Status" / Int32ul,
        "Bus" / Int32ul,
        "Device" / Int32ul,
        "Function" / Int32ul,
        "Segment" / Int32ul,
        "SecondaryBus" / Int32ul,
        "Slot" / Int32ul,
        "VendorID" / Int32ul,
        "DeviceID" / Int32ul,
        "ClassCode" / Int32ul,
        "DeviceSerialNumber" / Int64ul,
        "BridgeControl" / Int32ul,
        "BridgeStatus" / Int32ul,
        "UncorrectableErrorStatus" / Int32ul,
        "CorrectableErrorStatus" / Int32ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=16, version=1)
class Microsoft_Windows_WHEA_Logger_16_1(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "FRUId" / Guid,
        "FRUText" / CString,
        "ValidBits" / Int64ul,
        "PortType" / Int32ul,
        "Version" / Int32ul,
        "Command" / Int32ul,
        "Status" / Int32ul,
        "Bus" / Int32ul,
        "Device" / Int32ul,
        "Function" / Int32ul,
        "Segment" / Int32ul,
        "SecondaryBus" / Int32ul,
        "SecondaryDevice" / Int32ul,
        "SecondaryFunction" / Int32ul,
        "VendorID" / Int32ul,
        "DeviceID" / Int32ul,
        "ClassCode" / Int32ul,
        "DeviceSerialNumber" / Int64ul,
        "BridgeControl" / Int32ul,
        "BridgeStatus" / Int32ul,
        "UncorrectableErrorStatus" / Int32ul,
        "CorrectableErrorStatus" / Int32ul,
        "PrimaryDeviceName" / WString,
        "SecondaryDeviceName" / WString
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=17, version=0)
class Microsoft_Windows_WHEA_Logger_17_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "FRUId" / Guid,
        "FRUText" / CString,
        "ValidBits" / Int64ul,
        "PortType" / Int32ul,
        "Version" / Int32ul,
        "Command" / Int32ul,
        "Status" / Int32ul,
        "Bus" / Int32ul,
        "Device" / Int32ul,
        "Function" / Int32ul,
        "Segment" / Int32ul,
        "SecondaryBus" / Int32ul,
        "Slot" / Int32ul,
        "VendorID" / Int32ul,
        "DeviceID" / Int32ul,
        "ClassCode" / Int32ul,
        "DeviceSerialNumber" / Int64ul,
        "BridgeControl" / Int32ul,
        "BridgeStatus" / Int32ul,
        "UncorrectableErrorStatus" / Int32ul,
        "CorrectableErrorStatus" / Int32ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=17, version=1)
class Microsoft_Windows_WHEA_Logger_17_1(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "FRUId" / Guid,
        "FRUText" / CString,
        "ValidBits" / Int64ul,
        "PortType" / Int32ul,
        "Version" / Int32ul,
        "Command" / Int32ul,
        "Status" / Int32ul,
        "Bus" / Int32ul,
        "Device" / Int32ul,
        "Function" / Int32ul,
        "Segment" / Int32ul,
        "SecondaryBus" / Int32ul,
        "SecondaryDevice" / Int32ul,
        "SecondaryFunction" / Int32ul,
        "VendorID" / Int32ul,
        "DeviceID" / Int32ul,
        "ClassCode" / Int32ul,
        "DeviceSerialNumber" / Int64ul,
        "BridgeControl" / Int32ul,
        "BridgeStatus" / Int32ul,
        "UncorrectableErrorStatus" / Int32ul,
        "CorrectableErrorStatus" / Int32ul,
        "PrimaryDeviceName" / WString,
        "SecondaryDeviceName" / WString
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=18, version=0)
class Microsoft_Windows_WHEA_Logger_18_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "ApicId" / Int32ul,
        "MCABank" / Int32ul,
        "MciStat" / Int64ul,
        "MciAddr" / Int64ul,
        "MciMisc" / Int64ul,
        "ErrorType" / Int32ul,
        "TransactionType" / Int32ul,
        "Participation" / Int32ul,
        "RequestType" / Int32ul,
        "MemorIO" / Int32ul,
        "MemHierarchyLvl" / Int32ul,
        "Timeout" / Int32ul,
        "OperationType" / Int32ul,
        "Channel" / Int32ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=19, version=0)
class Microsoft_Windows_WHEA_Logger_19_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "ApicId" / Int32ul,
        "MCABank" / Int32ul,
        "MciStat" / Int64ul,
        "MciAddr" / Int64ul,
        "MciMisc" / Int64ul,
        "ErrorType" / Int32ul,
        "TransactionType" / Int32ul,
        "Participation" / Int32ul,
        "RequestType" / Int32ul,
        "MemorIO" / Int32ul,
        "MemHierarchyLvl" / Int32ul,
        "Timeout" / Int32ul,
        "OperationType" / Int32ul,
        "Channel" / Int32ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=20, version=0)
class Microsoft_Windows_WHEA_Logger_20_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "ApicId" / Int32ul,
        "MCABank" / Int32ul,
        "MciStat" / Int64ul,
        "MciAddr" / Int64ul,
        "MciMisc" / Int64ul,
        "ErrorType" / Int32ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=21, version=0)
class Microsoft_Windows_WHEA_Logger_21_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "ApicId" / Int32ul,
        "MCABank" / Int32ul,
        "MciStat" / Int64ul,
        "MciAddr" / Int64ul,
        "MciMisc" / Int64ul,
        "ErrorType" / Int32ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=22, version=0)
class Microsoft_Windows_WHEA_Logger_22_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "FRUId" / Guid,
        "FRUText" / CString,
        "ValidBits" / Int64ul,
        "ErrorStatus" / Int64ul,
        "PhysicalAddress" / Int64ul,
        "PhysicalAddressMask" / Int64ul,
        "Node" / Int32ul,
        "Card" / Int32ul,
        "Module" / Int32ul,
        "Bank" / Int32ul,
        "Device" / Int32ul,
        "Row" / Int32ul,
        "Column" / Int32ul,
        "BitPosition" / Int32ul,
        "RequesterId" / Int64ul,
        "ResponderId" / Int64ul,
        "TargetId" / Int64ul,
        "ErrorType" / Int8ul,
        "Extended" / Int32ul,
        "RankNumber" / Int32ul,
        "CardHandle" / Int32ul,
        "ModuleHandle" / Int32ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=23, version=0)
class Microsoft_Windows_WHEA_Logger_23_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "FRUId" / Guid,
        "FRUText" / CString,
        "ValidBits" / Int64ul,
        "ErrorStatus" / Int64ul,
        "PhysicalAddress" / Int64ul,
        "PhysicalAddressMask" / Int64ul,
        "Node" / Int32ul,
        "Card" / Int32ul,
        "Module" / Int32ul,
        "Bank" / Int32ul,
        "Device" / Int32ul,
        "Row" / Int32ul,
        "Column" / Int32ul,
        "BitPosition" / Int32ul,
        "RequesterId" / Int64ul,
        "ResponderId" / Int64ul,
        "TargetId" / Int64ul,
        "ErrorType" / Int8ul,
        "Extended" / Int32ul,
        "RankNumber" / Int32ul,
        "CardHandle" / Int32ul,
        "ModuleHandle" / Int32ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=24, version=0)
class Microsoft_Windows_WHEA_Logger_24_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "FRUId" / Guid,
        "FRUText" / CString,
        "ValidBits" / Int64ul,
        "ErrorType" / Int16ul,
        "BusNumber" / Int32ul,
        "BusSegment" / Int32ul,
        "BusAddress" / Int64ul,
        "BusData" / Int64ul,
        "Command" / Int64ul,
        "PCIXCommand" / Int8ul,
        "RequesterId" / Int64ul,
        "CompleterId" / Int64ul,
        "TargetId" / Int64ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=25, version=0)
class Microsoft_Windows_WHEA_Logger_25_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "FRUId" / Guid,
        "FRUText" / CString,
        "ValidBits" / Int64ul,
        "ErrorType" / Int16ul,
        "BusNumber" / Int32ul,
        "BusSegment" / Int32ul,
        "BusAddress" / Int64ul,
        "BusData" / Int64ul,
        "Command" / Int64ul,
        "PCIXCommand" / Int8ul,
        "RequesterId" / Int64ul,
        "CompleterId" / Int64ul,
        "TargetId" / Int64ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=26, version=0)
class Microsoft_Windows_WHEA_Logger_26_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "FRUId" / Guid,
        "FRUText" / CString,
        "ValidBits" / Int64ul,
        "ErrorType" / Int8ul,
        "VendorId" / Int32ul,
        "DeviceId" / Int32ul,
        "ClassCode" / Int32ul,
        "FunctionNumber" / Int32ul,
        "DeviceNumber" / Int32ul,
        "BusNumber" / Int32ul,
        "SegmentNumber" / Int32ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=27, version=0)
class Microsoft_Windows_WHEA_Logger_27_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "FRUId" / Guid,
        "FRUText" / CString,
        "ValidBits" / Int64ul,
        "ErrorType" / Int8ul,
        "VendorId" / Int32ul,
        "DeviceId" / Int32ul,
        "ClassCode" / Int32ul,
        "FunctionNumber" / Int32ul,
        "DeviceNumber" / Int32ul,
        "BusNumber" / Int32ul,
        "SegmentNumber" / Int32ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=28, version=0)
class Microsoft_Windows_WHEA_Logger_28_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "MPIDR_EL1" / Int64ul,
        "MIDR_EL1" / Int64ul,
        "RunningState" / Int32ul,
        "PSCIState" / Int32ul,
        "ErrorType" / Int32ul,
        "TransactionType" / Int32ul,
        "Participation" / Int32ul,
        "CacheLevel" / Int32ul,
        "AffinityLevel" / Int32ul,
        "Timeout" / Int32ul,
        "OperationType" / Int32ul,
        "TLBOperationType" / Int32ul,
        "AddressSpace" / Int32ul,
        "AccessMode" / Int32ul,
        "PrecisePC" / Int32ul,
        "RestartablePC" / Int32ul,
        "VirtualFaultAddress" / Int64ul,
        "PhysicalFaultAddress" / Int64ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=29, version=0)
class Microsoft_Windows_WHEA_Logger_29_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "MPIDR_EL1" / Int64ul,
        "MIDR_EL1" / Int64ul,
        "RunningState" / Int32ul,
        "PSCIState" / Int32ul,
        "ErrorType" / Int32ul,
        "TransactionType" / Int32ul,
        "Participation" / Int32ul,
        "CacheLevel" / Int32ul,
        "AffinityLevel" / Int32ul,
        "Timeout" / Int32ul,
        "OperationType" / Int32ul,
        "TLBOperationType" / Int32ul,
        "AddressSpace" / Int32ul,
        "AccessMode" / Int32ul,
        "PrecisePC" / Int32ul,
        "RestartablePC" / Int32ul,
        "VirtualFaultAddress" / Int64ul,
        "PhysicalFaultAddress" / Int64ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=40, version=0)
class Microsoft_Windows_WHEA_Logger_40_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "FRUId" / Guid,
        "FRUText" / CString,
        "ValidBits" / Int64ul,
        "PortType" / Int32ul,
        "Version" / Int32ul,
        "Command" / Int32ul,
        "Status" / Int32ul,
        "Bus" / Int32ul,
        "Device" / Int32ul,
        "Function" / Int32ul,
        "Segment" / Int32ul,
        "SecondaryBus" / Int32ul,
        "Slot" / Int32ul,
        "VendorID" / Int32ul,
        "DeviceID" / Int32ul,
        "ClassCode" / Int32ul,
        "DeviceSerialNumber" / Int64ul,
        "BridgeControl" / Int32ul,
        "BridgeStatus" / Int32ul,
        "UncorrectableErrorStatus" / Int32ul,
        "CorrectableErrorStatus" / Int32ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=40, version=1)
class Microsoft_Windows_WHEA_Logger_40_1(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "FRUId" / Guid,
        "FRUText" / CString,
        "ValidBits" / Int64ul,
        "PortType" / Int32ul,
        "Version" / Int32ul,
        "Command" / Int32ul,
        "Status" / Int32ul,
        "Bus" / Int32ul,
        "Device" / Int32ul,
        "Function" / Int32ul,
        "Segment" / Int32ul,
        "SecondaryBus" / Int32ul,
        "SecondaryDevice" / Int32ul,
        "SecondaryFunction" / Int32ul,
        "VendorID" / Int32ul,
        "DeviceID" / Int32ul,
        "ClassCode" / Int32ul,
        "DeviceSerialNumber" / Int64ul,
        "BridgeControl" / Int32ul,
        "BridgeStatus" / Int32ul,
        "UncorrectableErrorStatus" / Int32ul,
        "CorrectableErrorStatus" / Int32ul,
        "PrimaryDeviceName" / WString,
        "SecondaryDeviceName" / WString
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=41, version=0)
class Microsoft_Windows_WHEA_Logger_41_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "FRUId" / Guid,
        "FRUText" / CString,
        "ValidBits" / Int64ul,
        "PortType" / Int32ul,
        "Version" / Int32ul,
        "Command" / Int32ul,
        "Status" / Int32ul,
        "Bus" / Int32ul,
        "Device" / Int32ul,
        "Function" / Int32ul,
        "Segment" / Int32ul,
        "SecondaryBus" / Int32ul,
        "Slot" / Int32ul,
        "VendorID" / Int32ul,
        "DeviceID" / Int32ul,
        "ClassCode" / Int32ul,
        "DeviceSerialNumber" / Int64ul,
        "BridgeControl" / Int32ul,
        "BridgeStatus" / Int32ul,
        "UncorrectableErrorStatus" / Int32ul,
        "CorrectableErrorStatus" / Int32ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=41, version=1)
class Microsoft_Windows_WHEA_Logger_41_1(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "FRUId" / Guid,
        "FRUText" / CString,
        "ValidBits" / Int64ul,
        "PortType" / Int32ul,
        "Version" / Int32ul,
        "Command" / Int32ul,
        "Status" / Int32ul,
        "Bus" / Int32ul,
        "Device" / Int32ul,
        "Function" / Int32ul,
        "Segment" / Int32ul,
        "SecondaryBus" / Int32ul,
        "SecondaryDevice" / Int32ul,
        "SecondaryFunction" / Int32ul,
        "VendorID" / Int32ul,
        "DeviceID" / Int32ul,
        "ClassCode" / Int32ul,
        "DeviceSerialNumber" / Int64ul,
        "BridgeControl" / Int32ul,
        "BridgeStatus" / Int32ul,
        "UncorrectableErrorStatus" / Int32ul,
        "CorrectableErrorStatus" / Int32ul,
        "PrimaryDeviceName" / WString,
        "SecondaryDeviceName" / WString
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=42, version=0)
class Microsoft_Windows_WHEA_Logger_42_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "FRUId" / Guid,
        "FRUText" / CString,
        "ValidBits" / Int64ul,
        "ErrorType" / Int16ul,
        "BusNumber" / Int32ul,
        "BusSegment" / Int32ul,
        "BusAddress" / Int64ul,
        "BusData" / Int64ul,
        "Command" / Int64ul,
        "PCIXCommand" / Int8ul,
        "RequesterId" / Int64ul,
        "CompleterId" / Int64ul,
        "TargetId" / Int64ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=43, version=0)
class Microsoft_Windows_WHEA_Logger_43_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "FRUId" / Guid,
        "FRUText" / CString,
        "ValidBits" / Int64ul,
        "ErrorType" / Int16ul,
        "BusNumber" / Int32ul,
        "BusSegment" / Int32ul,
        "BusAddress" / Int64ul,
        "BusData" / Int64ul,
        "Command" / Int64ul,
        "PCIXCommand" / Int8ul,
        "RequesterId" / Int64ul,
        "CompleterId" / Int64ul,
        "TargetId" / Int64ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=44, version=0)
class Microsoft_Windows_WHEA_Logger_44_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "FRUId" / Guid,
        "FRUText" / CString,
        "ValidBits" / Int64ul,
        "ErrorType" / Int8ul,
        "VendorId" / Int32ul,
        "DeviceId" / Int32ul,
        "ClassCode" / Int32ul,
        "FunctionNumber" / Int32ul,
        "DeviceNumber" / Int32ul,
        "BusNumber" / Int32ul,
        "SegmentNumber" / Int32ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=45, version=0)
class Microsoft_Windows_WHEA_Logger_45_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "FRUId" / Guid,
        "FRUText" / CString,
        "ValidBits" / Int64ul,
        "ErrorType" / Int8ul,
        "VendorId" / Int32ul,
        "DeviceId" / Int32ul,
        "ClassCode" / Int32ul,
        "FunctionNumber" / Int32ul,
        "DeviceNumber" / Int32ul,
        "BusNumber" / Int32ul,
        "SegmentNumber" / Int32ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=46, version=0)
class Microsoft_Windows_WHEA_Logger_46_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "FRUId" / Guid,
        "FRUText" / CString,
        "ValidBits" / Int64ul,
        "ErrorStatus" / Int64ul,
        "PhysicalAddress" / Int64ul,
        "PhysicalAddressMask" / Int64ul,
        "Node" / Int32ul,
        "Card" / Int32ul,
        "Module" / Int32ul,
        "Bank" / Int32ul,
        "Device" / Int32ul,
        "Row" / Int32ul,
        "Column" / Int32ul,
        "BitPosition" / Int32ul,
        "RequesterId" / Int64ul,
        "ResponderId" / Int64ul,
        "TargetId" / Int64ul,
        "ErrorType" / Int8ul,
        "Extended" / Int32ul,
        "RankNumber" / Int32ul,
        "CardHandle" / Int32ul,
        "ModuleHandle" / Int32ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=47, version=0)
class Microsoft_Windows_WHEA_Logger_47_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "FRUId" / Guid,
        "FRUText" / CString,
        "ValidBits" / Int64ul,
        "ErrorStatus" / Int64ul,
        "PhysicalAddress" / Int64ul,
        "PhysicalAddressMask" / Int64ul,
        "Node" / Int32ul,
        "Card" / Int32ul,
        "Module" / Int32ul,
        "Bank" / Int32ul,
        "Device" / Int32ul,
        "Row" / Int32ul,
        "Column" / Int32ul,
        "BitPosition" / Int32ul,
        "RequesterId" / Int64ul,
        "ResponderId" / Int64ul,
        "TargetId" / Int64ul,
        "ErrorType" / Int8ul,
        "Extended" / Int32ul,
        "RankNumber" / Int32ul,
        "CardHandle" / Int32ul,
        "ModuleHandle" / Int32ul,
        "Length" / Int32ul,
        "RawData" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=48, version=0)
class Microsoft_Windows_WHEA_Logger_48_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "Bank" / Int32ul,
        "MciStatus" / Int64ul,
        "MciAddr" / Int64ul,
        "MciMisc" / Int64ul,
        "FRUText" / CString
    )


@declare(guid=guid("c26c4f3c-3f66-4e99-8f8a-39405cfed220"), event_id=49, version=0)
class Microsoft_Windows_WHEA_Logger_49_0(Etw):
    pattern = Struct(
        "ErrorSource" / Int32ul,
        "Bank" / Int32ul,
        "MciStatus" / Int64ul,
        "MciAddr" / Int64ul,
        "MciMisc" / Int64ul,
        "FRUText" / CString
    )

