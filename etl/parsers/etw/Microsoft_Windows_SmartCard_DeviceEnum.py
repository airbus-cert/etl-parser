# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SmartCard-DeviceEnum
GUID : aaeac398-3028-487c-9586-44eacad03637
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("aaeac398-3028-487c-9586-44eacad03637"), event_id=99, version=0)
class Microsoft_Windows_SmartCard_DeviceEnum_99_0(Etw):
    pattern = Struct(
        "InstancePath" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("aaeac398-3028-487c-9586-44eacad03637"), event_id=100, version=0)
class Microsoft_Windows_SmartCard_DeviceEnum_100_0(Etw):
    pattern = Struct(
        "InstancePath" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("aaeac398-3028-487c-9586-44eacad03637"), event_id=101, version=0)
class Microsoft_Windows_SmartCard_DeviceEnum_101_0(Etw):
    pattern = Struct(
        "InstancePath" / WString,
        "SessionId" / Int32ul
    )


@declare(guid=guid("aaeac398-3028-487c-9586-44eacad03637"), event_id=102, version=0)
class Microsoft_Windows_SmartCard_DeviceEnum_102_0(Etw):
    pattern = Struct(
        "InstancePath" / WString,
        "SessionId" / Int32ul
    )

