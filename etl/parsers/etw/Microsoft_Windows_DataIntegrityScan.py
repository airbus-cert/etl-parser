# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DataIntegrityScan
GUID : 13bc4371-4e21-4e46-a84f-8c0ffb548ced
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=11, version=0)
class Microsoft_Windows_DataIntegrityScan_11_0(Etw):
    pattern = Struct(
        "DiskNumber" / Int32ul,
        "DiskGuid" / Guid,
        "PortPoolId" / Guid,
        "PortDiskId" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=12, version=0)
class Microsoft_Windows_DataIntegrityScan_12_0(Etw):
    pattern = Struct(
        "DiskNumber" / Int32ul,
        "DiskGuid" / Guid,
        "PortPoolId" / Guid,
        "PortDiskId" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=21, version=0)
class Microsoft_Windows_DataIntegrityScan_21_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "FriendlyVolumeNameLength" / Int16ul,
        "FriendlyVolumeName" / Bytes(lambda this: this.FriendlyVolumeNameLength),
        "VolumeGuid" / Guid,
        "DiskNumber" / Int32ul,
        "DiskGuid" / Guid,
        "PortPoolId" / Guid,
        "PortDiskId" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=22, version=0)
class Microsoft_Windows_DataIntegrityScan_22_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "FriendlyVolumeNameLength" / Int16ul,
        "FriendlyVolumeName" / Bytes(lambda this: this.FriendlyVolumeNameLength),
        "HResult" / Int32sl,
        "DirectoryCount" / Int64ul,
        "FileCount" / Int64ul,
        "StreamCount" / Int64ul,
        "DataCount" / Int64ul,
        "FsctlCount" / Int64ul,
        "TotalBytesRepaired" / Int64ul,
        "TotalBytesFailed" / Int64ul,
        "MetadataBytesProcessed" / Int64ul,
        "DataBytesProcessed" / Int64ul,
        "TotalMetadataBytesInUse" / Int64ul,
        "TotalDataBytesInUse" / Int64ul,
        "TotalTimeTaken" / Int64ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=23, version=0)
class Microsoft_Windows_DataIntegrityScan_23_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "FriendlyVolumeNameLength" / Int16ul,
        "FriendlyVolumeName" / Bytes(lambda this: this.FriendlyVolumeNameLength),
        "HResult" / Int32sl,
        "DirectoryCount" / Int64ul,
        "FileCount" / Int64ul,
        "StreamCount" / Int64ul,
        "DataCount" / Int64ul,
        "FsctlCount" / Int64ul,
        "TotalBytesRepaired" / Int64ul,
        "TotalBytesFailed" / Int64ul,
        "MetadataBytesProcessed" / Int64ul,
        "DataBytesProcessed" / Int64ul,
        "TotalMetadataBytesInUse" / Int64ul,
        "TotalDataBytesInUse" / Int64ul,
        "TotalTimeTaken" / Int64ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=24, version=0)
class Microsoft_Windows_DataIntegrityScan_24_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "FriendlyVolumeNameLength" / Int16ul,
        "FriendlyVolumeName" / Bytes(lambda this: this.FriendlyVolumeNameLength),
        "HResult" / Int32sl,
        "Count" / Int64ul,
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=25, version=0)
class Microsoft_Windows_DataIntegrityScan_25_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "FriendlyVolumeNameLength" / Int16ul,
        "FriendlyVolumeName" / Bytes(lambda this: this.FriendlyVolumeNameLength),
        "HResult" / Int32sl,
        "DirectoryCount" / Int64ul,
        "FileCount" / Int64ul,
        "StreamCount" / Int64ul,
        "DataCount" / Int64ul,
        "FsctlCount" / Int64ul,
        "TotalBytesRepaired" / Int64ul,
        "TotalBytesFailed" / Int64ul,
        "MetadataBytesProcessed" / Int64ul,
        "DataBytesProcessed" / Int64ul,
        "TotalMetadataBytesInUse" / Int64ul,
        "TotalDataBytesInUse" / Int64ul,
        "TotalTimeTaken" / Int64ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=26, version=0)
class Microsoft_Windows_DataIntegrityScan_26_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "FriendlyVolumeNameLength" / Int16ul,
        "FriendlyVolumeName" / Bytes(lambda this: this.FriendlyVolumeNameLength),
        "HResult" / Int32sl,
        "DirectoryCount" / Int64ul,
        "FileCount" / Int64ul,
        "StreamCount" / Int64ul,
        "DataCount" / Int64ul,
        "FsctlCount" / Int64ul,
        "TotalBytesRepaired" / Int64ul,
        "TotalBytesFailed" / Int64ul,
        "MetadataBytesProcessed" / Int64ul,
        "DataBytesProcessed" / Int64ul,
        "TotalMetadataBytesInUse" / Int64ul,
        "TotalDataBytesInUse" / Int64ul,
        "TotalTimeTaken" / Int64ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=27, version=0)
class Microsoft_Windows_DataIntegrityScan_27_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "FriendlyVolumeNameLength" / Int16ul,
        "FriendlyVolumeName" / Bytes(lambda this: this.FriendlyVolumeNameLength),
        "DirectoryCount" / Int64ul,
        "FileCount" / Int64ul,
        "StreamCount" / Int64ul,
        "DataCount" / Int64ul,
        "FsctlCount" / Int64ul,
        "TotalBytesRepaired" / Int64ul,
        "TotalBytesFailed" / Int64ul,
        "MetadataBytesProcessed" / Int64ul,
        "DataBytesProcessed" / Int64ul,
        "TotalMetadataBytesInUse" / Int64ul,
        "TotalDataBytesInUse" / Int64ul,
        "TotalTimeTaken" / Int64ul,
        "PercentComplete" / Int16ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=54, version=0)
class Microsoft_Windows_DataIntegrityScan_54_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "InternalFileReference" / Int64ul,
        "FileOffset" / Int64ul,
        "Length" / Int64ul,
        "BytesRepaired" / Int64ul,
        "BytesFailed" / Int64ul,
        "Status" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=55, version=0)
class Microsoft_Windows_DataIntegrityScan_55_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "InternalFileReference" / Int64ul,
        "FileOffset" / Int64ul,
        "Length" / Int64ul,
        "BytesRepaired" / Int64ul,
        "BytesFailed" / Int64ul,
        "Status" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=56, version=0)
class Microsoft_Windows_DataIntegrityScan_56_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "InternalFileReference" / Int64ul,
        "FileOffset" / Int64ul,
        "Length" / Int64ul,
        "BytesRepaired" / Int64ul,
        "BytesFailed" / Int64ul,
        "Status" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=57, version=0)
class Microsoft_Windows_DataIntegrityScan_57_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "InternalFileReference" / Int64ul,
        "FileOffset" / Int64ul,
        "Length" / Int64ul,
        "BytesRepaired" / Int64ul,
        "BytesFailed" / Int64ul,
        "Status" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=58, version=0)
class Microsoft_Windows_DataIntegrityScan_58_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "InternalFileReference" / Int64ul,
        "FileOffset" / Int64ul,
        "Length" / Int64ul,
        "BytesRepaired" / Int64ul,
        "BytesFailed" / Int64ul,
        "Status" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=59, version=0)
class Microsoft_Windows_DataIntegrityScan_59_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "InternalFileReference" / Int64ul,
        "FileOffset" / Int64ul,
        "Length" / Int64ul,
        "BytesRepaired" / Int64ul,
        "BytesFailed" / Int64ul,
        "Status" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=60, version=0)
class Microsoft_Windows_DataIntegrityScan_60_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "InternalFileReference" / Int64ul,
        "FileOffset" / Int64ul,
        "Length" / Int64ul,
        "BytesRepaired" / Int64ul,
        "BytesFailed" / Int64ul,
        "Status" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=61, version=0)
class Microsoft_Windows_DataIntegrityScan_61_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "InternalFileReference" / Int64ul,
        "FileOffset" / Int64ul,
        "Length" / Int64ul,
        "BytesRepaired" / Int64ul,
        "BytesFailed" / Int64ul,
        "Status" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=62, version=0)
class Microsoft_Windows_DataIntegrityScan_62_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "InternalFileReference" / Int64ul,
        "FileOffset" / Int64ul,
        "Length" / Int64ul,
        "BytesRepaired" / Int64ul,
        "BytesFailed" / Int64ul,
        "Status" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=111, version=0)
class Microsoft_Windows_DataIntegrityScan_111_0(Etw):
    pattern = Struct(
        "DiskNumber" / Int32ul,
        "DiskGuid" / Guid,
        "PortPoolId" / Guid,
        "PortDiskId" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=112, version=0)
class Microsoft_Windows_DataIntegrityScan_112_0(Etw):
    pattern = Struct(
        "DiskNumber" / Int32ul,
        "DiskGuid" / Guid,
        "PortPoolId" / Guid,
        "PortDiskId" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=121, version=0)
class Microsoft_Windows_DataIntegrityScan_121_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "FriendlyVolumeNameLength" / Int16ul,
        "FriendlyVolumeName" / Bytes(lambda this: this.FriendlyVolumeNameLength),
        "DiskNumber" / Int32ul,
        "DiskOffset" / Int64ul,
        "Length" / Int64ul,
        "VolumeGuid" / Guid,
        "DiskGuid" / Guid,
        "PortPoolId" / Guid,
        "PortDiskId" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=122, version=0)
