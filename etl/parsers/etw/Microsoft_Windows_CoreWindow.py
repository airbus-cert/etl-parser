# -*- coding: utf-8 -*-
"""
Microsoft-Windows-CoreWindow
GUID : a3d95055-34cc-4e4a-b99f-ec88f5370495
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a3d95055-34cc-4e4a-b99f-ec88f5370495"), event_id=1003, version=0)
class Microsoft_Windows_CoreWindow_1003_0(Etw):
    pattern = Struct(
        "PointerId" / Int32ul
    )


@declare(guid=guid("a3d95055-34cc-4e4a-b99f-ec88f5370495"), event_id=1004, version=0)
class Microsoft_Windows_CoreWindow_1004_0(Etw):
    pattern = Struct(
        "PointerId" / Int32ul
    )


@declare(guid=guid("a3d95055-34cc-4e4a-b99f-ec88f5370495"), event_id=1005, version=0)
class Microsoft_Windows_CoreWindow_1005_0(Etw):
    pattern = Struct(
        "PointerId" / Int32ul
    )


@declare(guid=guid("a3d95055-34cc-4e4a-b99f-ec88f5370495"), event_id=1006, version=0)
class Microsoft_Windows_CoreWindow_1006_0(Etw):
    pattern = Struct(
        "PointerId" / Int32ul
    )

