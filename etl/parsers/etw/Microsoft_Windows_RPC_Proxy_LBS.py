# -*- coding: utf-8 -*-
"""
Microsoft-Windows-RPC-Proxy-LBS
GUID : 272a979b-34b5-48ec-94f5-7225a59c85a0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("272a979b-34b5-48ec-94f5-7225a59c85a0"), event_id=1, version=1)
class Microsoft_Windows_RPC_Proxy_LBS_1_1(Etw):
    pattern = Struct(
        "UserName" / WString
    )


@declare(guid=guid("272a979b-34b5-48ec-94f5-7225a59c85a0"), event_id=2, version=1)
class Microsoft_Windows_RPC_Proxy_LBS_2_1(Etw):
    pattern = Struct(
        "ServerName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("272a979b-34b5-48ec-94f5-7225a59c85a0"), event_id=3, version=1)
class Microsoft_Windows_RPC_Proxy_LBS_3_1(Etw):
    pattern = Struct(
        "UserName" / WString,
        "ServerList" / WString
    )


@declare(guid=guid("272a979b-34b5-48ec-94f5-7225a59c85a0"), event_id=4, version=1)
class Microsoft_Windows_RPC_Proxy_LBS_4_1(Etw):
    pattern = Struct(
        "ServerName" / WString
    )


@declare(guid=guid("272a979b-34b5-48ec-94f5-7225a59c85a0"), event_id=5, version=1)
class Microsoft_Windows_RPC_Proxy_LBS_5_1(Etw):
    pattern = Struct(
        "ServerName" / WString
    )

