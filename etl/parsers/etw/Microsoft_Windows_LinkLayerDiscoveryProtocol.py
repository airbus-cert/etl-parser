# -*- coding: utf-8 -*-
"""
Microsoft-Windows-LinkLayerDiscoveryProtocol
GUID : dcbfb8f0-cd19-4f1c-a27d-23ac706ded72
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("dcbfb8f0-cd19-4f1c-a27d-23ac706ded72"), event_id=10010, version=0)
class Microsoft_Windows_LinkLayerDiscoveryProtocol_10010_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul
    )


@declare(guid=guid("dcbfb8f0-cd19-4f1c-a27d-23ac706ded72"), event_id=10011, version=0)
class Microsoft_Windows_LinkLayerDiscoveryProtocol_10011_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul
    )


@declare(guid=guid("dcbfb8f0-cd19-4f1c-a27d-23ac706ded72"), event_id=10020, version=0)
class Microsoft_Windows_LinkLayerDiscoveryProtocol_10020_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul
    )


@declare(guid=guid("dcbfb8f0-cd19-4f1c-a27d-23ac706ded72"), event_id=10021, version=0)
class Microsoft_Windows_LinkLayerDiscoveryProtocol_10021_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "RejectReason" / Int32ul
    )


@declare(guid=guid("dcbfb8f0-cd19-4f1c-a27d-23ac706ded72"), event_id=10030, version=0)
class Microsoft_Windows_LinkLayerDiscoveryProtocol_10030_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "AdminParameter" / Int32ul,
        "OldValue" / Int32ul,
        "NewValue" / Int32ul
    )


@declare(guid=guid("dcbfb8f0-cd19-4f1c-a27d-23ac706ded72"), event_id=10040, version=0)
class Microsoft_Windows_LinkLayerDiscoveryProtocol_10040_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "PacketPayloadLength" / Int32ul,
        "PacketPayload" / Bytes(lambda this: this.PacketPayloadLength)
    )


@declare(guid=guid("dcbfb8f0-cd19-4f1c-a27d-23ac706ded72"), event_id=10041, version=0)
class Microsoft_Windows_LinkLayerDiscoveryProtocol_10041_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "SequenceNumber" / Int32ul,
        "PacketPayloadLength" / Int32ul,
        "PacketPayload" / Bytes(lambda this: this.PacketPayloadLength)
    )


@declare(guid=guid("dcbfb8f0-cd19-4f1c-a27d-23ac706ded72"), event_id=10042, version=0)
class Microsoft_Windows_LinkLayerDiscoveryProtocol_10042_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "SequenceNumber" / Int32ul,
        "PacketDiscardReason" / Int32ul
    )


@declare(guid=guid("dcbfb8f0-cd19-4f1c-a27d-23ac706ded72"), event_id=10043, version=0)
class Microsoft_Windows_LinkLayerDiscoveryProtocol_10043_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "SequenceNumber" / Int32ul
    )


@declare(guid=guid("dcbfb8f0-cd19-4f1c-a27d-23ac706ded72"), event_id=10050, version=0)
class Microsoft_Windows_LinkLayerDiscoveryProtocol_10050_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "MsapIdLength" / Int32ul,
        "MsapId" / Bytes(lambda this: this.MsapIdLength)
    )


@declare(guid=guid("dcbfb8f0-cd19-4f1c-a27d-23ac706ded72"), event_id=10051, version=0)
class Microsoft_Windows_LinkLayerDiscoveryProtocol_10051_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "MsapIdLength" / Int32ul,
        "MsapId" / Bytes(lambda this: this.MsapIdLength)
    )


@declare(guid=guid("dcbfb8f0-cd19-4f1c-a27d-23ac706ded72"), event_id=10052, version=0)
class Microsoft_Windows_LinkLayerDiscoveryProtocol_10052_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "MsapIdLength" / Int32ul,
        "MsapId" / Bytes(lambda this: this.MsapIdLength)
    )


@declare(guid=guid("dcbfb8f0-cd19-4f1c-a27d-23ac706ded72"), event_id=10053, version=0)
class Microsoft_Windows_LinkLayerDiscoveryProtocol_10053_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "MsapIdLength" / Int32ul,
        "MsapId" / Bytes(lambda this: this.MsapIdLength)
    )


@declare(guid=guid("dcbfb8f0-cd19-4f1c-a27d-23ac706ded72"), event_id=10060, version=0)
class Microsoft_Windows_LinkLayerDiscoveryProtocol_10060_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul
    )


@declare(guid=guid("dcbfb8f0-cd19-4f1c-a27d-23ac706ded72"), event_id=10061, version=0)
class Microsoft_Windows_LinkLayerDiscoveryProtocol_10061_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul
    )


@declare(guid=guid("dcbfb8f0-cd19-4f1c-a27d-23ac706ded72"), event_id=10062, version=0)
class Microsoft_Windows_LinkLayerDiscoveryProtocol_10062_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "ExistingMsapIdLength" / Int32ul,
        "ExistingMsapId" / Bytes(lambda this: this.ExistingMsapIdLength),
        "ReceivedMsapIdLength" / Int32ul,
        "ReceivedMsapId" / Bytes(lambda this: this.ReceivedMsapIdLength)
    )

