# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DesktopWindowManager-Diag
GUID : 31f60101-3703-48ea-8143-451f8de779d2
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("31f60101-3703-48ea-8143-451f8de779d2"), event_id=1, version=0)
class Microsoft_Windows_DesktopWindowManager_Diag_1_0(Etw):
    pattern = Struct(
        "PercentLessThan4" / Int32ul,
        "PercentLessThan8" / Int32ul,
        "PercentLessThan16" / Int32ul,
        "PercentLessThan32" / Int32ul,
        "PercentLessThan50" / Int32ul,
        "PercentLessThan100" / Int32ul,
        "PercentLessThan500" / Int32ul,
        "PercentLessThan1000" / Int32ul,
        "PercentLessThan2000" / Int32ul,
        "PercentLessThan5000" / Int32ul,
        "PercentLessThan10000" / Int32ul,
        "PercentGreater10000" / Int32ul,
        "PercentMissedFlips" / Int32ul,
        "FrameRateReductions" / Int32ul,
        "DiagEventsFired" / Int32ul,
        "PeakPercentSysMemUsed" / Int32ul,
        "PeakWindowCount" / Int32ul,
        "DiagFrames" / Int32ul,
        "DiagStatsDuration" / Int32ul
    )


@declare(guid=guid("31f60101-3703-48ea-8143-451f8de779d2"), event_id=2, version=0)
class Microsoft_Windows_DesktopWindowManager_Diag_2_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Diagnosis" / Int32ul
    )

