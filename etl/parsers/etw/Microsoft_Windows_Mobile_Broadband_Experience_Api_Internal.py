# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Mobile-Broadband-Experience-Api-Internal
GUID : 2aabd03b-f48b-419a-b4ce-7a14403f4a46
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("2aabd03b-f48b-419a-b4ce-7a14403f4a46"), event_id=1000, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Api_Internal_1000_0(Etw):
    pattern = Struct(
        "interfaceId" / WString,
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("2aabd03b-f48b-419a-b4ce-7a14403f4a46"), event_id=1001, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Api_Internal_1001_0(Etw):
    pattern = Struct(
        "propName" / WString,
        "interfaceId" / WString,
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("2aabd03b-f48b-419a-b4ce-7a14403f4a46"), event_id=1002, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Api_Internal_1002_0(Etw):
    pattern = Struct(
        "interfaceId" / WString,
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("2aabd03b-f48b-419a-b4ce-7a14403f4a46"), event_id=1003, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Api_Internal_1003_0(Etw):
    pattern = Struct(
        "interfaceId" / WString,
        "appUserModelId" / WString
    )


@declare(guid=guid("2aabd03b-f48b-419a-b4ce-7a14403f4a46"), event_id=1004, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Api_Internal_1004_0(Etw):
    pattern = Struct(
        "interfaceId" / WString,
        "appPackageFamilyName" / WString
    )


@declare(guid=guid("2aabd03b-f48b-419a-b4ce-7a14403f4a46"), event_id=1005, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Api_Internal_1005_0(Etw):
    pattern = Struct(
        "appPackageFamilyName" / WString,
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("2aabd03b-f48b-419a-b4ce-7a14403f4a46"), event_id=1006, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Api_Internal_1006_0(Etw):
    pattern = Struct(
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("2aabd03b-f48b-419a-b4ce-7a14403f4a46"), event_id=1007, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Api_Internal_1007_0(Etw):
    pattern = Struct(
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("2aabd03b-f48b-419a-b4ce-7a14403f4a46"), event_id=1008, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Api_Internal_1008_0(Etw):
    pattern = Struct(
        "appUserModelId" / WString
    )


@declare(guid=guid("2aabd03b-f48b-419a-b4ce-7a14403f4a46"), event_id=1009, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Api_Internal_1009_0(Etw):
    pattern = Struct(
        "appUserModelId" / WString
    )

