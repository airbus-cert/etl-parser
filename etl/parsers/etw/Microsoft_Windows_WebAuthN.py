# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WebAuthN
GUID : 3ae1ea61-c002-47fb-b06c-4022a8c98929
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1000, version=0)
class Microsoft_Windows_WebAuthN_1000_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1001, version=0)
class Microsoft_Windows_WebAuthN_1001_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1002, version=0)
class Microsoft_Windows_WebAuthN_1002_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Error" / Int32ul,
        "HResult" / Int32sl
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1003, version=0)
class Microsoft_Windows_WebAuthN_1003_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1004, version=0)
class Microsoft_Windows_WebAuthN_1004_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1005, version=0)
class Microsoft_Windows_WebAuthN_1005_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Error" / Int32ul,
        "HResult" / Int32sl
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1006, version=0)
class Microsoft_Windows_WebAuthN_1006_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "TicketLength" / Int32ul,
        "Ticket" / Bytes(lambda this: this.TicketLength)
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1007, version=0)
class Microsoft_Windows_WebAuthN_1007_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1008, version=0)
class Microsoft_Windows_WebAuthN_1008_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Error" / Int32ul,
        "HResult" / Int32sl
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1020, version=0)
class Microsoft_Windows_WebAuthN_1020_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1021, version=0)
class Microsoft_Windows_WebAuthN_1021_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1022, version=0)
class Microsoft_Windows_WebAuthN_1022_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Error" / Int32ul,
        "HResult" / Int32sl
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1023, version=0)
class Microsoft_Windows_WebAuthN_1023_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1024, version=0)
class Microsoft_Windows_WebAuthN_1024_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1025, version=0)
class Microsoft_Windows_WebAuthN_1025_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Error" / Int32ul,
        "HResult" / Int32sl
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1040, version=0)
class Microsoft_Windows_WebAuthN_1040_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "RpId" / WString,
        "AccountId" / WString,
        "ClientDataHashAlgId" / WString,
        "ClientDataLength" / Int32ul,
        "ClientDataHashLength" / Int32ul,
        "ClientDataHash" / Bytes(lambda this: this.ClientDataHashLength),
        "CredentialCount" / Int32ul,
        "CredentialParameterCount" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1041, version=0)
class Microsoft_Windows_WebAuthN_1041_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "AttestationFormatType" / WString,
        "RpIdHashLength" / Int32ul,
        "RpIdHash" / Bytes(lambda this: this.RpIdHashLength),
        "Flags" / Int32ul,
        "SignCount" / Int32ul,
        "AAGuid" / Guid,
        "CredentialIdLength" / Int32ul,
        "CredentialId" / Bytes(lambda this: this.CredentialIdLength),
        "U2fPublicKey" / Int8ul,
        "PublicKeyLength" / Int32ul,
        "PublicKey" / Bytes(lambda this: this.PublicKeyLength),
        "ResponseLength" / Int32ul,
        "Response" / Bytes(lambda this: this.ResponseLength)
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1042, version=0)
class Microsoft_Windows_WebAuthN_1042_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "RpId" / WString,
        "ClientDataHashAlgId" / WString,
        "ClientDataLength" / Int32ul,
        "ClientDataHashLength" / Int32ul,
        "ClientDataHash" / Bytes(lambda this: this.ClientDataHashLength),
        "CredentialCount" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1043, version=0)
