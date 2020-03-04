# -*- coding: utf-8 -*-
"""
Microsoft-Windows-OOBE-Machine-Plugins-Wireless
GUID : 0f352580-e9e2-46c2-8336-6ac66e986416
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("0f352580-e9e2-46c2-8336-6ac66e986416"), event_id=5111, version=0)
class Microsoft_Windows_OOBE_Machine_Plugins_Wireless_5111_0(Etw):
    pattern = Struct(
        "DWORD" / Int32ul
    )

