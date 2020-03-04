# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Spell-Checking
GUID : d0e22efc-ac66-4b25-a72d-382736b5e940
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d0e22efc-ac66-4b25-a72d-382736b5e940"), event_id=1, version=0)
class Microsoft_Windows_Spell_Checking_1_0(Etw):
    pattern = Struct(
        "WordlistType" / Int32ul
    )


@declare(guid=guid("d0e22efc-ac66-4b25-a72d-382736b5e940"), event_id=2, version=0)
class Microsoft_Windows_Spell_Checking_2_0(Etw):
    pattern = Struct(
        "WordlistType" / Int32ul
    )


@declare(guid=guid("d0e22efc-ac66-4b25-a72d-382736b5e940"), event_id=16, version=0)
class Microsoft_Windows_Spell_Checking_16_0(Etw):
    pattern = Struct(
        "First" / WString,
        "Second" / WString
    )


@declare(guid=guid("d0e22efc-ac66-4b25-a72d-382736b5e940"), event_id=17, version=0)
class Microsoft_Windows_Spell_Checking_17_0(Etw):
    pattern = Struct(
        "string" / WString
    )


@declare(guid=guid("d0e22efc-ac66-4b25-a72d-382736b5e940"), event_id=18, version=0)
class Microsoft_Windows_Spell_Checking_18_0(Etw):
    pattern = Struct(
        "string" / WString
    )


@declare(guid=guid("d0e22efc-ac66-4b25-a72d-382736b5e940"), event_id=19, version=0)
class Microsoft_Windows_Spell_Checking_19_0(Etw):
    pattern = Struct(
        "string" / WString
    )


@declare(guid=guid("d0e22efc-ac66-4b25-a72d-382736b5e940"), event_id=20, version=0)
class Microsoft_Windows_Spell_Checking_20_0(Etw):
    pattern = Struct(
        "wordlist" / Int32ul,
        "languageTag" / WString
    )


@declare(guid=guid("d0e22efc-ac66-4b25-a72d-382736b5e940"), event_id=23, version=0)
class Microsoft_Windows_Spell_Checking_23_0(Etw):
    pattern = Struct(
        "WordlistType" / Int32ul
    )


@declare(guid=guid("d0e22efc-ac66-4b25-a72d-382736b5e940"), event_id=24, version=0)
class Microsoft_Windows_Spell_Checking_24_0(Etw):
    pattern = Struct(
        "WordlistType" / Int32ul
    )


@declare(guid=guid("d0e22efc-ac66-4b25-a72d-382736b5e940"), event_id=27, version=0)
class Microsoft_Windows_Spell_Checking_27_0(Etw):
    pattern = Struct(
        "hr" / Int32sl
    )


@declare(guid=guid("d0e22efc-ac66-4b25-a72d-382736b5e940"), event_id=28, version=0)
class Microsoft_Windows_Spell_Checking_28_0(Etw):
    pattern = Struct(
        "hr" / Int32sl
    )


@declare(guid=guid("d0e22efc-ac66-4b25-a72d-382736b5e940"), event_id=29, version=0)
class Microsoft_Windows_Spell_Checking_29_0(Etw):
    pattern = Struct(
        "hr" / Int32sl
    )


@declare(guid=guid("d0e22efc-ac66-4b25-a72d-382736b5e940"), event_id=31, version=0)
class Microsoft_Windows_Spell_Checking_31_0(Etw):
    pattern = Struct(
        "wordlist" / Int32ul,
        "hr" / Int32sl
    )


@declare(guid=guid("d0e22efc-ac66-4b25-a72d-382736b5e940"), event_id=34, version=0)
class Microsoft_Windows_Spell_Checking_34_0(Etw):
    pattern = Struct(
        "First" / WString,
        "Second" / WString,
        "hr" / Int32sl
    )

