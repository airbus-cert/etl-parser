# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Biometrics
GUID : a0e3d8ea-c34f-4419-a1db-90435b8b21d0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1000, version=0)
class Microsoft_Windows_Biometrics_1000_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "SID" / WString,
        "Username" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1001, version=0)
class Microsoft_Windows_Biometrics_1001_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "SID" / WString,
        "Username" / WString
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1002, version=0)
class Microsoft_Windows_Biometrics_1002_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "SID" / WString,
        "Username" / WString
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1003, version=0)
class Microsoft_Windows_Biometrics_1003_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1004, version=0)
class Microsoft_Windows_Biometrics_1004_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "SID" / WString,
        "Username" / WString
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1005, version=0)
class Microsoft_Windows_Biometrics_1005_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1006, version=0)
class Microsoft_Windows_Biometrics_1006_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1007, version=0)
class Microsoft_Windows_Biometrics_1007_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1008, version=0)
class Microsoft_Windows_Biometrics_1008_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1009, version=0)
class Microsoft_Windows_Biometrics_1009_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "SID" / WString,
        "Username" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1010, version=0)
class Microsoft_Windows_Biometrics_1010_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "SID" / WString,
        "Username" / WString
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1011, version=0)
class Microsoft_Windows_Biometrics_1011_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1012, version=0)
class Microsoft_Windows_Biometrics_1012_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "ErrorCode" / Int32ul,
        "RejectDetail" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1013, version=0)
class Microsoft_Windows_Biometrics_1013_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1014, version=0)
class Microsoft_Windows_Biometrics_1014_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "SID" / WString,
        "Username" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1015, version=0)
class Microsoft_Windows_Biometrics_1015_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "SID" / WString,
        "Username" / WString
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1016, version=0)
class Microsoft_Windows_Biometrics_1016_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "Component" / Int32ul,
        "ControlCode" / Int32ul,
        "OperationStatus" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1017, version=0)
class Microsoft_Windows_Biometrics_1017_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "Component" / Int32ul,
        "ControlCode" / Int32ul,
        "OperationStatus" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1018, version=0)
class Microsoft_Windows_Biometrics_1018_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "Component" / Int32ul,
        "ControlCode" / Int32ul,
        "OperationStatus" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1019, version=0)
class Microsoft_Windows_Biometrics_1019_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "Component" / Int32ul,
        "ControlCode" / Int32ul,
        "OperationStatus" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1100, version=0)
class Microsoft_Windows_Biometrics_1100_0(Etw):
    pattern = Struct(
        "ModulePath" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1101, version=0)
class Microsoft_Windows_Biometrics_1101_0(Etw):
    pattern = Struct(
        "ModulePath" / WString
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1102, version=0)
class Microsoft_Windows_Biometrics_1102_0(Etw):
    pattern = Struct(
        "ModulePath" / WString,
        "Component" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1103, version=0)
class Microsoft_Windows_Biometrics_1103_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1104, version=0)
class Microsoft_Windows_Biometrics_1104_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1105, version=0)
class Microsoft_Windows_Biometrics_1105_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "Component" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1106, version=0)
class Microsoft_Windows_Biometrics_1106_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1107, version=0)
class Microsoft_Windows_Biometrics_1107_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1108, version=0)
class Microsoft_Windows_Biometrics_1108_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1109, version=0)
class Microsoft_Windows_Biometrics_1109_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1110, version=0)
class Microsoft_Windows_Biometrics_1110_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1111, version=0)
class Microsoft_Windows_Biometrics_1111_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1112, version=0)
class Microsoft_Windows_Biometrics_1112_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "Component" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1113, version=0)
class Microsoft_Windows_Biometrics_1113_0(Etw):
    pattern = Struct(
        "ModulePath" / WString
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1114, version=0)
class Microsoft_Windows_Biometrics_1114_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "SensorAdapter" / WString,
        "EngineAdapter" / WString,
        "StorageAdapter" / WString,
        "DatabaseID" / Guid,
        "SensorMode" / Int32ul,
        "SensorPool" / Int32ul,
        "IsolationLevel" / Int32ul,
        "IsolationSensorAdapter" / WString,
        "IsolationEngineAdapter" / WString,
        "IsolationStorageAdapter" / WString,
        "Component" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1400, version=0)
