# -*- coding: utf-8 -*-
"""
Microsoft-Windows-IdleTriggerProvider
GUID : 9e03f75a-bcbe-428a-8f3c-d46f2a444935
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9e03f75a-bcbe-428a-8f3c-d46f2a444935"), event_id=1, version=0)
class Microsoft_Windows_IdleTriggerProvider_1_0(Etw):
    pattern = Struct(
        "IdleStatusGuid" / Guid
    )

