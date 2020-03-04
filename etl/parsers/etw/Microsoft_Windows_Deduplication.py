# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Deduplication
GUID : f9fe3908-44b8-48d9-9a32-5a763ff5ed79
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4096, version=0)
class Microsoft_Windows_Deduplication_4096_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4097, version=0)
class Microsoft_Windows_Deduplication_4097_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Param4" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4098, version=0)
class Microsoft_Windows_Deduplication_4098_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Param4" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4099, version=0)
class Microsoft_Windows_Deduplication_4099_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Param4" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4100, version=0)
class Microsoft_Windows_Deduplication_4100_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Param4" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4101, version=0)
class Microsoft_Windows_Deduplication_4101_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4102, version=0)
class Microsoft_Windows_Deduplication_4102_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4103, version=0)
class Microsoft_Windows_Deduplication_4103_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4104, version=0)
class Microsoft_Windows_Deduplication_4104_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4105, version=0)
class Microsoft_Windows_Deduplication_4105_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4106, version=0)
class Microsoft_Windows_Deduplication_4106_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4107, version=0)
class Microsoft_Windows_Deduplication_4107_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4108, version=0)
class Microsoft_Windows_Deduplication_4108_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4109, version=0)
class Microsoft_Windows_Deduplication_4109_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4110, version=0)
class Microsoft_Windows_Deduplication_4110_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4111, version=0)
class Microsoft_Windows_Deduplication_4111_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4112, version=0)
class Microsoft_Windows_Deduplication_4112_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4113, version=0)
class Microsoft_Windows_Deduplication_4113_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4114, version=0)
class Microsoft_Windows_Deduplication_4114_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Param4" / WString,
        "Param5" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4115, version=0)
class Microsoft_Windows_Deduplication_4115_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4118, version=0)
class Microsoft_Windows_Deduplication_4118_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4119, version=0)
class Microsoft_Windows_Deduplication_4119_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4120, version=0)
class Microsoft_Windows_Deduplication_4120_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4121, version=0)
class Microsoft_Windows_Deduplication_4121_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4122, version=0)
class Microsoft_Windows_Deduplication_4122_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4123, version=0)
class Microsoft_Windows_Deduplication_4123_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4124, version=0)
class Microsoft_Windows_Deduplication_4124_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4125, version=0)
class Microsoft_Windows_Deduplication_4125_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4126, version=0)
class Microsoft_Windows_Deduplication_4126_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4127, version=0)
class Microsoft_Windows_Deduplication_4127_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4128, version=0)
class Microsoft_Windows_Deduplication_4128_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4129, version=0)
class Microsoft_Windows_Deduplication_4129_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4130, version=0)
class Microsoft_Windows_Deduplication_4130_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4131, version=0)
class Microsoft_Windows_Deduplication_4131_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4132, version=0)
class Microsoft_Windows_Deduplication_4132_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4133, version=0)
class Microsoft_Windows_Deduplication_4133_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4134, version=0)
class Microsoft_Windows_Deduplication_4134_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4135, version=0)
class Microsoft_Windows_Deduplication_4135_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4136, version=0)
class Microsoft_Windows_Deduplication_4136_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4137, version=0)
class Microsoft_Windows_Deduplication_4137_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4140, version=0)
class Microsoft_Windows_Deduplication_4140_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4141, version=0)
class Microsoft_Windows_Deduplication_4141_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4142, version=0)
class Microsoft_Windows_Deduplication_4142_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4143, version=0)
class Microsoft_Windows_Deduplication_4143_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4144, version=0)
class Microsoft_Windows_Deduplication_4144_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4145, version=0)
class Microsoft_Windows_Deduplication_4145_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4146, version=0)
class Microsoft_Windows_Deduplication_4146_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4147, version=0)
class Microsoft_Windows_Deduplication_4147_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4148, version=0)
class Microsoft_Windows_Deduplication_4148_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4149, version=0)
class Microsoft_Windows_Deduplication_4149_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4150, version=0)
class Microsoft_Windows_Deduplication_4150_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4151, version=0)
class Microsoft_Windows_Deduplication_4151_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4153, version=0)
class Microsoft_Windows_Deduplication_4153_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4154, version=0)
class Microsoft_Windows_Deduplication_4154_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4155, version=0)
class Microsoft_Windows_Deduplication_4155_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4156, version=0)
class Microsoft_Windows_Deduplication_4156_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4157, version=0)
class Microsoft_Windows_Deduplication_4157_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4158, version=0)
class Microsoft_Windows_Deduplication_4158_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4159, version=0)
class Microsoft_Windows_Deduplication_4159_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4160, version=0)
class Microsoft_Windows_Deduplication_4160_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4161, version=0)
class Microsoft_Windows_Deduplication_4161_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4162, version=0)
class Microsoft_Windows_Deduplication_4162_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4163, version=0)
class Microsoft_Windows_Deduplication_4163_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4164, version=0)
class Microsoft_Windows_Deduplication_4164_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4165, version=0)
class Microsoft_Windows_Deduplication_4165_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4166, version=0)
class Microsoft_Windows_Deduplication_4166_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4169, version=0)
class Microsoft_Windows_Deduplication_4169_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4171, version=0)
class Microsoft_Windows_Deduplication_4171_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4173, version=0)
class Microsoft_Windows_Deduplication_4173_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4174, version=0)
class Microsoft_Windows_Deduplication_4174_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4175, version=0)
class Microsoft_Windows_Deduplication_4175_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4176, version=0)
class Microsoft_Windows_Deduplication_4176_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4177, version=0)
class Microsoft_Windows_Deduplication_4177_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4178, version=0)
class Microsoft_Windows_Deduplication_4178_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4179, version=0)
class Microsoft_Windows_Deduplication_4179_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4180, version=0)
class Microsoft_Windows_Deduplication_4180_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4181, version=0)
class Microsoft_Windows_Deduplication_4181_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4182, version=0)
class Microsoft_Windows_Deduplication_4182_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4183, version=0)
class Microsoft_Windows_Deduplication_4183_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4184, version=0)
class Microsoft_Windows_Deduplication_4184_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4185, version=0)
class Microsoft_Windows_Deduplication_4185_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4186, version=0)
class Microsoft_Windows_Deduplication_4186_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4189, version=0)
class Microsoft_Windows_Deduplication_4189_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4190, version=0)
class Microsoft_Windows_Deduplication_4190_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4191, version=0)
class Microsoft_Windows_Deduplication_4191_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4192, version=0)
class Microsoft_Windows_Deduplication_4192_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4193, version=0)
class Microsoft_Windows_Deduplication_4193_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4194, version=0)
class Microsoft_Windows_Deduplication_4194_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4195, version=0)
class Microsoft_Windows_Deduplication_4195_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4196, version=0)
class Microsoft_Windows_Deduplication_4196_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=4197, version=0)
class Microsoft_Windows_Deduplication_4197_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6144, version=0)
class Microsoft_Windows_Deduplication_6144_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "ParentDirectoryId" / Int64ul,
        "FileId" / Int64ul,
        "VolumeDisplayName" / WString,
        "ParentDirectoryPath" / WString,
        "FileName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6145, version=0)
class Microsoft_Windows_Deduplication_6145_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6146, version=0)
class Microsoft_Windows_Deduplication_6146_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "ErorrCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6147, version=0)
class Microsoft_Windows_Deduplication_6147_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "ErorrCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6148, version=0)
class Microsoft_Windows_Deduplication_6148_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "AvailableMemoryMB" / Int32ul,
        "AvailableCores" / Int32ul,
        "Instances" / Int32ul,
        "ReadersPerInstance" / Int32ul,
        "JobPriorityType" / Int32ul,
        "IoThrottle" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6149, version=0)
class Microsoft_Windows_Deduplication_6149_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "AvailableMemoryMB" / Int32ul,
        "AvailableCores" / Int32ul,
        "JobPriorityType" / Int32ul,
        "Full" / Int8ul,
        "VolumeFreeSpaceMB" / Int64ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6150, version=0)
class Microsoft_Windows_Deduplication_6150_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "AvailableMemoryMB" / Int32ul,
        "JobPriorityType" / Int32ul,
        "Full" / Int8ul,
        "ReadOnly" / Int8ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6151, version=0)
class Microsoft_Windows_Deduplication_6151_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "AvailableMemoryMB" / Int32ul,
        "JobPriorityType" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6152, version=0)
class Microsoft_Windows_Deduplication_6152_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "AvailableMemoryMB" / Int32ul,
        "JobPriorityType" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6153, version=0)
class Microsoft_Windows_Deduplication_6153_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString,
        "SavingsRate" / Int32ul,
        "SavedSpaceMB" / Int64ul,
        "VolumeUsedSpaceMB" / Int64ul,
        "VolumeFreeSpaceMB" / Int64ul,
        "OptimizedFileCount" / Int64ul,
        "InPolicyFileCount" / Int64ul,
        "JobProcessedSpaceMB" / Int64ul,
        "JobOptimizedBytesMB" / Int64ul,
        "JobChurnBytesMB" / Int64ul,
        "JobSkippedBytesMB" / Int64ul,
        "PriorityMode" / Int8ul,
        "JobElapsedTime" / Int32ul,
        "JobThroughput" / Float32l,
        "ChurnThroughput" / Float32l,
        "FinalJobStage" / Int32ul,
        "FileSystem" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6154, version=0)
class Microsoft_Windows_Deduplication_6154_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "Full" / Int8ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString,
        "FreedupSpaceMB" / Int64ul,
        "VolumeFreeSpaceMB" / Int64ul,
        "JobElapsedTime" / Int64ul,
        "JobThroughput" / Float32l,
        "CompactedDataContainerCount" / Int64ul,
        "CompactedStreamContainerCount" / Int64ul,
        "ReclaimedFileLeakCount" / Int64ul,
        "FileSystem" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6155, version=0)
class Microsoft_Windows_Deduplication_6155_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6156, version=0)
class Microsoft_Windows_Deduplication_6156_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "Full" / Int8ul,
        "ReadOnly" / Int8ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString,
        "TotalCorruptionCount" / Int64ul,
        "FixableCorruptionCount" / Int64ul,
        "FileSystem" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6157, version=0)
class Microsoft_Windows_Deduplication_6157_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString,
        "UnOptimizedFiles" / Int64ul,
        "ProcessedSizeMB" / Int64ul,
        "JobElapsedTime" / Int64ul,
        "JobThroughput" / Float32l,
        "SkippedFiles" / Int64ul,
        "FailedFiles" / Int64ul,
        "FileSystem" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6158, version=0)
class Microsoft_Windows_Deduplication_6158_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "SystemMemoryPercent" / Int32ul,
        "JobPriorityType" / Int32ul,
        "JobScheduleMode" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6159, version=0)
class Microsoft_Windows_Deduplication_6159_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "SystemMemoryPercent" / Int32ul,
        "JobPriorityType" / Int32ul,
        "JobScheduleMode" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6160, version=0)
class Microsoft_Windows_Deduplication_6160_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "SystemMemoryPercent" / Int32ul,
        "JobPriorityType" / Int32ul,
        "JobScheduleMode" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6170, version=0)
class Microsoft_Windows_Deduplication_6170_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "SystemMemoryPercent" / Int32ul,
        "JobPriorityType" / Int32ul,
        "JobScheduleMode" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6171, version=0)
class Microsoft_Windows_Deduplication_6171_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "SystemMemoryPercent" / Int32ul,
        "JobPriorityType" / Int32ul,
        "JobScheduleMode" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6172, version=0)
class Microsoft_Windows_Deduplication_6172_0(Etw):
    pattern = Struct(
        "FilePath" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6173, version=0)
class Microsoft_Windows_Deduplication_6173_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "AvailableMemoryMB" / Int32ul,
        "AvailableCores" / Int32ul,
        "Instances" / Int32ul,
        "ReadersPerInstance" / Int32ul,
        "JobPriorityType" / Int32ul,
        "IoThrottle" / Int32ul,
        "FileId" / Int64ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6174, version=0)
class Microsoft_Windows_Deduplication_6174_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "AvailableMemoryMb" / Int32ul,
        "AvailableThreads" / Int32ul,
        "JobPriorityType" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6175, version=0)
class Microsoft_Windows_Deduplication_6175_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString,
        "SavingsRate" / Int32ul,
        "SavedSpaceMb" / Int64ul,
        "VolumeUsedSpaceMb" / Int64ul,
        "VolumeFreeSpaceMb" / Int64ul,
        "OptimizedFileCount" / Int64ul,
        "ChunkLookups" / Int64ul,
        "InsertedChunks" / Int64ul,
        "InsertedChunksLogicalMb" / Int64ul,
        "InsertedChunksPhysicalMb" / Int64ul,
        "CommittedStreamMaps" / Int64ul,
        "CommittedStreamMapEntries" / Int64ul,
        "CommittedStreamBytesLogicalMb" / Int64ul,
        "RetrievedChunkBytesPhysicalMb" / Int64ul,
        "RetrievedStreamBytesLogicalMb" / Int64ul,
        "DataPortTime" / Int32ul,
        "JobElapsedTime" / Int32ul,
        "IngressThroughput" / Float32l,
        "EgressThroughput" / Float32l,
        "FinalJobStage" / Int32ul,
        "FileSystem" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6176, version=0)
class Microsoft_Windows_Deduplication_6176_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "SystemMemoryPercent" / Int32ul,
        "JobPriorityType" / Int32ul,
        "JobScheduleMode" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6177, version=0)
class Microsoft_Windows_Deduplication_6177_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=6178, version=0)
class Microsoft_Windows_Deduplication_6178_0(Etw):
    pattern = Struct(
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "SavingsRate" / Int32ul,
        "SavedSpaceMb" / Int64ul,
        "VolumeUsedSpaceMb" / Int64ul,
        "VolumeFreeSpaceMb" / Int64ul,
        "OptimizedFileCount" / Int64ul,
        "ChunkLookups" / Int64ul,
        "InsertedChunks" / Int64ul,
        "InsertedChunksLogicalMb" / Int64ul,
        "InsertedChunksPhysicalMb" / Int64ul,
        "CommittedStreamMaps" / Int64ul,
        "CommittedStreamMapEntries" / Int64ul,
        "CommittedStreamBytesLogicalMb" / Int64ul,
        "RetrievedChunkBytesPhysicalMb" / Int64ul,
        "RetrievedStreamBytesLogicalMb" / Int64ul,
        "DataPortTime" / Int32ul,
        "JobElapsedTime" / Int32ul,
        "IngressThroughput" / Float32l,
        "EgressThroughput" / Float32l,
        "FileSystem" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8192, version=0)
class Microsoft_Windows_Deduplication_8192_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8193, version=0)
class Microsoft_Windows_Deduplication_8193_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8194, version=0)
class Microsoft_Windows_Deduplication_8194_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8195, version=0)
class Microsoft_Windows_Deduplication_8195_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8196, version=0)
class Microsoft_Windows_Deduplication_8196_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8197, version=0)
class Microsoft_Windows_Deduplication_8197_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8198, version=0)
class Microsoft_Windows_Deduplication_8198_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8199, version=0)
class Microsoft_Windows_Deduplication_8199_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8200, version=0)
class Microsoft_Windows_Deduplication_8200_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8201, version=0)
class Microsoft_Windows_Deduplication_8201_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8202, version=0)
class Microsoft_Windows_Deduplication_8202_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8203, version=0)
class Microsoft_Windows_Deduplication_8203_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8204, version=0)
class Microsoft_Windows_Deduplication_8204_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8205, version=0)
class Microsoft_Windows_Deduplication_8205_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8206, version=0)
class Microsoft_Windows_Deduplication_8206_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8207, version=0)
class Microsoft_Windows_Deduplication_8207_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8208, version=0)
class Microsoft_Windows_Deduplication_8208_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8209, version=0)
class Microsoft_Windows_Deduplication_8209_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8210, version=0)
class Microsoft_Windows_Deduplication_8210_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8211, version=0)
class Microsoft_Windows_Deduplication_8211_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8212, version=0)
class Microsoft_Windows_Deduplication_8212_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8213, version=0)
class Microsoft_Windows_Deduplication_8213_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Param4" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8214, version=0)
class Microsoft_Windows_Deduplication_8214_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Param4" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8215, version=0)
class Microsoft_Windows_Deduplication_8215_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Param4" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8216, version=0)
class Microsoft_Windows_Deduplication_8216_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Param4" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8217, version=0)
class Microsoft_Windows_Deduplication_8217_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8218, version=0)
class Microsoft_Windows_Deduplication_8218_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8219, version=0)
class Microsoft_Windows_Deduplication_8219_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8220, version=0)
class Microsoft_Windows_Deduplication_8220_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8221, version=0)
class Microsoft_Windows_Deduplication_8221_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8222, version=0)
class Microsoft_Windows_Deduplication_8222_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8223, version=0)
class Microsoft_Windows_Deduplication_8223_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8224, version=0)
class Microsoft_Windows_Deduplication_8224_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8225, version=0)
class Microsoft_Windows_Deduplication_8225_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8226, version=0)
class Microsoft_Windows_Deduplication_8226_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8227, version=0)
class Microsoft_Windows_Deduplication_8227_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8228, version=0)
class Microsoft_Windows_Deduplication_8228_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8230, version=0)
class Microsoft_Windows_Deduplication_8230_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Param4" / WString,
        "Param5" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8231, version=0)
