# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Deduplication-Change
GUID : 1d5e499d-739c-45a6-a3e1-8cbe0a352beb
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16384, version=0)
class Microsoft_Windows_Deduplication_Change_16384_0(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16385, version=0)
class Microsoft_Windows_Deduplication_Change_16385_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16386, version=0)
class Microsoft_Windows_Deduplication_Change_16386_0(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16387, version=0)
class Microsoft_Windows_Deduplication_Change_16387_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16388, version=0)
class Microsoft_Windows_Deduplication_Change_16388_0(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16389, version=0)
class Microsoft_Windows_Deduplication_Change_16389_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16390, version=0)
class Microsoft_Windows_Deduplication_Change_16390_0(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul,
        "InvalidFileName" / WString
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16391, version=0)
class Microsoft_Windows_Deduplication_Change_16391_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16392, version=0)
class Microsoft_Windows_Deduplication_Change_16392_0(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16393, version=0)
class Microsoft_Windows_Deduplication_Change_16393_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16394, version=0)
class Microsoft_Windows_Deduplication_Change_16394_0(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16395, version=0)
class Microsoft_Windows_Deduplication_Change_16395_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16396, version=0)
class Microsoft_Windows_Deduplication_Change_16396_0(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16397, version=0)
class Microsoft_Windows_Deduplication_Change_16397_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16398, version=0)
class Microsoft_Windows_Deduplication_Change_16398_0(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul,
        "ContainerOffset" / Int32ul,
        "StartIndex" / Int32ul,
        "EntryCount" / Int32ul,
        "Entries" / Int32sl
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16399, version=0)
class Microsoft_Windows_Deduplication_Change_16399_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16400, version=1)
class Microsoft_Windows_Deduplication_Change_16400_1(Etw):
    pattern = Struct(
        "Signature" / Int32ul,
        "MajorVersion" / Int8ul,
        "MinorVersion" / Int8ul,
        "VersionChecksum" / Int16ul,
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul,
        "ContainerOffset" / Int32ul,
        "UpdateSequenceNumber" / Int64ul,
        "ValidDataLength" / Int32ul,
        "ChunkCount" / Int32ul,
        "NextLocalId" / Int32ul,
        "Flags" / Int32ul,
        "LastAppendTime" / Int64ul,
        "BackupRedirectionTableOffset" / Int32ul,
        "LastReconciliationLocalId" / Int32ul,
        "Checksum" / Int64ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16401, version=0)
class Microsoft_Windows_Deduplication_Change_16401_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16402, version=1)
class Microsoft_Windows_Deduplication_Change_16402_1(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul,
        "WriteOffset" / Int64ul,
        "IsBatched" / Int8ul,
        "IsCorrupted" / Int8ul,
        "DataSize" / Int32ul,
        "Header" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16403, version=0)
class Microsoft_Windows_Deduplication_Change_16403_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16404, version=1)
class Microsoft_Windows_Deduplication_Change_16404_1(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul,
        "WriteOffset" / Int64ul,
        "IsBatched" / Int8ul,
        "IsCorrupted" / Int8ul,
        "DataSize" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16405, version=0)
class Microsoft_Windows_Deduplication_Change_16405_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16408, version=1)
class Microsoft_Windows_Deduplication_Change_16408_1(Etw):
    pattern = Struct(
        "Signature" / Int32ul,
        "MajorVersion" / Int8ul,
        "MinorVersion" / Int8ul,
        "VersionChecksum" / Int16ul,
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "LogNumber" / Int32ul,
        "Checksum" / Int32ul,
        "FileExtension" / WString
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16409, version=0)
class Microsoft_Windows_Deduplication_Change_16409_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16410, version=1)
class Microsoft_Windows_Deduplication_Change_16410_1(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "LogNumber" / Int32ul,
        "FileExtension" / WString,
        "DeleteLogOffset" / Int32ul,
        "StartIndex" / Int32ul,
        "EntryCount" / Int32ul,
        "Entries" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16411, version=0)
