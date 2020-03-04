# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Forwarding
GUID : 699e309c-e782-4400-98c8-e21d162d7b7b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("699e309c-e782-4400-98c8-e21d162d7b7b"), event_id=100, version=0)
class Microsoft_Windows_Forwarding_100_0(Etw):
    pattern = Struct(
        "Id" / WString,
        "Query" / WString
    )


@declare(guid=guid("699e309c-e782-4400-98c8-e21d162d7b7b"), event_id=101, version=0)
class Microsoft_Windows_Forwarding_101_0(Etw):
    pattern = Struct(
        "Id" / WString,
        "Query" / WString,
        "Status" / WString
    )


@declare(guid=guid("699e309c-e782-4400-98c8-e21d162d7b7b"), event_id=102, version=0)
class Microsoft_Windows_Forwarding_102_0(Etw):
    pattern = Struct(
        "Query" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("699e309c-e782-4400-98c8-e21d162d7b7b"), event_id=102, version=1)
class Microsoft_Windows_Forwarding_102_1(Etw):
    pattern = Struct(
        "Id" / WString,
        "Query" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("699e309c-e782-4400-98c8-e21d162d7b7b"), event_id=103, version=0)
class Microsoft_Windows_Forwarding_103_0(Etw):
    pattern = Struct(
        "Id" / WString
    )


@declare(guid=guid("699e309c-e782-4400-98c8-e21d162d7b7b"), event_id=104, version=0)
class Microsoft_Windows_Forwarding_104_0(Etw):
    pattern = Struct(
        "Id" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("699e309c-e782-4400-98c8-e21d162d7b7b"), event_id=104, version=1)
class Microsoft_Windows_Forwarding_104_1(Etw):
    pattern = Struct(
        "SubscriptionManagerAddress" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("699e309c-e782-4400-98c8-e21d162d7b7b"), event_id=105, version=0)
class Microsoft_Windows_Forwarding_105_0(Etw):
    pattern = Struct(
        "SubscriptionManagerAddress" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("699e309c-e782-4400-98c8-e21d162d7b7b"), event_id=107, version=0)
class Microsoft_Windows_Forwarding_107_0(Etw):
    pattern = Struct(
        "PolicyDescription" / WString
    )

