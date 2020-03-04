# -*- coding: utf-8 -*-
"""
Microsoft-User Experience Virtualization-Admin
GUID : 61bc445e-7a8d-420e-ab36-9c7143881b98
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("61bc445e-7a8d-420e-ab36-9c7143881b98"), event_id=0, version=0)
class Microsoft_User_Experience_Virtualization_Admin_0_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("61bc445e-7a8d-420e-ab36-9c7143881b98"), event_id=1, version=0)
class Microsoft_User_Experience_Virtualization_Admin_1_0(Etw):
    pattern = Struct(
        "String" / WString,
        "Ulong" / Int64ul
    )

