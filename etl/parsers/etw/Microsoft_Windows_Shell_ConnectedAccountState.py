# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Shell-ConnectedAccountState
GUID : 6df57621-e7e4-410f-a7e9-e43eeb61b11f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6df57621-e7e4-410f-a7e9-e43eeb61b11f"), event_id=100, version=0)
class Microsoft_Windows_Shell_ConnectedAccountState_100_0(Etw):
    pattern = Struct(
        "hc_stateid" / Int32ul
    )

