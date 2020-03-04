# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MSFTEDIT
GUID : 9640427c-7d03-4331-b8ee-fb77625bf381
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9640427c-7d03-4331-b8ee-fb77625bf381"), event_id=1, version=0)
class Microsoft_Windows_MSFTEDIT_1_0(Etw):
    pattern = Struct(
        "param1" / Int32ul,
        "param2" / Int32ul
    )


@declare(guid=guid("9640427c-7d03-4331-b8ee-fb77625bf381"), event_id=2, version=0)
class Microsoft_Windows_MSFTEDIT_2_0(Etw):
    pattern = Struct(
        "param1" / Int32ul,
        "param2" / Int32ul
    )


@declare(guid=guid("9640427c-7d03-4331-b8ee-fb77625bf381"), event_id=6, version=0)
class Microsoft_Windows_MSFTEDIT_6_0(Etw):
    pattern = Struct(
        "param1" / Int32ul,
        "param2" / Int32ul,
        "param3" / Int32ul
    )


@declare(guid=guid("9640427c-7d03-4331-b8ee-fb77625bf381"), event_id=7, version=0)
class Microsoft_Windows_MSFTEDIT_7_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("9640427c-7d03-4331-b8ee-fb77625bf381"), event_id=8, version=0)
class Microsoft_Windows_MSFTEDIT_8_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("9640427c-7d03-4331-b8ee-fb77625bf381"), event_id=9, version=0)
class Microsoft_Windows_MSFTEDIT_9_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("9640427c-7d03-4331-b8ee-fb77625bf381"), event_id=12, version=0)
class Microsoft_Windows_MSFTEDIT_12_0(Etw):
    pattern = Struct(
        "param1" / Int32ul,
        "param2" / Int32ul
    )


@declare(guid=guid("9640427c-7d03-4331-b8ee-fb77625bf381"), event_id=13, version=0)
class Microsoft_Windows_MSFTEDIT_13_0(Etw):
    pattern = Struct(
        "param1" / Int32ul,
        "param2" / Int32ul
    )

