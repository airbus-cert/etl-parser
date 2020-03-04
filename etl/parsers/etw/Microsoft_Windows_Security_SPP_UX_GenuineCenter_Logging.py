# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Security-SPP-UX-GenuineCenter-Logging
GUID : fb829150-cd7d-44c3-af5b-711a3c31cedc
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("fb829150-cd7d-44c3-af5b-711a3c31cedc"), event_id=200, version=0)
class Microsoft_Windows_Security_SPP_UX_GenuineCenter_Logging_200_0(Etw):
    pattern = Struct(
        "shKernelCacheValues" / WString
    )


@declare(guid=guid("fb829150-cd7d-44c3-af5b-711a3c31cedc"), event_id=201, version=0)
class Microsoft_Windows_Security_SPP_UX_GenuineCenter_Logging_201_0(Etw):
    pattern = Struct(
        "shErrorCode" / WString
    )

