# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Runtime-Networking
GUID : 6eb875eb-8f4a-4800-a00b-e484c97d7561
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=1, version=0)
class Microsoft_Windows_Runtime_Networking_1_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=2, version=0)
class Microsoft_Windows_Runtime_Networking_2_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul,
        "errorCode" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=3, version=0)
class Microsoft_Windows_Runtime_Networking_3_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=4, version=0)
class Microsoft_Windows_Runtime_Networking_4_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul,
        "errorCode" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=5, version=0)
class Microsoft_Windows_Runtime_Networking_5_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=6, version=0)
class Microsoft_Windows_Runtime_Networking_6_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=7, version=0)
class Microsoft_Windows_Runtime_Networking_7_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=8, version=0)
class Microsoft_Windows_Runtime_Networking_8_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "str2" / WString
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=9, version=0)
class Microsoft_Windows_Runtime_Networking_9_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "str2" / WString
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=10, version=0)
class Microsoft_Windows_Runtime_Networking_10_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "str2" / WString
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=11, version=0)
class Microsoft_Windows_Runtime_Networking_11_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=12, version=0)
class Microsoft_Windows_Runtime_Networking_12_0(Etw):
    pattern = Struct(
        "uri" / WString,
        "port" / Int32ul,
        "errorCode" / Int32ul,
        "errorMessage" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=13, version=0)
class Microsoft_Windows_Runtime_Networking_13_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "str2" / WString,
        "flags" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=14, version=0)
class Microsoft_Windows_Runtime_Networking_14_0(Etw):
    pattern = Struct(
        "uri" / WString,
        "port" / Int32ul,
        "errorCode" / Int32ul,
        "errorMessage" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=15, version=0)
class Microsoft_Windows_Runtime_Networking_15_0(Etw):
    pattern = Struct(
        "obj1" / Int64ul,
        "obj2" / Int64ul,
        "uri" / WString
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=16, version=0)
class Microsoft_Windows_Runtime_Networking_16_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "length" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=17, version=0)
class Microsoft_Windows_Runtime_Networking_17_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "length" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=18, version=0)
class Microsoft_Windows_Runtime_Networking_18_0(Etw):
    pattern = Struct(
        "obj" / Int64ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=19, version=0)
class Microsoft_Windows_Runtime_Networking_19_0(Etw):
    pattern = Struct(
        "obj" / Int64ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=20, version=0)
class Microsoft_Windows_Runtime_Networking_20_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "length" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=21, version=0)
class Microsoft_Windows_Runtime_Networking_21_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "errorCode" / Int32ul,
        "errorMessage" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=22, version=0)
class Microsoft_Windows_Runtime_Networking_22_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "statusDescription" / WString
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=23, version=0)
class Microsoft_Windows_Runtime_Networking_23_0(Etw):
    pattern = Struct(
        "obj" / Int64ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=24, version=0)
class Microsoft_Windows_Runtime_Networking_24_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "statusCode" / Int32ul,
        "statusDescription" / WString
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=25, version=0)
class Microsoft_Windows_Runtime_Networking_25_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "statusDescription" / WString
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=26, version=0)
class Microsoft_Windows_Runtime_Networking_26_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "errorCode" / Int32ul,
        "errorMessage" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=27, version=0)
class Microsoft_Windows_Runtime_Networking_27_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "length" / Int32ul,
        "limit" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=28, version=0)
class Microsoft_Windows_Runtime_Networking_28_0(Etw):
    pattern = Struct(
        "obj" / Int64ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=29, version=0)
class Microsoft_Windows_Runtime_Networking_29_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "statusDescription" / WString
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=30, version=0)
class Microsoft_Windows_Runtime_Networking_30_0(Etw):
    pattern = Struct(
        "obj" / Int64ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=31, version=0)
class Microsoft_Windows_Runtime_Networking_31_0(Etw):
    pattern = Struct(
        "statusDescription" / WString,
        "int1" / Int32ul,
        "int2" / Int32ul,
        "int3" / Int32ul,
        "int4" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=32, version=0)
class Microsoft_Windows_Runtime_Networking_32_0(Etw):
    pattern = Struct(
        "uri" / WString,
        "hresult" / Int32ul,
        "errorMessage" / Int32sl
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=33, version=0)
class Microsoft_Windows_Runtime_Networking_33_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul,
        "response" / WString,
        "errorCode" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=34, version=0)
class Microsoft_Windows_Runtime_Networking_34_0(Etw):
    pattern = Struct(
        "runtimeClass" / Int32ul,
        "api" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=35, version=0)
class Microsoft_Windows_Runtime_Networking_35_0(Etw):
    pattern = Struct(
        "runtimeClass" / Int32ul,
        "api" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=36, version=0)
class Microsoft_Windows_Runtime_Networking_36_0(Etw):
    pattern = Struct(
        "runtimeClass" / Int32ul,
        "api" / Int32ul,
        "hresult" / Int32ul,
        "errorMessage" / Int32sl
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=37, version=0)
class Microsoft_Windows_Runtime_Networking_37_0(Etw):
    pattern = Struct(
        "win32Api" / Int32ul,
        "error" / Int32ul,
        "errorMessage" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=38, version=0)
class Microsoft_Windows_Runtime_Networking_38_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "errorCode" / Int32ul,
        "errorMessage" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=39, version=0)
class Microsoft_Windows_Runtime_Networking_39_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "errorCode" / Int32ul,
        "errorMessage" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=40, version=0)
