# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Resource-Exhaustion-Resolver
GUID : 91f5fb12-fdea-4095-85d5-614b495cd9de
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("91f5fb12-fdea-4095-85d5-614b495cd9de"), event_id=1003, version=0)
class Microsoft_Windows_Resource_Exhaustion_Resolver_1003_0(Etw):
    pattern = Struct(
        "TimeSinceLastUI" / Int32ul,
        "EventGenerationTime" / Int64ul,
        "EventType" / Int32ul,
        "DropReasonCode" / Int32ul,
        "TimesUIShown" / Int8ul,
        "MaxCommit" / Int8ul
    )


@declare(guid=guid("91f5fb12-fdea-4095-85d5-614b495cd9de"), event_id=1004, version=0)
class Microsoft_Windows_Resource_Exhaustion_Resolver_1004_0(Etw):
    pattern = Struct(
        "Process_1_Name" / WString,
        "Process_1_ID" / Int32ul,
        "Process_1_CreationTime" / Int64ul,
        "Process_1_Version" / WString,
        "Process_2_Name" / WString,
        "Process_2_ID" / Int32ul,
        "Process_2_CreationTime" / Int64ul,
        "Process_2_Version" / WString,
        "Process_3_Name" / WString,
        "Process_3_ID" / Int32ul,
        "Process_3_CreationTime" / Int64ul,
        "Process_3_Version" / WString,
        "ResolverID" / Int32ul,
        "EventGenerationTime" / Int64ul
    )


@declare(guid=guid("91f5fb12-fdea-4095-85d5-614b495cd9de"), event_id=1005, version=0)
class Microsoft_Windows_Resource_Exhaustion_Resolver_1005_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("91f5fb12-fdea-4095-85d5-614b495cd9de"), event_id=1006, version=0)
class Microsoft_Windows_Resource_Exhaustion_Resolver_1006_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("91f5fb12-fdea-4095-85d5-614b495cd9de"), event_id=1007, version=0)
class Microsoft_Windows_Resource_Exhaustion_Resolver_1007_0(Etw):
    pattern = Struct(
        "RequestSize" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("91f5fb12-fdea-4095-85d5-614b495cd9de"), event_id=1008, version=0)
class Microsoft_Windows_Resource_Exhaustion_Resolver_1008_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("91f5fb12-fdea-4095-85d5-614b495cd9de"), event_id=1009, version=0)
class Microsoft_Windows_Resource_Exhaustion_Resolver_1009_0(Etw):
    pattern = Struct(
        "UIDisplayTime" / Int32ul,
        "UserAction" / Int32sl,
        "MaxCommit" / Int8ul
    )


@declare(guid=guid("91f5fb12-fdea-4095-85d5-614b495cd9de"), event_id=1010, version=0)
class Microsoft_Windows_Resource_Exhaustion_Resolver_1010_0(Etw):
    pattern = Struct(
        "ReasonCode" / Int32ul,
        "UserAction" / Int32sl,
        "MaxCommit" / Int8ul
    )


@declare(guid=guid("91f5fb12-fdea-4095-85d5-614b495cd9de"), event_id=1011, version=0)
class Microsoft_Windows_Resource_Exhaustion_Resolver_1011_0(Etw):
    pattern = Struct(
        "ReasonCode" / Int32ul,
        "UserAction" / Int32sl,
        "MaxCommit" / Int8ul
    )


@declare(guid=guid("91f5fb12-fdea-4095-85d5-614b495cd9de"), event_id=1012, version=0)
class Microsoft_Windows_Resource_Exhaustion_Resolver_1012_0(Etw):
    pattern = Struct(
        "TimesUIShown" / Int8ul,
        "UserAction" / Int32sl
    )


@declare(guid=guid("91f5fb12-fdea-4095-85d5-614b495cd9de"), event_id=1013, version=0)
class Microsoft_Windows_Resource_Exhaustion_Resolver_1013_0(Etw):
    pattern = Struct(
        "TimesUIShown" / Int8ul,
        "UserAction" / Int32sl
    )


@declare(guid=guid("91f5fb12-fdea-4095-85d5-614b495cd9de"), event_id=1014, version=0)
class Microsoft_Windows_Resource_Exhaustion_Resolver_1014_0(Etw):
    pattern = Struct(
        "ProcessImageName" / WString,
        "PID" / Int32ul,
        "CreationTime" / Int64ul,
        "DropReasonCode" / Int32ul
    )


@declare(guid=guid("91f5fb12-fdea-4095-85d5-614b495cd9de"), event_id=1015, version=0)
class Microsoft_Windows_Resource_Exhaustion_Resolver_1015_0(Etw):
    pattern = Struct(
        "Event" / Int32ul
    )


@declare(guid=guid("91f5fb12-fdea-4095-85d5-614b495cd9de"), event_id=1016, version=0)
class Microsoft_Windows_Resource_Exhaustion_Resolver_1016_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ResolutionAttempted" / Int8ul
    )


@declare(guid=guid("91f5fb12-fdea-4095-85d5-614b495cd9de"), event_id=1017, version=0)
class Microsoft_Windows_Resource_Exhaustion_Resolver_1017_0(Etw):
    pattern = Struct(
        "UIDisplayTime" / Int32ul,
        "UserAction" / Int32sl,
        "MaxCommit" / Int8ul
    )

