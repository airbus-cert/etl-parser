# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Spellchecking-Host
GUID : 1bda2ab1-bbc1-4acb-a849-c0ef2b249672
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("1bda2ab1-bbc1-4acb-a849-c0ef2b249672"), event_id=0, version=0)
class Microsoft_Windows_Spellchecking_Host_0_0(Etw):
    pattern = Struct(
        "clsid" / Guid,
        "hresult" / Int32ul
    )


@declare(guid=guid("1bda2ab1-bbc1-4acb-a849-c0ef2b249672"), event_id=1, version=0)
class Microsoft_Windows_Spellchecking_Host_1_0(Etw):
    pattern = Struct(
        "string" / WString,
        "hresult" / Int32ul
    )


@declare(guid=guid("1bda2ab1-bbc1-4acb-a849-c0ef2b249672"), event_id=2, version=0)
class Microsoft_Windows_Spellchecking_Host_2_0(Etw):
    pattern = Struct(
        "Wordlist" / Int32ul,
        "String" / WString,
        "Hresult" / Int32ul
    )


@declare(guid=guid("1bda2ab1-bbc1-4acb-a849-c0ef2b249672"), event_id=3, version=0)
class Microsoft_Windows_Spellchecking_Host_3_0(Etw):
    pattern = Struct(
        "Wordlist" / Int32ul
    )


@declare(guid=guid("1bda2ab1-bbc1-4acb-a849-c0ef2b249672"), event_id=4, version=0)
class Microsoft_Windows_Spellchecking_Host_4_0(Etw):
    pattern = Struct(
        "Wordlist" / Int32ul
    )

