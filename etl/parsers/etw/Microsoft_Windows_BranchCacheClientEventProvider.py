# -*- coding: utf-8 -*-
"""
Microsoft-Windows-BranchCacheClientEventProvider
GUID : e837619c-a2a8-4689-833f-47b48ebd2442
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e837619c-a2a8-4689-833f-47b48ebd2442"), event_id=10103, version=0)
class Microsoft_Windows_BranchCacheClientEventProvider_10103_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("e837619c-a2a8-4689-833f-47b48ebd2442"), event_id=10105, version=0)
class Microsoft_Windows_BranchCacheClientEventProvider_10105_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("e837619c-a2a8-4689-833f-47b48ebd2442"), event_id=10107, version=0)
class Microsoft_Windows_BranchCacheClientEventProvider_10107_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )

