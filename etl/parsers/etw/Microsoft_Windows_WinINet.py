# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WinINet
GUID : 43d1a55c-76d6-4f7e-995c-64c711e5cafe
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=101, version=0)
class Microsoft_Windows_WinINet_101_0(Etw):
    pattern = Struct(
        "HINTERNET" / Int64ul,
        "_UserAgentLength" / Int16ul,
        "UserAgent" / Bytes(lambda this: this._UserAgentLength),
        "_AccessTypeLength" / Int16ul,
        "AccessType" / Bytes(lambda this: this._AccessTypeLength),
        "_ProxyListLength" / Int16ul,
        "ProxyList" / Bytes(lambda this: this._ProxyListLength),
        "_ProxyBypassListLength" / Int16ul,
        "ProxyBypassList" / Bytes(lambda this: this._ProxyBypassListLength),
        "Flags" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=102, version=0)
class Microsoft_Windows_WinINet_102_0(Etw):
    pattern = Struct(
        "ConnectionHandle" / Int64ul,
        "ParentHandle" / Int64ul,
        "_URLLength" / Int16ul,
        "URL" / Bytes(lambda this: this._URLLength),
        "_HeadersLength" / Int16ul,
        "Headers" / Bytes(lambda this: this._HeadersLength),
        "Flags" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=103, version=0)
class Microsoft_Windows_WinINet_103_0(Etw):
    pattern = Struct(
        "ConnectionHandle" / Int64ul,
        "ParentHandle" / Int64ul,
        "_ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this._ServerNameLength),
        "ServerPort" / Int32ul,
        "_ServiceLength" / Int16ul,
        "Service" / Bytes(lambda this: this._ServiceLength),
        "Flags" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=104, version=0)
class Microsoft_Windows_WinINet_104_0(Etw):
    pattern = Struct(
        "ConnectionHandle" / Int64ul,
        "ParentHandle" / Int64ul,
        "_VerbLength" / Int16ul,
        "Verb" / Bytes(lambda this: this._VerbLength),
        "_ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this._ObjectNameLength),
        "_VersionLength" / Int16ul,
        "Version" / Bytes(lambda this: this._VersionLength),
        "_ReferrerLength" / Int32ul,
        "Referrer" / Bytes(lambda this: this._ReferrerLength),
        "_AcceptTypesLength" / Int16ul,
        "AcceptTypes" / Bytes(lambda this: this._AcceptTypesLength),
        "Flags" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=105, version=0)
class Microsoft_Windows_WinINet_105_0(Etw):
    pattern = Struct(
        "HINTERNET" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=106, version=0)
class Microsoft_Windows_WinINet_106_0(Etw):
    pattern = Struct(
        "HINTERNET" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=107, version=0)
class Microsoft_Windows_WinINet_107_0(Etw):
    pattern = Struct(
        "HINTERNET" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=108, version=0)
class Microsoft_Windows_WinINet_108_0(Etw):
    pattern = Struct(
        "ConnectionHandle" / Int64ul,
        "_ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this._ServerNameLength),
        "ServerPort" / Int32ul,
        "_ServiceLength" / Int16ul,
        "Service" / Bytes(lambda this: this._ServiceLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=200, version=0)
class Microsoft_Windows_WinINet_200_0(Etw):
    pattern = Struct(
        "HINTERNET" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=200, version=1)
class Microsoft_Windows_WinINet_200_1(Etw):
    pattern = Struct(
        "HINTERNET" / Int64ul,
        "Context" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=201, version=0)
class Microsoft_Windows_WinINet_201_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul,
        "SocketHandle" / Int64ul,
        "_VerbLength" / Int16ul,
        "Verb" / Bytes(lambda this: this._VerbLength),
        "Cookie" / Int8ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=202, version=0)
class Microsoft_Windows_WinINet_202_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=203, version=0)
class Microsoft_Windows_WinINet_203_0(Etw):
    pattern = Struct(
        "ResponseCode" / Int32sl,
        "RequestHandle" / Int64ul,
        "SocketHandle" / Int64ul,
        "_VerbLength" / Int16ul,
        "Verb" / Bytes(lambda this: this._VerbLength),
        "_ContentLengthStrLength" / Int16ul,
        "ContentLength" / Bytes(lambda this: this._ContentLengthStrLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=204, version=0)
class Microsoft_Windows_WinINet_204_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=205, version=0)
class Microsoft_Windows_WinINet_205_0(Etw):
    pattern = Struct(
        "ConnectionHandle" / Int64ul,
        "SocketHandle" / Int64ul,
        "_ReasonLength" / Int16ul,
        "Reason" / Bytes(lambda this: this._ReasonLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=206, version=0)
class Microsoft_Windows_WinINet_206_0(Etw):
    pattern = Struct(
        "ConnectionHandle" / Int64ul,
        "SocketHandle" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=207, version=0)
class Microsoft_Windows_WinINet_207_0(Etw):
    pattern = Struct(
        "ConnectionHandle" / Int64ul,
        "SocketHandle" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=208, version=0)
class Microsoft_Windows_WinINet_208_0(Etw):
    pattern = Struct(
        "ConnectionHandle" / Int64ul,
        "SocketHandle" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=209, version=0)
class Microsoft_Windows_WinINet_209_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=210, version=0)
class Microsoft_Windows_WinINet_210_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul,
        "Length" / Int16ul,
        "Headers" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=211, version=0)
class Microsoft_Windows_WinINet_211_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul,
        "Length" / Int16ul,
        "Headers" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=212, version=0)
