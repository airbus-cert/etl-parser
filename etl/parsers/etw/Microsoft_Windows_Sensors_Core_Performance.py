# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Sensors-Core-Performance
GUID : 9e051eaa-7fee-4f9f-8897-d86f3692e8af
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9e051eaa-7fee-4f9f-8897-d86f3692e8af"), event_id=1001, version=0)
class Microsoft_Windows_Sensors_Core_Performance_1001_0(Etw):
    pattern = Struct(
        "IoctlType" / Int32ul,
        "SensorObj" / Int64ul
    )


@declare(guid=guid("9e051eaa-7fee-4f9f-8897-d86f3692e8af"), event_id=1002, version=0)
class Microsoft_Windows_Sensors_Core_Performance_1002_0(Etw):
    pattern = Struct(
        "IoctlType" / Int32ul,
        "SensorObj" / Int64ul
    )


@declare(guid=guid("9e051eaa-7fee-4f9f-8897-d86f3692e8af"), event_id=1003, version=0)
class Microsoft_Windows_Sensors_Core_Performance_1003_0(Etw):
    pattern = Struct(
        "PayloadSize" / Int32ul
    )


@declare(guid=guid("9e051eaa-7fee-4f9f-8897-d86f3692e8af"), event_id=1004, version=0)
class Microsoft_Windows_Sensors_Core_Performance_1004_0(Etw):
    pattern = Struct(
        "PayloadSize" / Int32ul
    )


@declare(guid=guid("9e051eaa-7fee-4f9f-8897-d86f3692e8af"), event_id=1005, version=0)
class Microsoft_Windows_Sensors_Core_Performance_1005_0(Etw):
    pattern = Struct(
        "PayloadSize" / Int32ul
    )


@declare(guid=guid("9e051eaa-7fee-4f9f-8897-d86f3692e8af"), event_id=1006, version=0)
class Microsoft_Windows_Sensors_Core_Performance_1006_0(Etw):
    pattern = Struct(
        "PayloadSize" / Int32ul
    )


@declare(guid=guid("9e051eaa-7fee-4f9f-8897-d86f3692e8af"), event_id=1007, version=0)
class Microsoft_Windows_Sensors_Core_Performance_1007_0(Etw):
    pattern = Struct(
        "PayloadSize" / Int32ul
    )


@declare(guid=guid("9e051eaa-7fee-4f9f-8897-d86f3692e8af"), event_id=1008, version=0)
class Microsoft_Windows_Sensors_Core_Performance_1008_0(Etw):
    pattern = Struct(
        "PayloadSize" / Int32ul
    )


@declare(guid=guid("9e051eaa-7fee-4f9f-8897-d86f3692e8af"), event_id=1009, version=0)
class Microsoft_Windows_Sensors_Core_Performance_1009_0(Etw):
    pattern = Struct(
        "IoctlType" / Int32ul
    )


@declare(guid=guid("9e051eaa-7fee-4f9f-8897-d86f3692e8af"), event_id=1010, version=0)
class Microsoft_Windows_Sensors_Core_Performance_1010_0(Etw):
    pattern = Struct(
        "IoctlType" / Int32ul
    )


@declare(guid=guid("9e051eaa-7fee-4f9f-8897-d86f3692e8af"), event_id=1011, version=0)
class Microsoft_Windows_Sensors_Core_Performance_1011_0(Etw):
    pattern = Struct(
        "IoctlType" / Int32ul
    )


@declare(guid=guid("9e051eaa-7fee-4f9f-8897-d86f3692e8af"), event_id=1012, version=0)
class Microsoft_Windows_Sensors_Core_Performance_1012_0(Etw):
    pattern = Struct(
        "IoctlType" / Int32ul,
        "SensorObj" / Int64ul
    )


@declare(guid=guid("9e051eaa-7fee-4f9f-8897-d86f3692e8af"), event_id=1013, version=0)
class Microsoft_Windows_Sensors_Core_Performance_1013_0(Etw):
    pattern = Struct(
        "IoctlType" / Int32ul,
        "SensorObj" / Int64ul
    )


@declare(guid=guid("9e051eaa-7fee-4f9f-8897-d86f3692e8af"), event_id=1014, version=0)
class Microsoft_Windows_Sensors_Core_Performance_1014_0(Etw):
    pattern = Struct(
        "IoctlType" / Int32ul
    )


@declare(guid=guid("9e051eaa-7fee-4f9f-8897-d86f3692e8af"), event_id=1015, version=0)
class Microsoft_Windows_Sensors_Core_Performance_1015_0(Etw):
    pattern = Struct(
        "SensorObj" / Int64ul,
        "CollectionListPtr" / Int64ul
    )


@declare(guid=guid("9e051eaa-7fee-4f9f-8897-d86f3692e8af"), event_id=1016, version=0)
class Microsoft_Windows_Sensors_Core_Performance_1016_0(Etw):
    pattern = Struct(
        "SensorObj" / Int64ul,
        "CollectionListPtr" / Int64ul
    )


@declare(guid=guid("9e051eaa-7fee-4f9f-8897-d86f3692e8af"), event_id=1018, version=0)
class Microsoft_Windows_Sensors_Core_Performance_1018_0(Etw):
    pattern = Struct(
        "SensorObj" / Int64ul,
        "CollectionListPtr" / Int64ul
    )


@declare(guid=guid("9e051eaa-7fee-4f9f-8897-d86f3692e8af"), event_id=1019, version=0)
class Microsoft_Windows_Sensors_Core_Performance_1019_0(Etw):
    pattern = Struct(
        "SensorObj" / Int64ul,
        "CollectionListPtr" / Int64ul
    )


@declare(guid=guid("9e051eaa-7fee-4f9f-8897-d86f3692e8af"), event_id=1021, version=0)
class Microsoft_Windows_Sensors_Core_Performance_1021_0(Etw):
    pattern = Struct(
        "Driver" / Int64ul,
        "Sensor" / Int64ul,
        "ClientPID" / Int32ul,
        "Type" / Guid,
        "Interval" / Int32ul
    )


@declare(guid=guid("9e051eaa-7fee-4f9f-8897-d86f3692e8af"), event_id=1022, version=0)
class Microsoft_Windows_Sensors_Core_Performance_1022_0(Etw):
    pattern = Struct(
        "Sensor" / Int64ul,
        "DriverCollectionList" / Int64ul
    )


@declare(guid=guid("9e051eaa-7fee-4f9f-8897-d86f3692e8af"), event_id=1023, version=0)
class Microsoft_Windows_Sensors_Core_Performance_1023_0(Etw):
    pattern = Struct(
        "Sensor" / Int64ul,
        "DriverCollectionList" / Int64ul,
        "BufferCollectionList" / Int64ul
    )

