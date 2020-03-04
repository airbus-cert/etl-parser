# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Mobile-Broadband-Experience-SmsApi
GUID : 0ff1c24b-7f05-45c0-abdc-3c8521be4f62
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("0ff1c24b-7f05-45c0-abdc-3c8521be4f62"), event_id=5001, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_SmsApi_5001_0(Etw):
    pattern = Struct(
        "appId" / WString,
        "interfaceId" / WString
    )


@declare(guid=guid("0ff1c24b-7f05-45c0-abdc-3c8521be4f62"), event_id=5002, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_SmsApi_5002_0(Etw):
    pattern = Struct(
        "appId" / WString,
        "interfaceId" / WString
    )


@declare(guid=guid("0ff1c24b-7f05-45c0-abdc-3c8521be4f62"), event_id=5003, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_SmsApi_5003_0(Etw):
    pattern = Struct(
        "appId" / WString,
        "interfaceId" / WString
    )

