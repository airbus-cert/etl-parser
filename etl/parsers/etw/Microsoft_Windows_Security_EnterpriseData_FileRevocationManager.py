# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Security-EnterpriseData-FileRevocationManager
GUID : 2cd58181-0bb6-463e-828a-056ff837f966
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("2cd58181-0bb6-463e-828a-056ff837f966"), event_id=0, version=0)
class Microsoft_Windows_Security_EnterpriseData_FileRevocationManager_0_0(Etw):
    pattern = Struct(
        "EntIDString" / WString,
        "AppIDString" / WString
    )


@declare(guid=guid("2cd58181-0bb6-463e-828a-056ff837f966"), event_id=1, version=0)
class Microsoft_Windows_Security_EnterpriseData_FileRevocationManager_1_0(Etw):
    pattern = Struct(
        "EntIDString" / WString,
        "AppIDString" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("2cd58181-0bb6-463e-828a-056ff837f966"), event_id=17, version=0)
class Microsoft_Windows_Security_EnterpriseData_FileRevocationManager_17_0(Etw):
    pattern = Struct(
        "EntIDString" / WString,
        "AppIDString" / WString
    )


@declare(guid=guid("2cd58181-0bb6-463e-828a-056ff837f966"), event_id=18, version=0)
class Microsoft_Windows_Security_EnterpriseData_FileRevocationManager_18_0(Etw):
    pattern = Struct(
        "EntIDString" / WString,
        "AppIDString" / WString
    )


@declare(guid=guid("2cd58181-0bb6-463e-828a-056ff837f966"), event_id=19, version=0)
class Microsoft_Windows_Security_EnterpriseData_FileRevocationManager_19_0(Etw):
    pattern = Struct(
        "EntIDString" / WString,
        "AppIDString" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("2cd58181-0bb6-463e-828a-056ff837f966"), event_id=20, version=0)
class Microsoft_Windows_Security_EnterpriseData_FileRevocationManager_20_0(Etw):
    pattern = Struct(
        "PolicyString" / WString
    )

