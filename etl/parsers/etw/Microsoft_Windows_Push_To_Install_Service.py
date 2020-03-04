# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Push-To-Install-Service
GUID : 3a718a68-6974-4075-abd3-e8243caef398
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3a718a68-6974-4075-abd3-e8243caef398"), event_id=6001, version=0)
class Microsoft_Windows_Push_To_Install_Service_6001_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3a718a68-6974-4075-abd3-e8243caef398"), event_id=6002, version=0)
class Microsoft_Windows_Push_To_Install_Service_6002_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "LineNumber" / Int32ul,
        "FileName" / WString,
        "Function" / WString,
        "ExceptionDetails" / WString
    )


@declare(guid=guid("3a718a68-6974-4075-abd3-e8243caef398"), event_id=6003, version=0)
class Microsoft_Windows_Push_To_Install_Service_6003_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3a718a68-6974-4075-abd3-e8243caef398"), event_id=6004, version=0)
class Microsoft_Windows_Push_To_Install_Service_6004_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3a718a68-6974-4075-abd3-e8243caef398"), event_id=6005, version=0)
class Microsoft_Windows_Push_To_Install_Service_6005_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3a718a68-6974-4075-abd3-e8243caef398"), event_id=6006, version=0)
class Microsoft_Windows_Push_To_Install_Service_6006_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "ModuleName" / WString,
        "BuildName" / WString
    )

