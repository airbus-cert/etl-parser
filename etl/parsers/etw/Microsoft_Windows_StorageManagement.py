# -*- coding: utf-8 -*-
"""
Microsoft-Windows-StorageManagement
GUID : 7e58e69a-e361-4f06-b880-ad2f4b64c944
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7e58e69a-e361-4f06-b880-ad2f4b64c944"), event_id=1, version=0)
class Microsoft_Windows_StorageManagement_1_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("7e58e69a-e361-4f06-b880-ad2f4b64c944"), event_id=2, version=0)
class Microsoft_Windows_StorageManagement_2_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "ErrorCode" / Int32ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("7e58e69a-e361-4f06-b880-ad2f4b64c944"), event_id=3, version=0)
class Microsoft_Windows_StorageManagement_3_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("7e58e69a-e361-4f06-b880-ad2f4b64c944"), event_id=4, version=0)
class Microsoft_Windows_StorageManagement_4_0(Etw):
    pattern = Struct(
        "ClassName" / WString,
        "MethodName" / WString,
        "ErrorCode" / Int32ul,
        "MessageString" / WString
    )


@declare(guid=guid("7e58e69a-e361-4f06-b880-ad2f4b64c944"), event_id=5, version=0)
class Microsoft_Windows_StorageManagement_5_0(Etw):
    pattern = Struct(
        "ClassName" / WString,
        "MethodName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("7e58e69a-e361-4f06-b880-ad2f4b64c944"), event_id=6, version=0)
class Microsoft_Windows_StorageManagement_6_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )

