# -*- coding: utf-8 -*-
"""
LsaSrv
GUID : 199fe037-2b82-40a9-82ac-e1d46c792b99
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=100, version=0)
class LsaSrv_100_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "UserName" / WString,
        "DomainName" / WString,
        "ServerName" / WString,
        "ProtectedUser" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=200, version=0)
class LsaSrv_200_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "DomainName" / WString,
        "LogonId" / Int64ul,
        "LogoffTime" / SystemTime,
        "PID" / Int32ul,
        "Program" / WString,
        "PrincipalName" / WString,
        "ServerName" / WString,
        "PackageName" / WString,
        "CallType" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=300, version=0)
class LsaSrv_300_0(Etw):
    pattern = Struct(
        "TargetUserSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetLogonId" / Int64ul,
        "TargetLogonGuid" / Guid,
        "EventOrginal" / Int32ul,
        "EventCountTotal" / Int32ul,
        "SidList" / WString
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=301, version=0)
class LsaSrv_301_0(Etw):
    pattern = Struct(
        "TargetUserSid" / Sid,
        "TargetUserName" / WString,
        "TargetDomainName" / WString,
        "TargetLogonId" / Int64ul,
        "TargetLogonGuid" / Guid,
        "LogonType" / Int32ul,
        "EventIdx" / Int32ul,
        "EventCountTotal" / Int32ul,
        "UserClaims" / WString,
        "DeviceClaims" / WString
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=302, version=0)
class LsaSrv_302_0(Etw):
    pattern = Struct(
        "UserSid" / Sid,
        "LogonId" / Int64ul,
        "AuthorityName" / WString,
        "AccountName" / WString,
        "Elapse" / Int32ul
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=303, version=0)
class LsaSrv_303_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "UserName" / WString,
        "DomainName" / WString,
        "ProtectedUser" / Int32ul
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=320, version=0)
class LsaSrv_320_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "DomainName" / WString
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=321, version=0)
class LsaSrv_321_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=5000, version=0)
class LsaSrv_5000_0(Etw):
    pattern = Struct(
        "Package" / WString,
        "__binLength" / Int32ul,
        "Exception" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=6027, version=0)
class LsaSrv_6027_0(Etw):
    pattern = Struct(
        "Secret" / WString,
        "__binLength" / Int32ul,
        "status" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=6033, version=0)
class LsaSrv_6033_0(Etw):
    pattern = Struct(
        "Client" / WString
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=6035, version=0)
class LsaSrv_6035_0(Etw):
    pattern = Struct(
        "SID" / Sid
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=6036, version=0)
class LsaSrv_6036_0(Etw):
    pattern = Struct(
        "PID" / WString,
        "Program" / WString
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=6037, version=0)
class LsaSrv_6037_0(Etw):
    pattern = Struct(
        "PID" / WString,
        "Program" / WString,
        "TargetName" / WString
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=6040, version=0)
class LsaSrv_6040_0(Etw):
    pattern = Struct(
        "Package" / WString,
        "TargetName" / WString
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=6041, version=0)
class LsaSrv_6041_0(Etw):
    pattern = Struct(
        "TargetName" / WString,
        "TargetVersion" / WString
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=6145, version=0)
class LsaSrv_6145_0(Etw):
    pattern = Struct(
        "MissingCAPDNs" / WString
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=6146, version=0)
class LsaSrv_6146_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "CAPEName" / WString,
        "CAPEDesc" / WString
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=6182, version=0)
class LsaSrv_6182_0(Etw):
    pattern = Struct(
        "TargetLogonId" / Int64ul,
        "AccountName" / WString,
        "DomainName" / WString
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=32773, version=0)
class LsaSrv_32773_0(Etw):
    pattern = Struct(
        "Domain" / WString,
        "TargetDomain" / WString,
        "__binLength" / Int32ul,
        "status" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=32774, version=0)
class LsaSrv_32774_0(Etw):
    pattern = Struct(
        "Domain" / WString,
        "TargetDomain" / WString,
        "__binLength" / Int32ul,
        "status" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=32775, version=0)
class LsaSrv_32775_0(Etw):
    pattern = Struct(
        "Domain" / WString,
        "TargetDomain" / WString,
        "__binLength" / Int32ul,
        "status" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=32779, version=0)
class LsaSrv_32779_0(Etw):
    pattern = Struct(
        "SubCategoryGuid" / Guid
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=32780, version=0)
class LsaSrv_32780_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=40960, version=0)
class LsaSrv_40960_0(Etw):
    pattern = Struct(
        "Target" / WString,
        "Protocol" / WString,
        "Error" / WString
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=40961, version=0)
class LsaSrv_40961_0(Etw):
    pattern = Struct(
        "Target" / WString
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=40962, version=0)
class LsaSrv_40962_0(Etw):
    pattern = Struct(
        "Target" / WString,
        "Protocol" / WString
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=40965, version=0)
class LsaSrv_40965_0(Etw):
    pattern = Struct(
        "Target" / WString,
        "Protocol" / WString
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=40966, version=0)
class LsaSrv_40966_0(Etw):
    pattern = Struct(
        "Protocol" / WString
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=40967, version=0)
class LsaSrv_40967_0(Etw):
    pattern = Struct(
        "Protocol" / WString
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=40969, version=0)
class LsaSrv_40969_0(Etw):
    pattern = Struct(
        "Protocol" / WString
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=45057, version=0)
class LsaSrv_45057_0(Etw):
    pattern = Struct(
        "Username" / WString,
        "Package" / WString,
        "Error" / WString
    )


@declare(guid=guid("199fe037-2b82-40a9-82ac-e1d46c792b99"), event_id=45058, version=0)
class LsaSrv_45058_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "TimeStamp" / SystemTime
    )

