# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MPRMSG
GUID : f2c628ae-d26c-4352-9c45-74754e1e2f9f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20001, version=0)
class Microsoft_Windows_MPRMSG_20001_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20002, version=0)
class Microsoft_Windows_MPRMSG_20002_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20003, version=0)
class Microsoft_Windows_MPRMSG_20003_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20004, version=0)
class Microsoft_Windows_MPRMSG_20004_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20005, version=0)
class Microsoft_Windows_MPRMSG_20005_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20006, version=0)
class Microsoft_Windows_MPRMSG_20006_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20009, version=0)
class Microsoft_Windows_MPRMSG_20009_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20010, version=0)
class Microsoft_Windows_MPRMSG_20010_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20011, version=0)
class Microsoft_Windows_MPRMSG_20011_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20012, version=0)
class Microsoft_Windows_MPRMSG_20012_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20013, version=0)
class Microsoft_Windows_MPRMSG_20013_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20016, version=0)
class Microsoft_Windows_MPRMSG_20016_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20018, version=0)
class Microsoft_Windows_MPRMSG_20018_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20019, version=0)
class Microsoft_Windows_MPRMSG_20019_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20020, version=0)
class Microsoft_Windows_MPRMSG_20020_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20021, version=0)
class Microsoft_Windows_MPRMSG_20021_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20022, version=0)
class Microsoft_Windows_MPRMSG_20022_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20023, version=0)
class Microsoft_Windows_MPRMSG_20023_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20024, version=0)
class Microsoft_Windows_MPRMSG_20024_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20025, version=0)
class Microsoft_Windows_MPRMSG_20025_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20026, version=0)
class Microsoft_Windows_MPRMSG_20026_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20027, version=0)
class Microsoft_Windows_MPRMSG_20027_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20028, version=0)
class Microsoft_Windows_MPRMSG_20028_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20029, version=0)
class Microsoft_Windows_MPRMSG_20029_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20030, version=0)
class Microsoft_Windows_MPRMSG_20030_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20031, version=0)
class Microsoft_Windows_MPRMSG_20031_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20032, version=0)
class Microsoft_Windows_MPRMSG_20032_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20033, version=0)
class Microsoft_Windows_MPRMSG_20033_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20034, version=0)
class Microsoft_Windows_MPRMSG_20034_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20035, version=0)
class Microsoft_Windows_MPRMSG_20035_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20036, version=0)
class Microsoft_Windows_MPRMSG_20036_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20037, version=0)
class Microsoft_Windows_MPRMSG_20037_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20038, version=0)
class Microsoft_Windows_MPRMSG_20038_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20042, version=0)
class Microsoft_Windows_MPRMSG_20042_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20043, version=0)
class Microsoft_Windows_MPRMSG_20043_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20044, version=0)
class Microsoft_Windows_MPRMSG_20044_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20045, version=0)
class Microsoft_Windows_MPRMSG_20045_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20046, version=0)
class Microsoft_Windows_MPRMSG_20046_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20047, version=0)
class Microsoft_Windows_MPRMSG_20047_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20051, version=0)
class Microsoft_Windows_MPRMSG_20051_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20052, version=0)
class Microsoft_Windows_MPRMSG_20052_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20053, version=0)
class Microsoft_Windows_MPRMSG_20053_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20054, version=0)
class Microsoft_Windows_MPRMSG_20054_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20055, version=0)
class Microsoft_Windows_MPRMSG_20055_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20056, version=0)
class Microsoft_Windows_MPRMSG_20056_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20057, version=0)
class Microsoft_Windows_MPRMSG_20057_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20058, version=0)
class Microsoft_Windows_MPRMSG_20058_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20059, version=0)
class Microsoft_Windows_MPRMSG_20059_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20060, version=0)
class Microsoft_Windows_MPRMSG_20060_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20061, version=0)
class Microsoft_Windows_MPRMSG_20061_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20062, version=0)
class Microsoft_Windows_MPRMSG_20062_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20063, version=0)
class Microsoft_Windows_MPRMSG_20063_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20064, version=0)
class Microsoft_Windows_MPRMSG_20064_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20065, version=0)
class Microsoft_Windows_MPRMSG_20065_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20066, version=0)
class Microsoft_Windows_MPRMSG_20066_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20067, version=0)
class Microsoft_Windows_MPRMSG_20067_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20068, version=0)
class Microsoft_Windows_MPRMSG_20068_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20069, version=0)
class Microsoft_Windows_MPRMSG_20069_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20070, version=0)
class Microsoft_Windows_MPRMSG_20070_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20071, version=0)
class Microsoft_Windows_MPRMSG_20071_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20072, version=0)
class Microsoft_Windows_MPRMSG_20072_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20079, version=0)
class Microsoft_Windows_MPRMSG_20079_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20080, version=0)
class Microsoft_Windows_MPRMSG_20080_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20081, version=0)
class Microsoft_Windows_MPRMSG_20081_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20082, version=0)
class Microsoft_Windows_MPRMSG_20082_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20084, version=0)
class Microsoft_Windows_MPRMSG_20084_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20085, version=0)
class Microsoft_Windows_MPRMSG_20085_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20086, version=0)
class Microsoft_Windows_MPRMSG_20086_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20087, version=0)
class Microsoft_Windows_MPRMSG_20087_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20088, version=0)
class Microsoft_Windows_MPRMSG_20088_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20090, version=0)
class Microsoft_Windows_MPRMSG_20090_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20091, version=0)
class Microsoft_Windows_MPRMSG_20091_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20092, version=0)
class Microsoft_Windows_MPRMSG_20092_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20093, version=0)
class Microsoft_Windows_MPRMSG_20093_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20094, version=0)
class Microsoft_Windows_MPRMSG_20094_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20096, version=0)
class Microsoft_Windows_MPRMSG_20096_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20098, version=0)
class Microsoft_Windows_MPRMSG_20098_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20099, version=0)
class Microsoft_Windows_MPRMSG_20099_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20100, version=0)
class Microsoft_Windows_MPRMSG_20100_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20101, version=0)
class Microsoft_Windows_MPRMSG_20101_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20102, version=0)
class Microsoft_Windows_MPRMSG_20102_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20103, version=0)
class Microsoft_Windows_MPRMSG_20103_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20104, version=0)
class Microsoft_Windows_MPRMSG_20104_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20105, version=0)
class Microsoft_Windows_MPRMSG_20105_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20106, version=0)
class Microsoft_Windows_MPRMSG_20106_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20107, version=0)
class Microsoft_Windows_MPRMSG_20107_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20108, version=0)
class Microsoft_Windows_MPRMSG_20108_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20110, version=0)
class Microsoft_Windows_MPRMSG_20110_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20111, version=0)
class Microsoft_Windows_MPRMSG_20111_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20112, version=0)
class Microsoft_Windows_MPRMSG_20112_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20113, version=0)
class Microsoft_Windows_MPRMSG_20113_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20114, version=0)
class Microsoft_Windows_MPRMSG_20114_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20125, version=0)
class Microsoft_Windows_MPRMSG_20125_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20126, version=0)
class Microsoft_Windows_MPRMSG_20126_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20127, version=0)
class Microsoft_Windows_MPRMSG_20127_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20132, version=0)
class Microsoft_Windows_MPRMSG_20132_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20138, version=0)
class Microsoft_Windows_MPRMSG_20138_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20143, version=0)
class Microsoft_Windows_MPRMSG_20143_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20144, version=0)
class Microsoft_Windows_MPRMSG_20144_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20145, version=0)
class Microsoft_Windows_MPRMSG_20145_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20146, version=0)
class Microsoft_Windows_MPRMSG_20146_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20147, version=0)
class Microsoft_Windows_MPRMSG_20147_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20148, version=0)
class Microsoft_Windows_MPRMSG_20148_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20149, version=0)
class Microsoft_Windows_MPRMSG_20149_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20150, version=0)
class Microsoft_Windows_MPRMSG_20150_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20151, version=0)
class Microsoft_Windows_MPRMSG_20151_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20152, version=0)
class Microsoft_Windows_MPRMSG_20152_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20153, version=0)
class Microsoft_Windows_MPRMSG_20153_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20157, version=0)
class Microsoft_Windows_MPRMSG_20157_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20165, version=0)
class Microsoft_Windows_MPRMSG_20165_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20166, version=0)
class Microsoft_Windows_MPRMSG_20166_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20167, version=0)
class Microsoft_Windows_MPRMSG_20167_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20168, version=0)
class Microsoft_Windows_MPRMSG_20168_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20169, version=0)
class Microsoft_Windows_MPRMSG_20169_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20170, version=0)
class Microsoft_Windows_MPRMSG_20170_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20171, version=0)
class Microsoft_Windows_MPRMSG_20171_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20172, version=0)
class Microsoft_Windows_MPRMSG_20172_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20173, version=0)
class Microsoft_Windows_MPRMSG_20173_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20174, version=0)
class Microsoft_Windows_MPRMSG_20174_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20175, version=0)
class Microsoft_Windows_MPRMSG_20175_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20176, version=0)
class Microsoft_Windows_MPRMSG_20176_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20177, version=0)
class Microsoft_Windows_MPRMSG_20177_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20178, version=0)
class Microsoft_Windows_MPRMSG_20178_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20179, version=0)
class Microsoft_Windows_MPRMSG_20179_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20180, version=0)
class Microsoft_Windows_MPRMSG_20180_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20181, version=0)
class Microsoft_Windows_MPRMSG_20181_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20182, version=0)
class Microsoft_Windows_MPRMSG_20182_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20183, version=0)
class Microsoft_Windows_MPRMSG_20183_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20184, version=0)
class Microsoft_Windows_MPRMSG_20184_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20185, version=0)
class Microsoft_Windows_MPRMSG_20185_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20186, version=0)
class Microsoft_Windows_MPRMSG_20186_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20190, version=0)
class Microsoft_Windows_MPRMSG_20190_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20191, version=0)
class Microsoft_Windows_MPRMSG_20191_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20192, version=0)
class Microsoft_Windows_MPRMSG_20192_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20193, version=0)
class Microsoft_Windows_MPRMSG_20193_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20196, version=0)
class Microsoft_Windows_MPRMSG_20196_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20197, version=0)
class Microsoft_Windows_MPRMSG_20197_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20198, version=0)
class Microsoft_Windows_MPRMSG_20198_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20199, version=0)
class Microsoft_Windows_MPRMSG_20199_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20202, version=0)
class Microsoft_Windows_MPRMSG_20202_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20203, version=0)
class Microsoft_Windows_MPRMSG_20203_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20204, version=0)
class Microsoft_Windows_MPRMSG_20204_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20205, version=0)
class Microsoft_Windows_MPRMSG_20205_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20206, version=0)
class Microsoft_Windows_MPRMSG_20206_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20207, version=0)
class Microsoft_Windows_MPRMSG_20207_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20208, version=0)
class Microsoft_Windows_MPRMSG_20208_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20209, version=0)
class Microsoft_Windows_MPRMSG_20209_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20210, version=0)
class Microsoft_Windows_MPRMSG_20210_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20211, version=0)
class Microsoft_Windows_MPRMSG_20211_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20212, version=0)
class Microsoft_Windows_MPRMSG_20212_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20213, version=0)
class Microsoft_Windows_MPRMSG_20213_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20214, version=0)
class Microsoft_Windows_MPRMSG_20214_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20215, version=0)
class Microsoft_Windows_MPRMSG_20215_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20216, version=0)
class Microsoft_Windows_MPRMSG_20216_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20217, version=0)
class Microsoft_Windows_MPRMSG_20217_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20218, version=0)
class Microsoft_Windows_MPRMSG_20218_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20219, version=0)
class Microsoft_Windows_MPRMSG_20219_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20220, version=0)
class Microsoft_Windows_MPRMSG_20220_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20230, version=0)
class Microsoft_Windows_MPRMSG_20230_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20247, version=0)
class Microsoft_Windows_MPRMSG_20247_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20248, version=0)
class Microsoft_Windows_MPRMSG_20248_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20249, version=0)
class Microsoft_Windows_MPRMSG_20249_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20250, version=0)
class Microsoft_Windows_MPRMSG_20250_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20251, version=0)
class Microsoft_Windows_MPRMSG_20251_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString,
        "param8" / WString,
        "param9" / WString,
        "param10" / WString,
        "param11" / WString,
        "param12" / WString,
        "param13" / WString,
        "param14" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20252, version=0)
