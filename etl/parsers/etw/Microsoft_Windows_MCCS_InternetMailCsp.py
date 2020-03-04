# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MCCS-InternetMailCsp
GUID : bec5e7a4-0527-42e8-8174-fabde799ad7f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("bec5e7a4-0527-42e8-8174-fabde799ad7f"), event_id=1, version=0)
class Microsoft_Windows_MCCS_InternetMailCsp_1_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("bec5e7a4-0527-42e8-8174-fabde799ad7f"), event_id=2, version=0)
class Microsoft_Windows_MCCS_InternetMailCsp_2_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )

