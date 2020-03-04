# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Security-UserConsentVerifier
GUID : 40783728-8921-45d0-b231-919037b4b4fd
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("40783728-8921-45d0-b231-919037b4b4fd"), event_id=100, version=0)
class Microsoft_Windows_Security_UserConsentVerifier_100_0(Etw):
    pattern = Struct(
        "AppName" / WString,
        "AppMessage" / WString
    )


@declare(guid=guid("40783728-8921-45d0-b231-919037b4b4fd"), event_id=101, version=0)
class Microsoft_Windows_Security_UserConsentVerifier_101_0(Etw):
    pattern = Struct(
        "AppName" / WString,
        "AppMessage" / WString,
        "VerificationResult" / Int32ul
    )

