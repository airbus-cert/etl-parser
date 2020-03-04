# -*- coding: utf-8 -*-
"""
Microsoft-Windows-mobsync
GUID : b44aec44-38f4-4b59-8df3-10306abf19b2
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b44aec44-38f4-4b59-8df3-10306abf19b2"), event_id=60103, version=1)
class Microsoft_Windows_mobsync_60103_1(Etw):
    pattern = Struct(
        "LoopCount" / Int32ul
    )


@declare(guid=guid("b44aec44-38f4-4b59-8df3-10306abf19b2"), event_id=60104, version=1)
class Microsoft_Windows_mobsync_60104_1(Etw):
    pattern = Struct(
        "LoopCount" / Int32ul
    )


@declare(guid=guid("b44aec44-38f4-4b59-8df3-10306abf19b2"), event_id=60111, version=1)
class Microsoft_Windows_mobsync_60111_1(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("b44aec44-38f4-4b59-8df3-10306abf19b2"), event_id=60112, version=1)
class Microsoft_Windows_mobsync_60112_1(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("b44aec44-38f4-4b59-8df3-10306abf19b2"), event_id=60113, version=1)
class Microsoft_Windows_mobsync_60113_1(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("b44aec44-38f4-4b59-8df3-10306abf19b2"), event_id=60114, version=1)
class Microsoft_Windows_mobsync_60114_1(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("b44aec44-38f4-4b59-8df3-10306abf19b2"), event_id=60123, version=1)
class Microsoft_Windows_mobsync_60123_1(Etw):
    pattern = Struct(
        "LoopCount" / Int32ul
    )


@declare(guid=guid("b44aec44-38f4-4b59-8df3-10306abf19b2"), event_id=60124, version=1)
class Microsoft_Windows_mobsync_60124_1(Etw):
    pattern = Struct(
        "LoopCount" / Int32ul
    )

