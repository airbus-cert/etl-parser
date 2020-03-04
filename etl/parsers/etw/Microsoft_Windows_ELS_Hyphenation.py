# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ELS-Hyphenation
GUID : 51aedb05-890b-4ade-8ba1-0ba14b8e8973
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("51aedb05-890b-4ade-8ba1-0ba14b8e8973"), event_id=11, version=0)
class Microsoft_Windows_ELS_Hyphenation_11_0(Etw):
    pattern = Struct(
        "String" / WString
    )

