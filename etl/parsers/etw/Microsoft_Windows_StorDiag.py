# -*- coding: utf-8 -*-
"""
Microsoft-Windows-StorDiag
GUID : f5d05b38-80a6-4653-825d-c414e4ab3c68
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=1, version=1)
class Microsoft_Windows_StorDiag_1_1(Etw):
    pattern = Struct(
        "RequestProcessTime" / Int64ul,
        "OriginalIrp" / Int64ul,
        "Irp" / Int64ul,
        "MajorFunction" / Int8ul,
        "RequestType" / Int8ul,
        "SrbStatus" / Int8ul,
        "DeviceNumber" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=2, version=1)
class Microsoft_Windows_StorDiag_2_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "CurrentIOCount" / Int32ul,
        "ActiveIOCount" / Int32ul,
        "DeviceNumber" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=3, version=1)
class Microsoft_Windows_StorDiag_3_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Thread" / Int64ul,
        "CurrentIOCount" / Int32ul,
        "ActiveIOCount" / Int32ul,
        "DeviceNumber" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=4, version=1)
class Microsoft_Windows_StorDiag_4_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "RequestDurationin100ns" / Int64ul,
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "ServiceAction" / Int8ul,
        "SrbStatus" / Int8ul,
        "OriginalIrp" / Int64ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=5, version=1)
class Microsoft_Windows_StorDiag_5_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "IsWrite" / Int8ul,
        "FirstStartingLBA" / Int64ul,
        "LengthOfTransferinbytes" / Int64ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=6, version=1)
class Microsoft_Windows_StorDiag_6_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "IsWrite" / Int8ul,
        "FirstStartingLBA" / Int64ul,
        "LengthOfTransferinbytes" / Int64ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=7, version=1)
class Microsoft_Windows_StorDiag_7_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "TransferredLength" / Int64ul,
        "Flags" / Int32ul,
        "NTStatus" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=8, version=1)
class Microsoft_Windows_StorDiag_8_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "SenseKey" / Int8ul,
        "AddSense" / Int8ul,
        "AddSenseQ" / Int8ul,
        "CurrentRetryCount" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=201, version=1)
class Microsoft_Windows_StorDiag_201_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "RequestDurationin100ns" / Int64ul,
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "SrbStatus" / Int8ul,
        "OriginalIrp" / Int64ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=202, version=2)
class Microsoft_Windows_StorDiag_202_2(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransferinbytes" / Int64ul,
        "LBA" / Int64ul,
        "OriginalIrp" / Int64ul,
        "NvCachePriority" / Int8ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=203, version=2)
class Microsoft_Windows_StorDiag_203_2(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransferinbytes" / Int64ul,
        "LBA" / Int64ul,
        "OriginalIrp" / Int64ul,
        "NvCachePriority" / Int8ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=204, version=2)
class Microsoft_Windows_StorDiag_204_2(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransferinbytes" / Int64ul,
        "LBA" / Int64ul,
        "OriginalIrp" / Int64ul,
        "NvCachePriority" / Int8ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=205, version=2)
class Microsoft_Windows_StorDiag_205_2(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransferinbytes" / Int64ul,
        "LBA" / Int64ul,
        "OriginalIrp" / Int64ul,
        "NvCachePriority" / Int8ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=206, version=2)
class Microsoft_Windows_StorDiag_206_2(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransferinbytes" / Int64ul,
        "LBA" / Int64ul,
        "OriginalIrp" / Int64ul,
        "NvCachePriority" / Int8ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=207, version=2)
class Microsoft_Windows_StorDiag_207_2(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransferinbytes" / Int64ul,
        "LBA" / Int64ul,
        "OriginalIrp" / Int64ul,
        "NvCachePriority" / Int8ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=208, version=1)
class Microsoft_Windows_StorDiag_208_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "NTStatus" / Int32ul,
        "SrbStatus" / Int8ul,
        "ScsiStatus" / Int8ul,
        "SenseKey" / Int8ul,
        "AddSense" / Int8ul,
        "AddSenseQ" / Int8ul,
        "OriginalIrp" / Int64ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=208, version=2)
class Microsoft_Windows_StorDiag_208_2(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "NTStatus" / Int32ul,
        "SrbStatus" / Int8ul,
        "ScsiStatus" / Int8ul,
        "SenseKey" / Int8ul,
        "AddSense" / Int8ul,
        "AddSenseQ" / Int8ul,
        "OriginalIrp" / Int64ul,
        "NumberOfTimesRetried" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=209, version=1)
class Microsoft_Windows_StorDiag_209_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "CurrentRetryCount" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=209, version=2)
class Microsoft_Windows_StorDiag_209_2(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "CurrentRetryCount" / Int32ul,
        "NTStatus" / Int32ul,
        "SrbStatus" / Int8ul,
        "ScsiStatus" / Int8ul,
        "SenseKey" / Int8ul,
        "AddSense" / Int8ul,
        "AddSenseQ" / Int8ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=210, version=1)
class Microsoft_Windows_StorDiag_210_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=211, version=1)
class Microsoft_Windows_StorDiag_211_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "NTStatus" / Int32ul,
        "SrbStatus" / Int8ul,
        "ScsiStatus" / Int8ul,
        "SenseKey" / Int8ul,
        "AddSense" / Int8ul,
        "AddSenseQ" / Int8ul,
        "OriginalIrp" / Int64ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=212, version=1)
class Microsoft_Windows_StorDiag_212_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "MajorFunction" / Int32ul,
        "MinorFunction" / Int32ul,
        "Parameter" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=213, version=1)
class Microsoft_Windows_StorDiag_213_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "MajorFunction" / Int32ul,
        "MinorFunction" / Int32ul,
        "Parameter" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=214, version=1)
class Microsoft_Windows_StorDiag_214_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=215, version=1)
class Microsoft_Windows_StorDiag_215_1(Etw):
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


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=216, version=1)
class Microsoft_Windows_StorDiag_216_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=217, version=1)
class Microsoft_Windows_StorDiag_217_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "MinorFunction" / Int32ul,
        "Type" / Int32ul,
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=218, version=1)
class Microsoft_Windows_StorDiag_218_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=219, version=1)
class Microsoft_Windows_StorDiag_219_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "NumberOfChildren" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=220, version=1)
class Microsoft_Windows_StorDiag_220_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "QueueTag" / Int32ul,
        "Operation" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=221, version=1)
class Microsoft_Windows_StorDiag_221_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "Irp" / Int64ul,
        "MajorFunction" / Int32ul,
        "MinorFunction" / Int32ul,
        "Parameter" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=222, version=1)
class Microsoft_Windows_StorDiag_222_1(Etw):
    pattern = Struct(
        "DeviceGUID" / Guid,
        "DeviceNumber" / Int32ul,
        "RequestDurationin100ns" / Int64ul,
        "UpperLevelIrp" / Int64ul,
        "IrpStatus" / Int32ul,
        "DsmFlags" / Int32ul,
        "DataSetRangesCount" / Int32ul,
        "DataSetRanges" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=223, version=1)
class Microsoft_Windows_StorDiag_223_1(Etw):
    pattern = Struct(
        "DeviceGUID" / Guid,
        "DeviceNumber" / Int32ul,
        "RequestDurationin100ns" / Int64ul,
        "OriginalIrp" / Int64ul,
        "SrbStatus" / Int8ul,
        "SrbFlags" / Int32ul,
        "MaxAllowedLbaCount" / Int64ul,
        "MaxAllowedBlockDescriptorCount" / Int64ul,
        "LbaSizeinBytes" / Int32ul,
        "Srb_BlockDescriptorCount" / Int32ul,
        "Srb_BlockDescriptors" / Float32l
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=224, version=1)
class Microsoft_Windows_StorDiag_224_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "RequestDurationin100ns" / Int64ul,
        "UpperLevelIrp" / Int64ul,
        "IrpStatus" / Int32ul,
        "IsPartial" / Int8ul,
        "StartingOffset" / Int64ul,
        "BufferSize" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=225, version=1)
class Microsoft_Windows_StorDiag_225_1(Etw):
    pattern = Struct(
        "DeviceNumber" / Int32ul,
        "RequestDurationin100ns" / Int64ul,
        "UpperLevelIrp" / Int64ul,
        "IrpStatus" / Int32ul,
        "ResetAll" / Int8ul,
        "StartingOffset" / Int64ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=226, version=1)
class Microsoft_Windows_StorDiag_226_1(Etw):
    pattern = Struct(
        "DeviceGUID" / Guid,
        "DeviceNumber" / Int32ul,
        "Vendor" / CString,
        "Model" / CString,
        "FirmwareVersion" / CString,
        "SerialNumber" / CString,
        "IrpStatus" / Int32ul,
        "IoctlControlCode" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=500, version=1)
class Microsoft_Windows_StorDiag_500_1(Etw):
    pattern = Struct(
        "DeviceGUID" / Guid,
        "DeviceNumber" / Int32ul,
        "Vendor" / CString,
        "Model" / CString,
        "FirmwareVersion" / CString,
        "SerialNumber" / CString,
        "IrpStatus" / Int32ul,
        "LBA" / Int64ul,
        "TransferByteCount" / Int64ul,
        "NvCachePriority" / Int8ul,
        "PagingPriority" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=501, version=1)
class Microsoft_Windows_StorDiag_501_1(Etw):
    pattern = Struct(
        "DeviceGUID" / Guid,
        "DeviceNumber" / Int32ul,
        "Vendor" / CString,
        "Model" / CString,
        "FirmwareVersion" / CString,
        "SerialNumber" / CString,
        "IrpStatus" / Int32ul,
        "LBA" / Int64ul,
        "TransferByteCount" / Int64ul,
        "NvCachePriority" / Int8ul,
        "PagingPriority" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=502, version=1)
class Microsoft_Windows_StorDiag_502_1(Etw):
    pattern = Struct(
        "DeviceGUID" / Guid,
        "DeviceNumber" / Int32ul,
        "Vendor" / CString,
        "Model" / CString,
        "FirmwareVersion" / CString,
        "SerialNumber" / CString,
        "IrpStatus" / Int32ul,
        "LBA" / Int64ul,
        "TransferByteCount" / Int64ul,
        "NvCachePriority" / Int8ul,
        "PagingPriority" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=503, version=1)
class Microsoft_Windows_StorDiag_503_1(Etw):
    pattern = Struct(
        "DeviceGUID" / Guid,
        "DeviceNumber" / Int32ul,
        "Vendor" / CString,
        "Model" / CString,
        "FirmwareVersion" / CString,
        "SerialNumber" / CString,
        "IrpStatus" / Int32ul,
        "LBA" / Int64ul,
        "TransferByteCount" / Int64ul,
        "NvCachePriority" / Int8ul,
        "PagingPriority" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=504, version=1)
class Microsoft_Windows_StorDiag_504_1(Etw):
    pattern = Struct(
        "DeviceGUID" / Guid,
        "DeviceNumber" / Int32ul,
        "Vendor" / CString,
        "Model" / CString,
        "FirmwareVersion" / CString,
        "SerialNumber" / CString,
        "IrpStatus" / Int32ul,
        "IoctlControlCode" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=505, version=1)
class Microsoft_Windows_StorDiag_505_1(Etw):
    pattern = Struct(
        "DeviceGUID" / Guid,
        "DeviceNumber" / Int32ul,
        "Vendor" / CString,
        "Model" / CString,
        "FirmwareVersion" / CString,
        "SerialNumber" / CString,
        "DownLevelIrpStatus" / Int32ul,
        "SrbStatus" / Int8ul,
        "ScsiStatus" / Int8ul,
        "SenseKey" / Int8ul,
        "AdditionalSenseCode" / Int8ul,
        "AdditionalSenseCodeQualifier" / Int8ul,
        "CdbByteCount" / Int32ul,
        "CdbBytes" / Bytes(lambda this: this.CdbByteCount),
        "NumberOfRetriesDone" / Int8ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=506, version=1)
class Microsoft_Windows_StorDiag_506_1(Etw):
    pattern = Struct(
        "DeviceGUID" / Guid,
        "DeviceNumber" / Int32ul,
        "Vendor" / CString,
        "Model" / CString,
        "FirmwareVersion" / CString,
        "SerialNumber" / CString,
        "DownLevelIrpStatus" / Int32ul,
        "SrbStatus" / Int8ul,
        "ScsiStatus" / Int8ul,
        "SenseKey" / Int8ul,
        "AdditionalSenseCode" / Int8ul,
        "AdditionalSenseCodeQualifier" / Int8ul,
        "CdbByteCount" / Int32ul,
        "CdbBytes" / Bytes(lambda this: this.CdbByteCount),
        "NumberOfRetriesDone" / Int8ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=507, version=1)
class Microsoft_Windows_StorDiag_507_1(Etw):
    pattern = Struct(
        "DeviceGUID" / Guid,
        "DeviceNumber" / Int32ul,
        "Vendor" / CString,
        "Model" / CString,
        "FirmwareVersion" / CString,
        "SerialNumber" / CString,
        "DownLevelIrpStatus" / Int32ul,
        "SrbStatus" / Int8ul,
        "ScsiStatus" / Int8ul,
        "SenseKey" / Int8ul,
        "AdditionalSenseCode" / Int8ul,
        "AdditionalSenseCodeQualifier" / Int8ul,
        "CdbByteCount" / Int32ul,
        "CdbBytes" / Bytes(lambda this: this.CdbByteCount),
        "NumberOfRetriesDone" / Int8ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=508, version=1)
class Microsoft_Windows_StorDiag_508_1(Etw):
    pattern = Struct(
        "DeviceGUID" / Guid,
        "DeviceNumber" / Int32ul,
        "Vendor" / CString,
        "Model" / CString,
        "FirmwareVersion" / CString,
        "SerialNumber" / CString,
        "DownLevelIrpStatus" / Int32ul,
        "SrbStatus" / Int8ul,
        "SrbFunction" / Int32ul,
        "SrbFlags" / Int32ul,
        "NumberOfRetriesDone" / Int8ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=509, version=1)
class Microsoft_Windows_StorDiag_509_1(Etw):
    pattern = Struct(
        "DeviceGUID" / Guid,
        "DeviceNumber" / Int32ul,
        "Vendor" / CString,
        "Model" / CString,
        "FirmwareVersion" / CString,
        "SerialNumber" / CString,
        "IrpStatus" / Int32ul,
        "IrpMinorFunction" / Int8ul,
        "PnPType" / Int32ul,
        "PnPUsageInPath" / Int8ul,
        "CurrentPnpState" / Int32ul,
        "PreviousPnpState" / Int32ul,
        "PagingPathUsageCount" / Int32ul,
        "HibernationPathUsageCount" / Int32ul,
        "DumpPathUsageCount" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=510, version=1)
class Microsoft_Windows_StorDiag_510_1(Etw):
    pattern = Struct(
        "DeviceGUID" / Guid,
        "DeviceNumber" / Int32ul,
        "Vendor" / CString,
        "Model" / CString,
        "FirmwareVersion" / CString,
        "SerialNumber" / CString,
        "IrpStatus" / Int32ul,
        "IrpMinorFunction" / Int8ul,
        "PowerSystemContext" / Int32ul,
        "PowerStateType" / Int32ul,
        "PowerState" / Int32ul,
        "PowerShutdownType" / Int32ul,
        "CurrentPowerState" / Int32ul,
        "ContextPowerChangeState" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=511, version=1)
class Microsoft_Windows_StorDiag_511_1(Etw):
    pattern = Struct(
        "DeviceGUID" / Guid,
        "DeviceNumber" / Int32ul,
        "Vendor" / CString,
        "Model" / CString,
        "FirmwareVersion" / CString,
        "SerialNumber" / CString,
        "IrpStatus" / Int32ul,
        "IrpMinorFunction" / Int8ul,
        "WmiDataBlockGUID" / Guid,
        "WmiProviderId" / Int64ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=512, version=1)
class Microsoft_Windows_StorDiag_512_1(Etw):
    pattern = Struct(
        "DeviceGUID" / Guid,
        "Status" / Int32ul,
        "InputBufferLength" / Int32ul,
        "OutputBufferLength" / Int32ul,
        "DeviceNumber" / Int32ul,
        "PortDriverCodeSet" / Int32ul,
        "FirmwareGetInfoSupport" / Int32ul,
        "QueryFlag" / Int32ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=513, version=1)
class Microsoft_Windows_StorDiag_513_1(Etw):
    pattern = Struct(
        "DeviceGUID" / Guid,
        "Status" / Int32ul,
        "InputBufferLength" / Int32ul,
        "DeviceNumber" / Int32ul,
        "PortDriverCodeSet" / Int32ul,
        "FirmwareGetInfoSupport" / Int32ul,
        "HWFirmwareSupportUpgrade" / Int8ul,
        "ImagePayloadAlignment" / Int32ul,
        "SlotCount" / Int8ul,
        "SlotIndex" / Int32ul,
        "FWImageVersion" / Int32ul,
        "FWSize" / Int32ul,
        "FWSlot" / Int8ul,
        "FWImageBufferSize" / Int64ul,
        "Flags" / Int32ul,
        "FWImageOffset" / Int64ul
    )


@declare(guid=guid("f5d05b38-80a6-4653-825d-c414e4ab3c68"), event_id=514, version=1)
class Microsoft_Windows_StorDiag_514_1(Etw):
    pattern = Struct(
        "DeviceGUID" / Guid,
        "Status" / Int32ul,
        "InputBufferLength" / Int32ul,
        "DeviceNumber" / Int32ul,
        "PortDriverCodeSet" / Int32ul,
        "FirmwareGetInfoSupport" / Int32ul,
        "HWFirmwareSupportUpgrade" / Int8ul,
        "SlotCount" / Int8ul,
        "SlotIndex" / Int32ul,
        "FWImageVersion" / Int32ul,
        "FWSize" / Int32ul,
        "FWSlot" / Int8ul,
        "Flags" / Int32ul
    )

