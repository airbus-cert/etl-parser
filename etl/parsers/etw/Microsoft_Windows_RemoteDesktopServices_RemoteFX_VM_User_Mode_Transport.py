# -*- coding: utf-8 -*-
"""
Microsoft-Windows-RemoteDesktopServices-RemoteFX-VM-User-Mode-Transport
GUID : 741c6be3-f74b-4e4d-88e7-5ce3a35faeb3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("741c6be3-f74b-4e4d-88e7-5ce3a35faeb3"), event_id=1, version=0)
class Microsoft_Windows_RemoteDesktopServices_RemoteFX_VM_User_Mode_Transport_1_0(Etw):
    pattern = Struct(
        "message" / WString
    )


@declare(guid=guid("741c6be3-f74b-4e4d-88e7-5ce3a35faeb3"), event_id=2, version=0)
class Microsoft_Windows_RemoteDesktopServices_RemoteFX_VM_User_Mode_Transport_2_0(Etw):
    pattern = Struct(
        "message" / WString
    )


@declare(guid=guid("741c6be3-f74b-4e4d-88e7-5ce3a35faeb3"), event_id=3, version=0)
class Microsoft_Windows_RemoteDesktopServices_RemoteFX_VM_User_Mode_Transport_3_0(Etw):
    pattern = Struct(
        "message" / WString
    )


@declare(guid=guid("741c6be3-f74b-4e4d-88e7-5ce3a35faeb3"), event_id=4, version=0)
class Microsoft_Windows_RemoteDesktopServices_RemoteFX_VM_User_Mode_Transport_4_0(Etw):
    pattern = Struct(
        "message" / WString
    )


@declare(guid=guid("741c6be3-f74b-4e4d-88e7-5ce3a35faeb3"), event_id=5, version=0)
class Microsoft_Windows_RemoteDesktopServices_RemoteFX_VM_User_Mode_Transport_5_0(Etw):
    pattern = Struct(
        "function" / WString,
        "size" / Int32ul,
        "operation" / WString
    )


@declare(guid=guid("741c6be3-f74b-4e4d-88e7-5ce3a35faeb3"), event_id=6, version=0)
class Microsoft_Windows_RemoteDesktopServices_RemoteFX_VM_User_Mode_Transport_6_0(Etw):
    pattern = Struct(
        "function" / WString,
        "task" / WString
    )


@declare(guid=guid("741c6be3-f74b-4e4d-88e7-5ce3a35faeb3"), event_id=7, version=0)
class Microsoft_Windows_RemoteDesktopServices_RemoteFX_VM_User_Mode_Transport_7_0(Etw):
    pattern = Struct(
        "function" / WString,
        "task" / WString
    )


@declare(guid=guid("741c6be3-f74b-4e4d-88e7-5ce3a35faeb3"), event_id=8, version=0)
class Microsoft_Windows_RemoteDesktopServices_RemoteFX_VM_User_Mode_Transport_8_0(Etw):
    pattern = Struct(
        "function" / WString,
        "event" / WString
    )

