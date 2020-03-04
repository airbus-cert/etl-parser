# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DirectSound
GUID : 8a93b54b-c75a-49b5-a5be-9060715b1a33
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("8a93b54b-c75a-49b5-a5be-9060715b1a33"), event_id=1, version=0)
class Microsoft_Windows_DirectSound_1_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "hrString" / WString
    )

