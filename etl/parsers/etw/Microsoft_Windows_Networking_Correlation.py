# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Networking-Correlation
GUID : 83ed54f0-4d48-4e45-b16e-726ffd1fa4af
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("83ed54f0-4d48-4e45-b16e-726ffd1fa4af"), event_id=60001, version=0)
class Microsoft_Windows_Networking_Correlation_60001_0(Etw):
    pattern = Struct(
        "SourceProvider" / Guid,
        "Context" / Int32ul
    )


@declare(guid=guid("83ed54f0-4d48-4e45-b16e-726ffd1fa4af"), event_id=60002, version=0)
class Microsoft_Windows_Networking_Correlation_60002_0(Etw):
    pattern = Struct(
        "SourceProvider" / Guid,
        "Context" / Int32ul
    )


@declare(guid=guid("83ed54f0-4d48-4e45-b16e-726ffd1fa4af"), event_id=60003, version=0)
class Microsoft_Windows_Networking_Correlation_60003_0(Etw):
    pattern = Struct(
        "SourceProvider" / Guid,
        "Context" / Int32ul
    )

