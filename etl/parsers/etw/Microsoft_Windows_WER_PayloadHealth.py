# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WER-PayloadHealth
GUID : 4afddfde-002d-51ac-c109-c3b7897858d0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4afddfde-002d-51ac-c109-c3b7897858d0"), event_id=1, version=0)
class Microsoft_Windows_WER_PayloadHealth_1_0(Etw):
    pattern = Struct(
        "UploadDuration" / Int32ul,
        "PayloadSize" / Int64ul,
        "Protocol" / WString,
        "Stage" / WString,
        "BytesUploaded" / Int64ul,
        "ServerName" / WString
    )


@declare(guid=guid("4afddfde-002d-51ac-c109-c3b7897858d0"), event_id=2, version=0)
class Microsoft_Windows_WER_PayloadHealth_2_0(Etw):
    pattern = Struct(
        "HttpExchangeResult" / Int32ul,
        "UploadDuration" / Int32ul,
        "PayloadSize" / Int64ul,
        "Protocol" / WString,
        "Stage" / WString,
        "RequestStatusCode" / Int32ul,
        "BytesUploaded" / Int64ul,
        "ServerName" / WString,
        "TransportHr" / Int32ul
    )


@declare(guid=guid("4afddfde-002d-51ac-c109-c3b7897858d0"), event_id=3, version=0)
class Microsoft_Windows_WER_PayloadHealth_3_0(Etw):
    pattern = Struct(
        "HttpExchangeResult" / Int32ul,
        "LastBlockId" / Int32ul,
        "TotalBytesUploaded" / Int64ul
    )


@declare(guid=guid("4afddfde-002d-51ac-c109-c3b7897858d0"), event_id=4, version=0)
class Microsoft_Windows_WER_PayloadHealth_4_0(Etw):
    pattern = Struct(
        "HttpExchangeResult" / Int32ul,
        "LastBlockId" / Int32ul,
        "TotalBytesUploaded" / Int64ul
    )

