# -*- coding: utf-8 -*-
"""
Error Instrument
GUID : cd7cf0d0-02cc-4872-9b65-0dba0a90efe8
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("cd7cf0d0-02cc-4872-9b65-0dba0a90efe8"), event_id=1072, version=0)
class Error_Instrument_1072_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "WindowTitle" / WString,
        "MsgCaption" / WString,
        "MsgText" / WString,
        "CallerModuleName" / WString,
        "BaseAddress" / Int64ul,
        "ImageSize" / Int32ul,
        "ReturnAddress" / Int64ul,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )

