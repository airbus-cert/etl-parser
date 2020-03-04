# -*- coding: utf-8 -*-
"""
Microsoft-Windows-CDROM
GUID : 9b6123dc-9af6-4430-80d7-7d36f054fb9f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9b6123dc-9af6-4430-80d7-7d36f054fb9f"), event_id=100, version=0)
class Microsoft_Windows_CDROM_100_0(Etw):
    pattern = Struct(
        "DeviceName" / WString
    )