class Microsoft_Windows_Runtime_Networking_40_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "hresult" / Int32ul,
        "errorMessage" / Int32sl
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=41, version=0)
class Microsoft_Windows_Runtime_Networking_41_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "bytesRead" / Int32ul,
        "size" / Int32ul,
        "address" / Bytes(lambda this: this.size)
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=42, version=0)
class Microsoft_Windows_Runtime_Networking_42_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "handle" / Int64ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=43, version=0)
class Microsoft_Windows_Runtime_Networking_43_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "hresult" / Int32ul,
        "errorMessage" / Int32sl
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=44, version=0)
class Microsoft_Windows_Runtime_Networking_44_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "obj" / Int64ul,
        "length" / Int32ul,
        "handle" / Int64ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=45, version=0)
class Microsoft_Windows_Runtime_Networking_45_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "obj" / Int64ul,
        "read" / Int32ul,
        "length" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=46, version=0)
class Microsoft_Windows_Runtime_Networking_46_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "obj" / Int64ul,
        "length" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=47, version=0)
class Microsoft_Windows_Runtime_Networking_47_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "port1" / WString,
        "ip" / WString,
        "port2" / WString
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=48, version=0)
class Microsoft_Windows_Runtime_Networking_48_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "size" / Int32ul,
        "address" / Bytes(lambda this: this.size)
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=49, version=0)
class Microsoft_Windows_Runtime_Networking_49_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "size" / Int32ul,
        "address" / Bytes(lambda this: this.size)
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=50, version=0)
class Microsoft_Windows_Runtime_Networking_50_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "obj" / Int64ul,
        "length" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=51, version=0)
class Microsoft_Windows_Runtime_Networking_51_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "obj" / Int64ul,
        "length" / Int32ul,
        "handle" / Int64ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=52, version=0)
class Microsoft_Windows_Runtime_Networking_52_0(Etw):
    pattern = Struct(
        "obj" / Int64ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=53, version=0)
class Microsoft_Windows_Runtime_Networking_53_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "length" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=54, version=0)
class Microsoft_Windows_Runtime_Networking_54_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "hresult" / Int32ul,
        "errorMessage" / Int32sl
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=55, version=0)
class Microsoft_Windows_Runtime_Networking_55_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "hresult" / Int32ul,
        "errorMessage" / Int32sl
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=57, version=0)
class Microsoft_Windows_Runtime_Networking_57_0(Etw):
    pattern = Struct(
        "obj" / Int64ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=58, version=0)
class Microsoft_Windows_Runtime_Networking_58_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "statusCode" / Int32ul,
        "statusDescription" / WString
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=59, version=0)
class Microsoft_Windows_Runtime_Networking_59_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "hresult" / Int32ul,
        "errorMessage" / Int32sl
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=60, version=0)
class Microsoft_Windows_Runtime_Networking_60_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "obj" / Int64ul,
        "length" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=61, version=0)
class Microsoft_Windows_Runtime_Networking_61_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "obj" / Int64ul,
        "length" / Int32ul,
        "handle" / Int64ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=62, version=0)
class Microsoft_Windows_Runtime_Networking_62_0(Etw):
    pattern = Struct(
        "runtimeClass" / Int32ul,
        "pendingOperations" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=63, version=0)
class Microsoft_Windows_Runtime_Networking_63_0(Etw):
    pattern = Struct(
        "runtimeClass" / Int32ul,
        "pendingOperations" / Int32ul,
        "winsockPendingOperations" / Int32ul,
        "winsockDataAvailable" / Int8ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=64, version=0)
class Microsoft_Windows_Runtime_Networking_64_0(Etw):
    pattern = Struct(
        "runtimeClass" / Int32ul,
        "pendingOperations" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=65, version=0)
class Microsoft_Windows_Runtime_Networking_65_0(Etw):
    pattern = Struct(
        "runtimeClass" / Int32ul,
        "pendingOperations" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=66, version=0)
class Microsoft_Windows_Runtime_Networking_66_0(Etw):
    pattern = Struct(
        "connectorType" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=67, version=0)
class Microsoft_Windows_Runtime_Networking_67_0(Etw):
    pattern = Struct(
        "value" / WString,
        "resolutionResult" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=68, version=0)
class Microsoft_Windows_Runtime_Networking_68_0(Etw):
    pattern = Struct(
        "value" / WString,
        "errorCode" / Int32ul,
        "errorMessage" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=69, version=0)
class Microsoft_Windows_Runtime_Networking_69_0(Etw):
    pattern = Struct(
        "errorCount" / Int32ul,
        "errorList" / Int32ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=70, version=0)
class Microsoft_Windows_Runtime_Networking_70_0(Etw):
    pattern = Struct(
        "certificateThumbprint" / WString,
        "hasFatalError" / Int8ul,
        "errorCount" / Int32ul,
        "errorList" / Int32ul,
        "intermediateCertificatesCount" / Int32ul,
        "intermediateCertificatesList" / WString
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=71, version=0)
class Microsoft_Windows_Runtime_Networking_71_0(Etw):
    pattern = Struct(
        "obj" / Int64ul,
        "hresult" / Int32ul,
        "errorMessage" / Int32sl
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=72, version=0)
class Microsoft_Windows_Runtime_Networking_72_0(Etw):
    pattern = Struct(
        "obj" / Int64ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=73, version=0)
class Microsoft_Windows_Runtime_Networking_73_0(Etw):
    pattern = Struct(
        "functionName" / CString,
        "lineNumber" / Int32sl,
        "status" / Int32sl
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=74, version=0)
class Microsoft_Windows_Runtime_Networking_74_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=75, version=0)
class Microsoft_Windows_Runtime_Networking_75_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=76, version=0)
class Microsoft_Windows_Runtime_Networking_76_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul
    )


@declare(guid=guid("6eb875eb-8f4a-4800-a00b-e484c97d7561"), event_id=77, version=0)
class Microsoft_Windows_Runtime_Networking_77_0(Etw):
    pattern = Struct(
        "asyncOperation" / Int32ul,
        "asyncObject" / Int64ul
    )

