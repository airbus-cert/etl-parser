# -*- coding: utf-8 -*-
"""
Microsoft-Windows-HomeGroup-ListenerService
GUID : af0a5a6d-e009-46d4-8867-42f2240f8a72
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("af0a5a6d-e009-46d4-8867-42f2240f8a72"), event_id=1000, version=0)
class Microsoft_Windows_HomeGroup_ListenerService_1000_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "Message" / WString
    )

