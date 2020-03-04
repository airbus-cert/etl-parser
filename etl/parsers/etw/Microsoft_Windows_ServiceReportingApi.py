# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ServiceReportingApi
GUID : 606a6a38-70ec-4309-b3a3-82ff86f73329
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("606a6a38-70ec-4309-b3a3-82ff86f73329"), event_id=1, version=0)
class Microsoft_Windows_ServiceReportingApi_1_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "FunctionName" / WString,
        "LineNumber" / Int32sl,
        "DebugMessage" / WString
    )

