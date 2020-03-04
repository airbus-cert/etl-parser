# -*- coding: utf-8 -*-
"""
Microsoft-Windows-EDP-AppLearning
GUID : 9803daa0-81ba-483a-986c-f0e395b9f8d1
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9803daa0-81ba-483a-986c-f0e395b9f8d1"), event_id=401, version=0)
class Microsoft_Windows_EDP_AppLearning_401_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "Action" / Int32ul,
        "IdType" / Int32ul
    )


@declare(guid=guid("9803daa0-81ba-483a-986c-f0e395b9f8d1"), event_id=402, version=0)
class Microsoft_Windows_EDP_AppLearning_402_0(Etw):
    pattern = Struct(
        "WebSite" / WString
    )

