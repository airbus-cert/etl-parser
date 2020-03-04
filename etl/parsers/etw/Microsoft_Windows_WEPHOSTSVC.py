# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WEPHOSTSVC
GUID : d5f7235b-48e2-4e9c-92fe-0e4950aba9e8
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d5f7235b-48e2-4e9c-92fe-0e4950aba9e8"), event_id=1, version=0)
class Microsoft_Windows_WEPHOSTSVC_1_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("d5f7235b-48e2-4e9c-92fe-0e4950aba9e8"), event_id=2, version=0)
class Microsoft_Windows_WEPHOSTSVC_2_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )

