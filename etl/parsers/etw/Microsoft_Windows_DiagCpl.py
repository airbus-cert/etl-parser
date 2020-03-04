# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DiagCpl
GUID : 1a396961-5f3c-4c71-8310-44c653c0bf8a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("1a396961-5f3c-4c71-8310-44c653c0bf8a"), event_id=1001, version=0)
class Microsoft_Windows_DiagCpl_1001_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "FileName" / CString,
        "Function" / CString,
        "Line" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("1a396961-5f3c-4c71-8310-44c653c0bf8a"), event_id=1002, version=0)
class Microsoft_Windows_DiagCpl_1002_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "FileName" / CString,
        "Function" / CString,
        "Line" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("1a396961-5f3c-4c71-8310-44c653c0bf8a"), event_id=1003, version=0)
class Microsoft_Windows_DiagCpl_1003_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "FileName" / CString,
        "Function" / CString,
        "Line" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("1a396961-5f3c-4c71-8310-44c653c0bf8a"), event_id=2001, version=0)
class Microsoft_Windows_DiagCpl_2001_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "Line" / Int32ul,
        "Address" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("1a396961-5f3c-4c71-8310-44c653c0bf8a"), event_id=2002, version=0)
class Microsoft_Windows_DiagCpl_2002_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "Line" / Int32ul,
        "Address" / Int64ul
    )


@declare(guid=guid("1a396961-5f3c-4c71-8310-44c653c0bf8a"), event_id=4000, version=0)
class Microsoft_Windows_DiagCpl_4000_0(Etw):
    pattern = Struct(
        "SearchOnline" / Int32ul,
        "SearchType" / Int32ul,
        "ExitCode" / Int32ul
    )


@declare(guid=guid("1a396961-5f3c-4c71-8310-44c653c0bf8a"), event_id=4001, version=0)
class Microsoft_Windows_DiagCpl_4001_0(Etw):
    pattern = Struct(
        "SearchOnline" / Int32ul,
        "SearchType" / Int32ul,
        "ExitCode" / Int32ul
    )

