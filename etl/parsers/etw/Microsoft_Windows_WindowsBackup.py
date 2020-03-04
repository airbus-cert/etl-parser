# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WindowsBackup
GUID : 01979c6a-42fa-414c-b8aa-eee2c8202018
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("01979c6a-42fa-414c-b8aa-eee2c8202018"), event_id=100, version=0)
class Microsoft_Windows_WindowsBackup_100_0(Etw):
    pattern = Struct(
        "hc_stateid" / Int32ul,
        "pwszTimeStamp" / WString
    )


@declare(guid=guid("01979c6a-42fa-414c-b8aa-eee2c8202018"), event_id=101, version=0)
class Microsoft_Windows_WindowsBackup_101_0(Etw):
    pattern = Struct(
        "hc_stateid" / Int32ul
    )

