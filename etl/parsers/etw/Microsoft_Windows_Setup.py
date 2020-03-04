# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Setup
GUID : 75ebc33e-997f-49cf-b49f-ecc50184b75d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("75ebc33e-997f-49cf-b49f-ecc50184b75d"), event_id=1001, version=0)
class Microsoft_Windows_Setup_1001_0(Etw):
    pattern = Struct(
        "SetupPhase" / Int32ul
    )


@declare(guid=guid("75ebc33e-997f-49cf-b49f-ecc50184b75d"), event_id=1002, version=0)
class Microsoft_Windows_Setup_1002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("75ebc33e-997f-49cf-b49f-ecc50184b75d"), event_id=2002, version=0)
class Microsoft_Windows_Setup_2002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("75ebc33e-997f-49cf-b49f-ecc50184b75d"), event_id=2003, version=0)
class Microsoft_Windows_Setup_2003_0(Etw):
    pattern = Struct(
        "HostOSName" / WString,
        "Installwasanupgrade" / Int8ul,
        "HostOSwasWindowsPE" / Int8ul,
        "HostOSmajorversion" / Int32ul,
        "HostOSminorversion" / Int32ul,
        "HostOSbuildversion" / Int32ul,
        "HostOSservicepackName" / WString,
        "HostOSservicepackmajorversion" / Int32ul,
        "HostOSservicepackminorversion" / Int32ul
    )


@declare(guid=guid("75ebc33e-997f-49cf-b49f-ecc50184b75d"), event_id=2004, version=0)
class Microsoft_Windows_Setup_2004_0(Etw):
    pattern = Struct(
        "OSName" / WString,
        "OSEditionID" / WString,
        "OSmajorversion" / Int32ul,
        "OSminorversion" / Int32ul,
        "OSbuildversion" / Int32ul,
        "OSservicepackName" / WString,
        "OSservicepackmajorversion" / Int32ul,
        "OSservicepackminorversion" / Int32ul
    )

