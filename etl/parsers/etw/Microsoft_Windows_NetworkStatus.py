# -*- coding: utf-8 -*-
"""
Microsoft-Windows-NetworkStatus
GUID : 7868b0d4-1423-4681-afdf-27913575441e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7868b0d4-1423-4681-afdf-27913575441e"), event_id=8001, version=0)
class Microsoft_Windows_NetworkStatus_8001_0(Etw):
    pattern = Struct(
        "NetworkStatus" / Int32ul
    )

