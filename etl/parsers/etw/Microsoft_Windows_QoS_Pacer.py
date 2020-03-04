# -*- coding: utf-8 -*-
"""
Microsoft-Windows-QoS-Pacer
GUID : 914ed502-b70d-4add-b758-95692854f8a3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("914ed502-b70d-4add-b758-95692854f8a3"), event_id=1, version=0)
class Microsoft_Windows_QoS_Pacer_1_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "FlowType" / Int32ul,
        "SendSpecTokenRate" / Int32ul,
        "SendSpecTokenBucketSize" / Int32ul,
        "SendSpecPeakBandwidth" / Int32ul,
        "SendSpecLatency" / Int32ul,
        "SendSpecDelayVariation" / Int32ul,
        "SendSpecServiceType" / Int32ul,
        "SendSpecMaxSduSize" / Int32ul,
        "SendSpecMinimumPolicedSize" / Int32ul,
        "QoSObjectBufferLen" / Int32ul,
        "QoSObjectBuffer" / Bytes(lambda this: this.QoSObjectBufferLen)
    )


@declare(guid=guid("914ed502-b70d-4add-b758-95692854f8a3"), event_id=1, version=1)
class Microsoft_Windows_QoS_Pacer_1_1(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "FlowType" / Int32ul,
        "SendSpecTokenRate" / Int32ul,
        "SendSpecTokenBucketSize" / Int32ul,
        "SendSpecPeakBandwidth" / Int32ul,
        "SendSpecLatency" / Int32ul,
        "SendSpecDelayVariation" / Int32ul,
        "SendSpecServiceType" / Int32ul,
        "SendSpecMaxSduSize" / Int32ul,
        "SendSpecMinimumPolicedSize" / Int32ul,
        "DsClass" / Int16sl,
        "TrafficClass" / Int16sl,
        "QoSObjectBufferLen" / Int32ul,
        "QoSObjectBuffer" / Bytes(lambda this: this.QoSObjectBufferLen),
        "DefaultSystemFlow" / Int8ul
    )


@declare(guid=guid("914ed502-b70d-4add-b758-95692854f8a3"), event_id=2, version=0)
class Microsoft_Windows_QoS_Pacer_2_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "FlowType" / Int32ul,
        "OldSendSpecTokenRate" / Int32ul,
        "OldSendSpecTokenBucketSize" / Int32ul,
        "OldSendSpecPeakBandwidth" / Int32ul,
        "OldSendSpecLatency" / Int32ul,
        "OldSendSpecDelayVariation" / Int32ul,
        "OldSendSpecServiceType" / Int32ul,
        "OldSendSpecMaxSduSize" / Int32ul,
        "OldSendSpecMinimumPolicedSize" / Int32ul,
        "NewSendSpecTokenRate" / Int32ul,
        "NewSendSpecTokenBucketSize" / Int32ul,
        "NewSendSpecPeakBandwidth" / Int32ul,
        "NewSendSpecLatency" / Int32ul,
        "NewSendSpecDelayVariation" / Int32ul,
        "NewSendSpecServiceType" / Int32ul,
        "NewSendSpecMaxSduSize" / Int32ul,
        "NewSendSpecMinimumPolicedSize" / Int32ul,
        "NewQoSObjectBufferLen" / Int32ul,
        "NewQoSObjectBuffer" / Bytes(lambda this: this.NewQoSObjectBufferLen)
    )


@declare(guid=guid("914ed502-b70d-4add-b758-95692854f8a3"), event_id=2, version=1)
class Microsoft_Windows_QoS_Pacer_2_1(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "FlowType" / Int32ul,
        "SendSpecTokenRate" / Int32ul,
        "SendSpecTokenBucketSize" / Int32ul,
        "SendSpecPeakBandwidth" / Int32ul,
        "SendSpecLatency" / Int32ul,
        "SendSpecDelayVariation" / Int32ul,
        "SendSpecServiceType" / Int32ul,
        "SendSpecMaxSduSize" / Int32ul,
        "SendSpecMinimumPolicedSize" / Int32ul,
        "DsClass" / Int16sl,
        "TrafficClass" / Int16sl,
        "NewQoSObjectBufferLen" / Int32ul,
        "NewQoSObjectBuffer" / Bytes(lambda this: this.NewQoSObjectBufferLen),
        "AffectedPackets" / Int32ul
    )


@declare(guid=guid("914ed502-b70d-4add-b758-95692854f8a3"), event_id=3, version=0)
class Microsoft_Windows_QoS_Pacer_3_0(Etw):
    pattern = Struct(
        "NdisMediumType" / Int32ul,
        "FriendlyName" / WString,
        "DeviceName" / WString
    )


@declare(guid=guid("914ed502-b70d-4add-b758-95692854f8a3"), event_id=3, version=1)
class Microsoft_Windows_QoS_Pacer_3_1(Etw):
    pattern = Struct(
        "NetLuid" / Int64ul,
        "NdisMediumType" / Int32ul,
        "FriendlyNameLen" / Int32ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLen),
        "DeviceNameLen" / Int32ul,
        "DeviceName" / Bytes(lambda this: this.DeviceNameLen),
        "Context" / Int32ul
    )


@declare(guid=guid("914ed502-b70d-4add-b758-95692854f8a3"), event_id=4, version=0)
class Microsoft_Windows_QoS_Pacer_4_0(Etw):
    pattern = Struct(
        "NdisMediumType" / Int32ul,
        "FriendlyName" / WString,
        "DeviceName" / WString
    )


@declare(guid=guid("914ed502-b70d-4add-b758-95692854f8a3"), event_id=4, version=1)
class Microsoft_Windows_QoS_Pacer_4_1(Etw):
    pattern = Struct(
        "NetLuid" / Int64ul,
        "NdisMediumType" / Int32ul,
        "FriendlyNameLen" / Int32ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLen),
        "DeviceNameLen" / Int32ul,
        "DeviceName" / Bytes(lambda this: this.DeviceNameLen),
        "Context" / Int32ul
    )


@declare(guid=guid("914ed502-b70d-4add-b758-95692854f8a3"), event_id=5, version=0)
class Microsoft_Windows_QoS_Pacer_5_0(Etw):
    pattern = Struct(
        "FlowType" / Int32ul,
        "OldSendSpecTokenRate" / Int32ul,
        "OldSendSpecTokenBucketSize" / Int32ul,
        "OldSendSpecPeakBandwidth" / Int32ul,
        "OldSendSpecLatency" / Int32ul,
        "OldSendSpecDelayVariation" / Int32ul,
        "OldSendSpecServiceType" / Int32ul,
        "OldSendSpecMaxSduSize" / Int32ul,
        "OldSendSpecMinimumPolicedSize" / Int32ul,
        "NewSendSpecTokenRate" / Int32ul,
        "NewSendSpecTokenBucketSize" / Int32ul,
        "NewSendSpecPeakBandwidth" / Int32ul,
        "NewSendSpecLatency" / Int32ul,
        "NewSendSpecDelayVariation" / Int32ul,
        "NewSendSpecServiceType" / Int32ul,
        "NewSendSpecMaxSduSize" / Int32ul,
        "NewSendSpecMinimumPolicedSize" / Int32ul,
        "NewQoSObjectBufferLen" / Int32ul,
        "NewQoSObjectBuffer" / Bytes(lambda this: this.NewQoSObjectBufferLen),
        "AffectedPackets" / Int32ul
    )


@declare(guid=guid("914ed502-b70d-4add-b758-95692854f8a3"), event_id=6, version=0)
class Microsoft_Windows_QoS_Pacer_6_0(Etw):
    pattern = Struct(
        "DroppedPackets" / Int32ul,
        "PacketsScheduled" / Int32ul,
        "PacketsTransmitted" / Int32ul,
        "BytesScheduled" / Int64ul,
        "BytesTransmitted" / Int64ul,
        "NblSent" / Int32ul,
        "NblComplete" / Int32ul
    )


@declare(guid=guid("914ed502-b70d-4add-b758-95692854f8a3"), event_id=7, version=0)
class Microsoft_Windows_QoS_Pacer_7_0(Etw):
    pattern = Struct(
        "DropReason" / Int32ul
    )


@declare(guid=guid("914ed502-b70d-4add-b758-95692854f8a3"), event_id=8, version=0)
class Microsoft_Windows_QoS_Pacer_8_0(Etw):
    pattern = Struct(
        "DsClass" / Int16sl,
        "TrafficClass" / Int16sl,
        "Wmm" / Int16sl
    )


@declare(guid=guid("914ed502-b70d-4add-b758-95692854f8a3"), event_id=9, version=0)
class Microsoft_Windows_QoS_Pacer_9_0(Etw):
    pattern = Struct(
        "Allow" / Int32ul
    )


@declare(guid=guid("914ed502-b70d-4add-b758-95692854f8a3"), event_id=11, version=0)
class Microsoft_Windows_QoS_Pacer_11_0(Etw):
    pattern = Struct(
        "CurrentTime" / Int64ul,
        "BytesSent" / Int32ul,
        "BytesDropped" / Int32ul,
        "NewSendWindow" / Int32ul,
        "MinSendWindow" / Int32ul,
        "Weight" / Int32ul,
        "SBytesRequested" / Int64sl,
        "DropRate" / Int32ul,
        "IdleIntervals" / Int64ul,
        "RcSendWindow" / Int32ul,
        "RcEpisodeLength" / Int32ul,
        "RcStatMuxFactor" / Int32ul,
        "RcExitThreshold" / Int32ul,
        "AverageMaxBytesRequested" / Int32ul
    )


@declare(guid=guid("914ed502-b70d-4add-b758-95692854f8a3"), event_id=12, version=0)
class Microsoft_Windows_QoS_Pacer_12_0(Etw):
    pattern = Struct(
        "CurrentTime" / Int64ul,
        "ActiveFlows" / Int32ul,
        "ActiveWeight" / Int32ul,
        "NewSendWindow" / Int32ul
    )


@declare(guid=guid("914ed502-b70d-4add-b758-95692854f8a3"), event_id=13, version=0)
class Microsoft_Windows_QoS_Pacer_13_0(Etw):
    pattern = Struct(
        "FlowConformanceEvent" / Int32ul,
        "CurrentTime" / Int64ul,
        "LastConformanceTime" / Int64ul,
        "PeakConformanceTime" / Int64ul,
        "Tokens" / Int64ul,
        "MaxTokens" / Int64ul,
        "Rate" / Int64ul,
        "LastConformanceCredits" / Int32ul
    )


@declare(guid=guid("914ed502-b70d-4add-b758-95692854f8a3"), event_id=14, version=0)
class Microsoft_Windows_QoS_Pacer_14_0(Etw):
    pattern = Struct(
        "FlowSendQueueEvent" / Int32ul,
        "CurrentTime" / Int64ul,
        "IdleTime" / Int64ul,
        "DelayTime" / Int64ul,
        "BytesRequested" / Int32ul,
        "BytesSent" / Int32ul,
        "BytesQueued" / Int32ul
    )


@declare(guid=guid("914ed502-b70d-4add-b758-95692854f8a3"), event_id=15, version=0)
class Microsoft_Windows_QoS_Pacer_15_0(Etw):
    pattern = Struct(
        "TimerEvent" / Int32ul,
        "TimerId" / Int32ul,
        "CurrentTime" / Int64ul,
        "SetTime" / Int64ul,
        "RunTime" / Int64ul,
        "FlowsProcessed" / Int32ul,
        "NblsSent" / Int32ul,
        "NblsDropped" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("914ed502-b70d-4add-b758-95692854f8a3"), event_id=16, version=0)
class Microsoft_Windows_QoS_Pacer_16_0(Etw):
    pattern = Struct(
        "CurrentTime" / Int64ul,
        "BytesRequested" / Int32ul,
        "BytesCompleted" / Int32ul,
        "BytesInQueue" / Int32ul,
        "BufferAvailable" / Int64sl,
        "BetaTerm" / Int64sl,
        "AlphaTerm" / Int64sl,
        "DeltaSendWindow" / Int64sl,
        "NewSendWindow" / Int64sl
    )