class Microsoft_Windows_Deduplication_8231_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8232, version=0)
class Microsoft_Windows_Deduplication_8232_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8233, version=0)
class Microsoft_Windows_Deduplication_8233_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8234, version=0)
class Microsoft_Windows_Deduplication_8234_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8235, version=0)
class Microsoft_Windows_Deduplication_8235_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8236, version=0)
class Microsoft_Windows_Deduplication_8236_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8237, version=0)
class Microsoft_Windows_Deduplication_8237_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8238, version=0)
class Microsoft_Windows_Deduplication_8238_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8239, version=0)
class Microsoft_Windows_Deduplication_8239_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8240, version=0)
class Microsoft_Windows_Deduplication_8240_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8241, version=0)
class Microsoft_Windows_Deduplication_8241_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8242, version=0)
class Microsoft_Windows_Deduplication_8242_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8243, version=0)
class Microsoft_Windows_Deduplication_8243_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8244, version=0)
class Microsoft_Windows_Deduplication_8244_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8245, version=0)
class Microsoft_Windows_Deduplication_8245_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8246, version=0)
class Microsoft_Windows_Deduplication_8246_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8247, version=0)
class Microsoft_Windows_Deduplication_8247_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8248, version=0)
class Microsoft_Windows_Deduplication_8248_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8249, version=0)
class Microsoft_Windows_Deduplication_8249_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8250, version=0)
class Microsoft_Windows_Deduplication_8250_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8251, version=0)
class Microsoft_Windows_Deduplication_8251_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8252, version=0)
class Microsoft_Windows_Deduplication_8252_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8253, version=0)
class Microsoft_Windows_Deduplication_8253_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8254, version=0)
class Microsoft_Windows_Deduplication_8254_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8255, version=0)
class Microsoft_Windows_Deduplication_8255_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8256, version=0)
class Microsoft_Windows_Deduplication_8256_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8257, version=0)
class Microsoft_Windows_Deduplication_8257_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8258, version=0)
class Microsoft_Windows_Deduplication_8258_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8259, version=0)
class Microsoft_Windows_Deduplication_8259_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8260, version=0)
class Microsoft_Windows_Deduplication_8260_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=8261, version=0)
class Microsoft_Windows_Deduplication_8261_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=10240, version=0)
class Microsoft_Windows_Deduplication_10240_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "MinimumMemoryMB" / Int32ul,
        "MaximumMemoryMB" / Int32ul,
        "MinimumDiskMB" / Int32ul,
        "MaximumCores" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=10241, version=0)
class Microsoft_Windows_Deduplication_10241_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=10242, version=0)
class Microsoft_Windows_Deduplication_10242_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "ReconciledContainerCount" / Int32ul,
        "UnreconciledContainerCount" / Int32ul,
        "CatchUpReferences" / Int32ul,
        "CatchUpMergedContainerCount" / Int32ul,
        "ReconciledReferences" / Int32ul,
        "ReconciledMergedContainerCount" / Int32ul,
        "CrossReconciledReferences" / Int32ul,
        "CrossReconciledMergedContainerCount" / Int32ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString,
        "SkippedContainerCount" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=10243, version=0)
class Microsoft_Windows_Deduplication_10243_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "SystemMemoryPercent" / Int32ul,
        "MinimumMemoryMB" / Int32ul,
        "MaximumMemoryMB" / Int32ul,
        "AvailableMemoryMB" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=10244, version=0)
class Microsoft_Windows_Deduplication_10244_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "UnoptimizedBytes" / Int64ul,
        "MftCacheSizeMB" / Int64ul,
        "GrovelerLogBufferMB" / Int64ul,
        "DirectoryTableMB" / Int64ul,
        "DirectoryNamesMB" / Int64ul,
        "IndexMinEntries" / Int64ul,
        "IndexMaxEntries" / Int64ul,
        "IndexMinRequiredMB" / Int32ul,
        "IndexMaxRequiredMB" / Int32ul,
        "PipelineMinMB" / Int32ul,
        "PipelineMaxMB" / Int32ul,
        "ChunkStoreBatchBufferMemoryMB" / Int32ul,
        "ChunkStoreContainerListMB" / Int32ul,
        "CorruptionTableMemoryMB" / Int32ul,
        "HotspotRequiredMB" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=10245, version=0)
class Microsoft_Windows_Deduplication_10245_0(Etw):
    pattern = Struct(
        "SkipReason" / Int32ul,
        "FileId" / Int64ul,
        "FileOffset" / Int64ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=10246, version=0)
class Microsoft_Windows_Deduplication_10246_0(Etw):
    pattern = Struct(
        "Operation" / Int32ul,
        "NumberOfRetries" / Int32ul,
        "FileId" / Int64ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=10247, version=0)
class Microsoft_Windows_Deduplication_10247_0(Etw):
    pattern = Struct(
        "VolumeDisplayName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString,
        "Description" / WString,
        "SourceFile" / WString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=10248, version=0)
class Microsoft_Windows_Deduplication_10248_0(Etw):
    pattern = Struct(
        "FileId" / Int64ul,
        "FilePath" / WString,
        "FileSize" / Int64ul,
        "Flags" / Int32ul,
        "TotalRanges" / Int32ul,
        "SkippedRanges" / Int32ul,
        "AbortedRanges" / Int32ul,
        "CommittedRanges" / Int32ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString,
        "Description" / WString,
        "SourceFile" / WString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=10249, version=0)
class Microsoft_Windows_Deduplication_10249_0(Etw):
    pattern = Struct(
        "FileId" / Int64ul,
        "FilePath" / WString,
        "RangeOffset" / Int64ul,
        "RangeLength" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString,
        "Description" / WString,
        "SourceFile" / WString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=10250, version=0)
class Microsoft_Windows_Deduplication_10250_0(Etw):
    pattern = Struct(
        "MaxSize" / Int64ul,
        "CurrentSize" / Int64ul,
        "RemainingRanges" / Int32ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString,
        "Description" / WString,
        "SourceFile" / WString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=10251, version=0)
