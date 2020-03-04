# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Diagnosis-PerfHost
GUID : f27b948b-0a7c-4eb6-92ec-8a2c1b353ecd
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f27b948b-0a7c-4eb6-92ec-8a2c1b353ecd"), event_id=1, version=0)
class Microsoft_Windows_Diagnosis_PerfHost_1_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "Function" / CString
    )


@declare(guid=guid("f27b948b-0a7c-4eb6-92ec-8a2c1b353ecd"), event_id=2, version=0)
class Microsoft_Windows_Diagnosis_PerfHost_2_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ProviderName" / WString
    )


@declare(guid=guid("f27b948b-0a7c-4eb6-92ec-8a2c1b353ecd"), event_id=3, version=0)
class Microsoft_Windows_Diagnosis_PerfHost_3_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "Function" / CString
    )


@declare(guid=guid("f27b948b-0a7c-4eb6-92ec-8a2c1b353ecd"), event_id=4, version=0)
class Microsoft_Windows_Diagnosis_PerfHost_4_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "Function" / CString
    )


@declare(guid=guid("f27b948b-0a7c-4eb6-92ec-8a2c1b353ecd"), event_id=10, version=0)
class Microsoft_Windows_Diagnosis_PerfHost_10_0(Etw):
    pattern = Struct(
        "ReturnValue" / Int32ul,
        "Provider" / WString,
        "ProviderDll" / WString,
        "Function" / CString
    )


@declare(guid=guid("f27b948b-0a7c-4eb6-92ec-8a2c1b353ecd"), event_id=11, version=0)
class Microsoft_Windows_Diagnosis_PerfHost_11_0(Etw):
    pattern = Struct(
        "FirstArgument" / WString,
        "Provider" / WString,
        "ProviderDll" / WString,
        "Function" / CString
    )


@declare(guid=guid("f27b948b-0a7c-4eb6-92ec-8a2c1b353ecd"), event_id=12, version=0)
class Microsoft_Windows_Diagnosis_PerfHost_12_0(Etw):
    pattern = Struct(
        "Query" / WString,
        "Size" / Int32ul,
        "Provider" / WString,
        "ProviderDll" / WString,
        "Function" / CString
    )


@declare(guid=guid("f27b948b-0a7c-4eb6-92ec-8a2c1b353ecd"), event_id=13, version=0)
class Microsoft_Windows_Diagnosis_PerfHost_13_0(Etw):
    pattern = Struct(
        "Provider" / WString,
        "ProviderDll" / WString,
        "Function" / CString
    )

