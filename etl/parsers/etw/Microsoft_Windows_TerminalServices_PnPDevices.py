# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TerminalServices-PnPDevices
GUID : 27a8c1e2-eb19-463e-8424-b399df27a216
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("27a8c1e2-eb19-463e-8424-b399df27a216"), event_id=2, version=0)
class Microsoft_Windows_TerminalServices_PnPDevices_2_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("27a8c1e2-eb19-463e-8424-b399df27a216"), event_id=3, version=0)
class Microsoft_Windows_TerminalServices_PnPDevices_3_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("27a8c1e2-eb19-463e-8424-b399df27a216"), event_id=4, version=0)
class Microsoft_Windows_TerminalServices_PnPDevices_4_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("27a8c1e2-eb19-463e-8424-b399df27a216"), event_id=5, version=0)
class Microsoft_Windows_TerminalServices_PnPDevices_5_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("27a8c1e2-eb19-463e-8424-b399df27a216"), event_id=6, version=0)
class Microsoft_Windows_TerminalServices_PnPDevices_6_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("27a8c1e2-eb19-463e-8424-b399df27a216"), event_id=7, version=0)
class Microsoft_Windows_TerminalServices_PnPDevices_7_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("27a8c1e2-eb19-463e-8424-b399df27a216"), event_id=8, version=0)
class Microsoft_Windows_TerminalServices_PnPDevices_8_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("27a8c1e2-eb19-463e-8424-b399df27a216"), event_id=9, version=0)
class Microsoft_Windows_TerminalServices_PnPDevices_9_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("27a8c1e2-eb19-463e-8424-b399df27a216"), event_id=32, version=0)
class Microsoft_Windows_TerminalServices_PnPDevices_32_0(Etw):
    pattern = Struct(
        "deviceName" / WString
    )


@declare(guid=guid("27a8c1e2-eb19-463e-8424-b399df27a216"), event_id=33, version=0)
class Microsoft_Windows_TerminalServices_PnPDevices_33_0(Etw):
    pattern = Struct(
        "deviceName" / WString
    )


@declare(guid=guid("27a8c1e2-eb19-463e-8424-b399df27a216"), event_id=34, version=0)
class Microsoft_Windows_TerminalServices_PnPDevices_34_0(Etw):
    pattern = Struct(
        "deviceName" / WString
    )


@declare(guid=guid("27a8c1e2-eb19-463e-8424-b399df27a216"), event_id=35, version=0)
class Microsoft_Windows_TerminalServices_PnPDevices_35_0(Etw):
    pattern = Struct(
        "deviceName" / WString
    )


@declare(guid=guid("27a8c1e2-eb19-463e-8424-b399df27a216"), event_id=37, version=0)
class Microsoft_Windows_TerminalServices_PnPDevices_37_0(Etw):
    pattern = Struct(
        "deviceName" / WString
    )

