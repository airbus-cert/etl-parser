# -*- coding: utf-8 -*-
"""
NetJoin
GUID : 9741fd4e-3757-479f-a3c6-fc49f6d5edd0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9741fd4e-3757-479f-a3c6-fc49f6d5edd0"), event_id=4096, version=0)
class NetJoin_4096_0(Etw):
    pattern = Struct(
        "DomainName" / WString,
        "ComputerName" / WString
    )


@declare(guid=guid("9741fd4e-3757-479f-a3c6-fc49f6d5edd0"), event_id=4097, version=0)
class NetJoin_4097_0(Etw):
    pattern = Struct(
        "DomainName" / WString,
        "ComputerName" / WString,
        "NetStatusCode" / Int32ul
    )

