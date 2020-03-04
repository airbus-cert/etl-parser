# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-XDV
GUID : f029ac39-38f0-4a40-b7de-404d244004cb
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f029ac39-38f0-4a40-b7de-404d244004cb"), event_id=3, version=0)
class Microsoft_Windows_Kernel_XDV_3_0(Etw):
    pattern = Struct(
        "IRP_Address" / Int64ul,
        "IRP_Stack_Loc_Code" / Int32ul,
        "IRP_Parameters" / Int32ul,
        "Module" / WString,
        "UInt32_Event_Number" / Int32ul,
        "Address_Stack" / Int64ul
    )


@declare(guid=guid("f029ac39-38f0-4a40-b7de-404d244004cb"), event_id=4, version=0)
class Microsoft_Windows_Kernel_XDV_4_0(Etw):
    pattern = Struct(
        "RuleId" / Int32ul,
        "ErrorMessage" / CString,
        "Module" / WString,
        "Irql" / Int8ul
    )

