# -*- coding: utf-8 -*-
"""
Microsoft-Windows-PerfDisk
GUID : 7f9d83de-8abb-457f-98e8-4ad161449ecc
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7f9d83de-8abb-457f-98e8-4ad161449ecc"), event_id=1000, version=1)
class Microsoft_Windows_PerfDisk_1000_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("7f9d83de-8abb-457f-98e8-4ad161449ecc"), event_id=2000, version=1)
class Microsoft_Windows_PerfDisk_2000_1(Etw):
    pattern = Struct(
        "Win32Error" / Int32ul
    )


@declare(guid=guid("7f9d83de-8abb-457f-98e8-4ad161449ecc"), event_id=2001, version=1)
class Microsoft_Windows_PerfDisk_2001_1(Etw):
    pattern = Struct(
        "Win32Error" / Int32ul
    )

