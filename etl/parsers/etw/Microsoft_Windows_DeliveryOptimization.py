# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DeliveryOptimization
GUID : f8ad09ba-419c-5134-1750-270f4d0fb889
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f8ad09ba-419c-5134-1750-270f4d0fb889"), event_id=0, version=0)
class Microsoft_Windows_DeliveryOptimization_0_0(Etw):
    pattern = Struct(
        "policyName" / WString,
        "policyValue" / WString
    )