class Microsoft_Windows_MPRMSG_20252_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20253, version=0)
class Microsoft_Windows_MPRMSG_20253_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20254, version=0)
class Microsoft_Windows_MPRMSG_20254_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20255, version=0)
class Microsoft_Windows_MPRMSG_20255_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20256, version=0)
class Microsoft_Windows_MPRMSG_20256_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20257, version=0)
class Microsoft_Windows_MPRMSG_20257_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20258, version=0)
class Microsoft_Windows_MPRMSG_20258_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20259, version=0)
class Microsoft_Windows_MPRMSG_20259_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20260, version=0)
class Microsoft_Windows_MPRMSG_20260_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20261, version=0)
class Microsoft_Windows_MPRMSG_20261_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20262, version=0)
class Microsoft_Windows_MPRMSG_20262_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20263, version=0)
class Microsoft_Windows_MPRMSG_20263_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20264, version=0)
class Microsoft_Windows_MPRMSG_20264_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20265, version=0)
class Microsoft_Windows_MPRMSG_20265_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20266, version=0)
class Microsoft_Windows_MPRMSG_20266_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20267, version=0)
class Microsoft_Windows_MPRMSG_20267_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20268, version=0)
class Microsoft_Windows_MPRMSG_20268_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20269, version=0)
class Microsoft_Windows_MPRMSG_20269_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20270, version=0)
class Microsoft_Windows_MPRMSG_20270_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20271, version=0)
class Microsoft_Windows_MPRMSG_20271_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20272, version=0)
class Microsoft_Windows_MPRMSG_20272_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString,
        "param8" / WString,
        "param9" / WString,
        "param10" / WString,
        "param11" / WString,
        "param12" / WString,
        "param13" / WString,
        "param14" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20274, version=0)
