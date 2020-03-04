# -*- coding: utf-8 -*-
"""
Microsoft-WindowsPhone-CoreUIComponents
GUID : a0b7550f-4e9a-4f03-ad41-b8042d06a2f7
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1000, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1000_0(Etw):
    pattern = Struct(
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1001, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1001_0(Etw):
    pattern = Struct(
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1200, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1200_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1201, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1201_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "navigationError" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1202, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1202_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1203, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1203_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "navigationError" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1204, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1204_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1205, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1205_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1206, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1206_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1207, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1207_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "appLayer" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1208, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1208_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1209, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1209_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1210, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1210_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1211, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1211_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "navigationError" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1212, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1212_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1213, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1213_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "appLayer" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1214, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1214_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "appLayer" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString,
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1215, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1215_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "appLayer" / Int32ul,
        "unParam2" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1216, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1216_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "appLayer" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1217, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1217_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "appLayer" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1218, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1218_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "appLayer" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1219, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1219_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1220, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1220_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString,
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1221, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1221_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1222, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1222_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1223, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1223_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1225, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1225_0(Etw):
    pattern = Struct(
        "ActivationPolicy" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1230, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1230_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "appLayer" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1231, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1231_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "appLayer" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1232, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1232_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1233, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1233_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1234, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1234_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul,
        "TaskCancellationType" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1235, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1235_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul,
        "TaskCancellationType" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1236, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1236_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1237, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1237_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1241, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1241_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "navigationError" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1243, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1243_0(Etw):
    pattern = Struct(
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1244, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1244_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1245, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1245_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "hex" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1247, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1247_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1248, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1248_0(Etw):
    pattern = Struct(
        "unParam" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1249, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1249_0(Etw):
    pattern = Struct(
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1250, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1250_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "taskDehydrationEligibility" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1251, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1251_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "appLayer" / Int32ul,
        "unParam2" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1252, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1252_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "appLayer" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1253, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1253_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "appLayer" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1254, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1254_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1255, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1255_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1256, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1256_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "hex" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1258, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1258_0(Etw):
    pattern = Struct(
        "fBool" / Int8ul,
        "navigationError" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1260, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1260_0(Etw):
    pattern = Struct(
        "animtype" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1261, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1261_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1262, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1262_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "taskProperty" / Int32ul,
        "unParam3" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1263, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1263_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1264, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1264_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "TaskRunningOptions" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1265, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1265_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1266, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1266_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1267, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1267_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1268, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1268_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1269, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1269_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "TaskInstanceState" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1271, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1271_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1272, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1272_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1273, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1273_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1281, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1281_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1282, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1282_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1283, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1283_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1301, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1301_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1302, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1302_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1303, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1303_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1304, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1304_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1305, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1305_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1306, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1306_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1307, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1307_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1311, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1311_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ptr" / Int64ul,
        "pwsz" / WString,
        "pwsz2" / WString,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1313, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1313_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ptr" / Int64ul,
        "pwsz" / WString,
        "pwsz2" / WString,
        "pwsz3" / WString,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1314, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1314_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString,
        "hex" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1315, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1315_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString,
        "hex" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1316, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1316_0(Etw):
    pattern = Struct(
        "unParam1" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1400, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1400_0(Etw):
    pattern = Struct(
        "ptr" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1402, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1402_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "pwsz2" / WString,
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1405, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1405_0(Etw):
    pattern = Struct(
        "SystemKey" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1406, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1406_0(Etw):
    pattern = Struct(
        "SystemKey" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1415, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1415_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1416, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1416_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1417, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1417_0(Etw):
    pattern = Struct(
        "status" / Int32ul,
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1418, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1418_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1419, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1419_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1420, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1420_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1421, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1421_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool1" / Int8ul,
        "fBool2" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1422, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1422_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul,
        "SessionManagerType" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1424, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1424_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "dir" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1425, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1425_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1426, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1426_0(Etw):
    pattern = Struct(
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1428, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1428_0(Etw):
    pattern = Struct(
        "SystemKey" / Int32ul,
        "ActivationLevel" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1429, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1429_0(Etw):
    pattern = Struct(
        "SystemKey" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1432, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1432_0(Etw):
    pattern = Struct(
        "fBool" / Int8ul,
        "fBool2" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1433, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1433_0(Etw):
    pattern = Struct(
        "fBool" / Int8ul,
        "fBool2" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1434, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1434_0(Etw):
    pattern = Struct(
        "fBool" / Int8ul,
        "fBool2" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1435, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1435_0(Etw):
    pattern = Struct(
        "fBool" / Int8ul,
        "fBool2" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1436, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1436_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1437, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1437_0(Etw):
    pattern = Struct(
        "SystemKey" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1450, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1450_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "pwsz2" / WString,
        "pwsz3" / WString,
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1451, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1451_0(Etw):
    pattern = Struct(
        "status" / Int32ul,
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1452, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1452_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1453, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1453_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "Param" / Int32sl
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1459, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1459_0(Etw):
    pattern = Struct(
        "LaunchType" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1460, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1460_0(Etw):
    pattern = Struct(
        "LaunchType" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1461, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1461_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1462, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1462_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1463, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1463_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1464, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1464_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1465, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1465_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "pwsz2" / WString,
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1466, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1466_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1467, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1467_0(Etw):
    pattern = Struct(
        "unParam1" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1468, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1468_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1469, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1469_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1470, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1470_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1471, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1471_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1472, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1472_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "navigationError" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1473, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1473_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1474, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1474_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1475, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1475_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1476, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1476_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1477, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1477_0(Etw):
    pattern = Struct(
        "Importance" / Int32ul,
        "PriorityCloseInitiated" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1501, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1501_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1502, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1502_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1504, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1504_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1505, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1505_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ServerTaskState" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1506, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1506_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ServerTaskState" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1507, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1507_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ServerTaskState" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1508, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1508_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ServerTaskState" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1509, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1509_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ServerTaskState" / Int32ul,
        "ServerTaskState2" / Int32ul,
        "bool1" / Int8ul,
        "bool2" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1510, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1510_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1511, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1511_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1512, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1512_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "SystemKey" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1514, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1514_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "SystemKey" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1515, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1515_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1516, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1516_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1517, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1517_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1518, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1518_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1519, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1519_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1520, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1520_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1521, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1521_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "reason" / Int32ul,
        "pwsz" / WString,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1522, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1522_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul,
        "fBool2" / Int8ul,
        "reason1" / Int32ul,
        "reason2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1523, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1523_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "dir" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1524, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1524_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "dir" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1525, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1525_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "dir" / Int32ul,
        "animtype" / Int32ul,
        "animflags" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1526, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1526_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "dir" / Int32ul,
        "animtype" / Int32ul,
        "animflags" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1527, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1527_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1528, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1528_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ServerTaskState" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1530, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1530_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ServerTaskState" / Int32ul,
        "ServerTaskState2" / Int32ul,
        "ServerTaskState3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1531, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1531_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ServerTaskState" / Int32ul,
        "ServerTaskState2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1532, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1532_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ServerTaskState1" / Int32ul,
        "ServerTaskState2" / Int32ul,
        "fBool" / Int8ul,
        "ActivationPolicy" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1533, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1533_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool1" / Int8ul,
        "fBool2" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1534, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1534_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool1" / Int8ul,
        "fBool2" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1535, version=1)
class Microsoft_WindowsPhone_CoreUIComponents_1535_1(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "NavigationTimeoutEventType" / Int32ul,
        "TimeoutModifierType" / Int32ul,
        "Param" / Int32sl,
        "ServerTaskState1" / Int32ul,
        "ServerTaskState2" / Int32ul,
        "IsModernApplication" / Int8ul,
        "ApplicationId" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1536, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1536_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "NavigationTimeoutEventType" / Int32ul,
        "ServerTaskState1" / Int32ul,
        "ServerTaskState2" / Int32ul,
        "reason" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1537, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1537_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "NavigationTimeoutEventType" / Int32ul,
        "TimeoutModifierType" / Int32ul,
        "ServerTaskState1" / Int32ul,
        "ServerTaskState2" / Int32ul,
        "fBool" / Int8ul,
        "fBool2" / Int8ul,
        "fBool3" / Int8ul,
        "fBool4" / Int8ul,
        "reason" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1538, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1538_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1541, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1541_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ptr" / Int64ul,
        "pwsz" / WString,
        "pwsz2" / WString,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1543, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1543_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ptr" / Int64ul,
        "pwsz" / WString,
        "pwsz2" / WString,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1544, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1544_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1545, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1545_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1546, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1546_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "NavigationTimeoutEventType" / Int32ul,
        "ServerTaskState1" / Int32ul,
        "ServerTaskState2" / Int32ul,
        "fBool" / Int8ul,
        "fBool2" / Int8ul,
        "fBool3" / Int8ul,
        "fBool4" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1547, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1547_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1548, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1548_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1549, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1549_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "NavigationTimeoutEventType" / Int32ul,
        "ServerTaskState1" / Int32ul,
        "ServerTaskState2" / Int32ul,
        "fBool" / Int8ul,
        "fBool2" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1550, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1550_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1551, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1551_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1552, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1552_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul,
        "fBool2" / Int8ul,
        "fBool3" / Int8ul,
        "fBool4" / Int8ul,
        "fBool5" / Int8ul,
        "pwsz1" / WString,
        "reason" / Int32ul,
        "pwsz2" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1553, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1553_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool1" / Int8ul,
        "fBool2" / Int8ul,
        "fBool3" / Int8ul,
        "fBool4" / Int8ul,
        "fBool5" / Int8ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1554, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1554_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1555, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1555_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ServerTaskState" / Int32ul,
        "ServerTaskState2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1556, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1556_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ServerTaskState" / Int32ul,
        "ServerTaskState2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1557, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1557_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ServerTaskState" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1558, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1558_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString,
        "fBool" / Int8ul,
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1559, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1559_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString,
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1560, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1560_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1561, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1561_0(Etw):
    pattern = Struct(
        "unParam1" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1562, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1562_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1563, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1563_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1564, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1564_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1565, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1565_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString,
        "fBool1" / Int8ul,
        "fBool2" / Int8ul,
        "fBool3" / Int8ul,
        "unParam2" / Int32ul,
        "pwsz2" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1566, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1566_0(Etw):
    pattern = Struct(
        "unParam1" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul,
        "unParam4" / Int32ul,
        "unParam5" / Int32ul,
        "unParam6" / Int32ul,
        "unParam7" / Int8ul,
        "unParam8" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1567, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1567_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1568, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1568_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1569, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1569_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1570, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1570_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1571, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1571_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1572, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1572_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1573, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1573_0(Etw):
    pattern = Struct(
        "unParam1" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul,
        "unParam4" / Int32ul,
        "unParam5" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1574, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1574_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1575, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1575_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "TaskRunningOptions" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1576, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1576_0(Etw):
    pattern = Struct(
        "unParam1" / Int32ul,
        "unParam2" / Int32sl,
        "unParam3" / Int32sl,
        "unParam4" / Int32sl,
        "unParam5" / Int32sl
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1577, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1577_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString,
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1578, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1578_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ServerTaskState1" / Int32ul,
        "ServerTaskState2" / Int32ul,
        "reason" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1579, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1579_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ServerTaskState1" / Int32ul,
        "ServerTaskState2" / Int32ul,
        "reason" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1580, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1580_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int64ul,
        "unParam3" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1581, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1581_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "TaskInstanceState" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1582, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1582_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ServerTaskState" / Int32ul,
        "ServerTaskState2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1583, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1583_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1584, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1584_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ServerTaskState" / Int32ul,
        "ServerTaskState2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1585, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1585_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1586, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1586_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1587, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1587_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1588, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1588_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1589, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1589_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString,
        "unParam2" / Int32sl
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1590, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1590_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1591, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1591_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1601, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1601_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1602, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1602_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1610, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1610_0(Etw):
    pattern = Struct(
        "ptr" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1611, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1611_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ptr" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1612, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1612_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1700, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1700_0(Etw):
    pattern = Struct(
        "ptr" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1702, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1702_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1703, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1703_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1800, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1800_0(Etw):
    pattern = Struct(
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1801, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1801_0(Etw):
    pattern = Struct(
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1802, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1802_0(Etw):
    pattern = Struct(
        "hex" / Int32ul,
        "hex2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1803, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1803_0(Etw):
    pattern = Struct(
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1804, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1804_0(Etw):
    pattern = Struct(
        "fBool" / Int8ul,
        "fBool2" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1805, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1805_0(Etw):
    pattern = Struct(
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1806, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1806_0(Etw):
    pattern = Struct(
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1807, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1807_0(Etw):
    pattern = Struct(
        "fBool" / Int8ul,
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1812, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1812_0(Etw):
    pattern = Struct(
        "hex" / Int32ul,
        "hex2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1814, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1814_0(Etw):
    pattern = Struct(
        "hex" / Int32ul,
        "hex2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1815, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1815_0(Etw):
    pattern = Struct(
        "hex" / Int32ul,
        "hex2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1816, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1816_0(Etw):
    pattern = Struct(
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1817, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1817_0(Etw):
    pattern = Struct(
        "fBool" / Int8ul,
        "hex" / Int32ul,
        "hex2" / Int32ul,
        "hex3" / Int32ul,
        "hex4" / Int32ul,
        "hex5" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1900, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1900_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1901, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1901_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1902, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1902_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1903, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1903_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1904, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1904_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1905, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1905_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1906, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1906_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1907, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1907_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "dir" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1908, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1908_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "dir" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1909, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1909_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "dir" / Int32ul,
        "animtype" / Int32ul,
        "animflags" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1910, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1910_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "dir" / Int32ul,
        "animtype" / Int32ul,
        "animflags" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1911, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1911_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1912, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1912_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1913, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1913_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1914, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1914_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1915, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1915_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1916, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1916_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1917, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1917_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool1" / Int8ul,
        "fBool2" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1918, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1918_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1919, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1919_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1920, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1920_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1921, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1921_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=1922, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_1922_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2000, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2000_0(Etw):
    pattern = Struct(
        "ptr" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2001, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2001_0(Etw):
    pattern = Struct(
        "ptr" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2100, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2100_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2101, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2101_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2102, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2102_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2103, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2103_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "dir" / Int32ul,
        "animtype" / Int32ul,
        "animflags" / Int32ul,
        "PageState" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2104, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2104_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "dir" / Int32ul,
        "animtype" / Int32ul,
        "animflags" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2105, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2105_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "dir" / Int32ul,
        "PageState" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2106, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2106_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2107, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2107_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2108, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2108_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2109, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2109_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2110, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2110_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "PMS" / Int32ul,
        "PMS2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2111, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2111_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "PMSS" / Int32ul,
        "PMSS2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2112, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2112_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2113, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2113_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "SystemKey" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2114, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2114_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2115, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2115_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2116, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2116_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "PMES" / Int32ul,
        "PMES2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2117, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2117_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "SystemKey" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2118, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2118_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2119, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2119_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2120, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2120_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2121, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2121_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2122, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2122_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "reason" / Int32ul,
        "pwsz" / WString,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2123, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2123_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2130, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2130_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2131, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2131_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool1" / Int8ul,
        "fBool2" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2132, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2132_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool1" / Int8ul,
        "fBool2" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2133, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2133_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2200, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2200_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2201, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2201_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2202, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2202_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "PageState" / Int32ul,
        "PageState2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2203, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2203_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2204, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2204_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2205, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2205_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2206, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2206_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2207, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2207_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2208, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2208_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "SystemKey" / Int32ul,
        "bool1" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2209, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2209_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "NavigationTimeoutEventType" / Int32ul,
        "PageState" / Int32ul,
        "PageState2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2210, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2210_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "NavigationTimeoutEventType" / Int32ul,
        "PageState" / Int32ul,
        "PageState2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2211, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2211_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "NavigationTimeoutEventType" / Int32ul,
        "PageState" / Int32ul,
        "PageState2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2212, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2212_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2213, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2213_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2214, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2214_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "PageState" / Int32ul,
        "PageState2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2215, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2215_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2301, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2301_0(Etw):
    pattern = Struct(
        "ptr" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2302, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2302_0(Etw):
    pattern = Struct(
        "ptr" / Int64ul,
        "EMCRET" / Int32ul,
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2303, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2303_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2304, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2304_0(Etw):
    pattern = Struct(
        "ptr" / Int64ul,
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2313, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2313_0(Etw):
    pattern = Struct(
        "ptr" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2318, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2318_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2320, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2320_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2322, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2322_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2324, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2324_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2326, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2326_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2328, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2328_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2330, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2330_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2401, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2401_0(Etw):
    pattern = Struct(
        "ptr" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2402, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2402_0(Etw):
    pattern = Struct(
        "ptr" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2404, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2404_0(Etw):
    pattern = Struct(
        "ptr" / Int64ul,
        "fBool" / Int8ul,
        "fBool2" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2412, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2412_0(Etw):
    pattern = Struct(
        "ptr" / Int64ul,
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2420, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2420_0(Etw):
    pattern = Struct(
        "ptr" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2422, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2422_0(Etw):
    pattern = Struct(
        "ptr" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2424, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2424_0(Etw):
    pattern = Struct(
        "ptr" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2426, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2426_0(Etw):
    pattern = Struct(
        "ptr" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2501, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2501_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2502, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2502_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2504, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2504_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2510, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2510_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2511, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2511_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2520, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2520_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2521, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2521_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2522, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2522_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2523, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2523_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2524, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2524_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2525, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2525_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2526, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2526_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2527, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2527_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2528, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2528_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2531, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2531_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2532, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2532_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2533, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2533_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2534, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2534_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2535, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2535_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2536, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2536_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2537, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2537_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2538, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2538_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2539, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2539_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2540, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2540_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2541, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2541_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2542, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2542_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2543, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2543_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2544, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2544_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString,
        "unParam2" / Int32sl
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2800, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2800_0(Etw):
    pattern = Struct(
        "fBool1" / Int8ul,
        "fBool2" / Int8ul,
        "fBool3" / Int8ul,
        "Param" / Int32sl
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2802, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2802_0(Etw):
    pattern = Struct(
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2803, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2803_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2804, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2804_0(Etw):
    pattern = Struct(
        "Param" / Int32sl,
        "Param2" / Int32sl,
        "Param3" / Int32sl,
        "Param4" / Int32sl,
        "Param5" / Int32sl,
        "Param6" / Int32sl,
        "Param7" / Int32sl
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2900, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2900_0(Etw):
    pattern = Struct(
        "coreUIServiceType" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2901, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2901_0(Etw):
    pattern = Struct(
        "coreUIServiceType" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2902, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2902_0(Etw):
    pattern = Struct(
        "coreUIServiceType" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2903, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2903_0(Etw):
    pattern = Struct(
        "coreUIServiceType" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2904, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2904_0(Etw):
    pattern = Struct(
        "coreUIServiceType" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2905, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2905_0(Etw):
    pattern = Struct(
        "coreUIServiceType" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2906, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2906_0(Etw):
    pattern = Struct(
        "coreUIServiceType" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2907, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2907_0(Etw):
    pattern = Struct(
        "coreUIServiceType" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=2908, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_2908_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=5000, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_5000_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=5001, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_5001_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=5004, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_5004_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=5005, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_5005_0(Etw):
    pattern = Struct(
        "hex" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=5006, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_5006_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=5007, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_5007_0(Etw):
    pattern = Struct(
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=5008, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_5008_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=5010, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_5010_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=5012, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_5012_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=5050, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_5050_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=5052, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_5052_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=5054, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_5054_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=6000, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_6000_0(Etw):
    pattern = Struct(
        "hex" / Int32ul,
        "unParam" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString,
        "unParam2" / Int32ul,
        "pwsz3" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=6001, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_6001_0(Etw):
    pattern = Struct(
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=6002, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_6002_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "pwsz2" / WString,
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=6003, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_6003_0(Etw):
    pattern = Struct(
        "hex" / Int32ul,
        "unParam" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString,
        "unParam2" / Int32ul,
        "pwsz3" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=6004, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_6004_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=6005, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_6005_0(Etw):
    pattern = Struct(
        "hex" / Int32ul,
        "unParam" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString,
        "pwsz3" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7000, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7000_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7001, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7001_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7002, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7002_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7003, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7003_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7004, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7004_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7005, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7005_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7006, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7006_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7007, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7007_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7008, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7008_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7009, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7009_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7010, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7010_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7011, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7011_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "dir" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7012, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7012_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7013, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7013_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "dir" / Int32ul,
        "animtype" / Int32ul,
        "animflags" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7014, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7014_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7015, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7015_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7016, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7016_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7017, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7017_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7018, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7018_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7019, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7019_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7020, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7020_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7021, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7021_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7022, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7022_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7023, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7023_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7024, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7024_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7025, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7025_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7026, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7026_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7027, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7027_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7028, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7028_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7029, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7029_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7030, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7030_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7031, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7031_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7032, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7032_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7033, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7033_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7034, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7034_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7035, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7035_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7036, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7036_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "dir" / Int32ul,
        "animtype" / Int32ul,
        "animflags" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7037, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7037_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "dir" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7038, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7038_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7039, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7039_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "SystemKey" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7040, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7040_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7041, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7041_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7042, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7042_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "newstate" / Int32ul,
        "oldstate" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7044, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7044_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7045, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7045_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7046, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7046_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7047, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7047_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7048, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7048_0(Etw):
    pattern = Struct(
        "CurrentState" / Int8ul,
        "NewSipVisibilityValue" / Int8ul,
        "SipHeight" / Int64ul,
        "NavClientState" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7049, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7049_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7050, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7050_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7051, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7051_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7052, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7052_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7053, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7053_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7054, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7054_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7055, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7055_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7056, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7056_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7057, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7057_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7058, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7058_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7059, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7059_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7060, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7060_0(Etw):
    pattern = Struct(
        "unParam1" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul,
        "unParam4" / Int32ul,
        "unParam5" / Int32ul,
        "unParam6" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7061, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7061_0(Etw):
    pattern = Struct(
        "unParam1" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul,
        "unParam4" / Int32ul,
        "unParam5" / Int32ul,
        "unParam6" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7062, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7062_0(Etw):
    pattern = Struct(
        "unParam1" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul,
        "unParam4" / Int32ul,
        "unParam5" / Int32ul,
        "unParam6" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7063, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7063_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul,
        "unParam4" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7064, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7064_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "Occlusion" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=7065, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_7065_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8000, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8000_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8001, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8001_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8002, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8002_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul,
        "unParam4" / Int32ul,
        "unParam5" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8003, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8003_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul,
        "unParam4" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8004, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8004_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul,
        "unParam4" / Int32ul,
        "unParam5" / Int32ul,
        "unParam6" / Int32ul,
        "unParam7" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8005, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8005_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8006, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8006_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "activationLevel1" / Int32ul,
        "activationLevel2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8007, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8007_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8008, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8008_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8009, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8009_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8010, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8010_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul,
        "reason" / Int32ul,
        "dir1" / Int32ul,
        "dir2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8011, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8011_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8012, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8012_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8013, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8013_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8014, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8014_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul,
        "unParam4" / Int32ul,
        "unParam5" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8015, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8015_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul,
        "unParam4" / Int32ul,
        "unParam5" / Int32ul,
        "unParam6" / Int32ul,
        "unParam7" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8016, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8016_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8017, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8017_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul,
        "ServerTaskState" / Int32ul,
        "dir" / Int32ul,
        "animtype" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8018, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8018_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8019, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8019_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8020, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8020_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8021, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8021_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8022, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8022_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8023, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8023_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul,
        "currentState" / Int32ul,
        "targetState" / Int32ul,
        "direction" / Int32ul,
        "reason" / Int32ul,
        "pwsz" / WString,
        "firstActivation" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8100, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8100_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul,
        "unParam4" / Int32ul,
        "unParam5" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8101, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8101_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul,
        "dir" / Int32ul,
        "animtype" / Int32ul,
        "animflags" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8102, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8102_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul,
        "dir" / Int32ul,
        "animtype" / Int32ul,
        "animflags" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8103, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8103_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8104, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8104_0(Etw):
    pattern = Struct(
        "appLayer" / Int32ul,
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8105, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8105_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=8106, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_8106_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9000, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9000_0(Etw):
    pattern = Struct(
        "ptr" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9002, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9002_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ViewNavigationLevel" / Int32ul,
        "AnimationDirection" / Int32ul,
        "AnimationType" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9003, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9003_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul,
        "fBool2" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9004, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9004_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul,
        "fBool2" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9007, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9007_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9008, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9008_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9009, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9009_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9010, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9010_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9011, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9011_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9012, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9012_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9013, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9013_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9014, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9014_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9015, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9015_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul,
        "unParam4" / Int64ul,
        "unParam5" / Int64ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9016, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9016_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9017, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9017_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul,
        "dir" / Int32ul,
        "animtype" / Int32ul,
        "animflags" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9018, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9018_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "SystemKey" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9019, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9019_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "SystemKey" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9020, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9020_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ViewNavigationLevel" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9021, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9021_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9022, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9022_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9023, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9023_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "navigationError" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9024, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9024_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9025, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9025_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "fBool" / Int8ul,
        "fBool2" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9026, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9026_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "fBool" / Int8ul,
        "fBool2" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9027, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9027_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9028, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9028_0(Etw):
    pattern = Struct(
        "unParam1" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9029, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9029_0(Etw):
    pattern = Struct(
        "pwsz1" / WString,
        "pwsz2" / WString,
        "pwsz3" / WString,
        "ViewActivationFlags" / Int32ul,
        "pwsz4" / WString,
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9030, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9030_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "ViewNavigationLevel" / Int32ul,
        "AnimationDirection" / Int32ul,
        "AnimationType" / Int32ul,
        "fBool" / Int8ul,
        "fBool2" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9031, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9031_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "ViewNavigationLevel" / Int32ul,
        "AnimationDirection" / Int32ul,
        "AnimationType" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9032, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9032_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9033, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9033_0(Etw):
    pattern = Struct(
        "unParam" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9034, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9034_0(Etw):
    pattern = Struct(
        "unParam" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9035, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9035_0(Etw):
    pattern = Struct(
        "Param" / Int32sl,
        "Param2" / Int32sl,
        "navigationError" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9036, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9036_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9037, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9037_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9038, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9038_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9039, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9039_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9040, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9040_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9041, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9041_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "ViewNavigationLevel" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9042, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9042_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9043, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9043_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9044, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9044_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9045, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9045_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9500, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9500_0(Etw):
    pattern = Struct(
        "hex" / Int32ul,
        "unParam" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString,
        "ViewActivationFlags" / Int32ul,
        "un64Param" / Int64ul,
        "un64Param2" / Int64ul,
        "un64Param3" / Int64ul,
        "un64Param4" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9501, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9501_0(Etw):
    pattern = Struct(
        "unParam1" / Int32ul,
        "unParam2" / Int64ul,
        "unParam3" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9502, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9502_0(Etw):
    pattern = Struct(
        "hex" / Int32ul,
        "unParam" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString,
        "pwsz3" / WString,
        "ViewActivationFlags" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9503, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9503_0(Etw):
    pattern = Struct(
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9504, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9504_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "pwsz2" / WString,
        "pwsz3" / WString,
        "AnimationType" / Int32ul,
        "AnimationType2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9505, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9505_0(Etw):
    pattern = Struct(
        "hex" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9506, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9506_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul,
        "hex" / Int32ul,
        "reason" / Int32ul,
        "pwsz" / WString,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9507, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9507_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "pwsz2" / WString,
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9508, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9508_0(Etw):
    pattern = Struct(
        "hex" / Int32ul,
        "unParam" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString,
        "unParam2" / Int32ul,
        "pwsz3" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9509, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9509_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9510, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9510_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9511, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9511_0(Etw):
    pattern = Struct(
        "fBool" / Int8ul,
        "unParam1" / Int32ul,
        "unParam2" / Int32ul,
        "hex" / Int32ul,
        "reason" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9513, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9513_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9514, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9514_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int64ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9515, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9515_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9601, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9601_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9602, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9602_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9603, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9603_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9604, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9604_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9605, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9605_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9606, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9606_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9607, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9607_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9608, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9608_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9700, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9700_0(Etw):
    pattern = Struct(
        "hex" / Int32ul,
        "unParam" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString,
        "pwsz3" / WString,
        "ViewActivationFlags" / Int32ul,
        "pwsz4" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9701, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9701_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9702, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9702_0(Etw):
    pattern = Struct(
        "hex1" / Int32ul,
        "unParam" / Int32ul,
        "pwsz" / WString,
        "pwsz2" / WString,
        "pwsz3" / WString,
        "ViewActivationFlags" / Int32ul,
        "pwsz4" / WString,
        "hex2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9703, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9703_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9704, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9704_0(Etw):
    pattern = Struct(
        "unParam1" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul,
        "unParam4" / Int8ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9705, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9705_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9706, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9706_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9707, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9707_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=9708, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_9708_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "pwsz" / WString
    )


@declare(guid=guid("a0b7550f-4e9a-4f03-ad41-b8042d06a2f7"), event_id=20000, version=0)
class Microsoft_WindowsPhone_CoreUIComponents_20000_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "hex" / Int32ul,
        "pwsz2" / WString
    )

