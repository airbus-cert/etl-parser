# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DotNETRuntimeRundown
GUID : a669021c-c450-4609-a035-5af59af4df18
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=0, version=0)
class Microsoft_Windows_DotNETRuntimeRundown_0_0(Etw):
    pattern = Struct(
        "ClrInstanceID" / Int16ul,
        "Reserved1" / Int8ul,
        "Reserved2" / Int8ul,
        "FrameCount" / Int32ul,
        "Stack" / Int64ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=141, version=0)
class Microsoft_Windows_DotNETRuntimeRundown_141_0(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=141, version=1)
class Microsoft_Windows_DotNETRuntimeRundown_141_1(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=141, version=2)
class Microsoft_Windows_DotNETRuntimeRundown_141_2(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "ClrInstanceID" / Int16ul,
        "ReJITID" / Int64ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=142, version=0)
class Microsoft_Windows_DotNETRuntimeRundown_142_0(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=142, version=1)
class Microsoft_Windows_DotNETRuntimeRundown_142_1(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=142, version=2)
class Microsoft_Windows_DotNETRuntimeRundown_142_2(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "ClrInstanceID" / Int16ul,
        "ReJITID" / Int64ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=143, version=0)
class Microsoft_Windows_DotNETRuntimeRundown_143_0(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "MethodNamespace" / WString,
        "MethodName" / WString,
        "MethodSignature" / WString
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=143, version=1)
class Microsoft_Windows_DotNETRuntimeRundown_143_1(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "MethodNamespace" / WString,
        "MethodName" / WString,
        "MethodSignature" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=143, version=2)
class Microsoft_Windows_DotNETRuntimeRundown_143_2(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "MethodNamespace" / WString,
        "MethodName" / WString,
        "MethodSignature" / WString,
        "ClrInstanceID" / Int16ul,
        "ReJITID" / Int64ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=144, version=0)
class Microsoft_Windows_DotNETRuntimeRundown_144_0(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "MethodNamespace" / WString,
        "MethodName" / WString,
        "MethodSignature" / WString
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=144, version=1)
class Microsoft_Windows_DotNETRuntimeRundown_144_1(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "MethodNamespace" / WString,
        "MethodName" / WString,
        "MethodSignature" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=144, version=2)
class Microsoft_Windows_DotNETRuntimeRundown_144_2(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ModuleID" / Int64ul,
        "MethodStartAddress" / Int64ul,
        "MethodSize" / Int32ul,
        "MethodToken" / Int32ul,
        "MethodFlags" / Int32ul,
        "MethodNamespace" / WString,
        "MethodName" / WString,
        "MethodSignature" / WString,
        "ClrInstanceID" / Int16ul,
        "ReJITID" / Int64ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=145, version=1)
class Microsoft_Windows_DotNETRuntimeRundown_145_1(Etw):
    pattern = Struct(
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=146, version=1)
class Microsoft_Windows_DotNETRuntimeRundown_146_1(Etw):
    pattern = Struct(
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=147, version=1)
class Microsoft_Windows_DotNETRuntimeRundown_147_1(Etw):
    pattern = Struct(
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=148, version=1)
class Microsoft_Windows_DotNETRuntimeRundown_148_1(Etw):
    pattern = Struct(
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=149, version=0)
class Microsoft_Windows_DotNETRuntimeRundown_149_0(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ReJITID" / Int64ul,
        "MethodExtent" / Int8ul,
        "CountOfMapEntries" / Int16ul,
        "ILOffsets" / Int32ul,
        "NativeOffsets" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=150, version=0)
class Microsoft_Windows_DotNETRuntimeRundown_150_0(Etw):
    pattern = Struct(
        "MethodID" / Int64ul,
        "ReJITID" / Int64ul,
        "MethodExtent" / Int8ul,
        "CountOfMapEntries" / Int16ul,
        "ILOffsets" / Int32ul,
        "NativeOffsets" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=151, version=0)
