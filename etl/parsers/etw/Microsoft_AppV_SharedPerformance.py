# -*- coding: utf-8 -*-
"""
Microsoft-AppV-SharedPerformance
GUID : fb4a19ee-eb5a-47a4-bc52-e71aac6d0859
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=31, version=1)
class Microsoft_AppV_SharedPerformance_31_1(Etw):
    pattern = Struct(
        "IntValue" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=104, version=1)
class Microsoft_AppV_SharedPerformance_104_1(Etw):
    pattern = Struct(
        "IntValue" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4000, version=0)
class Microsoft_AppV_SharedPerformance_4000_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4001, version=0)
class Microsoft_AppV_SharedPerformance_4001_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4002, version=0)
class Microsoft_AppV_SharedPerformance_4002_0(Etw):
    pattern = Struct(
        "Guid" / Guid
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4003, version=0)
class Microsoft_AppV_SharedPerformance_4003_0(Etw):
    pattern = Struct(
        "Guid" / Guid
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4004, version=0)
class Microsoft_AppV_SharedPerformance_4004_0(Etw):
    pattern = Struct(
        "Guid" / Guid
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4005, version=0)
class Microsoft_AppV_SharedPerformance_4005_0(Etw):
    pattern = Struct(
        "Guid" / Guid
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4006, version=0)
class Microsoft_AppV_SharedPerformance_4006_0(Etw):
    pattern = Struct(
        "Guid" / Guid
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4007, version=0)
class Microsoft_AppV_SharedPerformance_4007_0(Etw):
    pattern = Struct(
        "Guid" / Guid
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4008, version=0)
class Microsoft_AppV_SharedPerformance_4008_0(Etw):
    pattern = Struct(
        "Guid" / Guid
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4009, version=0)
class Microsoft_AppV_SharedPerformance_4009_0(Etw):
    pattern = Struct(
        "Guid" / Guid
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4010, version=0)
class Microsoft_AppV_SharedPerformance_4010_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4011, version=0)
class Microsoft_AppV_SharedPerformance_4011_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4012, version=0)
class Microsoft_AppV_SharedPerformance_4012_0(Etw):
    pattern = Struct(
        "Guid" / Guid
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4013, version=0)
class Microsoft_AppV_SharedPerformance_4013_0(Etw):
    pattern = Struct(
        "Guid" / Guid
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4014, version=0)
class Microsoft_AppV_SharedPerformance_4014_0(Etw):
    pattern = Struct(
        "Guid" / Guid
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4015, version=0)
class Microsoft_AppV_SharedPerformance_4015_0(Etw):
    pattern = Struct(
        "Guid" / Guid
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4016, version=0)
class Microsoft_AppV_SharedPerformance_4016_0(Etw):
    pattern = Struct(
        "Guid" / Guid
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4017, version=0)
class Microsoft_AppV_SharedPerformance_4017_0(Etw):
    pattern = Struct(
        "Guid" / Guid
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4018, version=0)
class Microsoft_AppV_SharedPerformance_4018_0(Etw):
    pattern = Struct(
        "Guid" / Guid
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4019, version=0)
class Microsoft_AppV_SharedPerformance_4019_0(Etw):
    pattern = Struct(
        "Guid" / Guid
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4048, version=0)
class Microsoft_AppV_SharedPerformance_4048_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=4049, version=0)
class Microsoft_AppV_SharedPerformance_4049_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=5013, version=1)
class Microsoft_AppV_SharedPerformance_5013_1(Etw):
    pattern = Struct(
        "SessionID" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=5014, version=1)
class Microsoft_AppV_SharedPerformance_5014_1(Etw):
    pattern = Struct(
        "SessionID" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=5015, version=1)
class Microsoft_AppV_SharedPerformance_5015_1(Etw):
    pattern = Struct(
        "SessionID" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=5016, version=1)
class Microsoft_AppV_SharedPerformance_5016_1(Etw):
    pattern = Struct(
        "SessionID" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=5017, version=1)
class Microsoft_AppV_SharedPerformance_5017_1(Etw):
    pattern = Struct(
        "ClientEvent" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=5018, version=1)
class Microsoft_AppV_SharedPerformance_5018_1(Etw):
    pattern = Struct(
        "ClientEvent" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=5025, version=1)
class Microsoft_AppV_SharedPerformance_5025_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=5026, version=1)
class Microsoft_AppV_SharedPerformance_5026_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=5027, version=1)
class Microsoft_AppV_SharedPerformance_5027_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=5028, version=1)
class Microsoft_AppV_SharedPerformance_5028_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=5029, version=1)
class Microsoft_AppV_SharedPerformance_5029_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=5030, version=1)
class Microsoft_AppV_SharedPerformance_5030_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=5037, version=1)
class Microsoft_AppV_SharedPerformance_5037_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=5038, version=1)
class Microsoft_AppV_SharedPerformance_5038_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=5039, version=1)
class Microsoft_AppV_SharedPerformance_5039_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=5040, version=1)
class Microsoft_AppV_SharedPerformance_5040_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=5041, version=1)
class Microsoft_AppV_SharedPerformance_5041_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=5042, version=1)
class Microsoft_AppV_SharedPerformance_5042_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6002, version=0)
class Microsoft_AppV_SharedPerformance_6002_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "guid1" / Guid,
        "guid2" / Guid
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6003, version=0)
class Microsoft_AppV_SharedPerformance_6003_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "guid1" / Guid,
        "guid2" / Guid
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6004, version=0)
class Microsoft_AppV_SharedPerformance_6004_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6005, version=0)
class Microsoft_AppV_SharedPerformance_6005_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6008, version=0)
class Microsoft_AppV_SharedPerformance_6008_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "guid1" / Guid,
        "guid2" / Guid
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6009, version=0)
class Microsoft_AppV_SharedPerformance_6009_0(Etw):
    pattern = Struct(
        "str1" / WString,
        "guid1" / Guid,
        "guid2" / Guid
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6010, version=0)
class Microsoft_AppV_SharedPerformance_6010_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6011, version=0)
class Microsoft_AppV_SharedPerformance_6011_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6014, version=0)
class Microsoft_AppV_SharedPerformance_6014_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6015, version=0)
class Microsoft_AppV_SharedPerformance_6015_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6016, version=0)
class Microsoft_AppV_SharedPerformance_6016_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6017, version=0)
class Microsoft_AppV_SharedPerformance_6017_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6020, version=0)
class Microsoft_AppV_SharedPerformance_6020_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6021, version=0)
class Microsoft_AppV_SharedPerformance_6021_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6022, version=0)
class Microsoft_AppV_SharedPerformance_6022_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6023, version=0)
class Microsoft_AppV_SharedPerformance_6023_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6026, version=0)
class Microsoft_AppV_SharedPerformance_6026_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6027, version=0)
class Microsoft_AppV_SharedPerformance_6027_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6032, version=0)
class Microsoft_AppV_SharedPerformance_6032_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6033, version=0)
class Microsoft_AppV_SharedPerformance_6033_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6034, version=0)
class Microsoft_AppV_SharedPerformance_6034_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6035, version=0)
class Microsoft_AppV_SharedPerformance_6035_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6040, version=0)
class Microsoft_AppV_SharedPerformance_6040_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6041, version=0)
class Microsoft_AppV_SharedPerformance_6041_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6044, version=0)
class Microsoft_AppV_SharedPerformance_6044_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6045, version=0)
class Microsoft_AppV_SharedPerformance_6045_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6050, version=0)
class Microsoft_AppV_SharedPerformance_6050_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=6051, version=0)
class Microsoft_AppV_SharedPerformance_6051_0(Etw):
    pattern = Struct(
        "str" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=8032, version=1)
class Microsoft_AppV_SharedPerformance_8032_1(Etw):
    pattern = Struct(
        "ustring" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=8033, version=1)
class Microsoft_AppV_SharedPerformance_8033_1(Etw):
    pattern = Struct(
        "ustring" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=8034, version=1)
class Microsoft_AppV_SharedPerformance_8034_1(Etw):
    pattern = Struct(
        "ustring" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=8035, version=1)
class Microsoft_AppV_SharedPerformance_8035_1(Etw):
    pattern = Struct(
        "ustring" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=8036, version=1)
class Microsoft_AppV_SharedPerformance_8036_1(Etw):
    pattern = Struct(
        "uint64" / Int64ul,
        "uint32" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=8037, version=1)
class Microsoft_AppV_SharedPerformance_8037_1(Etw):
    pattern = Struct(
        "uint64" / Int64ul,
        "uint32" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=8040, version=1)
class Microsoft_AppV_SharedPerformance_8040_1(Etw):
    pattern = Struct(
        "ActivityId" / Int64ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=8041, version=1)
class Microsoft_AppV_SharedPerformance_8041_1(Etw):
    pattern = Struct(
        "ActivityId" / Int64ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=8042, version=1)
class Microsoft_AppV_SharedPerformance_8042_1(Etw):
    pattern = Struct(
        "ActivityId" / Int64ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=8043, version=1)
class Microsoft_AppV_SharedPerformance_8043_1(Etw):
    pattern = Struct(
        "ActivityId" / Int64ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=8044, version=1)
class Microsoft_AppV_SharedPerformance_8044_1(Etw):
    pattern = Struct(
        "ActivityId" / Int64ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=8045, version=1)
class Microsoft_AppV_SharedPerformance_8045_1(Etw):
    pattern = Struct(
        "ActivityId" / Int64ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=8046, version=1)
class Microsoft_AppV_SharedPerformance_8046_1(Etw):
    pattern = Struct(
        "ActivityId" / Int64ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=8047, version=1)
class Microsoft_AppV_SharedPerformance_8047_1(Etw):
    pattern = Struct(
        "ActivityId" / Int64ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=8048, version=1)
class Microsoft_AppV_SharedPerformance_8048_1(Etw):
    pattern = Struct(
        "ActivityId" / Int64ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=8049, version=1)
class Microsoft_AppV_SharedPerformance_8049_1(Etw):
    pattern = Struct(
        "ActivityId" / Int64ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=8050, version=1)
class Microsoft_AppV_SharedPerformance_8050_1(Etw):
    pattern = Struct(
        "ActivityId" / Int64ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=8051, version=1)
class Microsoft_AppV_SharedPerformance_8051_1(Etw):
    pattern = Struct(
        "ActivityId" / Int64ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=8052, version=1)
class Microsoft_AppV_SharedPerformance_8052_1(Etw):
    pattern = Struct(
        "ActivityId" / Int64ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=8053, version=1)
class Microsoft_AppV_SharedPerformance_8053_1(Etw):
    pattern = Struct(
        "ActivityId" / Int64ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=12012, version=1)
class Microsoft_AppV_SharedPerformance_12012_1(Etw):
    pattern = Struct(
        "pid" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=12013, version=1)
class Microsoft_AppV_SharedPerformance_12013_1(Etw):
    pattern = Struct(
        "pid" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=12014, version=1)
class Microsoft_AppV_SharedPerformance_12014_1(Etw):
    pattern = Struct(
        "pid" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=12015, version=1)
class Microsoft_AppV_SharedPerformance_12015_1(Etw):
    pattern = Struct(
        "pid" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=12020, version=1)
class Microsoft_AppV_SharedPerformance_12020_1(Etw):
    pattern = Struct(
        "pid" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=12021, version=1)
class Microsoft_AppV_SharedPerformance_12021_1(Etw):
    pattern = Struct(
        "pid" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=12022, version=1)
class Microsoft_AppV_SharedPerformance_12022_1(Etw):
    pattern = Struct(
        "pid" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=12023, version=1)
class Microsoft_AppV_SharedPerformance_12023_1(Etw):
    pattern = Struct(
        "pid" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=12028, version=1)
class Microsoft_AppV_SharedPerformance_12028_1(Etw):
    pattern = Struct(
        "pid" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=12029, version=1)
class Microsoft_AppV_SharedPerformance_12029_1(Etw):
    pattern = Struct(
        "pid" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14001, version=1)
class Microsoft_AppV_SharedPerformance_14001_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14002, version=1)
class Microsoft_AppV_SharedPerformance_14002_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14003, version=1)
class Microsoft_AppV_SharedPerformance_14003_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14004, version=1)
class Microsoft_AppV_SharedPerformance_14004_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14005, version=1)
class Microsoft_AppV_SharedPerformance_14005_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14006, version=1)
class Microsoft_AppV_SharedPerformance_14006_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14007, version=1)
class Microsoft_AppV_SharedPerformance_14007_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14008, version=1)
class Microsoft_AppV_SharedPerformance_14008_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14009, version=1)
class Microsoft_AppV_SharedPerformance_14009_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14010, version=1)
class Microsoft_AppV_SharedPerformance_14010_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14011, version=1)
class Microsoft_AppV_SharedPerformance_14011_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14012, version=1)
class Microsoft_AppV_SharedPerformance_14012_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14015, version=1)
class Microsoft_AppV_SharedPerformance_14015_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14016, version=1)
class Microsoft_AppV_SharedPerformance_14016_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14019, version=1)
class Microsoft_AppV_SharedPerformance_14019_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14020, version=1)
class Microsoft_AppV_SharedPerformance_14020_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14023, version=1)
class Microsoft_AppV_SharedPerformance_14023_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14024, version=1)
class Microsoft_AppV_SharedPerformance_14024_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14027, version=1)
class Microsoft_AppV_SharedPerformance_14027_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14028, version=1)
class Microsoft_AppV_SharedPerformance_14028_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14031, version=1)
class Microsoft_AppV_SharedPerformance_14031_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14032, version=1)
class Microsoft_AppV_SharedPerformance_14032_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14035, version=1)
class Microsoft_AppV_SharedPerformance_14035_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14036, version=1)
class Microsoft_AppV_SharedPerformance_14036_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14039, version=1)
class Microsoft_AppV_SharedPerformance_14039_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14040, version=1)
class Microsoft_AppV_SharedPerformance_14040_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14043, version=1)
class Microsoft_AppV_SharedPerformance_14043_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14044, version=1)
class Microsoft_AppV_SharedPerformance_14044_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14047, version=1)
class Microsoft_AppV_SharedPerformance_14047_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14048, version=1)
class Microsoft_AppV_SharedPerformance_14048_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14051, version=1)
class Microsoft_AppV_SharedPerformance_14051_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14052, version=1)
class Microsoft_AppV_SharedPerformance_14052_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14055, version=1)
class Microsoft_AppV_SharedPerformance_14055_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14056, version=1)
class Microsoft_AppV_SharedPerformance_14056_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14059, version=1)
class Microsoft_AppV_SharedPerformance_14059_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14060, version=1)
class Microsoft_AppV_SharedPerformance_14060_1(Etw):
    pattern = Struct(
        "Component" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14061, version=1)
class Microsoft_AppV_SharedPerformance_14061_1(Etw):
    pattern = Struct(
        "ActivityId" / Int64ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=14062, version=1)
class Microsoft_AppV_SharedPerformance_14062_1(Etw):
    pattern = Struct(
        "ActivityId" / Int64ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=24010, version=1)
class Microsoft_AppV_SharedPerformance_24010_1(Etw):
    pattern = Struct(
        "uint32" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=24011, version=1)
class Microsoft_AppV_SharedPerformance_24011_1(Etw):
    pattern = Struct(
        "uint32" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=30012, version=1)
class Microsoft_AppV_SharedPerformance_30012_1(Etw):
    pattern = Struct(
        "uint32" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=30013, version=1)
class Microsoft_AppV_SharedPerformance_30013_1(Etw):
    pattern = Struct(
        "uint32" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=30512, version=1)
class Microsoft_AppV_SharedPerformance_30512_1(Etw):
    pattern = Struct(
        "uint32" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=30513, version=1)
class Microsoft_AppV_SharedPerformance_30513_1(Etw):
    pattern = Struct(
        "uint32" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=30630, version=1)
class Microsoft_AppV_SharedPerformance_30630_1(Etw):
    pattern = Struct(
        "uint32" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=30633, version=1)
class Microsoft_AppV_SharedPerformance_30633_1(Etw):
    pattern = Struct(
        "uint32" / Int32ul
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=46012, version=0)
class Microsoft_AppV_SharedPerformance_46012_0(Etw):
    pattern = Struct(
        "ustring" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=46013, version=0)
class Microsoft_AppV_SharedPerformance_46013_0(Etw):
    pattern = Struct(
        "ustring" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=46014, version=0)
class Microsoft_AppV_SharedPerformance_46014_0(Etw):
    pattern = Struct(
        "ustring" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=46015, version=0)
class Microsoft_AppV_SharedPerformance_46015_0(Etw):
    pattern = Struct(
        "ustring" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=46016, version=0)
class Microsoft_AppV_SharedPerformance_46016_0(Etw):
    pattern = Struct(
        "ustring" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=46017, version=0)
class Microsoft_AppV_SharedPerformance_46017_0(Etw):
    pattern = Struct(
        "ustring" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=50000, version=1)
class Microsoft_AppV_SharedPerformance_50000_1(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("fb4a19ee-eb5a-47a4-bc52-e71aac6d0859"), event_id=50001, version=1)
class Microsoft_AppV_SharedPerformance_50001_1(Etw):
    pattern = Struct(
        "Name" / WString
    )

