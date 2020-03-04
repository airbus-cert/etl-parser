# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Direct3DShaderCache
GUID : 2d4ebca6-ea64-453f-a292-ae2ea0ee513b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=1, version=0)
class Microsoft_Windows_Direct3DShaderCache_1_0(Etw):
    pattern = Struct(
        "Cache" / Int64ul,
        "Type" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=2, version=0)
class Microsoft_Windows_Direct3DShaderCache_2_0(Etw):
    pattern = Struct(
        "Cache" / Int64ul,
        "Type" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=3, version=0)
class Microsoft_Windows_Direct3DShaderCache_3_0(Etw):
    pattern = Struct(
        "Cache" / Int64ul,
        "Type" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=4, version=0)
class Microsoft_Windows_Direct3DShaderCache_4_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "GUID" / Guid,
        "Filename" / WString,
        "FileCreateDisposition" / Int32ul,
        "Mode" / Int32ul,
        "MaximumInMemoryCacheSizeBytes" / Int32ul,
        "MaximumInMemoryCacheEntries" / Int32ul,
        "MaximumWriteQueueBytes" / Int32ul,
        "MaximumWriteQueueNumEntries" / Int32ul,
        "MaximumValueFileSizeBytes" / Int32ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=5, version=0)
class Microsoft_Windows_Direct3DShaderCache_5_0(Etw):
    pattern = Struct(
        "Return" / Int32sl,
        "Cache" / Int64ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=6, version=0)
class Microsoft_Windows_Direct3DShaderCache_6_0(Etw):
    pattern = Struct(
        "Cache" / Int64ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=8, version=0)
class Microsoft_Windows_Direct3DShaderCache_8_0(Etw):
    pattern = Struct(
        "Cache" / Int64ul,
        "NumKeyParts" / Int32ul,
        "KeyParts" / Int8ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=9, version=0)
class Microsoft_Windows_Direct3DShaderCache_9_0(Etw):
    pattern = Struct(
        "Return" / Int32sl,
        "FoundValue" / Int64ul,
        "FoundValueSize" / Int32ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=10, version=0)
class Microsoft_Windows_Direct3DShaderCache_10_0(Etw):
    pattern = Struct(
        "Cache" / Int64ul,
        "NumKeyParts" / Int32ul,
        "KeyParts" / Int16ul,
        "Value" / Int64ul,
        "ValueSize" / Int32ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=11, version=0)
class Microsoft_Windows_Direct3DShaderCache_11_0(Etw):
    pattern = Struct(
        "Return" / Int32sl
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=12, version=0)
class Microsoft_Windows_Direct3DShaderCache_12_0(Etw):
    pattern = Struct(
        "Value" / Int64ul,
        "ValueSize" / Int32ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=14, version=0)
class Microsoft_Windows_Direct3DShaderCache_14_0(Etw):
    pattern = Struct(
        "Cache" / Int64ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=15, version=0)
class Microsoft_Windows_Direct3DShaderCache_15_0(Etw):
    pattern = Struct(
        "Return" / Int32sl
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=102, version=0)
class Microsoft_Windows_Direct3DShaderCache_102_0(Etw):
    pattern = Struct(
        "NumEntries" / Int32ul,
        "CurrentMemoryUsage" / Int64ul,
        "MemoryBudget" / Int64ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=103, version=0)
class Microsoft_Windows_Direct3DShaderCache_103_0(Etw):
    pattern = Struct(
        "NumEntries" / Int32ul,
        "CurrentMemoryUsage" / Int64ul,
        "DeltaSize" / Int32ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=104, version=0)
class Microsoft_Windows_Direct3DShaderCache_104_0(Etw):
    pattern = Struct(
        "NumEntries" / Int32ul,
        "CurrentMemoryUsage" / Int64ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=105, version=0)
class Microsoft_Windows_Direct3DShaderCache_105_0(Etw):
    pattern = Struct(
        "NumEntries" / Int32ul,
        "CurrentMemoryUsage" / Int64ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=106, version=0)
class Microsoft_Windows_Direct3DShaderCache_106_0(Etw):
    pattern = Struct(
        "NumEntries" / Int32ul,
        "CurrentMemoryUsage" / Int64ul,
        "MemoryBudget" / Int64ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=107, version=0)
class Microsoft_Windows_Direct3DShaderCache_107_0(Etw):
    pattern = Struct(
        "NumEntries" / Int32ul,
        "CurrentMemoryUsage" / Int64ul,
        "DeltaSize" / Int32ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=108, version=0)
class Microsoft_Windows_Direct3DShaderCache_108_0(Etw):
    pattern = Struct(
        "NumEntries" / Int32ul,
        "CurrentMemoryUsage" / Int64ul,
        "MemoryBudget" / Int64ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=109, version=0)
