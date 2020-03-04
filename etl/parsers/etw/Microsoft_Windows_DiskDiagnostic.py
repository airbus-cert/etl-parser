# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DiskDiagnostic
GUID : e670a5a2-ce74-4ab4-9347-61b815319f4c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e670a5a2-ce74-4ab4-9347-61b815319f4c"), event_id=1, version=0)
class Microsoft_Windows_DiskDiagnostic_1_0(Etw):
    pattern = Struct(
        "DiskFriendlyName" / WString,
        "VolumeNames" / WString,
        "HardwareID" / WString
    )


@declare(guid=guid("e670a5a2-ce74-4ab4-9347-61b815319f4c"), event_id=4, version=0)
class Microsoft_Windows_DiskDiagnostic_4_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("e670a5a2-ce74-4ab4-9347-61b815319f4c"), event_id=5, version=0)
class Microsoft_Windows_DiskDiagnostic_5_0(Etw):
    pattern = Struct(
        "DiskFriendlyName" / WString,
        "VolumeNames" / WString,
        "HardwareID" / WString
    )


@declare(guid=guid("e670a5a2-ce74-4ab4-9347-61b815319f4c"), event_id=7, version=0)
class Microsoft_Windows_DiskDiagnostic_7_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )

