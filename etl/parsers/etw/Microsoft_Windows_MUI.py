# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MUI
GUID : a8a1f2f6-a13a-45e9-b1fe-3419569e5ef2
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a8a1f2f6-a13a-45e9-b1fe-3419569e5ef2"), event_id=2000, version=0)
class Microsoft_Windows_MUI_2000_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("a8a1f2f6-a13a-45e9-b1fe-3419569e5ef2"), event_id=2001, version=0)
class Microsoft_Windows_MUI_2001_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("a8a1f2f6-a13a-45e9-b1fe-3419569e5ef2"), event_id=2002, version=0)
class Microsoft_Windows_MUI_2002_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "Type" / Int32ul,
        "FunctionName" / CString
    )


@declare(guid=guid("a8a1f2f6-a13a-45e9-b1fe-3419569e5ef2"), event_id=2003, version=0)
class Microsoft_Windows_MUI_2003_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("a8a1f2f6-a13a-45e9-b1fe-3419569e5ef2"), event_id=2004, version=0)
class Microsoft_Windows_MUI_2004_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("a8a1f2f6-a13a-45e9-b1fe-3419569e5ef2"), event_id=2012, version=0)
class Microsoft_Windows_MUI_2012_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a8a1f2f6-a13a-45e9-b1fe-3419569e5ef2"), event_id=3000, version=0)
class Microsoft_Windows_MUI_3000_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "NewLanguage" / WString,
        "PrevLanguage" / WString,
        "ExtendedFlag" / Int32ul
    )


@declare(guid=guid("a8a1f2f6-a13a-45e9-b1fe-3419569e5ef2"), event_id=3002, version=0)
class Microsoft_Windows_MUI_3002_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "FunctionName" / CString,
        "ReturnValue" / Int32ul
    )


@declare(guid=guid("a8a1f2f6-a13a-45e9-b1fe-3419569e5ef2"), event_id=3003, version=0)
class Microsoft_Windows_MUI_3003_0(Etw):
    pattern = Struct(
        "Parameter" / WString
    )


@declare(guid=guid("a8a1f2f6-a13a-45e9-b1fe-3419569e5ef2"), event_id=3004, version=0)
class Microsoft_Windows_MUI_3004_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "Affinity" / WString,
        "Sequence" / Int32sl,
        "Priority" / Int32sl
    )


@declare(guid=guid("a8a1f2f6-a13a-45e9-b1fe-3419569e5ef2"), event_id=3005, version=0)
class Microsoft_Windows_MUI_3005_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("a8a1f2f6-a13a-45e9-b1fe-3419569e5ef2"), event_id=3006, version=0)
class Microsoft_Windows_MUI_3006_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("a8a1f2f6-a13a-45e9-b1fe-3419569e5ef2"), event_id=3007, version=0)
class Microsoft_Windows_MUI_3007_0(Etw):
    pattern = Struct(
        "NewCacheIndex" / Int32ul,
        "LiveCacheIndex" / Int32ul,
        "Config" / Int32ul
    )


@declare(guid=guid("a8a1f2f6-a13a-45e9-b1fe-3419569e5ef2"), event_id=3008, version=0)
class Microsoft_Windows_MUI_3008_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("a8a1f2f6-a13a-45e9-b1fe-3419569e5ef2"), event_id=3009, version=0)
class Microsoft_Windows_MUI_3009_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("a8a1f2f6-a13a-45e9-b1fe-3419569e5ef2"), event_id=3010, version=0)
class Microsoft_Windows_MUI_3010_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("a8a1f2f6-a13a-45e9-b1fe-3419569e5ef2"), event_id=3011, version=0)
class Microsoft_Windows_MUI_3011_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("a8a1f2f6-a13a-45e9-b1fe-3419569e5ef2"), event_id=3012, version=0)
class Microsoft_Windows_MUI_3012_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )

