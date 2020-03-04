# -*- coding: utf-8 -*-
"""
Microsoft-Windows-NdisImPlatformEventProvider
GUID : 11c5d8ad-756a-42c2-8087-eb1b4a72a846
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=1, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_1_0(Etw):
    pattern = Struct(
        "NetPnpEvent" / Int32ul,
        "Member" / WString
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=2, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_2_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "PowerState" / Int32ul
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=3, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_3_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "StatusBufferLength" / Int32ul,
        "StatusBuffer" / Bytes(lambda this: this.StatusBufferLength)
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=4, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_4_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "StatusBufferLength" / Int32ul,
        "StatusBuffer" / Bytes(lambda this: this.StatusBufferLength)
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=5, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_5_0(Etw):
    pattern = Struct(
        "Oid" / Int32ul,
        "Adapter" / WString,
        "OidBufferLen" / Int32ul,
        "OidBuffer" / Bytes(lambda this: this.OidBufferLen),
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=6, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_6_0(Etw):
    pattern = Struct(
        "Oid" / Int32ul,
        "TeamNic" / WString,
        "Member" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=7, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_7_0(Etw):
    pattern = Struct(
        "Oid" / Int32ul,
        "Adapter" / WString,
        "OidBufferLen" / Int32ul,
        "OidBuffer" / Bytes(lambda this: this.OidBufferLen),
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=8, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_8_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=9, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_9_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=10, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_10_0(Etw):
    pattern = Struct(
        "TeamNic" / WString,
        "PacketFilter" / Int32ul
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=11, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_11_0(Etw):
    pattern = Struct(
        "TeamNic" / WString,
        "Member" / WString,
        "PacketFilter" / Int32ul
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=12, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_12_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=13, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_13_0(Etw):
    pattern = Struct(
        "Member" / WString,
        "TeamNic" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=14, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_14_0(Etw):
    pattern = Struct(
        "Member" / WString,
        "TeamNic" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=15, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_15_0(Etw):
    pattern = Struct(
        "Oid" / Int32ul,
        "Adapter" / WString,
        "OidBufferLen" / Int32ul,
        "OidBuffer" / Bytes(lambda this: this.OidBufferLen),
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=16, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_16_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=17, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_17_0(Etw):
    pattern = Struct(
        "Adapter" / WString
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=19, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_19_0(Etw):
    pattern = Struct(
        "Adapter" / WString
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=20, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_20_0(Etw):
    pattern = Struct(
        "Adapter" / WString
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=21, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_21_0(Etw):
    pattern = Struct(
        "Adapter" / WString
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=22, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_22_0(Etw):
    pattern = Struct(
        "Adapter" / WString
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=23, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_23_0(Etw):
    pattern = Struct(
        "TeamNic" / WString,
        "Member" / WString
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=24, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_24_0(Etw):
    pattern = Struct(
        "Adapter" / WString
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=25, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_25_0(Etw):
    pattern = Struct(
        "Adapter" / WString
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=26, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_26_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=27, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_27_0(Etw):
    pattern = Struct(
        "TeamNic" / WString,
        "Member" / WString
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=28, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_28_0(Etw):
    pattern = Struct(
        "TeamNic" / WString,
        "Member" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=29, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_29_0(Etw):
    pattern = Struct(
        "TeamNic" / WString,
        "Member" / WString
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=30, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_30_0(Etw):
    pattern = Struct(
        "TeamNic" / WString,
        "Member" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=31, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_31_0(Etw):
    pattern = Struct(
        "Team" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=32, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_32_0(Etw):
    pattern = Struct(
        "Team" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=33, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_33_0(Etw):
    pattern = Struct(
        "Team" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=34, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_34_0(Etw):
    pattern = Struct(
        "Team" / WString,
        "Member" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=35, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_35_0(Etw):
    pattern = Struct(
        "Team" / WString,
        "Member" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=36, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_36_0(Etw):
    pattern = Struct(
        "Team" / WString,
        "TeamNic" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=37, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_37_0(Etw):
    pattern = Struct(
        "Team" / WString,
        "TeamNic" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=38, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_38_0(Etw):
    pattern = Struct(
        "Team" / WString,
        "TeamNic" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=39, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_39_0(Etw):
    pattern = Struct(
        "Team" / WString,
        "TeamNic" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=40, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_40_0(Etw):
    pattern = Struct(
        "Adapter" / WString
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=41, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_41_0(Etw):
    pattern = Struct(
        "TeamNic" / WString,
        "BufferLen" / Int32ul,
        "Buffer" / Bytes(lambda this: this.BufferLen)
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=42, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_42_0(Etw):
    pattern = Struct(
        "TeamNic" / WString,
        "BufferLen" / Int32ul,
        "Buffer" / Bytes(lambda this: this.BufferLen)
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=43, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_43_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "StatusBufferLength" / Int32ul,
        "StatusBuffer" / Bytes(lambda this: this.StatusBufferLength)
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=44, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_44_0(Etw):
    pattern = Struct(
        "TeamNic" / WString,
        "OldValue" / Int32ul,
        "NewValue" / Int32ul
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=45, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_45_0(Etw):
    pattern = Struct(
        "TeamNic" / WString,
        "OldValue" / Int32ul,
        "NewValue" / Int32ul
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=46, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_46_0(Etw):
    pattern = Struct(
        "Adapter" / WString
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=47, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_47_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("11c5d8ad-756a-42c2-8087-eb1b4a72a846"), event_id=48, version=0)
class Microsoft_Windows_NdisImPlatformEventProvider_48_0(Etw):
    pattern = Struct(
        "Adapter" / WString
    )

