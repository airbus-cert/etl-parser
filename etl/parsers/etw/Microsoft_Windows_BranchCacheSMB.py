# -*- coding: utf-8 -*-
"""
Microsoft-Windows-BranchCacheSMB
GUID : 4a933674-fb3d-4e8d-b01d-17ee14e91a3e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4a933674-fb3d-4e8d-b01d-17ee14e91a3e"), event_id=3000, version=0)
class Microsoft_Windows_BranchCacheSMB_3000_0(Etw):
    pattern = Struct(
        "MinHashVersion" / Int32ul,
        "MaxHashVersion" / Int32ul
    )


@declare(guid=guid("4a933674-fb3d-4e8d-b01d-17ee14e91a3e"), event_id=3002, version=0)
class Microsoft_Windows_BranchCacheSMB_3002_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("4a933674-fb3d-4e8d-b01d-17ee14e91a3e"), event_id=3003, version=0)
class Microsoft_Windows_BranchCacheSMB_3003_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "ContentHandle" / WString,
        "ResultCode" / WString,
        "Result" / WString
    )


@declare(guid=guid("4a933674-fb3d-4e8d-b01d-17ee14e91a3e"), event_id=3004, version=0)
class Microsoft_Windows_BranchCacheSMB_3004_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "ContentHandle" / WString,
        "ResultCode" / WString,
        "Result" / WString
    )


@declare(guid=guid("4a933674-fb3d-4e8d-b01d-17ee14e91a3e"), event_id=3005, version=0)
class Microsoft_Windows_BranchCacheSMB_3005_0(Etw):
    pattern = Struct(
        "ServiceActiveTimeInSeconds" / Int32ul,
        "SMBBranchCacheBytesRequested" / Int64ul,
        "SMBBranchCacheBytesReceived" / Int64ul,
        "SMBBranchCacheBytesPublished" / Int64ul,
        "SMBBranchCacheBytesRequestedFromServer" / Int64ul,
        "SMBBranchCacheHashesRequested" / Int32ul,
        "SMBBranchCacheHashesReceived" / Int32ul,
        "SMBBranchCacheHashBytesReceived" / Int64ul,
        "PrefetchOperationsQueued" / Int32ul,
        "PrefetchBytesReadFromCache" / Int64ul,
        "PrefetchBytesReadFromServer" / Int64ul,
        "ApplicationBytesReadFromCache" / Int64ul,
        "ApplicationBytesReadFromServer" / Int64ul,
        "ApplicationBytesReadFromServerNotCached" / Int64ul
    )


@declare(guid=guid("4a933674-fb3d-4e8d-b01d-17ee14e91a3e"), event_id=3012, version=0)
class Microsoft_Windows_BranchCacheSMB_3012_0(Etw):
    pattern = Struct(
        "CloseHandleCount" / WString,
        "OpenHandleCount" / WString,
        "ResultCode" / WString,
        "Result" / WString
    )


@declare(guid=guid("4a933674-fb3d-4e8d-b01d-17ee14e91a3e"), event_id=3013, version=0)
class Microsoft_Windows_BranchCacheSMB_3013_0(Etw):
    pattern = Struct(
        "CloseHandleCount" / WString,
        "OpenHandleCount" / WString,
        "ResultCode" / WString,
        "Result" / WString
    )