class Microsoft_Windows_Direct3DShaderCache_109_0(Etw):
    pattern = Struct(
        "TotalPages" / Int32ul,
        "TotalSize" / Int64ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=110, version=0)
class Microsoft_Windows_Direct3DShaderCache_110_0(Etw):
    pattern = Struct(
        "Filename" / WString,
        "FileCreateDisposition" / Int32ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=112, version=0)
class Microsoft_Windows_Direct3DShaderCache_112_0(Etw):
    pattern = Struct(
        "LastError" / Int32ul,
        "FileType" / Int32ul,
        "FileOp" / Int32ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=120, version=0)
class Microsoft_Windows_Direct3DShaderCache_120_0(Etw):
    pattern = Struct(
        "CurrentFileSize" / Int64ul,
        "CurrentWriteQueueSize" / Int64ul,
        "MaximimFileSize" / Int64ul,
        "NewValueSize" / Int32ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=121, version=0)
class Microsoft_Windows_Direct3DShaderCache_121_0(Etw):
    pattern = Struct(
        "CurrentFileSize" / Int64ul,
        "CurrentWriteQueueSize" / Int64ul,
        "MaximimWriteQueueSize" / Int64ul,
        "NewValueSize" / Int32ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=122, version=0)
class Microsoft_Windows_Direct3DShaderCache_122_0(Etw):
    pattern = Struct(
        "CurrentFileSize" / Int64ul,
        "CurrentWriteQueueSize" / Int64ul,
        "MaximimWriteQueueSize" / Int64ul,
        "NewValueSize" / Int32ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=123, version=0)
class Microsoft_Windows_Direct3DShaderCache_123_0(Etw):
    pattern = Struct(
        "CurrentFileSize" / Int64ul,
        "CurrentWriteQueueSize" / Int64ul,
        "MaximimWriteQueueSize" / Int64ul,
        "NewValueSize" / Int32ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=124, version=0)
class Microsoft_Windows_Direct3DShaderCache_124_0(Etw):
    pattern = Struct(
        "NumMappedValues" / Int32ul,
        "MappedMemoryUsage" / Int64ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=125, version=0)
class Microsoft_Windows_Direct3DShaderCache_125_0(Etw):
    pattern = Struct(
        "NumMappedValues" / Int32ul,
        "MappedMemoryUsage" / Int64ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=501, version=0)
class Microsoft_Windows_Direct3DShaderCache_501_0(Etw):
    pattern = Struct(
        "FileType" / Int32ul,
        "NumBytes" / Int64ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=502, version=0)
class Microsoft_Windows_Direct3DShaderCache_502_0(Etw):
    pattern = Struct(
        "FileType" / Int32ul,
        "NumBytes" / Int64ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=503, version=0)
class Microsoft_Windows_Direct3DShaderCache_503_0(Etw):
    pattern = Struct(
        "FileType" / Int32ul,
        "NumBytes" / Int64ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=504, version=0)
class Microsoft_Windows_Direct3DShaderCache_504_0(Etw):
    pattern = Struct(
        "FileType" / Int32ul,
        "NumBytes" / Int64ul
    )


@declare(guid=guid("2d4ebca6-ea64-453f-a292-ae2ea0ee513b"), event_id=2001, version=1)
class Microsoft_Windows_Direct3DShaderCache_2001_1(Etw):
    pattern = Struct(
        "UTCReplace_AppSessionGuid" / Int8ul,
        "Filename" / WString,
        "NumLookups" / Int32ul,
        "NumCacheHits" / Int32ul,
        "NumL1Hits" / Int32ul,
        "NumL1HitsInCacheFromAdd" / Int32ul,
        "NumAddRequests" / Int32ul,
        "NumFailedAdds" / Int32ul,
        "FailedAddTotalSize" / Int64ul,
        "MaxInMemoryEntries" / Int32ul,
        "MaxInMemorySize" / Int32ul,
        "NumDiskEntries" / Int32ul,
        "IndexFileSize" / Int64ul,
        "ValueFileSize" / Int64ul,
        "CompressedValueFileSize" / Int64ul,
        "HadCRCFailure" / Int8ul,
        "NumHashCollisions" / Int32ul,
        "TotalKeySize" / Int64ul,
        "TotalValueSize" / Int64ul,
        "AverageKeySize" / Double,
        "AverageValueSize" / Double,
        "MaxKeySize" / Int32ul,
        "MaxValueSize" / Int32ul,
        "TotalFindTime" / Double,
        "TotalAddTime" / Double,
        "AverageFindTime" / Double,
        "AverageAddTime" / Double,
        "MaxFindTime" / Double,
        "MaxAddTime" / Double,
        "InitializationTime" / Double,
        "DesiredOpen" / Int8ul,
        "SuccessfulOpen" / Int8ul
    )

