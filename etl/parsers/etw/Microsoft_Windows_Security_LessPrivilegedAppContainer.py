# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Security-LessPrivilegedAppContainer
GUID : 45eec9e5-4a1b-5446-7ad8-a4ab1313c437
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("45eec9e5-4a1b-5446-7ad8-a4ab1313c437"), event_id=1, version=0)
class Microsoft_Windows_Security_LessPrivilegedAppContainer_1_0(Etw):
    pattern = Struct(
        "FailureTime" / Int64ul,
        "StackHash" / Int32ul
    )

