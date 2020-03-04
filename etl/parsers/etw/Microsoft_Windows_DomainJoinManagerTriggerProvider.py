# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DomainJoinManagerTriggerProvider
GUID : 5b004607-1087-4f16-b10e-979685a8d131
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5b004607-1087-4f16-b10e-979685a8d131"), event_id=1, version=0)
class Microsoft_Windows_DomainJoinManagerTriggerProvider_1_0(Etw):
    pattern = Struct(
        "DomainMembershipChangeGuid" / Guid
    )


@declare(guid=guid("5b004607-1087-4f16-b10e-979685a8d131"), event_id=2, version=0)
class Microsoft_Windows_DomainJoinManagerTriggerProvider_2_0(Etw):
    pattern = Struct(
        "DomainMembershipChangeGuid" / Guid
    )