class Microsoft_Windows_WebAuthN_1043_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "RpIdHashLength" / Int32ul,
        "RpIdHash" / Bytes(lambda this: this.RpIdHashLength),
        "Flags" / Int32ul,
        "SignCount" / Int32ul,
        "CredentialIdLength" / Int32ul,
        "CredentialId" / Bytes(lambda this: this.CredentialIdLength)
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1060, version=0)
class Microsoft_Windows_WebAuthN_1060_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Action" / CString,
        "Error" / Int32ul,
        "HResult" / Int32sl
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1100, version=0)
class Microsoft_Windows_WebAuthN_1100_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Function" / CString,
        "CborError" / Int32sl,
        "CborErrorString" / CString,
        "ErrorOffset" / Int32ul,
        "LineNumber" / Int32ul,
        "EncodedLength" / Int32ul,
        "Encoded" / Bytes(lambda this: this.EncodedLength)
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1101, version=0)
class Microsoft_Windows_WebAuthN_1101_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "RpId" / WString,
        "UserIdLength" / Int32ul,
        "UserId" / Bytes(lambda this: this.UserIdLength),
        "ClientDataHashAlgId" / WString,
        "ClientDataLength" / Int32ul,
        "ClientDataHashLength" / Int32ul,
        "ClientDataHash" / Bytes(lambda this: this.ClientDataHashLength),
        "RequireResidentKey" / Int8ul,
        "CredentialCount" / Int32ul,
        "CredentialParameterCount" / Int32ul,
        "RequestLength" / Int32ul,
        "Request" / Bytes(lambda this: this.RequestLength)
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1102, version=0)
class Microsoft_Windows_WebAuthN_1102_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "AttestationFormatType" / WString,
        "RpIdHashLength" / Int32ul,
        "RpIdHash" / Bytes(lambda this: this.RpIdHashLength),
        "Flags" / Int32ul,
        "SignCount" / Int32ul,
        "AAGuid" / Guid,
        "CredentialIdLength" / Int32ul,
        "CredentialId" / Bytes(lambda this: this.CredentialIdLength),
        "U2fPublicKey" / Int8ul,
        "PublicKeyLength" / Int32ul,
        "PublicKey" / Bytes(lambda this: this.PublicKeyLength),
        "ResponseLength" / Int32ul,
        "Response" / Bytes(lambda this: this.ResponseLength)
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1103, version=0)
class Microsoft_Windows_WebAuthN_1103_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "RpId" / WString,
        "ClientDataHashAlgId" / WString,
        "ClientDataLength" / Int32ul,
        "ClientDataHashLength" / Int32ul,
        "ClientDataHash" / Bytes(lambda this: this.ClientDataHashLength),
        "CredentialCount" / Int32ul,
        "RequestLength" / Int32ul,
        "Request" / Bytes(lambda this: this.RequestLength)
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=1104, version=0)
class Microsoft_Windows_WebAuthN_1104_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "RpIdHashLength" / Int32ul,
        "RpIdHash" / Bytes(lambda this: this.RpIdHashLength),
        "Flags" / Int32ul,
        "SignCount" / Int32ul,
        "CredentialIdLength" / Int32ul,
        "CredentialId" / Bytes(lambda this: this.CredentialIdLength),
        "ResponseLength" / Int32ul,
        "Response" / Bytes(lambda this: this.ResponseLength)
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2100, version=0)
class Microsoft_Windows_WebAuthN_2100_0(Etw):
    pattern = Struct(
        "Command" / WString,
        "TransactionId" / Guid,
        "Flags" / Int32ul,
        "TimeoutMilliseconds" / Int32ul,
        "TicketLength" / Int32ul,
        "Ticket" / Bytes(lambda this: this.TicketLength),
        "RequestLength" / Int32ul,
        "Request" / Bytes(lambda this: this.RequestLength)
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2101, version=0)
class Microsoft_Windows_WebAuthN_2101_0(Etw):
    pattern = Struct(
        "RequestLength" / Int32ul,
        "Request" / Bytes(lambda this: this.RequestLength)
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2102, version=0)
class Microsoft_Windows_WebAuthN_2102_0(Etw):
    pattern = Struct(
        "Command" / WString,
        "TransactionId" / Guid,
        "ResponseLength" / Int32ul,
        "Response" / Bytes(lambda this: this.ResponseLength)
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2103, version=0)
class Microsoft_Windows_WebAuthN_2103_0(Etw):
    pattern = Struct(
        "Command" / WString,
        "TransactionId" / Guid,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2104, version=0)
class Microsoft_Windows_WebAuthN_2104_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "ProviderName" / WString,
        "DevicePath" / WString,
        "Manufacturer" / WString,
        "Product" / WString,
        "AAGuid" / Guid,
        "U2fProtocol" / Int8ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2105, version=0)
class Microsoft_Windows_WebAuthN_2105_0(Etw):
    pattern = Struct(
        "Function" / CString,
        "Location" / CString,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2106, version=0)
class Microsoft_Windows_WebAuthN_2106_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2110, version=0)
class Microsoft_Windows_WebAuthN_2110_0(Etw):
    pattern = Struct(
        "Transport" / Int32ul,
        "WnfState" / Int32ul,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2111, version=0)
class Microsoft_Windows_WebAuthN_2111_0(Etw):
    pattern = Struct(
        "Transport" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2200, version=0)
