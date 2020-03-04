# -*- coding: utf-8 -*-
"""
Microsoft-Windows-NDIS-PacketCapture
GUID : 2ed6006e-4729-4609-b423-3ee7bcd678ef
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("2ed6006e-4729-4609-b423-3ee7bcd678ef"), event_id=1001, version=0)
class Microsoft_Windows_NDIS_PacketCapture_1001_0(Etw):
    pattern = Struct(
        "MiniportIfIndex" / Int32ul,
        "LowerIfIndex" / Int32ul,
        "FragmentSize" / Int32ul,
        "Fragment" / Bytes(lambda this: this.FragmentSize),
        "GftFlowEntryId" / Int64ul,
        "GftOffloadInformation" / Int64ul
    )


@declare(guid=guid("2ed6006e-4729-4609-b423-3ee7bcd678ef"), event_id=1002, version=0)
class Microsoft_Windows_NDIS_PacketCapture_1002_0(Etw):
    pattern = Struct(
        "MiniportIfIndex" / Int32ul,
        "LowerIfIndex" / Int32ul,
        "MetadataSize" / Int32ul,
        "Metadata" / Bytes(lambda this: this.MetadataSize)
    )


@declare(guid=guid("2ed6006e-4729-4609-b423-3ee7bcd678ef"), event_id=1003, version=0)
class Microsoft_Windows_NDIS_PacketCapture_1003_0(Etw):
    pattern = Struct(
        "MiniportIfIndex" / Int32ul,
        "LowerIfIndex" / Int32ul,
        "SourcePortId" / Int32ul,
        "SourcePortName" / WString,
        "SourceNicName" / WString,
        "SourceNicType" / WString,
        "DestinationCount" / Int32ul,
        "Destination" / Double,
        "FragmentSize" / Int32ul,
        "Fragment" / Bytes(lambda this: this.FragmentSize),
        "OOBDataSize" / Int32ul,
        "OOBData" / Bytes(lambda this: this.OOBDataSize)
    )


@declare(guid=guid("2ed6006e-4729-4609-b423-3ee7bcd678ef"), event_id=1011, version=0)
class Microsoft_Windows_NDIS_PacketCapture_1011_0(Etw):
    pattern = Struct(
        "RulesCount" / Int32ul
    )


@declare(guid=guid("2ed6006e-4729-4609-b423-3ee7bcd678ef"), event_id=1012, version=0)
class Microsoft_Windows_NDIS_PacketCapture_1012_0(Etw):
    pattern = Struct(
        "FriendlyName" / WString,
        "UniqueName" / WString,
        "ServiceName" / WString,
        "Version" / WString
    )


@declare(guid=guid("2ed6006e-4729-4609-b423-3ee7bcd678ef"), event_id=1013, version=0)
class Microsoft_Windows_NDIS_PacketCapture_1013_0(Etw):
    pattern = Struct(
        "FriendlyName" / WString,
        "UniqueName" / WString,
        "ServiceName" / WString,
        "Version" / WString
    )


@declare(guid=guid("2ed6006e-4729-4609-b423-3ee7bcd678ef"), event_id=1014, version=0)
class Microsoft_Windows_NDIS_PacketCapture_1014_0(Etw):
    pattern = Struct(
        "MiniportIfIndex" / Int32ul,
        "LowerIfIndex" / Int32ul,
        "MediaType" / Int32ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("2ed6006e-4729-4609-b423-3ee7bcd678ef"), event_id=1015, version=0)
class Microsoft_Windows_NDIS_PacketCapture_1015_0(Etw):
    pattern = Struct(
        "MiniportIfIndex" / Int32ul,
        "LowerIfIndex" / Int32ul,
        "MediaType" / Int32ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("2ed6006e-4729-4609-b423-3ee7bcd678ef"), event_id=1016, version=0)
class Microsoft_Windows_NDIS_PacketCapture_1016_0(Etw):
    pattern = Struct(
        "RuleId" / Int8ul,
        "Directive" / Int8ul,
        "Length" / Int16ul,
        "Value" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("2ed6006e-4729-4609-b423-3ee7bcd678ef"), event_id=2001, version=0)
class Microsoft_Windows_NDIS_PacketCapture_2001_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("2ed6006e-4729-4609-b423-3ee7bcd678ef"), event_id=2002, version=0)
class Microsoft_Windows_NDIS_PacketCapture_2002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("2ed6006e-4729-4609-b423-3ee7bcd678ef"), event_id=2003, version=0)
class Microsoft_Windows_NDIS_PacketCapture_2003_0(Etw):
    pattern = Struct(
        "RuleId" / Int8ul,
        "Directive" / Int8ul,
        "Length" / Int16ul,
        "Value" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("2ed6006e-4729-4609-b423-3ee7bcd678ef"), event_id=3001, version=0)
class Microsoft_Windows_NDIS_PacketCapture_3001_0(Etw):
    pattern = Struct(
        "PreviousState" / Int8ul,
        "NextState" / Int8ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("2ed6006e-4729-4609-b423-3ee7bcd678ef"), event_id=3002, version=0)
class Microsoft_Windows_NDIS_PacketCapture_3002_0(Etw):
    pattern = Struct(
        "PreviousState" / Int8ul,
        "NextState" / Int8ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("2ed6006e-4729-4609-b423-3ee7bcd678ef"), event_id=5100, version=0)
class Microsoft_Windows_NDIS_PacketCapture_5100_0(Etw):
    pattern = Struct(
        "SourceId" / Int8ul,
        "RundownId" / Int32ul,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "ParamStr" / WString,
        "Description" / WString
    )


@declare(guid=guid("2ed6006e-4729-4609-b423-3ee7bcd678ef"), event_id=5101, version=0)
class Microsoft_Windows_NDIS_PacketCapture_5101_0(Etw):
    pattern = Struct(
        "SourceId" / Int8ul,
        "SourceName" / WString,
        "IfIndex" / Int32ul,
        "LayerCount" / Int16ul,
        "LayerInfo" / Int16sl
    )

