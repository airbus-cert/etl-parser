# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Security-SPP
GUID : e23b33b0-c8c9-472c-a5f9-f2bdfea0f156
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e23b33b0-c8c9-472c-a5f9-f2bdfea0f156"), event_id=2, version=0)
class Microsoft_Windows_Security_SPP_2_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("e23b33b0-c8c9-472c-a5f9-f2bdfea0f156"), event_id=3, version=0)
class Microsoft_Windows_Security_SPP_3_0(Etw):
    pattern = Struct(
        "IsLowPriorityInit" / Int8ul
    )


@declare(guid=guid("e23b33b0-c8c9-472c-a5f9-f2bdfea0f156"), event_id=4, version=0)
class Microsoft_Windows_Security_SPP_4_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("e23b33b0-c8c9-472c-a5f9-f2bdfea0f156"), event_id=11, version=0)
class Microsoft_Windows_Security_SPP_11_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("e23b33b0-c8c9-472c-a5f9-f2bdfea0f156"), event_id=13, version=0)
class Microsoft_Windows_Security_SPP_13_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("e23b33b0-c8c9-472c-a5f9-f2bdfea0f156"), event_id=15, version=0)
class Microsoft_Windows_Security_SPP_15_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )

