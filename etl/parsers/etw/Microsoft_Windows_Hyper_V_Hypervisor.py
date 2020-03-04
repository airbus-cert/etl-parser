# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Hyper-V-Hypervisor
GUID : 52fc89f8-995e-434c-a91e-199986449890
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=2, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_2_0(Etw):
    pattern = Struct(
        "SchedulerType" / Int32ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=10, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_10_0(Etw):
    pattern = Struct(
        "Error" / Int64ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=11, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_11_0(Etw):
    pattern = Struct(
        "Error" / Int64ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=12, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_12_0(Etw):
    pattern = Struct(
        "ProcessorFeatures" / Int64ul,
        "XsaveFeatures" / Int64ul,
        "CLFlushSize" / Int32ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=20, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_20_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=26, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_26_0(Etw):
    pattern = Struct(
        "BalStatus" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=34, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_34_0(Etw):
    pattern = Struct(
        "ImageName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=36, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_36_0(Etw):
    pattern = Struct(
        "ImageName" / WString
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=37, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_37_0(Etw):
    pattern = Struct(
        "ImageName" / WString
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=38, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_38_0(Etw):
    pattern = Struct(
        "BalStatus" / Int64ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=39, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_39_0(Etw):
    pattern = Struct(
        "LoadOptions" / CString
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=40, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_40_0(Etw):
    pattern = Struct(
        "HypervisorVersion" / Int32ul,
        "VersionSupported" / Int32ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=46, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_46_0(Etw):
    pattern = Struct(
        "MSRIndex" / Int32ul,
        "AllowedZeroes" / Int64ul,
        "AllowedOnes" / Int64ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=48, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_48_0(Etw):
    pattern = Struct(
        "Leaf" / Int32ul,
        "Register" / Int32ul,
        "FeaturesNeeded" / Int32ul,
        "FeaturesSupported" / Int32ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=63, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_63_0(Etw):
    pattern = Struct(
        "Phase" / Int32ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=80, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_80_0(Etw):
    pattern = Struct(
        "NtStatus" / Int32ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=86, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_86_0(Etw):
    pattern = Struct(
        "ExpectedVersion" / Int32ul,
        "ActualVersion" / Int32ul,
        "ExpectedFunctionTableSize" / Int32ul,
        "ActualFunctionTableSize" / Int32ul,
        "UpdateDllName" / WString
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=96, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_96_0(Etw):
    pattern = Struct(
        "CPU" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=97, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_97_0(Etw):
    pattern = Struct(
        "CPU" / Int32ul,
        "LeafNumber" / Int64ul,
        "Register" / Int64ul,
        "BSPCpuidData" / Int64ul,
        "APCpuidData" / Int64ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=129, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_129_0(Etw):
    pattern = Struct(
        "HardwarePresent" / Int8ul,
        "HardwareEnabled" / Int8ul,
        "Policy" / Int64ul,
        "EnabledFeatures" / Int64ul,
        "InternalInfo" / Int64ul,
        "Problems" / Int64ul,
        "AdditionalInfo" / Int64ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=144, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_144_0(Etw):
    pattern = Struct(
        "DeviceId" / Int64ul,
        "PartitionId" / Int64ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=145, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_145_0(Etw):
    pattern = Struct(
        "DeviceId" / Int64ul,
        "PartitionId" / Int64ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=146, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_146_0(Etw):
    pattern = Struct(
        "DeviceId" / Int64ul,
        "PartitionId" / Int64ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=147, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_147_0(Etw):
    pattern = Struct(
        "IoApicId" / Int8ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=148, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_148_0(Etw):
    pattern = Struct(
        "DeviceId" / Int64ul,
        "UnitBaseAddress" / Int64ul,
        "PartitionId" / Int64ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=149, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_149_0(Etw):
    pattern = Struct(
        "DeviceId" / Int64ul,
        "PartitionId" / Int64ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=152, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_152_0(Etw):
    pattern = Struct(
        "ImageName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=153, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_153_0(Etw):
    pattern = Struct(
        "ImageName" / WString
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=154, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_154_0(Etw):
    pattern = Struct(
        "MaxDelta" / Int64sl,
        "MinDelta" / Int64sl
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=155, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_155_0(Etw):
    pattern = Struct(
        "ProcessorFeatures" / Int64ul,
        "XsaveFeatures" / Int64ul,
        "CLFlushSize" / Int32ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=156, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_156_0(Etw):
    pattern = Struct(
        "NotAffectedRdclNo" / Int8ul,
        "NotAffectedAtom" / Int8ul,
        "CacheFlushSupported" / Int8ul,
        "SmtEnabled" / Int8ul,
        "ParentHypervisorFlushes" / Int8ul,
        "DisabledLoadOption" / Int8ul,
        "Enabled" / Int8ul,
        "CacheFlushNeeded" / Int8ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=8451, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_8451_0(Etw):
    pattern = Struct(
        "Error" / Int64ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=12550, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_12550_0(Etw):
    pattern = Struct(
        "Msr" / Int32ul,
        "IsWrite" / Int8ul,
        "MsrValue" / Int64ul,
        "AccessStatus" / Int16ul,
        "Pc" / Int64ul,
        "ImageBase" / Int64ul,
        "ImageChecksum" / Int32ul,
        "ImageTimestamp" / Int32ul,
        "ImageName" / CString
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=16641, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_16641_0(Etw):
    pattern = Struct(
        "PartitionId" / Int64ul
    )


@declare(guid=guid("52fc89f8-995e-434c-a91e-199986449890"), event_id=16642, version=0)
class Microsoft_Windows_Hyper_V_Hypervisor_16642_0(Etw):
    pattern = Struct(
        "PartitionId" / Int64ul
    )

