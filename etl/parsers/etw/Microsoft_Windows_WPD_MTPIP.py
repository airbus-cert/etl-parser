# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WPD-MTPIP
GUID : c374d21e-69b2-4cd7-9a25-62187c5a5619
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c374d21e-69b2-4cd7-9a25-62187c5a5619"), event_id=100, version=0)
class Microsoft_Windows_WPD_MTPIP_100_0(Etw):
    pattern = Struct(
        "MTPIPPacketLength" / Int32ul,
        "MTPIPPacketData" / Bytes(lambda this: this.MTPIPPacketLength)
    )


@declare(guid=guid("c374d21e-69b2-4cd7-9a25-62187c5a5619"), event_id=101, version=0)
class Microsoft_Windows_WPD_MTPIP_101_0(Etw):
    pattern = Struct(
        "MTPIPPacketLength" / Int32ul,
        "MTPIPPacketData" / Bytes(lambda this: this.MTPIPPacketLength)
    )


@declare(guid=guid("c374d21e-69b2-4cd7-9a25-62187c5a5619"), event_id=102, version=0)
class Microsoft_Windows_WPD_MTPIP_102_0(Etw):
    pattern = Struct(
        "MTPIPPacketLength" / Int32ul,
        "MTPIPPacketData" / Bytes(lambda this: this.MTPIPPacketLength)
    )


@declare(guid=guid("c374d21e-69b2-4cd7-9a25-62187c5a5619"), event_id=103, version=0)
class Microsoft_Windows_WPD_MTPIP_103_0(Etw):
    pattern = Struct(
        "MTPIPPacketLength" / Int32ul,
        "MTPIPPacketData" / Bytes(lambda this: this.MTPIPPacketLength)
    )


@declare(guid=guid("c374d21e-69b2-4cd7-9a25-62187c5a5619"), event_id=104, version=0)
class Microsoft_Windows_WPD_MTPIP_104_0(Etw):
    pattern = Struct(
        "MTPIPPacketLength" / Int32ul,
        "MTPIPPacketType" / Int32ul
    )


@declare(guid=guid("c374d21e-69b2-4cd7-9a25-62187c5a5619"), event_id=105, version=0)
class Microsoft_Windows_WPD_MTPIP_105_0(Etw):
    pattern = Struct(
        "MTPIPEventLength" / Int32ul,
        "MTPIPEventData" / Bytes(lambda this: this.MTPIPEventLength)
    )


@declare(guid=guid("c374d21e-69b2-4cd7-9a25-62187c5a5619"), event_id=106, version=0)
class Microsoft_Windows_WPD_MTPIP_106_0(Etw):
    pattern = Struct(
        "MTPIPPacketLength" / Int32ul,
        "MTPIPPacketType" / Int32ul
    )


@declare(guid=guid("c374d21e-69b2-4cd7-9a25-62187c5a5619"), event_id=107, version=0)
class Microsoft_Windows_WPD_MTPIP_107_0(Etw):
    pattern = Struct(
        "MTPIPPacketLength" / Int32ul,
        "MTPIPPacketType" / Int32ul
    )

