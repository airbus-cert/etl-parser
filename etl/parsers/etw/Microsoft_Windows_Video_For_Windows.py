# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Video-For-Windows
GUID : 712abb2d-d806-4b42-9682-26da01d8b307
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("712abb2d-d806-4b42-9682-26da01d8b307"), event_id=1, version=0)
class Microsoft_Windows_Video_For_Windows_1_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "FileName" / WString,
        "ContentType" / WString
    )

