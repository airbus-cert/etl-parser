# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TSF-UIManager
GUID : 4dd778b8-379c-4d8c-b659-517a43d6df7d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4dd778b8-379c-4d8c-b659-517a43d6df7d"), event_id=5, version=0)
class Microsoft_Windows_TSF_UIManager_5_0(Etw):
    pattern = Struct(
        "contextFlags" / Int32ul,
        "cItems" / Int32sl,
        "targetRangeLeft" / Int32sl,
        "targetRangeTop" / Int32sl,
        "targetRangeRight" / Int32sl,
        "targetRangeBottom" / Int32sl
    )


@declare(guid=guid("4dd778b8-379c-4d8c-b659-517a43d6df7d"), event_id=7, version=0)
class Microsoft_Windows_TSF_UIManager_7_0(Etw):
    pattern = Struct(
        "contextFlags" / Int32ul,
        "cItems" / Int32sl,
        "targetRangeLeft" / Int32sl,
        "targetRangeTop" / Int32sl,
        "targetRangeRight" / Int32sl,
        "targetRangeBottom" / Int32sl
    )


@declare(guid=guid("4dd778b8-379c-4d8c-b659-517a43d6df7d"), event_id=11, version=0)
class Microsoft_Windows_TSF_UIManager_11_0(Etw):
    pattern = Struct(
        "targetRangeLeft" / Int32sl,
        "targetRangeTop" / Int32sl,
        "targetRangeRight" / Int32sl,
        "targetRangeBottom" / Int32sl
    )


@declare(guid=guid("4dd778b8-379c-4d8c-b659-517a43d6df7d"), event_id=13, version=0)
class Microsoft_Windows_TSF_UIManager_13_0(Etw):
    pattern = Struct(
        "start" / Int32ul,
        "end" / Int32ul
    )


@declare(guid=guid("4dd778b8-379c-4d8c-b659-517a43d6df7d"), event_id=19, version=0)
class Microsoft_Windows_TSF_UIManager_19_0(Etw):
    pattern = Struct(
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl
    )


@declare(guid=guid("4dd778b8-379c-4d8c-b659-517a43d6df7d"), event_id=102, version=0)
class Microsoft_Windows_TSF_UIManager_102_0(Etw):
    pattern = Struct(
        "langId" / Int32ul,
        "clsId" / Guid,
        "guidProfile" / Guid
    )


@declare(guid=guid("4dd778b8-379c-4d8c-b659-517a43d6df7d"), event_id=214, version=0)
class Microsoft_Windows_TSF_UIManager_214_0(Etw):
    pattern = Struct(
        "value" / Int32ul
    )


@declare(guid=guid("4dd778b8-379c-4d8c-b659-517a43d6df7d"), event_id=216, version=0)
class Microsoft_Windows_TSF_UIManager_216_0(Etw):
    pattern = Struct(
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl
    )


@declare(guid=guid("4dd778b8-379c-4d8c-b659-517a43d6df7d"), event_id=308, version=0)
class Microsoft_Windows_TSF_UIManager_308_0(Etw):
    pattern = Struct(
        "action" / Int32ul,
        "param" / Int32sl
    )


@declare(guid=guid("4dd778b8-379c-4d8c-b659-517a43d6df7d"), event_id=310, version=0)
class Microsoft_Windows_TSF_UIManager_310_0(Etw):
    pattern = Struct(
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl
    )


@declare(guid=guid("4dd778b8-379c-4d8c-b659-517a43d6df7d"), event_id=311, version=0)
class Microsoft_Windows_TSF_UIManager_311_0(Etw):
    pattern = Struct(
        "langid" / Int32ul,
        "viewflags" / Int32ul
    )


@declare(guid=guid("4dd778b8-379c-4d8c-b659-517a43d6df7d"), event_id=350, version=0)
class Microsoft_Windows_TSF_UIManager_350_0(Etw):
    pattern = Struct(
        "value" / Int32ul
    )


@declare(guid=guid("4dd778b8-379c-4d8c-b659-517a43d6df7d"), event_id=400, version=0)
class Microsoft_Windows_TSF_UIManager_400_0(Etw):
    pattern = Struct(
        "value" / Int32ul
    )


@declare(guid=guid("4dd778b8-379c-4d8c-b659-517a43d6df7d"), event_id=402, version=0)
class Microsoft_Windows_TSF_UIManager_402_0(Etw):
    pattern = Struct(
        "index" / Int32ul,
        "commit" / Int8ul
    )


@declare(guid=guid("4dd778b8-379c-4d8c-b659-517a43d6df7d"), event_id=502, version=0)
class Microsoft_Windows_TSF_UIManager_502_0(Etw):
    pattern = Struct(
        "start" / Int32ul,
        "end" / Int32ul
    )


@declare(guid=guid("4dd778b8-379c-4d8c-b659-517a43d6df7d"), event_id=504, version=0)
class Microsoft_Windows_TSF_UIManager_504_0(Etw):
    pattern = Struct(
        "start" / Int32ul,
        "end" / Int32ul
    )

