# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Bluetooth-MTPEnum
GUID : 04268430-d489-424d-b914-0cff741d6684
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("04268430-d489-424d-b914-0cff741d6684"), event_id=100, version=0)
class Microsoft_Windows_Bluetooth_MTPEnum_100_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("04268430-d489-424d-b914-0cff741d6684"), event_id=101, version=0)
class Microsoft_Windows_Bluetooth_MTPEnum_101_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("04268430-d489-424d-b914-0cff741d6684"), event_id=102, version=0)
class Microsoft_Windows_Bluetooth_MTPEnum_102_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("04268430-d489-424d-b914-0cff741d6684"), event_id=103, version=0)
class Microsoft_Windows_Bluetooth_MTPEnum_103_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("04268430-d489-424d-b914-0cff741d6684"), event_id=200, version=0)
class Microsoft_Windows_Bluetooth_MTPEnum_200_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("04268430-d489-424d-b914-0cff741d6684"), event_id=201, version=0)
class Microsoft_Windows_Bluetooth_MTPEnum_201_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("04268430-d489-424d-b914-0cff741d6684"), event_id=202, version=0)
class Microsoft_Windows_Bluetooth_MTPEnum_202_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("04268430-d489-424d-b914-0cff741d6684"), event_id=203, version=0)
class Microsoft_Windows_Bluetooth_MTPEnum_203_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("04268430-d489-424d-b914-0cff741d6684"), event_id=204, version=0)
class Microsoft_Windows_Bluetooth_MTPEnum_204_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )

