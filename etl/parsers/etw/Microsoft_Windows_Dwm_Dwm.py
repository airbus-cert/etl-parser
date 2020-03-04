# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Dwm-Dwm
GUID : d29d56ea-4867-4221-b02e-cfd998834075
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d29d56ea-4867-4221-b02e-cfd998834075"), event_id=1, version=0)
class Microsoft_Windows_Dwm_Dwm_1_0(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "Input" / Int32ul
    )


@declare(guid=guid("d29d56ea-4867-4221-b02e-cfd998834075"), event_id=2, version=0)
class Microsoft_Windows_Dwm_Dwm_2_0(Etw):
    pattern = Struct(
        "State" / Int32ul
    )


@declare(guid=guid("d29d56ea-4867-4221-b02e-cfd998834075"), event_id=3, version=0)
class Microsoft_Windows_Dwm_Dwm_3_0(Etw):
    pattern = Struct(
        "Capability" / Int32ul,
        "Verified" / Int32ul
    )


@declare(guid=guid("d29d56ea-4867-4221-b02e-cfd998834075"), event_id=4, version=0)
class Microsoft_Windows_Dwm_Dwm_4_0(Etw):
    pattern = Struct(
        "Flag" / Int32ul
    )


@declare(guid=guid("d29d56ea-4867-4221-b02e-cfd998834075"), event_id=5, version=0)
class Microsoft_Windows_Dwm_Dwm_5_0(Etw):
    pattern = Struct(
        "Flag" / Int32ul
    )


@declare(guid=guid("d29d56ea-4867-4221-b02e-cfd998834075"), event_id=6, version=0)
class Microsoft_Windows_Dwm_Dwm_6_0(Etw):
    pattern = Struct(
        "IsCapable" / Int32ul,
        "AllowDwmcoreInSession" / Int32ul,
        "RemoteAppEnabled" / Int32ul,
        "AllowDwmcoreInClient" / Int32ul,
        "AllowThemesInCLient" / Int32ul
    )


@declare(guid=guid("d29d56ea-4867-4221-b02e-cfd998834075"), event_id=9, version=0)
class Microsoft_Windows_Dwm_Dwm_9_0(Etw):
    pattern = Struct(
        "MilRemote" / Int32ul
    )


@declare(guid=guid("d29d56ea-4867-4221-b02e-cfd998834075"), event_id=11, version=0)
class Microsoft_Windows_Dwm_Dwm_11_0(Etw):
    pattern = Struct(
        "CGhostOrHwndToGhost" / Int64ul
    )


@declare(guid=guid("d29d56ea-4867-4221-b02e-cfd998834075"), event_id=12, version=0)
class Microsoft_Windows_Dwm_Dwm_12_0(Etw):
    pattern = Struct(
        "CGhostOrHwndToGhost" / Int64ul
    )


@declare(guid=guid("d29d56ea-4867-4221-b02e-cfd998834075"), event_id=13, version=0)
class Microsoft_Windows_Dwm_Dwm_13_0(Etw):
    pattern = Struct(
        "CGhostOrHwndToGhost" / Int64ul
    )


@declare(guid=guid("d29d56ea-4867-4221-b02e-cfd998834075"), event_id=14, version=0)
class Microsoft_Windows_Dwm_Dwm_14_0(Etw):
    pattern = Struct(
        "StateBegin" / Int32ul,
        "StateEnd" / Int32ul
    )

