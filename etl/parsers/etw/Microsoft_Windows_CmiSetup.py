# -*- coding: utf-8 -*-
"""
Microsoft-Windows-CmiSetup
GUID : 75ebc33e-0cc6-49da-8cd9-8903a5222aa0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("75ebc33e-0cc6-49da-8cd9-8903a5222aa0"), event_id=1002, version=0)
class Microsoft_Windows_CmiSetup_1002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("75ebc33e-0cc6-49da-8cd9-8903a5222aa0"), event_id=2002, version=0)
class Microsoft_Windows_CmiSetup_2002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("75ebc33e-0cc6-49da-8cd9-8903a5222aa0"), event_id=3002, version=0)
class Microsoft_Windows_CmiSetup_3002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )

