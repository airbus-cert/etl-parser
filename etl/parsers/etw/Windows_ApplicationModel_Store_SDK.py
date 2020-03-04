# -*- coding: utf-8 -*-
"""
Windows-ApplicationModel-Store-SDK
GUID : ff79a477-c45f-4a52-8ae0-2b324346d4e4
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ff79a477-c45f-4a52-8ae0-2b324346d4e4"), event_id=1, version=0)
class Windows_ApplicationModel_Store_SDK_1_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "LineNumber" / Int32ul,
        "FileName" / WString,
        "Function" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("ff79a477-c45f-4a52-8ae0-2b324346d4e4"), event_id=2, version=0)
class Windows_ApplicationModel_Store_SDK_2_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "LineNumber" / Int32ul,
        "FileName" / WString,
        "Function" / WString,
        "ExceptionDetails" / WString
    )


@declare(guid=guid("ff79a477-c45f-4a52-8ae0-2b324346d4e4"), event_id=3, version=0)
class Windows_ApplicationModel_Store_SDK_3_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "LineNumber" / Int32ul,
        "FileName" / WString,
        "MemberName" / WString
    )


@declare(guid=guid("ff79a477-c45f-4a52-8ae0-2b324346d4e4"), event_id=4, version=0)
class Windows_ApplicationModel_Store_SDK_4_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "LineNumber" / Int32ul,
        "FileName" / WString,
        "MemberName" / WString
    )


@declare(guid=guid("ff79a477-c45f-4a52-8ae0-2b324346d4e4"), event_id=5, version=0)
class Windows_ApplicationModel_Store_SDK_5_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "LineNumber" / Int32ul,
        "FileName" / WString,
        "MemberName" / WString
    )


@declare(guid=guid("ff79a477-c45f-4a52-8ae0-2b324346d4e4"), event_id=2000, version=0)
class Windows_ApplicationModel_Store_SDK_2000_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "ModuleName" / WString,
        "BuildName" / WString
    )


@declare(guid=guid("ff79a477-c45f-4a52-8ae0-2b324346d4e4"), event_id=2001, version=0)
class Windows_ApplicationModel_Store_SDK_2001_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("ff79a477-c45f-4a52-8ae0-2b324346d4e4"), event_id=2002, version=0)
class Windows_ApplicationModel_Store_SDK_2002_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("ff79a477-c45f-4a52-8ae0-2b324346d4e4"), event_id=2003, version=0)
class Windows_ApplicationModel_Store_SDK_2003_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("ff79a477-c45f-4a52-8ae0-2b324346d4e4"), event_id=2004, version=0)
class Windows_ApplicationModel_Store_SDK_2004_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("ff79a477-c45f-4a52-8ae0-2b324346d4e4"), event_id=3001, version=0)
class Windows_ApplicationModel_Store_SDK_3001_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("ff79a477-c45f-4a52-8ae0-2b324346d4e4"), event_id=3002, version=0)
class Windows_ApplicationModel_Store_SDK_3002_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("ff79a477-c45f-4a52-8ae0-2b324346d4e4"), event_id=3003, version=0)
class Windows_ApplicationModel_Store_SDK_3003_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("ff79a477-c45f-4a52-8ae0-2b324346d4e4"), event_id=3004, version=0)
class Windows_ApplicationModel_Store_SDK_3004_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Function" / CString,
        "ErrorCode" / Int32sl,
        "Source" / CString,
        "LineNumber" / Int32ul
    )

