# -*- coding: utf-8 -*-
"""
Microsoft-Windows-PktMon
GUID : 4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac"), event_id=10, version=0)
class Microsoft_Windows_PktMon_10_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac"), event_id=20, version=0)
class Microsoft_Windows_PktMon_20_0(Etw):
    pattern = Struct(
        "Id" / Int16ul,
        "Type" / Int16ul,
        "Name" / WString,
        "Description" / WString
    )


@declare(guid=guid("4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac"), event_id=30, version=0)
class Microsoft_Windows_PktMon_30_0(Etw):
    pattern = Struct(
        "ComponentId" / Int16ul,
        "Type" / Int16ul,
        "Value" / Int32ul
    )


@declare(guid=guid("4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac"), event_id=40, version=0)
class Microsoft_Windows_PktMon_40_0(Etw):
    pattern = Struct(
        "ComponentId" / Int16ul,
        "Type" / Int16ul,
        "Value" / Guid
    )


@declare(guid=guid("4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac"), event_id=50, version=0)
class Microsoft_Windows_PktMon_50_0(Etw):
    pattern = Struct(
        "ComponentId" / Int16ul,
        "Type" / Int16ul,
        "Value" / Int32ul
    )


@declare(guid=guid("4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac"), event_id=60, version=0)
class Microsoft_Windows_PktMon_60_0(Etw):
    pattern = Struct(
        "ComponentId" / Int16ul,
        "Type" / Int16ul,
        "Value" / Int16ul
    )


@declare(guid=guid("4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac"), event_id=70, version=0)
class Microsoft_Windows_PktMon_70_0(Etw):
    pattern = Struct(
        "ComponentId" / Int16ul,
        "Type" / Int16ul,
        "Size" / Int32ul,
        "Value" / Bytes(lambda this: this.Size)
    )


@declare(guid=guid("4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac"), event_id=73, version=0)
class Microsoft_Windows_PktMon_73_0(Etw):
    pattern = Struct(
        "ComponentId" / Int16ul,
        "Type" / Int16ul,
        "Value" / WString
    )


@declare(guid=guid("4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac"), event_id=75, version=0)
class Microsoft_Windows_PktMon_75_0(Etw):
    pattern = Struct(
        "ComponentId" / Int16ul,
        "Type" / Int16ul,
        "EtherType" / Int16ul
    )


@declare(guid=guid("4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac"), event_id=80, version=0)
class Microsoft_Windows_PktMon_80_0(Etw):
    pattern = Struct(
        "ComponentId" / Int16ul,
        "DirTagIn" / Int16ul,
        "PacketsIn" / Int64ul,
        "BytesIn" / Int64ul,
        "DirTagOut" / Int16ul,
        "PacketsOut" / Int64ul,
        "BytesOut" / Int64ul
    )


@declare(guid=guid("4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac"), event_id=90, version=0)
class Microsoft_Windows_PktMon_90_0(Etw):
    pattern = Struct(
        "ComponentId" / Int16ul,
        "EdgeName" / WString,
        "EdgeId" / Int16ul,
        "DirTagIn" / Int16ul,
        "PacketsIn" / Int64ul,
        "BytesIn" / Int64ul,
        "DirTagOut" / Int16ul,
        "PacketsOut" / Int64ul,
        "BytesOut" / Int64ul
    )


@declare(guid=guid("4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac"), event_id=100, version=0)
class Microsoft_Windows_PktMon_100_0(Etw):
    pattern = Struct(
        "FilterId" / Int16ul,
        "FilterName" / WString,
        "EtherType" / Int16ul,
        "VlanId" / Int16ul,
        "IpAddress1" / Int32ul,
        "IpAddress2" / Int32ul,
        "Protocol" / Int8ul,
        "Port1" / Int16ul,
        "Port2" / Int16ul,
        "TCPFlags" / Int8ul
    )


@declare(guid=guid("4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac"), event_id=110, version=0)
class Microsoft_Windows_PktMon_110_0(Etw):
    pattern = Struct(
        "FilterId" / Int16ul,
        "FilterName" / WString,
        "EtherType" / Int16ul,
        "VlanId" / Int16ul,
        "Protocol" / Int8ul,
        "Port1" / Int16ul,
        "Port2" / Int16ul,
        "TCPFlags" / Int8ul
    )


@declare(guid=guid("4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac"), event_id=120, version=0)
class Microsoft_Windows_PktMon_120_0(Etw):
    pattern = Struct(
        "EtherType" / Int16ul,
        "VlanId" / Int16ul,
        "DestinationIP" / Int32ul,
        "SourceIP" / Int32ul,
        "Protocol" / Int8ul,
        "DestinationPort" / Int16ul,
        "SourcePort" / Int16ul,
        "TCPFlags" / Int8ul,
        "PktGroupId" / Int64ul,
        "PktCount" / Int16ul,
        "AppearanceCount" / Int16ul,
        "DirTag" / Int16ul,
        "PacketType" / Int16ul,
        "ComponentId" / Int16ul,
        "EdgeId" / Int16ul,
        "FilterId" / Int16ul,
        "DropReason" / Int32ul,
        "DropLocation" / Int32ul
    )


@declare(guid=guid("4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac"), event_id=130, version=0)
class Microsoft_Windows_PktMon_130_0(Etw):
    pattern = Struct(
        "EtherType" / Int16ul,
        "VlanId" / Int16ul,
        "Protocol" / Int8ul,
        "DestinationPort" / Int16ul,
        "SourcePort" / Int16ul,
        "TCPFlags" / Int8ul,
        "PktGroupId" / Int64ul,
        "PktCount" / Int16ul,
        "AppearanceCount" / Int16ul,
        "DirTag" / Int16ul,
        "PacketType" / Int16ul,
        "ComponentId" / Int16ul,
        "EdgeId" / Int16ul,
        "FilterId" / Int16ul,
        "DropReason" / Int32ul,
        "DropLocation" / Int32ul
    )


@declare(guid=guid("4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac"), event_id=140, version=0)
class Microsoft_Windows_PktMon_140_0(Etw):
    pattern = Struct(
        "EtherType" / Int16ul,
        "VlanId" / Int16ul,
        "DestinationIP" / Int32ul,
        "SourceIP" / Int32ul,
        "Protocol" / Int8ul,
        "DestinationPort" / Int16ul,
        "SourcePort" / Int16ul,
        "TCPFlags" / Int8ul,
        "PktGroupId" / Int64ul,
        "PktCount" / Int16ul,
        "AppearanceCount" / Int16ul,
        "DirTag" / Int16ul,
        "PacketType" / Int16ul,
        "ComponentId" / Int16ul,
        "EdgeId" / Int16ul,
        "FilterId" / Int16ul,
        "DropReason" / Int32ul,
        "DropLocation" / Int32ul
    )


@declare(guid=guid("4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac"), event_id=150, version=0)
class Microsoft_Windows_PktMon_150_0(Etw):
    pattern = Struct(
        "EtherType" / Int16ul,
        "VlanId" / Int16ul,
        "Protocol" / Int8ul,
        "DestinationPort" / Int16ul,
        "SourcePort" / Int16ul,
        "TCPFlags" / Int8ul,
        "PktGroupId" / Int64ul,
        "PktCount" / Int16ul,
        "AppearanceCount" / Int16ul,
        "DirTag" / Int16ul,
        "PacketType" / Int16ul,
        "ComponentId" / Int16ul,
        "EdgeId" / Int16ul,
        "FilterId" / Int16ul,
        "DropReason" / Int32ul,
        "DropLocation" / Int32ul
    )


@declare(guid=guid("4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac"), event_id=160, version=0)
class Microsoft_Windows_PktMon_160_0(Etw):
    pattern = Struct(
        "PktGroupId" / Int64ul,
        "PktNumber" / Int16ul,
        "AppearanceCount" / Int16ul,
        "DirTag" / Int16ul,
        "PacketType" / Int16ul,
        "ComponentId" / Int16ul,
        "EdgeId" / Int16ul,
        "FilterId" / Int16ul,
        "DropReason" / Int32ul,
        "DropLocation" / Int32ul,
        "OriginalPayloadSize" / Int16ul,
        "LoggedPayloadSize" / Int16ul,
        "Payload" / Bytes(lambda this: this.LoggedPayloadSize)
    )


@declare(guid=guid("4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac"), event_id=170, version=0)
class Microsoft_Windows_PktMon_170_0(Etw):
    pattern = Struct(
        "PktGroupId" / Int64ul,
        "PktNumber" / Int16ul,
        "AppearanceCount" / Int16ul,
        "DirTag" / Int16ul,
        "PacketType" / Int16ul,
        "ComponentId" / Int16ul,
        "EdgeId" / Int16ul,
        "FilterId" / Int16ul,
        "DropReason" / Int32ul,
        "DropLocation" / Int32ul,
        "OriginalPayloadSize" / Int16ul,
        "LoggedPayloadSize" / Int16ul,
        "Payload" / Bytes(lambda this: this.LoggedPayloadSize)
    )


@declare(guid=guid("4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac"), event_id=180, version=0)
class Microsoft_Windows_PktMon_180_0(Etw):
    pattern = Struct(
        "PktGroupId" / Int64ul,
        "PktNumber" / Int16ul,
        "AppearanceCount" / Int16ul,
        "DirTag" / Int16ul,
        "PacketType" / Int16ul,
        "ComponentId" / Int16ul,
        "EdgeId" / Int16ul,
        "FilterId" / Int16ul,
        "DropReason" / Int32ul,
        "DropLocation" / Int32ul,
        "TcpIpChecksum" / Int64ul,
        "TcpLargeSend" / Int64ul,
        "Ieee8021Q" / Int64ul,
        "HashInfo" / Int64ul,
        "HashValue" / Int64ul,
        "VirtualSubnetInfo" / Int64ul,
        "TcpRecvSegCoalesceInfo" / Int64ul,
        "NrtNameResolutionId" / Int64ul,
        "TcpSendOffloadsSupplementalInfo" / Int64ul,
        "SwitchForwardingDetail" / Int64ul,
        "GftOffloadInfo" / Int64ul,
        "GftFlowEntryId" / Int64ul
    )


@declare(guid=guid("4d4f80d9-c8bd-4d73-bb5b-19c90402c5ac"), event_id=190, version=0)
class Microsoft_Windows_PktMon_190_0(Etw):
    pattern = Struct(
        "PktGroupId" / Int64ul,
        "PktNumber" / Int16ul,
        "AppearanceCount" / Int16ul,
        "DirTag" / Int16ul,
        "PacketType" / Int16ul,
        "ComponentId" / Int16ul,
        "EdgeId" / Int16ul,
        "FilterId" / Int16ul,
        "DropReason" / Int32ul,
        "DropLocation" / Int32ul,
        "TcpIpChecksum" / Int64ul,
        "TcpLargeSend" / Int64ul,
        "Ieee8021Q" / Int64ul,
        "HashInfo" / Int64ul,
        "HashValue" / Int64ul,
        "VirtualSubnetInfo" / Int64ul,
        "TcpRecvSegCoalesceInfo" / Int64ul,
        "NrtNameResolutionId" / Int64ul,
        "TcpSendOffloadsSupplementalInfo" / Int64ul,
        "SwitchForwardingDetail" / Int64ul,
        "GftOffloadInfo" / Int64ul,
        "GftFlowEntryId" / Int64ul
    )

