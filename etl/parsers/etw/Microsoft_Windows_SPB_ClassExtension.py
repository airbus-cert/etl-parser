# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SPB-ClassExtension
GUID : 72cd9ff7-4af8-4b89-aede-5f26fda13567
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("72cd9ff7-4af8-4b89-aede-5f26fda13567"), event_id=1000, version=1)
class Microsoft_Windows_SPB_ClassExtension_1000_1(Etw):
    pattern = Struct(
        "ControlDeviceName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("72cd9ff7-4af8-4b89-aede-5f26fda13567"), event_id=1001, version=1)
class Microsoft_Windows_SPB_ClassExtension_1001_1(Etw):
    pattern = Struct(
        "ControlDeviceName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("72cd9ff7-4af8-4b89-aede-5f26fda13567"), event_id=1010, version=1)
class Microsoft_Windows_SPB_ClassExtension_1010_1(Etw):
    pattern = Struct(
        "Controller" / Int64ul,
        "TargetName" / WString,
        "ScopeTag" / WString,
        "File" / Int64ul,
        "Request" / Int64ul,
        "RequestType" / Int8sl,
        "Length" / Int32ul
    )


@declare(guid=guid("72cd9ff7-4af8-4b89-aede-5f26fda13567"), event_id=1015, version=1)
class Microsoft_Windows_SPB_ClassExtension_1015_1(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "CompletionStatus" / Int32ul,
        "Information" / Int64ul
    )


@declare(guid=guid("72cd9ff7-4af8-4b89-aede-5f26fda13567"), event_id=1018, version=1)
class Microsoft_Windows_SPB_ClassExtension_1018_1(Etw):
    pattern = Struct(
        "Data" / Int8ul
    )


@declare(guid=guid("72cd9ff7-4af8-4b89-aede-5f26fda13567"), event_id=1019, version=1)
class Microsoft_Windows_SPB_ClassExtension_1019_1(Etw):
    pattern = Struct(
        "Controller" / Int64ul,
        "TargetName" / WString,
        "ScopeTag" / WString,
        "File" / Int64ul
    )


@declare(guid=guid("72cd9ff7-4af8-4b89-aede-5f26fda13567"), event_id=1020, version=1)
class Microsoft_Windows_SPB_ClassExtension_1020_1(Etw):
    pattern = Struct(
        "Controller" / Int64ul,
        "DeviceState" / Int32ul
    )


@declare(guid=guid("72cd9ff7-4af8-4b89-aede-5f26fda13567"), event_id=1021, version=1)
class Microsoft_Windows_SPB_ClassExtension_1021_1(Etw):
    pattern = Struct(
        "IoTotalByteCount" / Int64ul,
        "TransferCount" / Int32ul
    )


@declare(guid=guid("72cd9ff7-4af8-4b89-aede-5f26fda13567"), event_id=1022, version=1)
class Microsoft_Windows_SPB_ClassExtension_1022_1(Etw):
    pattern = Struct(
        "TransferIndex" / Int32ul,
        "TransferDirection" / Int32ul,
        "TransferTotalByteCount" / Int64ul
    )


@declare(guid=guid("72cd9ff7-4af8-4b89-aede-5f26fda13567"), event_id=1023, version=1)
class Microsoft_Windows_SPB_ClassExtension_1023_1(Etw):
    pattern = Struct(
        "BufferIndex" / Int32ul,
        "ByteCount" / Int32ul,
        "Buffer" / Bytes(lambda this: this.ByteCount)
    )

