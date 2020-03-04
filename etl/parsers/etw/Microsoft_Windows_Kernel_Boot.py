# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-Boot
GUID : 15ca44ff-4d7a-4baa-bba5-0998955e531e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=1, version=0)
class Microsoft_Windows_Kernel_Boot_1_0(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul,
        "BitsPerPixel" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=2, version=0)
class Microsoft_Windows_Kernel_Boot_2_0(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul,
        "BitsPerPixel" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=3, version=0)
class Microsoft_Windows_Kernel_Boot_3_0(Etw):
    pattern = Struct(
        "BytesPerMs" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=4, version=0)
class Microsoft_Windows_Kernel_Boot_4_0(Etw):
    pattern = Struct(
        "DeviceID" / Int32ul,
        "FileName" / WString,
        "BytesRead" / Int64ul,
        "BytesWritten" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=5, version=0)
class Microsoft_Windows_Kernel_Boot_5_0(Etw):
    pattern = Struct(
        "ApplicationGuid" / Guid,
        "BytesRead" / Int64ul,
        "BytesWritten" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=6, version=0)
class Microsoft_Windows_Kernel_Boot_6_0(Etw):
    pattern = Struct(
        "ImageName" / WString,
        "ImageFlags" / Int32ul,
        "Reason" / Int32ul,
        "ErrorIgnored" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=7, version=0)
class Microsoft_Windows_Kernel_Boot_7_0(Etw):
    pattern = Struct(
        "BootmgrTime" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=8, version=0)
class Microsoft_Windows_Kernel_Boot_8_0(Etw):
    pattern = Struct(
        "ImageName" / WString
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=9, version=0)
class Microsoft_Windows_Kernel_Boot_9_0(Etw):
    pattern = Struct(
        "DriveNumber" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=10, version=0)
class Microsoft_Windows_Kernel_Boot_10_0(Etw):
    pattern = Struct(
        "FwStartPage" / Int64ul,
        "FwPageCount" / Int64ul,
        "FwMemoryType" / Int32ul,
        "FwMemoryAttributes" / Int32ul,
        "BlStartPage" / Int64ul,
        "BlPageCount" / Int64ul,
        "BlMemoryType" / Int32ul,
        "BlMemoryAttributes" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=11, version=0)
class Microsoft_Windows_Kernel_Boot_11_0(Etw):
    pattern = Struct(
        "PreBootMgrTime" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=12, version=0)
class Microsoft_Windows_Kernel_Boot_12_0(Etw):
    pattern = Struct(
        "UefiVariableName" / WString,
        "Size" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=13, version=0)
class Microsoft_Windows_Kernel_Boot_13_0(Etw):
    pattern = Struct(
        "ApplicationGuid" / Guid,
        "Element" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=14, version=0)
class Microsoft_Windows_Kernel_Boot_14_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=15, version=0)
class Microsoft_Windows_Kernel_Boot_15_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=16, version=0)
class Microsoft_Windows_Kernel_Boot_16_0(Etw):
    pattern = Struct(
        "FailureStatus" / Int64ul,
        "FailureMsgId" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=16, version=1)
class Microsoft_Windows_Kernel_Boot_16_1(Etw):
    pattern = Struct(
        "FailureStatus" / Int32ul,
        "FailureMsg" / WString
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=18, version=0)
class Microsoft_Windows_Kernel_Boot_18_0(Etw):
    pattern = Struct(
        "EntryCount" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=19, version=0)
class Microsoft_Windows_Kernel_Boot_19_0(Etw):
    pattern = Struct(
        "ToolsCount" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=20, version=0)
class Microsoft_Windows_Kernel_Boot_20_0(Etw):
    pattern = Struct(
        "LastShutdownGood" / Int8ul,
        "LastBootGood" / Int8ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=20, version=1)
class Microsoft_Windows_Kernel_Boot_20_1(Etw):
    pattern = Struct(
        "LastShutdownGood" / Int8ul,
        "LastBootGood" / Int8ul,
        "LastBootId" / Int32ul,
        "BootStatusPolicy" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=21, version=0)
class Microsoft_Windows_Kernel_Boot_21_0(Etw):
    pattern = Struct(
        "OptionSelected" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=25, version=0)
class Microsoft_Windows_Kernel_Boot_25_0(Etw):
    pattern = Struct(
        "BootMenuPolicy" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=27, version=0)
class Microsoft_Windows_Kernel_Boot_27_0(Etw):
    pattern = Struct(
        "BootType" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=27, version=1)
class Microsoft_Windows_Kernel_Boot_27_1(Etw):
    pattern = Struct(
        "BootType" / Int32ul,
        "LoadOptions" / CString
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=28, version=0)
class Microsoft_Windows_Kernel_Boot_28_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=29, version=0)
class Microsoft_Windows_Kernel_Boot_29_0(Etw):
    pattern = Struct(
        "FailureStatus" / Int64ul,
        "FailureMsgId" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=29, version=1)
class Microsoft_Windows_Kernel_Boot_29_1(Etw):
    pattern = Struct(
        "FailureStatus" / Int32ul,
        "FailureMsg" / WString
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=30, version=0)
class Microsoft_Windows_Kernel_Boot_30_0(Etw):
    pattern = Struct(
        "ResetEndStart" / Int64ul,
        "LoadOSImageStart" / Int64ul,
        "StartOSImageStart" / Int64ul,
        "ExitBootServicesEntry" / Int64ul,
        "ExitBootServicesExit" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=31, version=0)
class Microsoft_Windows_Kernel_Boot_31_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=32, version=0)
class Microsoft_Windows_Kernel_Boot_32_0(Etw):
    pattern = Struct(
        "BitlockerUserInputTime" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=33, version=0)
class Microsoft_Windows_Kernel_Boot_33_0(Etw):
    pattern = Struct(
        "ImageName" / WString,
        "ImageLoadStatus" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=34, version=0)
class Microsoft_Windows_Kernel_Boot_34_0(Etw):
    pattern = Struct(
        "PeImageName" / WString,
        "PeImageLoadStatus" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=35, version=0)
class Microsoft_Windows_Kernel_Boot_35_0(Etw):
    pattern = Struct(
        "UpdateCapsuleStatus" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=36, version=0)
class Microsoft_Windows_Kernel_Boot_36_0(Etw):
    pattern = Struct(
        "DeviceFlags" / Int32ul,
        "PcrBitmap" / Int32ul,
        "UpdateSupportedStatus" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=37, version=0)
class Microsoft_Windows_Kernel_Boot_37_0(Etw):
    pattern = Struct(
        "ImageName" / WString,
        "ImageLoadStatus" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=38, version=0)
class Microsoft_Windows_Kernel_Boot_38_0(Etw):
    pattern = Struct(
        "ImageName" / WString,
        "ImageLoadStatus" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=39, version=0)
class Microsoft_Windows_Kernel_Boot_39_0(Etw):
    pattern = Struct(
        "HiveName" / WString,
        "HiveLoadStatus" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=40, version=0)
class Microsoft_Windows_Kernel_Boot_40_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=41, version=0)
class Microsoft_Windows_Kernel_Boot_41_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=42, version=0)
class Microsoft_Windows_Kernel_Boot_42_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "FailedPath" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=43, version=0)
class Microsoft_Windows_Kernel_Boot_43_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "Import" / CString,
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=44, version=0)
class Microsoft_Windows_Kernel_Boot_44_0(Etw):
    pattern = Struct(
        "CachedCopyStatus" / Int32ul,
        "IdkGenerationStatus" / Int32ul,
        "MeasuringStatus" / Int32ul,
        "SealingAndCachingStatus" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=45, version=0)
class Microsoft_Windows_Kernel_Boot_45_0(Etw):
    pattern = Struct(
        "CachedCopyStatus" / Int32ul,
        "IdkGenerationStatus" / Int32ul,
        "MeasuringStatus" / Int32ul,
        "SealingAndCachingStatus" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=46, version=0)
class Microsoft_Windows_Kernel_Boot_46_0(Etw):
    pattern = Struct(
        "RetrieveDriverListTime" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=47, version=0)
class Microsoft_Windows_Kernel_Boot_47_0(Etw):
    pattern = Struct(
        "LoadDriversTime" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=48, version=0)
class Microsoft_Windows_Kernel_Boot_48_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "LoadHiveTime" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=49, version=0)
class Microsoft_Windows_Kernel_Boot_49_0(Etw):
    pattern = Struct(
        "ImageName" / WString,
        "SiPolicyStatus" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=50, version=0)
class Microsoft_Windows_Kernel_Boot_50_0(Etw):
    pattern = Struct(
        "CachedCopyStatus" / Int32ul,
        "UnsealingCachedCopyStatus" / Int32ul,
        "KeyGenerationAndSaveStatus" / Int32ul,
        "SealingStatus" / Int32ul,
        "TpmPcrMask" / Int32ul,
        "ProtectorAssistedUnsealStatus" / Int32ul,
        "ProtectorAssistedResealStatus" / Int32ul,
        "ProtectorSealUpdateStatus" / Int32ul,
        "TpmCounterOpStatus" / Int32ul,
        "TpmCounterCreateStatus" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=51, version=0)
class Microsoft_Windows_Kernel_Boot_51_0(Etw):
    pattern = Struct(
        "CachedCopyStatus" / Int32ul,
        "UnsealingCachedCopyStatus" / Int32ul,
        "KeyGenerationAndSaveStatus" / Int32ul,
        "SealingStatus" / Int32ul,
        "TpmPcrMask" / Int32ul,
        "ProtectorAssistedUnsealStatus" / Int32ul,
        "ProtectorAssistedResealStatus" / Int32ul,
        "ProtectorSealUpdateStatus" / Int32ul,
        "TpmCounterOpStatus" / Int32ul,
        "TpmCounterCreateStatus" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=52, version=0)
class Microsoft_Windows_Kernel_Boot_52_0(Etw):
    pattern = Struct(
        "ApplicationIdentifier" / Guid,
        "ApplicationLoadTime" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=53, version=0)
class Microsoft_Windows_Kernel_Boot_53_0(Etw):
    pattern = Struct(
        "ApplicationIdentifier" / Guid,
        "ApplicationExecutionTime" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=54, version=0)
class Microsoft_Windows_Kernel_Boot_54_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "FileName" / WString
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=55, version=0)
class Microsoft_Windows_Kernel_Boot_55_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "FailurePoint" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=56, version=0)
class Microsoft_Windows_Kernel_Boot_56_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=57, version=0)
class Microsoft_Windows_Kernel_Boot_57_0(Etw):
    pattern = Struct(
        "TpmSrkProvisioningStatus" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=58, version=0)
class Microsoft_Windows_Kernel_Boot_58_0(Etw):
    pattern = Struct(
        "TpmSrkProvisioningTime" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=59, version=0)
class Microsoft_Windows_Kernel_Boot_59_0(Etw):
    pattern = Struct(
        "TpmBindingProvisioningStatus" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=61, version=0)
class Microsoft_Windows_Kernel_Boot_61_0(Etw):
    pattern = Struct(
        "PmrLowBase" / Int64ul,
        "PmrLowSize" / Int64ul,
        "PmrHighBase" / Int64ul,
        "PmrHighSize" / Int64ul,
        "FirmwareProvidedAcm" / Int8ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=62, version=0)
class Microsoft_Windows_Kernel_Boot_62_0(Etw):
    pattern = Struct(
        "TxtErrorCode" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=63, version=0)
class Microsoft_Windows_Kernel_Boot_63_0(Etw):
    pattern = Struct(
        "Base" / Int64ul,
        "Size" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=64, version=0)
class Microsoft_Windows_Kernel_Boot_64_0(Etw):
    pattern = Struct(
        "Base" / Int64ul,
        "Size" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=65, version=0)
class Microsoft_Windows_Kernel_Boot_65_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=66, version=0)
class Microsoft_Windows_Kernel_Boot_66_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=67, version=0)
class Microsoft_Windows_Kernel_Boot_67_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=68, version=0)
class Microsoft_Windows_Kernel_Boot_68_0(Etw):
    pattern = Struct(
        "BiosDataSize" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=69, version=0)
class Microsoft_Windows_Kernel_Boot_69_0(Etw):
    pattern = Struct(
        "AcmMinMleHeaderVer" / Int32ul,
        "MleHeaderVersion" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=70, version=0)
class Microsoft_Windows_Kernel_Boot_70_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=71, version=0)
class Microsoft_Windows_Kernel_Boot_71_0(Etw):
    pattern = Struct(
        "DeviceID" / Int32ul,
        "FileName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=72, version=0)
class Microsoft_Windows_Kernel_Boot_72_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=73, version=0)
class Microsoft_Windows_Kernel_Boot_73_0(Etw):
    pattern = Struct(
        "TxtStatus" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=74, version=0)
class Microsoft_Windows_Kernel_Boot_74_0(Etw):
    pattern = Struct(
        "CachedCopyStatus" / Int32ul,
        "KeyGenerationStatus" / Int32ul,
        "SealAndSaveStatus" / Int32ul,
        "UEFIKeysStatus" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=75, version=0)
class Microsoft_Windows_Kernel_Boot_75_0(Etw):
    pattern = Struct(
        "CachedCopyStatus" / Int32ul,
        "KeyGenerationStatus" / Int32ul,
        "SealAndSaveStatus" / Int32ul,
        "UEFIKeysStatus" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=77, version=0)
class Microsoft_Windows_Kernel_Boot_77_0(Etw):
    pattern = Struct(
        "DebuggerStatus" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=100, version=1)
class Microsoft_Windows_Kernel_Boot_100_1(Etw):
    pattern = Struct(
        "Secure" / Int8ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=101, version=0)
class Microsoft_Windows_Kernel_Boot_101_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=102, version=1)
class Microsoft_Windows_Kernel_Boot_102_1(Etw):
    pattern = Struct(
        "SoftRestartCount" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=102, version=2)
class Microsoft_Windows_Kernel_Boot_102_2(Etw):
    pattern = Struct(
        "SoftRestartCount" / Int32ul,
        "Secure" / Int8ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=103, version=0)
class Microsoft_Windows_Kernel_Boot_103_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=104, version=0)
class Microsoft_Windows_Kernel_Boot_104_0(Etw):
    pattern = Struct(
        "ReserveDescriptors" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=105, version=0)
class Microsoft_Windows_Kernel_Boot_105_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=106, version=0)
class Microsoft_Windows_Kernel_Boot_106_0(Etw):
    pattern = Struct(
        "ApplicationId" / Guid,
        "RunCount" / Int32ul,
        "PageCount" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=107, version=0)
class Microsoft_Windows_Kernel_Boot_107_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "BlockId" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=108, version=0)
class Microsoft_Windows_Kernel_Boot_108_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=109, version=0)
class Microsoft_Windows_Kernel_Boot_109_0(Etw):
    pattern = Struct(
        "FreePersistentPages" / Int8ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=110, version=0)
class Microsoft_Windows_Kernel_Boot_110_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=111, version=0)
class Microsoft_Windows_Kernel_Boot_111_0(Etw):
    pattern = Struct(
        "ApplicationId" / Guid,
        "FreePersistentPages" / Int8ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=112, version=0)
class Microsoft_Windows_Kernel_Boot_112_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=113, version=0)
class Microsoft_Windows_Kernel_Boot_113_0(Etw):
    pattern = Struct(
        "ApplicationId" / Guid,
        "BlockId" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=114, version=0)
class Microsoft_Windows_Kernel_Boot_114_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "RunsClaimed" / Int32ul,
        "PageCount" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=115, version=0)
class Microsoft_Windows_Kernel_Boot_115_0(Etw):
    pattern = Struct(
        "FreePersistentPages" / Int8ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=116, version=0)
class Microsoft_Windows_Kernel_Boot_116_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=118, version=0)
class Microsoft_Windows_Kernel_Boot_118_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=119, version=0)
class Microsoft_Windows_Kernel_Boot_119_0(Etw):
    pattern = Struct(
        "ApplicationId" / Guid,
        "BlockId" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=121, version=0)
class Microsoft_Windows_Kernel_Boot_121_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=122, version=0)
class Microsoft_Windows_Kernel_Boot_122_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Flags" / Int32ul,
        "BufferSize" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=123, version=0)
class Microsoft_Windows_Kernel_Boot_123_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "DataSize" / Int32ul,
        "BufferSize" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=124, version=0)
class Microsoft_Windows_Kernel_Boot_124_0(Etw):
    pattern = Struct(
        "Phase" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=126, version=0)
class Microsoft_Windows_Kernel_Boot_126_0(Etw):
    pattern = Struct(
        "LowAddress" / Int64ul,
        "HighAddress" / Int64ul,
        "SkipBytes" / Int64ul,
        "TotalBytes" / Int64ul,
        "CacheType" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=127, version=0)
class Microsoft_Windows_Kernel_Boot_127_0(Etw):
    pattern = Struct(
        "Mdl" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=128, version=0)
class Microsoft_Windows_Kernel_Boot_128_0(Etw):
    pattern = Struct(
        "StartTime" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=130, version=0)
class Microsoft_Windows_Kernel_Boot_130_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int32ul,
        "DescriptorCount" / Int32ul,
        "MemoryDescriptor" / Int8sl
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=132, version=0)
class Microsoft_Windows_Kernel_Boot_132_0(Etw):
    pattern = Struct(
        "DescriptorCount" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=133, version=0)
class Microsoft_Windows_Kernel_Boot_133_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "PageCount" / Int64ul,
        "MemoryType" / Int32ul,
        "Attributes" / Int32ul,
        "LowAddress" / Int64ul,
        "HighAddress" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=136, version=0)
class Microsoft_Windows_Kernel_Boot_136_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "OutstandingCount" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=137, version=0)
class Microsoft_Windows_Kernel_Boot_137_0(Etw):
    pattern = Struct(
        "Identifier" / Guid,
        "PartitionId" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=138, version=0)
class Microsoft_Windows_Kernel_Boot_138_0(Etw):
    pattern = Struct(
        "Identifier" / Guid,
        "PartitionPageCount" / Int64ul,
        "AllocatedBlockCount" / Int64ul,
        "AllocatedRunCount" / Int64ul,
        "AllocatedPageCount" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=139, version=0)
class Microsoft_Windows_Kernel_Boot_139_0(Etw):
    pattern = Struct(
        "Identifier" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=140, version=0)
class Microsoft_Windows_Kernel_Boot_140_0(Etw):
    pattern = Struct(
        "Identifier" / Guid
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=141, version=0)
class Microsoft_Windows_Kernel_Boot_141_0(Etw):
    pattern = Struct(
        "Identifier" / Guid,
        "RunCount" / Int32ul,
        "PageCount" / Int64ul,
        "Status" / Int32ul,
        "PartitionNameLength" / Int16ul,
        "PartitionName" / Bytes(lambda this: this.PartitionNameLength)
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=141, version=1)
class Microsoft_Windows_Kernel_Boot_141_1(Etw):
    pattern = Struct(
        "Identifier" / Guid,
        "RunCount" / Int32ul,
        "PageCount" / Int64ul,
        "IoSpaceRunCount" / Int32ul,
        "IoSpacePageCount" / Int64ul,
        "Status" / Int32ul,
        "PartitionNameLength" / Int16ul,
        "PartitionName" / Bytes(lambda this: this.PartitionNameLength)
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=142, version=0)
class Microsoft_Windows_Kernel_Boot_142_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "ActualSize" / Int32ul,
        "ExpectedSize" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=143, version=0)
class Microsoft_Windows_Kernel_Boot_143_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=145, version=0)
class Microsoft_Windows_Kernel_Boot_145_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=146, version=0)
class Microsoft_Windows_Kernel_Boot_146_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=147, version=0)
class Microsoft_Windows_Kernel_Boot_147_0(Etw):
    pattern = Struct(
        "ApplicationId" / Guid,
        "BlockId" / Int64ul,
        "FreePersistentPages" / Int8ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=148, version=0)
class Microsoft_Windows_Kernel_Boot_148_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=150, version=0)
class Microsoft_Windows_Kernel_Boot_150_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=151, version=0)
class Microsoft_Windows_Kernel_Boot_151_0(Etw):
    pattern = Struct(
        "PartitionId" / Int32ul,
        "RunCount" / Int32ul,
        "PageCount" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=151, version=1)
class Microsoft_Windows_Kernel_Boot_151_1(Etw):
    pattern = Struct(
        "PartitionId" / Int32ul,
        "RunCount" / Int32ul,
        "PageCount" / Int64ul,
        "IoSpaceMemory" / Int8ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=152, version=0)
class Microsoft_Windows_Kernel_Boot_152_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=153, version=0)
class Microsoft_Windows_Kernel_Boot_153_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "EnableDisableReason" / Int32ul,
        "VsmPolicy" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=154, version=0)
class Microsoft_Windows_Kernel_Boot_154_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=155, version=0)
class Microsoft_Windows_Kernel_Boot_155_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=156, version=0)
class Microsoft_Windows_Kernel_Boot_156_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "EnableDisableReason" / Int32ul,
        "VsmPolicy" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=157, version=0)
class Microsoft_Windows_Kernel_Boot_157_0(Etw):
    pattern = Struct(
        "DiagCode" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=158, version=0)
class Microsoft_Windows_Kernel_Boot_158_0(Etw):
    pattern = Struct(
        "DiagCode" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=159, version=0)
class Microsoft_Windows_Kernel_Boot_159_0(Etw):
    pattern = Struct(
        "BasePage" / Int64ul,
        "PageCount" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=160, version=0)
class Microsoft_Windows_Kernel_Boot_160_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=161, version=0)
class Microsoft_Windows_Kernel_Boot_161_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=162, version=0)
class Microsoft_Windows_Kernel_Boot_162_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=163, version=0)
class Microsoft_Windows_Kernel_Boot_163_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=164, version=0)
class Microsoft_Windows_Kernel_Boot_164_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=165, version=0)
class Microsoft_Windows_Kernel_Boot_165_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=166, version=0)
class Microsoft_Windows_Kernel_Boot_166_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=167, version=0)
class Microsoft_Windows_Kernel_Boot_167_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=168, version=0)
class Microsoft_Windows_Kernel_Boot_168_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=169, version=0)
class Microsoft_Windows_Kernel_Boot_169_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=170, version=0)
class Microsoft_Windows_Kernel_Boot_170_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=171, version=0)
class Microsoft_Windows_Kernel_Boot_171_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=172, version=0)
class Microsoft_Windows_Kernel_Boot_172_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=173, version=0)
class Microsoft_Windows_Kernel_Boot_173_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=174, version=0)
class Microsoft_Windows_Kernel_Boot_174_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=175, version=0)
class Microsoft_Windows_Kernel_Boot_175_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=176, version=0)
class Microsoft_Windows_Kernel_Boot_176_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=177, version=0)
class Microsoft_Windows_Kernel_Boot_177_0(Etw):
    pattern = Struct(
        "VendorGuid" / Guid,
        "VariableName" / WString,
        "Attributes" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=178, version=0)
class Microsoft_Windows_Kernel_Boot_178_0(Etw):
    pattern = Struct(
        "VendorGuid" / Guid,
        "VariableName" / WString,
        "Attributes" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=179, version=0)
class Microsoft_Windows_Kernel_Boot_179_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=180, version=0)
class Microsoft_Windows_Kernel_Boot_180_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=181, version=0)
class Microsoft_Windows_Kernel_Boot_181_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=182, version=0)
class Microsoft_Windows_Kernel_Boot_182_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=200, version=0)
class Microsoft_Windows_Kernel_Boot_200_0(Etw):
    pattern = Struct(
        "CommandCode" / Int32ul,
        "ResponseCode" / Int32ul,
        "ResponseMilliseconds" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=201, version=0)
class Microsoft_Windows_Kernel_Boot_201_0(Etw):
    pattern = Struct(
        "CommandCode" / Int32ul,
        "ResponseCode" / Int32ul,
        "ResponseMilliseconds" / Int64ul,
        "CommandSize" / Int32ul,
        "CommandData" / Bytes(lambda this: this.CommandSize),
        "ResponseSize" / Int32ul,
        "ResponseData" / Bytes(lambda this: this.ResponseSize)
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=202, version=0)
class Microsoft_Windows_Kernel_Boot_202_0(Etw):
    pattern = Struct(
        "CommandCode" / Int32ul,
        "ErrorCode" / Int32ul,
        "ResponseMilliseconds" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=203, version=0)