class Microsoft_Windows_WebAuthN_2200_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2201, version=0)
class Microsoft_Windows_WebAuthN_2201_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2202, version=0)
class Microsoft_Windows_WebAuthN_2202_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2203, version=0)
class Microsoft_Windows_WebAuthN_2203_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2210, version=0)
class Microsoft_Windows_WebAuthN_2210_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "DevicePath" / WString,
        "Manufacturer" / WString,
        "Product" / WString
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2211, version=0)
class Microsoft_Windows_WebAuthN_2211_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "DevicePath" / WString,
        "Manufacturer" / WString,
        "Product" / WString,
        "AAGuid" / Guid,
        "U2fProtocol" / Int8ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2212, version=0)
class Microsoft_Windows_WebAuthN_2212_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "DevicePath" / WString,
        "Manufacturer" / WString,
        "Product" / WString,
        "AAGuid" / Guid,
        "U2fProtocol" / Int8ul,
        "State" / Int32ul,
        "Status" / Int32ul,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2213, version=0)
class Microsoft_Windows_WebAuthN_2213_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "DevicePath" / WString,
        "Manufacturer" / WString,
        "Product" / WString,
        "AAGuid" / Guid,
        "U2fProtocol" / Int8ul,
        "State" / Int32ul,
        "Status" / Int32ul,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2220, version=0)
class Microsoft_Windows_WebAuthN_2220_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "DevicePath" / WString,
        "Manufacturer" / WString,
        "Product" / WString
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2221, version=0)
class Microsoft_Windows_WebAuthN_2221_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "DevicePath" / WString,
        "Manufacturer" / WString,
        "Product" / WString
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2222, version=0)
class Microsoft_Windows_WebAuthN_2222_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2223, version=0)
class Microsoft_Windows_WebAuthN_2223_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "DevicePath" / WString,
        "Manufacturer" / WString,
        "Product" / WString
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2224, version=0)
class Microsoft_Windows_WebAuthN_2224_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "DevicePath" / WString,
        "Manufacturer" / WString,
        "Product" / WString,
        "DeviceErr" / Int32ul,
        "Status" / Int32ul,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2225, version=0)
class Microsoft_Windows_WebAuthN_2225_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "RequestCommand" / Int8ul,
        "RequestLength" / Int32ul,
        "Request" / Bytes(lambda this: this.RequestLength),
        "ResponseCommand" / Int8ul,
        "ResponseLength" / Int32ul,
        "Response" / Bytes(lambda this: this.ResponseLength)
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2226, version=0)
class Microsoft_Windows_WebAuthN_2226_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "RequestCommand" / Int8ul,
        "RequestLength" / Int32ul,
        "Request" / Bytes(lambda this: this.RequestLength),
        "ResponseCommand" / Int8ul,
        "ResponseLength" / Int32ul,
        "Response" / Bytes(lambda this: this.ResponseLength),
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2250, version=0)
class Microsoft_Windows_WebAuthN_2250_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2251, version=0)
class Microsoft_Windows_WebAuthN_2251_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2252, version=0)
class Microsoft_Windows_WebAuthN_2252_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2253, version=0)
class Microsoft_Windows_WebAuthN_2253_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2260, version=0)
class Microsoft_Windows_WebAuthN_2260_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "DevicePath" / WString,
        "PairedName" / WString
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2261, version=0)
class Microsoft_Windows_WebAuthN_2261_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "DevicePath" / WString,
        "PairedName" / WString,
        "AAGuid" / Guid,
        "U2fProtocol" / Int8ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2262, version=0)
class Microsoft_Windows_WebAuthN_2262_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "DevicePath" / WString,
        "PairedName" / WString,
        "AAGuid" / Guid,
        "U2fProtocol" / Int8ul,
        "State" / Int32ul,
        "Status" / Int32ul,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2263, version=0)
class Microsoft_Windows_WebAuthN_2263_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "DevicePath" / WString,
        "PairedName" / WString,
        "AAGuid" / Guid,
        "U2fProtocol" / Int8ul,
        "State" / Int32ul,
        "Status" / Int32ul,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2270, version=0)
class Microsoft_Windows_WebAuthN_2270_0(Etw):
    pattern = Struct(
        "Function" / CString,
        "Location" / CString,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2271, version=0)