class Microsoft_Windows_Deduplication_10251_0(Etw):
    pattern = Struct(
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "MaximumSizeMB" / Int32ul,
        "AllocationSizeMB" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=10252, version=0)
class Microsoft_Windows_Deduplication_10252_0(Etw):
    pattern = Struct(
        "JobType" / Int32ul,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "UnoptimizedBytes" / Int64ul,
        "IndexMinEntries" / Int64ul,
        "IndexMaxEntries" / Int64ul,
        "IndexMinRequiredMb" / Int32ul,
        "IndexMaxRequiredMb" / Int32ul,
        "PipelineMinMb" / Int32ul,
        "PipelineMaxMb" / Int32ul,
        "ChunkStoreBatchBufferMemoryMb" / Int32ul,
        "ChunkStoreContainerListMb" / Int32ul,
        "CorruptionTableMemoryMb" / Int32ul,
        "HotspotRequiredMb" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=10253, version=0)
class Microsoft_Windows_Deduplication_10253_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "FileId" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=10254, version=0)
class Microsoft_Windows_Deduplication_10254_0(Etw):
    pattern = Struct(
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "ReconciliationMemoryPercentage" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=10255, version=0)
class Microsoft_Windows_Deduplication_10255_0(Etw):
    pattern = Struct(
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "ReconciliationMemoryPercentage" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12800, version=0)
class Microsoft_Windows_Deduplication_12800_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "ParentDirectoryId" / Int64ul,
        "FileId" / Int64ul,
        "VolumeDisplayName" / WString,
        "ParentDirectoryPath" / WString,
        "FileName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12801, version=0)
class Microsoft_Windows_Deduplication_12801_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "DetectionTime" / Int64ul,
        "VolumeGuidPath" / WString,
        "Fixed" / Int8ul,
        "FileId" / Int64ul,
        "FilePath" / WString,
        "CorruptionType" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12802, version=0)
class Microsoft_Windows_Deduplication_12802_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "DetectionTime" / Int64ul,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "Fixed" / Int8ul,
        "FileId" / Int64ul,
        "FilePath" / WString,
        "ContainerId" / Int32ul,
        "FileLocator" / Int32ul,
        "RecordLocator" / Int32ul,
        "CorruptionType" / Int32ul,
        "ItemType" / Int32ul,
        "ChunkStoreType" / Int32ul,
        "HasRedundantCopy" / Int8ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12803, version=0)
class Microsoft_Windows_Deduplication_12803_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "DetectedCorruptionCount" / Int32ul,
        "FixedCorruptionCount" / Int32ul,
        "CorruptedUserFileCount" / Int32ul,
        "FixedUserFileCount" / Int32ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString,
        "ReadOnlyMode" / Int8ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12804, version=0)
class Microsoft_Windows_Deduplication_12804_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "DetectedCorruptionCount" / Int32ul,
        "FixedCorruptionCount" / Int32ul,
        "CorruptedUserFileCount" / Int32ul,
        "FixedUserFileCount" / Int32ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString,
        "ReadOnlyMode" / Int8ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12805, version=0)
class Microsoft_Windows_Deduplication_12805_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "DetectedCorruptionCount" / Int32ul,
        "FixedCorruptionCount" / Int32ul,
        "CorruptedUserFileCount" / Int32ul,
        "FixedUserFileCount" / Int32ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString,
        "ReadOnlyMode" / Int8ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12806, version=0)
class Microsoft_Windows_Deduplication_12806_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12810, version=0)
class Microsoft_Windows_Deduplication_12810_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "DetectedCorruptionCount" / Int32ul,
        "FixableCorruptionCount" / Int32ul,
        "CorruptedUserFileCount" / Int32ul,
        "FixableUserFileCount" / Int32ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString,
        "ReadOnlyMode" / Int8ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12817, version=0)
class Microsoft_Windows_Deduplication_12817_0(Etw):
    pattern = Struct(
        "Full" / Int8ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "TotalChunkStoreCorruptedItemCount" / Int32ul,
        "DataChunkStoreCorruptedItemCount" / Int32ul,
        "DataChunkStoreCorruptedContainerCount" / Int32ul,
        "DataChunkStoreFixedItemCount" / Int32ul,
        "StreamMapChunkStoreCorruptedItemCount" / Int32ul,
        "StreamMapChunkStoreCorruptedContainerCount" / Int32ul,
        "StreamMapChunkStoreFixedItemCount" / Int32ul,
        "HotspotChunkStoreCorruptedItemCount" / Int32ul,
        "HotspotChunkStoreCorruptedContainerCount" / Int32ul,
        "HotspotChunkStoreFixedItemCount" / Int32ul,
        "CorruptedReparsePointCount" / Int32ul,
        "RecallBitmapCorruptedItemCount" / Int32ul,
        "RecallBitmapFixedItemCount" / Int32ul,
        "TotalCorruptedItemCount" / Int32ul,
        "CorruptedUserFileCount" / Int32ul,
        "FixedUserFileCount" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12818, version=0)
class Microsoft_Windows_Deduplication_12818_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "ParentDirectoryId" / Int64ul,
        "FileId" / Int64ul,
        "VolumeDisplayName" / WString,
        "ParentDirectoryPath" / WString,
        "FileName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12819, version=0)
class Microsoft_Windows_Deduplication_12819_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "Threshold" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12820, version=0)
class Microsoft_Windows_Deduplication_12820_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12822, version=0)
class Microsoft_Windows_Deduplication_12822_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12823, version=0)
class Microsoft_Windows_Deduplication_12823_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12824, version=0)
class Microsoft_Windows_Deduplication_12824_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12825, version=0)
class Microsoft_Windows_Deduplication_12825_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12826, version=0)
class Microsoft_Windows_Deduplication_12826_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "DetectedCorruptionCount" / Int32ul,
        "FixableCorruptionCount" / Int32ul,
        "CorruptedUserFileCount" / Int32ul,
        "FixableUserFileCount" / Int32ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString,
        "ReadOnlyMode" / Int8ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12827, version=0)
class Microsoft_Windows_Deduplication_12827_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "ParentDirectoryId" / Int64ul,
        "FileId" / Int64ul,
        "VolumeDisplayName" / WString,
        "ParentDirectoryPath" / WString,
        "FileName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12828, version=0)
class Microsoft_Windows_Deduplication_12828_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "ParentDirectoryId" / Int64ul,
        "FileId" / Int64ul,
        "VolumeDisplayName" / WString,
        "ParentDirectoryPath" / WString,
        "FileName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12829, version=0)
class Microsoft_Windows_Deduplication_12829_0(Etw):
    pattern = Struct(
        "Full" / Int8ul,
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "TotalChunkStoreCorruptedItemCount" / Int32ul,
        "DataChunkStoreCorruptedItemCount" / Int32ul,
        "DataChunkStoreCorruptedContainerCount" / Int32ul,
        "DataChunkStoreFixableItemCount" / Int32ul,
        "StreamMapChunkStoreCorruptedItemCount" / Int32ul,
        "StreamMapChunkStoreCorruptedContainerCount" / Int32ul,
        "StreamMapChunkStoreFixableItemCount" / Int32ul,
        "HotspotChunkStoreCorruptedItemCount" / Int32ul,
        "HotspotChunkStoreCorruptedContainerCount" / Int32ul,
        "HotspotChunkStoreFixableItemCount" / Int32ul,
        "CorruptedReparsePointCount" / Int32ul,
        "RecallBitmapCorruptedItemCount" / Int32ul,
        "RecallBitmapFixedItemCount" / Int32ul,
        "TotalCorruptedItemCount" / Int32ul,
        "CorruptedUserFileCount" / Int32ul,
        "FixableUserFileCount" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12830, version=0)
class Microsoft_Windows_Deduplication_12830_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12831, version=0)
class Microsoft_Windows_Deduplication_12831_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "DetectionTime" / Int64ul,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "Fixed" / Int8ul,
        "ContainerId" / Int32ul,
        "CorruptionType" / Int32ul,
        "ItemType" / Int32ul,
        "HasRedundantCopy" / Int8ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12832, version=0)
class Microsoft_Windows_Deduplication_12832_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "DetectionTime" / Int64ul,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "Fixed" / Int8ul,
        "FileId" / Int64ul,
        "FilePath" / WString,
        "ContainerId" / Int32ul,
        "FileLocator" / Int32ul,
        "RecordLocator" / Int32ul,
        "CorruptionType" / Int32ul,
        "ItemType" / Int32ul,
        "ChunkStoreType" / Int32ul,
        "HasRedundantCopy" / Int8ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12833, version=0)
class Microsoft_Windows_Deduplication_12833_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12834, version=0)
class Microsoft_Windows_Deduplication_12834_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "ParentDirectoryId" / Int64ul,
        "FileId" / Int64ul,
        "VolumeDisplayName" / WString,
        "ParentDirectoryPath" / WString,
        "FileName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12835, version=0)
class Microsoft_Windows_Deduplication_12835_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "Threshold" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12836, version=0)
class Microsoft_Windows_Deduplication_12836_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "DetectionTime" / Int64ul,
        "VolumeGuidPath" / WString,
        "Fixed" / Int8ul,
        "FileId" / Int64ul,
        "FilePath" / WString,
        "TargetFileId" / Int64ul,
        "TargetFilePath" / WString,
        "CorruptionType" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=12837, version=0)
class Microsoft_Windows_Deduplication_12837_0(Etw):
    pattern = Struct(
        "JobInstanceId" / Guid,
        "DetectionTime" / Int64ul,
        "VolumeGuidPath" / WString,
        "VolumeDisplayName" / WString,
        "Fixed" / Int8ul,
        "FileId" / Int64ul,
        "FilePath" / WString,
        "ContainerId" / Int32ul,
        "FileLocator" / Int32ul,
        "RecordLocator" / Int32ul,
        "CorruptionType" / Int32ul,
        "ItemType" / Int32ul,
        "ChunkStoreType" / Int32ul,
        "HasRedundantCopy" / Int8ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20480, version=0)
class Microsoft_Windows_Deduplication_20480_0(Etw):
    pattern = Struct(
        "FileId" / Int64ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20481, version=0)
class Microsoft_Windows_Deduplication_20481_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20482, version=0)
class Microsoft_Windows_Deduplication_20482_0(Etw):
    pattern = Struct(
        "Stream" / Int64ul,
        "FileId" / Int64ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20483, version=0)
class Microsoft_Windows_Deduplication_20483_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20484, version=1)
class Microsoft_Windows_Deduplication_20484_1(Etw):
    pattern = Struct(
        "Stream" / Int64ul,
        "FileId" / Int64ul,
        "StartIndex" / Int32ul,
        "EntryCount" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20485, version=0)
class Microsoft_Windows_Deduplication_20485_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20486, version=0)
class Microsoft_Windows_Deduplication_20486_0(Etw):
    pattern = Struct(
        "Stream" / Int64ul,
        "FileId" / Int64ul,
        "IoType" / Int32ul,
        "NextRequest" / Int64ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20487, version=0)
class Microsoft_Windows_Deduplication_20487_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20488, version=0)
class Microsoft_Windows_Deduplication_20488_0(Etw):
    pattern = Struct(
        "ItemType" / Int32ul,
        "DataSize" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20489, version=0)
class Microsoft_Windows_Deduplication_20489_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20490, version=0)
class Microsoft_Windows_Deduplication_20490_0(Etw):
    pattern = Struct(
        "ContainerId" / Int32ul,
        "Generation" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20491, version=0)
class Microsoft_Windows_Deduplication_20491_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20492, version=0)
class Microsoft_Windows_Deduplication_20492_0(Etw):
    pattern = Struct(
        "ContainerId" / Int32ul,
        "Generation" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20493, version=0)