class Microsoft_Windows_DotNETRuntimeRundown_151_0(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "AssemblyID" / Int64ul,
        "AppDomainID" / Int64ul,
        "ModuleFlags" / Int32ul,
        "Reserved1" / Int32ul,
        "ModuleILPath" / WString,
        "ModuleNativePath" / WString
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=151, version=1)
class Microsoft_Windows_DotNETRuntimeRundown_151_1(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "AssemblyID" / Int64ul,
        "AppDomainID" / Int64ul,
        "ModuleFlags" / Int32ul,
        "Reserved1" / Int32ul,
        "ModuleILPath" / WString,
        "ModuleNativePath" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=152, version=0)
class Microsoft_Windows_DotNETRuntimeRundown_152_0(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "AssemblyID" / Int64ul,
        "AppDomainID" / Int64ul,
        "ModuleFlags" / Int32ul,
        "Reserved1" / Int32ul,
        "ModuleILPath" / WString,
        "ModuleNativePath" / WString
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=152, version=1)
class Microsoft_Windows_DotNETRuntimeRundown_152_1(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "AssemblyID" / Int64ul,
        "AppDomainID" / Int64ul,
        "ModuleFlags" / Int32ul,
        "Reserved1" / Int32ul,
        "ModuleILPath" / WString,
        "ModuleNativePath" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=153, version=0)
class Microsoft_Windows_DotNETRuntimeRundown_153_0(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "AssemblyID" / Int64ul,
        "ModuleFlags" / Int32ul,
        "Reserved1" / Int32ul,
        "ModuleILPath" / WString,
        "ModuleNativePath" / WString
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=153, version=1)
class Microsoft_Windows_DotNETRuntimeRundown_153_1(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "AssemblyID" / Int64ul,
        "ModuleFlags" / Int32ul,
        "Reserved1" / Int32ul,
        "ModuleILPath" / WString,
        "ModuleNativePath" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=153, version=2)
class Microsoft_Windows_DotNETRuntimeRundown_153_2(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "AssemblyID" / Int64ul,
        "ModuleFlags" / Int32ul,
        "Reserved1" / Int32ul,
        "ModuleILPath" / WString,
        "ModuleNativePath" / WString,
        "ClrInstanceID" / Int16ul,
        "ManagedPdbSignature" / Guid,
        "ManagedPdbAge" / Int32ul,
        "ManagedPdbBuildPath" / WString,
        "NativePdbSignature" / Guid,
        "NativePdbAge" / Int32ul,
        "NativePdbBuildPath" / WString
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=154, version=0)
class Microsoft_Windows_DotNETRuntimeRundown_154_0(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "AssemblyID" / Int64ul,
        "ModuleFlags" / Int32ul,
        "Reserved1" / Int32ul,
        "ModuleILPath" / WString,
        "ModuleNativePath" / WString
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=154, version=1)
class Microsoft_Windows_DotNETRuntimeRundown_154_1(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "AssemblyID" / Int64ul,
        "ModuleFlags" / Int32ul,
        "Reserved1" / Int32ul,
        "ModuleILPath" / WString,
        "ModuleNativePath" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=154, version=2)
class Microsoft_Windows_DotNETRuntimeRundown_154_2(Etw):
    pattern = Struct(
        "ModuleID" / Int64ul,
        "AssemblyID" / Int64ul,
        "ModuleFlags" / Int32ul,
        "Reserved1" / Int32ul,
        "ModuleILPath" / WString,
        "ModuleNativePath" / WString,
        "ClrInstanceID" / Int16ul,
        "ManagedPdbSignature" / Guid,
        "ManagedPdbAge" / Int32ul,
        "ManagedPdbBuildPath" / WString,
        "NativePdbSignature" / Guid,
        "NativePdbAge" / Int32ul,
        "NativePdbBuildPath" / WString
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=155, version=0)
class Microsoft_Windows_DotNETRuntimeRundown_155_0(Etw):
    pattern = Struct(
        "AssemblyID" / Int64ul,
        "AppDomainID" / Int64ul,
        "AssemblyFlags" / Int32ul,
        "FullyQualifiedAssemblyName" / WString
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=155, version=1)
class Microsoft_Windows_DotNETRuntimeRundown_155_1(Etw):
    pattern = Struct(
        "AssemblyID" / Int64ul,
        "AppDomainID" / Int64ul,
        "BindingID" / Int64ul,
        "AssemblyFlags" / Int32ul,
        "FullyQualifiedAssemblyName" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=156, version=0)
