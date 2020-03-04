# -*- coding: utf-8 -*-
"""
Microsoft-Windows-StorPort
GUID : c4636a1e-7986-4646-bf10-7bc3b4a76e8e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=1, version=1)
class Microsoft_Windows_StorPort_1_1(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=2, version=1)
class Microsoft_Windows_StorPort_2_1(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=4, version=1)
class Microsoft_Windows_StorPort_4_1(Etw):
    pattern = Struct(
        "MiniportExtension" / Int64ul,
        "PortNumber" / Int32ul,
        "PauseTime" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=5, version=1)
class Microsoft_Windows_StorPort_5_1(Etw):
    pattern = Struct(
        "MiniportExtension" / Int64ul,
        "PortNumber" / Int32ul,
        "LinkDownTime" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=6, version=1)
class Microsoft_Windows_StorPort_6_1(Etw):
    pattern = Struct(
        "MiniportExtension" / Int64ul,
        "PortNumber" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=7, version=1)
class Microsoft_Windows_StorPort_7_1(Etw):
    pattern = Struct(
        "MiniportExtension" / Int64ul,
        "PortNumber" / Int32ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=8, version=1)
class Microsoft_Windows_StorPort_8_1(Etw):
    pattern = Struct(
        "MiniportExtension" / Int64ul,
        "PortNumber" / Int32ul,
        "PauseTime" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=9, version=1)
class Microsoft_Windows_StorPort_9_1(Etw):
    pattern = Struct(
        "MiniportExtension" / Int64ul,
        "PortNumber" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=10, version=1)
class Microsoft_Windows_StorPort_10_1(Etw):
    pattern = Struct(
        "MiniportExtension" / Int64ul,
        "PauseTime" / Int32ul,
        "PortNumber" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=11, version=1)
class Microsoft_Windows_StorPort_11_1(Etw):
    pattern = Struct(
        "MiniportExtension" / Int64ul,
        "PortNumber" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=12, version=1)
class Microsoft_Windows_StorPort_12_1(Etw):
    pattern = Struct(
        "MiniportExtension" / Int64ul,
        "PortNumber" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=13, version=1)
class Microsoft_Windows_StorPort_13_1(Etw):
    pattern = Struct(
        "MiniportExtension" / Int64ul,
        "PortNumber" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "RequestDuration" / Int32ul,
        "Command" / Int8ul,
        "ScsiStatus" / Int8ul,
        "SrbStatus" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=14, version=1)
class Microsoft_Windows_StorPort_14_1(Etw):
    pattern = Struct(
        "Field" / WString,
        "PivotField" / WString,
        "PivotValue" / Int32ul,
        "OriginalValue" / Int32ul,
        "NewValue" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=15, version=1)
class Microsoft_Windows_StorPort_15_1(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "PortNumber" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "CurrentDepth" / Int32ul,
        "NewDepth" / Int32ul,
        "MaxDepth" / Int32ul,
        "StorportApi" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=16, version=1)
class Microsoft_Windows_StorPort_16_1(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "PortNumber" / Int32ul,
        "InitialCount" / Int32ul,
        "MaxCount" / Int32ul,
        "ResourceSize" / Int32ul,
        "MemorySize" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=17, version=1)
class Microsoft_Windows_StorPort_17_1(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "PortNumber" / Int32ul,
        "CurrentOutstanding" / Int32ul,
        "OldHighWaterMark" / Int32ul,
        "NewHighWaterMark" / Int32ul,
        "MaxCount" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=18, version=1)
class Microsoft_Windows_StorPort_18_1(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "PortNumber" / Int32ul,
        "CurrentOutstanding" / Int32ul,
        "HighWaterMark" / Int32ul,
        "MaxCount" / Int32ul,
        "MemAllocFailures" / Int32ul,
        "ConsecutiveFailures" / Int32ul,
        "SuspendCount" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=19, version=1)
class Microsoft_Windows_StorPort_19_1(Etw):
    pattern = Struct(
        "Version" / Int32ul,
        "Size" / Int32ul,
        "Flags" / Int32ul,
        "ConcurrentChannels" / Int32ul,
        "FirstRedirectionMessageNumber" / Int32ul,
        "LastRedirectionMessageNumber" / Int32ul,
        "DeviceNode" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=20, version=1)
class Microsoft_Windows_StorPort_20_1(Etw):
    pattern = Struct(
        "Version" / Int32ul,
        "Size" / Int32ul,
        "Flags" / Int32ul,
        "ConcurrentChannels" / Int32ul,
        "FirstRedirectionMessageNumber" / Int32ul,
        "LastRedirectionMessageNumber" / Int32ul,
        "DeviceNode" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=21, version=1)
class Microsoft_Windows_StorPort_21_1(Etw):
    pattern = Struct(
        "HwInitializationDataSize" / Int32ul,
        "AdapterInterfaceType" / Int32ul,
        "DeviceExtensionSize" / Int32ul,
        "SpecificLuExtensionSize" / Int32ul,
        "SrbExtensionSize" / Int32ul,
        "FeatureSupport" / Int32ul,
        "SrbTypeFlags" / Int32ul,
        "AddressTypeFlags" / Int32ul,
        "HwFreeAdapterResources" / Int64ul,
        "HwProcessServiceRequest" / Int64ul,
        "HwCompleteServiceIrp" / Int64ul,
        "HwInitializeTracing" / Int64ul,
        "HwCleanupTracing" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=22, version=1)
class Microsoft_Windows_StorPort_22_1(Etw):
    pattern = Struct(
        "Length" / Int32ul,
        "MaxTransferLength" / Int32ul,
        "NumberOfBuses" / Int32ul,
        "MaxNumberOfTargets" / Int32ul,
        "MaxNumberOfLogicalUnits" / Int32ul,
        "MaxNumberOfIO" / Int32ul,
        "MaxIOsPerLun" / Int32ul,
        "InitialLunQueueDepth" / Int32ul,
        "RequestedDumpBufferSize" / Int32ul,
        "FeatureSupport" / Int32ul,
        "SrbType" / Int8ul,
        "AddressType" / Int8ul,
        "Dma64BitAddress" / Int8ul,
        "BusResetHoldTime" / Int32ul,
        "InterruptSynchronizationMode" / Int32ul,
        "CachesData" / Int8ul,
        "VirtualDevice" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=23, version=1)
class Microsoft_Windows_StorPort_23_1(Etw):
    pattern = Struct(
        "Length" / Int32ul,
        "MaxTransferLength" / Int32ul,
        "NumberOfBuses" / Int32ul,
        "MaxNumberOfTargets" / Int32ul,
        "MaxNumberOfLogicalUnits" / Int32ul,
        "MaxNumberOfIO" / Int32ul,
        "MaxIOsPerLun" / Int32ul,
        "InitialLunQueueDepth" / Int32ul,
        "RequestedDumpBufferSize" / Int32ul,
        "FeatureSupport" / Int32ul,
        "SrbType" / Int8ul,
        "AddressType" / Int8ul,
        "Dma64BitAddress" / Int8ul,
        "BusResetHoldTime" / Int32ul,
        "InterruptSynchronizationMode" / Int32ul,
        "CachesData" / Int8ul,
        "VirtualDevice" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=24, version=1)
class Microsoft_Windows_StorPort_24_1(Etw):
    pattern = Struct(
        "Operation" / WString,
        "Duration_100ns" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=25, version=1)
class Microsoft_Windows_StorPort_25_1(Etw):
    pattern = Struct(
        "MiniportExtension" / Int64ul,
        "PortNumber" / Int32ul,
        "ChangedEntity" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "Attributes" / Int32ul,
        "HwStateChange" / Int64ul,
        "HwStateChangeContext" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=26, version=1)
class Microsoft_Windows_StorPort_26_1(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "PortNumber" / Int32ul,
        "ChangedEntity" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "Attributes" / Int32ul,
        "HwStateChange" / Int64ul,
        "HwStateChangeContext" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=27, version=1)
class Microsoft_Windows_StorPort_27_1(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "AdapterHardwareId" / WString,
        "MiniportName" / WString,
        "AdapterInterfaceType" / Int32ul,
        "Flags" / Int64ul,
        "AllowStorageD3" / Int8ul,
        "AcpiDsdProperty" / Int32ul,
        "StorageD3RegistryState" / Int32ul,
        "StorageD3Enable" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=200, version=2)
class Microsoft_Windows_StorPort_200_2(Etw):
    pattern = Struct(
        "RequestDuration_100ns" / Int64ul,
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "SrbStatus" / Int8ul,
        "OriginalIrp" / Int64ul,
        "Port" / Int8ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "ScsiStatus" / Int8ul,
        "ByteLengthOfTransfer" / Int32ul,
        "BuildIoDuration_100ns" / Int64ul,
        "StartIoDuration_100ns" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=201, version=2)
class Microsoft_Windows_StorPort_201_2(Etw):
    pattern = Struct(
        "RequestDuration_100ns" / Int64ul,
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "SrbStatus" / Int8ul,
        "OriginalIrp" / Int64ul,
        "Port" / Int8ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "ScsiStatus" / Int8ul,
        "ByteLengthOfTransfer" / Int32ul,
        "BuildIoDuration_100ns" / Int64ul,
        "StartIoDuration_100ns" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=202, version=2)
class Microsoft_Windows_StorPort_202_2(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransferinblocks" / Int64ul,
        "LBA" / Int64ul,
        "OriginalIrp" / Int64ul,
        "NvCachePriority" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=203, version=2)
class Microsoft_Windows_StorPort_203_2(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransferinblocks" / Int64ul,
        "LBA" / Int64ul,
        "OriginalIrp" / Int64ul,
        "NvCachePriority" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=204, version=2)
class Microsoft_Windows_StorPort_204_2(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransferinblocks" / Int64ul,
        "LBA" / Int64ul,
        "OriginalIrp" / Int64ul,
        "NvCachePriority" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=205, version=2)
class Microsoft_Windows_StorPort_205_2(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransferinblocks" / Int64ul,
        "LBA" / Int64ul,
        "OriginalIrp" / Int64ul,
        "NvCachePriority" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=206, version=2)
class Microsoft_Windows_StorPort_206_2(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransferinblocks" / Int64ul,
        "LBA" / Int64ul,
        "OriginalIrp" / Int64ul,
        "NvCachePriority" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=207, version=2)
class Microsoft_Windows_StorPort_207_2(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransferinblocks" / Int64ul,
        "LBA" / Int64ul,
        "OriginalIrp" / Int64ul,
        "NvCachePriority" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=208, version=1)
class Microsoft_Windows_StorPort_208_1(Etw):
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


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=209, version=1)
class Microsoft_Windows_StorPort_209_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "CurrentRetryCount" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=210, version=1)
class Microsoft_Windows_StorPort_210_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=211, version=1)
class Microsoft_Windows_StorPort_211_1(Etw):
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


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=212, version=1)
class Microsoft_Windows_StorPort_212_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "MajorFunction" / Int32ul,
        "MinorFunction" / Int32ul,
        "Parameter" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=213, version=1)
class Microsoft_Windows_StorPort_213_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "MajorFunction" / Int32ul,
        "MinorFunction" / Int32ul,
        "Parameter" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=214, version=1)
class Microsoft_Windows_StorPort_214_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=215, version=2)
class Microsoft_Windows_StorPort_215_2(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "Irp" / Int64ul,
        "MinorFunction" / Int32ul,
        "Type" / Int8ul,
        "OldState" / Int32ul,
        "NewState" / Int32ul,
        "Action" / Int32ul,
        "PowerStateContext" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=216, version=2)
class Microsoft_Windows_StorPort_216_2(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Irp" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=217, version=1)
class Microsoft_Windows_StorPort_217_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "MinorFunction" / Int32ul,
        "Type" / Int32ul,
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=218, version=1)
class Microsoft_Windows_StorPort_218_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=219, version=1)
class Microsoft_Windows_StorPort_219_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "NumberOfChildren" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=220, version=1)
class Microsoft_Windows_StorPort_220_1(Etw):
    pattern = Struct(
        "QueueTag" / Int32ul,
        "Operation" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=221, version=1)
class Microsoft_Windows_StorPort_221_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "MajorFunction" / Int32ul,
        "MinorFunction" / Int32ul,
        "Parameter" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=222, version=1)
class Microsoft_Windows_StorPort_222_1(Etw):
    pattern = Struct(
        "Port" / Int8ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "RequestDuration" / Int64ul,
        "CDBLength" / Int32ul,
        "CDB" / Bytes(lambda this: this.CDBLength),
        "SrbStatus" / Int8ul,
        "Irp" / Int64ul,
        "OriginalIrp" / Int64ul,
        "BuildIoDuration" / Int64ul,
        "StartIoDuration" / Int64ul,
        "MiniportDuration" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=223, version=1)
class Microsoft_Windows_StorPort_223_1(Etw):
    pattern = Struct(
        "Port" / Int8ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "RequestDuration" / Int64ul,
        "CDBLength" / Int32ul,
        "CDB" / Bytes(lambda this: this.CDBLength),
        "SrbStatus" / Int8ul,
        "Irp" / Int64ul,
        "OriginalIrp" / Int64ul,
        "BuildIoDuration" / Int64ul,
        "StartIoDuration" / Int64ul,
        "MiniportDuration" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=224, version=1)
class Microsoft_Windows_StorPort_224_1(Etw):
    pattern = Struct(
        "DpcRoutine" / Int64ul,
        "DpcRoutineName" / WString,
        "PortNumber" / Int32ul,
        "CompletionCount" / Int32ul,
        "QpcTicks" / Int64ul,
        "Duration_100ns" / Int64ul,
        "SwitchDpcProc" / Int8ul,
        "RevertDpcProc" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=225, version=1)
class Microsoft_Windows_StorPort_225_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "DIrpRequested" / Int8ul,
        "DPNRDurationMsec" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=226, version=1)
class Microsoft_Windows_StorPort_226_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "DIrpRequested" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=227, version=1)
class Microsoft_Windows_StorPort_227_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "DIrpRequested" / Int8ul,
        "IdleTimeoutMsec" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=228, version=1)
class Microsoft_Windows_StorPort_228_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "DIrpRequested" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=229, version=2)
class Microsoft_Windows_StorPort_229_2(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "RegistrationStatus" / Int32ul,
        "Requested_D3ColdSupported" / Int8ul,
        "Requested_WakeCapable" / Int8ul,
        "Requested_IdleTimeoutInMS" / Int32ul,
        "NumberOfFStates" / Int32ul,
        "Actual_D3ColdSupported" / Int8ul,
        "Actual_WakeCapable" / Int8ul,
        "Actual_IdleTimeoutInMS" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=230, version=1)
class Microsoft_Windows_StorPort_230_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Component" / Int32ul,
        "FState" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=231, version=1)
class Microsoft_Windows_StorPort_231_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Component" / Int32ul,
        "FState" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=232, version=1)
class Microsoft_Windows_StorPort_232_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Component" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=233, version=1)
class Microsoft_Windows_StorPort_233_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Component" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=234, version=1)
class Microsoft_Windows_StorPort_234_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Component" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=235, version=1)
class Microsoft_Windows_StorPort_235_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Component" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=236, version=1)
class Microsoft_Windows_StorPort_236_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "DIrpRequested" / Int8ul,
        "DPNRDurationMsec" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=237, version=1)
class Microsoft_Windows_StorPort_237_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "DIrpRequested" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=238, version=1)
class Microsoft_Windows_StorPort_238_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "DIrpRequested" / Int8ul,
        "IdleTimeoutMsec" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=239, version=1)
class Microsoft_Windows_StorPort_239_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "DIrpRequested" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=240, version=1)
class Microsoft_Windows_StorPort_240_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "D3ColdSupported" / Int8ul,
        "IdleTimeoutInMS" / Int32ul,
        "NumberOfFStates" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=241, version=1)
class Microsoft_Windows_StorPort_241_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "Component" / Int32ul,
        "FState" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=242, version=1)
class Microsoft_Windows_StorPort_242_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "Component" / Int32ul,
        "FState" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=243, version=1)
class Microsoft_Windows_StorPort_243_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "Component" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=244, version=1)
class Microsoft_Windows_StorPort_244_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "Component" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=245, version=1)
class Microsoft_Windows_StorPort_245_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "Component" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=246, version=1)
class Microsoft_Windows_StorPort_246_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "Component" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=247, version=1)
class Microsoft_Windows_StorPort_247_1(Etw):
    pattern = Struct(
        "QueueID" / Int64ul,
        "QueueTag" / Int32ul,
        "Operation" / Int8ul,
        "EnqueueReason" / Int8ul,
        "QueuedIoCount" / Int32ul,
        "OutstandingIoCount" / Int32ul,
        "NTStatus" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=248, version=1)
class Microsoft_Windows_StorPort_248_1(Etw):
    pattern = Struct(
        "IsrRoutine" / Int64ul,
        "PortNumber" / Int32ul,
        "Processor" / Int32ul,
        "Duration_100ns" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=250, version=1)
class Microsoft_Windows_StorPort_250_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=251, version=1)
class Microsoft_Windows_StorPort_251_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=252, version=1)
class Microsoft_Windows_StorPort_252_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul,
        "Parameter5Name" / WString,
        "Parameter5Value" / Int64ul,
        "Parameter6Name" / WString,
        "Parameter6Value" / Int64ul,
        "Parameter7Name" / WString,
        "Parameter7Value" / Int64ul,
        "Parameter8Name" / WString,
        "Parameter8Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=253, version=1)
class Microsoft_Windows_StorPort_253_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=254, version=1)
class Microsoft_Windows_StorPort_254_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=255, version=1)
class Microsoft_Windows_StorPort_255_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul,
        "Parameter5Name" / WString,
        "Parameter5Value" / Int64ul,
        "Parameter6Name" / WString,
        "Parameter6Value" / Int64ul,
        "Parameter7Name" / WString,
        "Parameter7Value" / Int64ul,
        "Parameter8Name" / WString,
        "Parameter8Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=256, version=1)
class Microsoft_Windows_StorPort_256_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Irp" / Int64ul,
        "Srb" / Int64ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=257, version=1)
class Microsoft_Windows_StorPort_257_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Irp" / Int64ul,
        "Srb" / Int64ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=258, version=1)
class Microsoft_Windows_StorPort_258_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Irp" / Int64ul,
        "Srb" / Int64ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul,
        "Parameter5Name" / WString,
        "Parameter5Value" / Int64ul,
        "Parameter6Name" / WString,
        "Parameter6Value" / Int64ul,
        "Parameter7Name" / WString,
        "Parameter7Value" / Int64ul,
        "Parameter8Name" / WString,
        "Parameter8Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=259, version=1)
class Microsoft_Windows_StorPort_259_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Component" / Int32ul,
        "FState" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=260, version=1)
class Microsoft_Windows_StorPort_260_1(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "Irp" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=261, version=1)
class Microsoft_Windows_StorPort_261_1(Etw):
    pattern = Struct(
        "PoHandle" / Int64ul,
        "PortNumber" / Int32ul,
        "Requested_AdapterIdleTimeout_ms" / Int32ul,
        "Actual_AdapterIdleTimeout_ms" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=262, version=1)
class Microsoft_Windows_StorPort_262_1(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Irp" / Int64ul,
        "MinorFunction" / Int32ul,
        "Type" / Int8ul,
        "OldState" / Int32ul,
        "NewState" / Int32ul,
        "Action" / Int32ul,
        "PowerStateContext" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=263, version=1)
class Microsoft_Windows_StorPort_263_1(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "CurrentPowerCycleCount" / Int32ul,
        "PotentialPowerCycleCount" / Int32ul,
        "MinPowerCyclePeriodInMS" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=264, version=1)
class Microsoft_Windows_StorPort_264_1(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "CurrentD3IdleTimeout" / Int32ul,
        "NewD3IdleTimeout" / Int32ul,
        "IoCoalescingOn" / Int8ul,
        "OnBatteryPower" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=265, version=1)
class Microsoft_Windows_StorPort_265_1(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "PreviousPowerHint" / Int32ul,
        "PreviousResumeLatency_ms" / Int32ul,
        "NewPowerHint" / Int32ul,
        "NewResumeLatency_ms" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=267, version=1)
class Microsoft_Windows_StorPort_267_1(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=268, version=1)
class Microsoft_Windows_StorPort_268_1(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Success" / Int8ul,
        "ActiveRefsDuringMaintenanceTime" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=269, version=1)
class Microsoft_Windows_StorPort_269_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "IOCTLCode" / Int32ul,
        "AdapterRequest" / Int8ul,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "ProtocolType" / Int32ul,
        "CommandCode" / Int32ul,
        "ReturnStatus" / Int32ul,
        "ErrorCode" / Int32ul,
        "UntaggedRequest" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=500, version=2)
class Microsoft_Windows_StorPort_500_2(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "ClassDeviceGuid" / Guid,
        "SrbFunction" / Int32ul,
        "CdbLength" / Int32ul,
        "Cdb" / Bytes(lambda this: this.CdbLength),
        "SrbTimeout" / Int32ul,
        "AbortSupported" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=501, version=1)
class Microsoft_Windows_StorPort_501_1(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "PathID" / Int8ul,
        "RequestingUnitClassDeviceGuid" / Guid
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=502, version=1)
class Microsoft_Windows_StorPort_502_1(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "ClassDeviceGuid" / Guid,
        "Reason" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=503, version=1)
class Microsoft_Windows_StorPort_503_1(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "ClassDeviceGuid" / Guid,
        "Reason" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=504, version=3)
class Microsoft_Windows_StorPort_504_3(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "ClassDeviceGuid" / Guid,
        "AdapterGuid" / Guid,
        "BusType" / Int32ul,
        "MiniportName" / WString,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "SystemUptime_s" / Int64ul,
        "Version" / Int8ul,
        "TotalErrors" / Int32ul,
        "TotalReadWriteErrors" / Int32ul,
        "TotalImpendingDeviceFailureErrors" / Int32ul,
        "TotalDeviceFailureErrors" / Int32ul,
        "TimeoutsInMiniport" / Int32ul,
        "LastError_RequestDuration_ms" / Int32ul,
        "LastError_WaitDuration_ms" / Int32ul,
        "LastError_Command" / Int8ul,
        "LastError_SrbStatus" / Int8ul,
        "LastError_ScsiStatus" / Int8ul,
        "LastError_SenseKey" / Int8ul,
        "LastError_AddSense" / Int8ul,
        "LastError_AddSenseQ" / Int8ul,
        "LastError_IoSize" / Int32ul,
        "LastError_QueueDepth" / Int32ul,
        "LastError_LBA" / Int64ul,
        "SampledErrorLogArrayLength" / Int32ul,
        "SampledErrorLogArray" / Bytes(lambda this: this.SampledErrorLogArrayLength),
        "UniqueErrorLogArrayLength" / Int32ul,
        "UniqueErrorLogArray" / Bytes(lambda this: this.UniqueErrorLogArrayLength)
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=505, version=4)
class Microsoft_Windows_StorPort_505_4(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "ClassDeviceGuid" / Guid,
        "AdapterGuid" / Guid,
        "BusType" / Int32ul,
        "MiniportName" / WString,
        "IoTimeout_s" / Int32ul,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "SystemUptime_s" / Int64ul,
        "Version" / Int8ul,
        "TotalIoCount" / Int64ul,
        "TotalDeviceQueueIoCount" / Int64ul,
        "MaxDeviceQueueCount" / Int32ul,
        "MaxOutstandingCount" / Int32ul,
        "TotalDeviceQueueIoWaitDuration_100ns" / Int64ul,
        "MaxDeviceQueueIoWaitDuration_100ns" / Int64ul,
        "DeviceQueueIoWaitExceededTimeoutCount" / Int64ul,
        "DeviceQueueIoBusyCount" / Int64ul,
        "DeviceQueueIoPausedCount" / Int64ul,
        "DeviceQueueIoUntaggedCommandOutstandingCount" / Int64ul,
        "DeviceQueueIoPausedForUntaggedCount" / Int64ul,
        "MaxReadWriteLatency_100ns" / Int32ul,
        "MaxFlushLatency_100ns" / Int32ul,
        "MaxUnmapLatency_100ns" / Int32ul,
        "IoLatencyBuckets" / WString,
        "BucketIoSuccess1" / Int64ul,
        "BucketIoSuccess2" / Int64ul,
        "BucketIoSuccess3" / Int64ul,
        "BucketIoSuccess4" / Int64ul,
        "BucketIoSuccess5" / Int64ul,
        "BucketIoSuccess6" / Int64ul,
        "BucketIoSuccess7" / Int64ul,
        "BucketIoSuccess8" / Int64ul,
        "BucketIoSuccess9" / Int64ul,
        "BucketIoSuccess10" / Int64ul,
        "BucketIoSuccess11" / Int64ul,
        "BucketIoSuccess12" / Int64ul,
        "BucketIoFailed1" / Int64ul,
        "BucketIoFailed2" / Int64ul,
        "BucketIoFailed3" / Int64ul,
        "BucketIoFailed4" / Int64ul,
        "BucketIoFailed5" / Int64ul,
        "BucketIoFailed6" / Int64ul,
        "BucketIoFailed7" / Int64ul,
        "BucketIoFailed8" / Int64ul,
        "BucketIoFailed9" / Int64ul,
        "BucketIoFailed10" / Int64ul,
        "BucketIoFailed11" / Int64ul,
        "BucketIoFailed12" / Int64ul,
        "BucketIoLatency1_100ns" / Int64ul,
        "BucketIoLatency2_100ns" / Int64ul,
        "BucketIoLatency3_100ns" / Int64ul,
        "BucketIoLatency4_100ns" / Int64ul,
        "BucketIoLatency5_100ns" / Int64ul,
        "BucketIoLatency6_100ns" / Int64ul,
        "BucketIoLatency7_100ns" / Int64ul,
        "BucketIoLatency8_100ns" / Int64ul,
        "BucketIoLatency9_100ns" / Int64ul,
        "BucketIoLatency10_100ns" / Int64ul,
        "BucketIoLatency11_100ns" / Int64ul,
        "BucketIoLatency12_100ns" / Int64ul,
        "TotalReadBytes" / Int64ul,
        "TotalWriteBytes" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=506, version=2)
class Microsoft_Windows_StorPort_506_2(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "ClassDeviceGuid" / Guid,
        "UnresponsiveRequests" / Int64ul,
        "QosGuaranteeFailures" / Int64ul,
        "QosGuaranteeThreshold_s" / Int8ul,
        "UnitQueueTimeoutCount" / Int64ul,
        "AdapterQueueTimeoutCount" / Int64ul,
        "HwQueueTimeoutCount" / Int32ul,
        "MaxUnitQueueDepth" / Int32ul,
        "MaxAdapterQueueDepth" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=507, version=1)
class Microsoft_Windows_StorPort_507_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "ClassDeviceGuid" / Guid,
        "SrbFunction" / Int32ul,
        "CdbLength" / Int32ul,
        "Cdb" / Bytes(lambda this: this.CdbLength),
        "IoDispatchToResetTime_100ns" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=508, version=1)
class Microsoft_Windows_StorPort_508_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "ClassDeviceGuid" / Guid,
        "AbortedReq_SrbFunction" / Int32ul,
        "AbortedReq_CdbLength" / Int32ul,
        "AbortedReq_Cdb" / Bytes(lambda this: this.AbortedReq_CdbLength)
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=509, version=1)
class Microsoft_Windows_StorPort_509_1(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "ClassDeviceGuid" / Guid,
        "AbortSrbTimeout" / Int32ul,
        "AbortedReq_SrbFunction" / Int32ul,
        "AbortedReq_CdbLength" / Int32ul,
        "AbortedReq_Cdb" / Bytes(lambda this: this.AbortedReq_CdbLength)
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=510, version=3)
class Microsoft_Windows_StorPort_510_3(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "ClassDeviceGuid" / Guid,
        "AdapterGuid" / Guid,
        "MiniportName" / WString,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "SystemUptime_s" / Int64ul,
        "Revision" / Int32ul,
        "SmartReturnStatus" / Int8ul,
        "SmartAttributesLength" / Int32ul,
        "SmartAttributes" / Bytes(lambda this: this.SmartAttributesLength)
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=511, version=3)
class Microsoft_Windows_StorPort_511_3(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "ClassDeviceGuid" / Guid,
        "AdapterGuid" / Guid,
        "MiniportName" / WString,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "SystemUptime_s" / Int64ul,
        "Revision" / Int32ul,
        "GeneralLength" / Int32ul,
        "General" / Bytes(lambda this: this.GeneralLength),
        "FreeFallLength" / Int32ul,
        "Freefall" / Bytes(lambda this: this.FreeFallLength),
        "RotatingMediaLength" / Int32ul,
        "RotatingMedia" / Bytes(lambda this: this.RotatingMediaLength),
        "GeneralErrorsLength" / Int32ul,
        "GeneralErrors" / Bytes(lambda this: this.GeneralErrorsLength),
        "TemperatureLength" / Int32ul,
        "Temperature" / Bytes(lambda this: this.TemperatureLength),
        "TransportLength" / Int32ul,
        "Transport" / Bytes(lambda this: this.TransportLength),
        "SolidStateDeviceLength" / Int32ul,
        "SolidStateDevice" / Bytes(lambda this: this.SolidStateDeviceLength)
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=512, version=4)
class Microsoft_Windows_StorPort_512_4(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "ClassDeviceGuid" / Guid,
        "AdapterGuid" / Guid,
        "MiniportName" / WString,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "SystemUptime_s" / Int64ul,
        "CriticalWarning" / Int32ul,
        "NvmeHealthLogLength" / Int32ul,
        "NvmeHealthLog" / Bytes(lambda this: this.NvmeHealthLogLength),
        "VendorSpecificLogPageCode" / Int8ul,
        "VendorSpecificLogPageVersion" / Int16ul,
        "VendorSpecificLogLength" / Int32ul,
        "VendorSpecificLog" / Bytes(lambda this: this.VendorSpecificLogLength)
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=513, version=1)
class Microsoft_Windows_StorPort_513_1(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "PortNumber" / Int32sl,
        "AllocationPolicy" / Int32ul,
        "DeviceMinSizeInBytes" / Int32ul,
        "DevicePreferredSizeInBytes" / Int32ul,
        "PolicyMaxInBytes" / Int32ul,
        "TargetAllocationSizeInBytes" / Int32ul,
        "ActualAllocationSizeInBytes" / Int32ul,
        "RangesAllocated" / Int32ul,
        "Success" / Int32ul,
        "FailReason" / Int32ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=514, version=2)
class Microsoft_Windows_StorPort_514_2(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "ClassDeviceGuid" / Guid,
        "Irp" / Int64ul,
        "OriginalIrp" / Int64ul,
        "LengthOfTransferinblocks" / Int64ul,
        "RequestLBA" / Int64ul,
        "CurrentLBA" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=515, version=2)
class Microsoft_Windows_StorPort_515_2(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "ClassDeviceGuid" / Guid,
        "Irp" / Int64ul,
        "OriginalIrp" / Int64ul,
        "LBA" / Int64ul,
        "PendingIoCount" / Int32ul,
        "ResetWritePointerAll" / Int8ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=516, version=1)
class Microsoft_Windows_StorPort_516_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=517, version=1)
class Microsoft_Windows_StorPort_517_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=518, version=1)
class Microsoft_Windows_StorPort_518_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul,
        "Parameter5Name" / WString,
        "Parameter5Value" / Int64ul,
        "Parameter6Name" / WString,
        "Parameter6Value" / Int64ul,
        "Parameter7Name" / WString,
        "Parameter7Value" / Int64ul,
        "Parameter8Name" / WString,
        "Parameter8Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=519, version=1)
class Microsoft_Windows_StorPort_519_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=520, version=1)
class Microsoft_Windows_StorPort_520_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=521, version=1)
class Microsoft_Windows_StorPort_521_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul,
        "Parameter5Name" / WString,
        "Parameter5Value" / Int64ul,
        "Parameter6Name" / WString,
        "Parameter6Value" / Int64ul,
        "Parameter7Name" / WString,
        "Parameter7Value" / Int64ul,
        "Parameter8Name" / WString,
        "Parameter8Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=522, version=1)
class Microsoft_Windows_StorPort_522_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Irp" / Int64ul,
        "Srb" / Int64ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=523, version=1)
class Microsoft_Windows_StorPort_523_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Irp" / Int64ul,
        "Srb" / Int64ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=524, version=1)
class Microsoft_Windows_StorPort_524_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Irp" / Int64ul,
        "Srb" / Int64ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul,
        "Parameter5Name" / WString,
        "Parameter5Value" / Int64ul,
        "Parameter6Name" / WString,
        "Parameter6Value" / Int64ul,
        "Parameter7Name" / WString,
        "Parameter7Value" / Int64ul,
        "Parameter8Name" / WString,
        "Parameter8Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=525, version=1)
class Microsoft_Windows_StorPort_525_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=526, version=1)
class Microsoft_Windows_StorPort_526_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=527, version=1)
class Microsoft_Windows_StorPort_527_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul,
        "Parameter5Name" / WString,
        "Parameter5Value" / Int64ul,
        "Parameter6Name" / WString,
        "Parameter6Value" / Int64ul,
        "Parameter7Name" / WString,
        "Parameter7Value" / Int64ul,
        "Parameter8Name" / WString,
        "Parameter8Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=528, version=1)
class Microsoft_Windows_StorPort_528_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=529, version=1)
class Microsoft_Windows_StorPort_529_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=530, version=1)
class Microsoft_Windows_StorPort_530_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul,
        "Parameter5Name" / WString,
        "Parameter5Value" / Int64ul,
        "Parameter6Name" / WString,
        "Parameter6Value" / Int64ul,
        "Parameter7Name" / WString,
        "Parameter7Value" / Int64ul,
        "Parameter8Name" / WString,
        "Parameter8Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=531, version=1)
class Microsoft_Windows_StorPort_531_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Irp" / Int64ul,
        "Srb" / Int64ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=532, version=1)
class Microsoft_Windows_StorPort_532_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Irp" / Int64ul,
        "Srb" / Int64ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=533, version=1)
class Microsoft_Windows_StorPort_533_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Irp" / Int64ul,
        "Srb" / Int64ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul,
        "Parameter5Name" / WString,
        "Parameter5Value" / Int64ul,
        "Parameter6Name" / WString,
        "Parameter6Value" / Int64ul,
        "Parameter7Name" / WString,
        "Parameter7Value" / Int64ul,
        "Parameter8Name" / WString,
        "Parameter8Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=534, version=1)
class Microsoft_Windows_StorPort_534_1(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "ClassDeviceGuid" / Guid,
        "AdapterGuid" / Guid,
        "MiniportName" / WString,
        "VendorId" / CString,
        "ProductId" / CString,
        "DataLength" / Int32ul,
        "Data" / Bytes(lambda this: this.DataLength),
        "Id" / Int32ul,
        "Description" / WString
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=535, version=1)
class Microsoft_Windows_StorPort_535_1(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "ClassDeviceGuid" / Guid,
        "AdapterGuid" / Guid,
        "MiniportName" / WString,
        "VendorId" / CString,
        "ProductId" / CString,
        "FailReason" / WString
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=536, version=1)
class Microsoft_Windows_StorPort_536_1(Etw):
    pattern = Struct(
        "PortNumber" / Int32ul,
        "PathID" / Int8ul,
        "TargetID" / Int8ul,
        "LUN" / Int8ul,
        "ClassDeviceGuid" / Guid,
        "AdapterGuid" / Guid,
        "MiniportName" / WString,
        "VendorId" / CString,
        "ProductId" / CString,
        "FailReason" / WString
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=537, version=1)
class Microsoft_Windows_StorPort_537_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=538, version=1)
class Microsoft_Windows_StorPort_538_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=539, version=1)
class Microsoft_Windows_StorPort_539_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul,
        "Parameter5Name" / WString,
        "Parameter5Value" / Int64ul,
        "Parameter6Name" / WString,
        "Parameter6Value" / Int64ul,
        "Parameter7Name" / WString,
        "Parameter7Value" / Int64ul,
        "Parameter8Name" / WString,
        "Parameter8Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=540, version=1)
class Microsoft_Windows_StorPort_540_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=541, version=1)
class Microsoft_Windows_StorPort_541_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=542, version=1)
class Microsoft_Windows_StorPort_542_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul,
        "Parameter5Name" / WString,
        "Parameter5Value" / Int64ul,
        "Parameter6Name" / WString,
        "Parameter6Value" / Int64ul,
        "Parameter7Name" / WString,
        "Parameter7Value" / Int64ul,
        "Parameter8Name" / WString,
        "Parameter8Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=543, version=1)
class Microsoft_Windows_StorPort_543_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=544, version=1)
class Microsoft_Windows_StorPort_544_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=545, version=1)
class Microsoft_Windows_StorPort_545_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul,
        "Parameter5Name" / WString,
        "Parameter5Value" / Int64ul,
        "Parameter6Name" / WString,
        "Parameter6Value" / Int64ul,
        "Parameter7Name" / WString,
        "Parameter7Value" / Int64ul,
        "Parameter8Name" / WString,
        "Parameter8Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=546, version=1)
class Microsoft_Windows_StorPort_546_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=547, version=1)
class Microsoft_Windows_StorPort_547_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul
    )


@declare(guid=guid("c4636a1e-7986-4646-bf10-7bc3b4a76e8e"), event_id=548, version=1)
class Microsoft_Windows_StorPort_548_1(Etw):
    pattern = Struct(
        "MiniportName" / WString,
        "MiniportEventId" / Int32ul,
        "MiniportEventDescription" / WString,
        "PortNumber" / Int32ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "Parameter1Name" / WString,
        "Parameter1Value" / Int64ul,
        "Parameter2Name" / WString,
        "Parameter2Value" / Int64ul,
        "Parameter3Name" / WString,
        "Parameter3Value" / Int64ul,
        "Parameter4Name" / WString,
        "Parameter4Value" / Int64ul,
        "Parameter5Name" / WString,
        "Parameter5Value" / Int64ul,
        "Parameter6Name" / WString,
        "Parameter6Value" / Int64ul,
        "Parameter7Name" / WString,
        "Parameter7Value" / Int64ul,
        "Parameter8Name" / WString,
        "Parameter8Value" / Int64ul
    )