class Microsoft_Windows_Deduplication_Change_16411_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16412, version=1)
class Microsoft_Windows_Deduplication_Change_16412_1(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "LogNumber" / Int32ul,
        "FileExtension" / WString
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16413, version=0)
class Microsoft_Windows_Deduplication_Change_16413_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16414, version=1)
class Microsoft_Windows_Deduplication_Change_16414_1(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "LogNumber" / Int32ul,
        "FileExtension" / WString
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16415, version=0)
class Microsoft_Windows_Deduplication_Change_16415_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16416, version=1)
class Microsoft_Windows_Deduplication_Change_16416_1(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "FileName" / WString,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul,
        "BitLength" / Int32ul,
        "StartIndex" / Int32ul,
        "EntryCount" / Int32ul,
        "Entries" / Bytes(lambda this: this.EntryCount)
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16417, version=0)
class Microsoft_Windows_Deduplication_Change_16417_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16418, version=1)
class Microsoft_Windows_Deduplication_Change_16418_1(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "FileName" / WString,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16419, version=0)
class Microsoft_Windows_Deduplication_Change_16419_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16420, version=0)
class Microsoft_Windows_Deduplication_Change_16420_0(Etw):
    pattern = Struct(
        "Signature" / Int32ul,
        "MajorVersion" / Int8ul,
        "MinorVersion" / Int8ul,
        "VersionChecksum" / Int16ul,
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "LogNumber" / Int32ul,
        "Checksum" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16421, version=0)
class Microsoft_Windows_Deduplication_Change_16421_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16422, version=1)
class Microsoft_Windows_Deduplication_Change_16422_1(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul,
        "WriteOffset" / Int64ul,
        "IsBatched" / Int8ul,
        "IsCorrupted" / Int8ul,
        "DataSize" / Int32ul,
        "Header" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16423, version=0)
class Microsoft_Windows_Deduplication_Change_16423_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16424, version=1)
class Microsoft_Windows_Deduplication_Change_16424_1(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul,
        "WriteOffset" / Int64ul,
        "IsBatched" / Int8ul,
        "IsCorrupted" / Int8ul,
        "DataSize" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16425, version=0)
class Microsoft_Windows_Deduplication_Change_16425_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16426, version=1)
class Microsoft_Windows_Deduplication_Change_16426_1(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul,
        "WriteOffset" / Int64ul,
        "IsBatched" / Int8ul,
        "IsCorrupted" / Int8ul,
        "DataSize" / Int32ul,
        "Header" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16427, version=0)
class Microsoft_Windows_Deduplication_Change_16427_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16428, version=3)
class Microsoft_Windows_Deduplication_Change_16428_3(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul,
        "WriteOffset" / Int64ul,
        "IsBatched" / Int8ul,
        "IsCorrupted" / Int8ul,
        "DataSize" / Int32ul,
        "StartIndex" / Int32ul,
        "EntryCount" / Int32ul,
        "Entries" / Int64ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16429, version=0)
class Microsoft_Windows_Deduplication_Change_16429_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16430, version=2)
class Microsoft_Windows_Deduplication_Change_16430_2(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "LogNumber" / Int32ul,
        "MergeLogOffset" / Int32ul,
        "StartIndex" / Int32ul,
        "EntryCount" / Int32ul,
        "Entries" / Int32sl
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16431, version=0)
class Microsoft_Windows_Deduplication_Change_16431_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16432, version=0)
class Microsoft_Windows_Deduplication_Change_16432_0(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "LogNumber" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16433, version=0)
class Microsoft_Windows_Deduplication_Change_16433_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16434, version=0)
class Microsoft_Windows_Deduplication_Change_16434_0(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "LogNumber" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16435, version=0)
class Microsoft_Windows_Deduplication_Change_16435_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16436, version=0)
class Microsoft_Windows_Deduplication_Change_16436_0(Etw):
    pattern = Struct(
        "EntryToRemove" / WString,
        "EntryToAdd" / WString
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16437, version=0)
class Microsoft_Windows_Deduplication_Change_16437_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16438, version=0)
class Microsoft_Windows_Deduplication_Change_16438_0(Etw):
    pattern = Struct(
        "FileId" / Int64ul,
        "FilePath" / WString,
        "SizeBackedByChunkStore" / Int64ul,
        "StreamMapInfoSize" / Int16ul,
        "StreamMapInfo" / Bytes(lambda this: this.StreamMapInfoSize)
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16439, version=0)
class Microsoft_Windows_Deduplication_Change_16439_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul,
        "ReparsePointSet" / Int8ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16440, version=0)
