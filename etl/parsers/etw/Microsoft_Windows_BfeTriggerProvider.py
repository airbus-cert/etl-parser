# -*- coding: utf-8 -*-
"""
Microsoft-Windows-BfeTriggerProvider
GUID : 54732ee5-61ca-4727-9da1-10be5a4f773d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("54732ee5-61ca-4727-9da1-10be5a4f773d"), event_id=1, version=0)
class Microsoft_Windows_BfeTriggerProvider_1_0(Etw):
    pattern = Struct(
        "FirewallPortStatusChangeGuid" / Guid
    )


@declare(guid=guid("54732ee5-61ca-4727-9da1-10be5a4f773d"), event_id=2, version=0)
class Microsoft_Windows_BfeTriggerProvider_2_0(Etw):
    pattern = Struct(
        "FirewallPortStatusChangeGuid" / Guid
    )

