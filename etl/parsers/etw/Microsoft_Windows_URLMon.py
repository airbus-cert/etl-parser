# -*- coding: utf-8 -*-
"""
Microsoft-Windows-URLMon
GUID : 245f975d-909d-49ed-b8f9-9a75691d6b6b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("245f975d-909d-49ed-b8f9-9a75691d6b6b"), event_id=801, version=0)
class Microsoft_Windows_URLMon_801_0(Etw):
    pattern = Struct(
        "Msg" / Int32ul,
        "URL" / WString
    )


@declare(guid=guid("245f975d-909d-49ed-b8f9-9a75691d6b6b"), event_id=802, version=0)
class Microsoft_Windows_URLMon_802_0(Etw):
    pattern = Struct(
        "Msg" / Int32ul,
        "URL" / WString
    )


@declare(guid=guid("245f975d-909d-49ed-b8f9-9a75691d6b6b"), event_id=803, version=0)
class Microsoft_Windows_URLMon_803_0(Etw):
    pattern = Struct(
        "Msg" / Int32ul,
        "URL" / WString,
        "Bytes" / Int32ul
    )


@declare(guid=guid("245f975d-909d-49ed-b8f9-9a75691d6b6b"), event_id=804, version=0)
class Microsoft_Windows_URLMon_804_0(Etw):
    pattern = Struct(
        "Bytes" / Int32ul,
        "URL" / WString
    )


@declare(guid=guid("245f975d-909d-49ed-b8f9-9a75691d6b6b"), event_id=805, version=0)
class Microsoft_Windows_URLMon_805_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "URL" / WString
    )


@declare(guid=guid("245f975d-909d-49ed-b8f9-9a75691d6b6b"), event_id=806, version=0)
class Microsoft_Windows_URLMon_806_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "URL" / WString
    )


@declare(guid=guid("245f975d-909d-49ed-b8f9-9a75691d6b6b"), event_id=807, version=0)
class Microsoft_Windows_URLMon_807_0(Etw):
    pattern = Struct(
        "CInet" / Int64ul,
        "Binding" / Int64ul
    )


@declare(guid=guid("245f975d-909d-49ed-b8f9-9a75691d6b6b"), event_id=808, version=0)
class Microsoft_Windows_URLMon_808_0(Etw):
    pattern = Struct(
        "Operation" / Int32ul,
        "Bytes" / Int32ul,
        "URL" / WString,
        "CInet" / Int64ul
    )

