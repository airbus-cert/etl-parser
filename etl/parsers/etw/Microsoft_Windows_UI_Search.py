# -*- coding: utf-8 -*-
"""
Microsoft-Windows-UI-Search
GUID : d8965fcf-7397-4e0e-b750-21a4580bd880
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d8965fcf-7397-4e0e-b750-21a4580bd880"), event_id=101, version=0)
class Microsoft_Windows_UI_Search_101_0(Etw):
    pattern = Struct(
        "XAMLView" / Int32ul
    )


@declare(guid=guid("d8965fcf-7397-4e0e-b750-21a4580bd880"), event_id=102, version=0)
class Microsoft_Windows_UI_Search_102_0(Etw):
    pattern = Struct(
        "XAMLView" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("d8965fcf-7397-4e0e-b750-21a4580bd880"), event_id=201, version=0)
class Microsoft_Windows_UI_Search_201_0(Etw):
    pattern = Struct(
        "ThreadID" / Int32ul,
        "XAMLView" / Int32ul
    )


@declare(guid=guid("d8965fcf-7397-4e0e-b750-21a4580bd880"), event_id=202, version=0)
class Microsoft_Windows_UI_Search_202_0(Etw):
    pattern = Struct(
        "ThreadID" / Int32ul,
        "XAMLView" / Int32ul
    )


@declare(guid=guid("d8965fcf-7397-4e0e-b750-21a4580bd880"), event_id=302, version=0)
class Microsoft_Windows_UI_Search_302_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("d8965fcf-7397-4e0e-b750-21a4580bd880"), event_id=402, version=0)
class Microsoft_Windows_UI_Search_402_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("d8965fcf-7397-4e0e-b750-21a4580bd880"), event_id=501, version=0)
class Microsoft_Windows_UI_Search_501_0(Etw):
    pattern = Struct(
        "ServiceIndex" / Int32ul
    )


@declare(guid=guid("d8965fcf-7397-4e0e-b750-21a4580bd880"), event_id=502, version=0)
class Microsoft_Windows_UI_Search_502_0(Etw):
    pattern = Struct(
        "ServiceIndex" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("d8965fcf-7397-4e0e-b750-21a4580bd880"), event_id=503, version=0)
class Microsoft_Windows_UI_Search_503_0(Etw):
    pattern = Struct(
        "ServiceIndex" / Int32ul
    )


@declare(guid=guid("d8965fcf-7397-4e0e-b750-21a4580bd880"), event_id=504, version=0)
class Microsoft_Windows_UI_Search_504_0(Etw):
    pattern = Struct(
        "ServiceIndex" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("d8965fcf-7397-4e0e-b750-21a4580bd880"), event_id=601, version=0)
class Microsoft_Windows_UI_Search_601_0(Etw):
    pattern = Struct(
        "XAMLView" / Int32ul
    )


@declare(guid=guid("d8965fcf-7397-4e0e-b750-21a4580bd880"), event_id=602, version=0)
class Microsoft_Windows_UI_Search_602_0(Etw):
    pattern = Struct(
        "XAMLView" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("d8965fcf-7397-4e0e-b750-21a4580bd880"), event_id=710, version=0)
class Microsoft_Windows_UI_Search_710_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("d8965fcf-7397-4e0e-b750-21a4580bd880"), event_id=711, version=0)
class Microsoft_Windows_UI_Search_711_0(Etw):
    pattern = Struct(
        "QueryString" / WString
    )


@declare(guid=guid("d8965fcf-7397-4e0e-b750-21a4580bd880"), event_id=910, version=0)
class Microsoft_Windows_UI_Search_910_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "Message" / WString
    )


@declare(guid=guid("d8965fcf-7397-4e0e-b750-21a4580bd880"), event_id=1001, version=0)
class Microsoft_Windows_UI_Search_1001_0(Etw):
    pattern = Struct(
        "Visibility" / Int32ul,
        "XAMLView" / Int32ul
    )


@declare(guid=guid("d8965fcf-7397-4e0e-b750-21a4580bd880"), event_id=1836, version=0)
class Microsoft_Windows_UI_Search_1836_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "LaunchMode" / Int32ul
    )

