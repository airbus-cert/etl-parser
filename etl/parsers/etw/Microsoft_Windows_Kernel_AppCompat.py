# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-AppCompat
GUID : 16a1adc1-9b7f-4cd9-94b3-d8296ab1b130
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("16a1adc1-9b7f-4cd9-94b3-d8296ab1b130"), event_id=1, version=0)
class Microsoft_Windows_Kernel_AppCompat_1_0(Etw):
    pattern = Struct(
        "ExecutablePathLength" / Int16ul,
        "ExecutablePath" / Bytes(lambda this: this.ExecutablePathLength),
        "RegistryPathLength" / Int16ul,
        "RegistryPath" / Bytes(lambda this: this.RegistryPathLength)
    )


@declare(guid=guid("16a1adc1-9b7f-4cd9-94b3-d8296ab1b130"), event_id=3, version=0)
class Microsoft_Windows_Kernel_AppCompat_3_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("16a1adc1-9b7f-4cd9-94b3-d8296ab1b130"), event_id=5, version=0)
class Microsoft_Windows_Kernel_AppCompat_5_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("16a1adc1-9b7f-4cd9-94b3-d8296ab1b130"), event_id=7, version=0)
class Microsoft_Windows_Kernel_AppCompat_7_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("16a1adc1-9b7f-4cd9-94b3-d8296ab1b130"), event_id=9, version=0)
class Microsoft_Windows_Kernel_AppCompat_9_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("16a1adc1-9b7f-4cd9-94b3-d8296ab1b130"), event_id=11, version=0)
class Microsoft_Windows_Kernel_AppCompat_11_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("16a1adc1-9b7f-4cd9-94b3-d8296ab1b130"), event_id=13, version=0)
class Microsoft_Windows_Kernel_AppCompat_13_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("16a1adc1-9b7f-4cd9-94b3-d8296ab1b130"), event_id=15, version=0)
class Microsoft_Windows_Kernel_AppCompat_15_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("16a1adc1-9b7f-4cd9-94b3-d8296ab1b130"), event_id=17, version=0)
class Microsoft_Windows_Kernel_AppCompat_17_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )

