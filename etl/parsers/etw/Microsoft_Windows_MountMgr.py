# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MountMgr
GUID : e3bac9f8-27be-4823-8d7f-1cc320c05fa7
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e3bac9f8-27be-4823-8d7f-1cc320c05fa7"), event_id=100, version=0)
class Microsoft_Windows_MountMgr_100_0(Etw):
    pattern = Struct(
        "CVEId" / WString
    )

