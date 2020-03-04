# -*- coding: utf-8 -*-
"""
Microsoft-Windows-NetworkSecurity
GUID : 7b702970-90bc-4584-8b20-c0799086ee5a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7b702970-90bc-4584-8b20-c0799086ee5a"), event_id=801, version=0)
class Microsoft_Windows_NetworkSecurity_801_0(Etw):
    pattern = Struct(
        "SaContextID" / Int64ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("7b702970-90bc-4584-8b20-c0799086ee5a"), event_id=802, version=0)
class Microsoft_Windows_NetworkSecurity_802_0(Etw):
    pattern = Struct(
        "SaContextID" / Int64ul,
        "Result" / Int32ul
    )


@declare(guid=guid("7b702970-90bc-4584-8b20-c0799086ee5a"), event_id=803, version=0)
class Microsoft_Windows_NetworkSecurity_803_0(Etw):
    pattern = Struct(
        "SaContextID" / Int64ul,
        "LocalAddr" / WString,
        "LocalMask" / WString,
        "LocalPort" / Int16ul,
        "RemoteAddress" / WString,
        "RemoteMask" / WString,
        "RemotePort" / Int16ul,
        "IPProtocol" / Int8ul,
        "LocalTunnelEndpt" / WString,
        "RemoteTunnelEndpt" / WString
    )


@declare(guid=guid("7b702970-90bc-4584-8b20-c0799086ee5a"), event_id=804, version=0)
class Microsoft_Windows_NetworkSecurity_804_0(Etw):
    pattern = Struct(
        "SaContextID" / Int64ul
    )


@declare(guid=guid("7b702970-90bc-4584-8b20-c0799086ee5a"), event_id=805, version=0)
class Microsoft_Windows_NetworkSecurity_805_0(Etw):
    pattern = Struct(
        "SaContextID" / Int64ul,
        "SPI" / Int32ul
    )


@declare(guid=guid("7b702970-90bc-4584-8b20-c0799086ee5a"), event_id=808, version=0)
class Microsoft_Windows_NetworkSecurity_808_0(Etw):
    pattern = Struct(
        "SaContextID" / Int64ul
    )

