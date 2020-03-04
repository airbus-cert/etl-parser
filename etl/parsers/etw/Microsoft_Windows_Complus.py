# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Complus
GUID : 0f177893-4a9c-4709-b921-f432d67f43d5
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=774, version=0)
class Microsoft_Windows_Complus_774_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=775, version=0)
class Microsoft_Windows_Complus_775_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=776, version=0)
class Microsoft_Windows_Complus_776_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=777, version=0)
class Microsoft_Windows_Complus_777_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=778, version=0)
class Microsoft_Windows_Complus_778_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=779, version=0)
class Microsoft_Windows_Complus_779_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=780, version=0)
class Microsoft_Windows_Complus_780_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=781, version=0)
class Microsoft_Windows_Complus_781_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=782, version=0)
class Microsoft_Windows_Complus_782_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=783, version=0)
class Microsoft_Windows_Complus_783_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=4433, version=0)
class Microsoft_Windows_Complus_4433_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=4434, version=0)
class Microsoft_Windows_Complus_4434_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=4452, version=0)
class Microsoft_Windows_Complus_4452_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=4458, version=0)
class Microsoft_Windows_Complus_4458_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=4459, version=0)
class Microsoft_Windows_Complus_4459_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=4460, version=0)
class Microsoft_Windows_Complus_4460_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=4464, version=0)
class Microsoft_Windows_Complus_4464_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=4465, version=0)
class Microsoft_Windows_Complus_4465_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=4792, version=0)
class Microsoft_Windows_Complus_4792_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=4823, version=0)
class Microsoft_Windows_Complus_4823_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=4864, version=0)
class Microsoft_Windows_Complus_4864_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=5485, version=0)
class Microsoft_Windows_Complus_5485_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=5486, version=0)
class Microsoft_Windows_Complus_5486_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("0f177893-4a9c-4709-b921-f432d67f43d5"), event_id=5488, version=0)
class Microsoft_Windows_Complus_5488_0(Etw):
    pattern = Struct(
        "param1" / WString
    )

