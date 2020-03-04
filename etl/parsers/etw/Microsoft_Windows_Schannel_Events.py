# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Schannel-Events
GUID : 91cc1150-71aa-47e2-ae18-c96e61736b6f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("91cc1150-71aa-47e2-ae18-c96e61736b6f"), event_id=258, version=0)
class Microsoft_Windows_Schannel_Events_258_0(Etw):
    pattern = Struct(
        "ReturnValue" / Int32ul
    )


@declare(guid=guid("91cc1150-71aa-47e2-ae18-c96e61736b6f"), event_id=513, version=0)
class Microsoft_Windows_Schannel_Events_513_0(Etw):
    pattern = Struct(
        "CredHandle" / Int64ul,
        "ContextHandle" / Int64ul
    )


@declare(guid=guid("91cc1150-71aa-47e2-ae18-c96e61736b6f"), event_id=514, version=0)
class Microsoft_Windows_Schannel_Events_514_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "ReturnValue" / Int32ul
    )


@declare(guid=guid("91cc1150-71aa-47e2-ae18-c96e61736b6f"), event_id=769, version=0)
class Microsoft_Windows_Schannel_Events_769_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "AllocationSize" / Int32ul
    )


@declare(guid=guid("91cc1150-71aa-47e2-ae18-c96e61736b6f"), event_id=770, version=0)
class Microsoft_Windows_Schannel_Events_770_0(Etw):
    pattern = Struct(
        "Address" / Int64ul
    )


@declare(guid=guid("91cc1150-71aa-47e2-ae18-c96e61736b6f"), event_id=1537, version=0)
class Microsoft_Windows_Schannel_Events_1537_0(Etw):
    pattern = Struct(
        "CredHandle" / Int64ul
    )


@declare(guid=guid("91cc1150-71aa-47e2-ae18-c96e61736b6f"), event_id=1793, version=0)
class Microsoft_Windows_Schannel_Events_1793_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "TargetName" / WString
    )

