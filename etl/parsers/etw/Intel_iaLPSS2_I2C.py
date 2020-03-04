# -*- coding: utf-8 -*-
"""
Intel-iaLPSS2-I2C
GUID : c2f86198-03ca-4771-8d4c-ce6e15cbca56
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1001, version=0)
class Intel_iaLPSS2_I2C_1001_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1002, version=0)
class Intel_iaLPSS2_I2C_1002_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1003, version=0)
class Intel_iaLPSS2_I2C_1003_0(Etw):
    pattern = Struct(
        "Function" / CString
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1004, version=0)
class Intel_iaLPSS2_I2C_1004_0(Etw):
    pattern = Struct(
        "Function" / CString
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1005, version=0)
class Intel_iaLPSS2_I2C_1005_0(Etw):
    pattern = Struct(
        "Function" / CString,
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1013, version=0)
class Intel_iaLPSS2_I2C_1013_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1014, version=0)
class Intel_iaLPSS2_I2C_1014_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1023, version=0)
class Intel_iaLPSS2_I2C_1023_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1024, version=0)
class Intel_iaLPSS2_I2C_1024_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1025, version=0)
class Intel_iaLPSS2_I2C_1025_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1026, version=0)
class Intel_iaLPSS2_I2C_1026_0(Etw):
    pattern = Struct(
        "Instance" / Int32ul,
        "Version" / Int32ul,
        "Revision" / Int32ul,
        "Mode" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1027, version=0)
class Intel_iaLPSS2_I2C_1027_0(Etw):
    pattern = Struct(
        "Instance" / Int32ul,
        "Version" / Int32ul,
        "Revision" / Int32ul,
        "Mode" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1028, version=0)
class Intel_iaLPSS2_I2C_1028_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1029, version=0)
class Intel_iaLPSS2_I2C_1029_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1030, version=0)
class Intel_iaLPSS2_I2C_1030_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1031, version=0)
class Intel_iaLPSS2_I2C_1031_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1032, version=0)
class Intel_iaLPSS2_I2C_1032_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1043, version=0)
class Intel_iaLPSS2_I2C_1043_0(Etw):
    pattern = Struct(
        "MBAR" / Int32ul,
        "PA" / Int64ul,
        "LEN" / Int32ul,
        "VA" / Int64ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1044, version=0)
class Intel_iaLPSS2_I2C_1044_0(Etw):
    pattern = Struct(
        "MBAR" / Int32ul,
        "PA" / Int64ul,
        "LEN" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1045, version=0)
class Intel_iaLPSS2_I2C_1045_0(Etw):
    pattern = Struct(
        "MBAR" / Int32ul,
        "PA" / Int64ul,
        "LEN" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1046, version=0)
class Intel_iaLPSS2_I2C_1046_0(Etw):
    pattern = Struct(
        "Vector" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1047, version=0)
class Intel_iaLPSS2_I2C_1047_0(Etw):
    pattern = Struct(
        "MBAR_count" / Int32ul,
        "INT_count" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1061, version=0)
class Intel_iaLPSS2_I2C_1061_0(Etw):
    pattern = Struct(
        "WdfPowerState" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1062, version=0)
class Intel_iaLPSS2_I2C_1062_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1063, version=0)
class Intel_iaLPSS2_I2C_1063_0(Etw):
    pattern = Struct(
        "WdfPowerState" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1065, version=0)
class Intel_iaLPSS2_I2C_1065_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1067, version=0)
class Intel_iaLPSS2_I2C_1067_0(Etw):
    pattern = Struct(
        "MonitorState" / Int32ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1068, version=0)
class Intel_iaLPSS2_I2C_1068_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1070, version=0)
class Intel_iaLPSS2_I2C_1070_0(Etw):
    pattern = Struct(
        "Function" / CString
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1071, version=0)
class Intel_iaLPSS2_I2C_1071_0(Etw):
    pattern = Struct(
        "SpbController" / Int64ul,
        "SpbTarget" / Int64ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1072, version=0)
class Intel_iaLPSS2_I2C_1072_0(Etw):
    pattern = Struct(
        "SpbController" / Int64ul,
        "SpbTarget" / Int64ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1073, version=0)
class Intel_iaLPSS2_I2C_1073_0(Etw):
    pattern = Struct(
        "SpbController" / Int64ul,
        "SpbTarget" / Int64ul,
        "SpbRequest" / Int64ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1074, version=0)
class Intel_iaLPSS2_I2C_1074_0(Etw):
    pattern = Struct(
        "SpbController" / Int64ul,
        "SpbTarget" / Int64ul,
        "SpbRequest" / Int64ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1075, version=0)
class Intel_iaLPSS2_I2C_1075_0(Etw):
    pattern = Struct(
        "SpbController" / Int64ul,
        "SpbTarget" / Int64ul,
        "SpbRequest" / Int64ul,
        "Length" / Int64ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1076, version=0)
class Intel_iaLPSS2_I2C_1076_0(Etw):
    pattern = Struct(
        "SpbController" / Int64ul,
        "SpbTarget" / Int64ul,
        "SpbRequest" / Int64ul,
        "Length" / Int64ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1077, version=0)
class Intel_iaLPSS2_I2C_1077_0(Etw):
    pattern = Struct(
        "SpbController" / Int64ul,
        "SpbTarget" / Int64ul,
        "SpbRequest" / Int64ul,
        "TransferCount" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1078, version=0)
class Intel_iaLPSS2_I2C_1078_0(Etw):
    pattern = Struct(
        "SpbController" / Int64ul,
        "FxTarget" / Int64ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1079, version=0)
class Intel_iaLPSS2_I2C_1079_0(Etw):
    pattern = Struct(
        "SpbController" / Int64ul,
        "SpbTarget" / Int64ul,
        "SpbRequest" / Int64ul,
        "InputLength" / Int64ul,
        "OutputLength" / Int64ul,
        "IoControlCode" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1081, version=0)
class Intel_iaLPSS2_I2C_1081_0(Etw):
    pattern = Struct(
        "SlaveAddress" / Int16ul,
        "AddressMode" / Int32ul,
        "ClkFreq" / Int64ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1082, version=0)
class Intel_iaLPSS2_I2C_1082_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1083, version=0)
class Intel_iaLPSS2_I2C_1083_0(Etw):
    pattern = Struct(
        "SlaveAddress" / Int16ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1084, version=0)
class Intel_iaLPSS2_I2C_1084_0(Etw):
    pattern = Struct(
        "SlaveAddress" / Int16ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1085, version=0)
class Intel_iaLPSS2_I2C_1085_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1086, version=0)
class Intel_iaLPSS2_I2C_1086_0(Etw):
    pattern = Struct(
        "SlaveAddress" / Int16ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1091, version=0)
class Intel_iaLPSS2_I2C_1091_0(Etw):
    pattern = Struct(
        "SlaveAddress" / Int16ul,
        "Idx" / Int32ul,
        "Count" / Int32ul,
        "Direction" / Int32ul,
        "Type" / Int32ul,
        "Length" / Int64ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1092, version=0)
class Intel_iaLPSS2_I2C_1092_0(Etw):
    pattern = Struct(
        "SlaveAddress" / Int16ul,
        "Idx" / Int32ul,
        "Count" / Int32ul,
        "Direction" / Int32ul,
        "Type" / Int32ul,
        "Length" / Int64ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1093, version=0)
class Intel_iaLPSS2_I2C_1093_0(Etw):
    pattern = Struct(
        "SlaveAddress" / Int16ul,
        "Idx" / Int32ul,
        "Count" / Int32ul,
        "Length" / Int64ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1094, version=0)
class Intel_iaLPSS2_I2C_1094_0(Etw):
    pattern = Struct(
        "SlaveAddress" / Int16ul,
        "Idx" / Int32ul,
        "Count" / Int32ul,
        "Length" / Int64ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1095, version=0)
class Intel_iaLPSS2_I2C_1095_0(Etw):
    pattern = Struct(
        "SlaveAddress" / Int16ul,
        "Idx" / Int32ul,
        "Count" / Int32ul,
        "Delay_us" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1096, version=0)
class Intel_iaLPSS2_I2C_1096_0(Etw):
    pattern = Struct(
        "SlaveAddress" / Int16ul,
        "Idx" / Int32ul,
        "Count" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1100, version=0)
class Intel_iaLPSS2_I2C_1100_0(Etw):
    pattern = Struct(
        "HwStatus" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1101, version=0)
class Intel_iaLPSS2_I2C_1101_0(Etw):
    pattern = Struct(
        "HwStatus" / Int32ul,
        "SwStatus" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1102, version=0)
class Intel_iaLPSS2_I2C_1102_0(Etw):
    pattern = Struct(
        "HwMask" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1171, version=0)
class Intel_iaLPSS2_I2C_1171_0(Etw):
    pattern = Struct(
        "Current" / Int32ul,
        "Expected" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1172, version=0)
class Intel_iaLPSS2_I2C_1172_0(Etw):
    pattern = Struct(
        "Current" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1176, version=0)
class Intel_iaLPSS2_I2C_1176_0(Etw):
    pattern = Struct(
        "Frequency" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1179, version=0)
class Intel_iaLPSS2_I2C_1179_0(Etw):
    pattern = Struct(
        "SpbController" / Int64ul,
        "SpbTarget" / Int64ul,
        "SpbRequest" / Int64ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1187, version=0)
class Intel_iaLPSS2_I2C_1187_0(Etw):
    pattern = Struct(
        "SpbController" / Int64ul,
        "SpbTarget" / Int64ul,
        "SpbRequest" / Int64ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1188, version=0)
class Intel_iaLPSS2_I2C_1188_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1189, version=0)
class Intel_iaLPSS2_I2C_1189_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1190, version=0)
class Intel_iaLPSS2_I2C_1190_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1191, version=0)
class Intel_iaLPSS2_I2C_1191_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1192, version=0)
class Intel_iaLPSS2_I2C_1192_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1193, version=0)
class Intel_iaLPSS2_I2C_1193_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1194, version=0)
class Intel_iaLPSS2_I2C_1194_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1195, version=0)
class Intel_iaLPSS2_I2C_1195_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1196, version=0)
class Intel_iaLPSS2_I2C_1196_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1197, version=0)
class Intel_iaLPSS2_I2C_1197_0(Etw):
    pattern = Struct(
        "SpbController" / Int64ul,
        "SpbRequest" / Int64ul,
        "Type" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1198, version=0)
class Intel_iaLPSS2_I2C_1198_0(Etw):
    pattern = Struct(
        "Function" / CString,
        "SpbController" / Int64ul,
        "SpbRequest" / Int64ul,
        "TotalInformation" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1199, version=0)
class Intel_iaLPSS2_I2C_1199_0(Etw):
    pattern = Struct(
        "Function" / CString,
        "SpbController" / Int64ul,
        "SpbRequest" / Int64ul,
        "TotalInformation" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1201, version=0)
class Intel_iaLPSS2_I2C_1201_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Capability" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1202, version=0)
class Intel_iaLPSS2_I2C_1202_0(Etw):
    pattern = Struct(
        "SlaveAddress" / Int16ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1203, version=0)
class Intel_iaLPSS2_I2C_1203_0(Etw):
    pattern = Struct(
        "SlaveAddress" / Int16ul,
        "Idx" / Int32ul,
        "Count" / Int32ul,
        "Length" / Int64ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1204, version=0)
class Intel_iaLPSS2_I2C_1204_0(Etw):
    pattern = Struct(
        "SlaveAddress" / Int16ul,
        "Idx" / Int32ul,
        "Count" / Int32ul,
        "Length" / Int64ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1205, version=0)
class Intel_iaLPSS2_I2C_1205_0(Etw):
    pattern = Struct(
        "SlaveAddress" / Int16ul,
        "Idx" / Int32ul,
        "Count" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1206, version=0)
class Intel_iaLPSS2_I2C_1206_0(Etw):
    pattern = Struct(
        "SlaveAddress" / Int16ul,
        "Idx" / Int32ul,
        "Count" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1207, version=0)
class Intel_iaLPSS2_I2C_1207_0(Etw):
    pattern = Struct(
        "SlaveAddress" / Int16ul,
        "Idx" / Int32ul,
        "Count" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1208, version=0)
class Intel_iaLPSS2_I2C_1208_0(Etw):
    pattern = Struct(
        "SlaveAddress" / Int16ul,
        "Idx" / Int32ul,
        "Count" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1209, version=0)
class Intel_iaLPSS2_I2C_1209_0(Etw):
    pattern = Struct(
        "SlaveAddress" / Int16ul,
        "Idx" / Int32ul,
        "Count" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1210, version=0)
class Intel_iaLPSS2_I2C_1210_0(Etw):
    pattern = Struct(
        "SlaveAddress" / Int16ul,
        "Idx" / Int32ul,
        "Count" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1215, version=0)
class Intel_iaLPSS2_I2C_1215_0(Etw):
    pattern = Struct(
        "SlaveAddress" / Int16ul,
        "Idx" / Int32ul,
        "Count" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1220, version=0)
class Intel_iaLPSS2_I2C_1220_0(Etw):
    pattern = Struct(
        "SlaveAddress" / Int16ul,
        "Idx" / Int32ul,
        "Count" / Int32ul,
        "Length" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c2f86198-03ca-4771-8d4c-ce6e15cbca56"), event_id=1225, version=0)
class Intel_iaLPSS2_I2C_1225_0(Etw):
    pattern = Struct(
        "HwStatus" / Int32ul,
        "SwStatus" / Int32ul
    )

