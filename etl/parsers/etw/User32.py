# -*- coding: utf-8 -*-
"""
User32
GUID : b0aa8734-56f7-41cc-b2f4-de228e98b946
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b0aa8734-56f7-41cc-b2f4-de228e98b946"), event_id=1073, version=0)
class User32_1073_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("b0aa8734-56f7-41cc-b2f4-de228e98b946"), event_id=1074, version=0)
class User32_1074_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString
    )


@declare(guid=guid("b0aa8734-56f7-41cc-b2f4-de228e98b946"), event_id=1075, version=0)
class User32_1075_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("b0aa8734-56f7-41cc-b2f4-de228e98b946"), event_id=1076, version=0)
class User32_1076_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString
    )


@declare(guid=guid("b0aa8734-56f7-41cc-b2f4-de228e98b946"), event_id=1077, version=0)
class User32_1077_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )

