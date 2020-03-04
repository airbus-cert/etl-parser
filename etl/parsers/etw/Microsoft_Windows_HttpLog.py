# -*- coding: utf-8 -*-
"""
Microsoft-Windows-HttpLog
GUID : c42a2738-2333-40a5-a32f-6acc36449dcc
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c42a2738-2333-40a5-a32f-6acc36449dcc"), event_id=1, version=0)
class Microsoft_Windows_HttpLog_1_0(Etw):
    pattern = Struct(
        "ServerSessionId" / Int64ul,
        "UrlGroupId" / Int64ul,
        "UrlContext" / Int64ul,
        "DateTime" / Int64ul,
        "RemoteAddrLength" / Int32ul,
        "RemoteAddr" / Bytes(lambda this: this.RemoteAddrLength),
        "LocalAddrLength" / Int32ul,
        "LocalAddr" / Bytes(lambda this: this.LocalAddrLength),
        "KernelCached" / Int32ul,
        "HttpMajorVer" / Int16ul,
        "HttpMinorVer" / Int16ul,
        "BytesSent" / Int64ul,
        "BytesReceived" / Int64ul,
        "TimeTaken" / Int64ul,
        "UserName" / WString,
        "Method" / CString,
        "UriStem" / WString,
        "UriQuery" / CString,
        "ProtocolStatus" / Int16ul,
        "ProtocolSubStatus" / Int16ul,
        "Win32Status" / Int32ul,
        "Host" / CString,
        "UserAgent" / CString,
        "Cookie" / CString,
        "Referer" / CString,
        "AppContext" / CString
    )

