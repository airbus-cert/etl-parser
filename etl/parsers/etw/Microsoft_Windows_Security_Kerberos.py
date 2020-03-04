# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Security-Kerberos
GUID : 98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=3, version=0)
class Microsoft_Windows_Security_Kerberos_3_0(Etw):
    pattern = Struct(
        "LogonSession" / WString,
        "ClientTime" / WString,
        "ServerTime" / WString,
        "ErrorCode" / WString,
        "ErrorMessage" / WString,
        "ExtendedError" / WString,
        "ClientRealm" / WString,
        "ClientName" / WString,
        "ServerRealm" / WString,
        "ServerName" / WString,
        "TargetName" / WString,
        "ErrorText" / WString,
        "File" / WString,
        "Line" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=4, version=0)
class Microsoft_Windows_Security_Kerberos_4_0(Etw):
    pattern = Struct(
        "Server" / WString,
        "TargetRealm" / WString,
        "Targetname" / WString,
        "ClientRealm" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=5, version=0)
class Microsoft_Windows_Security_Kerberos_5_0(Etw):
    pattern = Struct(
        "Server" / WString,
        "KDCRealm" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=5, version=1)
class Microsoft_Windows_Security_Kerberos_5_1(Etw):
    pattern = Struct(
        "Error" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=6, version=0)
class Microsoft_Windows_Security_Kerberos_6_0(Etw):
    pattern = Struct(
        "NeededSize" / WString,
        "ActualSize" / WString,
        "ClientProcessID" / WString,
        "ClientName" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=6, version=1)
class Microsoft_Windows_Security_Kerberos_6_1(Etw):
    pattern = Struct(
        "Error" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=7, version=0)
class Microsoft_Windows_Security_Kerberos_7_0(Etw):
    pattern = Struct(
        "ClientName" / WString,
        "Realm" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=7, version=1)
class Microsoft_Windows_Security_Kerberos_7_1(Etw):
    pattern = Struct(
        "Error" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=8, version=0)
class Microsoft_Windows_Security_Kerberos_8_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Message" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=8, version=1)
class Microsoft_Windows_Security_Kerberos_8_1(Etw):
    pattern = Struct(
        "Error" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=9, version=0)
class Microsoft_Windows_Security_Kerberos_9_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Message" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=9, version=1)
class Microsoft_Windows_Security_Kerberos_9_1(Etw):
    pattern = Struct(
        "Error" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=10, version=1)
class Microsoft_Windows_Security_Kerberos_10_1(Etw):
    pattern = Struct(
        "Error" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=11, version=1)
class Microsoft_Windows_Security_Kerberos_11_1(Etw):
    pattern = Struct(
        "Error" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=12, version=1)
class Microsoft_Windows_Security_Kerberos_12_1(Etw):
    pattern = Struct(
        "Error" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=13, version=0)
class Microsoft_Windows_Security_Kerberos_13_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=14, version=0)
class Microsoft_Windows_Security_Kerberos_14_0(Etw):
    pattern = Struct(
        "Username" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=14, version=1)
class Microsoft_Windows_Security_Kerberos_14_1(Etw):
    pattern = Struct(
        "Error" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=15, version=0)
class Microsoft_Windows_Security_Kerberos_15_0(Etw):
    pattern = Struct(
        "NeededSize" / WString,
        "ActualSize" / WString,
        "ClientProcessID" / WString,
        "RequiredSize" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=15, version=1)
class Microsoft_Windows_Security_Kerberos_15_1(Etw):
    pattern = Struct(
        "Error" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=16, version=0)
class Microsoft_Windows_Security_Kerberos_16_0(Etw):
    pattern = Struct(
        "Username" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=16, version=1)
class Microsoft_Windows_Security_Kerberos_16_1(Etw):
    pattern = Struct(
        "Error" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=17, version=0)
class Microsoft_Windows_Security_Kerberos_17_0(Etw):
    pattern = Struct(
        "Forest" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=17, version=1)
class Microsoft_Windows_Security_Kerberos_17_1(Etw):
    pattern = Struct(
        "Error" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=18, version=0)
class Microsoft_Windows_Security_Kerberos_18_0(Etw):
    pattern = Struct(
        "Luid" / WString,
        "ClientPrincipalName" / WString,
        "ServicePrincipalName" / WString,
        "TicketFlags" / WString,
        "StartTime" / WString,
        "EndTime" / WString,
        "RenewUntil" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=18, version=1)
class Microsoft_Windows_Security_Kerberos_18_1(Etw):
    pattern = Struct(
        "Error" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=19, version=0)
class Microsoft_Windows_Security_Kerberos_19_0(Etw):
    pattern = Struct(
        "ErrorCode" / WString
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=19, version=1)
class Microsoft_Windows_Security_Kerberos_19_1(Etw):
    pattern = Struct(
        "Error" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=20, version=0)
class Microsoft_Windows_Security_Kerberos_20_0(Etw):
    pattern = Struct(
        "DomainName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=100, version=0)
class Microsoft_Windows_Security_Kerberos_100_0(Etw):
    pattern = Struct(
        "SPN" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=101, version=0)
class Microsoft_Windows_Security_Kerberos_101_0(Etw):
    pattern = Struct(
        "SPN" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=102, version=0)
class Microsoft_Windows_Security_Kerberos_102_0(Etw):
    pattern = Struct(
        "DomainController" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=103, version=0)
class Microsoft_Windows_Security_Kerberos_103_0(Etw):
    pattern = Struct(
        "ClientUpn" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=104, version=0)
class Microsoft_Windows_Security_Kerberos_104_0(Etw):
    pattern = Struct(
        "TargetDomain" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=105, version=0)
class Microsoft_Windows_Security_Kerberos_105_0(Etw):
    pattern = Struct(
        "LuidHighPart" / Int32ul,
        "LuidLowPart" / Int32ul,
        "DomainName" / WString,
        "UserName" / WString,
        "Refresh" / Int8ul,
        "CurrentFileTime" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=106, version=0)
class Microsoft_Windows_Security_Kerberos_106_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=107, version=0)
class Microsoft_Windows_Security_Kerberos_107_0(Etw):
    pattern = Struct(
        "ExpectedDomainName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=108, version=0)
class Microsoft_Windows_Security_Kerberos_108_0(Etw):
    pattern = Struct(
        "ServerName" / WString,
        "ServerPort" / Int32ul,
        "ServerVdir" / WString,
        "ErrorCode" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=109, version=0)
class Microsoft_Windows_Security_Kerberos_109_0(Etw):
    pattern = Struct(
        "Proxy" / WString,
        "ProxyBypass" / WString,
        "ProxyEpoch" / Int32ul,
        "SupportedSchemes" / Int32ul,
        "FirstScheme" / Int32ul,
        "DigestCredInitialized" / Int8ul,
        "DigestCredDomainAndUserName" / WString,
        "DigestCredEpoch" / Int32ul,
        "BasicCredInitialized" / Int8ul,
        "BasicCredDomainAndUserName" / WString,
        "BasicCredEpoch" / Int32ul
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=200, version=0)
class Microsoft_Windows_Security_Kerberos_200_0(Etw):
    pattern = Struct(
        "TargetDomain" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=201, version=0)
class Microsoft_Windows_Security_Kerberos_201_0(Etw):
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


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=202, version=0)
class Microsoft_Windows_Security_Kerberos_202_0(Etw):
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


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=300, version=0)
class Microsoft_Windows_Security_Kerberos_300_0(Etw):
    pattern = Struct(
        "DomainController" / WString,
        "TargetDomain" / WString
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=301, version=0)
class Microsoft_Windows_Security_Kerberos_301_0(Etw):
    pattern = Struct(
        "Target" / WString
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=302, version=0)
class Microsoft_Windows_Security_Kerberos_302_0(Etw):
    pattern = Struct(
        "DomainController" / WString,
        "TargetDomain" / WString,
        "DesiredFlags" / Int32ul,
        "CacheFlags" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("98e6cfcb-ee0a-41e0-a57b-622d4e1b30b1"), event_id=303, version=0)
class Microsoft_Windows_Security_Kerberos_303_0(Etw):
    pattern = Struct(
        "LuidHighPart" / Int32ul,
        "LuidLowPart" / Int32ul,
        "DomainName" / WString,
        "UserName" / WString,
        "UpdateCurrent" / Int8ul,
        "UpdateOld" / Int8ul,
        "Refresh" / Int8ul,
        "LastFileTime" / WString,
        "CurrentFileTime" / WString
    )

