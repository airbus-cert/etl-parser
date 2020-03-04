# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Diagnosis-Scheduled
GUID : 40ab57c2-1c53-4df9-9324-ff7cf898a02c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("40ab57c2-1c53-4df9-9324-ff7cf898a02c"), event_id=5, version=0)
class Microsoft_Windows_Diagnosis_Scheduled_5_0(Etw):
    pattern = Struct(
        "PackagePath" / WString
    )


@declare(guid=guid("40ab57c2-1c53-4df9-9324-ff7cf898a02c"), event_id=6, version=0)
class Microsoft_Windows_Diagnosis_Scheduled_6_0(Etw):
    pattern = Struct(
        "PackageID" / WString
    )


@declare(guid=guid("40ab57c2-1c53-4df9-9324-ff7cf898a02c"), event_id=7, version=0)
class Microsoft_Windows_Diagnosis_Scheduled_7_0(Etw):
    pattern = Struct(
        "PackageID" / WString
    )


@declare(guid=guid("40ab57c2-1c53-4df9-9324-ff7cf898a02c"), event_id=8, version=0)
class Microsoft_Windows_Diagnosis_Scheduled_8_0(Etw):
    pattern = Struct(
        "PackageID" / WString,
        "RootCauseCount" / Int32sl
    )


@declare(guid=guid("40ab57c2-1c53-4df9-9324-ff7cf898a02c"), event_id=9, version=0)
class Microsoft_Windows_Diagnosis_Scheduled_9_0(Etw):
    pattern = Struct(
        "RootCauseID" / WString,
        "RootCauseName" / WString,
        "RootCauseDescription" / WString
    )


@declare(guid=guid("40ab57c2-1c53-4df9-9324-ff7cf898a02c"), event_id=10, version=0)
class Microsoft_Windows_Diagnosis_Scheduled_10_0(Etw):
    pattern = Struct(
        "RootCauseID" / WString,
        "ResolutionID" / WString
    )


@declare(guid=guid("40ab57c2-1c53-4df9-9324-ff7cf898a02c"), event_id=11, version=0)
class Microsoft_Windows_Diagnosis_Scheduled_11_0(Etw):
    pattern = Struct(
        "RootCauseID" / WString,
        "ResolutionID" / WString
    )


@declare(guid=guid("40ab57c2-1c53-4df9-9324-ff7cf898a02c"), event_id=12, version=0)
class Microsoft_Windows_Diagnosis_Scheduled_12_0(Etw):
    pattern = Struct(
        "RootCauseID" / WString
    )


@declare(guid=guid("40ab57c2-1c53-4df9-9324-ff7cf898a02c"), event_id=13, version=0)
class Microsoft_Windows_Diagnosis_Scheduled_13_0(Etw):
    pattern = Struct(
        "RootCauseID" / WString
    )


@declare(guid=guid("40ab57c2-1c53-4df9-9324-ff7cf898a02c"), event_id=14, version=0)
class Microsoft_Windows_Diagnosis_Scheduled_14_0(Etw):
    pattern = Struct(
        "RootCauseID" / WString
    )


@declare(guid=guid("40ab57c2-1c53-4df9-9324-ff7cf898a02c"), event_id=15, version=0)
class Microsoft_Windows_Diagnosis_Scheduled_15_0(Etw):
    pattern = Struct(
        "PackageID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("40ab57c2-1c53-4df9-9324-ff7cf898a02c"), event_id=96, version=0)
class Microsoft_Windows_Diagnosis_Scheduled_96_0(Etw):
    pattern = Struct(
        "hc_stateid" / Int32ul,
        "Data1" / WString,
        "Data2" / WString
    )


@declare(guid=guid("40ab57c2-1c53-4df9-9324-ff7cf898a02c"), event_id=97, version=0)
class Microsoft_Windows_Diagnosis_Scheduled_97_0(Etw):
    pattern = Struct(
        "hc_stateid" / Int32ul
    )


@declare(guid=guid("40ab57c2-1c53-4df9-9324-ff7cf898a02c"), event_id=98, version=0)
class Microsoft_Windows_Diagnosis_Scheduled_98_0(Etw):
    pattern = Struct(
        "hc_stateid" / Int32ul,
        "Data1" / WString,
        "Data2" / WString
    )


@declare(guid=guid("40ab57c2-1c53-4df9-9324-ff7cf898a02c"), event_id=99, version=0)
class Microsoft_Windows_Diagnosis_Scheduled_99_0(Etw):
    pattern = Struct(
        "hc_stateid" / Int32ul
    )


@declare(guid=guid("40ab57c2-1c53-4df9-9324-ff7cf898a02c"), event_id=100, version=0)
class Microsoft_Windows_Diagnosis_Scheduled_100_0(Etw):
    pattern = Struct(
        "hc_stateid" / Int32ul
    )

