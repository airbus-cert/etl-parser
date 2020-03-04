# -*- coding: utf-8 -*-
"""
Microsoft-Windows-StartupRepair
GUID : c914f0df-835a-4a22-8c70-732c9a80c634
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1001, version=0)
class Microsoft_Windows_StartupRepair_1001_0(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "EndTime" / Int64ul,
        "NumAttempts" / Int16ul,
        "NumRootCauses" / Int16ul,
        "LaunchType" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1002, version=0)
class Microsoft_Windows_StartupRepair_1002_0(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "EndTime" / Int64ul,
        "NumAttempts" / Int16ul,
        "NumRootCauses" / Int16ul,
        "LaunchType" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1101, version=0)
class Microsoft_Windows_StartupRepair_1101_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1102, version=0)
class Microsoft_Windows_StartupRepair_1102_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1103, version=0)
class Microsoft_Windows_StartupRepair_1103_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1104, version=0)
class Microsoft_Windows_StartupRepair_1104_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1105, version=0)
class Microsoft_Windows_StartupRepair_1105_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1106, version=0)
class Microsoft_Windows_StartupRepair_1106_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1107, version=0)
class Microsoft_Windows_StartupRepair_1107_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1108, version=0)
class Microsoft_Windows_StartupRepair_1108_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1109, version=0)
class Microsoft_Windows_StartupRepair_1109_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1110, version=0)
class Microsoft_Windows_StartupRepair_1110_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1112, version=0)
class Microsoft_Windows_StartupRepair_1112_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1113, version=0)
class Microsoft_Windows_StartupRepair_1113_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1114, version=0)
class Microsoft_Windows_StartupRepair_1114_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1115, version=0)
class Microsoft_Windows_StartupRepair_1115_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1116, version=0)
class Microsoft_Windows_StartupRepair_1116_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1117, version=0)
class Microsoft_Windows_StartupRepair_1117_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1118, version=0)
class Microsoft_Windows_StartupRepair_1118_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1119, version=0)
class Microsoft_Windows_StartupRepair_1119_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1120, version=0)
class Microsoft_Windows_StartupRepair_1120_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1121, version=0)
class Microsoft_Windows_StartupRepair_1121_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1122, version=0)
class Microsoft_Windows_StartupRepair_1122_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1123, version=0)
class Microsoft_Windows_StartupRepair_1123_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1124, version=0)
class Microsoft_Windows_StartupRepair_1124_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1125, version=0)
class Microsoft_Windows_StartupRepair_1125_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1126, version=0)
class Microsoft_Windows_StartupRepair_1126_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1127, version=0)
class Microsoft_Windows_StartupRepair_1127_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1128, version=0)
class Microsoft_Windows_StartupRepair_1128_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1129, version=0)
class Microsoft_Windows_StartupRepair_1129_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1130, version=0)
class Microsoft_Windows_StartupRepair_1130_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1131, version=0)
class Microsoft_Windows_StartupRepair_1131_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1132, version=0)
class Microsoft_Windows_StartupRepair_1132_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1133, version=0)
class Microsoft_Windows_StartupRepair_1133_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1134, version=0)
class Microsoft_Windows_StartupRepair_1134_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1135, version=0)
class Microsoft_Windows_StartupRepair_1135_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1136, version=0)
class Microsoft_Windows_StartupRepair_1136_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1137, version=0)
class Microsoft_Windows_StartupRepair_1137_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1138, version=0)
class Microsoft_Windows_StartupRepair_1138_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1139, version=0)
class Microsoft_Windows_StartupRepair_1139_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1140, version=0)
class Microsoft_Windows_StartupRepair_1140_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1141, version=0)
class Microsoft_Windows_StartupRepair_1141_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1201, version=0)
class Microsoft_Windows_StartupRepair_1201_0(Etw):
    pattern = Struct(
        "RepairStatus" / Int32ul,
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1202, version=0)
class Microsoft_Windows_StartupRepair_1202_0(Etw):
    pattern = Struct(
        "RepairStatus" / Int32ul,
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1203, version=0)
class Microsoft_Windows_StartupRepair_1203_0(Etw):
    pattern = Struct(
        "RepairStatus" / Int32ul,
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1204, version=0)
class Microsoft_Windows_StartupRepair_1204_0(Etw):
    pattern = Struct(
        "RepairStatus" / Int32ul,
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1205, version=0)
class Microsoft_Windows_StartupRepair_1205_0(Etw):
    pattern = Struct(
        "RepairStatus" / Int32ul,
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1206, version=0)
class Microsoft_Windows_StartupRepair_1206_0(Etw):
    pattern = Struct(
        "RepairStatus" / Int32ul,
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1207, version=0)
class Microsoft_Windows_StartupRepair_1207_0(Etw):
    pattern = Struct(
        "RepairStatus" / Int32ul,
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1208, version=0)
class Microsoft_Windows_StartupRepair_1208_0(Etw):
    pattern = Struct(
        "RepairStatus" / Int32ul,
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1209, version=0)
class Microsoft_Windows_StartupRepair_1209_0(Etw):
    pattern = Struct(
        "RepairStatus" / Int32ul,
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1210, version=0)
class Microsoft_Windows_StartupRepair_1210_0(Etw):
    pattern = Struct(
        "RepairStatus" / Int32ul,
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1211, version=0)
class Microsoft_Windows_StartupRepair_1211_0(Etw):
    pattern = Struct(
        "RepairStatus" / Int32ul,
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1212, version=0)
class Microsoft_Windows_StartupRepair_1212_0(Etw):
    pattern = Struct(
        "RepairStatus" / Int32ul,
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1213, version=0)
class Microsoft_Windows_StartupRepair_1213_0(Etw):
    pattern = Struct(
        "RepairStatus" / Int32ul,
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1214, version=0)
class Microsoft_Windows_StartupRepair_1214_0(Etw):
    pattern = Struct(
        "RepairStatus" / Int32ul,
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1215, version=0)
class Microsoft_Windows_StartupRepair_1215_0(Etw):
    pattern = Struct(
        "RepairStatus" / Int32ul,
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1216, version=0)
class Microsoft_Windows_StartupRepair_1216_0(Etw):
    pattern = Struct(
        "RepairStatus" / Int32ul,
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1217, version=0)
class Microsoft_Windows_StartupRepair_1217_0(Etw):
    pattern = Struct(
        "RepairStatus" / Int32ul,
        "Info" / WString
    )


@declare(guid=guid("c914f0df-835a-4a22-8c70-732c9a80c634"), event_id=1218, version=0)
class Microsoft_Windows_StartupRepair_1218_0(Etw):
    pattern = Struct(
        "RepairStatus" / Int32ul,
        "Info" / WString
    )

