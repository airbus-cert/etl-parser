# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SEC
GUID : 16c6501a-ff2d-46ea-868d-8f96cb0cb52d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=1, version=0)
class Microsoft_Windows_SEC_1_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "CreatorProcessId" / Int32ul,
        "CreatorProcessTime" / Int64sl,
        "CreatorProcessName" / WString,
        "ProcessName" / WString,
        "CommandLine" / WString,
        "PartialCRC1" / Int32ul,
        "PartialCRC2" / Int32ul,
        "PartialCRC3" / Int32ul,
        "MotW" / Int8ul,
        "IntegrityLevel" / Int32ul,
        "TokenElevationType" / Int32ul,
        "Elevated" / Int8ul,
        "Impersonation" / Int8ul,
        "SubjectLogonId" / Int64ul,
        "ProcessStartKey" / Int64ul,
        "CreatorProcessStartKey" / Int64ul,
        "CommandLineTruncated" / Int8ul,
        "CommandLineSize" / Int32ul,
        "MitigationPolicy" / Int64ul,
        "ProtectionLevel" / Int8ul,
        "EnterprisePolicy" / Int32ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=2, version=0)
class Microsoft_Windows_SEC_2_0(Etw):
    pattern = Struct(
        "DriverUnloadTime" / Int64sl
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=3, version=0)
class Microsoft_Windows_SEC_3_0(Etw):
    pattern = Struct(
        "DriverLoadTime" / Int64sl
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=4, version=0)
class Microsoft_Windows_SEC_4_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "FileName" / WString,
        "FileAttributes" / Int32ul,
        "Dispositon" / Int32ul,
        "ProcessStartKey" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=5, version=0)
class Microsoft_Windows_SEC_5_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "FileName" / WString,
        "NewFileName" / WString,
        "FileAttributes" / Int32ul,
        "ProcessStartKey" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=6, version=0)
class Microsoft_Windows_SEC_6_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "FileName" / WString,
        "FileAttributes" / Int32ul,
        "ProcessStartKey" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=7, version=0)
class Microsoft_Windows_SEC_7_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "FileName" / WString,
        "FileAttributes" / Int32ul,
        "ProcessStartKey" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=8, version=0)
class Microsoft_Windows_SEC_8_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "Key" / WString,
        "ProcessStartKey" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=9, version=0)
class Microsoft_Windows_SEC_9_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "Key" / WString,
        "ProcessStartKey" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=10, version=0)
class Microsoft_Windows_SEC_10_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "Key" / WString,
        "NewKey" / WString,
        "ProcessStartKey" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=11, version=0)
class Microsoft_Windows_SEC_11_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "Key" / WString,
        "Hive" / WString,
        "RestoreFlags" / Int32ul,
        "ProcessStartKey" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=12, version=0)
class Microsoft_Windows_SEC_12_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "Key" / WString,
        "Hive" / WString,
        "NewHive" / WString,
        "ProcessStartKey" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=13, version=0)
class Microsoft_Windows_SEC_13_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "Key" / WString,
        "Value" / WString,
        "OldValueDataType" / Int32ul,
        "OldValueDataSize" / Int32ul,
        "OldValueCopiedSize" / Int32ul,
        "OldValueData" / Bytes(lambda this: this.OldValueCopiedSize),
        "NewValueDataType" / Int32ul,
        "NewValueDataSize" / Int32ul,
        "NewValueCopiedSize" / Int32ul,
        "NewValueData" / Bytes(lambda this: this.NewValueCopiedSize),
        "ProcessStartKey" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=16, version=0)
class Microsoft_Windows_SEC_16_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "Key" / WString,
        "Value" / WString,
        "DataType" / Int32ul,
        "ValueDataSize" / Int32ul,
        "ValueCopiedSize" / Int32ul,
        "ValueData" / Bytes(lambda this: this.ValueCopiedSize),
        "ProcessStartKey" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=17, version=0)
class Microsoft_Windows_SEC_17_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "ImageName" / WString,
        "DocumentName" / WString,
        "ProcessStartKey" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=18, version=0)
class Microsoft_Windows_SEC_18_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessTime" / Int64sl,
        "TargetProcessName" / WString,
        "TargetThreadId" / Int32ul,
        "TargetThreadStartAddress" / Int64ul,
        "StartAddressVadQueryResult" / Int32ul,
        "StartAddressVadAllocationBase" / Int64ul,
        "StartAddressVadAllocationProtect" / Int32ul,
        "StartAddressVadRegionType" / Int32ul,
        "StartAddressVadRegionSize" / Int64ul,
        "StartAddressVadProtect" / Int32ul,
        "SourceProcessStartKey" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "MappedModuleName" / WString
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=19, version=0)
class Microsoft_Windows_SEC_19_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessTime" / Int64sl,
        "TargetProcess" / WString,
        "Access" / Int32ul,
        "SourceProcessStartKey" / Int64ul,
        "TargetProcessStartKey" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=20, version=0)
class Microsoft_Windows_SEC_20_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "Desktop" / WString,
        "Access" / Int32ul,
        "Duplicate" / Int8ul,
        "Kernel" / Int8ul,
        "ProcessStartKey" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=21, version=0)
class Microsoft_Windows_SEC_21_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "VolumeName" / WString,
        "VolWriteOffset" / Int64ul,
        "VolWriteSize" / Int64ul,
        "SystemVolume" / Int8ul,
        "ProcessStartKey" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=22, version=0)
class Microsoft_Windows_SEC_22_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "ProcessName" / WString,
        "CommandLine" / WString,
        "ProcessStartKey" / Int64ul,
        "CommandLineTruncated" / Int8ul,
        "CommandLineSize" / Int32ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=23, version=0)
class Microsoft_Windows_SEC_23_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "ImageName" / WString,
        "MotW" / Int8ul,
        "PartialCRC1" / Int32ul,
        "PartialCRC2" / Int32ul,
        "PartialCRC3" / Int32ul,
        "SystemModeImage" / Int8ul,
        "LoadImageAddress" / Int64ul,
        "ProcessStartKey" / Int64ul,
        "LoadImageSize" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=24, version=0)
class Microsoft_Windows_SEC_24_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "ImageName" / WString,
        "MotW" / Int8ul,
        "PartialCRC1" / Int32ul,
        "PartialCRC2" / Int32ul,
        "PartialCRC3" / Int32ul,
        "ImageSignatureLevel" / Int32ul,
        "ImageSignatureType" / Int32ul,
        "CurrentCodeIntegrityOptions" / Int32ul,
        "OriginalCodeIntegrityOptions" / Int32ul,
        "ProcessStartKey" / Int64ul,
        "ImageBase" / Int64ul,
        "ImageSize" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=25, version=0)
class Microsoft_Windows_SEC_25_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "AffectedProcessId" / Int32ul,
        "AffectedProcessTime" / Int64sl,
        "CurrentTokenPointer" / Int64ul,
        "CurrentTokenPrivPresent" / Int64ul,
        "CurrentTokenPrivEnabled" / Int64ul,
        "CurrentTokenPrivEnabledByDefault" / Int64ul,
        "CurrentTokenIntegrityLevel" / Int32ul,
        "CurrentTokenUserSid" / Sid,
        "PreviousTokenPointer" / Int64ul,
        "PreviousTokenPrivPresent" / Int64ul,
        "PreviousTokenPrivEnabled" / Int64ul,
        "PreviousTokenPrivEnabledByDefault" / Int64ul,
        "PreviousTokenIntegrityLevel" / Int32ul,
        "PreviousTokenUserSid" / Sid,
        "OriginalTokenPointer" / Int64ul,
        "OriginalTokenPrivPresent" / Int64ul,
        "OriginalTokenPrivEnabled" / Int64ul,
        "OriginalTokenPrivEnabledByDefault" / Int64ul,
        "OriginalTokenIntegrityLevel" / Int32ul,
        "OriginalTokenUserSid" / Sid,
        "SystemTokenPointer" / Int64ul,
        "InlineCheck" / Int8ul,
        "AffectedProcessStartKey" / Int64ul,
        "PrimaryTokenFrozen" / Int8ul,
        "ParentTokenIntegrityLevel" / Int32ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=27, version=0)
class Microsoft_Windows_SEC_27_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "AffectedProcessId" / Int32ul,
        "AffectedProcessStartKey" / Int64ul,
        "AffectedProcessTime" / Int64sl,
        "InlineCheck" / Int8ul,
        "CurrentDaclPointer" / Int64ul,
        "CurrentDaclValidAceList" / Int8ul,
        "CurrentDaclAceCount" / Int32ul,
        "CurrentDaclSids" / WString,
        "CurrentDaclAccessMaskBlobSize" / Int32ul,
        "CurrentDaclAccessMasks" / Bytes(lambda this: this.CurrentDaclAccessMaskBlobSize),
        "PreviousDaclPointer" / Int64ul,
        "PreviousDaclValidAceList" / Int8ul,
        "PreviousDaclAceCount" / Int32ul,
        "PreviousDaclSids" / WString,
        "PreviousDaclAccessMaskBlobSize" / Int32ul,
        "PreviousDaclAccessMasks" / Bytes(lambda this: this.PreviousDaclAccessMaskBlobSize),
        "OriginalDaclPointer" / Int64ul,
        "OriginalDaclValidAceList" / Int8ul,
        "OriginalDaclAceCount" / Int32ul,
        "OriginalDaclSids" / WString,
        "OriginalDaclAccessMaskBlobSize" / Int32ul,
        "OriginalDaclAccessMasks" / Bytes(lambda this: this.OriginalDaclAccessMaskBlobSize)
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=28, version=0)
class Microsoft_Windows_SEC_28_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessStartKey" / Int64ul,
        "Flags" / Int32ul,
        "ThreadId" / Int32ul,
        "CallerAddress" / Int64ul,
        "StartAddress" / Int64ul,
        "BackTraceSize" / Int32ul,
        "BackTrace" / Bytes(lambda this: this.BackTraceSize),
        "TargetCodeSize" / Int32ul,
        "TargetCode" / Bytes(lambda this: this.TargetCodeSize),
        "CallerCodeSize" / Int32ul,
        "CallerCode" / Bytes(lambda this: this.CallerCodeSize)
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=29, version=0)
class Microsoft_Windows_SEC_29_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "CurrentValue" / Int64ul,
        "OriginalValue" / Int64ul,
        "IsSynchronous" / Int8ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=30, version=0)
