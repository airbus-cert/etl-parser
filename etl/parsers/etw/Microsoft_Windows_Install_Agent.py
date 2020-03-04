# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Install-Agent
GUID : e0c6f6de-258a-50e0-ac1a-103482d118bc
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e0c6f6de-258a-50e0-ac1a-103482d118bc"), event_id=2000, version=0)
class Microsoft_Windows_Install_Agent_2000_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "ModuleName" / WString,
        "BuildName" / WString
    )


@declare(guid=guid("e0c6f6de-258a-50e0-ac1a-103482d118bc"), event_id=2001, version=0)
class Microsoft_Windows_Install_Agent_2001_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("e0c6f6de-258a-50e0-ac1a-103482d118bc"), event_id=2002, version=0)
class Microsoft_Windows_Install_Agent_2002_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("e0c6f6de-258a-50e0-ac1a-103482d118bc"), event_id=2003, version=0)
class Microsoft_Windows_Install_Agent_2003_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("e0c6f6de-258a-50e0-ac1a-103482d118bc"), event_id=2004, version=0)
class Microsoft_Windows_Install_Agent_2004_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("e0c6f6de-258a-50e0-ac1a-103482d118bc"), event_id=2005, version=0)
class Microsoft_Windows_Install_Agent_2005_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul,
        "CorrelationVector" / CString,
        "ProductId" / WString
    )


@declare(guid=guid("e0c6f6de-258a-50e0-ac1a-103482d118bc"), event_id=2006, version=0)
class Microsoft_Windows_Install_Agent_2006_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul,
        "CorrelationVector" / CString,
        "ProductId" / WString
    )


@declare(guid=guid("e0c6f6de-258a-50e0-ac1a-103482d118bc"), event_id=2007, version=0)
class Microsoft_Windows_Install_Agent_2007_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul,
        "CorrelationVector" / CString,
        "ProductId" / WString
    )


@declare(guid=guid("e0c6f6de-258a-50e0-ac1a-103482d118bc"), event_id=2008, version=0)
class Microsoft_Windows_Install_Agent_2008_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul,
        "CorrelationVector" / CString,
        "ProductId" / WString
    )

