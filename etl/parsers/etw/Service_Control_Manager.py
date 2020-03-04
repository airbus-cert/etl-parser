# -*- coding: utf-8 -*-
"""
Service Control Manager
GUID : 555908d1-a6d7-4695-8e1e-26931d2012f4
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7000, version=0)
class Service_Control_Manager_7000_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "BinaryData" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7001, version=0)
class Service_Control_Manager_7001_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "BinaryData" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7002, version=0)
class Service_Control_Manager_7002_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "BinaryData" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7003, version=0)
class Service_Control_Manager_7003_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "BinaryData" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7005, version=0)
class Service_Control_Manager_7005_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7006, version=0)
class Service_Control_Manager_7006_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7009, version=0)
class Service_Control_Manager_7009_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "BinaryData" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7010, version=0)
class Service_Control_Manager_7010_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7011, version=0)
class Service_Control_Manager_7011_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7013, version=0)
class Service_Control_Manager_7013_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7014, version=0)
class Service_Control_Manager_7014_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7016, version=0)
class Service_Control_Manager_7016_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7017, version=0)
class Service_Control_Manager_7017_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "BinaryData" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7019, version=0)
class Service_Control_Manager_7019_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "BinaryData" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7020, version=0)
class Service_Control_Manager_7020_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "BinaryData" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7021, version=0)
class Service_Control_Manager_7021_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7022, version=0)
class Service_Control_Manager_7022_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "BinaryData" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7023, version=0)
class Service_Control_Manager_7023_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "BinaryData" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7024, version=0)
class Service_Control_Manager_7024_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "BinaryData" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7026, version=0)
class Service_Control_Manager_7026_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7028, version=0)
class Service_Control_Manager_7028_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7030, version=0)
class Service_Control_Manager_7030_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7031, version=0)
class Service_Control_Manager_7031_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "__binLength" / Int32ul,
        "BinaryData" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7032, version=0)
class Service_Control_Manager_7032_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7034, version=0)
class Service_Control_Manager_7034_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "BinaryData" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7035, version=0)
class Service_Control_Manager_7035_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7036, version=0)
class Service_Control_Manager_7036_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "BinaryData" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7037, version=0)
class Service_Control_Manager_7037_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7038, version=0)
class Service_Control_Manager_7038_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7039, version=0)
class Service_Control_Manager_7039_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7040, version=0)
class Service_Control_Manager_7040_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7041, version=0)
class Service_Control_Manager_7041_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7042, version=0)
class Service_Control_Manager_7042_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "__binLength" / Int32ul,
        "BinaryData" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7043, version=0)
class Service_Control_Manager_7043_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "BinaryData" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7044, version=0)
class Service_Control_Manager_7044_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "BinaryData" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7045, version=0)
class Service_Control_Manager_7045_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ImagePath" / WString,
        "ServiceType" / WString,
        "StartType" / WString,
        "AccountName" / WString
    )


@declare(guid=guid("555908d1-a6d7-4695-8e1e-26931d2012f4"), event_id=7046, version=0)
class Service_Control_Manager_7046_0(Etw):
    pattern = Struct(
        "param1" / WString
    )

