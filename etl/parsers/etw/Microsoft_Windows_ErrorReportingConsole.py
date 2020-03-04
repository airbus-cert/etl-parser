# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ErrorReportingConsole
GUID : 017247f2-7e96-11dc-8314-0800200c9a66
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("017247f2-7e96-11dc-8314-0800200c9a66"), event_id=103, version=0)
class Microsoft_Windows_ErrorReportingConsole_103_0(Etw):
    pattern = Struct(
        "ResponseId" / Int32ul
    )


@declare(guid=guid("017247f2-7e96-11dc-8314-0800200c9a66"), event_id=104, version=0)
class Microsoft_Windows_ErrorReportingConsole_104_0(Etw):
    pattern = Struct(
        "ResponseId" / Int32ul
    )


@declare(guid=guid("017247f2-7e96-11dc-8314-0800200c9a66"), event_id=105, version=0)
class Microsoft_Windows_ErrorReportingConsole_105_0(Etw):
    pattern = Struct(
        "PageId" / Int32ul
    )


@declare(guid=guid("017247f2-7e96-11dc-8314-0800200c9a66"), event_id=106, version=0)
class Microsoft_Windows_ErrorReportingConsole_106_0(Etw):
    pattern = Struct(
        "PageId" / Int32ul
    )