class Microsoft_Windows_WinINet_212_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul,
        "Length" / Int16ul,
        "Headers" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=213, version=0)
class Microsoft_Windows_WinINet_213_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=301, version=0)
class Microsoft_Windows_WinINet_301_0(Etw):
    pattern = Struct(
        "_ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this._ServerNameLength),
        "ConnectionHandle" / Int64ul,
        "SocketHandle" / Int64ul,
        "LocalPort" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=302, version=0)
class Microsoft_Windows_WinINet_302_0(Etw):
    pattern = Struct(
        "_ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this._ServerNameLength),
        "ConnectionHandle" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=303, version=0)
class Microsoft_Windows_WinINet_303_0(Etw):
    pattern = Struct(
        "SocketHandle" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=304, version=0)
class Microsoft_Windows_WinINet_304_0(Etw):
    pattern = Struct(
        "_HostNameLength" / Int16ul,
        "HostName" / Bytes(lambda this: this._HostNameLength),
        "RequestHandle" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=305, version=0)
class Microsoft_Windows_WinINet_305_0(Etw):
    pattern = Struct(
        "_HostNameLength" / Int16ul,
        "HostName" / Bytes(lambda this: this._HostNameLength),
        "RequestHandle" / Int64ul,
        "_AddressListLength" / Int16ul,
        "AddressList" / Bytes(lambda this: this._AddressListLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=306, version=0)
class Microsoft_Windows_WinINet_306_0(Etw):
    pattern = Struct(
        "_HostNameLength" / Int16ul,
        "HostName" / Bytes(lambda this: this._HostNameLength),
        "RequestHandle" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=307, version=0)
class Microsoft_Windows_WinINet_307_0(Etw):
    pattern = Struct(
        "_HostNameLength" / Int16ul,
        "HostName" / Bytes(lambda this: this._HostNameLength),
        "RequestHandle" / Int64ul,
        "_AddressListLength" / Int16ul,
        "AddressList" / Bytes(lambda this: this._AddressListLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=308, version=0)
class Microsoft_Windows_WinINet_308_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=400, version=0)
class Microsoft_Windows_WinINet_400_0(Etw):
    pattern = Struct(
        "CorrelationID" / Guid,
        "InternetFlags" / Int32ul,
        "Length" / Int16ul,
        "Headers" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=401, version=0)
class Microsoft_Windows_WinINet_401_0(Etw):
    pattern = Struct(
        "CorrelationID" / Guid,
        "ResponseCode" / Int32sl,
        "Length" / Int16ul,
        "Headers" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=402, version=0)
class Microsoft_Windows_WinINet_402_0(Etw):
    pattern = Struct(
        "CorrelationID" / Guid
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=403, version=0)
class Microsoft_Windows_WinINet_403_0(Etw):
    pattern = Struct(
        "CorrelationID" / Guid,
        "Status" / Int16ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=404, version=0)
class Microsoft_Windows_WinINet_404_0(Etw):
    pattern = Struct(
        "CorrelationID" / Guid,
        "Length" / Int64sl,
        "TruncatedLength" / Int16ul,
        "TruncatedData" / Bytes(lambda this: this.TruncatedLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=405, version=0)
class Microsoft_Windows_WinINet_405_0(Etw):
    pattern = Struct(
        "CorrelationID" / Guid,
        "Length" / Int64sl,
        "TruncatedLength" / Int16ul,
        "TruncatedData" / Bytes(lambda this: this.TruncatedLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=406, version=0)
class Microsoft_Windows_WinINet_406_0(Etw):
    pattern = Struct(
        "CorrelationID" / Guid,
        "Length" / Int64sl
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=407, version=0)
class Microsoft_Windows_WinINet_407_0(Etw):
    pattern = Struct(
        "CorrelationID" / Guid,
        "Status" / Int16ul,
        "Length" / Int32ul,
        "Reason" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=408, version=0)
class Microsoft_Windows_WinINet_408_0(Etw):
    pattern = Struct(
        "CorrelationID" / Guid,
        "Length" / Int64sl
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=409, version=0)
class Microsoft_Windows_WinINet_409_0(Etw):
    pattern = Struct(
        "CorrelationID" / Guid,
        "Status" / Int16ul,
        "Length" / Int32ul,
        "Reason" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=410, version=0)
class Microsoft_Windows_WinINet_410_0(Etw):
    pattern = Struct(
        "CorrelationID" / Guid,
        "Length" / Int64sl
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=411, version=0)
class Microsoft_Windows_WinINet_411_0(Etw):
    pattern = Struct(
        "CorrelationID" / Guid,
        "Length" / Int64sl
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=412, version=0)
class Microsoft_Windows_WinINet_412_0(Etw):
    pattern = Struct(
        "CorrelationID" / Guid
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=413, version=0)
class Microsoft_Windows_WinINet_413_0(Etw):
    pattern = Struct(
        "CorrelationID" / Guid
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=414, version=0)
class Microsoft_Windows_WinINet_414_0(Etw):
    pattern = Struct(
        "CorrelationID" / Guid,
        "SequenceNumber" / Int32ul,
        "PayloadByteLength" / Int32ul,
        "Payload" / Bytes(lambda this: this.PayloadByteLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=415, version=0)
class Microsoft_Windows_WinINet_415_0(Etw):
    pattern = Struct(
        "CorrelationID" / Guid,
        "SequenceNumber" / Int32ul,
        "PayloadByteLength" / Int32ul,
        "Payload" / Bytes(lambda this: this.PayloadByteLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=416, version=0)
class Microsoft_Windows_WinINet_416_0(Etw):
    pattern = Struct(
        "CorrelationID" / Guid,
        "SequenceNumber" / Int32ul,
        "PayloadByteLength" / Int32ul,
        "Payload" / Bytes(lambda this: this.PayloadByteLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=417, version=0)
class Microsoft_Windows_WinINet_417_0(Etw):
    pattern = Struct(
        "CorrelationID" / Guid,
        "SequenceNumber" / Int32ul,
        "PayloadByteLength" / Int32ul,
        "Payload" / Bytes(lambda this: this.PayloadByteLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=501, version=0)
class Microsoft_Windows_WinINet_501_0(Etw):
    pattern = Struct(
        "URLLength" / Int32ul,
        "URL" / Bytes(lambda this: this.URLLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=502, version=0)
class Microsoft_Windows_WinINet_502_0(Etw):
    pattern = Struct(
        "_DomainLength" / Int16ul,
        "Domain" / Bytes(lambda this: this._DomainLength),
        "_PathLength" / Int16ul,
        "Path" / Bytes(lambda this: this._PathLength),
        "_NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this._NameLength),
        "_ValueLength" / Int16ul,
        "Value" / Bytes(lambda this: this._ValueLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=503, version=0)
class Microsoft_Windows_WinINet_503_0(Etw):
    pattern = Struct(
        "_DomainLength" / Int16ul,
        "Domain" / Bytes(lambda this: this._DomainLength),
        "_PathLength" / Int16ul,
        "Path" / Bytes(lambda this: this._PathLength),
        "_NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this._NameLength),
        "_ValueLength" / Int16ul,
        "Value" / Bytes(lambda this: this._ValueLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=504, version=0)
class Microsoft_Windows_WinINet_504_0(Etw):
    pattern = Struct(
        "_DomainLength" / Int16ul,
        "Domain" / Bytes(lambda this: this._DomainLength),
        "_PathLength" / Int16ul,
        "Path" / Bytes(lambda this: this._PathLength),
        "_NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this._NameLength),
        "_ValueLength" / Int16ul,
        "Value" / Bytes(lambda this: this._ValueLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=505, version=0)
class Microsoft_Windows_WinINet_505_0(Etw):
    pattern = Struct(
        "_DomainLength" / Int16ul,
        "Domain" / Bytes(lambda this: this._DomainLength),
        "_PathLength" / Int16ul,
        "Path" / Bytes(lambda this: this._PathLength),
        "_NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this._NameLength),
        "_ValueLength" / Int16ul,
        "Value" / Bytes(lambda this: this._ValueLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=506, version=0)
class Microsoft_Windows_WinINet_506_0(Etw):
    pattern = Struct(
        "URLLength" / Int32ul,
        "URL" / Bytes(lambda this: this.URLLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=507, version=0)
class Microsoft_Windows_WinINet_507_0(Etw):
    pattern = Struct(
        "_DomainLength" / Int16ul,
        "Domain" / Bytes(lambda this: this._DomainLength),
        "_PathLength" / Int16ul,
        "Path" / Bytes(lambda this: this._PathLength),
        "_NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this._NameLength),
        "_ValueLength" / Int16ul,
        "Value" / Bytes(lambda this: this._ValueLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=601, version=0)
class Microsoft_Windows_WinINet_601_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul,
        "_SchemeLength" / Int16ul,
        "Scheme" / Bytes(lambda this: this._SchemeLength),
        "IsProxy" / Int8ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=602, version=0)
class Microsoft_Windows_WinINet_602_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul,
        "IsProxy" / Int8ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=603, version=0)
class Microsoft_Windows_WinINet_603_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul,
        "IsProxy" / Int8ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=604, version=0)
class Microsoft_Windows_WinINet_604_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul,
        "IsProxy" / Int8ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=605, version=0)
class Microsoft_Windows_WinINet_605_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul,
        "IsProxy" / Int8ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=606, version=0)
class Microsoft_Windows_WinINet_606_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul,
        "_SchemeLength" / Int16ul,
        "Scheme" / Bytes(lambda this: this._SchemeLength),
        "IsProxy" / Int8ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=701, version=0)
class Microsoft_Windows_WinINet_701_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=702, version=0)
class Microsoft_Windows_WinINet_702_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=703, version=0)
class Microsoft_Windows_WinINet_703_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=704, version=0)
class Microsoft_Windows_WinINet_704_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=705, version=0)
class Microsoft_Windows_WinINet_705_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul,
        "_CertHashLength" / Int16ul,
        "CertHash" / Bytes(lambda this: this._CertHashLength),
        "WarningFlags" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=706, version=0)
class Microsoft_Windows_WinINet_706_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=707, version=0)
class Microsoft_Windows_WinINet_707_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=708, version=0)
class Microsoft_Windows_WinINet_708_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul,
        "_CertHashLength" / Int16ul,
        "CertHash" / Bytes(lambda this: this._CertHashLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=711, version=0)
class Microsoft_Windows_WinINet_711_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=712, version=0)
class Microsoft_Windows_WinINet_712_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=713, version=0)
class Microsoft_Windows_WinINet_713_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=801, version=0)
class Microsoft_Windows_WinINet_801_0(Etw):
    pattern = Struct(
        "_ConnectionNameLength" / Int16ul,
        "ConnectionName" / Bytes(lambda this: this._ConnectionNameLength),
        "DetectFlags" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=801, version=1)
class Microsoft_Windows_WinINet_801_1(Etw):
    pattern = Struct(
        "_ConnectionNameLength" / Int16ul,
        "ConnectionName" / Bytes(lambda this: this._ConnectionNameLength),
        "DetectFlags" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=802, version=0)
class Microsoft_Windows_WinINet_802_0(Etw):
    pattern = Struct(
        "_InterfaceLength" / Int16ul,
        "Interface" / Bytes(lambda this: this._InterfaceLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=802, version=1)
class Microsoft_Windows_WinINet_802_1(Etw):
    pattern = Struct(
        "_InterfaceLength" / Int16ul,
        "Interface" / Bytes(lambda this: this._InterfaceLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=803, version=0)
class Microsoft_Windows_WinINet_803_0(Etw):
    pattern = Struct(
        "_InterfaceLength" / Int16ul,
        "Interface" / Bytes(lambda this: this._InterfaceLength),
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=803, version=1)
class Microsoft_Windows_WinINet_803_1(Etw):
    pattern = Struct(
        "_InterfaceLength" / Int16ul,
        "Interface" / Bytes(lambda this: this._InterfaceLength),
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=804, version=0)
class Microsoft_Windows_WinINet_804_0(Etw):
    pattern = Struct(
        "_InterfaceLength" / Int16ul,
        "Interface" / Bytes(lambda this: this._InterfaceLength),
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength),
        "Error" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=804, version=1)
class Microsoft_Windows_WinINet_804_1(Etw):
    pattern = Struct(
        "_InterfaceLength" / Int16ul,
        "Interface" / Bytes(lambda this: this._InterfaceLength),
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength),
        "Error" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=805, version=0)
