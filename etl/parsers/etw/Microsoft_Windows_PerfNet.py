# -*- coding: utf-8 -*-
"""
Microsoft-Windows-PerfNet
GUID : cab2b8a5-49b9-4eec-b1b0-fac21da05a3b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("cab2b8a5-49b9-4eec-b1b0-fac21da05a3b"), event_id=1000, version=1)
class Microsoft_Windows_PerfNet_1000_1(Etw):
    pattern = Struct(
        "Win32Error" / Int32ul
    )


@declare(guid=guid("cab2b8a5-49b9-4eec-b1b0-fac21da05a3b"), event_id=2000, version=1)
class Microsoft_Windows_PerfNet_2000_1(Etw):
    pattern = Struct(
        "Win32Error" / Int32ul
    )


@declare(guid=guid("cab2b8a5-49b9-4eec-b1b0-fac21da05a3b"), event_id=2001, version=1)
class Microsoft_Windows_PerfNet_2001_1(Etw):
    pattern = Struct(
        "Win32Error" / Int32ul
    )


@declare(guid=guid("cab2b8a5-49b9-4eec-b1b0-fac21da05a3b"), event_id=2001, version=2)
class Microsoft_Windows_PerfNet_2001_2(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("cab2b8a5-49b9-4eec-b1b0-fac21da05a3b"), event_id=2002, version=1)
class Microsoft_Windows_PerfNet_2002_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("cab2b8a5-49b9-4eec-b1b0-fac21da05a3b"), event_id=2003, version=1)
class Microsoft_Windows_PerfNet_2003_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("cab2b8a5-49b9-4eec-b1b0-fac21da05a3b"), event_id=2004, version=1)
class Microsoft_Windows_PerfNet_2004_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("cab2b8a5-49b9-4eec-b1b0-fac21da05a3b"), event_id=2005, version=1)
class Microsoft_Windows_PerfNet_2005_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul,
        "IOCompletionNTSTATUS" / Int32ul
    )


@declare(guid=guid("cab2b8a5-49b9-4eec-b1b0-fac21da05a3b"), event_id=2006, version=1)
class Microsoft_Windows_PerfNet_2006_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul,
        "IOCompletionNTSTATUS" / Int32ul
    )