class Microsoft_Windows_DataIntegrityScan_122_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "FriendlyVolumeNameLength" / Int16ul,
        "FriendlyVolumeName" / Bytes(lambda this: this.FriendlyVolumeNameLength),
        "HResult" / Int32sl,
        "DirectoryCount" / Int64ul,
        "FileCount" / Int64ul,
        "StreamCount" / Int64ul,
        "DataCount" / Int64ul,
        "FsctlCount" / Int64ul,
        "TotalBytesRepaired" / Int64ul,
        "TotalBytesFailed" / Int64ul,
        "MetadataBytesProcessed" / Int64ul,
        "DataBytesProcessed" / Int64ul,
        "TotalMetadataBytesInUse" / Int64ul,
        "TotalDataBytesInUse" / Int64ul,
        "MaxThreadCount" / Int32ul,
        "TotalTimeTaken" / Int64ul,
        "DiskNumber" / Int32ul,
        "DiskOffset" / Int64ul,
        "Length" / Int64ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=123, version=0)
class Microsoft_Windows_DataIntegrityScan_123_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "FriendlyVolumeNameLength" / Int16ul,
        "FriendlyVolumeName" / Bytes(lambda this: this.FriendlyVolumeNameLength),
        "HResult" / Int32sl,
        "DirectoryCount" / Int64ul,
        "FileCount" / Int64ul,
        "StreamCount" / Int64ul,
        "DataCount" / Int64ul,
        "FsctlCount" / Int64ul,
        "TotalBytesRepaired" / Int64ul,
        "TotalBytesFailed" / Int64ul,
        "MetadataBytesProcessed" / Int64ul,
        "DataBytesProcessed" / Int64ul,
        "TotalMetadataBytesInUse" / Int64ul,
        "TotalDataBytesInUse" / Int64ul,
        "MaxThreadCount" / Int32ul,
        "TotalTimeTaken" / Int64ul,
        "DiskNumber" / Int32ul,
        "DiskOffset" / Int64ul,
        "Length" / Int64ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=124, version=0)
class Microsoft_Windows_DataIntegrityScan_124_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "FriendlyVolumeNameLength" / Int16ul,
        "FriendlyVolumeName" / Bytes(lambda this: this.FriendlyVolumeNameLength),
        "HResult" / Int32sl,
        "Count" / Int64ul,
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=125, version=0)
class Microsoft_Windows_DataIntegrityScan_125_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "FriendlyVolumeNameLength" / Int16ul,
        "FriendlyVolumeName" / Bytes(lambda this: this.FriendlyVolumeNameLength),
        "HResult" / Int32sl,
        "DirectoryCount" / Int64ul,
        "FileCount" / Int64ul,
        "StreamCount" / Int64ul,
        "DataCount" / Int64ul,
        "FsctlCount" / Int64ul,
        "TotalBytesRepaired" / Int64ul,
        "TotalBytesFailed" / Int64ul,
        "MetadataBytesProcessed" / Int64ul,
        "DataBytesProcessed" / Int64ul,
        "TotalMetadataBytesInUse" / Int64ul,
        "TotalDataBytesInUse" / Int64ul,
        "MaxThreadCount" / Int32ul,
        "TotalTimeTaken" / Int64ul,
        "DiskNumber" / Int32ul,
        "DiskOffset" / Int64ul,
        "Length" / Int64ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=126, version=0)
class Microsoft_Windows_DataIntegrityScan_126_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "FriendlyVolumeNameLength" / Int16ul,
        "FriendlyVolumeName" / Bytes(lambda this: this.FriendlyVolumeNameLength),
        "HResult" / Int32sl,
        "DirectoryCount" / Int64ul,
        "FileCount" / Int64ul,
        "StreamCount" / Int64ul,
        "DataCount" / Int64ul,
        "FsctlCount" / Int64ul,
        "TotalBytesRepaired" / Int64ul,
        "TotalBytesFailed" / Int64ul,
        "MetadataBytesProcessed" / Int64ul,
        "DataBytesProcessed" / Int64ul,
        "TotalMetadataBytesInUse" / Int64ul,
        "TotalDataBytesInUse" / Int64ul,
        "MaxThreadCount" / Int32ul,
        "TotalTimeTaken" / Int64ul,
        "DiskNumber" / Int32ul,
        "DiskOffset" / Int64ul,
        "Length" / Int64ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=127, version=0)
