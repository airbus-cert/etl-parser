# -*- coding: utf-8 -*-
"""
Microsoft-Windows-BackgroundTransfer-ContentPrefetcher
GUID : 648a0644-7d62-4fd3-8841-440064762f95
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("648a0644-7d62-4fd3-8841-440064762f95"), event_id=0, version=0)
class Microsoft_Windows_BackgroundTransfer_ContentPrefetcher_0_0(Etw):
    pattern = Struct(
        "appName" / WString
    )


@declare(guid=guid("648a0644-7d62-4fd3-8841-440064762f95"), event_id=1, version=0)
class Microsoft_Windows_BackgroundTransfer_ContentPrefetcher_1_0(Etw):
    pattern = Struct(
        "appName" / WString
    )


@declare(guid=guid("648a0644-7d62-4fd3-8841-440064762f95"), event_id=2, version=0)
class Microsoft_Windows_BackgroundTransfer_ContentPrefetcher_2_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("648a0644-7d62-4fd3-8841-440064762f95"), event_id=3, version=0)
class Microsoft_Windows_BackgroundTransfer_ContentPrefetcher_3_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("648a0644-7d62-4fd3-8841-440064762f95"), event_id=4, version=0)
class Microsoft_Windows_BackgroundTransfer_ContentPrefetcher_4_0(Etw):
    pattern = Struct(
        "uri" / WString,
        "httpStatusCode" / Int32ul,
        "errorString" / WString
    )


@declare(guid=guid("648a0644-7d62-4fd3-8841-440064762f95"), event_id=6, version=0)
class Microsoft_Windows_BackgroundTransfer_ContentPrefetcher_6_0(Etw):
    pattern = Struct(
        "uri" / WString,
        "statusCode" / Int32ul,
        "errorString" / WString
    )


@declare(guid=guid("648a0644-7d62-4fd3-8841-440064762f95"), event_id=7, version=0)
class Microsoft_Windows_BackgroundTransfer_ContentPrefetcher_7_0(Etw):
    pattern = Struct(
        "uri" / WString,
        "errorString" / CString
    )


@declare(guid=guid("648a0644-7d62-4fd3-8841-440064762f95"), event_id=8, version=0)
class Microsoft_Windows_BackgroundTransfer_ContentPrefetcher_8_0(Etw):
    pattern = Struct(
        "uri" / WString,
        "xmlBlob" / CString
    )


@declare(guid=guid("648a0644-7d62-4fd3-8841-440064762f95"), event_id=9, version=0)
class Microsoft_Windows_BackgroundTransfer_ContentPrefetcher_9_0(Etw):
    pattern = Struct(
        "statusCode" / Int32ul,
        "errorReason" / WString,
        "sourceText" / WString,
        "errorOffset" / Int32ul
    )


@declare(guid=guid("648a0644-7d62-4fd3-8841-440064762f95"), event_id=10, version=0)
class Microsoft_Windows_BackgroundTransfer_ContentPrefetcher_10_0(Etw):
    pattern = Struct(
        "count" / Int32ul
    )


@declare(guid=guid("648a0644-7d62-4fd3-8841-440064762f95"), event_id=11, version=0)
class Microsoft_Windows_BackgroundTransfer_ContentPrefetcher_11_0(Etw):
    pattern = Struct(
        "uri" / WString
    )


@declare(guid=guid("648a0644-7d62-4fd3-8841-440064762f95"), event_id=12, version=0)
class Microsoft_Windows_BackgroundTransfer_ContentPrefetcher_12_0(Etw):
    pattern = Struct(
        "appName" / WString,
        "httpStatusCode" / Int32ul,
        "errorString" / WString
    )


@declare(guid=guid("648a0644-7d62-4fd3-8841-440064762f95"), event_id=13, version=0)
class Microsoft_Windows_BackgroundTransfer_ContentPrefetcher_13_0(Etw):
    pattern = Struct(
        "appName" / WString,
        "errorString" / CString
    )


@declare(guid=guid("648a0644-7d62-4fd3-8841-440064762f95"), event_id=14, version=0)
class Microsoft_Windows_BackgroundTransfer_ContentPrefetcher_14_0(Etw):
    pattern = Struct(
        "appName" / WString
    )


@declare(guid=guid("648a0644-7d62-4fd3-8841-440064762f95"), event_id=15, version=0)
class Microsoft_Windows_BackgroundTransfer_ContentPrefetcher_15_0(Etw):
    pattern = Struct(
        "appName" / WString,
        "errorString" / Int32ul
    )


@declare(guid=guid("648a0644-7d62-4fd3-8841-440064762f95"), event_id=16, version=0)
class Microsoft_Windows_BackgroundTransfer_ContentPrefetcher_16_0(Etw):
    pattern = Struct(
        "uri" / WString,
        "statusCode" / Int32ul
    )


@declare(guid=guid("648a0644-7d62-4fd3-8841-440064762f95"), event_id=17, version=0)
class Microsoft_Windows_BackgroundTransfer_ContentPrefetcher_17_0(Etw):
    pattern = Struct(
        "count" / Int32ul
    )


@declare(guid=guid("648a0644-7d62-4fd3-8841-440064762f95"), event_id=18, version=0)
class Microsoft_Windows_BackgroundTransfer_ContentPrefetcher_18_0(Etw):
    pattern = Struct(
        "uri" / WString
    )