class Microsoft_Windows_MPRMSG_20274_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20275, version=0)
class Microsoft_Windows_MPRMSG_20275_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20276, version=0)
class Microsoft_Windows_MPRMSG_20276_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20279, version=0)
class Microsoft_Windows_MPRMSG_20279_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20280, version=0)
class Microsoft_Windows_MPRMSG_20280_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20281, version=0)
class Microsoft_Windows_MPRMSG_20281_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20282, version=0)
class Microsoft_Windows_MPRMSG_20282_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20283, version=0)
class Microsoft_Windows_MPRMSG_20283_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20284, version=0)
class Microsoft_Windows_MPRMSG_20284_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20285, version=0)
class Microsoft_Windows_MPRMSG_20285_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20286, version=0)
class Microsoft_Windows_MPRMSG_20286_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20287, version=0)
class Microsoft_Windows_MPRMSG_20287_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20288, version=0)
class Microsoft_Windows_MPRMSG_20288_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20289, version=0)
class Microsoft_Windows_MPRMSG_20289_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20290, version=0)
class Microsoft_Windows_MPRMSG_20290_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20291, version=0)
class Microsoft_Windows_MPRMSG_20291_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("f2c628ae-d26c-4352-9c45-74754e1e2f9f"), event_id=20292, version=0)
class Microsoft_Windows_MPRMSG_20292_0(Etw):
    pattern = Struct(
        "MaxCount" / WString,
        "HResult" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )

