# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MMCSS
GUID : 36008301-e154-466c-acec-5f4cbd6b4694
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("36008301-e154-466c-acec-5f4cbd6b4694"), event_id=1, version=1)
class Microsoft_Windows_MMCSS_1_1(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "ThreadID" / Int32ul,
        "Priority" / Int8ul,
        "TaskIndex" / Int32ul
    )


@declare(guid=guid("36008301-e154-466c-acec-5f4cbd6b4694"), event_id=2, version=1)
class Microsoft_Windows_MMCSS_2_1(Etw):
    pattern = Struct(
        "Reason" / Int32ul
    )


@declare(guid=guid("36008301-e154-466c-acec-5f4cbd6b4694"), event_id=3, version=1)
class Microsoft_Windows_MMCSS_3_1(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Duration" / Int32ul
    )


@declare(guid=guid("36008301-e154-466c-acec-5f4cbd6b4694"), event_id=7, version=1)
class Microsoft_Windows_MMCSS_7_1(Etw):
    pattern = Struct(
        "ThreadID" / Int32ul,
        "MediumPriority" / Int8ul,
        "LowPriority" / Int8ul,
        "UberLowPriority" / Int8ul,
        "TaskName" / WString,
        "TaskIndex" / Int32ul,
        "Category" / Int8ul,
        "Flags" / Int8ul
    )


@declare(guid=guid("36008301-e154-466c-acec-5f4cbd6b4694"), event_id=8, version=1)
class Microsoft_Windows_MMCSS_8_1(Etw):
    pattern = Struct(
        "ThreadID" / Int32ul,
        "OriginalBasePriority" / Int8ul
    )


@declare(guid=guid("36008301-e154-466c-acec-5f4cbd6b4694"), event_id=12, version=1)
class Microsoft_Windows_MMCSS_12_1(Etw):
    pattern = Struct(
        "TaskIndex" / Int32ul,
        "Duration" / Int32ul,
        "PreDuration" / Int32ul
    )


@declare(guid=guid("36008301-e154-466c-acec-5f4cbd6b4694"), event_id=13, version=1)
class Microsoft_Windows_MMCSS_13_1(Etw):
    pattern = Struct(
        "TaskIndex" / Int32ul
    )


@declare(guid=guid("36008301-e154-466c-acec-5f4cbd6b4694"), event_id=14, version=1)
class Microsoft_Windows_MMCSS_14_1(Etw):
    pattern = Struct(
        "TaskIndex" / Int32ul,
        "ThreadTag" / Int32ul
    )


@declare(guid=guid("36008301-e154-466c-acec-5f4cbd6b4694"), event_id=15, version=1)
class Microsoft_Windows_MMCSS_15_1(Etw):
    pattern = Struct(
        "TaskIndex" / Int32ul
    )


@declare(guid=guid("36008301-e154-466c-acec-5f4cbd6b4694"), event_id=16, version=1)
class Microsoft_Windows_MMCSS_16_1(Etw):
    pattern = Struct(
        "TurboEngaged" / Int32ul
    )


@declare(guid=guid("36008301-e154-466c-acec-5f4cbd6b4694"), event_id=17, version=1)
class Microsoft_Windows_MMCSS_17_1(Etw):
    pattern = Struct(
        "ThreadID" / Int32ul
    )


@declare(guid=guid("36008301-e154-466c-acec-5f4cbd6b4694"), event_id=18, version=1)
class Microsoft_Windows_MMCSS_18_1(Etw):
    pattern = Struct(
        "ThreadID" / Int32ul
    )


@declare(guid=guid("36008301-e154-466c-acec-5f4cbd6b4694"), event_id=19, version=1)
class Microsoft_Windows_MMCSS_19_1(Etw):
    pattern = Struct(
        "TaskIndex" / Int32ul
    )

