# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WPD-API
GUID : 31569dcf-9c6f-4b8e-843a-b7c1cc7ffcba
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("31569dcf-9c6f-4b8e-843a-b7c1cc7ffcba"), event_id=100, version=0)
class Microsoft_Windows_WPD_API_100_0(Etw):
    pattern = Struct(
        "WpdAPICommandCategoryGUID" / Guid,
        "WpdAPICommandID" / Int32ul,
        "WpdSerializedData_Length" / Int32ul,
        "WpdSerializedData_Buffer" / Bytes(lambda this: this.WpdSerializedData_Length)
    )


@declare(guid=guid("31569dcf-9c6f-4b8e-843a-b7c1cc7ffcba"), event_id=101, version=0)
class Microsoft_Windows_WPD_API_101_0(Etw):
    pattern = Struct(
        "WpdAPICommandCategoryGUID" / Guid,
        "WpdAPICommandID" / Int32ul,
        "WPDAPIOPerationHR" / Int32ul,
        "WpdSerializedData_Length" / Int32ul,
        "WpdSerializedData_Buffer" / Bytes(lambda this: this.WpdSerializedData_Length)
    )

