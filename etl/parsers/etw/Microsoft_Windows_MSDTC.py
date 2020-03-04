# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MSDTC
GUID : 719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4097, version=0)
class Microsoft_Windows_MSDTC_4097_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4098, version=0)
class Microsoft_Windows_MSDTC_4098_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4099, version=0)
class Microsoft_Windows_MSDTC_4099_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4100, version=0)
class Microsoft_Windows_MSDTC_4100_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4101, version=0)
class Microsoft_Windows_MSDTC_4101_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4102, version=0)
class Microsoft_Windows_MSDTC_4102_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4103, version=0)
class Microsoft_Windows_MSDTC_4103_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4104, version=0)
class Microsoft_Windows_MSDTC_4104_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4105, version=0)
class Microsoft_Windows_MSDTC_4105_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4106, version=0)
class Microsoft_Windows_MSDTC_4106_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4107, version=0)
class Microsoft_Windows_MSDTC_4107_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4108, version=0)
class Microsoft_Windows_MSDTC_4108_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4109, version=0)
class Microsoft_Windows_MSDTC_4109_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4110, version=0)
class Microsoft_Windows_MSDTC_4110_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4111, version=0)
class Microsoft_Windows_MSDTC_4111_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4112, version=0)
class Microsoft_Windows_MSDTC_4112_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4113, version=0)
class Microsoft_Windows_MSDTC_4113_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4114, version=0)
class Microsoft_Windows_MSDTC_4114_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4115, version=0)
class Microsoft_Windows_MSDTC_4115_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4116, version=0)
class Microsoft_Windows_MSDTC_4116_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4117, version=0)
class Microsoft_Windows_MSDTC_4117_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4118, version=0)
class Microsoft_Windows_MSDTC_4118_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4119, version=0)
class Microsoft_Windows_MSDTC_4119_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4120, version=0)
class Microsoft_Windows_MSDTC_4120_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4121, version=0)
class Microsoft_Windows_MSDTC_4121_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4122, version=0)
class Microsoft_Windows_MSDTC_4122_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4123, version=0)
class Microsoft_Windows_MSDTC_4123_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4124, version=0)
class Microsoft_Windows_MSDTC_4124_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4125, version=0)
class Microsoft_Windows_MSDTC_4125_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4126, version=0)
class Microsoft_Windows_MSDTC_4126_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4127, version=0)
class Microsoft_Windows_MSDTC_4127_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4128, version=0)
class Microsoft_Windows_MSDTC_4128_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4129, version=0)
class Microsoft_Windows_MSDTC_4129_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4130, version=0)
class Microsoft_Windows_MSDTC_4130_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4131, version=0)
class Microsoft_Windows_MSDTC_4131_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4132, version=0)
class Microsoft_Windows_MSDTC_4132_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4133, version=0)
class Microsoft_Windows_MSDTC_4133_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4134, version=0)
class Microsoft_Windows_MSDTC_4134_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4135, version=0)
class Microsoft_Windows_MSDTC_4135_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4136, version=0)
class Microsoft_Windows_MSDTC_4136_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4137, version=0)
class Microsoft_Windows_MSDTC_4137_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4138, version=0)
class Microsoft_Windows_MSDTC_4138_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4139, version=0)
class Microsoft_Windows_MSDTC_4139_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4140, version=0)
class Microsoft_Windows_MSDTC_4140_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4141, version=0)
class Microsoft_Windows_MSDTC_4141_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4142, version=0)
class Microsoft_Windows_MSDTC_4142_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4143, version=0)
class Microsoft_Windows_MSDTC_4143_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4144, version=0)
class Microsoft_Windows_MSDTC_4144_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4145, version=0)
class Microsoft_Windows_MSDTC_4145_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4146, version=0)
class Microsoft_Windows_MSDTC_4146_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4147, version=0)
class Microsoft_Windows_MSDTC_4147_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4148, version=0)
class Microsoft_Windows_MSDTC_4148_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4149, version=0)
class Microsoft_Windows_MSDTC_4149_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4150, version=0)
class Microsoft_Windows_MSDTC_4150_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4151, version=0)
class Microsoft_Windows_MSDTC_4151_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4152, version=0)
class Microsoft_Windows_MSDTC_4152_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4153, version=0)
class Microsoft_Windows_MSDTC_4153_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4154, version=0)
class Microsoft_Windows_MSDTC_4154_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4155, version=0)
class Microsoft_Windows_MSDTC_4155_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4156, version=0)
class Microsoft_Windows_MSDTC_4156_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4157, version=0)
class Microsoft_Windows_MSDTC_4157_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4158, version=0)
class Microsoft_Windows_MSDTC_4158_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4159, version=0)
class Microsoft_Windows_MSDTC_4159_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4160, version=0)
class Microsoft_Windows_MSDTC_4160_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4161, version=0)
class Microsoft_Windows_MSDTC_4161_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4162, version=0)
class Microsoft_Windows_MSDTC_4162_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4163, version=0)
class Microsoft_Windows_MSDTC_4163_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4164, version=0)
class Microsoft_Windows_MSDTC_4164_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4165, version=0)
class Microsoft_Windows_MSDTC_4165_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4166, version=0)
class Microsoft_Windows_MSDTC_4166_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4167, version=0)
class Microsoft_Windows_MSDTC_4167_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4168, version=0)
class Microsoft_Windows_MSDTC_4168_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4169, version=0)
class Microsoft_Windows_MSDTC_4169_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4170, version=0)
class Microsoft_Windows_MSDTC_4170_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4171, version=0)
class Microsoft_Windows_MSDTC_4171_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4172, version=0)
class Microsoft_Windows_MSDTC_4172_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4173, version=0)
class Microsoft_Windows_MSDTC_4173_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4174, version=0)
class Microsoft_Windows_MSDTC_4174_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4175, version=0)
class Microsoft_Windows_MSDTC_4175_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4176, version=0)
class Microsoft_Windows_MSDTC_4176_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4177, version=0)
class Microsoft_Windows_MSDTC_4177_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4178, version=0)
class Microsoft_Windows_MSDTC_4178_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4179, version=0)
class Microsoft_Windows_MSDTC_4179_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4180, version=0)
class Microsoft_Windows_MSDTC_4180_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4181, version=0)
class Microsoft_Windows_MSDTC_4181_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4182, version=0)
class Microsoft_Windows_MSDTC_4182_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4183, version=0)
class Microsoft_Windows_MSDTC_4183_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4184, version=0)
class Microsoft_Windows_MSDTC_4184_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4185, version=0)
class Microsoft_Windows_MSDTC_4185_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4186, version=0)
class Microsoft_Windows_MSDTC_4186_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4187, version=0)
class Microsoft_Windows_MSDTC_4187_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4188, version=0)
class Microsoft_Windows_MSDTC_4188_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4189, version=0)
class Microsoft_Windows_MSDTC_4189_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4190, version=0)
class Microsoft_Windows_MSDTC_4190_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4191, version=0)
class Microsoft_Windows_MSDTC_4191_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4192, version=0)
class Microsoft_Windows_MSDTC_4192_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4193, version=0)
class Microsoft_Windows_MSDTC_4193_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4194, version=0)
class Microsoft_Windows_MSDTC_4194_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4195, version=0)
class Microsoft_Windows_MSDTC_4195_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4196, version=0)
class Microsoft_Windows_MSDTC_4196_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4197, version=0)
class Microsoft_Windows_MSDTC_4197_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4198, version=0)
class Microsoft_Windows_MSDTC_4198_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4199, version=0)
class Microsoft_Windows_MSDTC_4199_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4200, version=0)
class Microsoft_Windows_MSDTC_4200_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4201, version=0)
class Microsoft_Windows_MSDTC_4201_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4208, version=0)
class Microsoft_Windows_MSDTC_4208_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4209, version=0)
class Microsoft_Windows_MSDTC_4209_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4210, version=0)
class Microsoft_Windows_MSDTC_4210_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4211, version=0)
class Microsoft_Windows_MSDTC_4211_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4212, version=0)
class Microsoft_Windows_MSDTC_4212_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4213, version=0)
class Microsoft_Windows_MSDTC_4213_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4214, version=0)
class Microsoft_Windows_MSDTC_4214_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4215, version=0)
class Microsoft_Windows_MSDTC_4215_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4216, version=0)
class Microsoft_Windows_MSDTC_4216_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4217, version=0)
class Microsoft_Windows_MSDTC_4217_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4224, version=0)
class Microsoft_Windows_MSDTC_4224_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4225, version=0)
class Microsoft_Windows_MSDTC_4225_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4226, version=0)
class Microsoft_Windows_MSDTC_4226_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4227, version=0)
class Microsoft_Windows_MSDTC_4227_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4228, version=0)
class Microsoft_Windows_MSDTC_4228_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4229, version=0)
class Microsoft_Windows_MSDTC_4229_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4230, version=0)
class Microsoft_Windows_MSDTC_4230_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4231, version=0)
class Microsoft_Windows_MSDTC_4231_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4232, version=0)
class Microsoft_Windows_MSDTC_4232_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4233, version=0)
class Microsoft_Windows_MSDTC_4233_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4240, version=0)
class Microsoft_Windows_MSDTC_4240_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4241, version=0)
class Microsoft_Windows_MSDTC_4241_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4242, version=0)
class Microsoft_Windows_MSDTC_4242_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4243, version=0)
class Microsoft_Windows_MSDTC_4243_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4244, version=0)
class Microsoft_Windows_MSDTC_4244_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4245, version=0)
class Microsoft_Windows_MSDTC_4245_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4246, version=0)
class Microsoft_Windows_MSDTC_4246_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4247, version=0)
class Microsoft_Windows_MSDTC_4247_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4248, version=0)
class Microsoft_Windows_MSDTC_4248_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4249, version=0)
class Microsoft_Windows_MSDTC_4249_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4352, version=0)
class Microsoft_Windows_MSDTC_4352_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4353, version=0)
class Microsoft_Windows_MSDTC_4353_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4354, version=0)
class Microsoft_Windows_MSDTC_4354_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4355, version=0)
class Microsoft_Windows_MSDTC_4355_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4356, version=0)
class Microsoft_Windows_MSDTC_4356_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4357, version=0)
class Microsoft_Windows_MSDTC_4357_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4358, version=0)
class Microsoft_Windows_MSDTC_4358_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4359, version=0)
class Microsoft_Windows_MSDTC_4359_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4360, version=0)
class Microsoft_Windows_MSDTC_4360_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4361, version=0)
class Microsoft_Windows_MSDTC_4361_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4362, version=0)
class Microsoft_Windows_MSDTC_4362_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4363, version=0)
class Microsoft_Windows_MSDTC_4363_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4367, version=0)
class Microsoft_Windows_MSDTC_4367_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4368, version=0)
class Microsoft_Windows_MSDTC_4368_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4370, version=0)
class Microsoft_Windows_MSDTC_4370_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4371, version=0)
class Microsoft_Windows_MSDTC_4371_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4372, version=0)
class Microsoft_Windows_MSDTC_4372_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4373, version=0)
class Microsoft_Windows_MSDTC_4373_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4374, version=0)
class Microsoft_Windows_MSDTC_4374_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4375, version=0)
class Microsoft_Windows_MSDTC_4375_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4376, version=0)
class Microsoft_Windows_MSDTC_4376_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4377, version=0)
class Microsoft_Windows_MSDTC_4377_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4378, version=0)
class Microsoft_Windows_MSDTC_4378_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4379, version=0)
class Microsoft_Windows_MSDTC_4379_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4380, version=0)
class Microsoft_Windows_MSDTC_4380_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4381, version=0)
class Microsoft_Windows_MSDTC_4381_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4382, version=0)
class Microsoft_Windows_MSDTC_4382_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4383, version=0)
class Microsoft_Windows_MSDTC_4383_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4384, version=0)
class Microsoft_Windows_MSDTC_4384_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4385, version=0)
class Microsoft_Windows_MSDTC_4385_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4386, version=0)
class Microsoft_Windows_MSDTC_4386_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4387, version=0)
class Microsoft_Windows_MSDTC_4387_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4388, version=0)
class Microsoft_Windows_MSDTC_4388_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4389, version=0)
class Microsoft_Windows_MSDTC_4389_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4390, version=0)
class Microsoft_Windows_MSDTC_4390_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4391, version=0)
class Microsoft_Windows_MSDTC_4391_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4392, version=0)
class Microsoft_Windows_MSDTC_4392_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4393, version=0)
class Microsoft_Windows_MSDTC_4393_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4394, version=0)
class Microsoft_Windows_MSDTC_4394_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4395, version=0)
class Microsoft_Windows_MSDTC_4395_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4396, version=0)
class Microsoft_Windows_MSDTC_4396_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4397, version=0)
class Microsoft_Windows_MSDTC_4397_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4398, version=0)
class Microsoft_Windows_MSDTC_4398_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4399, version=0)
class Microsoft_Windows_MSDTC_4399_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4400, version=0)
class Microsoft_Windows_MSDTC_4400_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4401, version=0)
class Microsoft_Windows_MSDTC_4401_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4402, version=0)
class Microsoft_Windows_MSDTC_4402_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4403, version=0)
class Microsoft_Windows_MSDTC_4403_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4404, version=0)
class Microsoft_Windows_MSDTC_4404_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4405, version=0)
class Microsoft_Windows_MSDTC_4405_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4406, version=0)
class Microsoft_Windows_MSDTC_4406_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4407, version=0)
class Microsoft_Windows_MSDTC_4407_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4408, version=0)
class Microsoft_Windows_MSDTC_4408_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4409, version=0)
class Microsoft_Windows_MSDTC_4409_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4410, version=0)
class Microsoft_Windows_MSDTC_4410_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4411, version=0)
class Microsoft_Windows_MSDTC_4411_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4412, version=0)
class Microsoft_Windows_MSDTC_4412_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4413, version=0)
class Microsoft_Windows_MSDTC_4413_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4414, version=0)
class Microsoft_Windows_MSDTC_4414_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4415, version=0)
class Microsoft_Windows_MSDTC_4415_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4416, version=0)
class Microsoft_Windows_MSDTC_4416_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4417, version=0)
class Microsoft_Windows_MSDTC_4417_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4418, version=0)
class Microsoft_Windows_MSDTC_4418_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4419, version=0)
class Microsoft_Windows_MSDTC_4419_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4420, version=0)
class Microsoft_Windows_MSDTC_4420_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4421, version=0)
class Microsoft_Windows_MSDTC_4421_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4422, version=0)
class Microsoft_Windows_MSDTC_4422_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4424, version=0)
class Microsoft_Windows_MSDTC_4424_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4425, version=0)
class Microsoft_Windows_MSDTC_4425_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4426, version=0)
class Microsoft_Windows_MSDTC_4426_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4427, version=0)
class Microsoft_Windows_MSDTC_4427_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4428, version=0)
class Microsoft_Windows_MSDTC_4428_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4429, version=0)
class Microsoft_Windows_MSDTC_4429_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4431, version=0)
class Microsoft_Windows_MSDTC_4431_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4432, version=0)
class Microsoft_Windows_MSDTC_4432_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4433, version=0)
class Microsoft_Windows_MSDTC_4433_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4434, version=0)
class Microsoft_Windows_MSDTC_4434_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4435, version=0)
class Microsoft_Windows_MSDTC_4435_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4436, version=0)
class Microsoft_Windows_MSDTC_4436_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4437, version=0)
class Microsoft_Windows_MSDTC_4437_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4438, version=0)
class Microsoft_Windows_MSDTC_4438_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4439, version=0)
class Microsoft_Windows_MSDTC_4439_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4440, version=0)
class Microsoft_Windows_MSDTC_4440_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4441, version=0)
class Microsoft_Windows_MSDTC_4441_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4442, version=0)
class Microsoft_Windows_MSDTC_4442_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4443, version=0)
class Microsoft_Windows_MSDTC_4443_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4444, version=0)
class Microsoft_Windows_MSDTC_4444_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4445, version=0)
class Microsoft_Windows_MSDTC_4445_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4446, version=0)
class Microsoft_Windows_MSDTC_4446_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4447, version=0)
class Microsoft_Windows_MSDTC_4447_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4448, version=0)
class Microsoft_Windows_MSDTC_4448_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4449, version=0)
class Microsoft_Windows_MSDTC_4449_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4452, version=0)
class Microsoft_Windows_MSDTC_4452_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4453, version=0)
class Microsoft_Windows_MSDTC_4453_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4454, version=0)
class Microsoft_Windows_MSDTC_4454_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4455, version=0)
class Microsoft_Windows_MSDTC_4455_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4456, version=0)
class Microsoft_Windows_MSDTC_4456_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4457, version=0)
class Microsoft_Windows_MSDTC_4457_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4458, version=0)
class Microsoft_Windows_MSDTC_4458_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4459, version=0)
class Microsoft_Windows_MSDTC_4459_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4460, version=0)
class Microsoft_Windows_MSDTC_4460_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=4461, version=0)
class Microsoft_Windows_MSDTC_4461_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53248, version=0)
class Microsoft_Windows_MSDTC_53248_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53249, version=0)
class Microsoft_Windows_MSDTC_53249_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53250, version=0)
class Microsoft_Windows_MSDTC_53250_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53251, version=0)
class Microsoft_Windows_MSDTC_53251_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53252, version=0)
class Microsoft_Windows_MSDTC_53252_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53253, version=0)
class Microsoft_Windows_MSDTC_53253_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53254, version=0)
class Microsoft_Windows_MSDTC_53254_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53255, version=0)
class Microsoft_Windows_MSDTC_53255_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53256, version=0)
class Microsoft_Windows_MSDTC_53256_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53257, version=0)
class Microsoft_Windows_MSDTC_53257_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53258, version=0)
class Microsoft_Windows_MSDTC_53258_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53259, version=0)
class Microsoft_Windows_MSDTC_53259_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53260, version=0)
class Microsoft_Windows_MSDTC_53260_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53261, version=0)
class Microsoft_Windows_MSDTC_53261_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53262, version=0)
class Microsoft_Windows_MSDTC_53262_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53263, version=0)
class Microsoft_Windows_MSDTC_53263_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53264, version=0)
class Microsoft_Windows_MSDTC_53264_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53265, version=0)
class Microsoft_Windows_MSDTC_53265_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53266, version=0)
class Microsoft_Windows_MSDTC_53266_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53267, version=0)
class Microsoft_Windows_MSDTC_53267_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53268, version=0)
class Microsoft_Windows_MSDTC_53268_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53269, version=0)
class Microsoft_Windows_MSDTC_53269_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53270, version=0)
class Microsoft_Windows_MSDTC_53270_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53271, version=0)
class Microsoft_Windows_MSDTC_53271_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53272, version=0)
class Microsoft_Windows_MSDTC_53272_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53273, version=0)
class Microsoft_Windows_MSDTC_53273_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53274, version=0)
class Microsoft_Windows_MSDTC_53274_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53275, version=0)
class Microsoft_Windows_MSDTC_53275_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53276, version=0)
class Microsoft_Windows_MSDTC_53276_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53277, version=0)
class Microsoft_Windows_MSDTC_53277_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53278, version=0)
class Microsoft_Windows_MSDTC_53278_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53279, version=0)
class Microsoft_Windows_MSDTC_53279_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53280, version=0)
class Microsoft_Windows_MSDTC_53280_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53281, version=0)
class Microsoft_Windows_MSDTC_53281_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53282, version=0)
class Microsoft_Windows_MSDTC_53282_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53283, version=0)
class Microsoft_Windows_MSDTC_53283_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53284, version=0)
class Microsoft_Windows_MSDTC_53284_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53285, version=0)
class Microsoft_Windows_MSDTC_53285_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53286, version=0)
class Microsoft_Windows_MSDTC_53286_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53287, version=0)
class Microsoft_Windows_MSDTC_53287_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53288, version=0)
class Microsoft_Windows_MSDTC_53288_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53290, version=0)
class Microsoft_Windows_MSDTC_53290_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53291, version=0)
class Microsoft_Windows_MSDTC_53291_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53294, version=0)
class Microsoft_Windows_MSDTC_53294_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53295, version=0)
class Microsoft_Windows_MSDTC_53295_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53296, version=0)
class Microsoft_Windows_MSDTC_53296_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53297, version=0)
class Microsoft_Windows_MSDTC_53297_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53298, version=0)
class Microsoft_Windows_MSDTC_53298_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53299, version=0)
class Microsoft_Windows_MSDTC_53299_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53300, version=0)
class Microsoft_Windows_MSDTC_53300_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53301, version=0)
class Microsoft_Windows_MSDTC_53301_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53302, version=0)
class Microsoft_Windows_MSDTC_53302_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53303, version=0)
class Microsoft_Windows_MSDTC_53303_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53304, version=0)
class Microsoft_Windows_MSDTC_53304_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53305, version=0)
class Microsoft_Windows_MSDTC_53305_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53312, version=0)
class Microsoft_Windows_MSDTC_53312_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53315, version=0)
class Microsoft_Windows_MSDTC_53315_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53316, version=0)
class Microsoft_Windows_MSDTC_53316_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53317, version=0)
class Microsoft_Windows_MSDTC_53317_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53318, version=0)
class Microsoft_Windows_MSDTC_53318_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53319, version=0)
class Microsoft_Windows_MSDTC_53319_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53320, version=0)
class Microsoft_Windows_MSDTC_53320_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53321, version=0)
class Microsoft_Windows_MSDTC_53321_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53322, version=0)
class Microsoft_Windows_MSDTC_53322_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53323, version=0)
class Microsoft_Windows_MSDTC_53323_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53324, version=0)
class Microsoft_Windows_MSDTC_53324_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53325, version=0)
class Microsoft_Windows_MSDTC_53325_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53376, version=0)
class Microsoft_Windows_MSDTC_53376_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53377, version=0)
class Microsoft_Windows_MSDTC_53377_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53378, version=0)
class Microsoft_Windows_MSDTC_53378_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53379, version=0)
class Microsoft_Windows_MSDTC_53379_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53380, version=0)
class Microsoft_Windows_MSDTC_53380_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53381, version=0)
class Microsoft_Windows_MSDTC_53381_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53504, version=0)
class Microsoft_Windows_MSDTC_53504_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53505, version=0)
class Microsoft_Windows_MSDTC_53505_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53506, version=0)
class Microsoft_Windows_MSDTC_53506_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53507, version=0)
class Microsoft_Windows_MSDTC_53507_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53508, version=0)
class Microsoft_Windows_MSDTC_53508_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53509, version=0)
class Microsoft_Windows_MSDTC_53509_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53510, version=0)
class Microsoft_Windows_MSDTC_53510_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53511, version=0)
class Microsoft_Windows_MSDTC_53511_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53512, version=0)
class Microsoft_Windows_MSDTC_53512_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53513, version=0)
class Microsoft_Windows_MSDTC_53513_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53514, version=0)
class Microsoft_Windows_MSDTC_53514_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53515, version=0)
class Microsoft_Windows_MSDTC_53515_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53516, version=0)
class Microsoft_Windows_MSDTC_53516_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53517, version=0)
class Microsoft_Windows_MSDTC_53517_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53518, version=0)
class Microsoft_Windows_MSDTC_53518_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53519, version=0)
class Microsoft_Windows_MSDTC_53519_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53520, version=0)
class Microsoft_Windows_MSDTC_53520_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53521, version=0)
class Microsoft_Windows_MSDTC_53521_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53522, version=0)
class Microsoft_Windows_MSDTC_53522_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("719be4ed-e9bc-4dd8-a7cf-c85ce8e4975d"), event_id=53523, version=0)
class Microsoft_Windows_MSDTC_53523_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )

