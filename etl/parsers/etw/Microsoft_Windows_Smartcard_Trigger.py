# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Smartcard-Trigger
GUID : aedd909f-41c6-401a-9e41-dfc33006af5d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("aedd909f-41c6-401a-9e41-dfc33006af5d"), event_id=1000, version=0)
class Microsoft_Windows_Smartcard_Trigger_1000_0(Etw):
    pattern = Struct(
        "ScDeviceEnumGuid" / Guid
    )

