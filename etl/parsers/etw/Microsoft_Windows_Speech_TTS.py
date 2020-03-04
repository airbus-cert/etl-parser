# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Speech-TTS
GUID : 74dcc47a-846e-4c98-9e2c-80043ed82b15
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("74dcc47a-846e-4c98-9e2c-80043ed82b15"), event_id=1, version=0)
class Microsoft_Windows_Speech_TTS_1_0(Etw):
    pattern = Struct(
        "Instance" / Int64ul
    )


@declare(guid=guid("74dcc47a-846e-4c98-9e2c-80043ed82b15"), event_id=2, version=0)
class Microsoft_Windows_Speech_TTS_2_0(Etw):
    pattern = Struct(
        "Instance" / Int64ul
    )


@declare(guid=guid("74dcc47a-846e-4c98-9e2c-80043ed82b15"), event_id=3, version=0)
class Microsoft_Windows_Speech_TTS_3_0(Etw):
    pattern = Struct(
        "Instance" / Int64ul
    )


@declare(guid=guid("74dcc47a-846e-4c98-9e2c-80043ed82b15"), event_id=4, version=0)
class Microsoft_Windows_Speech_TTS_4_0(Etw):
    pattern = Struct(
        "Instance" / Int64ul
    )


@declare(guid=guid("74dcc47a-846e-4c98-9e2c-80043ed82b15"), event_id=5, version=0)
class Microsoft_Windows_Speech_TTS_5_0(Etw):
    pattern = Struct(
        "Instance" / Int64ul
    )

