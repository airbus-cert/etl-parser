# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Diagnosis-PCW
GUID : aabf8b86-7936-4fa2-acb0-63127f879dbf
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("aabf8b86-7936-4fa2-acb0-63127f879dbf"), event_id=1, version=0)
class Microsoft_Windows_Diagnosis_PCW_1_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ProviderGuid" / Guid
    )


@declare(guid=guid("aabf8b86-7936-4fa2-acb0-63127f879dbf"), event_id=2, version=0)
class Microsoft_Windows_Diagnosis_PCW_2_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ProviderGuid" / Guid,
        "CounterSetGuid" / Guid
    )


@declare(guid=guid("aabf8b86-7936-4fa2-acb0-63127f879dbf"), event_id=3, version=0)
class Microsoft_Windows_Diagnosis_PCW_3_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "CounterSetGuid" / Guid,
        "InstanceName" / WString,
        "InstanceId" / Int32ul
    )


@declare(guid=guid("aabf8b86-7936-4fa2-acb0-63127f879dbf"), event_id=4, version=0)
class Microsoft_Windows_Diagnosis_PCW_4_0(Etw):
    pattern = Struct(
        "ProviderGuid" / Guid,
        "CallbackReason" / Int32ul,
        "MachineName" / WString,
        "MachineNameSize" / Int32ul
    )


@declare(guid=guid("aabf8b86-7936-4fa2-acb0-63127f879dbf"), event_id=5, version=0)
class Microsoft_Windows_Diagnosis_PCW_5_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("aabf8b86-7936-4fa2-acb0-63127f879dbf"), event_id=6, version=0)
class Microsoft_Windows_Diagnosis_PCW_6_0(Etw):
    pattern = Struct(
        "ProviderGuid" / Guid,
        "Size" / Int32ul
    )


@declare(guid=guid("aabf8b86-7936-4fa2-acb0-63127f879dbf"), event_id=7, version=0)
class Microsoft_Windows_Diagnosis_PCW_7_0(Etw):
    pattern = Struct(
        "ProviderGuid" / Guid,
        "RequestCode" / Int32ul
    )


@declare(guid=guid("aabf8b86-7936-4fa2-acb0-63127f879dbf"), event_id=8, version=0)
class Microsoft_Windows_Diagnosis_PCW_8_0(Etw):
    pattern = Struct(
        "ProviderGuid" / Guid,
        "Status" / Int32ul,
        "Size" / Int32ul
    )


@declare(guid=guid("aabf8b86-7936-4fa2-acb0-63127f879dbf"), event_id=9, version=0)
class Microsoft_Windows_Diagnosis_PCW_9_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("aabf8b86-7936-4fa2-acb0-63127f879dbf"), event_id=13, version=0)
class Microsoft_Windows_Diagnosis_PCW_13_0(Etw):
    pattern = Struct(
        "ProviderGuid" / Guid,
        "Id" / Int64ul
    )


@declare(guid=guid("aabf8b86-7936-4fa2-acb0-63127f879dbf"), event_id=16, version=0)
class Microsoft_Windows_Diagnosis_PCW_16_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "CounterSetGuid" / Guid,
        "InstanceName" / WString,
        "InstanceId" / Int32ul,
        "CounterId" / Int32ul
    )


@declare(guid=guid("aabf8b86-7936-4fa2-acb0-63127f879dbf"), event_id=17, version=0)
class Microsoft_Windows_Diagnosis_PCW_17_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ProviderGuid" / Guid
    )


@declare(guid=guid("aabf8b86-7936-4fa2-acb0-63127f879dbf"), event_id=18, version=0)
class Microsoft_Windows_Diagnosis_PCW_18_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "CounterSetGuid" / Guid,
        "InstanceName" / WString,
        "InstanceId" / Int32ul
    )


@declare(guid=guid("aabf8b86-7936-4fa2-acb0-63127f879dbf"), event_id=19, version=0)
class Microsoft_Windows_Diagnosis_PCW_19_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "CounterSetGuid" / Guid,
        "InstanceName" / WString,
        "InstanceId" / Int32ul
    )


@declare(guid=guid("aabf8b86-7936-4fa2-acb0-63127f879dbf"), event_id=20, version=0)
class Microsoft_Windows_Diagnosis_PCW_20_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Phase" / Int32ul
    )


@declare(guid=guid("aabf8b86-7936-4fa2-acb0-63127f879dbf"), event_id=21, version=0)
class Microsoft_Windows_Diagnosis_PCW_21_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "CounterSetNameLength" / Int16ul,
        "CounterSetName" / Bytes(lambda this: this.CounterSetNameLength)
    )


@declare(guid=guid("aabf8b86-7936-4fa2-acb0-63127f879dbf"), event_id=22, version=0)
class Microsoft_Windows_Diagnosis_PCW_22_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "CounterSetNameLength" / Int16ul,
        "CounterSetName" / Bytes(lambda this: this.CounterSetNameLength),
        "InstanceNameLength" / Int16ul,
        "InstanceName" / Bytes(lambda this: this.InstanceNameLength)
    )


@declare(guid=guid("aabf8b86-7936-4fa2-acb0-63127f879dbf"), event_id=23, version=0)
class Microsoft_Windows_Diagnosis_PCW_23_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "CounterSetNameLength" / Int16ul,
        "CounterSetName" / Bytes(lambda this: this.CounterSetNameLength),
        "InstanceNameLength" / Int16ul,
        "InstanceName" / Bytes(lambda this: this.InstanceNameLength)
    )


@declare(guid=guid("aabf8b86-7936-4fa2-acb0-63127f879dbf"), event_id=24, version=0)
class Microsoft_Windows_Diagnosis_PCW_24_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "FunctionIndex" / Int32ul
    )


@declare(guid=guid("aabf8b86-7936-4fa2-acb0-63127f879dbf"), event_id=25, version=0)
class Microsoft_Windows_Diagnosis_PCW_25_0(Etw):
    pattern = Struct(
        "ProviderGuid" / Guid,
        "CounterSetGuid" / Guid
    )

