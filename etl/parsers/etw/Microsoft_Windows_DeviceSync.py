# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DeviceSync
GUID : 09ec9687-d7ad-40ca-9c5e-78a04a5ae993
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("09ec9687-d7ad-40ca-9c5e-78a04a5ae993"), event_id=1001, version=0)
class Microsoft_Windows_DeviceSync_1001_0(Etw):
    pattern = Struct(
        "Error_DUID" / Guid,
        "Error_Partnership" / Guid,
        "Error_Type" / Int8ul,
        "Error_HResult" / Int32sl,
        "Error_Time" / Int64ul,
        "nameLen" / Int32ul,
        "dataName" / Bytes(lambda this: this.nameLen),
        "descLen" / Int32ul,
        "dataDesc" / Bytes(lambda this: this.descLen),
        "detailLen" / Int32ul,
        "dataDetail" / Bytes(lambda this: this.detailLen),
        "Error_Link" / WString
    )


@declare(guid=guid("09ec9687-d7ad-40ca-9c5e-78a04a5ae993"), event_id=1002, version=0)
class Microsoft_Windows_DeviceSync_1002_0(Etw):
    pattern = Struct(
        "Event_DUID" / Guid,
        "Event_Partnership" / Guid,
        "Event_Code" / Int8ul,
        "Event_Time" / Int64ul
    )

