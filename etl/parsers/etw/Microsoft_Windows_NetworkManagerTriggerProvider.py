# -*- coding: utf-8 -*-
"""
Microsoft-Windows-NetworkManagerTriggerProvider
GUID : 9b307223-4e4d-4bf5-9be8-995cd8e7420b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9b307223-4e4d-4bf5-9be8-995cd8e7420b"), event_id=1, version=0)
class Microsoft_Windows_NetworkManagerTriggerProvider_1_0(Etw):
    pattern = Struct(
        "NetworkChangeGuid" / Guid
    )


@declare(guid=guid("9b307223-4e4d-4bf5-9be8-995cd8e7420b"), event_id=2, version=0)
class Microsoft_Windows_NetworkManagerTriggerProvider_2_0(Etw):
    pattern = Struct(
        "NetworkChangeGuid" / Guid
    )

