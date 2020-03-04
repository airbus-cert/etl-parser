# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Crashdump
GUID : ecdaacfa-6fe9-477c-b5f0-85b76f8f50aa
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ecdaacfa-6fe9-477c-b5f0-85b76f8f50aa"), event_id=1, version=1)
class Microsoft_Windows_Crashdump_1_1(Etw):
    pattern = Struct(
        "ResumeCapable" / Int8ul,
        "ReasonCodes" / Int32ul
    )


@declare(guid=guid("ecdaacfa-6fe9-477c-b5f0-85b76f8f50aa"), event_id=2, version=1)
class Microsoft_Windows_Crashdump_2_1(Etw):
    pattern = Struct(
        "Minimum" / Int32ul,
        "Maximum" / Int32ul
    )

