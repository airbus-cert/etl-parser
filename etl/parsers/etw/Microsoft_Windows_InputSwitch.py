# -*- coding: utf-8 -*-
"""
Microsoft-Windows-InputSwitch
GUID : bb8e7234-bbf4-48a7-8741-339206ed1dfb
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("bb8e7234-bbf4-48a7-8741-339206ed1dfb"), event_id=2, version=0)
class Microsoft_Windows_InputSwitch_2_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("bb8e7234-bbf4-48a7-8741-339206ed1dfb"), event_id=4, version=0)
class Microsoft_Windows_InputSwitch_4_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("bb8e7234-bbf4-48a7-8741-339206ed1dfb"), event_id=6, version=0)
class Microsoft_Windows_InputSwitch_6_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("bb8e7234-bbf4-48a7-8741-339206ed1dfb"), event_id=8, version=0)
class Microsoft_Windows_InputSwitch_8_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("bb8e7234-bbf4-48a7-8741-339206ed1dfb"), event_id=10, version=0)
class Microsoft_Windows_InputSwitch_10_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("bb8e7234-bbf4-48a7-8741-339206ed1dfb"), event_id=12, version=0)
class Microsoft_Windows_InputSwitch_12_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("bb8e7234-bbf4-48a7-8741-339206ed1dfb"), event_id=13, version=0)
class Microsoft_Windows_InputSwitch_13_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )

