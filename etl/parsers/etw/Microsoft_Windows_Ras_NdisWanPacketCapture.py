# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Ras-NdisWanPacketCapture
GUID : d84521f7-2235-4237-a7c0-14e3a9676286
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d84521f7-2235-4237-a7c0-14e3a9676286"), event_id=5001, version=0)
class Microsoft_Windows_Ras_NdisWanPacketCapture_5001_0(Etw):
    pattern = Struct(
        "RoutingDomainID" / WString,
        "RRASUserName" / WString,
        "FragmentSize" / Int32ul,
        "Fragment" / Bytes(lambda this: this.FragmentSize)
    )


@declare(guid=guid("d84521f7-2235-4237-a7c0-14e3a9676286"), event_id=5002, version=0)
class Microsoft_Windows_Ras_NdisWanPacketCapture_5002_0(Etw):
    pattern = Struct(
        "RoutingDomainID" / WString,
        "RRASUserName" / WString,
        "FragmentSize" / Int32ul,
        "Fragment" / Bytes(lambda this: this.FragmentSize)
    )


@declare(guid=guid("d84521f7-2235-4237-a7c0-14e3a9676286"), event_id=5003, version=0)
class Microsoft_Windows_Ras_NdisWanPacketCapture_5003_0(Etw):
    pattern = Struct(
        "param1" / WString
    )

