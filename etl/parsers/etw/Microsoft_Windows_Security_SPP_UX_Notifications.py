# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Security-SPP-UX-Notifications
GUID : c4efc9bb-2570-4821-8923-1bad317d2d4b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c4efc9bb-2570-4821-8923-1bad317d2d4b"), event_id=100, version=0)
class Microsoft_Windows_Security_SPP_UX_Notifications_100_0(Etw):
    pattern = Struct(
        "hc_stateid" / Int32ul
    )

