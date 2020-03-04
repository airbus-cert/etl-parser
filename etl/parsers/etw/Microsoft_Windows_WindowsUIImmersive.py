# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WindowsUIImmersive
GUID : 74827cbb-1e0f-45a2-8523-c605866d2f22
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("74827cbb-1e0f-45a2-8523-c605866d2f22"), event_id=8705, version=0)
class Microsoft_Windows_WindowsUIImmersive_8705_0(Etw):
    pattern = Struct(
        "CommandID" / Int32ul
    )


@declare(guid=guid("74827cbb-1e0f-45a2-8523-c605866d2f22"), event_id=8712, version=0)
class Microsoft_Windows_WindowsUIImmersive_8712_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("74827cbb-1e0f-45a2-8523-c605866d2f22"), event_id=8720, version=0)
class Microsoft_Windows_WindowsUIImmersive_8720_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul,
        "ProcessID" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("74827cbb-1e0f-45a2-8523-c605866d2f22"), event_id=8722, version=0)
class Microsoft_Windows_WindowsUIImmersive_8722_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul,
        "DismissReason" / Int32ul
    )


@declare(guid=guid("74827cbb-1e0f-45a2-8523-c605866d2f22"), event_id=8723, version=0)
class Microsoft_Windows_WindowsUIImmersive_8723_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("74827cbb-1e0f-45a2-8523-c605866d2f22"), event_id=8742, version=0)
class Microsoft_Windows_WindowsUIImmersive_8742_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul
    )


@declare(guid=guid("74827cbb-1e0f-45a2-8523-c605866d2f22"), event_id=8751, version=0)
class Microsoft_Windows_WindowsUIImmersive_8751_0(Etw):
    pattern = Struct(
        "Left" / Int32sl,
        "Top" / Int32sl,
        "Right" / Int32sl,
        "Bottom" / Int32sl
    )