class Microsoft_Windows_DotNETRuntimeRundown_156_0(Etw):
    pattern = Struct(
        "AssemblyID" / Int64ul,
        "AppDomainID" / Int64ul,
        "AssemblyFlags" / Int32ul,
        "FullyQualifiedAssemblyName" / WString
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=156, version=1)
class Microsoft_Windows_DotNETRuntimeRundown_156_1(Etw):
    pattern = Struct(
        "AssemblyID" / Int64ul,
        "AppDomainID" / Int64ul,
        "BindingID" / Int64ul,
        "AssemblyFlags" / Int32ul,
        "FullyQualifiedAssemblyName" / WString,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=157, version=0)
class Microsoft_Windows_DotNETRuntimeRundown_157_0(Etw):
    pattern = Struct(
        "AppDomainID" / Int64ul,
        "AppDomainFlags" / Int32ul,
        "AppDomainName" / WString
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=157, version=1)
class Microsoft_Windows_DotNETRuntimeRundown_157_1(Etw):
    pattern = Struct(
        "AppDomainID" / Int64ul,
        "AppDomainFlags" / Int32ul,
        "AppDomainName" / WString,
        "AppDomainIndex" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=158, version=0)
class Microsoft_Windows_DotNETRuntimeRundown_158_0(Etw):
    pattern = Struct(
        "AppDomainID" / Int64ul,
        "AppDomainFlags" / Int32ul,
        "AppDomainName" / WString
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=158, version=1)
class Microsoft_Windows_DotNETRuntimeRundown_158_1(Etw):
    pattern = Struct(
        "AppDomainID" / Int64ul,
        "AppDomainFlags" / Int32ul,
        "AppDomainName" / WString,
        "AppDomainIndex" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=159, version=0)
class Microsoft_Windows_DotNETRuntimeRundown_159_0(Etw):
    pattern = Struct(
        "ManagedThreadID" / Int64ul,
        "AppDomainID" / Int64ul,
        "Flags" / Int32ul,
        "ManagedThreadIndex" / Int32ul,
        "OSThreadID" / Int32ul,
        "ClrInstanceID" / Int16ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=160, version=0)
class Microsoft_Windows_DotNETRuntimeRundown_160_0(Etw):
    pattern = Struct(
        "ClrInstanceID" / Int16ul,
        "ModuleID" / Int64ul,
        "RangeBegin" / Int32ul,
        "RangeSize" / Int32ul,
        "RangeType" / Int8ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=161, version=0)
class Microsoft_Windows_DotNETRuntimeRundown_161_0(Etw):
    pattern = Struct(
        "ClrInstanceID" / Int16ul,
        "ModuleID" / Int64ul,
        "RangeBegin" / Int32ul,
        "RangeSize" / Int32ul,
        "RangeType" / Int8ul
    )


@declare(guid=guid("a669021c-c450-4609-a035-5af59af4df18"), event_id=187, version=0)
class Microsoft_Windows_DotNETRuntimeRundown_187_0(Etw):
    pattern = Struct(
        "ClrInstanceID" / Int16ul,
        "Sku" / Int16ul,
        "BclMajorVersion" / Int16ul,
        "BclMinorVersion" / Int16ul,
        "BclBuildNumber" / Int16ul,
        "BclQfeNumber" / Int16ul,
        "VMMajorVersion" / Int16ul,
        "VMMinorVersion" / Int16ul,
        "VMBuildNumber" / Int16ul,
        "VMQfeNumber" / Int16ul,
        "StartupFlags" / Int32ul,
        "StartupMode" / Int8ul,
        "CommandLine" / WString,
        "ComObjectGuid" / Guid,
        "RuntimeDllPath" / WString
    )

