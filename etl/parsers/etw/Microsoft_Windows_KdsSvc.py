# -*- coding: utf-8 -*-
"""
Microsoft-Windows-KdsSvc
GUID : 89203471-d554-47d4-bde4-7552ec219999
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("89203471-d554-47d4-bde4-7552ec219999"), event_id=4001, version=0)
class Microsoft_Windows_KdsSvc_4001_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("89203471-d554-47d4-bde4-7552ec219999"), event_id=4004, version=0)
class Microsoft_Windows_KdsSvc_4004_0(Etw):
    pattern = Struct(
        "MRKID" / WString
    )


@declare(guid=guid("89203471-d554-47d4-bde4-7552ec219999"), event_id=4005, version=0)
class Microsoft_Windows_KdsSvc_4005_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("89203471-d554-47d4-bde4-7552ec219999"), event_id=4006, version=0)
class Microsoft_Windows_KdsSvc_4006_0(Etw):
    pattern = Struct(
        "MRKIDGUID" / Guid,
        "AttrName" / WString
    )


@declare(guid=guid("89203471-d554-47d4-bde4-7552ec219999"), event_id=4007, version=0)
class Microsoft_Windows_KdsSvc_4007_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("89203471-d554-47d4-bde4-7552ec219999"), event_id=4008, version=0)
class Microsoft_Windows_KdsSvc_4008_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("89203471-d554-47d4-bde4-7552ec219999"), event_id=4009, version=0)
class Microsoft_Windows_KdsSvc_4009_0(Etw):
    pattern = Struct(
        "MRKID" / Guid,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("89203471-d554-47d4-bde4-7552ec219999"), event_id=4010, version=0)
class Microsoft_Windows_KdsSvc_4010_0(Etw):
    pattern = Struct(
        "AttrName" / WString
    )

