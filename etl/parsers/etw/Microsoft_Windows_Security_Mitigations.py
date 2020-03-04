# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Security-Mitigations
GUID : fae10392-f0af-4ac0-b8ff-9f4d920c3cdf
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=1, version=0)
class Microsoft_Windows_Security_Mitigations_1_0(Etw):
    pattern = Struct(
        "ProcessPathLength" / Int16ul,
        "ProcessPath" / Bytes(lambda this: this.ProcessPathLength),
        "ProcessCommandLineLength" / Int16ul,
        "ProcessCommandLine" / Bytes(lambda this: this.ProcessCommandLineLength),
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=2, version=0)
class Microsoft_Windows_Security_Mitigations_2_0(Etw):
    pattern = Struct(
        "ProcessPathLength" / Int16ul,
        "ProcessPath" / Bytes(lambda this: this.ProcessPathLength),
        "ProcessCommandLineLength" / Int16ul,
        "ProcessCommandLine" / Bytes(lambda this: this.ProcessCommandLineLength),
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=3, version=0)
class Microsoft_Windows_Security_Mitigations_3_0(Etw):
    pattern = Struct(
        "ProcessPathLength" / Int16ul,
        "ProcessPath" / Bytes(lambda this: this.ProcessPathLength),
        "ProcessCommandLineLength" / Int16ul,
        "ProcessCommandLine" / Bytes(lambda this: this.ProcessCommandLineLength),
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "ChildImagePathNameLength" / Int16ul,
        "ChildImagePathName" / Bytes(lambda this: this.ChildImagePathNameLength),
        "ChildCommandLineLength" / Int16ul,
        "ChildCommandLine" / Bytes(lambda this: this.ChildCommandLineLength)
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=4, version=0)
class Microsoft_Windows_Security_Mitigations_4_0(Etw):
    pattern = Struct(
        "ProcessPathLength" / Int16ul,
        "ProcessPath" / Bytes(lambda this: this.ProcessPathLength),
        "ProcessCommandLineLength" / Int16ul,
        "ProcessCommandLine" / Bytes(lambda this: this.ProcessCommandLineLength),
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "ChildImagePathNameLength" / Int16ul,
        "ChildImagePathName" / Bytes(lambda this: this.ChildImagePathNameLength),
        "ChildCommandLineLength" / Int16ul,
        "ChildCommandLine" / Bytes(lambda this: this.ChildCommandLineLength)
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=5, version=0)
class Microsoft_Windows_Security_Mitigations_5_0(Etw):
    pattern = Struct(
        "ProcessPathLength" / Int16ul,
        "ProcessPath" / Bytes(lambda this: this.ProcessPathLength),
        "ProcessCommandLineLength" / Int16ul,
        "ProcessCommandLine" / Bytes(lambda this: this.ProcessCommandLineLength),
        "ProcessId" / Int32ul,
        "ProcessCreateTime" / Int64ul,
        "ProcessStartKey" / Int64ul,
        "ProcessSignatureLevel" / Int8ul,
        "ProcessSectionSignatureLevel" / Int8ul,
        "ProcessProtection" / Int8ul,
        "TargetThreadId" / Int32ul,
        "TargetThreadCreateTime" / Int64ul,
        "ImageNameLength" / Int16ul,
        "ImageName" / Bytes(lambda this: this.ImageNameLength)
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=6, version=0)
class Microsoft_Windows_Security_Mitigations_6_0(Etw):
    pattern = Struct(
        "ProcessPathLength" / Int16ul,
        "ProcessPath" / Bytes(lambda this: this.ProcessPathLength),
        "ProcessCommandLineLength" / Int16ul,
        "ProcessCommandLine" / Bytes(lambda this: this.ProcessCommandLineLength),
        "ProcessId" / Int32ul,
        "ProcessCreateTime" / Int64ul,
        "ProcessStartKey" / Int64ul,
        "ProcessSignatureLevel" / Int8ul,
        "ProcessSectionSignatureLevel" / Int8ul,
        "ProcessProtection" / Int8ul,
        "TargetThreadId" / Int32ul,
        "TargetThreadCreateTime" / Int64ul,
        "ImageNameLength" / Int16ul,
        "ImageName" / Bytes(lambda this: this.ImageNameLength)
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=7, version=0)
class Microsoft_Windows_Security_Mitigations_7_0(Etw):
    pattern = Struct(
        "ProcessPathLength" / Int16ul,
        "ProcessPath" / Bytes(lambda this: this.ProcessPathLength),
        "ProcessCommandLineLength" / Int16ul,
        "ProcessCommandLine" / Bytes(lambda this: this.ProcessCommandLineLength),
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=8, version=0)
class Microsoft_Windows_Security_Mitigations_8_0(Etw):
    pattern = Struct(
        "ProcessPathLength" / Int16ul,
        "ProcessPath" / Bytes(lambda this: this.ProcessPathLength),
        "ProcessCommandLineLength" / Int16ul,
        "ProcessCommandLine" / Bytes(lambda this: this.ProcessCommandLineLength),
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=9, version=0)
class Microsoft_Windows_Security_Mitigations_9_0(Etw):
    pattern = Struct(
        "ProcessPathLength" / Int16ul,
        "ProcessPath" / Bytes(lambda this: this.ProcessPathLength),
        "ProcessCommandLineLength" / Int16ul,
        "ProcessCommandLine" / Bytes(lambda this: this.ProcessCommandLineLength),
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=10, version=0)
class Microsoft_Windows_Security_Mitigations_10_0(Etw):
    pattern = Struct(
        "ProcessPathLength" / Int16ul,
        "ProcessPath" / Bytes(lambda this: this.ProcessPathLength),
        "ProcessCommandLineLength" / Int16ul,
        "ProcessCommandLine" / Bytes(lambda this: this.ProcessCommandLineLength),
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=11, version=0)
class Microsoft_Windows_Security_Mitigations_11_0(Etw):
    pattern = Struct(
        "ProcessPathLength" / Int16ul,
        "ProcessPath" / Bytes(lambda this: this.ProcessPathLength),
        "ProcessCommandLineLength" / Int16ul,
        "ProcessCommandLine" / Bytes(lambda this: this.ProcessCommandLineLength),
        "ProcessId" / Int32ul,
        "ProcessCreateTime" / Int64ul,
        "ProcessStartKey" / Int64ul,
        "ProcessSignatureLevel" / Int8ul,
        "ProcessSectionSignatureLevel" / Int8ul,
        "ProcessProtection" / Int8ul,
        "TargetThreadId" / Int32ul,
        "TargetThreadCreateTime" / Int64ul,
        "RequiredSignatureLevel" / Int8ul,
        "SignatureLevel" / Int8ul,
        "ImageNameLength" / Int16ul,
        "ImageName" / Bytes(lambda this: this.ImageNameLength)
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=12, version=0)
class Microsoft_Windows_Security_Mitigations_12_0(Etw):
    pattern = Struct(
        "ProcessPathLength" / Int16ul,
        "ProcessPath" / Bytes(lambda this: this.ProcessPathLength),
        "ProcessCommandLineLength" / Int16ul,
        "ProcessCommandLine" / Bytes(lambda this: this.ProcessCommandLineLength),
        "ProcessId" / Int32ul,
        "ProcessCreateTime" / Int64ul,
        "ProcessStartKey" / Int64ul,
        "ProcessSignatureLevel" / Int8ul,
        "ProcessSectionSignatureLevel" / Int8ul,
        "ProcessProtection" / Int8ul,
        "TargetThreadId" / Int32ul,
        "TargetThreadCreateTime" / Int64ul,
        "RequiredSignatureLevel" / Int8ul,
        "SignatureLevel" / Int8ul,
        "ImageNameLength" / Int16ul,
        "ImageName" / Bytes(lambda this: this.ImageNameLength)
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=13, version=0)
class Microsoft_Windows_Security_Mitigations_13_0(Etw):
    pattern = Struct(
        "Subcode" / Int32ul,
        "ProcessPath" / WString,
        "ProcessId" / Int32ul,
        "ModuleFullPath" / WString,
        "ModuleBase" / Int64ul,
        "ModuleAddress" / Int64ul,
        "MemAddress" / Int64ul,
        "MemModuleFullPath" / WString,
        "MemModuleBase" / Int64ul,
        "APIName" / WString,
        "ProcessStartTime" / Int64ul,
        "ThreadId" / Int32ul
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=14, version=0)
class Microsoft_Windows_Security_Mitigations_14_0(Etw):
    pattern = Struct(
        "Subcode" / Int32ul,
        "ProcessPath" / WString,
        "ProcessId" / Int32ul,
        "ModuleFullPath" / WString,
        "ModuleBase" / Int64ul,
        "ModuleAddress" / Int64ul,
        "MemAddress" / Int64ul,
        "MemModuleFullPath" / WString,
        "MemModuleBase" / Int64ul,
        "APIName" / WString,
        "ProcessStartTime" / Int64ul,
        "ThreadId" / Int32ul
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=15, version=0)
class Microsoft_Windows_Security_Mitigations_15_0(Etw):
    pattern = Struct(
        "Subcode" / Int32ul,
        "ProcessPath" / WString,
        "ProcessId" / Int32ul,
        "ModuleFullPath" / WString,
        "ModuleBase" / Int64ul,
        "ModuleAddress" / Int64ul,
        "MemAddress" / Int64ul,
        "MemModuleFullPath" / WString,
        "MemModuleBase" / Int64ul,
        "APIName" / WString,
        "ProcessStartTime" / Int64ul,
        "ThreadId" / Int32ul
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=16, version=0)
class Microsoft_Windows_Security_Mitigations_16_0(Etw):
    pattern = Struct(
        "Subcode" / Int32ul,
        "ProcessPath" / WString,
        "ProcessId" / Int32ul,
        "ModuleFullPath" / WString,
        "ModuleBase" / Int64ul,
        "ModuleAddress" / Int64ul,
        "MemAddress" / Int64ul,
        "MemModuleFullPath" / WString,
        "MemModuleBase" / Int64ul,
        "APIName" / WString,
        "ProcessStartTime" / Int64ul,
        "ThreadId" / Int32ul
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=17, version=0)
class Microsoft_Windows_Security_Mitigations_17_0(Etw):
    pattern = Struct(
        "Subcode" / Int32ul,
        "ProcessPath" / WString,
        "ProcessId" / Int32ul,
        "ModuleFullPath" / WString,
        "ModuleBase" / Int64ul,
        "ModuleAddress" / Int64ul,
        "MemAddress" / Int64ul,
        "MemModuleFullPath" / WString,
        "MemModuleBase" / Int64ul,
        "APIName" / WString,
        "ProcessStartTime" / Int64ul,
        "ThreadId" / Int32ul
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=18, version=0)
class Microsoft_Windows_Security_Mitigations_18_0(Etw):
    pattern = Struct(
        "Subcode" / Int32ul,
        "ProcessPath" / WString,
        "ProcessId" / Int32ul,
        "ModuleFullPath" / WString,
        "ModuleBase" / Int64ul,
        "ModuleAddress" / Int64ul,
        "MemAddress" / Int64ul,
        "MemModuleFullPath" / WString,
        "MemModuleBase" / Int64ul,
        "APIName" / WString,
        "ProcessStartTime" / Int64ul,
        "ThreadId" / Int32ul
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=19, version=0)
class Microsoft_Windows_Security_Mitigations_19_0(Etw):
    pattern = Struct(
        "Subcode" / Int32ul,
        "ProcessPath" / WString,
        "ProcessId" / Int32ul,
        "HookedAPI" / WString,
        "ReturnAddress" / Int64ul,
        "CalledAddress" / Int64ul,
        "TargetAddress" / Int64ul,
        "StackAddress" / Int64ul,
        "FrameAddress" / Int64ul,
        "ReturnAddressModuleFullPath" / WString,
        "ProcessStartTime" / Int64ul,
        "ThreadId" / Int32ul
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=20, version=0)
class Microsoft_Windows_Security_Mitigations_20_0(Etw):
    pattern = Struct(
        "Subcode" / Int32ul,
        "ProcessPath" / WString,
        "ProcessId" / Int32ul,
        "HookedAPI" / WString,
        "ReturnAddress" / Int64ul,
        "CalledAddress" / Int64ul,
        "TargetAddress" / Int64ul,
        "StackAddress" / Int64ul,
        "FrameAddress" / Int64ul,
        "ReturnAddressModuleFullPath" / WString,
        "ProcessStartTime" / Int64ul,
        "ThreadId" / Int32ul
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=21, version=0)
class Microsoft_Windows_Security_Mitigations_21_0(Etw):
    pattern = Struct(
        "Subcode" / Int32ul,
        "ProcessPath" / WString,
        "ProcessId" / Int32ul,
        "HookedAPI" / WString,
        "ReturnAddress" / Int64ul,
        "CalledAddress" / Int64ul,
        "TargetAddress" / Int64ul,
        "StackAddress" / Int64ul,
        "FrameAddress" / Int64ul,
        "ReturnAddressModuleFullPath" / WString,
        "ProcessStartTime" / Int64ul,
        "ThreadId" / Int32ul
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=22, version=0)
class Microsoft_Windows_Security_Mitigations_22_0(Etw):
    pattern = Struct(
        "Subcode" / Int32ul,
        "ProcessPath" / WString,
        "ProcessId" / Int32ul,
        "HookedAPI" / WString,
        "ReturnAddress" / Int64ul,
        "CalledAddress" / Int64ul,
        "TargetAddress" / Int64ul,
        "StackAddress" / Int64ul,
        "FrameAddress" / Int64ul,
        "ReturnAddressModuleFullPath" / WString,
        "ProcessStartTime" / Int64ul,
        "ThreadId" / Int32ul
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=23, version=0)
class Microsoft_Windows_Security_Mitigations_23_0(Etw):
    pattern = Struct(
        "Subcode" / Int32ul,
        "ProcessPath" / WString,
        "ProcessId" / Int32ul,
        "HookedAPI" / WString,
        "ReturnAddress" / Int64ul,
        "CalledAddress" / Int64ul,
        "TargetAddress" / Int64ul,
        "StackAddress" / Int64ul,
        "FrameAddress" / Int64ul,
        "ReturnAddressModuleFullPath" / WString,
        "ProcessStartTime" / Int64ul,
        "ThreadId" / Int32ul
    )


@declare(guid=guid("fae10392-f0af-4ac0-b8ff-9f4d920c3cdf"), event_id=24, version=0)
class Microsoft_Windows_Security_Mitigations_24_0(Etw):
    pattern = Struct(
        "Subcode" / Int32ul,
        "ProcessPath" / WString,
        "ProcessId" / Int32ul,
        "HookedAPI" / WString,
        "ReturnAddress" / Int64ul,
        "CalledAddress" / Int64ul,
        "TargetAddress" / Int64ul,
        "StackAddress" / Int64ul,
        "FrameAddress" / Int64ul,
        "ReturnAddressModuleFullPath" / WString,
        "ProcessStartTime" / Int64ul,
        "ThreadId" / Int32ul
    )

