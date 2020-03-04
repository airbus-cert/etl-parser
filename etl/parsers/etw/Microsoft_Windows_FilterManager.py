# -*- coding: utf-8 -*-
"""
Microsoft-Windows-FilterManager
GUID : f3c5e28e-63f6-49c7-a204-e48a1bc4b09d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f3c5e28e-63f6-49c7-a204-e48a1bc4b09d"), event_id=1, version=0)
class Microsoft_Windows_FilterManager_1_0(Etw):
    pattern = Struct(
        "FinalStatus" / Int32ul,
        "DeviceVersionMajor" / Int32ul,
        "DeviceVersionMinor" / Int32ul,
        "DeviceNameLength" / Int16ul,
        "DeviceName" / Bytes(lambda this: this.DeviceNameLength),
        "DeviceTime" / Int64ul
    )


@declare(guid=guid("f3c5e28e-63f6-49c7-a204-e48a1bc4b09d"), event_id=2, version=0)
class Microsoft_Windows_FilterManager_2_0(Etw):
    pattern = Struct(
        "FinalStatus" / Int32ul,
        "ExtraStringLength" / Int16ul,
        "ExtraString" / Bytes(lambda this: this.ExtraStringLength)
    )


@declare(guid=guid("f3c5e28e-63f6-49c7-a204-e48a1bc4b09d"), event_id=3, version=0)
class Microsoft_Windows_FilterManager_3_0(Etw):
    pattern = Struct(
        "FinalStatus" / Int32ul,
        "ExtraStringLength" / Int16ul,
        "ExtraString" / Bytes(lambda this: this.ExtraStringLength)
    )


@declare(guid=guid("f3c5e28e-63f6-49c7-a204-e48a1bc4b09d"), event_id=4, version=0)
class Microsoft_Windows_FilterManager_4_0(Etw):
    pattern = Struct(
        "FinalStatus" / Int32ul,
        "DeviceVersionMajor" / Int32ul,
        "DeviceVersionMinor" / Int32ul,
        "DeviceNameLength" / Int16ul,
        "DeviceName" / Bytes(lambda this: this.DeviceNameLength),
        "DeviceTime" / Int64ul,
        "ExtraStringLength" / Int16ul,
        "ExtraString" / Bytes(lambda this: this.ExtraStringLength)
    )


@declare(guid=guid("f3c5e28e-63f6-49c7-a204-e48a1bc4b09d"), event_id=5, version=0)
class Microsoft_Windows_FilterManager_5_0(Etw):
    pattern = Struct(
        "FinalStatus" / Int32ul,
        "DeviceVersionMajor" / Int32ul,
        "DeviceVersionMinor" / Int32ul,
        "DeviceNameLength" / Int16ul,
        "DeviceName" / Bytes(lambda this: this.DeviceNameLength),
        "DeviceTime" / Int64ul
    )


@declare(guid=guid("f3c5e28e-63f6-49c7-a204-e48a1bc4b09d"), event_id=6, version=0)
class Microsoft_Windows_FilterManager_6_0(Etw):
    pattern = Struct(
        "FinalStatus" / Int32ul,
        "DeviceVersionMajor" / Int32ul,
        "DeviceVersionMinor" / Int32ul,
        "DeviceNameLength" / Int16ul,
        "DeviceName" / Bytes(lambda this: this.DeviceNameLength),
        "DeviceTime" / Int64ul
    )


@declare(guid=guid("f3c5e28e-63f6-49c7-a204-e48a1bc4b09d"), event_id=7, version=0)
class Microsoft_Windows_FilterManager_7_0(Etw):
    pattern = Struct(
        "FinalStatus" / Int32ul,
        "DeviceVersionMajor" / Int32ul,
        "DeviceVersionMinor" / Int32ul,
        "DeviceNameLength" / Int16ul,
        "DeviceName" / Bytes(lambda this: this.DeviceNameLength),
        "DeviceTime" / Int64ul
    )


@declare(guid=guid("f3c5e28e-63f6-49c7-a204-e48a1bc4b09d"), event_id=8, version=0)
class Microsoft_Windows_FilterManager_8_0(Etw):
    pattern = Struct(
        "FinalStatus" / Int32ul,
        "ExtraStringLength" / Int16ul,
        "ExtraString" / Bytes(lambda this: this.ExtraStringLength)
    )


@declare(guid=guid("f3c5e28e-63f6-49c7-a204-e48a1bc4b09d"), event_id=9, version=0)
class Microsoft_Windows_FilterManager_9_0(Etw):
    pattern = Struct(
        "FinalStatus" / Int32ul,
        "ExtraStringLength" / Int16ul,
        "ExtraString" / Bytes(lambda this: this.ExtraStringLength)
    )


@declare(guid=guid("f3c5e28e-63f6-49c7-a204-e48a1bc4b09d"), event_id=10, version=0)
class Microsoft_Windows_FilterManager_10_0(Etw):
    pattern = Struct(
        "FinalStatus" / Int32ul,
        "ExtraStringLength" / Int16ul,
        "ExtraString" / Bytes(lambda this: this.ExtraStringLength)
    )

