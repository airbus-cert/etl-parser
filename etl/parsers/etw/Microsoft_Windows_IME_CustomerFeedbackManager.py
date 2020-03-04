# -*- coding: utf-8 -*-
"""
Microsoft-Windows-IME-CustomerFeedbackManager
GUID : e2242b38-9453-42fd-b446-00746e76eb82
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e2242b38-9453-42fd-b446-00746e76eb82"), event_id=1, version=0)
class Microsoft_Windows_IME_CustomerFeedbackManager_1_0(Etw):
    pattern = Struct(
        "Msg" / WString
    )


@declare(guid=guid("e2242b38-9453-42fd-b446-00746e76eb82"), event_id=11, version=0)
class Microsoft_Windows_IME_CustomerFeedbackManager_11_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "ThreadID" / Int32ul
    )


@declare(guid=guid("e2242b38-9453-42fd-b446-00746e76eb82"), event_id=14, version=0)
class Microsoft_Windows_IME_CustomerFeedbackManager_14_0(Etw):
    pattern = Struct(
        "path" / WString
    )


@declare(guid=guid("e2242b38-9453-42fd-b446-00746e76eb82"), event_id=15, version=0)
class Microsoft_Windows_IME_CustomerFeedbackManager_15_0(Etw):
    pattern = Struct(
        "pattern" / WString,
        "result" / WString
    )


@declare(guid=guid("e2242b38-9453-42fd-b446-00746e76eb82"), event_id=16, version=0)
class Microsoft_Windows_IME_CustomerFeedbackManager_16_0(Etw):
    pattern = Struct(
        "pattern" / WString,
        "result" / WString
    )


@declare(guid=guid("e2242b38-9453-42fd-b446-00746e76eb82"), event_id=17, version=0)
class Microsoft_Windows_IME_CustomerFeedbackManager_17_0(Etw):
    pattern = Struct(
        "path" / WString
    )


@declare(guid=guid("e2242b38-9453-42fd-b446-00746e76eb82"), event_id=18, version=0)
class Microsoft_Windows_IME_CustomerFeedbackManager_18_0(Etw):
    pattern = Struct(
        "GLE" / Int32ul
    )