class Microsoft_Windows_WinINet_805_0(Etw):
    pattern = Struct(
        "DetectFlags" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=806, version=0)
class Microsoft_Windows_WinINet_806_0(Etw):
    pattern = Struct(
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength),
        "DetectFlags" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=806, version=1)
class Microsoft_Windows_WinINet_806_1(Etw):
    pattern = Struct(
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength),
        "DetectFlags" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=807, version=0)
class Microsoft_Windows_WinINet_807_0(Etw):
    pattern = Struct(
        "DetectFlags" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=808, version=0)
class Microsoft_Windows_WinINet_808_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=809, version=0)
class Microsoft_Windows_WinINet_809_0(Etw):
    pattern = Struct(
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=809, version=1)
class Microsoft_Windows_WinINet_809_1(Etw):
    pattern = Struct(
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=810, version=0)
class Microsoft_Windows_WinINet_810_0(Etw):
    pattern = Struct(
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=810, version=1)
class Microsoft_Windows_WinINet_810_1(Etw):
    pattern = Struct(
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=811, version=0)
class Microsoft_Windows_WinINet_811_0(Etw):
    pattern = Struct(
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength),
        "Error" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=811, version=1)
class Microsoft_Windows_WinINet_811_1(Etw):
    pattern = Struct(
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength),
        "Error" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=812, version=0)
class Microsoft_Windows_WinINet_812_0(Etw):
    pattern = Struct(
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength),
        "_MIMETypeLength" / Int16ul,
        "MIMEType" / Bytes(lambda this: this._MIMETypeLength),
        "Error" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=812, version=1)
class Microsoft_Windows_WinINet_812_1(Etw):
    pattern = Struct(
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength),
        "_MIMETypeLength" / Int16ul,
        "MIMEType" / Bytes(lambda this: this._MIMETypeLength),
        "Error" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=813, version=0)
