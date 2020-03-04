# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Storage-Tiering
GUID : 4a104570-ec6d-4560-a40f-858fa955e84f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4a104570-ec6d-4560-a40f-858fa955e84f"), event_id=11, version=0)
class Microsoft_Windows_Storage_Tiering_11_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength)
    )


@declare(guid=guid("4a104570-ec6d-4560-a40f-858fa955e84f"), event_id=12, version=0)
class Microsoft_Windows_Storage_Tiering_12_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength)
    )


@declare(guid=guid("4a104570-ec6d-4560-a40f-858fa955e84f"), event_id=13, version=0)
class Microsoft_Windows_Storage_Tiering_13_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "CsvNameLength" / Int16ul,
        "CsvName" / Bytes(lambda this: this.CsvNameLength)
    )


@declare(guid=guid("4a104570-ec6d-4560-a40f-858fa955e84f"), event_id=21, version=0)
class Microsoft_Windows_Storage_Tiering_21_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "AskedToMoveToFlash" / Int64ul,
        "AskedToMoveToDisk" / Int64ul,
        "MovedToFlash" / Int64ul,
        "MovedToDisk" / Int64ul,
        "HResult" / Int32sl,
        "ProcessTimeInMinutes" / Int32sl,
        "DefragTimeInMinutes" / Int32sl
    )


@declare(guid=guid("4a104570-ec6d-4560-a40f-858fa955e84f"), event_id=22, version=0)
class Microsoft_Windows_Storage_Tiering_22_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "Report" / WString,
        "FasterTierSize" / WString,
        "TotalIOPercentFromPerfTier" / Int16ul,
        "SizeOfPerfTierPinnedFiles" / WString,
        "PercentOfPerfTierPinnedFilesIO" / Int16ul,
        "SizeOfCapacityTierPinnedFiles" / WString,
        "PercentOfCapacityTierPinnedFilesIO" / Int16ul
    )


@declare(guid=guid("4a104570-ec6d-4560-a40f-858fa955e84f"), event_id=31, version=0)
class Microsoft_Windows_Storage_Tiering_31_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "NumberEntries" / Int32ul
    )

