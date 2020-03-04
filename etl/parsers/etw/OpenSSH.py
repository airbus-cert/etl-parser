# -*- coding: utf-8 -*-
"""
OpenSSH
GUID : c4b57d35-0636-4bc3-a262-370f249f9802
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c4b57d35-0636-4bc3-a262-370f249f9802"), event_id=1, version=0)
class OpenSSH_1_0(Etw):
    pattern = Struct(
        "process" / WString,
        "payload" / WString
    )


@declare(guid=guid("c4b57d35-0636-4bc3-a262-370f249f9802"), event_id=2, version=0)
class OpenSSH_2_0(Etw):
    pattern = Struct(
        "process" / WString,
        "payload" / WString
    )


@declare(guid=guid("c4b57d35-0636-4bc3-a262-370f249f9802"), event_id=3, version=0)
class OpenSSH_3_0(Etw):
    pattern = Struct(
        "process" / WString,
        "payload" / WString
    )


@declare(guid=guid("c4b57d35-0636-4bc3-a262-370f249f9802"), event_id=4, version=0)
class OpenSSH_4_0(Etw):
    pattern = Struct(
        "process" / WString,
        "payload" / WString
    )


@declare(guid=guid("c4b57d35-0636-4bc3-a262-370f249f9802"), event_id=6, version=0)
class OpenSSH_6_0(Etw):
    pattern = Struct(
        "process" / WString,
        "payload" / WString
    )

