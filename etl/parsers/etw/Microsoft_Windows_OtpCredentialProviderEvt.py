# -*- coding: utf-8 -*-
"""
Microsoft-Windows-OtpCredentialProviderEvt
GUID : 5cad485a-210f-4c16-80c5-f892de74e28d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5cad485a-210f-4c16-80c5-f892de74e28d"), event_id=10000, version=0)
class Microsoft_Windows_OtpCredentialProviderEvt_10000_0(Etw):
    pattern = Struct(
        "serverAddress" / WString,
        "path" / WString,
        "port" / Int32ul,
        "errCode" / Int32ul
    )


@declare(guid=guid("5cad485a-210f-4c16-80c5-f892de74e28d"), event_id=10001, version=0)
class Microsoft_Windows_OtpCredentialProviderEvt_10001_0(Etw):
    pattern = Struct(
        "serverAddress" / WString,
        "path" / WString,
        "port" / Int32ul,
        "errCode" / Int32ul
    )


@declare(guid=guid("5cad485a-210f-4c16-80c5-f892de74e28d"), event_id=10002, version=0)
class Microsoft_Windows_OtpCredentialProviderEvt_10002_0(Etw):
    pattern = Struct(
        "serverAddress" / WString,
        "path" / WString,
        "port" / Int32ul,
        "errCode" / Int32ul
    )


@declare(guid=guid("5cad485a-210f-4c16-80c5-f892de74e28d"), event_id=10003, version=0)
class Microsoft_Windows_OtpCredentialProviderEvt_10003_0(Etw):
    pattern = Struct(
        "user" / WString,
        "templateName" / WString
    )


@declare(guid=guid("5cad485a-210f-4c16-80c5-f892de74e28d"), event_id=10004, version=0)
class Microsoft_Windows_OtpCredentialProviderEvt_10004_0(Etw):
    pattern = Struct(
        "errorCode" / WString
    )


@declare(guid=guid("5cad485a-210f-4c16-80c5-f892de74e28d"), event_id=10005, version=0)
class Microsoft_Windows_OtpCredentialProviderEvt_10005_0(Etw):
    pattern = Struct(
        "user" / WString,
        "serverAddress" / WString,
        "errorCode" / WString
    )


@declare(guid=guid("5cad485a-210f-4c16-80c5-f892de74e28d"), event_id=10006, version=0)
class Microsoft_Windows_OtpCredentialProviderEvt_10006_0(Etw):
    pattern = Struct(
        "user" / WString,
        "serverAddress" / WString,
        "errorCode" / WString
    )


@declare(guid=guid("5cad485a-210f-4c16-80c5-f892de74e28d"), event_id=10007, version=0)
class Microsoft_Windows_OtpCredentialProviderEvt_10007_0(Etw):
    pattern = Struct(
        "errorCode" / WString
    )


@declare(guid=guid("5cad485a-210f-4c16-80c5-f892de74e28d"), event_id=10008, version=0)
class Microsoft_Windows_OtpCredentialProviderEvt_10008_0(Etw):
    pattern = Struct(
        "user" / WString
    )


@declare(guid=guid("5cad485a-210f-4c16-80c5-f892de74e28d"), event_id=10011, version=0)
class Microsoft_Windows_OtpCredentialProviderEvt_10011_0(Etw):
    pattern = Struct(
        "user" / WString,
        "errorCode" / WString
    )


@declare(guid=guid("5cad485a-210f-4c16-80c5-f892de74e28d"), event_id=10012, version=0)
class Microsoft_Windows_OtpCredentialProviderEvt_10012_0(Etw):
    pattern = Struct(
        "user" / WString,
        "errorCode" / WString
    )


@declare(guid=guid("5cad485a-210f-4c16-80c5-f892de74e28d"), event_id=10013, version=0)
class Microsoft_Windows_OtpCredentialProviderEvt_10013_0(Etw):
    pattern = Struct(
        "errorCode" / WString
    )


@declare(guid=guid("5cad485a-210f-4c16-80c5-f892de74e28d"), event_id=10014, version=0)
class Microsoft_Windows_OtpCredentialProviderEvt_10014_0(Etw):
    pattern = Struct(
        "errorCode" / WString
    )


@declare(guid=guid("5cad485a-210f-4c16-80c5-f892de74e28d"), event_id=10015, version=0)
class Microsoft_Windows_OtpCredentialProviderEvt_10015_0(Etw):
    pattern = Struct(
        "errorCode" / WString
    )


@declare(guid=guid("5cad485a-210f-4c16-80c5-f892de74e28d"), event_id=10018, version=0)
class Microsoft_Windows_OtpCredentialProviderEvt_10018_0(Etw):
    pattern = Struct(
        "OTPUserName" / WString,
        "CAName" / WString
    )


@declare(guid=guid("5cad485a-210f-4c16-80c5-f892de74e28d"), event_id=10019, version=0)
class Microsoft_Windows_OtpCredentialProviderEvt_10019_0(Etw):
    pattern = Struct(
        "OTPUserName" / WString,
        "CAName" / WString
    )


@declare(guid=guid("5cad485a-210f-4c16-80c5-f892de74e28d"), event_id=10022, version=0)
class Microsoft_Windows_OtpCredentialProviderEvt_10022_0(Etw):
    pattern = Struct(
        "CAName" / WString
    )