class Microsoft_Windows_WinINet_813_0(Etw):
    pattern = Struct(
        "_URLLength" / Int16ul,
        "URL" / Bytes(lambda this: this._URLLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=813, version=1)
class Microsoft_Windows_WinINet_813_1(Etw):
    pattern = Struct(
        "_URLLength" / Int16ul,
        "URL" / Bytes(lambda this: this._URLLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=814, version=0)
class Microsoft_Windows_WinINet_814_0(Etw):
    pattern = Struct(
        "_URLLength" / Int16ul,
        "URL" / Bytes(lambda this: this._URLLength),
        "_ProxyStringLength" / Int16ul,
        "ProxyString" / Bytes(lambda this: this._ProxyStringLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=814, version=1)
class Microsoft_Windows_WinINet_814_1(Etw):
    pattern = Struct(
        "_URLLength" / Int16ul,
        "URL" / Bytes(lambda this: this._URLLength),
        "_ProxyStringLength" / Int16ul,
        "ProxyString" / Bytes(lambda this: this._ProxyStringLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=815, version=0)
class Microsoft_Windows_WinINet_815_0(Etw):
    pattern = Struct(
        "_URLLength" / Int16ul,
        "URL" / Bytes(lambda this: this._URLLength),
        "Error" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=815, version=1)
class Microsoft_Windows_WinINet_815_1(Etw):
    pattern = Struct(
        "_URLLength" / Int16ul,
        "URL" / Bytes(lambda this: this._URLLength),
        "Error" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=819, version=0)
class Microsoft_Windows_WinINet_819_0(Etw):
    pattern = Struct(
        "WPADNetworkDecision" / Int32ul,
        "NetworkCount" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=834, version=0)
class Microsoft_Windows_WinINet_834_0(Etw):
    pattern = Struct(
        "UniqueId" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=835, version=0)
class Microsoft_Windows_WinINet_835_0(Etw):
    pattern = Struct(
        "UniqueId" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=901, version=0)
class Microsoft_Windows_WinINet_901_0(Etw):
    pattern = Struct(
        "AppPackageSid" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=902, version=0)
class Microsoft_Windows_WinINet_902_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "Offline" / Int8ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1000, version=0)
class Microsoft_Windows_WinINet_1000_0(Etw):
    pattern = Struct(
        "_TestStr0Length" / Int8ul,
        "TestStr0" / Bytes(lambda this: this._TestStr0Length),
        "_TestStr1Length" / Int16ul,
        "TestStr1" / Bytes(lambda this: this._TestStr1Length),
        "_TestStr2Length" / Int32ul,
        "TestStr2" / Bytes(lambda this: this._TestStr2Length),
        "_TestStr0WLength" / Int8ul,
        "TestStr0W" / Bytes(lambda this: this._TestStr0WLength),
        "_TestStr1WLength" / Int16ul,
        "TestStr1W" / Bytes(lambda this: this._TestStr1WLength),
        "_TestStr2WLength" / Int32ul,
        "TestStr2W" / Bytes(lambda this: this._TestStr2WLength),
        "TestStrLength" / Int16ul,
        "TestStr" / Bytes(lambda this: this.TestStrLength),
        "TestStrWLength" / Int16ul,
        "TestStrW" / Bytes(lambda this: this.TestStrWLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1007, version=0)
class Microsoft_Windows_WinINet_1007_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "AddressName" / CString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1008, version=0)
class Microsoft_Windows_WinINet_1008_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "StatusLineLength" / Int32ul,
        "StatusLine" / Bytes(lambda this: this.StatusLineLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1009, version=0)
class Microsoft_Windows_WinINet_1009_0(Etw):
    pattern = Struct(
        "Request" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1011, version=0)
class Microsoft_Windows_WinINet_1011_0(Etw):
    pattern = Struct(
        "Request" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1013, version=0)
class Microsoft_Windows_WinINet_1013_0(Etw):
    pattern = Struct(
        "Request" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1015, version=0)
class Microsoft_Windows_WinINet_1015_0(Etw):
    pattern = Struct(
        "Request" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1017, version=0)
class Microsoft_Windows_WinINet_1017_0(Etw):
    pattern = Struct(
        "Request" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1019, version=0)
class Microsoft_Windows_WinINet_1019_0(Etw):
    pattern = Struct(
        "Request" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1021, version=0)
class Microsoft_Windows_WinINet_1021_0(Etw):
    pattern = Struct(
        "Request" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1023, version=0)
class Microsoft_Windows_WinINet_1023_0(Etw):
    pattern = Struct(
        "Request" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1025, version=0)
class Microsoft_Windows_WinINet_1025_0(Etw):
    pattern = Struct(
        "Request" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1027, version=0)
class Microsoft_Windows_WinINet_1027_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "HostName" / CString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1028, version=0)
class Microsoft_Windows_WinINet_1028_0(Etw):
    pattern = Struct(
        "Request" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1029, version=0)
class Microsoft_Windows_WinINet_1029_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "HostName" / CString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1030, version=0)
class Microsoft_Windows_WinINet_1030_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "HostName" / CString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1031, version=0)
class Microsoft_Windows_WinINet_1031_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1033, version=0)
class Microsoft_Windows_WinINet_1033_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1035, version=0)
class Microsoft_Windows_WinINet_1035_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1037, version=0)
class Microsoft_Windows_WinINet_1037_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1039, version=0)
class Microsoft_Windows_WinINet_1039_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1041, version=0)
class Microsoft_Windows_WinINet_1041_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1043, version=0)
class Microsoft_Windows_WinINet_1043_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1045, version=0)
class Microsoft_Windows_WinINet_1045_0(Etw):
    pattern = Struct(
        "Request" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1046, version=0)
class Microsoft_Windows_WinINet_1046_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Socket" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1046, version=1)
class Microsoft_Windows_WinINet_1046_1(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Socket" / Int32ul,
        "Protocol" / Int32ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1047, version=0)
class Microsoft_Windows_WinINet_1047_0(Etw):
    pattern = Struct(
        "Request" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1048, version=0)
class Microsoft_Windows_WinINet_1048_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Socket" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1049, version=0)
class Microsoft_Windows_WinINet_1049_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "AddressName" / CString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1051, version=0)
class Microsoft_Windows_WinINet_1051_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "AddressName" / CString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1052, version=0)
class Microsoft_Windows_WinINet_1052_0(Etw):
    pattern = Struct(
        "error" / Int32ul,
        "Flags" / Int32ul,
        "AddressName" / CString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1053, version=0)
class Microsoft_Windows_WinINet_1053_0(Etw):
    pattern = Struct(
        "Order" / Int32ul,
        "AddressName" / CString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1054, version=0)
class Microsoft_Windows_WinINet_1054_0(Etw):
    pattern = Struct(
        "error" / Int32ul,
        "AddressName" / CString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1055, version=0)
class Microsoft_Windows_WinINet_1055_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1056, version=0)
class Microsoft_Windows_WinINet_1056_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1057, version=0)
class Microsoft_Windows_WinINet_1057_0(Etw):
    pattern = Struct(
        "URL" / CString,
        "Verb" / CString,
        "RequestHeaders" / CString,
        "ResponseHeaders" / CString,
        "Status" / Int32ul,
        "UsageLogRequestCache" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1058, version=0)
class Microsoft_Windows_WinINet_1058_0(Etw):
    pattern = Struct(
        "URL" / CString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1059, version=0)
class Microsoft_Windows_WinINet_1059_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Socket" / Int32ul,
        "SourcePort" / Int32ul,
        "RemoteAddressIndex" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1060, version=0)
class Microsoft_Windows_WinINet_1060_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Socket" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1061, version=0)
class Microsoft_Windows_WinINet_1061_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1062, version=0)
class Microsoft_Windows_WinINet_1062_0(Etw):
    pattern = Struct(
        "ManifestURL" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1063, version=0)
class Microsoft_Windows_WinINet_1063_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "OldPriority" / Int32sl,
        "NewPriority" / Int32sl
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1064, version=0)
class Microsoft_Windows_WinINet_1064_0(Etw):
    pattern = Struct(
        "RequestHandle" / Int64ul,
        "StreamId" / Int32ul,
        "Size" / Int32ul,
        "Headers" / Int8ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1065, version=0)
class Microsoft_Windows_WinINet_1065_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "HostName" / CString,
        "NegotiationCount" / Int32ul,
        "Socket" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1066, version=0)
class Microsoft_Windows_WinINet_1066_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "HostName" / CString,
        "NegotiationCount" / Int32ul,
        "Socket" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1067, version=0)
class Microsoft_Windows_WinINet_1067_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Socket" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1068, version=0)
class Microsoft_Windows_WinINet_1068_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Socket" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1069, version=0)
class Microsoft_Windows_WinINet_1069_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "Operation" / Int32ul,
        "ClientType" / Int32ul,
        "ThreadInfoUIType" / Int32ul,
        "IsSync" / Int8ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1070, version=0)
class Microsoft_Windows_WinINet_1070_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "Operation" / Int32ul,
        "ClientType" / Int32ul,
        "ThreadInfoUIType" / Int32ul,
        "IsSync" / Int8ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1071, version=0)
class Microsoft_Windows_WinINet_1071_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "Operation" / Int32ul,
        "ClientType" / Int32ul,
        "ThreadInfoUIType" / Int32ul,
        "IsSync" / Int8ul,
        "DataLength" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1072, version=0)
class Microsoft_Windows_WinINet_1072_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "Operation" / Int32ul,
        "ClientType" / Int32ul,
        "ThreadInfoUIType" / Int32ul,
        "IsSync" / Int8ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1073, version=0)
class Microsoft_Windows_WinINet_1073_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Url" / WString,
        "LocalFileName" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1074, version=0)
class Microsoft_Windows_WinINet_1074_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1075, version=0)
class Microsoft_Windows_WinINet_1075_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Handle" / Int64ul,
        "Url" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1076, version=0)
class Microsoft_Windows_WinINet_1076_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1077, version=0)
class Microsoft_Windows_WinINet_1077_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Handle" / Int64ul,
        "Url" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1078, version=0)
class Microsoft_Windows_WinINet_1078_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1079, version=0)
class Microsoft_Windows_WinINet_1079_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "DataSize" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1080, version=0)
class Microsoft_Windows_WinINet_1080_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1081, version=0)
class Microsoft_Windows_WinINet_1081_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1082, version=0)
class Microsoft_Windows_WinINet_1082_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1083, version=0)
class Microsoft_Windows_WinINet_1083_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Url" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1084, version=0)
class Microsoft_Windows_WinINet_1084_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1085, version=0)
class Microsoft_Windows_WinINet_1085_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1086, version=0)
class Microsoft_Windows_WinINet_1086_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1087, version=0)
class Microsoft_Windows_WinINet_1087_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1088, version=0)
class Microsoft_Windows_WinINet_1088_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1089, version=0)
class Microsoft_Windows_WinINet_1089_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Handle" / Int64ul,
        "Directory" / WString,
        "IsIEAppContainer" / Int8ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1090, version=0)
class Microsoft_Windows_WinINet_1090_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1091, version=0)
class Microsoft_Windows_WinINet_1091_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1092, version=0)
class Microsoft_Windows_WinINet_1092_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1093, version=0)
class Microsoft_Windows_WinINet_1093_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1094, version=0)
class Microsoft_Windows_WinINet_1094_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1095, version=0)
class Microsoft_Windows_WinINet_1095_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Url" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1096, version=0)
class Microsoft_Windows_WinINet_1096_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1097, version=0)
class Microsoft_Windows_WinINet_1097_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Url" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1098, version=0)
class Microsoft_Windows_WinINet_1098_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1099, version=0)
class Microsoft_Windows_WinINet_1099_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Url" / WString,
        "Flags" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1100, version=0)
class Microsoft_Windows_WinINet_1100_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1101, version=0)
class Microsoft_Windows_WinINet_1101_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "MasterUrl" / WString,
        "ManifestURL" / WString,
        "DataSize" / Int32ul,
        "EntryType" / Int32ul,
        "HeaderSize" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1102, version=0)
class Microsoft_Windows_WinINet_1102_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1103, version=0)
class Microsoft_Windows_WinINet_1103_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1104, version=0)
class Microsoft_Windows_WinINet_1104_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1105, version=0)
class Microsoft_Windows_WinINet_1105_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1106, version=0)
class Microsoft_Windows_WinINet_1106_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1107, version=0)
class Microsoft_Windows_WinINet_1107_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1108, version=0)
class Microsoft_Windows_WinINet_1108_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1109, version=0)
class Microsoft_Windows_WinINet_1109_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1110, version=0)
class Microsoft_Windows_WinINet_1110_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1111, version=0)
class Microsoft_Windows_WinINet_1111_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Handle" / Int64ul,
        "Directory" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1112, version=0)
