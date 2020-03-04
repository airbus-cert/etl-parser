# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TunnelDriver
GUID : 4edbe902-9ed3-4cf0-93e8-b8b5fa920299
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1000, version=0)
class Microsoft_Windows_TunnelDriver_1000_0(Etw):
    pattern = Struct(
        "TunnelType" / Int32ul,
        "Index" / Int32ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1001, version=0)
class Microsoft_Windows_TunnelDriver_1001_0(Etw):
    pattern = Struct(
        "TunnelType" / Int32ul,
        "ErrorCode" / Int32ul,
        "TunnelReasonCode" / Int32ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1002, version=0)
class Microsoft_Windows_TunnelDriver_1002_0(Etw):
    pattern = Struct(
        "TunnelType" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1003, version=0)
class Microsoft_Windows_TunnelDriver_1003_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "Forwarding" / Int32ul,
        "WeakHostReceive" / Int32ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1006, version=0)
class Microsoft_Windows_TunnelDriver_1006_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1007, version=0)
class Microsoft_Windows_TunnelDriver_1007_0(Etw):
    pattern = Struct(
        "TunnelType" / Int32ul,
        "InterfaceIndex" / Int32ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1008, version=0)
class Microsoft_Windows_TunnelDriver_1008_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1010, version=0)
class Microsoft_Windows_TunnelDriver_1010_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1011, version=0)
class Microsoft_Windows_TunnelDriver_1011_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1012, version=0)
class Microsoft_Windows_TunnelDriver_1012_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1013, version=0)
class Microsoft_Windows_TunnelDriver_1013_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1014, version=0)
class Microsoft_Windows_TunnelDriver_1014_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "MediaStatus" / Int32ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1015, version=0)
class Microsoft_Windows_TunnelDriver_1015_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "ErrorCode" / Int32ul,
        "ReadError" / Int32ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1016, version=0)
class Microsoft_Windows_TunnelDriver_1016_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "TunnelType" / Int32ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1017, version=0)
class Microsoft_Windows_TunnelDriver_1017_0(Etw):
    pattern = Struct(
        "TunnelType" / Int32ul,
        "Index" / Int32ul,
        "InterfaceOperation" / Int32ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1018, version=0)
class Microsoft_Windows_TunnelDriver_1018_0(Etw):
    pattern = Struct(
        "TeredoFlowTuple" / Int32ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1020, version=0)
class Microsoft_Windows_TunnelDriver_1020_0(Etw):
    pattern = Struct(
        "IpAddrV6Length" / Int32ul,
        "LocalIpv6Address" / Bytes(lambda this: this.IpAddrV6Length),
        "RemoteIPv6Address" / Bytes(lambda this: this.IpAddrV6Length)
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1021, version=0)
class Microsoft_Windows_TunnelDriver_1021_0(Etw):
    pattern = Struct(
        "SourceIPv4Address" / Int32ul,
        "DestinationIPv4Address" / Int32ul,
        "SourcePort" / Int16ul,
        "DestinationPort" / Int16ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1022, version=0)
class Microsoft_Windows_TunnelDriver_1022_0(Etw):
    pattern = Struct(
        "NTStatus" / Int32ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1023, version=0)
class Microsoft_Windows_TunnelDriver_1023_0(Etw):
    pattern = Struct(
        "IpAddrV6Length" / Int32ul,
        "LocalIPv4Address" / Int32ul,
        "RemoteIPv4Address" / Int32ul,
        "LocalIPv6" / Bytes(lambda this: this.IpAddrV6Length),
        "RemoteIPv6" / Bytes(lambda this: this.IpAddrV6Length),
        "NTStatus" / Int32ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1024, version=0)
class Microsoft_Windows_TunnelDriver_1024_0(Etw):
    pattern = Struct(
        "TunnelType" / Int32ul,
        "TunnelInterfaceIndex" / Int32ul,
        "IPv4Address" / Int32ul,
        "YesorNo" / Int32ul,
        "InterfaceIndex" / Int32ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1025, version=0)
class Microsoft_Windows_TunnelDriver_1025_0(Etw):
    pattern = Struct(
        "TunnelType" / Int32ul,
        "OffloadedNblCount" / Int32ul,
        "ReturnedNblCount" / Int32ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1026, version=0)
class Microsoft_Windows_TunnelDriver_1026_0(Etw):
    pattern = Struct(
        "TunnelType" / Int32ul,
        "InterfaceIndex" / Int32ul,
        "DroppedNblCount" / Int32ul
    )


@declare(guid=guid("4edbe902-9ed3-4cf0-93e8-b8b5fa920299"), event_id=1027, version=0)
class Microsoft_Windows_TunnelDriver_1027_0(Etw):
    pattern = Struct(
        "ProcessID" / Int64ul,
        "FilterID" / Int64ul,
        "FlowHandle" / Int64ul
    )

