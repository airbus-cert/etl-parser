# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SCPNP
GUID : 9f650c63-9409-453c-a652-83d7185a2e83
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9f650c63-9409-453c-a652-83d7185a2e83"), event_id=1000, version=0)
class Microsoft_Windows_SCPNP_1000_0(Etw):
    pattern = Struct(
        "ReaderName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("9f650c63-9409-453c-a652-83d7185a2e83"), event_id=1001, version=0)
class Microsoft_Windows_SCPNP_1001_0(Etw):
    pattern = Struct(
        "ReaderName" / WString,
        "FriendlyName" / WString
    )

