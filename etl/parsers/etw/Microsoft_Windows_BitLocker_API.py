# -*- coding: utf-8 -*-
"""
Microsoft-Windows-BitLocker-API
GUID : 5d674230-ca9f-11da-a94d-0800200c9a66
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=513, version=0)
class Microsoft_Windows_BitLocker_API_513_0(Etw):
    pattern = Struct(
        "ProtectorGUID" / Guid,
        "VolumeGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=514, version=0)
class Microsoft_Windows_BitLocker_API_514_0(Etw):
    pattern = Struct(
        "ProtectorGUID" / Guid,
        "ErrorCode" / Int32ul,
        "VolumeGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=515, version=0)
class Microsoft_Windows_BitLocker_API_515_0(Etw):
    pattern = Struct(
        "ProtectorGUID" / Guid,
        "VolumeGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=516, version=0)
class Microsoft_Windows_BitLocker_API_516_0(Etw):
    pattern = Struct(
        "ProtectorGUID" / Guid,
        "Thumbprint" / WString,
        "VolumeGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=517, version=0)
class Microsoft_Windows_BitLocker_API_517_0(Etw):
    pattern = Struct(
        "ProtectorGUID" / Guid,
        "Thumbprint" / WString,
        "VolumeGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=518, version=0)
class Microsoft_Windows_BitLocker_API_518_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Thumbprint" / WString,
        "VolumeGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=519, version=0)
class Microsoft_Windows_BitLocker_API_519_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "VolumeGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=520, version=0)
class Microsoft_Windows_BitLocker_API_520_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "VolumeGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=521, version=0)
class Microsoft_Windows_BitLocker_API_521_0(Etw):
    pattern = Struct(
        "VolumeGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=522, version=0)
class Microsoft_Windows_BitLocker_API_522_0(Etw):
    pattern = Struct(
        "BootApplication" / WString,
        "VolumeGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=523, version=0)
class Microsoft_Windows_BitLocker_API_523_0(Etw):
    pattern = Struct(
        "BCDSetting" / Int32ul,
        "BootApplication" / WString,
        "VolumeGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=524, version=0)
class Microsoft_Windows_BitLocker_API_524_0(Etw):
    pattern = Struct(
        "VolumeGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=525, version=0)
class Microsoft_Windows_BitLocker_API_525_0(Etw):
    pattern = Struct(
        "VolumeGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=526, version=0)
class Microsoft_Windows_BitLocker_API_526_0(Etw):
    pattern = Struct(
        "VolumeGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=527, version=0)
class Microsoft_Windows_BitLocker_API_527_0(Etw):
    pattern = Struct(
        "VolumeGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=528, version=0)
class Microsoft_Windows_BitLocker_API_528_0(Etw):
    pattern = Struct(
        "VolumeGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=529, version=0)
class Microsoft_Windows_BitLocker_API_529_0(Etw):
    pattern = Struct(
        "VolumeGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=530, version=0)
class Microsoft_Windows_BitLocker_API_530_0(Etw):
    pattern = Struct(
        "VolumeGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=531, version=0)
class Microsoft_Windows_BitLocker_API_531_0(Etw):
    pattern = Struct(
        "VolumeGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=768, version=0)
class Microsoft_Windows_BitLocker_API_768_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "AlgorithmType" / Int16ul
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=769, version=0)
class Microsoft_Windows_BitLocker_API_769_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "AlgorithmType" / Int16ul
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=770, version=0)
class Microsoft_Windows_BitLocker_API_770_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=771, version=0)
class Microsoft_Windows_BitLocker_API_771_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=772, version=0)
class Microsoft_Windows_BitLocker_API_772_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "AlgorithmType" / Int16ul
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=773, version=0)
class Microsoft_Windows_BitLocker_API_773_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=774, version=0)
class Microsoft_Windows_BitLocker_API_774_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=775, version=0)
class Microsoft_Windows_BitLocker_API_775_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ProtectorGUID" / Guid,
        "ProtectorType" / Int32ul
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=776, version=0)
class Microsoft_Windows_BitLocker_API_776_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ProtectorGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=777, version=0)
class Microsoft_Windows_BitLocker_API_777_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ProtectorGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=778, version=0)
class Microsoft_Windows_BitLocker_API_778_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=779, version=0)
class Microsoft_Windows_BitLocker_API_779_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=780, version=0)
class Microsoft_Windows_BitLocker_API_780_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=781, version=0)
class Microsoft_Windows_BitLocker_API_781_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=782, version=0)
class Microsoft_Windows_BitLocker_API_782_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ProtectorGUID" / Guid,
        "ProtectorType" / Int32ul
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=783, version=0)
class Microsoft_Windows_BitLocker_API_783_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ProtectorGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=784, version=0)
class Microsoft_Windows_BitLocker_API_784_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ProtectorGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=785, version=0)
class Microsoft_Windows_BitLocker_API_785_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ProtectorGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=786, version=0)
class Microsoft_Windows_BitLocker_API_786_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=787, version=0)
class Microsoft_Windows_BitLocker_API_787_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=788, version=0)
class Microsoft_Windows_BitLocker_API_788_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=790, version=0)
class Microsoft_Windows_BitLocker_API_790_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=792, version=0)
class Microsoft_Windows_BitLocker_API_792_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=793, version=0)
class Microsoft_Windows_BitLocker_API_793_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=794, version=0)
class Microsoft_Windows_BitLocker_API_794_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=795, version=0)
class Microsoft_Windows_BitLocker_API_795_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=796, version=0)
class Microsoft_Windows_BitLocker_API_796_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=797, version=0)
class Microsoft_Windows_BitLocker_API_797_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=798, version=0)
class Microsoft_Windows_BitLocker_API_798_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=799, version=0)
class Microsoft_Windows_BitLocker_API_799_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=800, version=0)
class Microsoft_Windows_BitLocker_API_800_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=801, version=0)
class Microsoft_Windows_BitLocker_API_801_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=802, version=0)
class Microsoft_Windows_BitLocker_API_802_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ExpectedKeyLength" / Int32sl,
        "ActualKeyLength" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=803, version=0)
class Microsoft_Windows_BitLocker_API_803_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ExpectedKeyLength" / Int32sl,
        "ActualKeyLength" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=804, version=0)
class Microsoft_Windows_BitLocker_API_804_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=805, version=0)
class Microsoft_Windows_BitLocker_API_805_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "ProtectorGUID" / Guid,
        "ProtectorType" / Int32ul,
        "UnlockTime" / SystemTime
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=806, version=0)
class Microsoft_Windows_BitLocker_API_806_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "ResealTime" / SystemTime
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=807, version=0)
class Microsoft_Windows_BitLocker_API_807_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=808, version=0)
class Microsoft_Windows_BitLocker_API_808_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=811, version=0)
class Microsoft_Windows_BitLocker_API_811_0(Etw):
    pattern = Struct(
        "VariableName" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=812, version=0)
class Microsoft_Windows_BitLocker_API_812_0(Etw):
    pattern = Struct(
        "VariableName" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=813, version=0)
class Microsoft_Windows_BitLocker_API_813_0(Etw):
    pattern = Struct(
        "VariableName" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=817, version=0)
class Microsoft_Windows_BitLocker_API_817_0(Etw):
    pattern = Struct(
        "PCRBitmap" / Int32ul,
        "PCRBitmapSource" / Int32ul,
        "PCRValuesSize" / Int32ul,
        "PCRValues" / Bytes(lambda this: this.PCRValuesSize),
        "FilteredTcgLogSize" / Int32ul,
        "FilteredTcgLog" / Bytes(lambda this: this.FilteredTcgLogSize)
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=818, version=0)
class Microsoft_Windows_BitLocker_API_818_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=819, version=0)
class Microsoft_Windows_BitLocker_API_819_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=820, version=0)
class Microsoft_Windows_BitLocker_API_820_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=821, version=0)
class Microsoft_Windows_BitLocker_API_821_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=822, version=0)
class Microsoft_Windows_BitLocker_API_822_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=823, version=0)
class Microsoft_Windows_BitLocker_API_823_0(Etw):
    pattern = Struct(
        "VolumeGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=824, version=0)
class Microsoft_Windows_BitLocker_API_824_0(Etw):
    pattern = Struct(
        "VolumeGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=825, version=0)
class Microsoft_Windows_BitLocker_API_825_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=827, version=0)
class Microsoft_Windows_BitLocker_API_827_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=828, version=0)
class Microsoft_Windows_BitLocker_API_828_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ProtectorGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=829, version=0)
class Microsoft_Windows_BitLocker_API_829_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=831, version=0)
class Microsoft_Windows_BitLocker_API_831_0(Etw):
    pattern = Struct(
        "JsonErrorCode" / Int32sl,
        "LocalizedJsonError" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=832, version=0)
class Microsoft_Windows_BitLocker_API_832_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=834, version=0)
class Microsoft_Windows_BitLocker_API_834_0(Etw):
    pattern = Struct(
        "PCRBitmap" / Int32ul,
        "PCRBitmapSource" / Int32ul,
        "PCRValuesSize" / Int32ul,
        "PCRValues" / Bytes(lambda this: this.PCRValuesSize),
        "FilteredTcgLogSize" / Int32ul,
        "FilteredTcgLog" / Bytes(lambda this: this.FilteredTcgLogSize)
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=840, version=0)
class Microsoft_Windows_BitLocker_API_840_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "BinaryDataSize" / Int32ul,
        "BinaryData" / Bytes(lambda this: this.BinaryDataSize)
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=841, version=0)
class Microsoft_Windows_BitLocker_API_841_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=842, version=0)
class Microsoft_Windows_BitLocker_API_842_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=843, version=0)
class Microsoft_Windows_BitLocker_API_843_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "ResealTime" / SystemTime
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=844, version=0)
class Microsoft_Windows_BitLocker_API_844_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=845, version=0)
class Microsoft_Windows_BitLocker_API_845_0(Etw):
    pattern = Struct(
        "VolumeMountPoint" / WString,
        "ProtectorGUID" / Guid,
        "TraceGUID" / Guid
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=846, version=0)
class Microsoft_Windows_BitLocker_API_846_0(Etw):
    pattern = Struct(
        "VolumeMountPoint" / WString,
        "TraceGUID" / Guid,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=847, version=0)
class Microsoft_Windows_BitLocker_API_847_0(Etw):
    pattern = Struct(
        "JsonErrorCode" / Int32sl,
        "LocalizedJsonError" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=848, version=0)
class Microsoft_Windows_BitLocker_API_848_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=849, version=0)
class Microsoft_Windows_BitLocker_API_849_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=850, version=0)
class Microsoft_Windows_BitLocker_API_850_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=851, version=0)
class Microsoft_Windows_BitLocker_API_851_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=852, version=0)
class Microsoft_Windows_BitLocker_API_852_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=853, version=0)
class Microsoft_Windows_BitLocker_API_853_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=854, version=0)
class Microsoft_Windows_BitLocker_API_854_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=856, version=0)
class Microsoft_Windows_BitLocker_API_856_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=858, version=0)
class Microsoft_Windows_BitLocker_API_858_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=859, version=0)
class Microsoft_Windows_BitLocker_API_859_0(Etw):
    pattern = Struct(
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ProtectorGUID" / Guid,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=860, version=0)
class Microsoft_Windows_BitLocker_API_860_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=861, version=0)
class Microsoft_Windows_BitLocker_API_861_0(Etw):
    pattern = Struct(
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ProtectorGUID" / Guid,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=862, version=0)
class Microsoft_Windows_BitLocker_API_862_0(Etw):
    pattern = Struct(
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ProtectorGUID" / Guid,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=863, version=0)
class Microsoft_Windows_BitLocker_API_863_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=4096, version=0)
class Microsoft_Windows_BitLocker_API_4096_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=4099, version=0)
class Microsoft_Windows_BitLocker_API_4099_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=4102, version=0)
class Microsoft_Windows_BitLocker_API_4102_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=4103, version=0)
class Microsoft_Windows_BitLocker_API_4103_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=4106, version=0)
class Microsoft_Windows_BitLocker_API_4106_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=4111, version=0)
class Microsoft_Windows_BitLocker_API_4111_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=4112, version=0)
class Microsoft_Windows_BitLocker_API_4112_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=4113, version=0)
class Microsoft_Windows_BitLocker_API_4113_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=4114, version=0)
class Microsoft_Windows_BitLocker_API_4114_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=4116, version=0)
class Microsoft_Windows_BitLocker_API_4116_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=4117, version=0)
class Microsoft_Windows_BitLocker_API_4117_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=4118, version=0)
class Microsoft_Windows_BitLocker_API_4118_0(Etw):
    pattern = Struct(
        "IdentificationGUID" / Guid,
        "VolumeName" / WString,
        "VolumeMountPoint" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("5d674230-ca9f-11da-a94d-0800200c9a66"), event_id=4123, version=0)
class Microsoft_Windows_BitLocker_API_4123_0(Etw):
    pattern = Struct(
        "VolumeMountPoint" / WString,
        "ProtectorGUIDs" / WString,
        "TraceGUID" / Guid
    )

