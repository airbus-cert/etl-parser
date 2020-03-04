# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WinINet-Config
GUID : 5402e5ea-1bdd-4390-82be-e108f1e634f5
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5402e5ea-1bdd-4390-82be-e108f1e634f5"), event_id=5600, version=0)
class Microsoft_Windows_WinINet_Config_5600_0(Etw):
    pattern = Struct(
        "fAutoDetect" / Int8ul,
        "pwszAutoConfigUrl" / WString,
        "pwszProxy" / WString,
        "pwszProxyBypass" / WString
    )

