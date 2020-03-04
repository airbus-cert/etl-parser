# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Security-ExchangeActiveSyncProvisioning
GUID : 9249d0d0-f034-402f-a29b-92fa8853d9f3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9249d0d0-f034-402f-a29b-92fa8853d9f3"), event_id=1, version=0)
class Microsoft_Windows_Security_ExchangeActiveSyncProvisioning_1_0(Etw):
    pattern = Struct(
        "DllPath" / WString
    )


@declare(guid=guid("9249d0d0-f034-402f-a29b-92fa8853d9f3"), event_id=2, version=0)
class Microsoft_Windows_Security_ExchangeActiveSyncProvisioning_2_0(Etw):
    pattern = Struct(
        "DllPath" / WString
    )


@declare(guid=guid("9249d0d0-f034-402f-a29b-92fa8853d9f3"), event_id=101, version=0)
class Microsoft_Windows_Security_ExchangeActiveSyncProvisioning_101_0(Etw):
    pattern = Struct(
        "TimeSpent" / Int32ul
    )

