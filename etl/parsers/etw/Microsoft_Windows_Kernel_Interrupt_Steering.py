# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-Interrupt-Steering
GUID : 951b41ea-c830-44dc-a671-e2c9958809b8
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("951b41ea-c830-44dc-a671-e2c9958809b8"), event_id=1, version=0)
class Microsoft_Windows_Kernel_Interrupt_Steering_1_0(Etw):
    pattern = Struct(
        "LoadPercent" / Int32ul,
        "GsivCount" / Int32ul,
        "MaskCount" / Int32ul,
        "GroupCount" / Int16ul,
        "Mask" / Int64ul
    )


@declare(guid=guid("951b41ea-c830-44dc-a671-e2c9958809b8"), event_id=2, version=0)
class Microsoft_Windows_Kernel_Interrupt_Steering_2_0(Etw):
    pattern = Struct(
        "LoadPercent" / Int32ul,
        "GsivCount" / Int32ul,
        "MaskCount" / Int32ul,
        "GroupCount" / Int16ul,
        "Mask" / Int64ul
    )


@declare(guid=guid("951b41ea-c830-44dc-a671-e2c9958809b8"), event_id=3, version=0)
class Microsoft_Windows_Kernel_Interrupt_Steering_3_0(Etw):
    pattern = Struct(
        "Gsiv" / Int32ul,
        "NewTarget" / Int32ul,
        "OldTarget" / Int32ul,
        "Vector" / Int32ul,
        "ServiceRoutine" / Int64ul,
        "IsrLoad" / Int32ul,
        "DpcLoad" / Int32ul
    )


@declare(guid=guid("951b41ea-c830-44dc-a671-e2c9958809b8"), event_id=4, version=0)
class Microsoft_Windows_Kernel_Interrupt_Steering_4_0(Etw):
    pattern = Struct(
        "Gsiv" / Int32ul,
        "NewTarget" / Int32ul,
        "OldTarget" / Int32ul,
        "Vector" / Int32ul,
        "ServiceRoutine" / Int64ul,
        "IsrLoad" / Int32ul,
        "DpcLoad" / Int32ul
    )


@declare(guid=guid("951b41ea-c830-44dc-a671-e2c9958809b8"), event_id=5, version=0)
class Microsoft_Windows_Kernel_Interrupt_Steering_5_0(Etw):
    pattern = Struct(
        "Gsiv" / Int32ul,
        "NewTarget" / Int32ul,
        "OldTarget" / Int32ul,
        "Vector" / Int32ul,
        "ServiceRoutine" / Int64ul,
        "IsrLoad" / Int32ul,
        "DpcLoad" / Int32ul
    )


@declare(guid=guid("951b41ea-c830-44dc-a671-e2c9958809b8"), event_id=6, version=0)
class Microsoft_Windows_Kernel_Interrupt_Steering_6_0(Etw):
    pattern = Struct(
        "Gsiv" / Int32ul,
        "NewTarget" / Int32ul,
        "OldTarget" / Int32ul,
        "Vector" / Int32ul,
        "ServiceRoutine" / Int64ul,
        "IsrLoad" / Int32ul,
        "DpcLoad" / Int32ul
    )


@declare(guid=guid("951b41ea-c830-44dc-a671-e2c9958809b8"), event_id=7, version=0)
class Microsoft_Windows_Kernel_Interrupt_Steering_7_0(Etw):
    pattern = Struct(
        "ProcIndex" / Int32ul,
        "DeviceInterrupts" / Int32ul
    )


@declare(guid=guid("951b41ea-c830-44dc-a671-e2c9958809b8"), event_id=8, version=0)
class Microsoft_Windows_Kernel_Interrupt_Steering_8_0(Etw):
    pattern = Struct(
        "ProcIndex" / Int32ul,
        "DeviceInterrupts" / Int32ul
    )

