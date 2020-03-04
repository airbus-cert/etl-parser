# -*- coding: utf-8 -*-
"""
Ntfs
GUID : dd70bc80-ef44-421b-8ac3-cd31da613a4e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("dd70bc80-ef44-421b-8ac3-cd31da613a4e"), event_id=55, version=0)
class Ntfs_55_0(Etw):
    pattern = Struct(
        "DriveName" / WString,
        "DeviceName" / WString,
        "CorruptionState" / Int32ul,
        "HeaderFlags" / Int32ul,
        "Severity" / WString,
        "Origin" / WString,
        "Verb" / WString,
        "Description" / WString,
        "Signature" / Int32ul,
        "Outcome" / WString,
        "SampleLength" / Int16ul,
        "SampleData" / Bytes(lambda this: this.SampleLength),
        "SourceFile" / Int32ul,
        "SourceLine" / Int16ul,
        "SourceTag" / Int32ul,
        "AdditionalInfo" / Int32ul,
        "CallStack" / CString
    )


@declare(guid=guid("dd70bc80-ef44-421b-8ac3-cd31da613a4e"), event_id=130, version=0)
class Ntfs_130_0(Etw):
    pattern = Struct(
        "VolumeIdLength" / Int16ul,
        "VolumeId" / Bytes(lambda this: this.VolumeIdLength),
        "RepairDetail" / WString,
        "RepairDataLength" / Int16ul,
        "RepairData" / Bytes(lambda this: this.RepairDataLength)
    )


@declare(guid=guid("dd70bc80-ef44-421b-8ac3-cd31da613a4e"), event_id=131, version=0)
class Ntfs_131_0(Etw):
    pattern = Struct(
        "VolumeIdLength" / Int16ul,
        "VolumeId" / Bytes(lambda this: this.VolumeIdLength),
        "RepairDetail" / WString,
        "RepairDataLength" / Int16ul,
        "RepairData" / Bytes(lambda this: this.RepairDataLength)
    )


@declare(guid=guid("dd70bc80-ef44-421b-8ac3-cd31da613a4e"), event_id=133, version=0)
class Ntfs_133_0(Etw):
    pattern = Struct(
        "TotalCount" / Int32ul,
        "BadFrsCount" / Int32ul,
        "OrphanChildFRSCount" / Int32ul,
        "BadClustersCount" / Int32ul,
        "BadFreeClustersCount" / Int32ul,
        "CrossLinkCount" / Int32ul,
        "SDEntryCount" / Int32ul,
        "InvalidSidCount" / Int32ul,
        "IndexAttributeCount" / Int32ul,
        "IndexSubtreeCount" / Int32ul,
        "IndexOffsetCount" / Int32ul,
        "IndexEntryCount" / Int32ul,
        "IndexOrderCount" / Int32ul,
        "ConnectCount" / Int32ul,
        "BreakCycleCount" / Int32ul,
        "FRSAllocateCount" / Int32ul,
        "OthersCount" / Int32ul
    )

