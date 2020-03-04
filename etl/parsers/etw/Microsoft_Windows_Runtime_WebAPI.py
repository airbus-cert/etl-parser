# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Runtime-WebAPI
GUID : 6bd96334-dc49-441a-b9c4-41425ba628d8
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=1, version=0)
class Microsoft_Windows_Runtime_WebAPI_1_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=2, version=0)
class Microsoft_Windows_Runtime_WebAPI_2_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul,
        "errorCode" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=3, version=0)
class Microsoft_Windows_Runtime_WebAPI_3_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=4, version=0)
class Microsoft_Windows_Runtime_WebAPI_4_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul,
        "errorCode" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=5, version=0)
class Microsoft_Windows_Runtime_WebAPI_5_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=6, version=0)
class Microsoft_Windows_Runtime_WebAPI_6_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=7, version=0)
class Microsoft_Windows_Runtime_WebAPI_7_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul,
        "callback" / Int64ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=8, version=0)
class Microsoft_Windows_Runtime_WebAPI_8_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul,
        "callback" / Int64ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=9, version=0)
class Microsoft_Windows_Runtime_WebAPI_9_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul,
        "errorCode" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=10, version=0)
class Microsoft_Windows_Runtime_WebAPI_10_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul,
        "errorCode" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=11, version=0)
class Microsoft_Windows_Runtime_WebAPI_11_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul,
        "errorCode" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=12, version=0)
class Microsoft_Windows_Runtime_WebAPI_12_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=13, version=0)
class Microsoft_Windows_Runtime_WebAPI_13_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "str2" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=14, version=0)
class Microsoft_Windows_Runtime_WebAPI_14_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "str2" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=15, version=0)
class Microsoft_Windows_Runtime_WebAPI_15_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "str2" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=16, version=0)
class Microsoft_Windows_Runtime_WebAPI_16_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=17, version=0)
class Microsoft_Windows_Runtime_WebAPI_17_0(Etw):
    pattern = Struct(
        "uri" / WString,
        "port" / Int32ul,
        "errorCode" / Int32ul,
        "errorMessage" / Int32ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=18, version=0)
class Microsoft_Windows_Runtime_WebAPI_18_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "str2" / WString,
        "flags" / Int32ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=19, version=0)
class Microsoft_Windows_Runtime_WebAPI_19_0(Etw):
    pattern = Struct(
        "uri" / WString,
        "port" / Int32ul,
        "errorCode" / Int32ul,
        "errorMessage" / Int32ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=20, version=0)
class Microsoft_Windows_Runtime_WebAPI_20_0(Etw):
    pattern = Struct(
        "obj1" / Int64ul,
        "obj2" / Int64ul,
        "uri" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=21, version=0)
class Microsoft_Windows_Runtime_WebAPI_21_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "length" / Int32ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=22, version=0)
class Microsoft_Windows_Runtime_WebAPI_22_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "length" / Int32ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=23, version=0)
class Microsoft_Windows_Runtime_WebAPI_23_0(Etw):
    pattern = Struct(
        "obj" / Int64ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=24, version=0)
class Microsoft_Windows_Runtime_WebAPI_24_0(Etw):
    pattern = Struct(
        "obj" / Int64ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=25, version=0)
class Microsoft_Windows_Runtime_WebAPI_25_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "length" / Int32ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=26, version=0)
class Microsoft_Windows_Runtime_WebAPI_26_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "errorCode" / Int32ul,
        "errorMessage" / Int32ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=27, version=0)
class Microsoft_Windows_Runtime_WebAPI_27_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "statusDescription" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=28, version=0)
class Microsoft_Windows_Runtime_WebAPI_28_0(Etw):
    pattern = Struct(
        "obj" / Int64ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=29, version=0)
class Microsoft_Windows_Runtime_WebAPI_29_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "statusCode" / Int32ul,
        "statusDescription" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=30, version=0)
class Microsoft_Windows_Runtime_WebAPI_30_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "statusDescription" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=31, version=0)
class Microsoft_Windows_Runtime_WebAPI_31_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "errorCode" / Int32ul,
        "errorMessage" / Int32ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=32, version=0)
class Microsoft_Windows_Runtime_WebAPI_32_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "length" / Int32ul,
        "limit" / Int32ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=33, version=0)
class Microsoft_Windows_Runtime_WebAPI_33_0(Etw):
    pattern = Struct(
        "obj" / Int64ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=34, version=0)
class Microsoft_Windows_Runtime_WebAPI_34_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "statusDescription" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=35, version=0)
class Microsoft_Windows_Runtime_WebAPI_35_0(Etw):
    pattern = Struct(
        "obj" / Int64ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=36, version=0)
