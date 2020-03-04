# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Subsys-SMSS
GUID : 43e63da5-41d1-4fbf-aded-1bbed98fdd1d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("43e63da5-41d1-4fbf-aded-1bbed98fdd1d"), event_id=1, version=0)
class Microsoft_Windows_Subsys_SMSS_1_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "ImageNameLength" / Int16ul,
        "ImageName" / Bytes(lambda this: this.ImageNameLength)
    )


@declare(guid=guid("43e63da5-41d1-4fbf-aded-1bbed98fdd1d"), event_id=2, version=0)
class Microsoft_Windows_Subsys_SMSS_2_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul
    )


@declare(guid=guid("43e63da5-41d1-4fbf-aded-1bbed98fdd1d"), event_id=11, version=0)
class Microsoft_Windows_Subsys_SMSS_11_0(Etw):
    pattern = Struct(
        "FromNameLength" / Int16ul,
        "ToNameLength" / Int16ul,
        "FromName" / Bytes(lambda this: this.FromNameLength),
        "ToName" / Bytes(lambda this: this.ToNameLength)
    )


@declare(guid=guid("43e63da5-41d1-4fbf-aded-1bbed98fdd1d"), event_id=12, version=0)
class Microsoft_Windows_Subsys_SMSS_12_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("43e63da5-41d1-4fbf-aded-1bbed98fdd1d"), event_id=13, version=0)
class Microsoft_Windows_Subsys_SMSS_13_0(Etw):
    pattern = Struct(
        "CurrentRunLevel" / WString,
        "TargetRunLevel" / WString
    )


@declare(guid=guid("43e63da5-41d1-4fbf-aded-1bbed98fdd1d"), event_id=14, version=0)
class Microsoft_Windows_Subsys_SMSS_14_0(Etw):
    pattern = Struct(
        "CurrentRunLevel" / WString,
        "TargetRunLevel" / WString
    )


@declare(guid=guid("43e63da5-41d1-4fbf-aded-1bbed98fdd1d"), event_id=15, version=0)
class Microsoft_Windows_Subsys_SMSS_15_0(Etw):
    pattern = Struct(
        "CurrentRunLevel" / WString,
        "TargetRunLevel" / WString,
        "AgentName" / WString,
        "Error" / WString
    )


@declare(guid=guid("43e63da5-41d1-4fbf-aded-1bbed98fdd1d"), event_id=16, version=0)
class Microsoft_Windows_Subsys_SMSS_16_0(Etw):
    pattern = Struct(
        "CurrentRunLevel" / WString,
        "TargetRunLevel" / WString,
        "AgentName" / WString,
        "Error" / WString
    )


@declare(guid=guid("43e63da5-41d1-4fbf-aded-1bbed98fdd1d"), event_id=18, version=0)
class Microsoft_Windows_Subsys_SMSS_18_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("43e63da5-41d1-4fbf-aded-1bbed98fdd1d"), event_id=22, version=0)
class Microsoft_Windows_Subsys_SMSS_22_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("43e63da5-41d1-4fbf-aded-1bbed98fdd1d"), event_id=23, version=0)
class Microsoft_Windows_Subsys_SMSS_23_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "ImageNameLength" / Int16ul,
        "ImageName" / Bytes(lambda this: this.ImageNameLength)
    )


@declare(guid=guid("43e63da5-41d1-4fbf-aded-1bbed98fdd1d"), event_id=24, version=0)
class Microsoft_Windows_Subsys_SMSS_24_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("43e63da5-41d1-4fbf-aded-1bbed98fdd1d"), event_id=26, version=0)
class Microsoft_Windows_Subsys_SMSS_26_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )

