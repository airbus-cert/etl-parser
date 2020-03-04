# -*- coding: utf-8 -*-
"""
Microsoft-Windows-AuthenticationProvider
GUID : dddc1d91-51a1-4a8d-95b5-350c4ee3d809
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("dddc1d91-51a1-4a8d-95b5-350c4ee3d809"), event_id=101, version=0)
class Microsoft_Windows_AuthenticationProvider_101_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "UserName" / WString,
        "DomainName" / WString,
        "ServerName" / WString,
        "ProtectedUser" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("dddc1d91-51a1-4a8d-95b5-350c4ee3d809"), event_id=304, version=0)
class Microsoft_Windows_AuthenticationProvider_304_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "UserName" / WString,
        "DomainName" / WString,
        "ProtectedUser" / Int32ul
    )

