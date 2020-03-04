# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DAL-Provider
GUID : 7e87506f-bace-4bf1-bc09-3a1f37045c71
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7e87506f-bace-4bf1-bc09-3a1f37045c71"), event_id=1, version=0)
class Microsoft_Windows_DAL_Provider_1_0(Etw):
    pattern = Struct(
        "NetFn" / Int8ul,
        "CommandID" / Int8ul,
        "PacketSize" / Int32ul,
        "PacketData" / Bytes(lambda this: this.PacketSize),
        "SessionId" / Int32ul,
        "SequenceNumber" / Int32ul
    )


@declare(guid=guid("7e87506f-bace-4bf1-bc09-3a1f37045c71"), event_id=2, version=0)
class Microsoft_Windows_DAL_Provider_2_0(Etw):
    pattern = Struct(
        "NetFn" / Int8ul,
        "CommandID" / Int8ul,
        "PacketSize" / Int32ul,
        "PacketData" / Bytes(lambda this: this.PacketSize),
        "SessionId" / Int32ul,
        "SequenceNumber" / Int32ul
    )


@declare(guid=guid("7e87506f-bace-4bf1-bc09-3a1f37045c71"), event_id=11, version=0)
class Microsoft_Windows_DAL_Provider_11_0(Etw):
    pattern = Struct(
        "MI_Result" / Int32sl,
        "Operation" / WString
    )


@declare(guid=guid("7e87506f-bace-4bf1-bc09-3a1f37045c71"), event_id=15, version=0)
class Microsoft_Windows_DAL_Provider_15_0(Etw):
    pattern = Struct(
        "id" / Int8ul
    )


@declare(guid=guid("7e87506f-bace-4bf1-bc09-3a1f37045c71"), event_id=16, version=0)
class Microsoft_Windows_DAL_Provider_16_0(Etw):
    pattern = Struct(
        "id" / Int8ul
    )


@declare(guid=guid("7e87506f-bace-4bf1-bc09-3a1f37045c71"), event_id=17, version=0)
class Microsoft_Windows_DAL_Provider_17_0(Etw):
    pattern = Struct(
        "target" / WString,
        "protocol" / Int16ul,
        "port" / Int16ul,
        "authentication" / Int16ul,
        "usessl" / Int8ul,
        "skipcacheck" / Int8ul,
        "skipcncheck" / Int8ul,
        "skiprevocationcheck" / Int8ul,
        "timeoutsec" / Int32ul
    )


@declare(guid=guid("7e87506f-bace-4bf1-bc09-3a1f37045c71"), event_id=30, version=0)
class Microsoft_Windows_DAL_Provider_30_0(Etw):
    pattern = Struct(
        "NetFn" / Int8ul,
        "CommandID" / Int8ul,
        "PacketSize" / Int32ul,
        "PacketData" / Bytes(lambda this: this.PacketSize),
        "SessionId" / Int32ul,
        "SequenceNumber" / Int32ul
    )


@declare(guid=guid("7e87506f-bace-4bf1-bc09-3a1f37045c71"), event_id=31, version=0)
class Microsoft_Windows_DAL_Provider_31_0(Etw):
    pattern = Struct(
        "NetFn" / Int8ul,
        "CommandID" / Int8ul,
        "PacketSize" / Int32ul,
        "PacketData" / Bytes(lambda this: this.PacketSize),
        "SessionId" / Int32ul,
        "SequenceNumber" / Int32ul
    )

