# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SPB-HIDI2C
GUID : 991f8fe6-249d-44d6-b93d-5a3060c1dedb
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("991f8fe6-249d-44d6-b93d-5a3060c1dedb"), event_id=1000, version=1)
class Microsoft_Windows_SPB_HIDI2C_1000_1(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("991f8fe6-249d-44d6-b93d-5a3060c1dedb"), event_id=1001, version=1)
class Microsoft_Windows_SPB_HIDI2C_1001_1(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("991f8fe6-249d-44d6-b93d-5a3060c1dedb"), event_id=1002, version=1)
class Microsoft_Windows_SPB_HIDI2C_1002_1(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("991f8fe6-249d-44d6-b93d-5a3060c1dedb"), event_id=1003, version=1)
class Microsoft_Windows_SPB_HIDI2C_1003_1(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("991f8fe6-249d-44d6-b93d-5a3060c1dedb"), event_id=1011, version=1)
class Microsoft_Windows_SPB_HIDI2C_1011_1(Etw):
    pattern = Struct(
        "SpbIoTarget" / Int64ul,
        "SpbRequest" / Int64ul
    )


@declare(guid=guid("991f8fe6-249d-44d6-b93d-5a3060c1dedb"), event_id=1012, version=1)
class Microsoft_Windows_SPB_HIDI2C_1012_1(Etw):
    pattern = Struct(
        "SpbIoTarget" / Int64ul,
        "SpbRequest" / Int64ul
    )


@declare(guid=guid("991f8fe6-249d-44d6-b93d-5a3060c1dedb"), event_id=1013, version=1)
class Microsoft_Windows_SPB_HIDI2C_1013_1(Etw):
    pattern = Struct(
        "HidReadRequest" / Int64ul
    )


@declare(guid=guid("991f8fe6-249d-44d6-b93d-5a3060c1dedb"), event_id=1014, version=1)
class Microsoft_Windows_SPB_HIDI2C_1014_1(Etw):
    pattern = Struct(
        "HidReadRequest" / Int64ul
    )


@declare(guid=guid("991f8fe6-249d-44d6-b93d-5a3060c1dedb"), event_id=1020, version=1)
class Microsoft_Windows_SPB_HIDI2C_1020_1(Etw):
    pattern = Struct(
        "SpbIoTarget" / Int64ul,
        "Opcode" / Int16ul,
        "Status" / Int32ul
    )


@declare(guid=guid("991f8fe6-249d-44d6-b93d-5a3060c1dedb"), event_id=1021, version=1)
class Microsoft_Windows_SPB_HIDI2C_1021_1(Etw):
    pattern = Struct(
        "SpbIoTarget" / Int64ul,
        "Opcode" / Int16ul,
        "Status" / Int32ul
    )

