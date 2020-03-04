# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Websocket-Protocol-Component
GUID : cba5f63c-e2cf-4b36-8305-bde1311924fc
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("cba5f63c-e2cf-4b36-8305-bde1311924fc"), event_id=1, version=0)
class Microsoft_Windows_Websocket_Protocol_Component_1_0(Etw):
    pattern = Struct(
        "TraceMessage" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("cba5f63c-e2cf-4b36-8305-bde1311924fc"), event_id=2, version=0)
class Microsoft_Windows_Websocket_Protocol_Component_2_0(Etw):
    pattern = Struct(
        "Id" / Int32ul,
        "OperationType" / Int32ul
    )


@declare(guid=guid("cba5f63c-e2cf-4b36-8305-bde1311924fc"), event_id=3, version=0)
class Microsoft_Windows_Websocket_Protocol_Component_3_0(Etw):
    pattern = Struct(
        "Id" / Int32ul,
        "ActionType" / Int32ul
    )


@declare(guid=guid("cba5f63c-e2cf-4b36-8305-bde1311924fc"), event_id=4, version=0)
class Microsoft_Windows_Websocket_Protocol_Component_4_0(Etw):
    pattern = Struct(
        "Id" / Int32ul
    )

