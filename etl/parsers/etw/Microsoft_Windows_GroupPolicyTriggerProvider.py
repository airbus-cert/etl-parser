# -*- coding: utf-8 -*-
"""
Microsoft-Windows-GroupPolicyTriggerProvider
GUID : bd2f4252-5e1e-49fc-9a30-f3978ad89ee2
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("bd2f4252-5e1e-49fc-9a30-f3978ad89ee2"), event_id=1, version=0)
class Microsoft_Windows_GroupPolicyTriggerProvider_1_0(Etw):
    pattern = Struct(
        "GPTriggerEventGuid" / Guid
    )


@declare(guid=guid("bd2f4252-5e1e-49fc-9a30-f3978ad89ee2"), event_id=2, version=0)
class Microsoft_Windows_GroupPolicyTriggerProvider_2_0(Etw):
    pattern = Struct(
        "GPTriggerEventGuid" / Guid
    )

