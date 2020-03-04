# -*- coding: utf-8 -*-
"""
Microsoft-Windows-CorruptedFileRecovery-Client
GUID : ba093605-3909-4345-990b-26b746adee0a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ba093605-3909-4345-990b-26b746adee0a"), event_id=1, version=0)
class Microsoft_Windows_CorruptedFileRecovery_Client_1_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "AppName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ba093605-3909-4345-990b-26b746adee0a"), event_id=2, version=0)
class Microsoft_Windows_CorruptedFileRecovery_Client_2_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "AppName" / WString
    )


@declare(guid=guid("ba093605-3909-4345-990b-26b746adee0a"), event_id=3, version=0)
class Microsoft_Windows_CorruptedFileRecovery_Client_3_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "AppName" / WString
    )