class Microsoft_Windows_Deduplication_20493_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20494, version=0)
class Microsoft_Windows_Deduplication_20494_0(Etw):
    pattern = Struct(
        "ContainerId" / Int32ul,
        "Generation" / Int32ul,
        "RootPathLength" / Int16ul,
        "RootPath" / Bytes(lambda this: this.RootPathLength)
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20495, version=0)
class Microsoft_Windows_Deduplication_20495_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20496, version=0)
class Microsoft_Windows_Deduplication_20496_0(Etw):
    pattern = Struct(
        "ContainerId" / Int32ul,
        "Generation" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20497, version=0)
class Microsoft_Windows_Deduplication_20497_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20498, version=0)
class Microsoft_Windows_Deduplication_20498_0(Etw):
    pattern = Struct(
        "ContainerId" / Int32ul,
        "Generation" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20499, version=0)
class Microsoft_Windows_Deduplication_20499_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20500, version=0)
class Microsoft_Windows_Deduplication_20500_0(Etw):
    pattern = Struct(
        "ContainerId" / Int32ul,
        "Generation" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20501, version=0)
class Microsoft_Windows_Deduplication_20501_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20502, version=0)
class Microsoft_Windows_Deduplication_20502_0(Etw):
    pattern = Struct(
        "ContainerId" / Int32ul,
        "Generation" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20503, version=0)
class Microsoft_Windows_Deduplication_20503_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20504, version=0)
class Microsoft_Windows_Deduplication_20504_0(Etw):
    pattern = Struct(
        "ContainerId" / Int32ul,
        "Generation" / Int32ul,
        "Buffer" / Int64ul,
        "Offset" / Int32ul,
        "Length" / Int32ul,
        "IoType" / Int32ul,
        "Synchronous" / Int8ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20505, version=0)
class Microsoft_Windows_Deduplication_20505_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20506, version=0)
class Microsoft_Windows_Deduplication_20506_0(Etw):
    pattern = Struct(
        "Block" / Int64ul,
        "Size" / Int32ul,
        "BufferType" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20507, version=0)
class Microsoft_Windows_Deduplication_20507_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20508, version=0)
class Microsoft_Windows_Deduplication_20508_0(Etw):
    pattern = Struct(
        "Block" / Int64ul,
        "Size" / Int32ul,
        "BufferType" / Int32ul,
        "BufferOffset" / Int32ul,
        "OutputCapacity" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20509, version=0)
class Microsoft_Windows_Deduplication_20509_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20510, version=0)
class Microsoft_Windows_Deduplication_20510_0(Etw):
    pattern = Struct(
        "UnderlyingFileObject" / Int64ul,
        "CacheFileSize" / Int64ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20511, version=0)
class Microsoft_Windows_Deduplication_20511_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20512, version=0)
class Microsoft_Windows_Deduplication_20512_0(Etw):
    pattern = Struct(
        "CacheFileObject" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20513, version=0)
class Microsoft_Windows_Deduplication_20513_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20514, version=0)
class Microsoft_Windows_Deduplication_20514_0(Etw):
    pattern = Struct(
        "Bcb" / Int64ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20515, version=0)
class Microsoft_Windows_Deduplication_20515_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20516, version=0)
class Microsoft_Windows_Deduplication_20516_0(Etw):
    pattern = Struct(
        "CacheFileObject" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20517, version=0)
class Microsoft_Windows_Deduplication_20517_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20518, version=0)
class Microsoft_Windows_Deduplication_20518_0(Etw):
    pattern = Struct(
        "CacheFileObject" / Int64ul,
        "UnderlyingFileObject" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20519, version=0)
class Microsoft_Windows_Deduplication_20519_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20520, version=0)
class Microsoft_Windows_Deduplication_20520_0(Etw):
    pattern = Struct(
        "ContainerId" / Int32ul,
        "Generation" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20521, version=0)
class Microsoft_Windows_Deduplication_20521_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20522, version=0)
class Microsoft_Windows_Deduplication_20522_0(Etw):
    pattern = Struct(
        "Stream" / Int64ul,
        "FileId" / Int64ul,
        "StartIndex" / Int32ul,
        "EntryCount" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20523, version=0)
class Microsoft_Windows_Deduplication_20523_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20524, version=0)
class Microsoft_Windows_Deduplication_20524_0(Etw):
    pattern = Struct(
        "ContainerId" / Int32ul,
        "Generation" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20525, version=0)
class Microsoft_Windows_Deduplication_20525_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20526, version=0)
class Microsoft_Windows_Deduplication_20526_0(Etw):
    pattern = Struct(
        "ContainerId" / Int32ul,
        "Generation" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20527, version=0)
class Microsoft_Windows_Deduplication_20527_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20528, version=0)
class Microsoft_Windows_Deduplication_20528_0(Etw):
    pattern = Struct(
        "ReadLength" / Int32ul,
        "PagingIo" / Int8ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20529, version=0)
class Microsoft_Windows_Deduplication_20529_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20530, version=0)
class Microsoft_Windows_Deduplication_20530_0(Etw):
    pattern = Struct(
        "ContainerId" / Int32ul,
        "Generation" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20531, version=0)
class Microsoft_Windows_Deduplication_20531_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20532, version=0)
class Microsoft_Windows_Deduplication_20532_0(Etw):
    pattern = Struct(
        "ContainerId" / Int32ul,
        "Generation" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=20533, version=0)
class Microsoft_Windows_Deduplication_20533_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24616, version=0)
class Microsoft_Windows_Deduplication_24616_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul,
        "IoType" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24617, version=0)
class Microsoft_Windows_Deduplication_24617_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24618, version=0)
class Microsoft_Windows_Deduplication_24618_0(Etw):
    pattern = Struct(
        "TlCache" / Int64ul,
        "Stream" / Int64ul,
        "RequestStartOffset" / Int64ul,
        "RequestEndOffset" / Int64ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24619, version=0)
