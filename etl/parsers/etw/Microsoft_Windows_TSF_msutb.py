# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TSF-msutb
GUID : 74b655a2-8958-410e-80e2-3457051b8dff
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("74b655a2-8958-410e-80e2-3457051b8dff"), event_id=1, version=0)
class Microsoft_Windows_TSF_msutb_1_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("74b655a2-8958-410e-80e2-3457051b8dff"), event_id=7, version=0)
class Microsoft_Windows_TSF_msutb_7_0(Etw):
    pattern = Struct(
        "flags_current" / Int32ul,
        "flags_new" / Int32ul
    )


@declare(guid=guid("74b655a2-8958-410e-80e2-3457051b8dff"), event_id=8, version=0)
class Microsoft_Windows_TSF_msutb_8_0(Etw):
    pattern = Struct(
        "flags_current" / Int32ul,
        "flags_new" / Int32ul
    )


@declare(guid=guid("74b655a2-8958-410e-80e2-3457051b8dff"), event_id=9, version=0)
class Microsoft_Windows_TSF_msutb_9_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("74b655a2-8958-410e-80e2-3457051b8dff"), event_id=10, version=0)
class Microsoft_Windows_TSF_msutb_10_0(Etw):
    pattern = Struct(
        "tid_current" / Int32ul,
        "tid_new" / Int32ul
    )


@declare(guid=guid("74b655a2-8958-410e-80e2-3457051b8dff"), event_id=11, version=0)
class Microsoft_Windows_TSF_msutb_11_0(Etw):
    pattern = Struct(
        "tid_current" / Int32ul,
        "tid_new" / Int32ul
    )


@declare(guid=guid("74b655a2-8958-410e-80e2-3457051b8dff"), event_id=12, version=0)
class Microsoft_Windows_TSF_msutb_12_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )

