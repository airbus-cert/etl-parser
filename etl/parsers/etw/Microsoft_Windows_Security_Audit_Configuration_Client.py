# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Security-Audit-Configuration-Client
GUID : 08466062-aed4-4834-8b04-cddb414504e5
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("08466062-aed4-4834-8b04-cddb414504e5"), event_id=101, version=0)
class Microsoft_Windows_Security_Audit_Configuration_Client_101_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("08466062-aed4-4834-8b04-cddb414504e5"), event_id=102, version=0)
class Microsoft_Windows_Security_Audit_Configuration_Client_102_0(Etw):
    pattern = Struct(
        "GPOList" / WString
    )


@declare(guid=guid("08466062-aed4-4834-8b04-cddb414504e5"), event_id=104, version=0)
class Microsoft_Windows_Security_Audit_Configuration_Client_104_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("08466062-aed4-4834-8b04-cddb414504e5"), event_id=105, version=0)
class Microsoft_Windows_Security_Audit_Configuration_Client_105_0(Etw):
    pattern = Struct(
        "GPOName" / WString,
        "GPOID" / WString,
        "SysvolPath" / WString
    )


@declare(guid=guid("08466062-aed4-4834-8b04-cddb414504e5"), event_id=106, version=0)
class Microsoft_Windows_Security_Audit_Configuration_Client_106_0(Etw):
    pattern = Struct(
        "RemoteFile" / WString,
        "LocalFile" / WString,
        "GPOName" / WString
    )


@declare(guid=guid("08466062-aed4-4834-8b04-cddb414504e5"), event_id=107, version=0)
class Microsoft_Windows_Security_Audit_Configuration_Client_107_0(Etw):
    pattern = Struct(
        "RemoteFile" / WString,
        "LocalFile" / WString,
        "GPOName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("08466062-aed4-4834-8b04-cddb414504e5"), event_id=109, version=0)
class Microsoft_Windows_Security_Audit_Configuration_Client_109_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("08466062-aed4-4834-8b04-cddb414504e5"), event_id=111, version=0)
class Microsoft_Windows_Security_Audit_Configuration_Client_111_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("08466062-aed4-4834-8b04-cddb414504e5"), event_id=113, version=0)
class Microsoft_Windows_Security_Audit_Configuration_Client_113_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("08466062-aed4-4834-8b04-cddb414504e5"), event_id=115, version=0)
class Microsoft_Windows_Security_Audit_Configuration_Client_115_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("08466062-aed4-4834-8b04-cddb414504e5"), event_id=201, version=0)
class Microsoft_Windows_Security_Audit_Configuration_Client_201_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("08466062-aed4-4834-8b04-cddb414504e5"), event_id=202, version=0)
class Microsoft_Windows_Security_Audit_Configuration_Client_202_0(Etw):
    pattern = Struct(
        "GPOList" / WString
    )


@declare(guid=guid("08466062-aed4-4834-8b04-cddb414504e5"), event_id=204, version=0)
class Microsoft_Windows_Security_Audit_Configuration_Client_204_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("08466062-aed4-4834-8b04-cddb414504e5"), event_id=205, version=0)
class Microsoft_Windows_Security_Audit_Configuration_Client_205_0(Etw):
    pattern = Struct(
        "GPOName" / WString,
        "GPOID" / WString,
        "SysvolPath" / WString
    )


@declare(guid=guid("08466062-aed4-4834-8b04-cddb414504e5"), event_id=206, version=0)
class Microsoft_Windows_Security_Audit_Configuration_Client_206_0(Etw):
    pattern = Struct(
        "RemoteFile" / WString,
        "LocalFile" / WString,
        "GPOName" / WString
    )


@declare(guid=guid("08466062-aed4-4834-8b04-cddb414504e5"), event_id=207, version=0)
class Microsoft_Windows_Security_Audit_Configuration_Client_207_0(Etw):
    pattern = Struct(
        "RemoteFile" / WString,
        "LocalFile" / WString,
        "GPOName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("08466062-aed4-4834-8b04-cddb414504e5"), event_id=209, version=0)
class Microsoft_Windows_Security_Audit_Configuration_Client_209_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("08466062-aed4-4834-8b04-cddb414504e5"), event_id=211, version=0)
class Microsoft_Windows_Security_Audit_Configuration_Client_211_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("08466062-aed4-4834-8b04-cddb414504e5"), event_id=213, version=0)
class Microsoft_Windows_Security_Audit_Configuration_Client_213_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("08466062-aed4-4834-8b04-cddb414504e5"), event_id=215, version=0)
class Microsoft_Windows_Security_Audit_Configuration_Client_215_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )

