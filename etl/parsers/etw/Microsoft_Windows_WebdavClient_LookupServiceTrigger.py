# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WebdavClient-LookupServiceTrigger
GUID : 22b6d684-fa63-4578-87c9-effcbe6643c7
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("22b6d684-fa63-4578-87c9-effcbe6643c7"), event_id=1, version=0)
class Microsoft_Windows_WebdavClient_LookupServiceTrigger_1_0(Etw):
    pattern = Struct(
        "WebclntLookupServieTrigger" / Guid
    )

