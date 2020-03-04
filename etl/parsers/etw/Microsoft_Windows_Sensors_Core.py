# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Sensors-Core
GUID : 751c292b-23e6-58cf-1fd4-38f8512c66c2
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1001, version=0)
class Microsoft_Windows_Sensors_Core_1001_0(Etw):
    pattern = Struct(
        "WdfDeviceInit" / Int64ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1002, version=0)
class Microsoft_Windows_Sensors_Core_1002_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1003, version=0)
class Microsoft_Windows_Sensors_Core_1003_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "IsStateChangeSupported" / Int8ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1004, version=0)
class Microsoft_Windows_Sensors_Core_1004_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "IsDriverPowerPolicyOwner" / Int8ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1005, version=0)
class Microsoft_Windows_Sensors_Core_1005_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "SensorType" / Guid,
        "PersistentUniqueID" / Guid
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1006, version=0)
class Microsoft_Windows_Sensors_Core_1006_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "VendorDefinedSubType" / Guid,
        "PersistentUniqueID" / Guid
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1007, version=0)
class Microsoft_Windows_Sensors_Core_1007_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "PersistentUniqueID" / Guid
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1008, version=0)
class Microsoft_Windows_Sensors_Core_1008_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "SensorType" / Guid,
        "PersistentUniqueID" / Guid
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1009, version=0)
class Microsoft_Windows_Sensors_Core_1009_0(Etw):
    pattern = Struct(
        "SENSOROBJECT" / Int64ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1010, version=0)
class Microsoft_Windows_Sensors_Core_1010_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "FmtId" / Guid,
        "Pid" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1011, version=0)
class Microsoft_Windows_Sensors_Core_1011_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "IntervalMs" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1012, version=0)
class Microsoft_Windows_Sensors_Core_1012_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "IntervalMs" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1013, version=0)
class Microsoft_Windows_Sensors_Core_1013_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "MaxDataSize" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1014, version=0)
class Microsoft_Windows_Sensors_Core_1014_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "MaxDataSize" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1015, version=0)
class Microsoft_Windows_Sensors_Core_1015_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "BatchSize" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1019, version=0)
class Microsoft_Windows_Sensors_Core_1019_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "pIntervalMs" / Int64ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1020, version=0)
class Microsoft_Windows_Sensors_Core_1020_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "IntervalMs" / Int32ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1021, version=0)
class Microsoft_Windows_Sensors_Core_1021_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "pThresholds" / Int64ul,
        "pSize" / Int64ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1022, version=0)
class Microsoft_Windows_Sensors_Core_1022_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "pThresholds" / Int64ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1023, version=0)
class Microsoft_Windows_Sensors_Core_1023_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "pProperties" / Int64ul,
        "pSize" / Int64ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1024, version=0)
class Microsoft_Windows_Sensors_Core_1024_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "pProperties" / Int64ul,
        "pSize" / Int64ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1025, version=0)
class Microsoft_Windows_Sensors_Core_1025_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "pDatafield" / Int64ul,
        "pProperties" / Int64ul,
        "pSize" / Int64ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1026, version=0)
class Microsoft_Windows_Sensors_Core_1026_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1027, version=0)
class Microsoft_Windows_Sensors_Core_1027_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1028, version=0)
class Microsoft_Windows_Sensors_Core_1028_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1029, version=0)
class Microsoft_Windows_Sensors_Core_1029_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1030, version=0)
class Microsoft_Windows_Sensors_Core_1030_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "pHistoryCollection" / Int64ul,
        "Size" / Int32ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1031, version=0)
class Microsoft_Windows_Sensors_Core_1031_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "pBytesWritten" / Int64ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1032, version=0)
class Microsoft_Windows_Sensors_Core_1032_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1033, version=0)
class Microsoft_Windows_Sensors_Core_1033_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "ReportLatencyMs" / Int32ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1034, version=0)
class Microsoft_Windows_Sensors_Core_1034_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1035, version=0)
class Microsoft_Windows_Sensors_Core_1035_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1036, version=0)
class Microsoft_Windows_Sensors_Core_1036_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SENSOROBJECT" / Int64ul,
        "Type" / Guid,
        "Category" / Guid,
        "SubType" / Guid,
        "PeristentUniqueId" / Guid,
        "Name" / WString,
        "Model" / WString,
        "Manufacturer" / WString
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1100, version=0)
class Microsoft_Windows_Sensors_Core_1100_0(Etw):
    pattern = Struct(
        "PeristentUniqueId" / Guid,
        "ProcessId" / Int32ul,
        "ReportIntervalMs" / Int32ul,
        "ReportLatencyMs" / Int32ul,
        "IsStreaming" / Int8ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1101, version=0)
