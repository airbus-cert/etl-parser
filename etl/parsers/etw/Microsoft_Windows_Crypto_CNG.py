# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Crypto-CNG
GUID : e3e0e2f0-c9c5-11e0-8ab9-9ebc4824019b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e3e0e2f0-c9c5-11e0-8ab9-9ebc4824019b"), event_id=1, version=0)
class Microsoft_Windows_Crypto_CNG_1_0(Etw):
    pattern = Struct(
        "ProviderName" / WString,
        "AlgorithmName" / WString,
        "dwFlags" / Int32ul,
        "Status" / Int32ul,
        "OperationType" / Int32ul
    )

