# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TabletPC-MathRecognizer
GUID : bdb462fc-a297-49a2-bf2e-4f1809e12abc
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("bdb462fc-a297-49a2-bf2e-4f1809e12abc"), event_id=3, version=0)
class Microsoft_Windows_TabletPC_MathRecognizer_3_0(Etw):
    pattern = Struct(
        "intvalue" / Int32ul
    )


@declare(guid=guid("bdb462fc-a297-49a2-bf2e-4f1809e12abc"), event_id=4, version=0)
class Microsoft_Windows_TabletPC_MathRecognizer_4_0(Etw):
    pattern = Struct(
        "intvalue" / Int32ul
    )


@declare(guid=guid("bdb462fc-a297-49a2-bf2e-4f1809e12abc"), event_id=5, version=0)
class Microsoft_Windows_TabletPC_MathRecognizer_5_0(Etw):
    pattern = Struct(
        "intvalue" / Int32ul
    )


@declare(guid=guid("bdb462fc-a297-49a2-bf2e-4f1809e12abc"), event_id=12, version=0)
class Microsoft_Windows_TabletPC_MathRecognizer_12_0(Etw):
    pattern = Struct(
        "intvalue" / Int32ul
    )


@declare(guid=guid("bdb462fc-a297-49a2-bf2e-4f1809e12abc"), event_id=17, version=0)
class Microsoft_Windows_TabletPC_MathRecognizer_17_0(Etw):
    pattern = Struct(
        "intvalue" / Int32ul
    )


@declare(guid=guid("bdb462fc-a297-49a2-bf2e-4f1809e12abc"), event_id=18, version=0)
class Microsoft_Windows_TabletPC_MathRecognizer_18_0(Etw):
    pattern = Struct(
        "intvalue" / Int32ul
    )

