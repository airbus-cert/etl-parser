# -*- coding: utf-8 -*-
"""
Microsoft-Windows-UserDataAccess-CEMAPI
GUID : 83a9277a-d2fc-4b34-bf81-8ceb4407824f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("83a9277a-d2fc-4b34-bf81-8ceb4407824f"), event_id=1, version=0)
class Microsoft_Windows_UserDataAccess_CEMAPI_1_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("83a9277a-d2fc-4b34-bf81-8ceb4407824f"), event_id=2, version=0)
class Microsoft_Windows_UserDataAccess_CEMAPI_2_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("83a9277a-d2fc-4b34-bf81-8ceb4407824f"), event_id=3, version=0)
class Microsoft_Windows_UserDataAccess_CEMAPI_3_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("83a9277a-d2fc-4b34-bf81-8ceb4407824f"), event_id=4803, version=0)
class Microsoft_Windows_UserDataAccess_CEMAPI_4803_0(Etw):
    pattern = Struct(
        "Prop_Hex_UInt32" / Int32ul
    )