class Microsoft_Windows_WinINet_1112_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1113, version=0)
class Microsoft_Windows_WinINet_1113_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1114, version=0)
class Microsoft_Windows_WinINet_1114_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1115, version=0)
class Microsoft_Windows_WinINet_1115_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1116, version=0)
class Microsoft_Windows_WinINet_1116_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1117, version=0)
class Microsoft_Windows_WinINet_1117_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Url" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1118, version=0)
class Microsoft_Windows_WinINet_1118_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1119, version=0)
class Microsoft_Windows_WinINet_1119_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Url" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1120, version=0)
class Microsoft_Windows_WinINet_1120_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1121, version=0)
class Microsoft_Windows_WinINet_1121_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Url" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1122, version=0)
class Microsoft_Windows_WinINet_1122_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1123, version=0)
class Microsoft_Windows_WinINet_1123_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1124, version=0)
class Microsoft_Windows_WinINet_1124_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1125, version=0)
class Microsoft_Windows_WinINet_1125_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1126, version=0)
class Microsoft_Windows_WinINet_1126_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1129, version=0)
class Microsoft_Windows_WinINet_1129_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Handle" / Int64ul,
        "Directory" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1130, version=0)
class Microsoft_Windows_WinINet_1130_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1131, version=0)
class Microsoft_Windows_WinINet_1131_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1132, version=0)
class Microsoft_Windows_WinINet_1132_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1133, version=0)
class Microsoft_Windows_WinINet_1133_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "MinimizedRDomain" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1134, version=0)
class Microsoft_Windows_WinINet_1134_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1135, version=0)
class Microsoft_Windows_WinINet_1135_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1136, version=0)
class Microsoft_Windows_WinINet_1136_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1137, version=0)
class Microsoft_Windows_WinINet_1137_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Hash" / Int64sl,
        "OperationCount" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1138, version=0)
class Microsoft_Windows_WinINet_1138_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1139, version=0)
class Microsoft_Windows_WinINet_1139_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1140, version=0)
class Microsoft_Windows_WinINet_1140_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1141, version=0)
class Microsoft_Windows_WinINet_1141_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Handle" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1142, version=0)
class Microsoft_Windows_WinINet_1142_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1143, version=0)
class Microsoft_Windows_WinINet_1143_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Url" / WString,
        "BlobSize" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1144, version=0)
class Microsoft_Windows_WinINet_1144_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1145, version=0)
class Microsoft_Windows_WinINet_1145_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Url" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1146, version=0)
class Microsoft_Windows_WinINet_1146_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1147, version=0)
class Microsoft_Windows_WinINet_1147_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1148, version=0)
class Microsoft_Windows_WinINet_1148_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1149, version=0)
class Microsoft_Windows_WinINet_1149_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Handle" / Int64ul,
        "IsCreateContainer" / Int8ul,
        "Directory" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1150, version=0)
class Microsoft_Windows_WinINet_1150_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1151, version=0)
class Microsoft_Windows_WinINet_1151_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1152, version=0)
class Microsoft_Windows_WinINet_1152_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1153, version=0)
class Microsoft_Windows_WinINet_1153_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Handle" / Int64ul,
        "Directory" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1154, version=0)
class Microsoft_Windows_WinINet_1154_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1155, version=0)
class Microsoft_Windows_WinINet_1155_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1156, version=0)
class Microsoft_Windows_WinINet_1156_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1157, version=0)
class Microsoft_Windows_WinINet_1157_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "MinimizedRDomain" / WString,
        "Hash" / Int64sl
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1158, version=0)
class Microsoft_Windows_WinINet_1158_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1159, version=0)
class Microsoft_Windows_WinINet_1159_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Hash" / Int64sl,
        "HstsEntryCount" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1160, version=0)
class Microsoft_Windows_WinINet_1160_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1161, version=0)
class Microsoft_Windows_WinINet_1161_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1162, version=0)
class Microsoft_Windows_WinINet_1162_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1163, version=0)
class Microsoft_Windows_WinINet_1163_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1164, version=0)
class Microsoft_Windows_WinINet_1164_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1165, version=0)
class Microsoft_Windows_WinINet_1165_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Handle" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1166, version=0)
class Microsoft_Windows_WinINet_1166_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1167, version=0)
class Microsoft_Windows_WinINet_1167_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1168, version=0)
class Microsoft_Windows_WinINet_1168_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1169, version=0)
class Microsoft_Windows_WinINet_1169_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Handle" / Int64ul,
        "Filter" / Int32ul,
        "GroupId" / Int64sl
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1170, version=0)
class Microsoft_Windows_WinINet_1170_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1171, version=0)
class Microsoft_Windows_WinINet_1171_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1172, version=0)
class Microsoft_Windows_WinINet_1172_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1173, version=0)
class Microsoft_Windows_WinINet_1173_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "EntryMaxAge" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1174, version=0)
class Microsoft_Windows_WinINet_1174_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1175, version=0)
class Microsoft_Windows_WinINet_1175_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Type" / Int32ul,
        "Flags" / Int32ul,
        "Url" / WString,
        "Redirect" / WString,
        "Filename" / WString,
        "Extension" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1176, version=0)
class Microsoft_Windows_WinINet_1176_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1177, version=0)
class Microsoft_Windows_WinINet_1177_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Url" / WString,
        "ValidateCreationTime" / Int8ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1178, version=0)
class Microsoft_Windows_WinINet_1178_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1179, version=0)
class Microsoft_Windows_WinINet_1179_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Url" / WString,
        "Flags" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1180, version=0)
class Microsoft_Windows_WinINet_1180_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1181, version=0)
class Microsoft_Windows_WinINet_1181_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1182, version=0)
class Microsoft_Windows_WinINet_1182_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1183, version=0)
class Microsoft_Windows_WinINet_1183_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Url" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1184, version=0)
class Microsoft_Windows_WinINet_1184_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1185, version=0)
class Microsoft_Windows_WinINet_1185_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Url" / WString,
        "Type" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1186, version=0)
class Microsoft_Windows_WinINet_1186_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1187, version=0)
class Microsoft_Windows_WinINet_1187_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Url" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1188, version=0)
class Microsoft_Windows_WinINet_1188_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1189, version=0)
class Microsoft_Windows_WinINet_1189_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Url" / WString,
        "Fields" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1190, version=0)
class Microsoft_Windows_WinINet_1190_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1191, version=0)
class Microsoft_Windows_WinINet_1191_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1192, version=0)
class Microsoft_Windows_WinINet_1192_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1193, version=0)
class Microsoft_Windows_WinINet_1193_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1194, version=0)
class Microsoft_Windows_WinINet_1194_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1195, version=0)
class Microsoft_Windows_WinINet_1195_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Limit" / Int64sl
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1196, version=0)
class Microsoft_Windows_WinINet_1196_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1197, version=0)
class Microsoft_Windows_WinINet_1197_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Factor" / Int32ul,
        "Filter" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1198, version=0)
class Microsoft_Windows_WinINet_1198_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1199, version=0)
class Microsoft_Windows_WinINet_1199_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1200, version=0)
class Microsoft_Windows_WinINet_1200_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1201, version=0)
class Microsoft_Windows_WinINet_1201_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1202, version=0)
class Microsoft_Windows_WinINet_1202_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1203, version=0)
class Microsoft_Windows_WinINet_1203_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Filename" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1204, version=0)
class Microsoft_Windows_WinINet_1204_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1205, version=0)
class Microsoft_Windows_WinINet_1205_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1206, version=0)
class Microsoft_Windows_WinINet_1206_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1207, version=0)
class Microsoft_Windows_WinINet_1207_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "GroupId" / Int64sl,
        "Flags" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1208, version=0)
class Microsoft_Windows_WinINet_1208_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1209, version=0)
class Microsoft_Windows_WinINet_1209_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1210, version=0)
class Microsoft_Windows_WinINet_1210_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1211, version=0)
class Microsoft_Windows_WinINet_1211_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "GroupId" / Int64sl
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1212, version=0)
class Microsoft_Windows_WinINet_1212_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1213, version=0)
class Microsoft_Windows_WinINet_1213_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "GroupId" / Int64sl,
        "Flags" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1214, version=0)
class Microsoft_Windows_WinINet_1214_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1215, version=0)
class Microsoft_Windows_WinINet_1215_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Url" / WString,
        "GroupId" / Int64sl,
        "Flags" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1216, version=0)
class Microsoft_Windows_WinINet_1216_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1217, version=0)
class Microsoft_Windows_WinINet_1217_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Handle" / Int64ul,
        "Name" / WString,
        "Directory" / WString,
        "Flags" / Int32ul,
        "Limit" / Int64sl,
        "EntryMaxAge" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1218, version=0)
class Microsoft_Windows_WinINet_1218_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1219, version=0)
class Microsoft_Windows_WinINet_1219_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1220, version=0)
class Microsoft_Windows_WinINet_1220_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1221, version=0)
class Microsoft_Windows_WinINet_1221_0(Etw):
    pattern = Struct(
        "TargetSize" / Int64sl,
        "Filter" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1222, version=0)
class Microsoft_Windows_WinINet_1222_0(Etw):
    pattern = Struct(
        "TargetSize" / Int64sl,
        "Filter" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1227, version=0)
class Microsoft_Windows_WinINet_1227_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Prefix" / WString,
        "Directory" / WString,
        "RootPath" / WString,
        "Limit" / Int64sl,
        "Options" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1228, version=0)
class Microsoft_Windows_WinINet_1228_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Prefix" / WString,
        "Directory" / WString,
        "RootPath" / WString,
        "Limit" / Int64sl,
        "Options" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1229, version=0)
class Microsoft_Windows_WinINet_1229_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "RootPath" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1230, version=0)
class Microsoft_Windows_WinINet_1230_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "RootPath" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1231, version=0)
class Microsoft_Windows_WinINet_1231_0(Etw):
    pattern = Struct(
        "RootPath" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1232, version=0)
class Microsoft_Windows_WinINet_1232_0(Etw):
    pattern = Struct(
        "RootPath" / WString
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1233, version=0)
class Microsoft_Windows_WinINet_1233_0(Etw):
    pattern = Struct(
        "LimitType" / Int32ul,
        "Limit" / Int64sl
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1234, version=0)
class Microsoft_Windows_WinINet_1234_0(Etw):
    pattern = Struct(
        "LimitType" / Int32ul,
        "Limit" / Int64sl
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1235, version=0)
class Microsoft_Windows_WinINet_1235_0(Etw):
    pattern = Struct(
        "LimitType" / Int32ul
    )


@declare(guid=guid("43d1a55c-76d6-4f7e-995c-64c711e5cafe"), event_id=1236, version=0)
class Microsoft_Windows_WinINet_1236_0(Etw):
    pattern = Struct(
        "LimitType" / Int32ul
    )

