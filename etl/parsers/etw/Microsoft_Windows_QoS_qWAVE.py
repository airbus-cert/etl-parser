# -*- coding: utf-8 -*-
"""
Microsoft-Windows-QoS-qWAVE
GUID : 6ba132c4-da49-415b-a7f4-31870dc9fe25
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6ba132c4-da49-415b-a7f4-31870dc9fe25"), event_id=1, version=0)
class Microsoft_Windows_QoS_qWAVE_1_0(Etw):
    pattern = Struct(
        "FlowId" / Int32ul,
        "SetFlowType" / Int32ul,
        "BufferLen" / Int32ul,
        "Buffer" / Bytes(lambda this: this.BufferLen),
        "Flags" / Int32ul,
        "FailureActivity" / Int32ul,
        "FailureErrorCodeType" / Int32ul,
        "FailureErrorCode" / Int32ul
    )


@declare(guid=guid("6ba132c4-da49-415b-a7f4-31870dc9fe25"), event_id=2, version=0)
class Microsoft_Windows_QoS_qWAVE_2_0(Etw):
    pattern = Struct(
        "FlowId" / Int32ul,
        "SetFlowType" / Int32ul,
        "BufferLen" / Int32ul,
        "Buffer" / Bytes(lambda this: this.BufferLen),
        "Flags" / Int32ul,
        "LLTDSupported" / Int8ul
    )


@declare(guid=guid("6ba132c4-da49-415b-a7f4-31870dc9fe25"), event_id=3, version=0)
class Microsoft_Windows_QoS_qWAVE_3_0(Etw):
    pattern = Struct(
        "FlowId" / Int32ul,
        "QueryFlowType" / Int32ul,
        "BufferLen" / Int32ul,
        "Buffer" / Bytes(lambda this: this.BufferLen),
        "Flags" / Int32ul,
        "FailureActivity" / Int32ul,
        "FailureErrorCodeType" / Int32ul,
        "FailureErrorCode" / Int32ul
    )


@declare(guid=guid("6ba132c4-da49-415b-a7f4-31870dc9fe25"), event_id=4, version=0)
class Microsoft_Windows_QoS_qWAVE_4_0(Etw):
    pattern = Struct(
        "FlowId" / Int32ul,
        "NotifyFlowType" / Int32ul,
        "BufferLen" / Int32ul,
        "Buffer" / Bytes(lambda this: this.BufferLen),
        "Flags" / Int32ul,
        "FailureActivity" / Int32ul,
        "FailureErrorCodeType" / Int32ul,
        "FailureErrorCode" / Int32ul
    )


@declare(guid=guid("6ba132c4-da49-415b-a7f4-31870dc9fe25"), event_id=5, version=0)
class Microsoft_Windows_QoS_qWAVE_5_0(Etw):
    pattern = Struct(
        "AddressLen" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLen),
        "TrafficType" / Int32ul,
        "Flags" / Int32ul,
        "FailureActivity" / Int32ul,
        "FailureErrorCodeType" / Int32ul,
        "FailureErrorCode" / Int32ul
    )


@declare(guid=guid("6ba132c4-da49-415b-a7f4-31870dc9fe25"), event_id=6, version=0)
class Microsoft_Windows_QoS_qWAVE_6_0(Etw):
    pattern = Struct(
        "BufferLen" / Int32ul,
        "Buffer" / Bytes(lambda this: this.BufferLen),
        "FailureActivity" / Int32ul,
        "FailureErrorCodeType" / Int32ul,
        "FailureErrorCode" / Int32ul
    )


@declare(guid=guid("6ba132c4-da49-415b-a7f4-31870dc9fe25"), event_id=7, version=0)
class Microsoft_Windows_QoS_qWAVE_7_0(Etw):
    pattern = Struct(
        "AddressLen" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLen),
        "Flags" / Int32ul,
        "FailureActivity" / Int32ul,
        "FailureErrorCodeType" / Int32ul,
        "FailureErrorCode" / Int32ul
    )


@declare(guid=guid("6ba132c4-da49-415b-a7f4-31870dc9fe25"), event_id=8, version=0)
class Microsoft_Windows_QoS_qWAVE_8_0(Etw):
    pattern = Struct(
        "AddressLen" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLen),
        "Flags" / Int32ul,
        "FailureActivity" / Int32ul,
        "FailureErrorCodeType" / Int32ul,
        "FailureErrorCode" / Int32ul
    )


@declare(guid=guid("6ba132c4-da49-415b-a7f4-31870dc9fe25"), event_id=9, version=0)
class Microsoft_Windows_QoS_qWAVE_9_0(Etw):
    pattern = Struct(
        "SourceAddressLen" / Int32ul,
        "SourceAddress" / Bytes(lambda this: this.SourceAddressLen),
        "DestAddressLen" / Int32ul,
        "DestAddress" / Bytes(lambda this: this.DestAddressLen),
        "BottleneckBandwidth" / Double,
        "Is8021pSupported" / Int8ul
    )


@declare(guid=guid("6ba132c4-da49-415b-a7f4-31870dc9fe25"), event_id=10, version=0)
class Microsoft_Windows_QoS_qWAVE_10_0(Etw):
    pattern = Struct(
        "SourceAddressLen" / Int32ul,
        "SourceAddress" / Bytes(lambda this: this.SourceAddressLen),
        "DestAddressLen" / Int32ul,
        "DestAddress" / Bytes(lambda this: this.DestAddressLen),
        "BottleneckBandwidth" / Double,
        "AvailableBandwidth" / Double,
        "Is8021pSupported" / Int8ul
    )


@declare(guid=guid("6ba132c4-da49-415b-a7f4-31870dc9fe25"), event_id=11, version=0)
class Microsoft_Windows_QoS_qWAVE_11_0(Etw):
    pattern = Struct(
        "SourceAddressLen" / Int32ul,
        "SourceAddress" / Bytes(lambda this: this.SourceAddressLen),
        "DestAddressLen" / Int32ul,
        "DestAddress" / Bytes(lambda this: this.DestAddressLen),
        "BottleneckBandwidth" / Double,
        "AvailableBandwidth" / Double,
        "Is8021pSupported" / Int8ul
    )


@declare(guid=guid("6ba132c4-da49-415b-a7f4-31870dc9fe25"), event_id=12, version=0)
class Microsoft_Windows_QoS_qWAVE_12_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "ThreadID" / Int32ul,
        "QoSHandle" / Int64ul,
        "FailureActivity" / Int32ul,
        "FailureErrorCodeType" / Int32ul,
        "FailureErrorCode" / Int32ul
    )


@declare(guid=guid("6ba132c4-da49-415b-a7f4-31870dc9fe25"), event_id=13, version=0)
class Microsoft_Windows_QoS_qWAVE_13_0(Etw):
    pattern = Struct(
        "LocalCollectionError" / Int32ul,
        "RemoteCollectionError" / Int32ul,
        "CrossTrafficCollectionError" / Int32ul,
        "PathAnalysisResult" / Int32ul,
        "RemoteAnalysisResult" / Int32ul,
        "LocalAnalysisResult" / Int32ul
    )


@declare(guid=guid("6ba132c4-da49-415b-a7f4-31870dc9fe25"), event_id=14, version=0)
class Microsoft_Windows_QoS_qWAVE_14_0(Etw):
    pattern = Struct(
        "AddressLen" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLen),
        "Flags" / Int32ul,
        "FailureActivity" / Int32ul,
        "FailureErrorCodeType" / Int32ul,
        "FailureErrorCode" / Int32ul
    )


@declare(guid=guid("6ba132c4-da49-415b-a7f4-31870dc9fe25"), event_id=15, version=0)
class Microsoft_Windows_QoS_qWAVE_15_0(Etw):
    pattern = Struct(
        "AddressLength" / Int32ul,
        "SourceAddress" / Bytes(lambda this: this.AddressLength),
        "DestinationAddress" / Bytes(lambda this: this.AddressLength),
        "BottleneckBandwidth" / Double,
        "AvailableBandwidth" / Double
    )


@declare(guid=guid("6ba132c4-da49-415b-a7f4-31870dc9fe25"), event_id=16, version=0)
class Microsoft_Windows_QoS_qWAVE_16_0(Etw):
    pattern = Struct(
        "AddressLength" / Int32ul,
        "SourceAddress" / Bytes(lambda this: this.AddressLength),
        "DestinationAddress" / Bytes(lambda this: this.AddressLength),
        "Quiescent" / Int8ul
    )


@declare(guid=guid("6ba132c4-da49-415b-a7f4-31870dc9fe25"), event_id=17, version=0)
class Microsoft_Windows_QoS_qWAVE_17_0(Etw):
    pattern = Struct(
        "AddressLen" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLen),
        "TrafficType" / Int32ul,
        "Flags" / Int32ul,
        "Offlink" / Int8ul
    )


@declare(guid=guid("6ba132c4-da49-415b-a7f4-31870dc9fe25"), event_id=18, version=0)
class Microsoft_Windows_QoS_qWAVE_18_0(Etw):
    pattern = Struct(
        "AddressLength" / Int32ul,
        "NonLLTDEnabledMachine" / Bytes(lambda this: this.AddressLength)
    )


@declare(guid=guid("6ba132c4-da49-415b-a7f4-31870dc9fe25"), event_id=19, version=0)
class Microsoft_Windows_QoS_qWAVE_19_0(Etw):
    pattern = Struct(
        "AddressLength" / Int32ul,
        "LLTDEnabledMachine" / Bytes(lambda this: this.AddressLength)
    )


@declare(guid=guid("6ba132c4-da49-415b-a7f4-31870dc9fe25"), event_id=20, version=0)
class Microsoft_Windows_QoS_qWAVE_20_0(Etw):
    pattern = Struct(
        "CurrentTime" / Int32ul,
        "SystemTime" / Int32ul,
        "RequestedBandwidth" / Double,
        "NumBursts" / Int32ul,
        "BurstSize" / Int32ul
    )

