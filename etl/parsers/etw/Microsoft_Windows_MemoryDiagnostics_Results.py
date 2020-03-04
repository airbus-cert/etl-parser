# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MemoryDiagnostics-Results
GUID : 5f92bc59-248f-4111-86a9-e393e12c6139
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5f92bc59-248f-4111-86a9-e393e12c6139"), event_id=1101, version=0)
class Microsoft_Windows_MemoryDiagnostics_Results_1101_0(Etw):
    pattern = Struct(
        "LaunchType" / WString,
        "CompletionType" / WString,
        "MemorySize" / Int32ul,
        "TestType" / Int32ul,
        "TestDuration" / Int32ul,
        "TestCount" / Int32ul,
        "NumPagesTested" / Int32ul,
        "NumPagesUnTested" / Int32ul,
        "NumBadPages" / Int32ul,
        "T1NumBadPages" / Int32ul,
        "T2NumBadPages" / Int32ul,
        "T3NumBadPages" / Int32ul,
        "T4NumBadPages" / Int32ul,
        "T5NumBadPages" / Int32ul,
        "T6NumBadPages" / Int32ul,
        "T7NumBadPages" / Int32ul,
        "T8NumBadPages" / Int32ul,
        "T9NumBadPages" / Int32ul,
        "T10NumBadPages" / Int32ul,
        "T11NumBadPages" / Int32ul,
        "T12NumBadPages" / Int32ul,
        "T13NumBadPages" / Int32ul,
        "T14NumBadPages" / Int32ul,
        "T15NumBadPages" / Int32ul,
        "T16NumBadPages" / Int32ul
    )


@declare(guid=guid("5f92bc59-248f-4111-86a9-e393e12c6139"), event_id=1102, version=0)
class Microsoft_Windows_MemoryDiagnostics_Results_1102_0(Etw):
    pattern = Struct(
        "LaunchType" / WString,
        "CompletionType" / WString,
        "MemorySize" / Int32ul,
        "TestType" / Int32ul,
        "TestDuration" / Int32ul,
        "TestCount" / Int32ul,
        "NumPagesTested" / Int32ul,
        "NumPagesUnTested" / Int32ul,
        "NumBadPages" / Int32ul,
        "T1NumBadPages" / Int32ul,
        "T2NumBadPages" / Int32ul,
        "T3NumBadPages" / Int32ul,
        "T4NumBadPages" / Int32ul,
        "T5NumBadPages" / Int32ul,
        "T6NumBadPages" / Int32ul,
        "T7NumBadPages" / Int32ul,
        "T8NumBadPages" / Int32ul,
        "T9NumBadPages" / Int32ul,
        "T10NumBadPages" / Int32ul,
        "T11NumBadPages" / Int32ul,
        "T12NumBadPages" / Int32ul,
        "T13NumBadPages" / Int32ul,
        "T14NumBadPages" / Int32ul,
        "T15NumBadPages" / Int32ul,
        "T16NumBadPages" / Int32ul
    )


@declare(guid=guid("5f92bc59-248f-4111-86a9-e393e12c6139"), event_id=1103, version=0)
class Microsoft_Windows_MemoryDiagnostics_Results_1103_0(Etw):
    pattern = Struct(
        "LaunchType" / WString,
        "CompletionType" / WString,
        "MemorySize" / Int32ul,
        "TestType" / Int32ul,
        "TestDuration" / Int32ul,
        "TestCount" / Int32ul,
        "NumPagesTested" / Int32ul,
        "NumPagesUnTested" / Int32ul,
        "NumBadPages" / Int32ul,
        "T1NumBadPages" / Int32ul,
        "T2NumBadPages" / Int32ul,
        "T3NumBadPages" / Int32ul,
        "T4NumBadPages" / Int32ul,
        "T5NumBadPages" / Int32ul,
        "T6NumBadPages" / Int32ul,
        "T7NumBadPages" / Int32ul,
        "T8NumBadPages" / Int32ul,
        "T9NumBadPages" / Int32ul,
        "T10NumBadPages" / Int32ul,
        "T11NumBadPages" / Int32ul,
        "T12NumBadPages" / Int32ul,
        "T13NumBadPages" / Int32ul,
        "T14NumBadPages" / Int32ul,
        "T15NumBadPages" / Int32ul,
        "T16NumBadPages" / Int32ul
    )


@declare(guid=guid("5f92bc59-248f-4111-86a9-e393e12c6139"), event_id=1104, version=0)
class Microsoft_Windows_MemoryDiagnostics_Results_1104_0(Etw):
    pattern = Struct(
        "LaunchType" / WString,
        "CompletionType" / WString,
        "MemorySize" / Int32ul,
        "TestType" / Int32ul,
        "TestDuration" / Int32ul,
        "TestCount" / Int32ul,
        "NumPagesTested" / Int32ul,
        "NumPagesUnTested" / Int32ul,
        "NumBadPages" / Int32ul,
        "T1NumBadPages" / Int32ul,
        "T2NumBadPages" / Int32ul,
        "T3NumBadPages" / Int32ul,
        "T4NumBadPages" / Int32ul,
        "T5NumBadPages" / Int32ul,
        "T6NumBadPages" / Int32ul,
        "T7NumBadPages" / Int32ul,
        "T8NumBadPages" / Int32ul,
        "T9NumBadPages" / Int32ul,
        "T10NumBadPages" / Int32ul,
        "T11NumBadPages" / Int32ul,
        "T12NumBadPages" / Int32ul,
        "T13NumBadPages" / Int32ul,
        "T14NumBadPages" / Int32ul,
        "T15NumBadPages" / Int32ul,
        "T16NumBadPages" / Int32ul
    )


@declare(guid=guid("5f92bc59-248f-4111-86a9-e393e12c6139"), event_id=1201, version=0)
class Microsoft_Windows_MemoryDiagnostics_Results_1201_0(Etw):
    pattern = Struct(
        "CompletionType" / WString
    )


@declare(guid=guid("5f92bc59-248f-4111-86a9-e393e12c6139"), event_id=1202, version=0)
class Microsoft_Windows_MemoryDiagnostics_Results_1202_0(Etw):
    pattern = Struct(
        "CompletionType" / WString
    )


@declare(guid=guid("5f92bc59-248f-4111-86a9-e393e12c6139"), event_id=2001, version=0)
class Microsoft_Windows_MemoryDiagnostics_Results_2001_0(Etw):
    pattern = Struct(
        "MemDiagRawDataLength" / Int32ul,
        "MemDiagRawData" / Bytes(lambda this: this.MemDiagRawDataLength)
    )

