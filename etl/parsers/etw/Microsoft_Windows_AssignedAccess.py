# -*- coding: utf-8 -*-
"""
Microsoft-Windows-AssignedAccess
GUID : 8530db6e-51c0-43d6-9d02-a8c2088526cd
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("8530db6e-51c0-43d6-9d02-a8c2088526cd"), event_id=10001, version=0)
class Microsoft_Windows_AssignedAccess_10001_0(Etw):
    pattern = Struct(
        "SID" / WString
    )


@declare(guid=guid("8530db6e-51c0-43d6-9d02-a8c2088526cd"), event_id=10002, version=0)
class Microsoft_Windows_AssignedAccess_10002_0(Etw):
    pattern = Struct(
        "SID" / WString
    )


@declare(guid=guid("8530db6e-51c0-43d6-9d02-a8c2088526cd"), event_id=10003, version=0)
class Microsoft_Windows_AssignedAccess_10003_0(Etw):
    pattern = Struct(
        "SID" / WString
    )


@declare(guid=guid("8530db6e-51c0-43d6-9d02-a8c2088526cd"), event_id=10004, version=0)
class Microsoft_Windows_AssignedAccess_10004_0(Etw):
    pattern = Struct(
        "AppID" / WString
    )


@declare(guid=guid("8530db6e-51c0-43d6-9d02-a8c2088526cd"), event_id=10010, version=0)
class Microsoft_Windows_AssignedAccess_10010_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8530db6e-51c0-43d6-9d02-a8c2088526cd"), event_id=10020, version=0)
class Microsoft_Windows_AssignedAccess_10020_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8530db6e-51c0-43d6-9d02-a8c2088526cd"), event_id=20000, version=0)
class Microsoft_Windows_AssignedAccess_20000_0(Etw):
    pattern = Struct(
        "SID" / WString,
        "UserName" / WString,
        "AppID" / WString,
        "AppName" / WString
    )


@declare(guid=guid("8530db6e-51c0-43d6-9d02-a8c2088526cd"), event_id=30000, version=0)
class Microsoft_Windows_AssignedAccess_30000_0(Etw):
    pattern = Struct(
        "File" / CString,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul,
        "ErrorCodeExpanded" / Int32sl
    )


@declare(guid=guid("8530db6e-51c0-43d6-9d02-a8c2088526cd"), event_id=31000, version=0)
class Microsoft_Windows_AssignedAccess_31000_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("8530db6e-51c0-43d6-9d02-a8c2088526cd"), event_id=31001, version=0)
class Microsoft_Windows_AssignedAccess_31001_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("8530db6e-51c0-43d6-9d02-a8c2088526cd"), event_id=31002, version=0)
class Microsoft_Windows_AssignedAccess_31002_0(Etw):
    pattern = Struct(
        "Custom" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8530db6e-51c0-43d6-9d02-a8c2088526cd"), event_id=32000, version=0)
class Microsoft_Windows_AssignedAccess_32000_0(Etw):
    pattern = Struct(
        "Custom" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8530db6e-51c0-43d6-9d02-a8c2088526cd"), event_id=33000, version=0)
class Microsoft_Windows_AssignedAccess_33000_0(Etw):
    pattern = Struct(
        "Custom" / WString,
        "ErrorCode" / Int32ul
    )