class Microsoft_Windows_Biometrics_1400_0(Etw):
    pattern = Struct(
        "Username" / WString
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1401, version=0)
class Microsoft_Windows_Biometrics_1401_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1402, version=0)
class Microsoft_Windows_Biometrics_1402_0(Etw):
    pattern = Struct(
        "Username" / WString
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1403, version=0)
class Microsoft_Windows_Biometrics_1403_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1500, version=0)
class Microsoft_Windows_Biometrics_1500_0(Etw):
    pattern = Struct(
        "SID" / WString,
        "Username" / WString
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1501, version=0)
class Microsoft_Windows_Biometrics_1501_0(Etw):
    pattern = Struct(
        "SID" / WString,
        "Username" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1503, version=0)
class Microsoft_Windows_Biometrics_1503_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1504, version=0)
class Microsoft_Windows_Biometrics_1504_0(Etw):
    pattern = Struct(
        "SID" / WString,
        "Username" / WString
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1505, version=0)
class Microsoft_Windows_Biometrics_1505_0(Etw):
    pattern = Struct(
        "SID" / WString,
        "Username" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1507, version=0)
class Microsoft_Windows_Biometrics_1507_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1508, version=0)
class Microsoft_Windows_Biometrics_1508_0(Etw):
    pattern = Struct(
        "SID" / WString,
        "Username" / WString
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1509, version=0)
class Microsoft_Windows_Biometrics_1509_0(Etw):
    pattern = Struct(
        "SID" / WString,
        "Username" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1511, version=0)
class Microsoft_Windows_Biometrics_1511_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1512, version=0)
class Microsoft_Windows_Biometrics_1512_0(Etw):
    pattern = Struct(
        "SID" / WString,
        "Username" / WString
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1513, version=0)
class Microsoft_Windows_Biometrics_1513_0(Etw):
    pattern = Struct(
        "SID" / WString,
        "Username" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1515, version=0)
class Microsoft_Windows_Biometrics_1515_0(Etw):
    pattern = Struct(
        "SID" / WString,
        "Username" / WString
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1516, version=0)
class Microsoft_Windows_Biometrics_1516_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1600, version=0)
class Microsoft_Windows_Biometrics_1600_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1605, version=0)
class Microsoft_Windows_Biometrics_1605_0(Etw):
    pattern = Struct(
        "SID" / WString,
        "Username" / WString
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1606, version=0)
class Microsoft_Windows_Biometrics_1606_0(Etw):
    pattern = Struct(
        "SID" / WString,
        "Username" / WString
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1607, version=0)
class Microsoft_Windows_Biometrics_1607_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1608, version=0)
class Microsoft_Windows_Biometrics_1608_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1609, version=0)
class Microsoft_Windows_Biometrics_1609_0(Etw):
    pattern = Struct(
        "BiometricSensor" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1700, version=0)
class Microsoft_Windows_Biometrics_1700_0(Etw):
    pattern = Struct(
        "SID" / WString,
        "Username" / WString,
        "Type" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1701, version=0)
class Microsoft_Windows_Biometrics_1701_0(Etw):
    pattern = Struct(
        "SID" / WString,
        "Username" / WString,
        "Type" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1702, version=0)
class Microsoft_Windows_Biometrics_1702_0(Etw):
    pattern = Struct(
        "SID" / WString,
        "Username" / WString,
        "Type" / Int32ul
    )


@declare(guid=guid("a0e3d8ea-c34f-4419-a1db-90435b8b21d0"), event_id=1703, version=0)
class Microsoft_Windows_Biometrics_1703_0(Etw):
    pattern = Struct(
        "SID" / WString,
        "Username" / WString,
        "Type" / Int32ul,
        "ErrorCode" / Int32ul
    )

