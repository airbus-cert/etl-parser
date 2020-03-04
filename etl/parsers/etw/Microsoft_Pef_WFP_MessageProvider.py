# -*- coding: utf-8 -*-
"""
Microsoft-Pef-WFP-MessageProvider
GUID : c22d1b14-c242-49de-9f17-1d76b8b9c458
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c22d1b14-c242-49de-9f17-1d76b8b9c458"), event_id=2000, version=0)
class Microsoft_Pef_WFP_MessageProvider_2000_0(Etw):
    pattern = Struct(
        "FragmentEventId" / Int16ul,
        "GroupId" / Int32ul,
        "ByteLength" / Int32ul,
        "Payload" / Bytes(lambda this: this.ByteLength)
    )


@declare(guid=guid("c22d1b14-c242-49de-9f17-1d76b8b9c458"), event_id=10001, version=0)
class Microsoft_Pef_WFP_MessageProvider_10001_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "MajorVersion" / Int16ul,
        "MinorVersion" / Int16ul
    )


@declare(guid=guid("c22d1b14-c242-49de-9f17-1d76b8b9c458"), event_id=10002, version=0)
class Microsoft_Pef_WFP_MessageProvider_10002_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "MajorVersion" / Int16ul,
        "MinorVersion" / Int16ul
    )


@declare(guid=guid("c22d1b14-c242-49de-9f17-1d76b8b9c458"), event_id=10003, version=0)
class Microsoft_Pef_WFP_MessageProvider_10003_0(Etw):
    pattern = Struct(
        "Callout" / Int32ul
    )


@declare(guid=guid("c22d1b14-c242-49de-9f17-1d76b8b9c458"), event_id=10004, version=0)
class Microsoft_Pef_WFP_MessageProvider_10004_0(Etw):
    pattern = Struct(
        "Callout" / Int32ul
    )


@declare(guid=guid("c22d1b14-c242-49de-9f17-1d76b8b9c458"), event_id=10005, version=0)
class Microsoft_Pef_WFP_MessageProvider_10005_0(Etw):
    pattern = Struct(
        "FilterId" / Int64ul,
        "Callout" / Int32ul,
        "FilterWeight" / Int64ul
    )


@declare(guid=guid("c22d1b14-c242-49de-9f17-1d76b8b9c458"), event_id=10006, version=0)
class Microsoft_Pef_WFP_MessageProvider_10006_0(Etw):
    pattern = Struct(
        "FilterId" / Int64ul,
        "Callout" / Int32ul,
        "FilterWeight" / Int64ul
    )


@declare(guid=guid("c22d1b14-c242-49de-9f17-1d76b8b9c458"), event_id=20001, version=0)
class Microsoft_Pef_WFP_MessageProvider_20001_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString,
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("c22d1b14-c242-49de-9f17-1d76b8b9c458"), event_id=20002, version=0)
class Microsoft_Pef_WFP_MessageProvider_20002_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString,
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("c22d1b14-c242-49de-9f17-1d76b8b9c458"), event_id=20003, version=0)
class Microsoft_Pef_WFP_MessageProvider_20003_0(Etw):
    pattern = Struct(
        "Callout" / Int32ul,
        "ErrorMessage" / WString,
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("c22d1b14-c242-49de-9f17-1d76b8b9c458"), event_id=20004, version=0)
class Microsoft_Pef_WFP_MessageProvider_20004_0(Etw):
    pattern = Struct(
        "Callout" / Int32ul,
        "ErrorMessage" / WString,
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("c22d1b14-c242-49de-9f17-1d76b8b9c458"), event_id=20005, version=0)
class Microsoft_Pef_WFP_MessageProvider_20005_0(Etw):
    pattern = Struct(
        "Callout" / Int32ul,
        "ErrorMessage" / WString,
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("c22d1b14-c242-49de-9f17-1d76b8b9c458"), event_id=60011, version=0)
class Microsoft_Pef_WFP_MessageProvider_60011_0(Etw):
    pattern = Struct(
        "SourceAddress" / Int32ul,
        "DestinationAddress" / Int32ul,
        "Protocol" / Int8ul,
        "ByteLength" / Int16ul,
        "MessageFrame" / Bytes(lambda this: this.ByteLength)
    )


@declare(guid=guid("c22d1b14-c242-49de-9f17-1d76b8b9c458"), event_id=60012, version=0)
class Microsoft_Pef_WFP_MessageProvider_60012_0(Etw):
    pattern = Struct(
        "SourceAddress" / Int32ul,
        "DestinationAddress" / Int32ul,
        "Protocol" / Int8ul,
        "FlowHandle" / Int64ul,
        "ByteLength" / Int16ul,
        "MessageFrame" / Bytes(lambda this: this.ByteLength)
    )


@declare(guid=guid("c22d1b14-c242-49de-9f17-1d76b8b9c458"), event_id=60021, version=0)
class Microsoft_Pef_WFP_MessageProvider_60021_0(Etw):
    pattern = Struct(
        "Protocol" / Int8ul,
        "ByteLength" / Int16ul,
        "MessageFrame" / Bytes(lambda this: this.ByteLength)
    )


@declare(guid=guid("c22d1b14-c242-49de-9f17-1d76b8b9c458"), event_id=60022, version=0)
class Microsoft_Pef_WFP_MessageProvider_60022_0(Etw):
    pattern = Struct(
        "Protocol" / Int8ul,
        "FlowHandle" / Int64ul,
        "ByteLength" / Int16ul,
        "MessageFrame" / Bytes(lambda this: this.ByteLength)
    )


@declare(guid=guid("c22d1b14-c242-49de-9f17-1d76b8b9c458"), event_id=60031, version=0)
class Microsoft_Pef_WFP_MessageProvider_60031_0(Etw):
    pattern = Struct(
        "SourceAddress" / Int32ul,
        "DestinationAddress" / Int32ul,
        "SourcePort" / Int16ul,
        "DestinationPort" / Int16ul,
        "Luid" / Int64ul,
        "Direction" / Int8ul,
        "Protocol" / Int8ul,
        "FlowHandle" / Int64ul,
        "ProcessId" / Int64ul,
        "ByteLength" / Int16ul,
        "ProcessPath" / Bytes(lambda this: this.ByteLength)
    )


@declare(guid=guid("c22d1b14-c242-49de-9f17-1d76b8b9c458"), event_id=60041, version=0)
class Microsoft_Pef_WFP_MessageProvider_60041_0(Etw):
    pattern = Struct(
        "SourcePort" / Int16ul,
        "DestinationPort" / Int16ul,
        "Luid" / Int64ul,
        "Direction" / Int8ul,
        "Protocol" / Int8ul,
        "FlowHandle" / Int64ul,
        "ProcessId" / Int64ul,
        "ByteLength" / Int16ul,
        "ProcessPath" / Bytes(lambda this: this.ByteLength)
    )


@declare(guid=guid("c22d1b14-c242-49de-9f17-1d76b8b9c458"), event_id=60050, version=0)
class Microsoft_Pef_WFP_MessageProvider_60050_0(Etw):
    pattern = Struct(
        "DiscardModule" / Int8ul,
        "DiscardReason" / Int32ul,
        "DiscardFilterID" / Int64ul
    )