class Microsoft_Windows_Deduplication_Change_16440_0(Etw):
    pattern = Struct(
        "FileId" / Int64ul,
        "FilePath" / WString
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16441, version=0)
class Microsoft_Windows_Deduplication_Change_16441_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16443, version=0)
class Microsoft_Windows_Deduplication_Change_16443_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16444, version=0)
class Microsoft_Windows_Deduplication_Change_16444_0(Etw):
    pattern = Struct(
        "FileId" / Int64ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16445, version=0)
class Microsoft_Windows_Deduplication_Change_16445_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16446, version=0)
class Microsoft_Windows_Deduplication_Change_16446_0(Etw):
    pattern = Struct(
        "FileId" / Int64ul,
        "Offset" / Int64ul,
        "BeyondFinalZero" / Int64ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16447, version=0)
class Microsoft_Windows_Deduplication_Change_16447_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16448, version=0)
class Microsoft_Windows_Deduplication_Change_16448_0(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "FileName" / WString,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16449, version=0)
class Microsoft_Windows_Deduplication_Change_16449_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16450, version=0)
class Microsoft_Windows_Deduplication_Change_16450_0(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul,
        "WriteOffset" / Int64ul,
        "IsBatched" / Int8ul,
        "IsCorrupted" / Int8ul,
        "DataSize" / Int32ul,
        "Header" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16451, version=0)
class Microsoft_Windows_Deduplication_Change_16451_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16452, version=0)
class Microsoft_Windows_Deduplication_Change_16452_0(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul,
        "WriteOffset" / Int64ul,
        "IsBatched" / Int8ul,
        "IsCorrupted" / Int8ul,
        "DataSize" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16453, version=0)
class Microsoft_Windows_Deduplication_Change_16453_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16454, version=0)
class Microsoft_Windows_Deduplication_Change_16454_0(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul,
        "WriteOffset" / Int64ul,
        "BatchChunkCount" / Int32ul,
        "BatchDataSize" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16455, version=0)
class Microsoft_Windows_Deduplication_Change_16455_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16456, version=1)
class Microsoft_Windows_Deduplication_Change_16456_1(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "FileName" / WString,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul,
        "FileCopyLevel" / Int32ul,
        "TotalEntryCount" / Int32ul,
        "StartIndex" / Int32ul,
        "EntryCount" / Int32ul,
        "Entries" / Int64sl
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16457, version=0)
class Microsoft_Windows_Deduplication_Change_16457_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16458, version=1)
class Microsoft_Windows_Deduplication_Change_16458_1(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "FileName" / WString,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul,
        "FileCopyLevel" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16459, version=0)
class Microsoft_Windows_Deduplication_Change_16459_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16460, version=0)
class Microsoft_Windows_Deduplication_Change_16460_0(Etw):
    pattern = Struct(
        "ChunkStoreType" / Int8ul,
        "FileName" / WString,
        "ContainerId" / Int32ul,
        "Generation" / Int32ul,
        "FileCopyLevel" / Int32ul
    )


@declare(guid=guid("1d5e499d-739c-45a6-a3e1-8cbe0a352beb"), event_id=16461, version=0)
class Microsoft_Windows_Deduplication_Change_16461_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )

