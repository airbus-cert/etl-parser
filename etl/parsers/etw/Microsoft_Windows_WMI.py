# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WMI
GUID : 1edeee53-0afe-4609-b846-d8c0b2075b1f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("1edeee53-0afe-4609-b846-d8c0b2075b1f"), event_id=67, version=0)
class Microsoft_Windows_WMI_67_0(Etw):
    pattern = Struct(
        "BackupFile" / WString
    )


@declare(guid=guid("1edeee53-0afe-4609-b846-d8c0b2075b1f"), event_id=68, version=0)
class Microsoft_Windows_WMI_68_0(Etw):
    pattern = Struct(
        "BackupFile" / WString,
        "Error" / WString
    )

