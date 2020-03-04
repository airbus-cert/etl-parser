# -*- coding: utf-8 -*-
"""
Microsoft-Windows-NetworkProfileTriggerProvider
GUID : fbcfac3f-8460-419f-8e48-1f0b49cdb85e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("fbcfac3f-8460-419f-8e48-1f0b49cdb85e"), event_id=1, version=0)
class Microsoft_Windows_NetworkProfileTriggerProvider_1_0(Etw):
    pattern = Struct(
        "ProfileChange" / WString
    )

