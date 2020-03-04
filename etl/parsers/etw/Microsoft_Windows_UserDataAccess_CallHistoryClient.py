# -*- coding: utf-8 -*-
"""
Microsoft-Windows-UserDataAccess-CallHistoryClient
GUID : f5988abb-323a-4098-8a34-85a3613d4638
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f5988abb-323a-4098-8a34-85a3613d4638"), event_id=1, version=0)
class Microsoft_Windows_UserDataAccess_CallHistoryClient_1_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("f5988abb-323a-4098-8a34-85a3613d4638"), event_id=2, version=0)
class Microsoft_Windows_UserDataAccess_CallHistoryClient_2_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("f5988abb-323a-4098-8a34-85a3613d4638"), event_id=3, version=0)
class Microsoft_Windows_UserDataAccess_CallHistoryClient_3_0(Etw):
    pattern = Struct(
        "ObjPtr" / Int64ul,
        "ObjType" / Int32sl,
        "ObjId" / Int32sl,
        "PropCode" / Int32ul
    )


@declare(guid=guid("f5988abb-323a-4098-8a34-85a3613d4638"), event_id=4, version=0)
class Microsoft_Windows_UserDataAccess_CallHistoryClient_4_0(Etw):
    pattern = Struct(
        "RpcCode" / Int32ul,
        "OldCode" / Int32sl
    )


@declare(guid=guid("f5988abb-323a-4098-8a34-85a3613d4638"), event_id=5, version=0)
class Microsoft_Windows_UserDataAccess_CallHistoryClient_5_0(Etw):
    pattern = Struct(
        "P1" / Int32ul
    )


@declare(guid=guid("f5988abb-323a-4098-8a34-85a3613d4638"), event_id=6, version=0)
class Microsoft_Windows_UserDataAccess_CallHistoryClient_6_0(Etw):
    pattern = Struct(
        "P1" / Int32ul
    )


@declare(guid=guid("f5988abb-323a-4098-8a34-85a3613d4638"), event_id=7, version=0)
class Microsoft_Windows_UserDataAccess_CallHistoryClient_7_0(Etw):
    pattern = Struct(
        "P1" / Int32ul
    )

