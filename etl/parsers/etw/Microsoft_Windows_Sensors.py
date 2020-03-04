# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Sensors
GUID : d8900e18-36cb-4548-966f-13f068d1f78e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1001, version=0)
class Microsoft_Windows_Sensors_1001_0(Etw):
    pattern = Struct(
        "DeviceID" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1002, version=0)
class Microsoft_Windows_Sensors_1002_0(Etw):
    pattern = Struct(
        "DeviceID" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1003, version=0)
class Microsoft_Windows_Sensors_1003_0(Etw):
    pattern = Struct(
        "SensorType" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1004, version=0)
class Microsoft_Windows_Sensors_1004_0(Etw):
    pattern = Struct(
        "SensorType" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1005, version=0)
class Microsoft_Windows_Sensors_1005_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1006, version=0)
class Microsoft_Windows_Sensors_1006_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1007, version=0)
class Microsoft_Windows_Sensors_1007_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1008, version=0)
class Microsoft_Windows_Sensors_1008_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1009, version=0)
class Microsoft_Windows_Sensors_1009_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1010, version=0)
class Microsoft_Windows_Sensors_1010_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1011, version=0)
class Microsoft_Windows_Sensors_1011_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1012, version=0)
class Microsoft_Windows_Sensors_1012_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1013, version=0)
class Microsoft_Windows_Sensors_1013_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1014, version=0)
class Microsoft_Windows_Sensors_1014_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1015, version=0)
class Microsoft_Windows_Sensors_1015_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString,
        "Timestamp" / SystemTime,
        "NumSubscribers" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1016, version=0)
class Microsoft_Windows_Sensors_1016_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString,
        "SensorState" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1017, version=0)
class Microsoft_Windows_Sensors_1017_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString,
        "SensorState" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1100, version=0)
class Microsoft_Windows_Sensors_1100_0(Etw):
    pattern = Struct(
        "SENSOR_ID" / Guid,
        "Timestamp" / SystemTime
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1101, version=0)
class Microsoft_Windows_Sensors_1101_0(Etw):
    pattern = Struct(
        "SENSOR_ID" / Guid,
        "Timestamp" / SystemTime
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1102, version=0)
class Microsoft_Windows_Sensors_1102_0(Etw):
    pattern = Struct(
        "WorkingSet" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1103, version=0)
class Microsoft_Windows_Sensors_1103_0(Etw):
    pattern = Struct(
        "CPUUsage" / Float32l
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1104, version=0)
class Microsoft_Windows_Sensors_1104_0(Etw):
    pattern = Struct(
        "SENSOR_ID" / Guid,
        "Timestamp" / SystemTime,
        "HRESULT" / Int32ul,
        "ReportPointer" / Int64ul,
        "SensorStateThisSensor" / Int32ul,
        "SensorStateAccumulated" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1105, version=0)
class Microsoft_Windows_Sensors_1105_0(Etw):
    pattern = Struct(
        "QuadrantAngle" / Float32l
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1106, version=0)
class Microsoft_Windows_Sensors_1106_0(Etw):
    pattern = Struct(
        "SensorState" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1107, version=0)
class Microsoft_Windows_Sensors_1107_0(Etw):
    pattern = Struct(
        "AccelerationX" / Float32l,
        "AccelerationY" / Float32l,
        "AccelerationZ" / Float32l,
        "PitchCalibration" / Float32l
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1108, version=0)
class Microsoft_Windows_Sensors_1108_0(Etw):
    pattern = Struct(
        "IsPitchGreaterThanThreshold" / Int32ul,
        "PitchAngle" / Float32l,
        "PitchThreshold" / Float32l,
        "PitchCalibration" / Float32l
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1109, version=0)
class Microsoft_Windows_Sensors_1109_0(Etw):
    pattern = Struct(
        "Theta" / Float32l,
        "AngularCalibration" / Float32l
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1110, version=0)
class Microsoft_Windows_Sensors_1110_0(Etw):
    pattern = Struct(
        "Theta" / Float32l
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1111, version=0)
class Microsoft_Windows_Sensors_1111_0(Etw):
    pattern = Struct(
        "GoodAngle" / Int32ul,
        "Quadrant" / Int32ul,
        "LastQuadrant" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1112, version=0)
class Microsoft_Windows_Sensors_1112_0(Etw):
    pattern = Struct(
        "TimerQueueStatus" / Int32ul,
        "TimerQueueAction" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1113, version=0)
class Microsoft_Windows_Sensors_1113_0(Etw):
    pattern = Struct(
        "GoodAngle" / Int32ul,
        "Quadrant" / Int32ul,
        "LastQuadrant" / Int32ul,
        "Theta" / Float32l
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1114, version=0)
class Microsoft_Windows_Sensors_1114_0(Etw):
    pattern = Struct(
        "GoodAngle" / Int32ul,
        "Quadrant" / Int32ul,
        "AngularThreshold" / Float32l,
        "Theta" / Float32l
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1119, version=0)
class Microsoft_Windows_Sensors_1119_0(Etw):
    pattern = Struct(
        "QuadrantAngle" / Float32l
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1120, version=0)
class Microsoft_Windows_Sensors_1120_0(Etw):
    pattern = Struct(
        "QuadrantAngle" / Float32l
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1121, version=0)
class Microsoft_Windows_Sensors_1121_0(Etw):
    pattern = Struct(
        "SENSOR_ID" / Guid,
        "SensorState" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1122, version=0)