class Microsoft_Windows_Sensors_Core_1101_0(Etw):
    pattern = Struct(
        "Interface" / WString
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1102, version=0)
class Microsoft_Windows_Sensors_Core_1102_0(Etw):
    pattern = Struct(
        "Interface" / WString
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1103, version=0)
class Microsoft_Windows_Sensors_Core_1103_0(Etw):
    pattern = Struct(
        "Interface" / WString
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1104, version=0)
class Microsoft_Windows_Sensors_Core_1104_0(Etw):
    pattern = Struct(
        "Interface" / WString
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1105, version=0)
class Microsoft_Windows_Sensors_Core_1105_0(Etw):
    pattern = Struct(
        "Interface" / WString,
        "PowerUsage" / Float32l
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1106, version=0)
class Microsoft_Windows_Sensors_Core_1106_0(Etw):
    pattern = Struct(
        "Interface" / WString
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1107, version=0)
class Microsoft_Windows_Sensors_Core_1107_0(Etw):
    pattern = Struct(
        "Interface" / WString
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1108, version=0)
class Microsoft_Windows_Sensors_Core_1108_0(Etw):
    pattern = Struct(
        "Interface" / WString
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1200, version=0)
class Microsoft_Windows_Sensors_Core_1200_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "Usage" / Int16ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1201, version=0)
class Microsoft_Windows_Sensors_Core_1201_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "Usage" / Int16ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1202, version=0)
class Microsoft_Windows_Sensors_Core_1202_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportIdInCaps" / Int8ul,
        "ReportIdInReport" / Int8ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1203, version=0)
class Microsoft_Windows_Sensors_Core_1203_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportId" / Int8ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1204, version=0)
class Microsoft_Windows_Sensors_Core_1204_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportId" / Int8ul,
        "Usage" / Int16ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1205, version=0)
class Microsoft_Windows_Sensors_Core_1205_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportId" / Int8ul,
        "Usage" / Int16ul,
        "fmtid" / Guid,
        "pid" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1206, version=0)
class Microsoft_Windows_Sensors_Core_1206_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportId" / Int8ul,
        "Usage" / Int16ul,
        "fmtid" / Guid,
        "pid" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1207, version=0)
class Microsoft_Windows_Sensors_Core_1207_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportId" / Int8ul,
        "Usage" / Int16ul,
        "fmtid" / Guid,
        "pid" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1208, version=0)
class Microsoft_Windows_Sensors_Core_1208_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportId" / Int8ul,
        "BitSize" / Int16ul,
        "ExpectedBitSize" / Int16ul,
        "ReportCount" / Int16ul,
        "ExpectedReportCount" / Int16ul,
        "Exponent" / Int16ul,
        "ExpectedExponent" / Int16ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1209, version=0)
class Microsoft_Windows_Sensors_Core_1209_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportId" / Int8ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1210, version=0)
class Microsoft_Windows_Sensors_Core_1210_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportId" / Int8ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1211, version=0)
class Microsoft_Windows_Sensors_Core_1211_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportId" / Int8ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1212, version=0)
class Microsoft_Windows_Sensors_Core_1212_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportId" / Int8ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1213, version=0)
class Microsoft_Windows_Sensors_Core_1213_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportId" / Int8ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1214, version=0)
class Microsoft_Windows_Sensors_Core_1214_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportId" / Int8ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1215, version=0)
class Microsoft_Windows_Sensors_Core_1215_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportId" / Int8ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1216, version=0)
class Microsoft_Windows_Sensors_Core_1216_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportId" / Int8ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1217, version=0)
class Microsoft_Windows_Sensors_Core_1217_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportId" / Int8ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1218, version=0)
class Microsoft_Windows_Sensors_Core_1218_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportId" / Int8ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1219, version=0)
class Microsoft_Windows_Sensors_Core_1219_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportId" / Int8ul,
        "IsWakeReportingStateSupported" / Int8ul,
        "IsWakePowerStateSupported" / Int8ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1220, version=0)
class Microsoft_Windows_Sensors_Core_1220_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "ReportIdInReport" / Int8ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1221, version=0)
class Microsoft_Windows_Sensors_Core_1221_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportId" / Int8ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1222, version=0)
class Microsoft_Windows_Sensors_Core_1222_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportId" / Int8ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1223, version=0)
class Microsoft_Windows_Sensors_Core_1223_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportId" / Int8ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1224, version=0)
class Microsoft_Windows_Sensors_Core_1224_0(Etw):
    pattern = Struct(
        "WdfDevice" / Int64ul,
        "SensorUsage" / Int16ul,
        "ReportId" / Int8ul
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1300, version=0)
class Microsoft_Windows_Sensors_Core_1300_0(Etw):
    pattern = Struct(
        "Interface" / WString
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1301, version=0)
class Microsoft_Windows_Sensors_Core_1301_0(Etw):
    pattern = Struct(
        "Interface" / WString
    )


@declare(guid=guid("751c292b-23e6-58cf-1fd4-38f8512c66c2"), event_id=1302, version=0)
class Microsoft_Windows_Sensors_Core_1302_0(Etw):
    pattern = Struct(
        "Interface" / WString
    )

