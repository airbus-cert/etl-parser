# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-Prefetch
GUID : 5322d61a-9efa-4bc3-a3f9-14be95c144f8
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5322d61a-9efa-4bc3-a3f9-14be95c144f8"), event_id=1, version=0)
class Microsoft_Windows_Kernel_Prefetch_1_0(Etw):
    pattern = Struct(
        "ScenarioNameLength" / Int16ul,
        "ScenarioName" / Bytes(lambda this: this.ScenarioNameLength),
        "ScenarioHashId" / Int32ul,
        "ScenarioType" / Int32ul,
        "PrefetchPhase" / Int32ul,
        "PrefetchType" / Int32ul,
        "IsTricklePhase" / Int8ul
    )


@declare(guid=guid("5322d61a-9efa-4bc3-a3f9-14be95c144f8"), event_id=1, version=1)
class Microsoft_Windows_Kernel_Prefetch_1_1(Etw):
    pattern = Struct(
        "ScenarioNameLength" / Int16ul,
        "ScenarioName" / Bytes(lambda this: this.ScenarioNameLength),
        "ScenarioHashId" / Int32ul,
        "ScenarioType" / Int32ul,
        "PrefetchPhaseMask" / Int32ul,
        "PrefetchType" / Int32ul,
        "IsTricklePhase" / Int8ul
    )


@declare(guid=guid("5322d61a-9efa-4bc3-a3f9-14be95c144f8"), event_id=2, version=0)
class Microsoft_Windows_Kernel_Prefetch_2_0(Etw):
    pattern = Struct(
        "ScenarioNameLength" / Int16ul,
        "ScenarioName" / Bytes(lambda this: this.ScenarioNameLength),
        "ScenarioHashId" / Int32ul,
        "ScenarioType" / Int32ul,
        "PrefetchPhase" / Int32ul,
        "PrefetchType" / Int32ul,
        "IsTricklePhase" / Int8ul,
        "NumPagesPrefetched" / Int64ul,
        "NumReadLists" / Int32ul
    )


@declare(guid=guid("5322d61a-9efa-4bc3-a3f9-14be95c144f8"), event_id=2, version=1)
class Microsoft_Windows_Kernel_Prefetch_2_1(Etw):
    pattern = Struct(
        "ScenarioNameLength" / Int16ul,
        "ScenarioName" / Bytes(lambda this: this.ScenarioNameLength),
        "ScenarioHashId" / Int32ul,
        "ScenarioType" / Int32ul,
        "PrefetchPhaseMask" / Int32ul,
        "PrefetchType" / Int32ul,
        "IsTricklePhase" / Int8ul,
        "NumPagesPrefetched" / Int64ul,
        "NumReadLists" / Int32ul
    )


@declare(guid=guid("5322d61a-9efa-4bc3-a3f9-14be95c144f8"), event_id=3, version=0)
class Microsoft_Windows_Kernel_Prefetch_3_0(Etw):
    pattern = Struct(
        "ScenarioNameLength" / Int16ul,
        "ScenarioName" / Bytes(lambda this: this.ScenarioNameLength),
        "ScenarioHashId" / Int32ul,
        "ScenarioType" / Int32ul,
        "PrefetchPhase" / Int32ul
    )


@declare(guid=guid("5322d61a-9efa-4bc3-a3f9-14be95c144f8"), event_id=3, version=1)
class Microsoft_Windows_Kernel_Prefetch_3_1(Etw):
    pattern = Struct(
        "ScenarioNameLength" / Int16ul,
        "ScenarioName" / Bytes(lambda this: this.ScenarioNameLength),
        "ScenarioHashId" / Int32ul,
        "ScenarioType" / Int32ul,
        "PrefetchPhaseMask" / Int32ul
    )


@declare(guid=guid("5322d61a-9efa-4bc3-a3f9-14be95c144f8"), event_id=4, version=0)
class Microsoft_Windows_Kernel_Prefetch_4_0(Etw):
    pattern = Struct(
        "ScenarioNameLength" / Int16ul,
        "ScenarioName" / Bytes(lambda this: this.ScenarioNameLength),
        "ScenarioHashId" / Int32ul,
        "ScenarioType" / Int32ul,
        "PrefetchPhase" / Int32ul
    )


@declare(guid=guid("5322d61a-9efa-4bc3-a3f9-14be95c144f8"), event_id=4, version=1)
class Microsoft_Windows_Kernel_Prefetch_4_1(Etw):
    pattern = Struct(
        "ScenarioNameLength" / Int16ul,
        "ScenarioName" / Bytes(lambda this: this.ScenarioNameLength),
        "ScenarioHashId" / Int32ul,
        "ScenarioType" / Int32ul,
        "PrefetchPhaseMask" / Int32ul
    )