class Microsoft_Windows_DataIntegrityScan_127_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "FriendlyVolumeNameLength" / Int16ul,
        "FriendlyVolumeName" / Bytes(lambda this: this.FriendlyVolumeNameLength),
        "HResult" / Int32sl,
        "DiskNumber" / Int32ul,
        "DiskOffset" / Int64ul,
        "Length" / Int64ul,
        "VolumeGuid" / Guid,
        "DiskGuid" / Guid,
        "PortPoolId" / Guid,
        "PortDiskId" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=128, version=0)
class Microsoft_Windows_DataIntegrityScan_128_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "FriendlyVolumeNameLength" / Int16ul,
        "FriendlyVolumeName" / Bytes(lambda this: this.FriendlyVolumeNameLength),
        "HResult" / Int32sl,
        "DiskNumber" / Int32ul,
        "DiskOffset" / Int64ul,
        "Length" / Int64ul,
        "VolumeGuid" / Guid,
        "DiskGuid" / Guid,
        "PortPoolId" / Guid,
        "PortDiskId" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=129, version=0)
class Microsoft_Windows_DataIntegrityScan_129_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "FriendlyVolumeNameLength" / Int16ul,
        "FriendlyVolumeName" / Bytes(lambda this: this.FriendlyVolumeNameLength),
        "DirectoryCount" / Int64ul,
        "FileCount" / Int64ul,
        "StreamCount" / Int64ul,
        "DataCount" / Int64ul,
        "FsctlCount" / Int64ul,
        "TotalBytesRepaired" / Int64ul,
        "TotalBytesFailed" / Int64ul,
        "MetadataBytesProcessed" / Int64ul,
        "DataBytesProcessed" / Int64ul,
        "TotalMetadataBytesInUse" / Int64ul,
        "TotalDataBytesInUse" / Int64ul,
        "MaxThreadCount" / Int32ul,
        "TotalTimeTaken" / Int64ul,
        "PercentComplete" / Int16ul,
        "DiskNumber" / Int32ul,
        "DiskOffset" / Int64ul,
        "Length" / Int64ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=154, version=0)
class Microsoft_Windows_DataIntegrityScan_154_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "InternalFileReference" / Int64ul,
        "FileOffset" / Int64ul,
        "Length" / Int64ul,
        "BytesRepaired" / Int64ul,
        "BytesFailed" / Int64ul,
        "Status" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=155, version=0)
class Microsoft_Windows_DataIntegrityScan_155_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "InternalFileReference" / Int64ul,
        "FileOffset" / Int64ul,
        "Length" / Int64ul,
        "BytesRepaired" / Int64ul,
        "BytesFailed" / Int64ul,
        "Status" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=156, version=0)
class Microsoft_Windows_DataIntegrityScan_156_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "InternalFileReference" / Int64ul,
        "FileOffset" / Int64ul,
        "Length" / Int64ul,
        "BytesRepaired" / Int64ul,
        "BytesFailed" / Int64ul,
        "Status" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=157, version=0)
class Microsoft_Windows_DataIntegrityScan_157_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "InternalFileReference" / Int64ul,
        "FileOffset" / Int64ul,
        "Length" / Int64ul,
        "BytesRepaired" / Int64ul,
        "BytesFailed" / Int64ul,
        "Status" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=158, version=0)
class Microsoft_Windows_DataIntegrityScan_158_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "InternalFileReference" / Int64ul,
        "FileOffset" / Int64ul,
        "Length" / Int64ul,
        "BytesRepaired" / Int64ul,
        "BytesFailed" / Int64ul,
        "Status" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=159, version=0)
class Microsoft_Windows_DataIntegrityScan_159_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "InternalFileReference" / Int64ul,
        "FileOffset" / Int64ul,
        "Length" / Int64ul,
        "BytesRepaired" / Int64ul,
        "BytesFailed" / Int64ul,
        "Status" / Int32ul,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=160, version=0)
class Microsoft_Windows_DataIntegrityScan_160_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "FriendlyVolumeNameLength" / Int16ul,
        "FriendlyVolumeName" / Bytes(lambda this: this.FriendlyVolumeNameLength),
        "ExtentCount" / Int64ul,
        "ExtentSize" / Int64ul,
        "HResult" / Int32sl,
        "VolumeGuid" / Guid
    )


@declare(guid=guid("13bc4371-4e21-4e46-a84f-8c0ffb548ced"), event_id=161, version=0)
class Microsoft_Windows_DataIntegrityScan_161_0(Etw):
    pattern = Struct(
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "FriendlyVolumeNameLength" / Int16ul,
        "FriendlyVolumeName" / Bytes(lambda this: this.FriendlyVolumeNameLength),
        "ExtentCount" / Int64ul,
        "ExtentSize" / Int64ul,
        "HResult" / Int32sl,
        "VolumeGuid" / Guid
    )