class Microsoft_Windows_Kernel_Boot_203_0(Etw):
    pattern = Struct(
        "CommandCode" / Int32ul,
        "ErrorCode" / Int32ul,
        "ResponseMilliseconds" / Int64ul,
        "CommandSize" / Int32ul,
        "CommandData" / Bytes(lambda this: this.CommandSize)
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=204, version=0)
class Microsoft_Windows_Kernel_Boot_204_0(Etw):
    pattern = Struct(
        "FveGlobalDataFlags" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=206, version=0)
class Microsoft_Windows_Kernel_Boot_206_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=207, version=0)
class Microsoft_Windows_Kernel_Boot_207_0(Etw):
    pattern = Struct(
        "Phase" / Int32ul,
        "StatusCode" / Int32ul,
        "EnvironmentState" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=208, version=0)
class Microsoft_Windows_Kernel_Boot_208_0(Etw):
    pattern = Struct(
        "InitState" / Int32ul,
        "StatusCode" / Int32ul,
        "FailureAddress" / Int64ul,
        "ReferenceAddress" / Int64ul,
        "ReasonCode" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=209, version=0)
class Microsoft_Windows_Kernel_Boot_209_0(Etw):
    pattern = Struct(
        "SvnCounterId" / Int32ul,
        "StatusCode" / Int32ul,
        "SvnValue" / Int32ul,
        "PrevSvnValue" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=210, version=0)
class Microsoft_Windows_Kernel_Boot_210_0(Etw):
    pattern = Struct(
        "SinitTimeMs" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=211, version=0)
class Microsoft_Windows_Kernel_Boot_211_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=212, version=0)
class Microsoft_Windows_Kernel_Boot_212_0(Etw):
    pattern = Struct(
        "PathLength" / Int16ul,
        "Path" / Bytes(lambda this: this.PathLength)
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=213, version=0)
class Microsoft_Windows_Kernel_Boot_213_0(Etw):
    pattern = Struct(
        "PathLength" / Int16ul,
        "Path" / Bytes(lambda this: this.PathLength)
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=214, version=0)
class Microsoft_Windows_Kernel_Boot_214_0(Etw):
    pattern = Struct(
        "TryComplete" / Int8ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=215, version=0)
class Microsoft_Windows_Kernel_Boot_215_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=217, version=0)
class Microsoft_Windows_Kernel_Boot_217_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=218, version=0)
class Microsoft_Windows_Kernel_Boot_218_0(Etw):
    pattern = Struct(
        "Function" / WString,
        "Status" / Int32ul,
        "Checkpoint" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=219, version=0)
class Microsoft_Windows_Kernel_Boot_219_0(Etw):
    pattern = Struct(
        "AcmDateDay" / Int8ul,
        "AcmDateMonth" / Int8ul,
        "AcmDateYear" / Int16ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=220, version=0)
class Microsoft_Windows_Kernel_Boot_220_0(Etw):
    pattern = Struct(
        "TxtStatus" / Int32ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=222, version=0)
class Microsoft_Windows_Kernel_Boot_222_0(Etw):
    pattern = Struct(
        "TxtStatus" / Int32ul,
        "Argument1" / Int64ul,
        "Argument2" / Int64ul
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=223, version=0)
class Microsoft_Windows_Kernel_Boot_223_0(Etw):
    pattern = Struct(
        "Phase" / Int32ul,
        "Status" / Int32ul,
        "Tries" / Int32ul,
        "RemainingNodesCount" / Int32ul,
        "RemainingNodes" / Int16sl
    )


@declare(guid=guid("15ca44ff-4d7a-4baa-bba5-0998955e531e"), event_id=224, version=0)
class Microsoft_Windows_Kernel_Boot_224_0(Etw):
    pattern = Struct(
        "AllocatedRegions" / Int32ul,
        "Tries" / Int32ul
    )