@declare(guid=guid("5322d61a-9efa-4bc3-a3f9-14be95c144f8"), event_id=5, version=0)
class Microsoft_Windows_Kernel_Prefetch_5_0(Etw):
    pattern = Struct(
        "ScenarioNameLength" / Int16ul,
        "ScenarioName" / Bytes(lambda this: this.ScenarioNameLength),
        "ScenarioHashId" / Int32ul,
        "ScenarioType" / Int32ul
    )


@declare(guid=guid("5322d61a-9efa-4bc3-a3f9-14be95c144f8"), event_id=6, version=0)
class Microsoft_Windows_Kernel_Prefetch_6_0(Etw):
    pattern = Struct(
        "ScenarioNameLength" / Int16ul,
        "ScenarioName" / Bytes(lambda this: this.ScenarioNameLength),
        "ScenarioHashId" / Int32ul,
        "ScenarioType" / Int32ul
    )


@declare(guid=guid("5322d61a-9efa-4bc3-a3f9-14be95c144f8"), event_id=7, version=0)
class Microsoft_Windows_Kernel_Prefetch_7_0(Etw):
    pattern = Struct(
        "ScenarioNameLength" / Int16ul,
        "ScenarioName" / Bytes(lambda this: this.ScenarioNameLength),
        "ScenarioHashId" / Int32ul,
        "ScenarioType" / Int32ul,
        "EndReason" / Int32ul
    )


@declare(guid=guid("5322d61a-9efa-4bc3-a3f9-14be95c144f8"), event_id=8, version=0)
class Microsoft_Windows_Kernel_Prefetch_8_0(Etw):
    pattern = Struct(
        "ScenarioNameLength" / Int16ul,
        "ScenarioName" / Bytes(lambda this: this.ScenarioNameLength),
        "ScenarioHashId" / Int32ul,
        "ScenarioType" / Int32ul,
        "ActionFlags" / Int16ul,
        "TraceReason" / Int8ul,
        "PrefetchReason" / Int8ul
    )


@declare(guid=guid("5322d61a-9efa-4bc3-a3f9-14be95c144f8"), event_id=8, version=1)
class Microsoft_Windows_Kernel_Prefetch_8_1(Etw):
    pattern = Struct(
        "ScenarioNameLength" / Int16ul,
        "ScenarioName" / Bytes(lambda this: this.ScenarioNameLength),
        "ScenarioHashId" / Int32ul,
        "ScenarioType" / Int32ul,
        "ActionFlags" / Int16ul,
        "TraceReason" / Int8ul,
        "PrefetchReason" / Int8ul,
        "NumLaunches" / Int32ul,
        "TimeSinceLastLaunchInS" / Int32ul
    )


@declare(guid=guid("5322d61a-9efa-4bc3-a3f9-14be95c144f8"), event_id=9, version=1)
class Microsoft_Windows_Kernel_Prefetch_9_1(Etw):
    pattern = Struct(
        "ScenarioNameLength" / Int16ul,
        "ScenarioName" / Bytes(lambda this: this.ScenarioNameLength),
        "ScenarioHashId" / Int32ul,
        "ScenarioType" / Int32ul,
        "WorkItemsCount" / Int32ul
    )


@declare(guid=guid("5322d61a-9efa-4bc3-a3f9-14be95c144f8"), event_id=10, version=1)
class Microsoft_Windows_Kernel_Prefetch_10_1(Etw):
    pattern = Struct(
        "ScenarioNameLength" / Int16ul,
        "ScenarioName" / Bytes(lambda this: this.ScenarioNameLength),
        "ScenarioHashId" / Int32ul,
        "ScenarioType" / Int32ul
    )


@declare(guid=guid("5322d61a-9efa-4bc3-a3f9-14be95c144f8"), event_id=11, version=0)
class Microsoft_Windows_Kernel_Prefetch_11_0(Etw):
    pattern = Struct(
        "ScenarioNameLength" / Int16ul,
        "ScenarioName" / Bytes(lambda this: this.ScenarioNameLength),
        "ScenarioHashId" / Int32ul,
        "ScenarioType" / Int32ul,
        "NumPhases" / Int32ul
    )


@declare(guid=guid("5322d61a-9efa-4bc3-a3f9-14be95c144f8"), event_id=12, version=0)
class Microsoft_Windows_Kernel_Prefetch_12_0(Etw):
    pattern = Struct(
        "ScenarioNameLength" / Int16ul,
        "ScenarioName" / Bytes(lambda this: this.ScenarioNameLength),
        "ScenarioHashId" / Int32ul,
        "ScenarioType" / Int32ul
    )


@declare(guid=guid("5322d61a-9efa-4bc3-a3f9-14be95c144f8"), event_id=13, version=0)
class Microsoft_Windows_Kernel_Prefetch_13_0(Etw):
    pattern = Struct(
        "ScenarioNameLength" / Int16ul,
        "ScenarioName" / Bytes(lambda this: this.ScenarioNameLength),
        "ScenarioHashId" / Int32ul,
        "ScenarioType" / Int32ul
    )

