# -*- coding: utf-8 -*-
"""
Microsoft-Windows-AAD
GUID : 4de9bc9c-b27a-43c9-8994-0915f1a5e24f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1002, version=0)
class Microsoft_Windows_AAD_1002_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1005, version=0)
class Microsoft_Windows_AAD_1005_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1007, version=0)
class Microsoft_Windows_AAD_1007_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1009, version=0)
class Microsoft_Windows_AAD_1009_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1011, version=0)
class Microsoft_Windows_AAD_1011_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1013, version=0)
class Microsoft_Windows_AAD_1013_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1015, version=0)
class Microsoft_Windows_AAD_1015_0(Etw):
    pattern = Struct(
        "Response" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1018, version=0)
class Microsoft_Windows_AAD_1018_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1019, version=0)
class Microsoft_Windows_AAD_1019_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1021, version=0)
class Microsoft_Windows_AAD_1021_0(Etw):
    pattern = Struct(
        "Status" / Int32sl
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1022, version=0)
class Microsoft_Windows_AAD_1022_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1023, version=0)
class Microsoft_Windows_AAD_1023_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1024, version=0)
class Microsoft_Windows_AAD_1024_0(Etw):
    pattern = Struct(
        "value" / Int32sl
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1025, version=0)
class Microsoft_Windows_AAD_1025_0(Etw):
    pattern = Struct(
        "value" / Int32sl,
        "Method" / WString,
        "EndpointUri" / WString,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1026, version=0)
class Microsoft_Windows_AAD_1026_0(Etw):
    pattern = Struct(
        "value" / Int32sl,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1029, version=0)
class Microsoft_Windows_AAD_1029_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1030, version=0)
class Microsoft_Windows_AAD_1030_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1032, version=0)
class Microsoft_Windows_AAD_1032_0(Etw):
    pattern = Struct(
        "value" / Int32sl
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1033, version=0)
class Microsoft_Windows_AAD_1033_0(Etw):
    pattern = Struct(
        "value" / Int32sl
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1035, version=0)
class Microsoft_Windows_AAD_1035_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1081, version=0)
class Microsoft_Windows_AAD_1081_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "ErrorDescription" / WString,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1082, version=0)
class Microsoft_Windows_AAD_1082_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "ErrorDescription" / WString,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1083, version=0)
class Microsoft_Windows_AAD_1083_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "ErrorDescription" / WString,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1084, version=0)
class Microsoft_Windows_AAD_1084_0(Etw):
    pattern = Struct(
        "Result" / Int32sl,
        "Target" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1085, version=0)
class Microsoft_Windows_AAD_1085_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1086, version=0)
class Microsoft_Windows_AAD_1086_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1087, version=0)
class Microsoft_Windows_AAD_1087_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1088, version=0)
class Microsoft_Windows_AAD_1088_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "ErrorDescription" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1089, version=0)
class Microsoft_Windows_AAD_1089_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1090, version=0)
class Microsoft_Windows_AAD_1090_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "ErrorDescription" / WString,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1091, version=0)
class Microsoft_Windows_AAD_1091_0(Etw):
    pattern = Struct(
        "Result" / Int32sl
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1092, version=0)
class Microsoft_Windows_AAD_1092_0(Etw):
    pattern = Struct(
        "CorrelationID" / WString,
        "RetryNumber" / Int32sl
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1093, version=0)
class Microsoft_Windows_AAD_1093_0(Etw):
    pattern = Struct(
        "API" / WString,
        "Result" / Int32sl
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1094, version=0)
class Microsoft_Windows_AAD_1094_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1095, version=0)
class Microsoft_Windows_AAD_1095_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1096, version=0)
class Microsoft_Windows_AAD_1096_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1097, version=0)
class Microsoft_Windows_AAD_1097_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ErrorMessage" / WString,
        "AdditionalInformation" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1098, version=0)
class Microsoft_Windows_AAD_1098_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ErrorMessage" / WString,
        "AdditionalInformation" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1099, version=0)
class Microsoft_Windows_AAD_1099_0(Etw):
    pattern = Struct(
        "OperationCode" / Int32ul,
        "OperationMessage" / WString,
        "AdditionalInformation" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1100, version=0)
class Microsoft_Windows_AAD_1100_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ErrorMessage" / WString,
        "AdditionalInformation" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1101, version=0)
class Microsoft_Windows_AAD_1101_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ErrorMessage" / WString,
        "AdditionalInformation" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1102, version=0)
class Microsoft_Windows_AAD_1102_0(Etw):
    pattern = Struct(
        "OperationCode" / Int32ul,
        "OperationMessage" / WString,
        "AdditionalInformation" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1103, version=0)
class Microsoft_Windows_AAD_1103_0(Etw):
    pattern = Struct(
        "Result" / Int32sl
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1104, version=0)
class Microsoft_Windows_AAD_1104_0(Etw):
    pattern = Struct(
        "API" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1105, version=0)
class Microsoft_Windows_AAD_1105_0(Etw):
    pattern = Struct(
        "API" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1106, version=0)
class Microsoft_Windows_AAD_1106_0(Etw):
    pattern = Struct(
        "value" / Int32sl,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1107, version=0)
class Microsoft_Windows_AAD_1107_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ErrorMessage" / WString,
        "AdditionalInformation" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1108, version=0)
class Microsoft_Windows_AAD_1108_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ErrorMessage" / WString,
        "AdditionalInformation" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1109, version=0)
class Microsoft_Windows_AAD_1109_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ErrorMessage" / WString,
        "AdditionalInformation" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1110, version=0)
class Microsoft_Windows_AAD_1110_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ErrorMessage" / WString,
        "AdditionalInformation" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1111, version=0)
class Microsoft_Windows_AAD_1111_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ErrorMessage" / WString,
        "AdditionalInformation" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1112, version=0)
class Microsoft_Windows_AAD_1112_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ErrorMessage" / WString,
        "AdditionalInformation" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1113, version=0)
class Microsoft_Windows_AAD_1113_0(Etw):
    pattern = Struct(
        "OperationCode" / Int32ul,
        "OperationMessage" / WString,
        "AdditionalInformation" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1114, version=0)
class Microsoft_Windows_AAD_1114_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ErrorMessage" / WString,
        "AdditionalInformation" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1115, version=0)
class Microsoft_Windows_AAD_1115_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ErrorMessage" / WString,
        "AdditionalInformation" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1116, version=0)
class Microsoft_Windows_AAD_1116_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1117, version=0)
class Microsoft_Windows_AAD_1117_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1118, version=0)
class Microsoft_Windows_AAD_1118_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1119, version=0)
class Microsoft_Windows_AAD_1119_0(Etw):
    pattern = Struct(
        "Response" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1120, version=0)
class Microsoft_Windows_AAD_1120_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1121, version=0)
class Microsoft_Windows_AAD_1121_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1122, version=0)
class Microsoft_Windows_AAD_1122_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1124, version=0)
class Microsoft_Windows_AAD_1124_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1129, version=0)
class Microsoft_Windows_AAD_1129_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1130, version=0)
class Microsoft_Windows_AAD_1130_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1131, version=0)
class Microsoft_Windows_AAD_1131_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1132, version=0)
class Microsoft_Windows_AAD_1132_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1133, version=0)
class Microsoft_Windows_AAD_1133_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1134, version=0)
class Microsoft_Windows_AAD_1134_0(Etw):
    pattern = Struct(
        "API" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1135, version=0)
class Microsoft_Windows_AAD_1135_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1137, version=0)
class Microsoft_Windows_AAD_1137_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1139, version=0)
class Microsoft_Windows_AAD_1139_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1141, version=0)
class Microsoft_Windows_AAD_1141_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1142, version=0)
class Microsoft_Windows_AAD_1142_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1143, version=0)
class Microsoft_Windows_AAD_1143_0(Etw):
    pattern = Struct(
        "value" / Int32sl,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1144, version=0)
class Microsoft_Windows_AAD_1144_0(Etw):
    pattern = Struct(
        "value" / Int32sl,
        "Method" / WString,
        "EndpointUri" / WString,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1145, version=0)
class Microsoft_Windows_AAD_1145_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1146, version=0)
class Microsoft_Windows_AAD_1146_0(Etw):
    pattern = Struct(
        "NoOfTargets" / Int64ul,
        "RequestType" / Int64ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1148, version=0)
class Microsoft_Windows_AAD_1148_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1150, version=0)
class Microsoft_Windows_AAD_1150_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1151, version=0)
class Microsoft_Windows_AAD_1151_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1152, version=0)
class Microsoft_Windows_AAD_1152_0(Etw):
    pattern = Struct(
        "Result" / Int32sl
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1153, version=0)
class Microsoft_Windows_AAD_1153_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1154, version=0)
class Microsoft_Windows_AAD_1154_0(Etw):
    pattern = Struct(
        "seconds" / Int32sl,
        "URI" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1155, version=0)
class Microsoft_Windows_AAD_1155_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1156, version=0)
class Microsoft_Windows_AAD_1156_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "ExpiryTime" / Int64ul,
        "PasswordChangeURI" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1158, version=0)
class Microsoft_Windows_AAD_1158_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1159, version=0)
class Microsoft_Windows_AAD_1159_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1160, version=0)
class Microsoft_Windows_AAD_1160_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1161, version=0)
class Microsoft_Windows_AAD_1161_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1162, version=0)
class Microsoft_Windows_AAD_1162_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1163, version=0)
class Microsoft_Windows_AAD_1163_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1164, version=0)
class Microsoft_Windows_AAD_1164_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1165, version=0)
class Microsoft_Windows_AAD_1165_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1202, version=0)
class Microsoft_Windows_AAD_1202_0(Etw):
    pattern = Struct(
        "Result" / Int32sl
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1203, version=0)
class Microsoft_Windows_AAD_1203_0(Etw):
    pattern = Struct(
        "Result" / Int32sl,
        "FunctionName" / CString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1205, version=0)
class Microsoft_Windows_AAD_1205_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1207, version=0)
class Microsoft_Windows_AAD_1207_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1208, version=0)
class Microsoft_Windows_AAD_1208_0(Etw):
    pattern = Struct(
        "value1" / WString,
        "value2" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1209, version=0)
class Microsoft_Windows_AAD_1209_0(Etw):
    pattern = Struct(
        "value1" / WString,
        "value2" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1210, version=0)
class Microsoft_Windows_AAD_1210_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1211, version=0)
class Microsoft_Windows_AAD_1211_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1212, version=0)
class Microsoft_Windows_AAD_1212_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1215, version=0)
class Microsoft_Windows_AAD_1215_0(Etw):
    pattern = Struct(
        "Result" / Int32sl
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1216, version=0)
class Microsoft_Windows_AAD_1216_0(Etw):
    pattern = Struct(
        "Result" / Int32sl,
        "Target" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1217, version=0)
class Microsoft_Windows_AAD_1217_0(Etw):
    pattern = Struct(
        "value1" / WString,
        "value2" / WString,
        "value3" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1219, version=0)
class Microsoft_Windows_AAD_1219_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1221, version=0)
class Microsoft_Windows_AAD_1221_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1223, version=0)
class Microsoft_Windows_AAD_1223_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1225, version=0)
class Microsoft_Windows_AAD_1225_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1227, version=0)
class Microsoft_Windows_AAD_1227_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1229, version=0)
class Microsoft_Windows_AAD_1229_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1230, version=0)
class Microsoft_Windows_AAD_1230_0(Etw):
    pattern = Struct(
        "API" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1231, version=0)
class Microsoft_Windows_AAD_1231_0(Etw):
    pattern = Struct(
        "Response" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1232, version=0)
class Microsoft_Windows_AAD_1232_0(Etw):
    pattern = Struct(
        "Response" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1233, version=0)
class Microsoft_Windows_AAD_1233_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1234, version=0)
class Microsoft_Windows_AAD_1234_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1235, version=0)
class Microsoft_Windows_AAD_1235_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "CorrelationID" / WString
    )


@declare(guid=guid("4de9bc9c-b27a-43c9-8994-0915f1a5e24f"), event_id=1241, version=0)
class Microsoft_Windows_AAD_1241_0(Etw):
    pattern = Struct(
        "value" / WString
    )

