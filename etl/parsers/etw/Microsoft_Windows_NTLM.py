# -*- coding: utf-8 -*-
"""
Microsoft-Windows-NTLM
GUID : ac43300d-5fcc-4800-8e99-1bd3f85f0320
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ac43300d-5fcc-4800-8e99-1bd3f85f0320"), event_id=100, version=0)
class Microsoft_Windows_NTLM_100_0(Etw):
    pattern = Struct(
        "AccountName" / WString,
        "DeviceName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("ac43300d-5fcc-4800-8e99-1bd3f85f0320"), event_id=101, version=0)
class Microsoft_Windows_NTLM_101_0(Etw):
    pattern = Struct(
        "AccountName" / WString,
        "DeviceName" / WString,
        "Status" / Int32ul,
        "SiloName" / WString,
        "PolicyName" / WString
    )


@declare(guid=guid("ac43300d-5fcc-4800-8e99-1bd3f85f0320"), event_id=301, version=0)
class Microsoft_Windows_NTLM_301_0(Etw):
    pattern = Struct(
        "AccountName" / WString,
        "DeviceName" / WString,
        "Status" / Int32ul,
        "SiloName" / WString,
        "PolicyName" / WString
    )


@declare(guid=guid("ac43300d-5fcc-4800-8e99-1bd3f85f0320"), event_id=4001, version=0)
class Microsoft_Windows_NTLM_4001_0(Etw):
    pattern = Struct(
        "TargetName" / WString,
        "UserName" / WString,
        "DomainName" / WString,
        "CallerPID" / Int32ul,
        "ProcessName" / WString,
        "ClientLUID" / Int64ul,
        "ClientUserName" / WString,
        "ClientDomainName" / WString,
        "MechanismOID" / WString
    )


@declare(guid=guid("ac43300d-5fcc-4800-8e99-1bd3f85f0320"), event_id=4002, version=0)
class Microsoft_Windows_NTLM_4002_0(Etw):
    pattern = Struct(
        "CallerPID" / Int32ul,
        "ProcessName" / WString,
        "ClientLUID" / Int64ul,
        "ClientUserName" / WString,
        "ClientDomainName" / WString,
        "MechanismOID" / WString
    )


@declare(guid=guid("ac43300d-5fcc-4800-8e99-1bd3f85f0320"), event_id=4003, version=0)
class Microsoft_Windows_NTLM_4003_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "DomainName" / WString,
        "Workstation" / WString,
        "CallerPID" / Int32ul,
        "ProcessName" / WString,
        "LogonType" / Int32ul,
        "InProc" / Int8ul,
        "MechanismOID" / WString
    )


@declare(guid=guid("ac43300d-5fcc-4800-8e99-1bd3f85f0320"), event_id=4010, version=0)
class Microsoft_Windows_NTLM_4010_0(Etw):
    pattern = Struct(
        "CallerPID" / Int32ul,
        "ProcessName" / WString,
        "NegotiatedSecurity" / Int32ul,
        "RequiredSecurity" / Int32ul
    )


@declare(guid=guid("ac43300d-5fcc-4800-8e99-1bd3f85f0320"), event_id=4011, version=0)
class Microsoft_Windows_NTLM_4011_0(Etw):
    pattern = Struct(
        "CallerPID" / Int32ul,
        "ProcessName" / WString,
        "NegotiatedSecurity" / Int32ul,
        "RequiredSecurity" / Int32ul
    )


@declare(guid=guid("ac43300d-5fcc-4800-8e99-1bd3f85f0320"), event_id=4012, version=0)
class Microsoft_Windows_NTLM_4012_0(Etw):
    pattern = Struct(
        "AccountName" / WString,
        "DeviceName" / WString
    )


@declare(guid=guid("ac43300d-5fcc-4800-8e99-1bd3f85f0320"), event_id=4013, version=0)
class Microsoft_Windows_NTLM_4013_0(Etw):
    pattern = Struct(
        "TargetName" / WString,
        "UserName" / WString,
        "DomainName" / WString,
        "CallerPID" / Int32ul,
        "ProcessName" / WString,
        "ClientLUID" / Int64ul,
        "ClientUserName" / WString,
        "ClientDomainName" / WString,
        "MechanismOID" / WString
    )


@declare(guid=guid("ac43300d-5fcc-4800-8e99-1bd3f85f0320"), event_id=8001, version=0)
class Microsoft_Windows_NTLM_8001_0(Etw):
    pattern = Struct(
        "TargetName" / WString,
        "UserName" / WString,
        "DomainName" / WString,
        "CallerPID" / Int32ul,
        "ProcessName" / WString,
        "ClientLUID" / Int64ul,
        "ClientUserName" / WString,
        "ClientDomainName" / WString,
        "MechanismOID" / WString
    )


@declare(guid=guid("ac43300d-5fcc-4800-8e99-1bd3f85f0320"), event_id=8002, version=0)
class Microsoft_Windows_NTLM_8002_0(Etw):
    pattern = Struct(
        "CallerPID" / Int32ul,
        "ProcessName" / WString,
        "ClientLUID" / Int64ul,
        "ClientUserName" / WString,
        "ClientDomainName" / WString,
        "MechanismOID" / WString
    )


@declare(guid=guid("ac43300d-5fcc-4800-8e99-1bd3f85f0320"), event_id=8003, version=0)
class Microsoft_Windows_NTLM_8003_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "DomainName" / WString,
        "Workstation" / WString,
        "CallerPID" / Int32ul,
        "ProcessName" / WString,
        "LogonType" / Int32ul,
        "InProc" / Int8ul,
        "MechanismOID" / WString
    )

