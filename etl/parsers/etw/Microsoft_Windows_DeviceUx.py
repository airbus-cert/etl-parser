# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DeviceUx
GUID : ded165cf-485d-4770-a3e7-9c5f0320e80c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ded165cf-485d-4770-a3e7-9c5f0320e80c"), event_id=51, version=0)
class Microsoft_Windows_DeviceUx_51_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "Integer2" / Int32ul
    )


@declare(guid=guid("ded165cf-485d-4770-a3e7-9c5f0320e80c"), event_id=55, version=0)
class Microsoft_Windows_DeviceUx_55_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "Integer2" / Int32ul
    )


@declare(guid=guid("ded165cf-485d-4770-a3e7-9c5f0320e80c"), event_id=80, version=0)
class Microsoft_Windows_DeviceUx_80_0(Etw):
    pattern = Struct(
        "querycookie" / Int64ul,
        "EnumerationTime" / Int32ul,
        "CountOfItems" / Int32ul
    )


@declare(guid=guid("ded165cf-485d-4770-a3e7-9c5f0320e80c"), event_id=81, version=0)
class Microsoft_Windows_DeviceUx_81_0(Etw):
    pattern = Struct(
        "querycookie" / Int64ul,
        "EnumerationTime" / Int32ul,
        "CountOfItems" / Int32ul
    )


@declare(guid=guid("ded165cf-485d-4770-a3e7-9c5f0320e80c"), event_id=82, version=0)
class Microsoft_Windows_DeviceUx_82_0(Etw):
    pattern = Struct(
        "querycookie" / Int64ul
    )


@declare(guid=guid("ded165cf-485d-4770-a3e7-9c5f0320e80c"), event_id=83, version=0)
class Microsoft_Windows_DeviceUx_83_0(Etw):
    pattern = Struct(
        "querycookie" / Int64ul
    )


@declare(guid=guid("ded165cf-485d-4770-a3e7-9c5f0320e80c"), event_id=1001, version=0)
class Microsoft_Windows_DeviceUx_1001_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )

