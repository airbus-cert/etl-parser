# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Winsock-WS2HELP
GUID : d5c25f9a-4d47-493e-9184-40dd397a004d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d5c25f9a-4d47-493e-9184-40dd397a004d"), event_id=1, version=0)
class Microsoft_Windows_Winsock_WS2HELP_1_0(Etw):
    pattern = Struct(
        "LSPName" / WString,
        "Catalog" / Int32ul,
        "Installer" / CString,
        "GUID" / Guid,
        "Category" / Int32ul
    )


@declare(guid=guid("d5c25f9a-4d47-493e-9184-40dd397a004d"), event_id=2, version=0)
class Microsoft_Windows_Winsock_WS2HELP_2_0(Etw):
    pattern = Struct(
        "LSPName" / WString,
        "Catalog" / Int32ul,
        "Installer" / CString,
        "GUID" / Guid,
        "Category" / Int32ul
    )


@declare(guid=guid("d5c25f9a-4d47-493e-9184-40dd397a004d"), event_id=3, version=0)
class Microsoft_Windows_Winsock_WS2HELP_3_0(Etw):
    pattern = Struct(
        "LSPName" / WString,
        "Catalog" / Int32ul,
        "Installer" / CString,
        "GUID" / Guid,
        "Category" / Int32ul
    )


@declare(guid=guid("d5c25f9a-4d47-493e-9184-40dd397a004d"), event_id=4, version=0)
class Microsoft_Windows_Winsock_WS2HELP_4_0(Etw):
    pattern = Struct(
        "Catalog" / Int32ul
    )

