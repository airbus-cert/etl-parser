# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Devices-Background
GUID : 64ef2b1c-4ae1-4e64-8599-1636e441ec88
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("64ef2b1c-4ae1-4e64-8599-1636e441ec88"), event_id=1, version=0)
class Microsoft_Windows_Devices_Background_1_0(Etw):
    pattern = Struct(
        "TriggerID" / Guid,
        "Application" / WString,
        "TaskType" / Int32ul,
        "Device" / WString,
        "HardwareId" / WString,
        "Arguments" / WString
    )


@declare(guid=guid("64ef2b1c-4ae1-4e64-8599-1636e441ec88"), event_id=2, version=0)
class Microsoft_Windows_Devices_Background_2_0(Etw):
    pattern = Struct(
        "TriggerID" / Guid,
        "TaskProcessID" / Int32sl,
        "Device" / WString
    )


@declare(guid=guid("64ef2b1c-4ae1-4e64-8599-1636e441ec88"), event_id=3, version=0)
class Microsoft_Windows_Devices_Background_3_0(Etw):
    pattern = Struct(
        "TriggerID" / Guid,
        "Reason" / Int32ul,
        "Device" / WString
    )


@declare(guid=guid("64ef2b1c-4ae1-4e64-8599-1636e441ec88"), event_id=4, version=0)
class Microsoft_Windows_Devices_Background_4_0(Etw):
    pattern = Struct(
        "TriggerID" / Guid,
        "Duration" / Int32sl
    )


@declare(guid=guid("64ef2b1c-4ae1-4e64-8599-1636e441ec88"), event_id=5, version=0)
class Microsoft_Windows_Devices_Background_5_0(Etw):
    pattern = Struct(
        "TriggerID" / Guid,
        "Application" / WString,
        "TaskType" / Int32ul,
        "Device" / WString,
        "HardwareId" / WString,
        "Arguments" / WString,
        "Reason" / Int32ul,
        "Error" / Int32sl
    )


@declare(guid=guid("64ef2b1c-4ae1-4e64-8599-1636e441ec88"), event_id=6, version=0)
class Microsoft_Windows_Devices_Background_6_0(Etw):
    pattern = Struct(
        "TriggerID" / Guid,
        "Application" / WString,
        "TaskType" / Int32ul,
        "Device" / WString,
        "HardwareId" / WString,
        "Arguments" / WString,
        "Error" / Int32sl
    )


@declare(guid=guid("64ef2b1c-4ae1-4e64-8599-1636e441ec88"), event_id=10, version=0)
class Microsoft_Windows_Devices_Background_10_0(Etw):
    pattern = Struct(
        "TriggerID" / Guid,
        "Application" / WString,
        "TaskType" / Int32ul,
        "Device" / WString,
        "HardwareId" / WString,
        "Arguments" / WString
    )


@declare(guid=guid("64ef2b1c-4ae1-4e64-8599-1636e441ec88"), event_id=11, version=0)
class Microsoft_Windows_Devices_Background_11_0(Etw):
    pattern = Struct(
        "TriggerID" / Guid,
        "TaskProcessID" / Int32sl,
        "Device" / WString
    )


@declare(guid=guid("64ef2b1c-4ae1-4e64-8599-1636e441ec88"), event_id=12, version=0)
class Microsoft_Windows_Devices_Background_12_0(Etw):
    pattern = Struct(
        "TriggerID" / Guid,
        "Reason" / Int32ul,
        "Device" / WString
    )


@declare(guid=guid("64ef2b1c-4ae1-4e64-8599-1636e441ec88"), event_id=13, version=0)
class Microsoft_Windows_Devices_Background_13_0(Etw):
    pattern = Struct(
        "TriggerID" / Guid,
        "Duration" / Int32sl
    )


@declare(guid=guid("64ef2b1c-4ae1-4e64-8599-1636e441ec88"), event_id=14, version=0)
class Microsoft_Windows_Devices_Background_14_0(Etw):
    pattern = Struct(
        "TriggerID" / Guid,
        "Application" / WString,
        "TaskType" / Int32ul,
        "Device" / WString,
        "HardwareId" / WString,
        "Arguments" / WString,
        "Reason" / Int32ul,
        "Error" / Int32sl
    )


@declare(guid=guid("64ef2b1c-4ae1-4e64-8599-1636e441ec88"), event_id=15, version=0)
class Microsoft_Windows_Devices_Background_15_0(Etw):
    pattern = Struct(
        "TriggerID" / Guid,
        "Application" / WString,
        "TaskType" / Int32ul,
        "Device" / WString,
        "HardwareId" / WString,
        "Arguments" / WString,
        "Error" / Int32sl
    )


@declare(guid=guid("64ef2b1c-4ae1-4e64-8599-1636e441ec88"), event_id=20, version=0)
class Microsoft_Windows_Devices_Background_20_0(Etw):
    pattern = Struct(
        "TriggerID" / Guid,
        "Application" / WString,
        "TaskType" / Int32ul,
        "Device" / WString,
        "HardwareId" / WString,
        "Arguments" / WString
    )


@declare(guid=guid("64ef2b1c-4ae1-4e64-8599-1636e441ec88"), event_id=21, version=0)
class Microsoft_Windows_Devices_Background_21_0(Etw):
    pattern = Struct(
        "TriggerID" / Guid,
        "Application" / WString,
        "TaskType" / Int32ul,
        "Device" / WString,
        "HardwareId" / WString,
        "Arguments" / WString
    )


@declare(guid=guid("64ef2b1c-4ae1-4e64-8599-1636e441ec88"), event_id=22, version=0)
class Microsoft_Windows_Devices_Background_22_0(Etw):
    pattern = Struct(
        "TriggerID" / Guid,
        "Application" / WString,
        "TaskType" / Int32ul,
        "Device" / WString,
        "HardwareId" / WString,
        "Arguments" / WString
    )


@declare(guid=guid("64ef2b1c-4ae1-4e64-8599-1636e441ec88"), event_id=30, version=0)
class Microsoft_Windows_Devices_Background_30_0(Etw):
    pattern = Struct(
        "packageName" / WString,
        "aepId" / WString
    )

