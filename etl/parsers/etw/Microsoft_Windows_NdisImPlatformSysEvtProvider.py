# -*- coding: utf-8 -*-
"""
Microsoft-Windows-NdisImPlatformSysEvtProvider
GUID : 62de9e48-90c6-4755-8813-6a7d655b0802
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("62de9e48-90c6-4755-8813-6a7d655b0802"), event_id=16993, version=0)
class Microsoft_Windows_NdisImPlatformSysEvtProvider_16993_0(Etw):
    pattern = Struct(
        "Team" / WString,
        "Status" / WString
    )


@declare(guid=guid("62de9e48-90c6-4755-8813-6a7d655b0802"), event_id=16994, version=0)
class Microsoft_Windows_NdisImPlatformSysEvtProvider_16994_0(Etw):
    pattern = Struct(
        "Member" / WString,
        "Status" / WString
    )


@declare(guid=guid("62de9e48-90c6-4755-8813-6a7d655b0802"), event_id=16995, version=0)
class Microsoft_Windows_NdisImPlatformSysEvtProvider_16995_0(Etw):
    pattern = Struct(
        "TeamNic" / WString,
        "Status" / WString
    )


@declare(guid=guid("62de9e48-90c6-4755-8813-6a7d655b0802"), event_id=16996, version=0)
class Microsoft_Windows_NdisImPlatformSysEvtProvider_16996_0(Etw):
    pattern = Struct(
        "TeamNic" / WString,
        "Team" / WString,
        "Status" / WString
    )


@declare(guid=guid("62de9e48-90c6-4755-8813-6a7d655b0802"), event_id=16997, version=0)
class Microsoft_Windows_NdisImPlatformSysEvtProvider_16997_0(Etw):
    pattern = Struct(
        "Member" / WString,
        "TeamNic" / WString,
        "Status" / WString
    )


@declare(guid=guid("62de9e48-90c6-4755-8813-6a7d655b0802"), event_id=16998, version=0)
class Microsoft_Windows_NdisImPlatformSysEvtProvider_16998_0(Etw):
    pattern = Struct(
        "Member" / WString,
        "TeamNic" / WString,
        "Status" / WString
    )


@declare(guid=guid("62de9e48-90c6-4755-8813-6a7d655b0802"), event_id=16999, version=0)
class Microsoft_Windows_NdisImPlatformSysEvtProvider_16999_0(Etw):
    pattern = Struct(
        "Status" / WString
    )

