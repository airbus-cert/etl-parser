# -*- coding: utf-8 -*-
"""
Microsoft-Windows-PerfProc
GUID : 72d211e1-4c54-4a93-9520-4901681b2271
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("72d211e1-4c54-4a93-9520-4901681b2271"), event_id=2001, version=1)
class Microsoft_Windows_PerfProc_2001_1(Etw):
    pattern = Struct(
        "Win32Error" / Int32ul
    )


@declare(guid=guid("72d211e1-4c54-4a93-9520-4901681b2271"), event_id=2002, version=1)
class Microsoft_Windows_PerfProc_2002_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("72d211e1-4c54-4a93-9520-4901681b2271"), event_id=2003, version=1)
class Microsoft_Windows_PerfProc_2003_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("72d211e1-4c54-4a93-9520-4901681b2271"), event_id=2004, version=1)
class Microsoft_Windows_PerfProc_2004_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("72d211e1-4c54-4a93-9520-4901681b2271"), event_id=2005, version=1)
class Microsoft_Windows_PerfProc_2005_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("72d211e1-4c54-4a93-9520-4901681b2271"), event_id=8192, version=1)
class Microsoft_Windows_PerfProc_8192_1(Etw):
    pattern = Struct(
        "Win32Error" / Int32ul
    )