class Microsoft_Windows_Sensors_1122_0(Etw):
    pattern = Struct(
        "SENSOR_ID" / Guid,
        "SensorState" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1123, version=0)
class Microsoft_Windows_Sensors_1123_0(Etw):
    pattern = Struct(
        "SensorState" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1124, version=0)
class Microsoft_Windows_Sensors_1124_0(Etw):
    pattern = Struct(
        "SensorState" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1207, version=0)
class Microsoft_Windows_Sensors_1207_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1208, version=0)
class Microsoft_Windows_Sensors_1208_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1209, version=0)
class Microsoft_Windows_Sensors_1209_0(Etw):
    pattern = Struct(
        "EventNumber" / Int32ul,
        "EventCount" / Int32ul,
        "SENSOR_ID" / Guid,
        "ConnectedClients" / Int32ul,
        "SubscribedClients" / Int32ul,
        "SilentClients" / Int32ul,
        "PID" / Int32ul,
        "ClientBitfield" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1301, version=0)
class Microsoft_Windows_Sensors_1301_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString,
        "SENSOR_ID" / Guid,
        "Timestamp" / SystemTime
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1302, version=0)
class Microsoft_Windows_Sensors_1302_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString,
        "SENSOR_ID" / Guid,
        "Timestamp" / SystemTime
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1303, version=0)
class Microsoft_Windows_Sensors_1303_0(Etw):
    pattern = Struct(
        "SENSOR_ID" / Guid
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1304, version=0)
class Microsoft_Windows_Sensors_1304_0(Etw):
    pattern = Struct(
        "SENSOR_ID" / Guid
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1305, version=0)
class Microsoft_Windows_Sensors_1305_0(Etw):
    pattern = Struct(
        "SENSOR_ID" / Guid
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1306, version=0)
class Microsoft_Windows_Sensors_1306_0(Etw):
    pattern = Struct(
        "SENSOR_ID" / Guid
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1307, version=0)
class Microsoft_Windows_Sensors_1307_0(Etw):
    pattern = Struct(
        "SENSOR_ID" / Guid
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1308, version=0)
class Microsoft_Windows_Sensors_1308_0(Etw):
    pattern = Struct(
        "SENSOR_ID" / Guid
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1309, version=0)
class Microsoft_Windows_Sensors_1309_0(Etw):
    pattern = Struct(
        "SENSOR_ID" / Guid
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1310, version=0)
class Microsoft_Windows_Sensors_1310_0(Etw):
    pattern = Struct(
        "SENSOR_ID" / Guid
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1311, version=0)
class Microsoft_Windows_Sensors_1311_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString,
        "SENSOR_ID" / Guid,
        "SensorState" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1312, version=0)
class Microsoft_Windows_Sensors_1312_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString,
        "SENSOR_ID" / Guid,
        "SensorState" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1501, version=0)
class Microsoft_Windows_Sensors_1501_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString,
        "SENSOR_ID" / Guid
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1502, version=0)
class Microsoft_Windows_Sensors_1502_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString,
        "SENSOR_ID" / Guid
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1503, version=0)
class Microsoft_Windows_Sensors_1503_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString,
        "SENSOR_ID" / Guid
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1504, version=0)
class Microsoft_Windows_Sensors_1504_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString,
        "SENSOR_ID" / Guid
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1505, version=0)
class Microsoft_Windows_Sensors_1505_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString,
        "SENSOR_ID" / Guid
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1506, version=0)
class Microsoft_Windows_Sensors_1506_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString,
        "SENSOR_ID" / Guid
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1507, version=0)
class Microsoft_Windows_Sensors_1507_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString,
        "SENSOR_ID" / Guid
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1508, version=0)
class Microsoft_Windows_Sensors_1508_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString,
        "SENSOR_ID" / Guid
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1509, version=0)
class Microsoft_Windows_Sensors_1509_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString,
        "SENSOR_ID" / Guid,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1510, version=0)
class Microsoft_Windows_Sensors_1510_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString,
        "SENSOR_ID" / Guid,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1511, version=0)
class Microsoft_Windows_Sensors_1511_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString,
        "SENSOR_ID" / Guid,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=1512, version=0)
class Microsoft_Windows_Sensors_1512_0(Etw):
    pattern = Struct(
        "SensorObjectId" / WString,
        "SENSOR_ID" / Guid,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=3001, version=0)
class Microsoft_Windows_Sensors_3001_0(Etw):
    pattern = Struct(
        "GenericMessage" / WString
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=3002, version=0)
class Microsoft_Windows_Sensors_3002_0(Etw):
    pattern = Struct(
        "SENSOR_ID" / Guid,
        "MethodId" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=10001, version=0)
class Microsoft_Windows_Sensors_10001_0(Etw):
    pattern = Struct(
        "EventId" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=10002, version=0)
class Microsoft_Windows_Sensors_10002_0(Etw):
    pattern = Struct(
        "EventId" / Int32ul
    )


@declare(guid=guid("d8900e18-36cb-4548-966f-13f068d1f78e"), event_id=10003, version=0)
class Microsoft_Windows_Sensors_10003_0(Etw):
    pattern = Struct(
        "EventId" / Int32ul,
        "QuadrantChangeInterval" / Int32ul,
        "Angle" / Int32ul
    )

