# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-LiveDump
GUID : bef2aa8e-81cd-11e2-a7bb-5eac6188709b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("bef2aa8e-81cd-11e2-a7bb-5eac6188709b"), event_id=2, version=0)
class Microsoft_Windows_Kernel_LiveDump_2_0(Etw):
    pattern = Struct(
        "NTStatus" / Int32ul
    )


@declare(guid=guid("bef2aa8e-81cd-11e2-a7bb-5eac6188709b"), event_id=4, version=0)
class Microsoft_Windows_Kernel_LiveDump_4_0(Etw):
    pattern = Struct(
        "NTStatus" / Int32ul,
        "TotalBytes" / Int64ul,
        "HeaderBytes" / Int64ul,
        "PrimaryDataBytes" / Int64ul,
        "SecondaryDataBytes" / Int64ul
    )


@declare(guid=guid("bef2aa8e-81cd-11e2-a7bb-5eac6188709b"), event_id=106, version=0)
class Microsoft_Windows_Kernel_LiveDump_106_0(Etw):
    pattern = Struct(
        "NtEstimatedRequiredPrimaryDataBytes" / Int64ul,
        "NtEstimatedPrimaryDataBytes" / Int64ul,
        "HvEstimatedPrimaryDataBytes" / Int64ul,
        "HvEstimatedSecondaryDataBytes" / Int64ul
    )


@declare(guid=guid("bef2aa8e-81cd-11e2-a7bb-5eac6188709b"), event_id=107, version=0)
class Microsoft_Windows_Kernel_LiveDump_107_0(Etw):
    pattern = Struct(
        "NtPrimaryDataBytes" / Int64ul,
        "HvPrimaryDataBytes" / Int64ul,
        "HvSecondaryDataBytes" / Int64ul
    )


@declare(guid=guid("bef2aa8e-81cd-11e2-a7bb-5eac6188709b"), event_id=110, version=0)
class Microsoft_Windows_Kernel_LiveDump_110_0(Etw):
    pattern = Struct(
        "CallbackIdentifier" / CString
    )


@declare(guid=guid("bef2aa8e-81cd-11e2-a7bb-5eac6188709b"), event_id=111, version=0)
class Microsoft_Windows_Kernel_LiveDump_111_0(Etw):
    pattern = Struct(
        "CallbackIdentifier" / CString
    )


@declare(guid=guid("bef2aa8e-81cd-11e2-a7bb-5eac6188709b"), event_id=112, version=0)
class Microsoft_Windows_Kernel_LiveDump_112_0(Etw):
    pattern = Struct(
        "CallbackIdentifier" / CString,
        "NTStatus" / Int32ul
    )


@declare(guid=guid("bef2aa8e-81cd-11e2-a7bb-5eac6188709b"), event_id=202, version=0)
class Microsoft_Windows_Kernel_LiveDump_202_0(Etw):
    pattern = Struct(
        "NTStatus" / Int32ul
    )


@declare(guid=guid("bef2aa8e-81cd-11e2-a7bb-5eac6188709b"), event_id=204, version=0)
class Microsoft_Windows_Kernel_LiveDump_204_0(Etw):
    pattern = Struct(
        "NTStatus" / Int32ul,
        "TotalBytes" / Int64ul,
        "HeaderBytes" / Int64ul,
        "PrimaryDataBytes" / Int64ul,
        "SecondaryDataBytes" / Int64ul
    )


@declare(guid=guid("bef2aa8e-81cd-11e2-a7bb-5eac6188709b"), event_id=252, version=0)
class Microsoft_Windows_Kernel_LiveDump_252_0(Etw):
    pattern = Struct(
        "NTStatus" / Int32ul
    )

