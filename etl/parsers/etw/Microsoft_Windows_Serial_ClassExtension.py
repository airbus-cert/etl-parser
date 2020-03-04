# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Serial-ClassExtension
GUID : 47bc9477-a8ba-452e-b951-4f2ed3593cf9
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("47bc9477-a8ba-452e-b951-4f2ed3593cf9"), event_id=1000, version=1)
class Microsoft_Windows_Serial_ClassExtension_1000_1(Etw):
    pattern = Struct(
        "ControlDeviceName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("47bc9477-a8ba-452e-b951-4f2ed3593cf9"), event_id=1001, version=1)
class Microsoft_Windows_Serial_ClassExtension_1001_1(Etw):
    pattern = Struct(
        "ControlDeviceName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("47bc9477-a8ba-452e-b951-4f2ed3593cf9"), event_id=1002, version=1)
class Microsoft_Windows_Serial_ClassExtension_1002_1(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "IoControlCodeString" / WString
    )


@declare(guid=guid("47bc9477-a8ba-452e-b951-4f2ed3593cf9"), event_id=1003, version=1)
class Microsoft_Windows_Serial_ClassExtension_1003_1(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "IoControlCodeString" / WString
    )


@declare(guid=guid("47bc9477-a8ba-452e-b951-4f2ed3593cf9"), event_id=1004, version=1)
class Microsoft_Windows_Serial_ClassExtension_1004_1(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("47bc9477-a8ba-452e-b951-4f2ed3593cf9"), event_id=1005, version=1)
class Microsoft_Windows_Serial_ClassExtension_1005_1(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("47bc9477-a8ba-452e-b951-4f2ed3593cf9"), event_id=1006, version=1)
class Microsoft_Windows_Serial_ClassExtension_1006_1(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Length" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("47bc9477-a8ba-452e-b951-4f2ed3593cf9"), event_id=1007, version=1)
class Microsoft_Windows_Serial_ClassExtension_1007_1(Etw):
    pattern = Struct(
        "Data" / Int8ul
    )


@declare(guid=guid("47bc9477-a8ba-452e-b951-4f2ed3593cf9"), event_id=1008, version=1)
class Microsoft_Windows_Serial_ClassExtension_1008_1(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Queue" / Int64ul
    )

