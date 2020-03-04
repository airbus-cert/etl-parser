# -*- coding: utf-8 -*-
"""
Microsoft-Windows-AppID
GUID : 3cb2a168-fe19-4a4e-bdad-dcf422f13473
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3cb2a168-fe19-4a4e-bdad-dcf422f13473"), event_id=4001, version=0)
class Microsoft_Windows_AppID_4001_0(Etw):
    pattern = Struct(
        "FilePathLength" / Int16ul,
        "FilePathBuffer" / Bytes(lambda this: this.FilePathLength),
        "Status" / Int32ul
    )


@declare(guid=guid("3cb2a168-fe19-4a4e-bdad-dcf422f13473"), event_id=4002, version=0)
class Microsoft_Windows_AppID_4002_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("3cb2a168-fe19-4a4e-bdad-dcf422f13473"), event_id=4003, version=0)
class Microsoft_Windows_AppID_4003_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("3cb2a168-fe19-4a4e-bdad-dcf422f13473"), event_id=4004, version=0)
class Microsoft_Windows_AppID_4004_0(Etw):
    pattern = Struct(
        "FilePathLength" / Int16ul,
        "FilePathBuffer" / Bytes(lambda this: this.FilePathLength),
        "PublisherNameLength" / Int16ul,
        "PublisherNameBuffer" / Bytes(lambda this: this.PublisherNameLength),
        "Status" / Int32ul
    )


@declare(guid=guid("3cb2a168-fe19-4a4e-bdad-dcf422f13473"), event_id=4005, version=0)
class Microsoft_Windows_AppID_4005_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("3cb2a168-fe19-4a4e-bdad-dcf422f13473"), event_id=4007, version=0)
class Microsoft_Windows_AppID_4007_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("3cb2a168-fe19-4a4e-bdad-dcf422f13473"), event_id=4008, version=0)
class Microsoft_Windows_AppID_4008_0(Etw):
    pattern = Struct(
        "CallingFunctionNameLength" / Int16ul,
        "CallingFunctionName" / Bytes(lambda this: this.CallingFunctionNameLength),
        "FunctionCallNameLength" / Int16ul,
        "FunctionCallName" / Bytes(lambda this: this.FunctionCallNameLength),
        "Status" / Int32ul
    )

