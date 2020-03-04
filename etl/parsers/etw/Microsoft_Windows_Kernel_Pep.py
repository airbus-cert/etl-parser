# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-Pep
GUID : 5412704e-b2e1-4624-8ffd-55777b8f7373
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5412704e-b2e1-4624-8ffd-55777b8f7373"), event_id=1, version=0)
class Microsoft_Windows_Kernel_Pep_1_0(Etw):
    pattern = Struct(
        "VoltageRailId" / Int32ul,
        "VoltageRailName" / WString,
        "CurrentVoltageMv" / Int32ul,
        "MaxVoltageMv" / Int32ul
    )


@declare(guid=guid("5412704e-b2e1-4624-8ffd-55777b8f7373"), event_id=2, version=0)
class Microsoft_Windows_Kernel_Pep_2_0(Etw):
    pattern = Struct(
        "DeviceId" / Int64ul,
        "DeviceName" / WString,
        "PlatformStateDependencyCount" / Int32ul,
        "PlatformStateDependency" / Int8ul
    )


@declare(guid=guid("5412704e-b2e1-4624-8ffd-55777b8f7373"), event_id=3, version=0)
class Microsoft_Windows_Kernel_Pep_3_0(Etw):
    pattern = Struct(
        "VoltageRailId" / Int32ul,
        "DeviceId" / Int64ul,
        "ComponentIndex" / Int32ul,
        "CurrentFrequencyKHz" / Int32ul,
        "MaxFrequencyKHz" / Int32ul,
        "PlatformStateDependencyCount" / Int32ul,
        "PlatformStateDependency" / Int64sl,
        "ComponentDescriptionLength" / Int32ul,
        "ComponentDescription" / Bytes(lambda this: this.ComponentDescriptionLength)
    )


@declare(guid=guid("5412704e-b2e1-4624-8ffd-55777b8f7373"), event_id=4, version=0)
class Microsoft_Windows_Kernel_Pep_4_0(Etw):
    pattern = Struct(
        "VoltageRailId" / Int32ul,
        "OldRailVoltageMv" / Int32ul,
        "NewRailVoltageMv" / Int32ul
    )


@declare(guid=guid("5412704e-b2e1-4624-8ffd-55777b8f7373"), event_id=5, version=0)
class Microsoft_Windows_Kernel_Pep_5_0(Etw):
    pattern = Struct(
        "DeviceId" / Int64ul,
        "ComponentIndex" / Int32ul,
        "OldComponentFrequencyKHz" / Int32ul,
        "NewComponentFrequencyKHz" / Int32ul
    )


@declare(guid=guid("5412704e-b2e1-4624-8ffd-55777b8f7373"), event_id=6, version=0)
class Microsoft_Windows_Kernel_Pep_6_0(Etw):
    pattern = Struct(
        "PlatformStateCount" / Int32ul,
        "PlatformIdleStateResidency" / CString
    )


@declare(guid=guid("5412704e-b2e1-4624-8ffd-55777b8f7373"), event_id=7, version=0)
class Microsoft_Windows_Kernel_Pep_7_0(Etw):
    pattern = Struct(
        "OldPlatformState" / Int32ul,
        "NewPlatformState" / Int32ul
    )

