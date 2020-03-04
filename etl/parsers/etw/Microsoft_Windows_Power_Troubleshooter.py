# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Power-Troubleshooter
GUID : cdc05e28-c449-49c6-b9d2-88cf761644df
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("cdc05e28-c449-49c6-b9d2-88cf761644df"), event_id=1, version=0)
class Microsoft_Windows_Power_Troubleshooter_1_0(Etw):
    pattern = Struct(
        "SleepTime" / Int64ul,
        "WakeTime" / Int64ul,
        "SleepDuration" / Int32ul,
        "WakeDuration" / Int32ul,
        "DriverInitDuration" / Int32ul,
        "BiosInitDuration" / Int32ul,
        "HiberWriteDuration" / Int32ul,
        "HiberReadDuration" / Int32ul,
        "HiberPagesWritten" / Int32ul,
        "Attributes" / Int32ul,
        "TargetState" / Int32ul,
        "EffectiveState" / Int32ul,
        "WakeSourceType" / Int32ul,
        "WakeSourceTextLength" / Int16ul,
        "WakeSourceText" / Bytes(lambda this: this.WakeSourceTextLength)
    )


@declare(guid=guid("cdc05e28-c449-49c6-b9d2-88cf761644df"), event_id=1, version=1)
class Microsoft_Windows_Power_Troubleshooter_1_1(Etw):
    pattern = Struct(
        "SleepTime" / Int64ul,
        "WakeTime" / Int64ul,
        "SleepDuration" / Int32ul,
        "WakeDuration" / Int32ul,
        "DriverInitDuration" / Int32ul,
        "BiosInitDuration" / Int32ul,
        "HiberWriteDuration" / Int32ul,
        "HiberReadDuration" / Int32ul,
        "HiberPagesWritten" / Int32ul,
        "Attributes" / Int32ul,
        "TargetState" / Int32ul,
        "EffectiveState" / Int32ul,
        "WakeSourceType" / Int32ul,
        "WakeSourceTextLength" / Int16ul,
        "WakeSourceText" / Bytes(lambda this: this.WakeSourceTextLength),
        "WakeTimerOwnerLength" / Int16ul,
        "WakeTimerContextLength" / Int16ul,
        "WakeTimerOwner" / Bytes(lambda this: this.WakeTimerOwnerLength),
        "WakeTimerContext" / Bytes(lambda this: this.WakeTimerContextLength)
    )


@declare(guid=guid("cdc05e28-c449-49c6-b9d2-88cf761644df"), event_id=1, version=2)
class Microsoft_Windows_Power_Troubleshooter_1_2(Etw):
    pattern = Struct(
        "SleepTime" / Int64ul,
        "WakeTime" / Int64ul,
        "SleepDuration" / Int32ul,
        "WakeDuration" / Int32ul,
        "DriverInitDuration" / Int32ul,
        "BiosInitDuration" / Int32ul,
        "HiberWriteDuration" / Int32ul,
        "HiberReadDuration" / Int32ul,
        "HiberPagesWritten" / Int32ul,
        "Attributes" / Int32ul,
        "TargetState" / Int32ul,
        "EffectiveState" / Int32ul,
        "WakeSourceType" / Int32ul,
        "WakeSourceTextLength" / Int16ul,
        "WakeSourceText" / Bytes(lambda this: this.WakeSourceTextLength),
        "WakeTimerOwnerLength" / Int16ul,
        "WakeTimerContextLength" / Int16ul,
        "NoMultiStageResumeReason" / Int32ul,
        "WakeTimerOwner" / Bytes(lambda this: this.WakeTimerOwnerLength),
        "WakeTimerContext" / Bytes(lambda this: this.WakeTimerContextLength)
    )


@declare(guid=guid("cdc05e28-c449-49c6-b9d2-88cf761644df"), event_id=1, version=3)
class Microsoft_Windows_Power_Troubleshooter_1_3(Etw):
    pattern = Struct(
        "SleepTime" / Int64ul,
        "WakeTime" / Int64ul,
        "SleepDuration" / Int32ul,
        "WakeDuration" / Int32ul,
        "DriverInitDuration" / Int32ul,
        "BiosInitDuration" / Int32ul,
        "HiberWriteDuration" / Int32ul,
        "HiberReadDuration" / Int32ul,
        "HiberPagesWritten" / Int32ul,
        "Attributes" / Int32ul,
        "TargetState" / Int32ul,
        "EffectiveState" / Int32ul,
        "WakeSourceType" / Int32ul,
        "WakeSourceTextLength" / Int16ul,
        "WakeSourceText" / Bytes(lambda this: this.WakeSourceTextLength),
        "WakeTimerOwnerLength" / Int16ul,
        "WakeTimerContextLength" / Int16ul,
        "NoMultiStageResumeReason" / Int32ul,
        "WakeTimerOwner" / Bytes(lambda this: this.WakeTimerOwnerLength),
        "WakeTimerContext" / Bytes(lambda this: this.WakeTimerContextLength),
        "CheckpointDuration" / Int32ul
    )

