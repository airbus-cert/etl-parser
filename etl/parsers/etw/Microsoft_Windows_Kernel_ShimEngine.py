# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-ShimEngine
GUID : 0bf2fb94-7b60-4b4d-9766-e82f658df540
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("0bf2fb94-7b60-4b4d-9766-e82f658df540"), event_id=1, version=1)
class Microsoft_Windows_Kernel_ShimEngine_1_1(Etw):
    pattern = Struct(
        "EventId" / Int32ul,
        "DebugMessage" / CString
    )


@declare(guid=guid("0bf2fb94-7b60-4b4d-9766-e82f658df540"), event_id=2, version=1)
class Microsoft_Windows_Kernel_ShimEngine_2_1(Etw):
    pattern = Struct(
        "EventId" / Int32ul,
        "DebugMessage" / CString
    )


@declare(guid=guid("0bf2fb94-7b60-4b4d-9766-e82f658df540"), event_id=3, version=1)
class Microsoft_Windows_Kernel_ShimEngine_3_1(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "ShimSource" / Int32ul,
        "ShimCount" / Int32ul,
        "AppliedGuids" / WString
    )


@declare(guid=guid("0bf2fb94-7b60-4b4d-9766-e82f658df540"), event_id=4, version=1)
class Microsoft_Windows_Kernel_ShimEngine_4_1(Etw):
    pattern = Struct(
        "DeviceName" / WString,
        "DeviceClass" / WString,
        "FlagSource" / Int32ul,
        "Flags" / Int64ul
    )


@declare(guid=guid("0bf2fb94-7b60-4b4d-9766-e82f658df540"), event_id=5, version=1)
class Microsoft_Windows_Kernel_ShimEngine_5_1(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "DriverBase" / Int64ul,
        "DriverSize" / Int32ul,
        "DriverTimeStamp" / Int32ul,
        "DriverCheckSum" / Int32ul
    )


@declare(guid=guid("0bf2fb94-7b60-4b4d-9766-e82f658df540"), event_id=6, version=1)
class Microsoft_Windows_Kernel_ShimEngine_6_1(Etw):
    pattern = Struct(
        "DriverObject" / Int64ul,
        "DriverBase" / Int64ul
    )


@declare(guid=guid("0bf2fb94-7b60-4b4d-9766-e82f658df540"), event_id=10, version=1)
class Microsoft_Windows_Kernel_ShimEngine_10_1(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "DriverBase" / Int64ul,
        "DriverSize" / Int32ul,
        "DriverTimeStamp" / Int32ul,
        "DriverCheckSum" / Int32ul
    )


@declare(guid=guid("0bf2fb94-7b60-4b4d-9766-e82f658df540"), event_id=11, version=1)
class Microsoft_Windows_Kernel_ShimEngine_11_1(Etw):
    pattern = Struct(
        "DriverObject" / Int64ul,
        "DriverBase" / Int64ul
    )


@declare(guid=guid("0bf2fb94-7b60-4b4d-9766-e82f658df540"), event_id=12, version=1)
class Microsoft_Windows_Kernel_ShimEngine_12_1(Etw):
    pattern = Struct(
        "DriverBase" / Int64ul,
        "DriverSize" / Int32ul,
        "DriverObject" / Int64ul,
        "Pdo" / Int64ul,
        "Status" / Int32ul,
        "ServiceName" / WString,
        "HardwareId" / WString
    )


@declare(guid=guid("0bf2fb94-7b60-4b4d-9766-e82f658df540"), event_id=13, version=1)
class Microsoft_Windows_Kernel_ShimEngine_13_1(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "Caller" / Int64ul,
        "Type" / Int32ul,
        "Size" / Int64ul,
        "Tag" / Int32ul
    )


@declare(guid=guid("0bf2fb94-7b60-4b4d-9766-e82f658df540"), event_id=14, version=1)
class Microsoft_Windows_Kernel_ShimEngine_14_1(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "Caller" / Int64ul,
        "Tag" / Int32ul
    )


@declare(guid=guid("0bf2fb94-7b60-4b4d-9766-e82f658df540"), event_id=15, version=1)
class Microsoft_Windows_Kernel_ShimEngine_15_1(Etw):
    pattern = Struct(
        "DriverObject" / Int64ul,
        "Fdo" / Int64ul,
        "Irp" / Int64ul
    )


@declare(guid=guid("0bf2fb94-7b60-4b4d-9766-e82f658df540"), event_id=16, version=1)
class Microsoft_Windows_Kernel_ShimEngine_16_1(Etw):
    pattern = Struct(
        "DriverObject" / Int64ul,
        "Fdo" / Int64ul,
        "DeviceType" / Int32ul,
        "DeviceCharacteristics" / Int32ul,
        "Exclusive" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("0bf2fb94-7b60-4b4d-9766-e82f658df540"), event_id=17, version=1)
class Microsoft_Windows_Kernel_ShimEngine_17_1(Etw):
    pattern = Struct(
        "DriverObject" / Int64ul,
        "Fdo" / Int64ul,
        "Irp" / Int64ul,
        "MajorCode" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("0bf2fb94-7b60-4b4d-9766-e82f658df540"), event_id=18, version=1)
class Microsoft_Windows_Kernel_ShimEngine_18_1(Etw):
    pattern = Struct(
        "DriverObject" / Int64ul,
        "Fdo" / Int64ul,
        "Irp" / Int64ul,
        "MinorCode" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("0bf2fb94-7b60-4b4d-9766-e82f658df540"), event_id=19, version=1)
class Microsoft_Windows_Kernel_ShimEngine_19_1(Etw):
    pattern = Struct(
        "DriverObject" / Int64ul,
        "Fdo" / Int64ul,
        "Irp" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("0bf2fb94-7b60-4b4d-9766-e82f658df540"), event_id=20, version=1)
class Microsoft_Windows_Kernel_ShimEngine_20_1(Etw):
    pattern = Struct(
        "DriverObject" / Int64ul,
        "Fdo" / Int64ul,
        "Irp" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("0bf2fb94-7b60-4b4d-9766-e82f658df540"), event_id=21, version=1)
class Microsoft_Windows_Kernel_ShimEngine_21_1(Etw):
    pattern = Struct(
        "DriverObject" / Int64ul,
        "Fdo" / Int64ul,
        "Irp" / Int64ul,
        "MinorCode" / Int32ul,
        "PowerType" / Int32ul,
        "PowerState" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("0bf2fb94-7b60-4b4d-9766-e82f658df540"), event_id=22, version=1)
class Microsoft_Windows_Kernel_ShimEngine_22_1(Etw):
    pattern = Struct(
        "DriverObject" / Int64ul,
        "Fdo" / Int64ul,
        "Irp" / Int64ul,
        "MinorCode" / Int32ul,
        "PowerType" / Int32ul,
        "PowerState" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("0bf2fb94-7b60-4b4d-9766-e82f658df540"), event_id=23, version=1)
class Microsoft_Windows_Kernel_ShimEngine_23_1(Etw):
    pattern = Struct(
        "DriverObject" / Int64ul,
        "Fdo" / Int64ul,
        "Irp" / Int64ul,
        "MinorCode" / Int32ul,
        "PowerState" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("0bf2fb94-7b60-4b4d-9766-e82f658df540"), event_id=24, version=1)
class Microsoft_Windows_Kernel_ShimEngine_24_1(Etw):
    pattern = Struct(
        "DriverObject" / Int64ul,
        "Fdo" / Int64ul,
        "Irp" / Int64ul,
        "Status" / Int32ul
    )