class Microsoft_Windows_Runtime_WebAPI_36_0(Etw):
    pattern = Struct(
        "statusDescription" / WString,
        "int1" / Int32ul,
        "int2" / Int32ul,
        "int3" / Int32ul,
        "int4" / Int32ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=37, version=0)
class Microsoft_Windows_Runtime_WebAPI_37_0(Etw):
    pattern = Struct(
        "uri" / WString,
        "hresult" / Int32ul,
        "errorMessage" / Int32sl
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=38, version=0)
class Microsoft_Windows_Runtime_WebAPI_38_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul,
        "response" / WString,
        "errorCode" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=39, version=0)
class Microsoft_Windows_Runtime_WebAPI_39_0(Etw):
    pattern = Struct(
        "runtimeClass" / Int32ul,
        "api" / Int32ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=40, version=0)
class Microsoft_Windows_Runtime_WebAPI_40_0(Etw):
    pattern = Struct(
        "runtimeClass" / Int32ul,
        "api" / Int32ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=41, version=0)
class Microsoft_Windows_Runtime_WebAPI_41_0(Etw):
    pattern = Struct(
        "runtimeClass" / Int32ul,
        "api" / Int32ul,
        "hresult" / Int32ul,
        "errorMessage" / Int32sl
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=42, version=0)
class Microsoft_Windows_Runtime_WebAPI_42_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=43, version=0)
class Microsoft_Windows_Runtime_WebAPI_43_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=44, version=0)
class Microsoft_Windows_Runtime_WebAPI_44_0(Etw):
    pattern = Struct(
        "uri" / WString,
        "hresult" / Int32ul,
        "errorMessage" / Int32sl
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=45, version=0)
class Microsoft_Windows_Runtime_WebAPI_45_0(Etw):
    pattern = Struct(
        "uri" / WString,
        "statusCode" / Int32ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=46, version=0)
class Microsoft_Windows_Runtime_WebAPI_46_0(Etw):
    pattern = Struct(
        "uri" / WString,
        "hresult" / Int32ul,
        "errorMessage" / Int32sl
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=47, version=0)
class Microsoft_Windows_Runtime_WebAPI_47_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=48, version=0)
class Microsoft_Windows_Runtime_WebAPI_48_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "str2" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=49, version=0)
class Microsoft_Windows_Runtime_WebAPI_49_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=50, version=0)
class Microsoft_Windows_Runtime_WebAPI_50_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=51, version=0)
class Microsoft_Windows_Runtime_WebAPI_51_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "str2" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=53, version=0)
class Microsoft_Windows_Runtime_WebAPI_53_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=55, version=0)
class Microsoft_Windows_Runtime_WebAPI_55_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=56, version=0)
class Microsoft_Windows_Runtime_WebAPI_56_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=57, version=0)
class Microsoft_Windows_Runtime_WebAPI_57_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=58, version=0)
class Microsoft_Windows_Runtime_WebAPI_58_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=59, version=0)
class Microsoft_Windows_Runtime_WebAPI_59_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "str2" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=60, version=0)
class Microsoft_Windows_Runtime_WebAPI_60_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "str2" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=61, version=0)
class Microsoft_Windows_Runtime_WebAPI_61_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "str2" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=62, version=0)
class Microsoft_Windows_Runtime_WebAPI_62_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=63, version=0)
class Microsoft_Windows_Runtime_WebAPI_63_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=64, version=0)
class Microsoft_Windows_Runtime_WebAPI_64_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=65, version=0)
class Microsoft_Windows_Runtime_WebAPI_65_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=66, version=0)
class Microsoft_Windows_Runtime_WebAPI_66_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "str2" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=67, version=0)
class Microsoft_Windows_Runtime_WebAPI_67_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "str2" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=68, version=0)
class Microsoft_Windows_Runtime_WebAPI_68_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "str2" / WString
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=69, version=0)
class Microsoft_Windows_Runtime_WebAPI_69_0(Etw):
    pattern = Struct(
        "uri" / WString,
        "statusCode" / Int32ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=70, version=0)
class Microsoft_Windows_Runtime_WebAPI_70_0(Etw):
    pattern = Struct(
        "obj" / Int32ul
    )


@declare(guid=guid("6bd96334-dc49-441a-b9c4-41425ba628d8"), event_id=71, version=0)
class Microsoft_Windows_Runtime_WebAPI_71_0(Etw):
    pattern = Struct(
        "obj" / Int64ul
    )