class Microsoft_Windows_Deduplication_24619_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24620, version=0)
class Microsoft_Windows_Deduplication_24620_0(Etw):
    pattern = Struct(
        "Stream" / Int64ul,
        "CurrentOffset" / Int64ul,
        "AdjFinalOffset" / Int64ul,
        "FirstChunkByteOffset" / Int64ul,
        "ChunkRequestsEndOffset" / Int64ul,
        "TlCache" / Int64ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24621, version=0)
class Microsoft_Windows_Deduplication_24621_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24622, version=0)
class Microsoft_Windows_Deduplication_24622_0(Etw):
    pattern = Struct(
        "TlCache" / Int64ul,
        "Stream" / Int64ul,
        "StreamMapEntryCount" / Int32ul,
        "RequestStartOffset" / Int64ul,
        "RequestEndOffset" / Int64ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24623, version=0)
class Microsoft_Windows_Deduplication_24623_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24624, version=0)
class Microsoft_Windows_Deduplication_24624_0(Etw):
    pattern = Struct(
        "TlCache" / Int64ul,
        "Stream" / Int64ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24625, version=0)
class Microsoft_Windows_Deduplication_24625_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24626, version=0)
class Microsoft_Windows_Deduplication_24626_0(Etw):
    pattern = Struct(
        "Stream" / Int64ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24627, version=0)
class Microsoft_Windows_Deduplication_24627_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24629, version=0)
class Microsoft_Windows_Deduplication_24629_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24631, version=0)
class Microsoft_Windows_Deduplication_24631_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24632, version=0)
class Microsoft_Windows_Deduplication_24632_0(Etw):
    pattern = Struct(
        "BytesCopied" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24633, version=0)
class Microsoft_Windows_Deduplication_24633_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24635, version=0)
class Microsoft_Windows_Deduplication_24635_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24636, version=0)
class Microsoft_Windows_Deduplication_24636_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24637, version=0)
class Microsoft_Windows_Deduplication_24637_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24638, version=0)
class Microsoft_Windows_Deduplication_24638_0(Etw):
    pattern = Struct(
        "StreamContext" / Int64ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24639, version=0)
class Microsoft_Windows_Deduplication_24639_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24640, version=0)
class Microsoft_Windows_Deduplication_24640_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24641, version=0)
class Microsoft_Windows_Deduplication_24641_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24642, version=0)
class Microsoft_Windows_Deduplication_24642_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul,
        "IoType" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24643, version=0)
class Microsoft_Windows_Deduplication_24643_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24644, version=0)
class Microsoft_Windows_Deduplication_24644_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24645, version=0)
class Microsoft_Windows_Deduplication_24645_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24646, version=0)
class Microsoft_Windows_Deduplication_24646_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24647, version=0)
class Microsoft_Windows_Deduplication_24647_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24648, version=0)
class Microsoft_Windows_Deduplication_24648_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24649, version=0)
class Microsoft_Windows_Deduplication_24649_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24650, version=0)
class Microsoft_Windows_Deduplication_24650_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24651, version=0)
class Microsoft_Windows_Deduplication_24651_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24652, version=0)
class Microsoft_Windows_Deduplication_24652_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24653, version=0)
class Microsoft_Windows_Deduplication_24653_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24654, version=0)
class Microsoft_Windows_Deduplication_24654_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24655, version=0)
class Microsoft_Windows_Deduplication_24655_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24656, version=0)
class Microsoft_Windows_Deduplication_24656_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24657, version=0)
class Microsoft_Windows_Deduplication_24657_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24658, version=0)
class Microsoft_Windows_Deduplication_24658_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24659, version=0)
class Microsoft_Windows_Deduplication_24659_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24660, version=0)
class Microsoft_Windows_Deduplication_24660_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24661, version=0)
class Microsoft_Windows_Deduplication_24661_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24662, version=0)
class Microsoft_Windows_Deduplication_24662_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24663, version=0)
class Microsoft_Windows_Deduplication_24663_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24664, version=0)
class Microsoft_Windows_Deduplication_24664_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24665, version=0)
class Microsoft_Windows_Deduplication_24665_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24666, version=0)
class Microsoft_Windows_Deduplication_24666_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24667, version=0)
class Microsoft_Windows_Deduplication_24667_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24668, version=0)
class Microsoft_Windows_Deduplication_24668_0(Etw):
    pattern = Struct(
        "FilePath" / WString
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24669, version=0)
class Microsoft_Windows_Deduplication_24669_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24671, version=0)
class Microsoft_Windows_Deduplication_24671_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24673, version=0)
class Microsoft_Windows_Deduplication_24673_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24674, version=0)
class Microsoft_Windows_Deduplication_24674_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24675, version=0)
class Microsoft_Windows_Deduplication_24675_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24676, version=0)
class Microsoft_Windows_Deduplication_24676_0(Etw):
    pattern = Struct(
        "Offset" / Int64ul,
        "Length" / Int64ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24677, version=0)
class Microsoft_Windows_Deduplication_24677_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24679, version=0)
class Microsoft_Windows_Deduplication_24679_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24681, version=0)
class Microsoft_Windows_Deduplication_24681_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24682, version=0)
class Microsoft_Windows_Deduplication_24682_0(Etw):
    pattern = Struct(
        "BufferSize" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24683, version=0)
class Microsoft_Windows_Deduplication_24683_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24684, version=0)
class Microsoft_Windows_Deduplication_24684_0(Etw):
    pattern = Struct(
        "BufferSize" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24685, version=0)
class Microsoft_Windows_Deduplication_24685_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24686, version=0)
class Microsoft_Windows_Deduplication_24686_0(Etw):
    pattern = Struct(
        "BufferSize" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24687, version=0)
class Microsoft_Windows_Deduplication_24687_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24689, version=0)
class Microsoft_Windows_Deduplication_24689_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24690, version=0)
class Microsoft_Windows_Deduplication_24690_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("f9fe3908-44b8-48d9-9a32-5a763ff5ed79"), event_id=24691, version=0)
class Microsoft_Windows_Deduplication_24691_0(Etw):
    pattern = Struct(
        "CompletionStatus" / Int32ul
    )

