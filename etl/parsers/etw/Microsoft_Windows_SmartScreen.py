# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SmartScreen
GUID : 3cb2a168-fe34-4a4e-bdad-dcf422f34473
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3cb2a168-fe34-4a4e-bdad-dcf422f34473"), event_id=1000, version=0)
class Microsoft_Windows_SmartScreen_1000_0(Etw):
    pattern = Struct(
        "FilePath" / WString,
        "FullFileHash" / WString,
        "AuthenticodeHash" / WString,
        "AuthenticodeAlgorithm" / WString,
        "MarkOfTheWeb" / WString,
        "CallingProcessId" / Int32ul,
        "CallingProcessCreationTime" / Int64ul,
        "Sid" / WString,
        "ActivityId" / WString,
        "Enforcement" / WString,
        "Experience" / WString
    )


@declare(guid=guid("3cb2a168-fe34-4a4e-bdad-dcf422f34473"), event_id=1001, version=0)
class Microsoft_Windows_SmartScreen_1001_0(Etw):
    pattern = Struct(
        "Uri" / WString,
        "IP" / WString,
        "ReferrerUri" / WString,
        "ReferrerIP" / WString,
        "Recommendation" / WString,
        "HitType" / WString,
        "NavigationType" / WString,
        "ProductType" / WString,
        "CallingProcessId" / Int32ul,
        "CallingProcessCreationTime" / Int64ul,
        "Sid" / WString,
        "ActivityId" / WString,
        "Enforcement" / WString,
        "Experience" / WString
    )


@declare(guid=guid("3cb2a168-fe34-4a4e-bdad-dcf422f34473"), event_id=1002, version=0)
class Microsoft_Windows_SmartScreen_1002_0(Etw):
    pattern = Struct(
        "Action" / WString,
        "ActivitiyId" / WString
    )


@declare(guid=guid("3cb2a168-fe34-4a4e-bdad-dcf422f34473"), event_id=1003, version=0)
class Microsoft_Windows_SmartScreen_1003_0(Etw):
    pattern = Struct(
        "Data" / WString
    )

