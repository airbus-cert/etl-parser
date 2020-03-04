# -*- coding: utf-8 -*-
"""
Microsoft-Windows-VerifyHardwareSecurity
GUID : f3f53c76-b06d-4f15-b412-61164a0d2b73
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f3f53c76-b06d-4f15-b412-61164a0d2b73"), event_id=3001, version=0)
class Microsoft_Windows_VerifyHardwareSecurity_3001_0(Etw):
    pattern = Struct(
        "CurrentCheckBit" / Int32ul
    )


@declare(guid=guid("f3f53c76-b06d-4f15-b412-61164a0d2b73"), event_id=3003, version=0)
class Microsoft_Windows_VerifyHardwareSecurity_3003_0(Etw):
    pattern = Struct(
        "hr" / Int32sl
    )


@declare(guid=guid("f3f53c76-b06d-4f15-b412-61164a0d2b73"), event_id=3004, version=0)
class Microsoft_Windows_VerifyHardwareSecurity_3004_0(Etw):
    pattern = Struct(
        "name" / WString,
        "database" / WString
    )


@declare(guid=guid("f3f53c76-b06d-4f15-b412-61164a0d2b73"), event_id=3005, version=0)
class Microsoft_Windows_VerifyHardwareSecurity_3005_0(Etw):
    pattern = Struct(
        "hr" / Int32sl
    )


@declare(guid=guid("f3f53c76-b06d-4f15-b412-61164a0d2b73"), event_id=3007, version=0)
class Microsoft_Windows_VerifyHardwareSecurity_3007_0(Etw):
    pattern = Struct(
        "hr" / Int32sl
    )


@declare(guid=guid("f3f53c76-b06d-4f15-b412-61164a0d2b73"), event_id=3008, version=0)
class Microsoft_Windows_VerifyHardwareSecurity_3008_0(Etw):
    pattern = Struct(
        "HostProvider" / WString,
        "ModulePath" / WString,
        "Method" / WString,
        "InternalName" / WString
    )


@declare(guid=guid("f3f53c76-b06d-4f15-b412-61164a0d2b73"), event_id=3009, version=0)
class Microsoft_Windows_VerifyHardwareSecurity_3009_0(Etw):
    pattern = Struct(
        "HostProvider" / WString,
        "ModulePath" / WString,
        "Method" / WString,
        "InternalName" / WString,
        "hr" / Int32sl
    )


@declare(guid=guid("f3f53c76-b06d-4f15-b412-61164a0d2b73"), event_id=3010, version=0)
class Microsoft_Windows_VerifyHardwareSecurity_3010_0(Etw):
    pattern = Struct(
        "HostProvider" / WString,
        "ModulePath" / WString,
        "Method" / WString,
        "InternalName" / WString
    )


@declare(guid=guid("f3f53c76-b06d-4f15-b412-61164a0d2b73"), event_id=3011, version=0)
class Microsoft_Windows_VerifyHardwareSecurity_3011_0(Etw):
    pattern = Struct(
        "HostProvider" / WString,
        "ModulePath" / WString,
        "Method" / WString,
        "hr" / Int32sl
    )


@declare(guid=guid("f3f53c76-b06d-4f15-b412-61164a0d2b73"), event_id=3012, version=0)
class Microsoft_Windows_VerifyHardwareSecurity_3012_0(Etw):
    pattern = Struct(
        "HostProvider" / WString,
        "ModulePath" / WString,
        "Method" / WString,
        "InternalName" / WString
    )


@declare(guid=guid("f3f53c76-b06d-4f15-b412-61164a0d2b73"), event_id=3013, version=0)
class Microsoft_Windows_VerifyHardwareSecurity_3013_0(Etw):
    pattern = Struct(
        "HostProvider" / WString,
        "ModulePath" / WString,
        "Method" / WString,
        "InternalName" / WString
    )

