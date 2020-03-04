# -*- coding: utf-8 -*-
"""
Microsoft-Windows-RPCSS
GUID : d8975f88-7ddb-4ed0-91bf-3adf48c48e0c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d8975f88-7ddb-4ed0-91bf-3adf48c48e0c"), event_id=1, version=1)
class Microsoft_Windows_RPCSS_1_1(Etw):
    pattern = Struct(
        "DetectionLocation" / Int16ul,
        "Status" / Int32ul,
        "AdditionalData1" / Int32ul,
        "AdditionalData2" / Int32ul
    )


@declare(guid=guid("d8975f88-7ddb-4ed0-91bf-3adf48c48e0c"), event_id=2, version=1)
class Microsoft_Windows_RPCSS_2_1(Etw):
    pattern = Struct(
        "InterfaceUUID" / Guid,
        "ObjectUUID" / Guid,
        "Protocol" / CString,
        "EndPoint" / CString
    )


@declare(guid=guid("d8975f88-7ddb-4ed0-91bf-3adf48c48e0c"), event_id=3, version=1)
class Microsoft_Windows_RPCSS_3_1(Etw):
    pattern = Struct(
        "InterfaceUUID" / Guid,
        "ObjectUUID" / Guid,
        "Protocol" / CString,
        "EndPoint" / CString
    )

