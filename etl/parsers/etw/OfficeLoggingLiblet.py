# -*- coding: utf-8 -*-
"""
OfficeLoggingLiblet
GUID : f50d9315-e17e-43c1-8370-3edf6cc057be
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=100, version=0)
class OfficeLoggingLiblet_100_0(Etw):
    pattern = Struct(
        "wzProduct" / WString,
        "wzCategory" / WString,
        "wzTag" / WString,
        "wzMessage" / WString
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=101, version=0)
class OfficeLoggingLiblet_101_0(Etw):
    pattern = Struct(
        "wzProduct" / WString,
        "wzCategory" / WString,
        "wzTag" / WString,
        "wzMessage" / WString
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=102, version=0)
class OfficeLoggingLiblet_102_0(Etw):
    pattern = Struct(
        "wzProduct" / WString,
        "wzCategory" / WString,
        "wzTag" / WString,
        "wzMessage" / WString
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=103, version=0)
class OfficeLoggingLiblet_103_0(Etw):
    pattern = Struct(
        "wzProduct" / WString,
        "wzCategory" / WString,
        "wzTag" / WString,
        "wzMessage" / WString
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=104, version=0)
class OfficeLoggingLiblet_104_0(Etw):
    pattern = Struct(
        "wzProduct" / WString,
        "wzCategory" / WString,
        "wzTag" / WString,
        "wzMessage" / WString
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=105, version=0)
class OfficeLoggingLiblet_105_0(Etw):
    pattern = Struct(
        "dwTag" / Int32ul,
        "dwInstanceId" / Int32ul,
        "dwParentInstanceId" / Int32ul,
        "lpScopeName" / WString,
        "lpParentScenarioName" / WString,
        "dwParentScenarioTag" / Int32ul
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=106, version=0)
class OfficeLoggingLiblet_106_0(Etw):
    pattern = Struct(
        "dwTag" / Int32ul,
        "dwInstanceId" / Int32ul,
        "dwParentInstanceId" / Int32ul
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=107, version=0)
class OfficeLoggingLiblet_107_0(Etw):
    pattern = Struct(
        "dwTag" / Int32ul,
        "dwInstanceId" / Int32ul,
        "dwParentInstanceId" / Int32ul,
        "bWasSuccessful" / Int8ul,
        "bWasErrorCodeSet" / Int8ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=108, version=0)
class OfficeLoggingLiblet_108_0(Etw):
    pattern = Struct(
        "dwTag" / Int32ul,
        "dwInstanceId" / Int32ul,
        "lpScenarioName" / WString
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=109, version=0)
class OfficeLoggingLiblet_109_0(Etw):
    pattern = Struct(
        "dwTag" / Int32ul,
        "dwInstanceId" / Int32ul
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=110, version=0)
class OfficeLoggingLiblet_110_0(Etw):
    pattern = Struct(
        "dwTag" / Int32ul,
        "dwInstanceId" / Int32ul,
        "bWasSuccessful" / Int8ul,
        "bWasErrorCodeSet" / Int8ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=200, version=0)
class OfficeLoggingLiblet_200_0(Etw):
    pattern = Struct(
        "dwTag" / Int32ul,
        "dwInstanceId" / Int32ul,
        "FilesCreated" / Int64sl,
        "NumberOfFileReads" / Int64sl,
        "TotalBytesRead" / Int64sl,
        "NumberOfFileWrites" / Int64sl,
        "TotalBytesWritten" / Int64sl,
        "NumberOfSetEndOfFiles" / Int64sl,
        "NumberOfSeeks" / Int64sl,
        "NumberOfLocks" / Int64sl,
        "NumberOfUnlocks" / Int64sl
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=201, version=0)
class OfficeLoggingLiblet_201_0(Etw):
    pattern = Struct(
        "dwTag" / Int32ul,
        "dwInstanceId" / Int32ul,
        "Requests" / Int64sl,
        "BytesSent" / Int64sl,
        "ElapsedMilliseconds" / Int64sl,
        "BytesReceived" / Int64sl
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=202, version=0)
class OfficeLoggingLiblet_202_0(Etw):
    pattern = Struct(
        "dwTag" / Int32ul,
        "dwInstanceId" / Int32ul,
        "BytesUsedDelta" / Int64sl,
        "BytesUsedAtComplete" / Int64ul
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=1000, version=0)
class OfficeLoggingLiblet_1000_0(Etw):
    pattern = Struct(
        "Tag" / Int32ul,
        "InstanceId" / Int32ul,
        "ResourceScopePtr" / Int64ul,
        "FileUsagePtr" / Int64ul
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=1001, version=0)
class OfficeLoggingLiblet_1001_0(Etw):
    pattern = Struct(
        "Tag" / Int32ul,
        "InstanceId" / Int32ul,
        "ScopePtr" / Int64ul
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=1002, version=0)
class OfficeLoggingLiblet_1002_0(Etw):
    pattern = Struct(
        "Tag" / Int32ul,
        "InstanceId" / Int32ul,
        "ResourceScopePtr" / Int64ul,
        "NetworkUsagePtr" / Int64ul
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=1003, version=0)
class OfficeLoggingLiblet_1003_0(Etw):
    pattern = Struct(
        "ChildScopePtr" / Int64ul,
        "ParentScopePtr" / Int64ul,
        "TypeOfData" / WString
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=1004, version=0)
class OfficeLoggingLiblet_1004_0(Etw):
    pattern = Struct(
        "Result" / Int8ul,
        "StartCounter" / Int64sl
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=1005, version=0)
class OfficeLoggingLiblet_1005_0(Etw):
    pattern = Struct(
        "Result" / Int8ul,
        "StartCounter" / Int64sl,
        "StopCounter" / Int64sl,
        "ElapsedCounters" / Int64sl,
        "ElapsedMilliseconds" / Int64sl
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=1006, version=0)
class OfficeLoggingLiblet_1006_0(Etw):
    pattern = Struct(
        "Result" / Int8ul,
        "Frequency" / Int64sl
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=1007, version=0)
class OfficeLoggingLiblet_1007_0(Etw):
    pattern = Struct(
        "FunctionName" / WString,
        "CurrentResourcePrt" / Int64ul
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=1008, version=0)
class OfficeLoggingLiblet_1008_0(Etw):
    pattern = Struct(
        "Tag" / Int32ul,
        "InstanceId" / Int32ul,
        "ScopePtr" / Int64ul
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=1009, version=0)
class OfficeLoggingLiblet_1009_0(Etw):
    pattern = Struct(
        "Tag" / Int32ul,
        "InstanceId" / Int32ul,
        "ResourceScopePtr" / Int64ul,
        "MemoryUsagePtr" / Int64ul
    )


@declare(guid=guid("f50d9315-e17e-43c1-8370-3edf6cc057be"), event_id=1010, version=0)
class OfficeLoggingLiblet_1010_0(Etw):
    pattern = Struct(
        "Tag" / Int32ul,
        "InstanceId" / Int32ul,
        "ScopePtr" / Int64ul
    )

