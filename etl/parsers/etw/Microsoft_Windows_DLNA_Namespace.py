# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DLNA-Namespace
GUID : d38fb874-33e4-4dcf-911e-1b53bb106d53
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d38fb874-33e4-4dcf-911e-1b53bb106d53"), event_id=1001, version=0)
class Microsoft_Windows_DLNA_Namespace_1001_0(Etw):
    pattern = Struct(
        "HResultParam" / Int32ul
    )


@declare(guid=guid("d38fb874-33e4-4dcf-911e-1b53bb106d53"), event_id=1002, version=0)
class Microsoft_Windows_DLNA_Namespace_1002_0(Etw):
    pattern = Struct(
        "HResultParam" / Int32ul
    )


@declare(guid=guid("d38fb874-33e4-4dcf-911e-1b53bb106d53"), event_id=1003, version=0)
class Microsoft_Windows_DLNA_Namespace_1003_0(Etw):
    pattern = Struct(
        "ObjectID" / WString,
        "IsBrowseDirectChildren" / Int32ul,
        "Filter" / WString,
        "SortCriteria" / WString,
        "StartingOffset" / Int32ul,
        "NumItemsToRetrieve" / Int32ul,
        "NumItemsReturned" / Int32ul,
        "NumItemsMatched" / Int32ul,
        "HResultParam" / Int32ul
    )


@declare(guid=guid("d38fb874-33e4-4dcf-911e-1b53bb106d53"), event_id=1004, version=0)
class Microsoft_Windows_DLNA_Namespace_1004_0(Etw):
    pattern = Struct(
        "ObjectID" / WString,
        "IsBrowseDirectChildren" / Int32ul,
        "Filter" / WString,
        "SortCriteria" / WString,
        "StartingOffset" / Int32ul,
        "NumItemsToRetrieve" / Int32ul,
        "NumItemsReturned" / Int32ul,
        "NumItemsMatched" / Int32ul,
        "HResultParam" / Int32ul
    )


@declare(guid=guid("d38fb874-33e4-4dcf-911e-1b53bb106d53"), event_id=1005, version=0)
class Microsoft_Windows_DLNA_Namespace_1005_0(Etw):
    pattern = Struct(
        "ObjectID" / WString,
        "SearchCriteria" / WString,
        "Filter" / WString,
        "SortCriteria" / WString,
        "StartingOffset" / Int32ul,
        "NumItemsToRetrieve" / Int32ul,
        "NumItemsReturned" / Int32ul,
        "NumItemsMatched" / Int32ul,
        "HResultParam" / Int32ul
    )


@declare(guid=guid("d38fb874-33e4-4dcf-911e-1b53bb106d53"), event_id=1006, version=0)
class Microsoft_Windows_DLNA_Namespace_1006_0(Etw):
    pattern = Struct(
        "ObjectID" / WString,
        "SearchCriteria" / WString,
        "Filter" / WString,
        "SortCriteria" / WString,
        "StartingOffset" / Int32ul,
        "NumItemsToRetrieve" / Int32ul,
        "NumItemsReturned" / Int32ul,
        "NumItemsMatched" / Int32ul,
        "HResultParam" / Int32ul
    )

