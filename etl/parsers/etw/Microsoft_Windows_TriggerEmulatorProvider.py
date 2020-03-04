# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TriggerEmulatorProvider
GUID : f230d19a-5d93-47d9-a83f-53829edfb8df
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f230d19a-5d93-47d9-a83f-53829edfb8df"), event_id=1, version=0)
class Microsoft_Windows_TriggerEmulatorProvider_1_0(Etw):
    pattern = Struct(
        "ConsumerName" / WString,
        "NamedValues" / WString
    )

