# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Diagnostics-PerfTrack-Counters
GUID : c06ed57a-a7bd-42d7-b5ff-77a9dec5732d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c06ed57a-a7bd-42d7-b5ff-77a9dec5732d"), event_id=2000, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_Counters_2000_0(Etw):
    pattern = Struct(
        "WorkingSetPrivateSize" / Int64sl,
        "QuotaNonPagedPoolUsage" / Int64ul,
        "QuotaPagedPoolUsage" / Int64ul,
        "PrivatePageCount" / Int64ul,
        "VirtualSize" / Int64ul,
        "WorkingSetSize" / Int64ul,
        "HandleCount" / Int32ul,
        "SessionId" / Int32ul,
        "ProcessId" / Int32ul,
        "ProcessName" / WString
    )


@declare(guid=guid("c06ed57a-a7bd-42d7-b5ff-77a9dec5732d"), event_id=2001, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_Counters_2001_0(Etw):
    pattern = Struct(
        "CurrentSize" / Int64ul,
        "PeakSize" / Int64ul,
        "MinimumWorkingSet" / Int64ul,
        "MaximumWorkingSet" / Int64ul,
        "CurrentSizeIncludingTransitionInPages" / Int64ul,
        "PeakSizeIncludingTransitionInPages" / Int64ul,
        "PageFaultCount" / Int32ul,
        "TransitionRePurposeCount" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("c06ed57a-a7bd-42d7-b5ff-77a9dec5732d"), event_id=2002, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_Counters_2002_0(Etw):
    pattern = Struct(
        "PagedPoolPages" / Int32ul,
        "NonPagedPoolPages" / Int32ul
    )


@declare(guid=guid("c06ed57a-a7bd-42d7-b5ff-77a9dec5732d"), event_id=2003, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_Counters_2003_0(Etw):
    pattern = Struct(
        "PagedPoolPages" / Int64ul,
        "NonPagedPoolPages" / Int64ul,
        "SessionId" / Int32ul
    )


@declare(guid=guid("c06ed57a-a7bd-42d7-b5ff-77a9dec5732d"), event_id=2004, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_Counters_2004_0(Etw):
    pattern = Struct(
        "PagedAllocs" / Int32ul,
        "PagedFrees" / Int32ul,
        "PagedUsed" / Int64ul,
        "NonPagedAllocs" / Int32ul,
        "NonPagedFrees" / Int32ul,
        "NonPagedUsed" / Int64ul,
        "Tag" / CString
    )


@declare(guid=guid("c06ed57a-a7bd-42d7-b5ff-77a9dec5732d"), event_id=2005, version=0)
class Microsoft_Windows_Diagnostics_PerfTrack_Counters_2005_0(Etw):
    pattern = Struct(
        "PagedAllocs" / Int32ul,
        "PagedFrees" / Int32ul,
        "PagedUsed" / Int64ul,
        "NonPagedAllocs" / Int32ul,
        "NonPagedFrees" / Int32ul,
        "NonPagedUsed" / Int64ul,
        "SessionId" / Int32ul,
        "Tag" / CString
    )