class Microsoft_Windows_WebAuthN_2271_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "DevicePath" / WString,
        "PairedName" / WString
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2272, version=0)
class Microsoft_Windows_WebAuthN_2272_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "RequestCommand" / Int8ul,
        "RequestLength" / Int32ul,
        "Request" / Bytes(lambda this: this.RequestLength),
        "ResponseCommand" / Int8ul,
        "ResponseLength" / Int32ul,
        "Response" / Bytes(lambda this: this.ResponseLength)
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2273, version=0)
class Microsoft_Windows_WebAuthN_2273_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "RequestCommand" / Int8ul,
        "RequestLength" / Int32ul,
        "Request" / Bytes(lambda this: this.RequestLength),
        "ResponseCommand" / Int8ul,
        "ResponseLength" / Int32ul,
        "Response" / Bytes(lambda this: this.ResponseLength),
        "Location" / CString,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2300, version=0)
class Microsoft_Windows_WebAuthN_2300_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2301, version=0)
class Microsoft_Windows_WebAuthN_2301_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2302, version=0)
class Microsoft_Windows_WebAuthN_2302_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2303, version=0)
class Microsoft_Windows_WebAuthN_2303_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2310, version=0)
class Microsoft_Windows_WebAuthN_2310_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Reader" / WString
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2311, version=0)
class Microsoft_Windows_WebAuthN_2311_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Reader" / WString,
        "AAGuid" / Guid,
        "U2fProtocol" / Int8ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2312, version=0)
class Microsoft_Windows_WebAuthN_2312_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Reader" / WString,
        "AAGuid" / Guid,
        "U2fProtocol" / Int8ul,
        "State" / Int32ul,
        "Status" / Int32ul,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2313, version=0)
class Microsoft_Windows_WebAuthN_2313_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Reader" / WString,
        "AAGuid" / Guid,
        "U2fProtocol" / Int8ul,
        "State" / Int32ul,
        "Status" / Int32ul,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2314, version=0)
class Microsoft_Windows_WebAuthN_2314_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2315, version=0)
class Microsoft_Windows_WebAuthN_2315_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "NumberOfTimesScardCancelCommandsSent" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2316, version=0)
class Microsoft_Windows_WebAuthN_2316_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "CallCancelled" / Int8ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2320, version=0)
class Microsoft_Windows_WebAuthN_2320_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Reader" / WString
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2321, version=0)
class Microsoft_Windows_WebAuthN_2321_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Action" / CString,
        "Reader" / WString,
        "DeviceInstanceId" / WString
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2322, version=0)
class Microsoft_Windows_WebAuthN_2322_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Action" / CString,
        "Reader" / WString
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2323, version=0)
class Microsoft_Windows_WebAuthN_2323_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Action" / CString,
        "Reader" / WString,
        "ApduStatus" / Int16ul,
        "DeviceStatus" / Int32ul,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2324, version=0)
class Microsoft_Windows_WebAuthN_2324_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Action" / CString,
        "Reader" / WString,
        "ApduStatus" / Int16ul,
        "DeviceStatus" / Int32ul,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2325, version=0)
class Microsoft_Windows_WebAuthN_2325_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Reader" / WString
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2326, version=0)
class Microsoft_Windows_WebAuthN_2326_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Action" / CString,
        "Reader" / WString
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2327, version=0)
class Microsoft_Windows_WebAuthN_2327_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Reader" / WString,
        "RequestLength" / Int32ul,
        "Request" / Bytes(lambda this: this.RequestLength),
        "ResponseLength" / Int32ul,
        "Response" / Bytes(lambda this: this.ResponseLength),
        "ApduStatus" / Int16ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2328, version=0)
class Microsoft_Windows_WebAuthN_2328_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Reader" / WString,
        "RequestLength" / Int32ul,
        "Request" / Bytes(lambda this: this.RequestLength),
        "ResponseLength" / Int32ul,
        "Response" / Bytes(lambda this: this.ResponseLength),
        "ApduStatus" / Int16ul,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2400, version=0)
class Microsoft_Windows_WebAuthN_2400_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2401, version=0)
class Microsoft_Windows_WebAuthN_2401_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid
    )


@declare(guid=guid("3ae1ea61-c002-47fb-b06c-4022a8c98929"), event_id=2402, version=0)
class Microsoft_Windows_WebAuthN_2402_0(Etw):
    pattern = Struct(
        "TransactionId" / Guid,
        "Error" / Int32ul,
        "Win32Error" / Int32ul
    )

