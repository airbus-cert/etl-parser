# -*- coding: utf-8 -*-
"""
Microsoft-Windows-AsynchronousCausality
GUID : 19a4c69a-28eb-4d4b-8d94-5f19055a1b5c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=4112, version=1)
class Microsoft_Windows_AsynchronousCausality_4112_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "OperationName" / WString,
        "RelatedId" / Int64ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=4113, version=1)
class Microsoft_Windows_AsynchronousCausality_4113_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "OperationName" / WString,
        "RelatedId" / Int64ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=4114, version=1)
class Microsoft_Windows_AsynchronousCausality_4114_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "OperationName" / WString,
        "RelatedId" / Int64ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=4144, version=1)
class Microsoft_Windows_AsynchronousCausality_4144_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "OperationName" / WString,
        "RelatedId" / Int64ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=4145, version=1)
class Microsoft_Windows_AsynchronousCausality_4145_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "OperationName" / WString,
        "RelatedId" / Int64ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=4146, version=1)
class Microsoft_Windows_AsynchronousCausality_4146_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "OperationName" / WString,
        "RelatedId" / Int64ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=4176, version=1)
class Microsoft_Windows_AsynchronousCausality_4176_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "OperationName" / WString,
        "RelatedId" / Int64ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=4177, version=1)
class Microsoft_Windows_AsynchronousCausality_4177_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "OperationName" / WString,
        "RelatedId" / Int64ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=4178, version=1)
class Microsoft_Windows_AsynchronousCausality_4178_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "OperationName" / WString,
        "RelatedId" / Int64ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=8208, version=1)
class Microsoft_Windows_AsynchronousCausality_8208_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "CompletionStatus" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=8209, version=1)
class Microsoft_Windows_AsynchronousCausality_8209_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "CompletionStatus" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=8210, version=1)
class Microsoft_Windows_AsynchronousCausality_8210_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "CompletionStatus" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=8240, version=1)
class Microsoft_Windows_AsynchronousCausality_8240_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "CompletionStatus" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=8241, version=1)
class Microsoft_Windows_AsynchronousCausality_8241_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "CompletionStatus" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=8242, version=1)
class Microsoft_Windows_AsynchronousCausality_8242_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "CompletionStatus" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=8272, version=1)
class Microsoft_Windows_AsynchronousCausality_8272_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "CompletionStatus" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=8273, version=1)
class Microsoft_Windows_AsynchronousCausality_8273_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "CompletionStatus" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=8274, version=1)
class Microsoft_Windows_AsynchronousCausality_8274_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "CompletionStatus" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=12304, version=1)
class Microsoft_Windows_AsynchronousCausality_12304_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "Relation" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=12305, version=1)
class Microsoft_Windows_AsynchronousCausality_12305_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "Relation" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=12306, version=1)
class Microsoft_Windows_AsynchronousCausality_12306_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "Relation" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=12336, version=1)
class Microsoft_Windows_AsynchronousCausality_12336_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "Relation" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=12337, version=1)
class Microsoft_Windows_AsynchronousCausality_12337_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "Relation" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=12338, version=1)
class Microsoft_Windows_AsynchronousCausality_12338_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "Relation" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=12368, version=1)
class Microsoft_Windows_AsynchronousCausality_12368_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "Relation" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=12369, version=1)
class Microsoft_Windows_AsynchronousCausality_12369_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "Relation" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=12370, version=1)
class Microsoft_Windows_AsynchronousCausality_12370_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "Relation" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=16400, version=1)
class Microsoft_Windows_AsynchronousCausality_16400_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "WorkItemType" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=16401, version=1)
class Microsoft_Windows_AsynchronousCausality_16401_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "WorkItemType" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=16402, version=1)
class Microsoft_Windows_AsynchronousCausality_16402_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "WorkItemType" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=16432, version=1)
class Microsoft_Windows_AsynchronousCausality_16432_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "WorkItemType" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=16433, version=1)
class Microsoft_Windows_AsynchronousCausality_16433_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "WorkItemType" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=16434, version=1)
class Microsoft_Windows_AsynchronousCausality_16434_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "WorkItemType" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=16464, version=1)
class Microsoft_Windows_AsynchronousCausality_16464_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "WorkItemType" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=16465, version=1)
class Microsoft_Windows_AsynchronousCausality_16465_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "WorkItemType" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=16466, version=1)
class Microsoft_Windows_AsynchronousCausality_16466_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "WorkItemType" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=16656, version=1)
class Microsoft_Windows_AsynchronousCausality_16656_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "WorkItemType" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=16657, version=1)
class Microsoft_Windows_AsynchronousCausality_16657_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "WorkItemType" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=16658, version=1)
class Microsoft_Windows_AsynchronousCausality_16658_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "WorkItemType" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=16688, version=1)
class Microsoft_Windows_AsynchronousCausality_16688_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "WorkItemType" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=16689, version=1)
class Microsoft_Windows_AsynchronousCausality_16689_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "WorkItemType" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=16690, version=1)
class Microsoft_Windows_AsynchronousCausality_16690_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "WorkItemType" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=16720, version=1)
class Microsoft_Windows_AsynchronousCausality_16720_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "WorkItemType" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=16721, version=1)
class Microsoft_Windows_AsynchronousCausality_16721_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "WorkItemType" / Int8ul
    )


@declare(guid=guid("19a4c69a-28eb-4d4b-8d94-5f19055a1b5c"), event_id=16722, version=1)
class Microsoft_Windows_AsynchronousCausality_16722_1(Etw):
    pattern = Struct(
        "PlatformId" / Guid,
        "OperationId" / Int64ul,
        "WorkItemType" / Int8ul
    )