class Microsoft_Windows_SEC_30_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "CurrentValue" / Int64ul,
        "PreviousValue" / Int64ul,
        "OriginalValue" / Int64ul,
        "IsSynchronous" / Int8ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=31, version=0)
class Microsoft_Windows_SEC_31_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "SuspiciousEntryIndex" / Int32ul,
        "TableSize" / Int32ul,
        "Table" / Bytes(lambda this: this.TableSize),
        "CodeSize" / Int32ul,
        "Code" / Bytes(lambda this: this.CodeSize)
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=32, version=0)
class Microsoft_Windows_SEC_32_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "SuspiciousPointerIndex" / Int32ul,
        "TableSize" / Int32ul,
        "Table" / Bytes(lambda this: this.TableSize),
        "CodeSize" / Int32ul,
        "Code" / Bytes(lambda this: this.CodeSize)
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=33, version=0)
class Microsoft_Windows_SEC_33_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "SuspiciousPointerIndex" / Int32ul,
        "TableSize" / Int32ul,
        "Table" / Bytes(lambda this: this.TableSize),
        "CodeSize" / Int32ul,
        "Code" / Bytes(lambda this: this.CodeSize)
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=34, version=0)
class Microsoft_Windows_SEC_34_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessTime" / Int64sl,
        "TargetProcess" / WString,
        "Access" / Int32ul,
        "SourceProcessStartKey" / Int64ul,
        "TargetProcessStartKey" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=35, version=0)
class Microsoft_Windows_SEC_35_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "FileName" / WString,
        "OriginalCreationTime" / Int64sl,
        "OriginalLastAccessTime" / Int64sl,
        "OriginalLastWriteTime" / Int64sl,
        "OriginalChangeTime" / Int64sl,
        "ModifiedCreationTime" / Int64sl,
        "ModifiedLastAccessTime" / Int64sl,
        "ModifiedLastWriteTime" / Int64sl,
        "ModifiedChangeTime" / Int64sl,
        "FileAttributes" / Int32ul,
        "ProcessStartKey" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=36, version=0)
class Microsoft_Windows_SEC_36_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "AffectedProcessId" / Int32ul,
        "AffectedProcessTime" / Int64sl,
        "AffectedProcessStartKey" / Int64ul,
        "InlineCheck" / Int8ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=37, version=0)
class Microsoft_Windows_SEC_37_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ImageName" / WString,
        "ImageBase" / Int64ul,
        "ImageSize" / Int64ul,
        "DriverName" / WString,
        "DriverObject" / Int64ul,
        "DriverInit" / Int64ul,
        "DriverStartIo" / Int64ul,
        "DriverUnload" / Int64ul,
        "MajorFunctionArraySize" / Int32ul,
        "MajorFunctionArray" / Bytes(lambda this: this.MajorFunctionArraySize),
        "FastIoDispatchArraySize" / Int32ul,
        "FastIoDispatchArray" / Bytes(lambda this: this.FastIoDispatchArraySize),
        "SuspiciousDispatchBitmap" / Int64ul,
        "ContextInfoArraySize" / Int32ul,
        "ContextInfoArray" / Bytes(lambda this: this.ContextInfoArraySize)
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=38, version=0)
class Microsoft_Windows_SEC_38_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ProcessStartKey" / Int64ul,
        "OldFlags" / Int64ul,
        "NewFlags" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=39, version=0)
class Microsoft_Windows_SEC_39_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "SourceThreadId" / Int32ul,
        "TargetThreadId" / Int32ul,
        "UserSid" / Sid,
        "TargetProcessId" / Int32ul,
        "TargetProcessTime" / Int64sl,
        "AccessMask" / Int32ul,
        "ProcessStartKey" / Int64ul,
        "TargetProcessStartKey" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=40, version=0)
class Microsoft_Windows_SEC_40_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "FileName" / WString,
        "FileAttributes" / Int32ul,
        "ProcessStartKey" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=41, version=0)
class Microsoft_Windows_SEC_41_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "Key" / WString,
        "Value" / WString,
        "ProcessStartKey" / Int64ul
    )


@declare(guid=guid("16c6501a-ff2d-46ea-868d-8f96cb0cb52d"), event_id=42, version=0)
class Microsoft_Windows_SEC_42_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64ul,
        "ProcessId" / Int32ul,
        "ProcessTime" / Int64sl,
        "ThreadId" / Int32ul,
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "FileName" / WString,
        "FileAttributes" / Int32ul,
        "DesiredAccess" / Int32ul,
        "Dispositon" / Int32ul,
        "ProcessStartKey" / Int64ul
    )

