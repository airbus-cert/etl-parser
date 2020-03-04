# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Runtime-Web-Http
GUID : 41877cb4-11fc-4188-b590-712c143c881d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=1, version=0)
class Microsoft_Windows_Runtime_Web_Http_1_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=2, version=0)
class Microsoft_Windows_Runtime_Web_Http_2_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "str2" / WString
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=3, version=0)
class Microsoft_Windows_Runtime_Web_Http_3_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "str2" / WString
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=4, version=0)
class Microsoft_Windows_Runtime_Web_Http_4_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "str2" / WString
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=5, version=0)
class Microsoft_Windows_Runtime_Web_Http_5_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=6, version=0)
class Microsoft_Windows_Runtime_Web_Http_6_0(Etw):
    pattern = Struct(
        "uri" / WString,
        "port" / Int32ul,
        "errorCode" / Int32ul,
        "errorMessage" / Int32ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=7, version=0)
class Microsoft_Windows_Runtime_Web_Http_7_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "str2" / WString,
        "flags" / Int32ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=8, version=0)
class Microsoft_Windows_Runtime_Web_Http_8_0(Etw):
    pattern = Struct(
        "uri" / WString,
        "port" / Int32ul,
        "errorCode" / Int32ul,
        "errorMessage" / Int32ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=9, version=0)
class Microsoft_Windows_Runtime_Web_Http_9_0(Etw):
    pattern = Struct(
        "obj1" / Int64ul,
        "obj2" / Int64ul,
        "uri" / WString
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=10, version=0)
class Microsoft_Windows_Runtime_Web_Http_10_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "length" / Int32ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=11, version=0)
class Microsoft_Windows_Runtime_Web_Http_11_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "length" / Int32ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=12, version=0)
class Microsoft_Windows_Runtime_Web_Http_12_0(Etw):
    pattern = Struct(
        "obj" / Int64ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=13, version=0)
class Microsoft_Windows_Runtime_Web_Http_13_0(Etw):
    pattern = Struct(
        "obj" / Int64ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=14, version=0)
class Microsoft_Windows_Runtime_Web_Http_14_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "length" / Int32ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=15, version=0)
class Microsoft_Windows_Runtime_Web_Http_15_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "errorCode" / Int32ul,
        "errorMessage" / Int32ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=16, version=0)
class Microsoft_Windows_Runtime_Web_Http_16_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "statusDescription" / WString
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=17, version=0)
class Microsoft_Windows_Runtime_Web_Http_17_0(Etw):
    pattern = Struct(
        "obj" / Int64ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=18, version=0)
class Microsoft_Windows_Runtime_Web_Http_18_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "statusCode" / Int32ul,
        "statusDescription" / WString
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=19, version=0)
class Microsoft_Windows_Runtime_Web_Http_19_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "statusDescription" / WString
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=20, version=0)
class Microsoft_Windows_Runtime_Web_Http_20_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "errorCode" / Int32ul,
        "errorMessage" / Int32ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=21, version=0)
class Microsoft_Windows_Runtime_Web_Http_21_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "length" / Int32ul,
        "limit" / Int32ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=22, version=0)
class Microsoft_Windows_Runtime_Web_Http_22_0(Etw):
    pattern = Struct(
        "obj" / Int64ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=23, version=0)
class Microsoft_Windows_Runtime_Web_Http_23_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "statusDescription" / WString
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=24, version=0)
class Microsoft_Windows_Runtime_Web_Http_24_0(Etw):
    pattern = Struct(
        "obj" / Int64ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=25, version=0)
class Microsoft_Windows_Runtime_Web_Http_25_0(Etw):
    pattern = Struct(
        "statusDescription" / WString,
        "stage" / Int32ul,
        "retries" / Int32ul,
        "bytesSent" / Int64ul,
        "totalBytesToSend" / Int64ul,
        "bytesReceived" / Int64ul,
        "totalBytesToReceive" / Int64ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=26, version=0)
class Microsoft_Windows_Runtime_Web_Http_26_0(Etw):
    pattern = Struct(
        "uri" / WString,
        "hresult" / Int32ul,
        "errorMessage" / Int32sl
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=27, version=0)
class Microsoft_Windows_Runtime_Web_Http_27_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul,
        "response" / WString,
        "hresult" / Int32ul,
        "errorMessage" / Int32sl
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=28, version=0)
class Microsoft_Windows_Runtime_Web_Http_28_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=29, version=0)
class Microsoft_Windows_Runtime_Web_Http_29_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul,
        "hresult" / Int32ul,
        "errorMessage" / Int32sl
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=30, version=0)
class Microsoft_Windows_Runtime_Web_Http_30_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=31, version=0)
class Microsoft_Windows_Runtime_Web_Http_31_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul,
        "hresult" / Int32ul,
        "errorMessage" / Int32sl
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=32, version=0)
class Microsoft_Windows_Runtime_Web_Http_32_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=33, version=0)
class Microsoft_Windows_Runtime_Web_Http_33_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=34, version=0)
class Microsoft_Windows_Runtime_Web_Http_34_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=35, version=0)
class Microsoft_Windows_Runtime_Web_Http_35_0(Etw):
    pattern = Struct(
        "responseState" / Int32ul,
        "pendingReceiveOperations" / Int32sl
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=37, version=0)
class Microsoft_Windows_Runtime_Web_Http_37_0(Etw):
    pattern = Struct(
        "hresult" / Int32ul,
        "errorMessage" / Int32sl
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=39, version=0)
class Microsoft_Windows_Runtime_Web_Http_39_0(Etw):
    pattern = Struct(
        "hresult" / Int32ul,
        "errorMessage" / Int32sl
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=40, version=0)
class Microsoft_Windows_Runtime_Web_Http_40_0(Etw):
    pattern = Struct(
        "pendingOperations" / Int32ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=41, version=0)
class Microsoft_Windows_Runtime_Web_Http_41_0(Etw):
    pattern = Struct(
        "pendingOperations" / Int32ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=42, version=0)
class Microsoft_Windows_Runtime_Web_Http_42_0(Etw):
    pattern = Struct(
        "responseState" / Int32ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=43, version=0)
class Microsoft_Windows_Runtime_Web_Http_43_0(Etw):
    pattern = Struct(
        "obj" / Int64ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=44, version=0)
class Microsoft_Windows_Runtime_Web_Http_44_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=45, version=0)
class Microsoft_Windows_Runtime_Web_Http_45_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=46, version=0)
class Microsoft_Windows_Runtime_Web_Http_46_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul
    )


@declare(guid=guid("41877cb4-11fc-4188-b590-712c143c881d"), event_id=47, version=0)
class Microsoft_Windows_Runtime_Web_Http_47_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul
    )

