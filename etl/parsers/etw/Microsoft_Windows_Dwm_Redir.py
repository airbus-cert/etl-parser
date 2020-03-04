# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Dwm-Redir
GUID : 7d99f6a4-1bec-4c09-9703-3aaa8148347f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7d99f6a4-1bec-4c09-9703-3aaa8148347f"), event_id=1, version=0)
class Microsoft_Windows_Dwm_Redir_1_0(Etw):
    pattern = Struct(
        "FlipChain" / Int32ul,
        "SerialNumber" / Int32ul,
        "BuffersEmpty" / Int32ul,
        "Index" / Int32ul,
        "IndexUnconfirmed" / Int32ul,
        "hSurface" / Int64ul
    )


@declare(guid=guid("7d99f6a4-1bec-4c09-9703-3aaa8148347f"), event_id=2, version=0)
class Microsoft_Windows_Dwm_Redir_2_0(Etw):
    pattern = Struct(
        "FlipChain" / Int32ul,
        "SerialNumber" / Int32ul,
        "BuffersEmpty" / Int32ul,
        "Index" / Int32ul,
        "IndexUnconfirmed" / Int32ul,
        "hSurface" / Int64ul
    )


@declare(guid=guid("7d99f6a4-1bec-4c09-9703-3aaa8148347f"), event_id=3, version=0)
class Microsoft_Windows_Dwm_Redir_3_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "AsyncFlushType" / Int32ul
    )


@declare(guid=guid("7d99f6a4-1bec-4c09-9703-3aaa8148347f"), event_id=4, version=0)
class Microsoft_Windows_Dwm_Redir_4_0(Etw):
    pattern = Struct(
        "Hwnd" / Int64ul,
        "xSizeOld" / Int32ul,
        "ySizeOld" / Int32ul,
        "formatOld" / Int64ul,
        "xSizeNew" / Int32ul,
        "ySizeNew" / Int32ul,
        "formatNew" / Int64ul
    )


@declare(guid=guid("7d99f6a4-1bec-4c09-9703-3aaa8148347f"), event_id=7, version=0)
class Microsoft_Windows_Dwm_Redir_7_0(Etw):
    pattern = Struct(
        "Hwnd" / Int64ul,
        "MessageId" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("7d99f6a4-1bec-4c09-9703-3aaa8148347f"), event_id=8, version=0)
class Microsoft_Windows_Dwm_Redir_8_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "fExcludedFromLivePreview" / Int8ul
    )


@declare(guid=guid("7d99f6a4-1bec-4c09-9703-3aaa8148347f"), event_id=9, version=0)
class Microsoft_Windows_Dwm_Redir_9_0(Etw):
    pattern = Struct(
        "logicalSurfaceHandle" / Int64ul,
        "spriteHandle" / Int64ul,
        "windowHandle" / Int64ul
    )


@declare(guid=guid("7d99f6a4-1bec-4c09-9703-3aaa8148347f"), event_id=10, version=0)
class Microsoft_Windows_Dwm_Redir_10_0(Etw):
    pattern = Struct(
        "Channel" / Int32ul,
        "visualHandle" / Int32ul,
        "interactionHandle" / Int32ul,
        "visualInternalHandleAndChannel" / Int64ul,
        "interactionInternalHandleAndChannel" / Int64ul
    )


@declare(guid=guid("7d99f6a4-1bec-4c09-9703-3aaa8148347f"), event_id=11, version=0)
class Microsoft_Windows_Dwm_Redir_11_0(Etw):
    pattern = Struct(
        "Enum" / Int32ul
    )


@declare(guid=guid("7d99f6a4-1bec-4c09-9703-3aaa8148347f"), event_id=12, version=0)
class Microsoft_Windows_Dwm_Redir_12_0(Etw):
    pattern = Struct(
        "Enum" / Int32ul
    )

