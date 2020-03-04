# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Mobile-Broadband-Experience-Parser-Task
GUID : 28e25b07-c47f-473d-8b24-2e171cca808a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1000, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1000_0(Etw):
    pattern = Struct(
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1002, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1002_0(Etw):
    pattern = Struct(
        "id" / WString,
        "culture" / WString
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1003, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1003_0(Etw):
    pattern = Struct(
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1004, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1004_0(Etw):
    pattern = Struct(
        "id" / WString,
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1005, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1005_0(Etw):
    pattern = Struct(
        "path" / WString,
        "error" / WString
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1006, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1006_0(Etw):
    pattern = Struct(
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1007, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1007_0(Etw):
    pattern = Struct(
        "tag" / WString
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1008, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1008_0(Etw):
    pattern = Struct(
        "tag" / WString
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1009, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1009_0(Etw):
    pattern = Struct(
        "tag" / WString,
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1010, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1010_0(Etw):
    pattern = Struct(
        "path" / WString,
        "error" / WString
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1011, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1011_0(Etw):
    pattern = Struct(
        "profile" / WString,
        "path" / WString,
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1012, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1012_0(Etw):
    pattern = Struct(
        "profile" / WString,
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1013, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1013_0(Etw):
    pattern = Struct(
        "profile" / WString,
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1014, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1014_0(Etw):
    pattern = Struct(
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1015, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1015_0(Etw):
    pattern = Struct(
        "id" / WString
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1016, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1016_0(Etw):
    pattern = Struct(
        "id" / WString,
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1017, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1017_0(Etw):
    pattern = Struct(
        "profile" / WString,
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1020, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1020_0(Etw):
    pattern = Struct(
        "providerName" / WString
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1021, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1021_0(Etw):
    pattern = Struct(
        "providerName" / WString
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1022, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1022_0(Etw):
    pattern = Struct(
        "id" / WString
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1023, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1023_0(Etw):
    pattern = Struct(
        "id" / WString
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1030, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1030_0(Etw):
    pattern = Struct(
        "providerName" / WString
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1031, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1031_0(Etw):
    pattern = Struct(
        "providerName" / WString
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1032, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1032_0(Etw):
    pattern = Struct(
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1033, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1033_0(Etw):
    pattern = Struct(
        "culture" / WString
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=1034, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_1034_0(Etw):
    pattern = Struct(
        "culture" / WString
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=2001, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_2001_0(Etw):
    pattern = Struct(
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=3000, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_3000_0(Etw):
    pattern = Struct(
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=3001, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_3001_0(Etw):
    pattern = Struct(
        "path" / WString
    )


@declare(guid=guid("28e25b07-c47f-473d-8b24-2e171cca808a"), event_id=3002, version=0)
class Microsoft_Windows_Mobile_Broadband_Experience_Parser_Task_3002_0(Etw):
    pattern = Struct(
        "path" / WString,
        "error" / Int32ul,
        "hresult" / Int32sl
    )

