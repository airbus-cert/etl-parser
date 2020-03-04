# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Minstore
GUID : 55b24b1d-dd9c-44c0-ba77-4f749f1b6976
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=1, version=1)
class Microsoft_Windows_Minstore_1_1(Etw):
    pattern = Struct(
        "IdHigh" / Int64ul,
        "IdLow" / Int64ul,
        "TableType" / Int32ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=2, version=1)
class Microsoft_Windows_Minstore_2_1(Etw):
    pattern = Struct(
        "IdHigh" / Int64ul,
        "IdLow" / Int64ul,
        "TableType" / Int32ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=10, version=1)
class Microsoft_Windows_Minstore_10_1(Etw):
    pattern = Struct(
        "PageCount" / Int32ul,
        "IdHigh" / Int64ul,
        "IdLow" / Int64ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=11, version=1)
class Microsoft_Windows_Minstore_11_1(Etw):
    pattern = Struct(
        "PageCount" / Int32ul,
        "IdHigh" / Int64ul,
        "IdLow" / Int64ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=12, version=1)
class Microsoft_Windows_Minstore_12_1(Etw):
    pattern = Struct(
        "PageCount" / Int32ul,
        "IdHigh" / Int64ul,
        "IdLow" / Int64ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=13, version=1)
class Microsoft_Windows_Minstore_13_1(Etw):
    pattern = Struct(
        "PageCount" / Int32ul,
        "IdHigh" / Int64ul,
        "IdLow" / Int64ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=20, version=1)
class Microsoft_Windows_Minstore_20_1(Etw):
    pattern = Struct(
        "Pending" / Int32ul,
        "Amount" / Int32ul,
        "Lsn1" / Int64ul,
        "Lsn2" / Int64ul,
        "Lsn3" / Int64ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=21, version=1)
class Microsoft_Windows_Minstore_21_1(Etw):
    pattern = Struct(
        "PageCount" / Int32ul,
        "IdHigh" / Int64ul,
        "IdLow" / Int64ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=22, version=1)
class Microsoft_Windows_Minstore_22_1(Etw):
    pattern = Struct(
        "IsMetadata" / Int8ul,
        "RequestedTier" / Int32ul,
        "ActualTier" / Int32ul,
        "RequestedStartOfRange" / Int64ul,
        "RequestedCountOfRange" / Int64ul,
        "AllocatedStartOfRange" / Int64ul,
        "AllocatedCountOfRange" / Int64ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=23, version=1)
class Microsoft_Windows_Minstore_23_1(Etw):
    pattern = Struct(
        "Pending" / Int32ul,
        "Amount" / Int32ul,
        "Lsn1" / Int64ul,
        "Lsn2" / Int64ul,
        "Lsn3" / Int64ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=24, version=1)
class Microsoft_Windows_Minstore_24_1(Etw):
    pattern = Struct(
        "Pending" / Int32ul,
        "Amount" / Int32ul,
        "Lsn1" / Int64ul,
        "Lsn2" / Int64ul,
        "Lsn3" / Int64ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=25, version=1)
class Microsoft_Windows_Minstore_25_1(Etw):
    pattern = Struct(
        "SourceTier" / Int32ul,
        "TargetTier" / Int32ul,
        "SourceStartOfRange" / Int64ul,
        "SourceCountOfRange" / Int64ul,
        "TargetPhysicalOffset" / Int64ul,
        "SsdFillRatio" / Int32ul,
        "HddFillRatio" / Int32ul,
        "IsTargetReserved" / Int8ul,
        "DestageAllocationCount" / Int64ul,
        "FailedSsdDestage" / Int8ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=50, version=1)
class Microsoft_Windows_Minstore_50_1(Etw):
    pattern = Struct(
        "IdHigh" / Int64ul,
        "IdLow" / Int64ul,
        "Lcn" / Int64ul,
        "Level" / Int32ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=51, version=1)
class Microsoft_Windows_Minstore_51_1(Etw):
    pattern = Struct(
        "IdHigh" / Int64ul,
        "IdLow" / Int64ul,
        "Lcn" / Int64ul,
        "Level" / Int32ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=52, version=1)
class Microsoft_Windows_Minstore_52_1(Etw):
    pattern = Struct(
        "IdHigh" / Int64ul,
        "IdLow" / Int64ul,
        "Lcn" / Int64ul,
        "Level" / Int32ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=100, version=1)
class Microsoft_Windows_Minstore_100_1(Etw):
    pattern = Struct(
        "IdHigh" / Int64ul,
        "IdLow" / Int64ul,
        "PageLcn" / Int64ul,
        "Lcn" / Int64ul,
        "PageVirtualClock" / Int64ul,
        "VolumeVirtualClock" / Int64ul,
        "Scrubbing" / Int8ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=101, version=1)
class Microsoft_Windows_Minstore_101_1(Etw):
    pattern = Struct(
        "Lcn" / Int64ul,
        "Scrubbing" / Int8ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=1000, version=2)
class Microsoft_Windows_Minstore_1000_2(Etw):
    pattern = Struct(
        "IdHigh" / Int64ul,
        "IdLow" / Int64ul,
        "TableType" / Int32ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=1002, version=2)
class Microsoft_Windows_Minstore_1002_2(Etw):
    pattern = Struct(
        "IdHigh" / Int64ul,
        "IdLow" / Int64ul,
        "TableType" / Int32ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=1003, version=2)
class Microsoft_Windows_Minstore_1003_2(Etw):
    pattern = Struct(
        "IdHigh" / Int64ul,
        "IdLow" / Int64ul,
        "TableType" / Int32ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=1004, version=2)
class Microsoft_Windows_Minstore_1004_2(Etw):
    pattern = Struct(
        "IdHigh" / Int64ul,
        "IdLow" / Int64ul,
        "TableType" / Int32ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=1005, version=2)
class Microsoft_Windows_Minstore_1005_2(Etw):
    pattern = Struct(
        "IdHigh" / Int64ul,
        "IdLow" / Int64ul,
        "TableType" / Int32ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=1006, version=2)
class Microsoft_Windows_Minstore_1006_2(Etw):
    pattern = Struct(
        "IdHigh" / Int64ul,
        "IdLow" / Int64ul,
        "TableType" / Int32ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=1007, version=2)
class Microsoft_Windows_Minstore_1007_2(Etw):
    pattern = Struct(
        "IdHigh" / Int64ul,
        "IdLow" / Int64ul,
        "TableType" / Int32ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=1008, version=2)
class Microsoft_Windows_Minstore_1008_2(Etw):
    pattern = Struct(
        "IdHigh" / Int64ul,
        "IdLow" / Int64ul,
        "TableType" / Int32ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=1011, version=2)
class Microsoft_Windows_Minstore_1011_2(Etw):
    pattern = Struct(
        "StartLsn" / Int64ul,
        "EndLsn" / Int64ul,
        "TransactionsRemaining" / Int64ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=1012, version=2)
class Microsoft_Windows_Minstore_1012_2(Etw):
    pattern = Struct(
        "StartLsn" / Int64ul,
        "EndLsn" / Int64ul,
        "TransactionsRemaining" / Int64ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=1013, version=2)
class Microsoft_Windows_Minstore_1013_2(Etw):
    pattern = Struct(
        "StartLsn" / Int64ul,
        "EndLsn" / Int64ul,
        "TransactionsRemaining" / Int64ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=1014, version=2)
class Microsoft_Windows_Minstore_1014_2(Etw):
    pattern = Struct(
        "StartLsn" / Int64ul,
        "EndLsn" / Int64ul,
        "TransactionsRemaining" / Int64ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=1015, version=2)
class Microsoft_Windows_Minstore_1015_2(Etw):
    pattern = Struct(
        "StartLsn" / Int64ul,
        "EndLsn" / Int64ul,
        "TransactionsRemaining" / Int64ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=1016, version=2)
class Microsoft_Windows_Minstore_1016_2(Etw):
    pattern = Struct(
        "StartLsn" / Int64ul,
        "EndLsn" / Int64ul,
        "TransactionsRemaining" / Int64ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=1017, version=2)
class Microsoft_Windows_Minstore_1017_2(Etw):
    pattern = Struct(
        "StartLsn" / Int64ul,
        "EndLsn" / Int64ul,
        "TransactionsRemaining" / Int64ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=1018, version=2)
class Microsoft_Windows_Minstore_1018_2(Etw):
    pattern = Struct(
        "StartLsn" / Int64ul,
        "EndLsn" / Int64ul,
        "TransactionsRemaining" / Int64ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=1019, version=2)
class Microsoft_Windows_Minstore_1019_2(Etw):
    pattern = Struct(
        "StartLsn" / Int64ul,
        "EndLsn" / Int64ul,
        "TransactionsRemaining" / Int64ul
    )


@declare(guid=guid("55b24b1d-dd9c-44c0-ba77-4f749f1b6976"), event_id=1020, version=2)
class Microsoft_Windows_Minstore_1020_2(Etw):
    pattern = Struct(
        "StartLsn" / Int64ul,
        "EndLsn" / Int64ul,
        "TransactionsRemaining" / Int64ul
    )

