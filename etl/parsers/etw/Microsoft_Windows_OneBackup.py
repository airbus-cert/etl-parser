# -*- coding: utf-8 -*-
"""
Microsoft-Windows-OneBackup
GUID : 72561cf0-c85c-4f78-9e8d-cba9093df62d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("72561cf0-c85c-4f78-9e8d-cba9093df62d"), event_id=1000, version=0)
class Microsoft_Windows_OneBackup_1000_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("72561cf0-c85c-4f78-9e8d-cba9093df62d"), event_id=1001, version=0)
class Microsoft_Windows_OneBackup_1001_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("72561cf0-c85c-4f78-9e8d-cba9093df62d"), event_id=1002, version=0)
class Microsoft_Windows_OneBackup_1002_0(Etw):
    pattern = Struct(
        "Message" / WString
    )

