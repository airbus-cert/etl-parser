# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Shell-Core
GUID : 30336ed4-e327-447c-9de0-51b652c86108
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1, version=0)
class Microsoft_Windows_Shell_Core_1_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=2, version=0)
class Microsoft_Windows_Shell_Core_2_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=3, version=0)
class Microsoft_Windows_Shell_Core_3_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=4, version=0)
class Microsoft_Windows_Shell_Core_4_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=101, version=0)
class Microsoft_Windows_Shell_Core_101_0(Etw):
    pattern = Struct(
        "DeviceHandler" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=102, version=0)
class Microsoft_Windows_Shell_Core_102_0(Etw):
    pattern = Struct(
        "DeviceHandler" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=111, version=0)
class Microsoft_Windows_Shell_Core_111_0(Etw):
    pattern = Struct(
        "Command" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=112, version=0)
class Microsoft_Windows_Shell_Core_112_0(Etw):
    pattern = Struct(
        "Command" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=113, version=0)
class Microsoft_Windows_Shell_Core_113_0(Etw):
    pattern = Struct(
        "Message" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=114, version=0)
class Microsoft_Windows_Shell_Core_114_0(Etw):
    pattern = Struct(
        "Message" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=115, version=0)
class Microsoft_Windows_Shell_Core_115_0(Etw):
    pattern = Struct(
        "Message" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1021, version=0)
class Microsoft_Windows_Shell_Core_1021_0(Etw):
    pattern = Struct(
        "MaxResults" / Int32ul,
        "Query" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1022, version=0)
class Microsoft_Windows_Shell_Core_1022_0(Etw):
    pattern = Struct(
        "MaxResults" / Int32ul,
        "Query" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1028, version=0)
class Microsoft_Windows_Shell_Core_1028_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1029, version=0)
class Microsoft_Windows_Shell_Core_1029_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1033, version=0)
class Microsoft_Windows_Shell_Core_1033_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1035, version=0)
class Microsoft_Windows_Shell_Core_1035_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1037, version=0)
class Microsoft_Windows_Shell_Core_1037_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1040, version=0)
class Microsoft_Windows_Shell_Core_1040_0(Etw):
    pattern = Struct(
        "HandlerId" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1041, version=0)
class Microsoft_Windows_Shell_Core_1041_0(Etw):
    pattern = Struct(
        "HandlerId" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1042, version=0)
class Microsoft_Windows_Shell_Core_1042_0(Etw):
    pattern = Struct(
        "HandlerId" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1043, version=0)
class Microsoft_Windows_Shell_Core_1043_0(Etw):
    pattern = Struct(
        "HandlerId" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1044, version=0)
class Microsoft_Windows_Shell_Core_1044_0(Etw):
    pattern = Struct(
        "HandlerId" / Guid,
        "fReuse" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1045, version=0)
class Microsoft_Windows_Shell_Core_1045_0(Etw):
    pattern = Struct(
        "HandlerId" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1046, version=0)
class Microsoft_Windows_Shell_Core_1046_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1047, version=0)
class Microsoft_Windows_Shell_Core_1047_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1048, version=0)
class Microsoft_Windows_Shell_Core_1048_0(Etw):
    pattern = Struct(
        "ProviderId" / Guid,
        "Index" / Int32ul,
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1049, version=0)
class Microsoft_Windows_Shell_Core_1049_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1054, version=0)
class Microsoft_Windows_Shell_Core_1054_0(Etw):
    pattern = Struct(
        "HandlerId" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1055, version=0)
class Microsoft_Windows_Shell_Core_1055_0(Etw):
    pattern = Struct(
        "HandlerId" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1062, version=0)
class Microsoft_Windows_Shell_Core_1062_0(Etw):
    pattern = Struct(
        "HandlerId" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1063, version=0)
class Microsoft_Windows_Shell_Core_1063_0(Etw):
    pattern = Struct(
        "HandlerId" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1064, version=0)
class Microsoft_Windows_Shell_Core_1064_0(Etw):
    pattern = Struct(
        "HandlerId" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1065, version=0)
class Microsoft_Windows_Shell_Core_1065_0(Etw):
    pattern = Struct(
        "HandlerId" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1071, version=0)
class Microsoft_Windows_Shell_Core_1071_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1073, version=0)
class Microsoft_Windows_Shell_Core_1073_0(Etw):
    pattern = Struct(
        "Index" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1075, version=0)
class Microsoft_Windows_Shell_Core_1075_0(Etw):
    pattern = Struct(
        "iGroup" / Int32ul,
        "iItem" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1077, version=0)
class Microsoft_Windows_Shell_Core_1077_0(Etw):
    pattern = Struct(
        "Index" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1079, version=0)
class Microsoft_Windows_Shell_Core_1079_0(Etw):
    pattern = Struct(
        "iGroup" / Int32ul,
        "iItem" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1082, version=0)
class Microsoft_Windows_Shell_Core_1082_0(Etw):
    pattern = Struct(
        "Type" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1083, version=0)
class Microsoft_Windows_Shell_Core_1083_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Count" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1084, version=0)
class Microsoft_Windows_Shell_Core_1084_0(Etw):
    pattern = Struct(
        "Type" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1085, version=0)
class Microsoft_Windows_Shell_Core_1085_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Cookie" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1086, version=0)
class Microsoft_Windows_Shell_Core_1086_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Cookie" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1087, version=0)
class Microsoft_Windows_Shell_Core_1087_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Cookie" / Int32ul,
        "HRESULT" / Int32ul,
        "Count" / Int32ul,
        "fWaitingOnRealization" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1088, version=0)
class Microsoft_Windows_Shell_Core_1088_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Cookie" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1089, version=0)
class Microsoft_Windows_Shell_Core_1089_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Cookie" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1090, version=0)
class Microsoft_Windows_Shell_Core_1090_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Version" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1091, version=0)
class Microsoft_Windows_Shell_Core_1091_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Version" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1092, version=0)
class Microsoft_Windows_Shell_Core_1092_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Version" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1093, version=0)
class Microsoft_Windows_Shell_Core_1093_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Version" / Int32ul,
        "Cookie" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1094, version=0)
class Microsoft_Windows_Shell_Core_1094_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Version" / Int32ul,
        "Cookie" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1095, version=0)
class Microsoft_Windows_Shell_Core_1095_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Version" / Int32ul,
        "Cookie" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1096, version=0)
class Microsoft_Windows_Shell_Core_1096_0(Etw):
    pattern = Struct(
        "Cookie" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1097, version=0)
class Microsoft_Windows_Shell_Core_1097_0(Etw):
    pattern = Struct(
        "Event" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1098, version=0)
class Microsoft_Windows_Shell_Core_1098_0(Etw):
    pattern = Struct(
        "Event" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1099, version=0)
class Microsoft_Windows_Shell_Core_1099_0(Etw):
    pattern = Struct(
        "Event" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1100, version=0)
class Microsoft_Windows_Shell_Core_1100_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Version" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1101, version=0)
class Microsoft_Windows_Shell_Core_1101_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Version" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1103, version=0)
class Microsoft_Windows_Shell_Core_1103_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Version" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1106, version=0)
class Microsoft_Windows_Shell_Core_1106_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1108, version=0)
class Microsoft_Windows_Shell_Core_1108_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1109, version=0)
class Microsoft_Windows_Shell_Core_1109_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1113, version=0)
class Microsoft_Windows_Shell_Core_1113_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1114, version=0)
class Microsoft_Windows_Shell_Core_1114_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1115, version=0)
class Microsoft_Windows_Shell_Core_1115_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1116, version=0)
class Microsoft_Windows_Shell_Core_1116_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1118, version=0)
class Microsoft_Windows_Shell_Core_1118_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1120, version=0)
class Microsoft_Windows_Shell_Core_1120_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1121, version=0)
class Microsoft_Windows_Shell_Core_1121_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1128, version=0)
class Microsoft_Windows_Shell_Core_1128_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1130, version=0)
class Microsoft_Windows_Shell_Core_1130_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1152, version=0)
class Microsoft_Windows_Shell_Core_1152_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1415, version=0)
class Microsoft_Windows_Shell_Core_1415_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1417, version=0)
class Microsoft_Windows_Shell_Core_1417_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=1419, version=0)
class Microsoft_Windows_Shell_Core_1419_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=2022, version=0)
class Microsoft_Windows_Shell_Core_2022_0(Etw):
    pattern = Struct(
        "Message" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=2023, version=0)
class Microsoft_Windows_Shell_Core_2023_0(Etw):
    pattern = Struct(
        "Message" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=2024, version=0)
class Microsoft_Windows_Shell_Core_2024_0(Etw):
    pattern = Struct(
        "Message" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=2045, version=0)
class Microsoft_Windows_Shell_Core_2045_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=2047, version=0)
class Microsoft_Windows_Shell_Core_2047_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=2057, version=0)
class Microsoft_Windows_Shell_Core_2057_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=2058, version=0)
class Microsoft_Windows_Shell_Core_2058_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=2059, version=0)
class Microsoft_Windows_Shell_Core_2059_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=2060, version=0)
class Microsoft_Windows_Shell_Core_2060_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=2061, version=0)
class Microsoft_Windows_Shell_Core_2061_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=2062, version=0)
class Microsoft_Windows_Shell_Core_2062_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=2063, version=0)
class Microsoft_Windows_Shell_Core_2063_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=2064, version=0)
class Microsoft_Windows_Shell_Core_2064_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=2065, version=0)
class Microsoft_Windows_Shell_Core_2065_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=2067, version=0)
class Microsoft_Windows_Shell_Core_2067_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=3007, version=0)
class Microsoft_Windows_Shell_Core_3007_0(Etw):
    pattern = Struct(
        "dwFlags" / Int32ul,
        "pszTemplate" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=4001, version=0)
class Microsoft_Windows_Shell_Core_4001_0(Etw):
    pattern = Struct(
        "Message" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=4005, version=0)
class Microsoft_Windows_Shell_Core_4005_0(Etw):
    pattern = Struct(
        "ThreadID" / Int32ul,
        "pszName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=4007, version=0)
class Microsoft_Windows_Shell_Core_4007_0(Etw):
    pattern = Struct(
        "FakeShutdownReason" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=4008, version=0)
class Microsoft_Windows_Shell_Core_4008_0(Etw):
    pattern = Struct(
        "WParam" / Int32ul,
        "LParam" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6202, version=0)
class Microsoft_Windows_Shell_Core_6202_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6204, version=0)
class Microsoft_Windows_Shell_Core_6204_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6206, version=0)
class Microsoft_Windows_Shell_Core_6206_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "LowQuality" / Int8ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6217, version=0)
class Microsoft_Windows_Shell_Core_6217_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "RequestSize" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6218, version=0)
class Microsoft_Windows_Shell_Core_6218_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6220, version=0)
class Microsoft_Windows_Shell_Core_6220_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6226, version=0)
class Microsoft_Windows_Shell_Core_6226_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32sl,
        "RequestSize" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6228, version=0)
class Microsoft_Windows_Shell_Core_6228_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6230, version=0)
class Microsoft_Windows_Shell_Core_6230_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6231, version=0)
class Microsoft_Windows_Shell_Core_6231_0(Etw):
    pattern = Struct(
        "CropLookupSize" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6236, version=0)
class Microsoft_Windows_Shell_Core_6236_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6237, version=0)
class Microsoft_Windows_Shell_Core_6237_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6238, version=0)
class Microsoft_Windows_Shell_Core_6238_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6239, version=0)
class Microsoft_Windows_Shell_Core_6239_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6241, version=0)
class Microsoft_Windows_Shell_Core_6241_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6242, version=0)
class Microsoft_Windows_Shell_Core_6242_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "RequestSize" / Int32sl,
        "WTSFlags" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6243, version=0)
class Microsoft_Windows_Shell_Core_6243_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32sl,
        "CacheFlags" / Int32ul,
        "SizeX" / Int32sl,
        "SizeY" / Int32sl,
        "StreamType" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6510, version=0)
class Microsoft_Windows_Shell_Core_6510_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6515, version=0)
class Microsoft_Windows_Shell_Core_6515_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6516, version=0)
class Microsoft_Windows_Shell_Core_6516_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6517, version=0)
class Microsoft_Windows_Shell_Core_6517_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=6518, version=0)
class Microsoft_Windows_Shell_Core_6518_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9501, version=0)
class Microsoft_Windows_Shell_Core_9501_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9509, version=0)
class Microsoft_Windows_Shell_Core_9509_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9513, version=0)
class Microsoft_Windows_Shell_Core_9513_0(Etw):
    pattern = Struct(
        "Query" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9517, version=0)
class Microsoft_Windows_Shell_Core_9517_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9525, version=0)
class Microsoft_Windows_Shell_Core_9525_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9527, version=0)
class Microsoft_Windows_Shell_Core_9527_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9529, version=0)
class Microsoft_Windows_Shell_Core_9529_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9531, version=0)
class Microsoft_Windows_Shell_Core_9531_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9533, version=0)
class Microsoft_Windows_Shell_Core_9533_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9535, version=0)
class Microsoft_Windows_Shell_Core_9535_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9539, version=0)
class Microsoft_Windows_Shell_Core_9539_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9541, version=0)
class Microsoft_Windows_Shell_Core_9541_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9543, version=0)
class Microsoft_Windows_Shell_Core_9543_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9545, version=0)
class Microsoft_Windows_Shell_Core_9545_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9547, version=0)
class Microsoft_Windows_Shell_Core_9547_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9549, version=0)
class Microsoft_Windows_Shell_Core_9549_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9551, version=0)
class Microsoft_Windows_Shell_Core_9551_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9553, version=0)
class Microsoft_Windows_Shell_Core_9553_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9555, version=0)
class Microsoft_Windows_Shell_Core_9555_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9557, version=0)
class Microsoft_Windows_Shell_Core_9557_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9559, version=0)
class Microsoft_Windows_Shell_Core_9559_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9560, version=0)
class Microsoft_Windows_Shell_Core_9560_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9561, version=0)
class Microsoft_Windows_Shell_Core_9561_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9563, version=0)
class Microsoft_Windows_Shell_Core_9563_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9565, version=0)
class Microsoft_Windows_Shell_Core_9565_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9567, version=0)
class Microsoft_Windows_Shell_Core_9567_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9568, version=0)
class Microsoft_Windows_Shell_Core_9568_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9569, version=0)
class Microsoft_Windows_Shell_Core_9569_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9571, version=0)
class Microsoft_Windows_Shell_Core_9571_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9573, version=0)
class Microsoft_Windows_Shell_Core_9573_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9575, version=0)
class Microsoft_Windows_Shell_Core_9575_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9577, version=0)
class Microsoft_Windows_Shell_Core_9577_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9581, version=0)
class Microsoft_Windows_Shell_Core_9581_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9583, version=0)
class Microsoft_Windows_Shell_Core_9583_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9585, version=0)
class Microsoft_Windows_Shell_Core_9585_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9587, version=0)
class Microsoft_Windows_Shell_Core_9587_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9589, version=0)
class Microsoft_Windows_Shell_Core_9589_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9591, version=0)
class Microsoft_Windows_Shell_Core_9591_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9593, version=0)
class Microsoft_Windows_Shell_Core_9593_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9595, version=0)
class Microsoft_Windows_Shell_Core_9595_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9597, version=0)
class Microsoft_Windows_Shell_Core_9597_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9599, version=0)
class Microsoft_Windows_Shell_Core_9599_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9613, version=0)
class Microsoft_Windows_Shell_Core_9613_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSid" / Sid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9615, version=0)
class Microsoft_Windows_Shell_Core_9615_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9617, version=0)
class Microsoft_Windows_Shell_Core_9617_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9619, version=0)
class Microsoft_Windows_Shell_Core_9619_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9625, version=0)
class Microsoft_Windows_Shell_Core_9625_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9626, version=0)
class Microsoft_Windows_Shell_Core_9626_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9631, version=0)
class Microsoft_Windows_Shell_Core_9631_0(Etw):
    pattern = Struct(
        "WParam" / Int32ul,
        "LParam" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9633, version=0)
class Microsoft_Windows_Shell_Core_9633_0(Etw):
    pattern = Struct(
        "WParam" / Int32ul,
        "LParam" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9635, version=0)
class Microsoft_Windows_Shell_Core_9635_0(Etw):
    pattern = Struct(
        "WParam" / Int32ul,
        "LParam" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9639, version=0)
class Microsoft_Windows_Shell_Core_9639_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9641, version=0)
class Microsoft_Windows_Shell_Core_9641_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9647, version=0)
class Microsoft_Windows_Shell_Core_9647_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9648, version=0)
class Microsoft_Windows_Shell_Core_9648_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9649, version=0)
class Microsoft_Windows_Shell_Core_9649_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9652, version=0)
class Microsoft_Windows_Shell_Core_9652_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9653, version=0)
class Microsoft_Windows_Shell_Core_9653_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9654, version=0)
class Microsoft_Windows_Shell_Core_9654_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9660, version=0)
class Microsoft_Windows_Shell_Core_9660_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9705, version=0)
class Microsoft_Windows_Shell_Core_9705_0(Etw):
    pattern = Struct(
        "KeyName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9706, version=0)
class Microsoft_Windows_Shell_Core_9706_0(Etw):
    pattern = Struct(
        "KeyName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9707, version=0)
class Microsoft_Windows_Shell_Core_9707_0(Etw):
    pattern = Struct(
        "Command" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9708, version=0)
class Microsoft_Windows_Shell_Core_9708_0(Etw):
    pattern = Struct(
        "PID" / Int32ul,
        "Command" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9709, version=0)
class Microsoft_Windows_Shell_Core_9709_0(Etw):
    pattern = Struct(
        "Command" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9710, version=0)
class Microsoft_Windows_Shell_Core_9710_0(Etw):
    pattern = Struct(
        "PID" / Int32ul,
        "Command" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9711, version=0)
class Microsoft_Windows_Shell_Core_9711_0(Etw):
    pattern = Struct(
        "Command" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9712, version=0)
class Microsoft_Windows_Shell_Core_9712_0(Etw):
    pattern = Struct(
        "Command" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9713, version=0)
class Microsoft_Windows_Shell_Core_9713_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9714, version=0)
class Microsoft_Windows_Shell_Core_9714_0(Etw):
    pattern = Struct(
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9716, version=0)
class Microsoft_Windows_Shell_Core_9716_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9717, version=0)
class Microsoft_Windows_Shell_Core_9717_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9808, version=0)
class Microsoft_Windows_Shell_Core_9808_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9810, version=0)
class Microsoft_Windows_Shell_Core_9810_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9811, version=0)
class Microsoft_Windows_Shell_Core_9811_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9812, version=0)
class Microsoft_Windows_Shell_Core_9812_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "CallerId" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9903, version=0)
class Microsoft_Windows_Shell_Core_9903_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9904, version=0)
class Microsoft_Windows_Shell_Core_9904_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9905, version=0)
class Microsoft_Windows_Shell_Core_9905_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9906, version=0)
class Microsoft_Windows_Shell_Core_9906_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9907, version=0)
class Microsoft_Windows_Shell_Core_9907_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=9910, version=0)
class Microsoft_Windows_Shell_Core_9910_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=11011, version=0)
class Microsoft_Windows_Shell_Core_11011_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=11013, version=0)
class Microsoft_Windows_Shell_Core_11013_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=11014, version=0)
class Microsoft_Windows_Shell_Core_11014_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=12001, version=0)
class Microsoft_Windows_Shell_Core_12001_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=13503, version=0)
class Microsoft_Windows_Shell_Core_13503_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=13505, version=0)
class Microsoft_Windows_Shell_Core_13505_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=13507, version=0)
class Microsoft_Windows_Shell_Core_13507_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=13509, version=0)
class Microsoft_Windows_Shell_Core_13509_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=13511, version=0)
class Microsoft_Windows_Shell_Core_13511_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=13513, version=0)
class Microsoft_Windows_Shell_Core_13513_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=13515, version=0)
class Microsoft_Windows_Shell_Core_13515_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=13517, version=0)
class Microsoft_Windows_Shell_Core_13517_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=14004, version=0)
class Microsoft_Windows_Shell_Core_14004_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=14009, version=0)
class Microsoft_Windows_Shell_Core_14009_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=14201, version=0)
class Microsoft_Windows_Shell_Core_14201_0(Etw):
    pattern = Struct(
        "QueryId" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=14202, version=0)
class Microsoft_Windows_Shell_Core_14202_0(Etw):
    pattern = Struct(
        "QueryId" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=14203, version=0)
class Microsoft_Windows_Shell_Core_14203_0(Etw):
    pattern = Struct(
        "QueryId" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=14204, version=0)
class Microsoft_Windows_Shell_Core_14204_0(Etw):
    pattern = Struct(
        "QueryId" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=14205, version=0)
class Microsoft_Windows_Shell_Core_14205_0(Etw):
    pattern = Struct(
        "QueryId" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=14206, version=0)
class Microsoft_Windows_Shell_Core_14206_0(Etw):
    pattern = Struct(
        "QueryId" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=14207, version=0)
class Microsoft_Windows_Shell_Core_14207_0(Etw):
    pattern = Struct(
        "QueryId" / Int32ul,
        "QueryString" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=14209, version=0)
class Microsoft_Windows_Shell_Core_14209_0(Etw):
    pattern = Struct(
        "QueryId" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=14211, version=0)
class Microsoft_Windows_Shell_Core_14211_0(Etw):
    pattern = Struct(
        "QueryId" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=14213, version=0)
class Microsoft_Windows_Shell_Core_14213_0(Etw):
    pattern = Struct(
        "QueryId" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=14220, version=0)
class Microsoft_Windows_Shell_Core_14220_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=14561, version=0)
class Microsoft_Windows_Shell_Core_14561_0(Etw):
    pattern = Struct(
        "VARTYPEFrom" / Int16ul,
        "VARTYPETo" / Int16ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=14563, version=0)
class Microsoft_Windows_Shell_Core_14563_0(Etw):
    pattern = Struct(
        "VARTYPEFrom" / Int16ul,
        "VARTYPETo" / Int16ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=14564, version=0)
class Microsoft_Windows_Shell_Core_14564_0(Etw):
    pattern = Struct(
        "VARTYPEFrom" / Int16ul,
        "VARTYPETo" / Int16ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=15503, version=0)
class Microsoft_Windows_Shell_Core_15503_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=15504, version=0)
class Microsoft_Windows_Shell_Core_15504_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=15505, version=0)
class Microsoft_Windows_Shell_Core_15505_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=15506, version=0)
class Microsoft_Windows_Shell_Core_15506_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=15507, version=0)
class Microsoft_Windows_Shell_Core_15507_0(Etw):
    pattern = Struct(
        "CanonicalName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=15508, version=0)
class Microsoft_Windows_Shell_Core_15508_0(Etw):
    pattern = Struct(
        "CanonicalName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=15511, version=0)
class Microsoft_Windows_Shell_Core_15511_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=15512, version=0)
class Microsoft_Windows_Shell_Core_15512_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=15513, version=0)
class Microsoft_Windows_Shell_Core_15513_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=15514, version=0)
class Microsoft_Windows_Shell_Core_15514_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=15519, version=0)
class Microsoft_Windows_Shell_Core_15519_0(Etw):
    pattern = Struct(
        "CanonicalName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=15520, version=0)
class Microsoft_Windows_Shell_Core_15520_0(Etw):
    pattern = Struct(
        "CanonicalName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16503, version=0)
class Microsoft_Windows_Shell_Core_16503_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16504, version=0)
class Microsoft_Windows_Shell_Core_16504_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16505, version=0)
class Microsoft_Windows_Shell_Core_16505_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16506, version=0)
class Microsoft_Windows_Shell_Core_16506_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16507, version=0)
class Microsoft_Windows_Shell_Core_16507_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16508, version=0)
class Microsoft_Windows_Shell_Core_16508_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16511, version=0)
class Microsoft_Windows_Shell_Core_16511_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16512, version=0)
class Microsoft_Windows_Shell_Core_16512_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16608, version=0)
class Microsoft_Windows_Shell_Core_16608_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16609, version=0)
class Microsoft_Windows_Shell_Core_16609_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16614, version=0)
class Microsoft_Windows_Shell_Core_16614_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16615, version=0)
class Microsoft_Windows_Shell_Core_16615_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16620, version=0)
class Microsoft_Windows_Shell_Core_16620_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16621, version=0)
class Microsoft_Windows_Shell_Core_16621_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16716, version=0)
class Microsoft_Windows_Shell_Core_16716_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16717, version=0)
class Microsoft_Windows_Shell_Core_16717_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16722, version=0)
class Microsoft_Windows_Shell_Core_16722_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16723, version=0)
class Microsoft_Windows_Shell_Core_16723_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16724, version=0)
class Microsoft_Windows_Shell_Core_16724_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16725, version=0)
class Microsoft_Windows_Shell_Core_16725_0(Etw):
    pattern = Struct(
        "FMTID" / Guid,
        "PID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16801, version=0)
class Microsoft_Windows_Shell_Core_16801_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16805, version=0)
class Microsoft_Windows_Shell_Core_16805_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16807, version=0)
class Microsoft_Windows_Shell_Core_16807_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16809, version=0)
class Microsoft_Windows_Shell_Core_16809_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16811, version=0)
class Microsoft_Windows_Shell_Core_16811_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16813, version=0)
class Microsoft_Windows_Shell_Core_16813_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16815, version=0)
class Microsoft_Windows_Shell_Core_16815_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16817, version=0)
class Microsoft_Windows_Shell_Core_16817_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=16907, version=0)
class Microsoft_Windows_Shell_Core_16907_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=17008, version=0)
class Microsoft_Windows_Shell_Core_17008_0(Etw):
    pattern = Struct(
        "LoopCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=17117, version=0)
class Microsoft_Windows_Shell_Core_17117_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=17119, version=0)
class Microsoft_Windows_Shell_Core_17119_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=17121, version=0)
class Microsoft_Windows_Shell_Core_17121_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=17515, version=0)
class Microsoft_Windows_Shell_Core_17515_0(Etw):
    pattern = Struct(
        "Success" / Int32ul,
        "Path" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=17516, version=0)
class Microsoft_Windows_Shell_Core_17516_0(Etw):
    pattern = Struct(
        "Success" / Int32ul,
        "Path" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=17518, version=0)
class Microsoft_Windows_Shell_Core_17518_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18011, version=0)
class Microsoft_Windows_Shell_Core_18011_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18012, version=0)
class Microsoft_Windows_Shell_Core_18012_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18013, version=0)
class Microsoft_Windows_Shell_Core_18013_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18501, version=0)
class Microsoft_Windows_Shell_Core_18501_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18523, version=0)
class Microsoft_Windows_Shell_Core_18523_0(Etw):
    pattern = Struct(
        "Message" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18541, version=0)
class Microsoft_Windows_Shell_Core_18541_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18545, version=0)
class Microsoft_Windows_Shell_Core_18545_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ImageQualityFlags" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18546, version=0)
class Microsoft_Windows_Shell_Core_18546_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18550, version=0)
class Microsoft_Windows_Shell_Core_18550_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18559, version=0)
class Microsoft_Windows_Shell_Core_18559_0(Etw):
    pattern = Struct(
        "LoopCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18561, version=0)
class Microsoft_Windows_Shell_Core_18561_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18571, version=0)
class Microsoft_Windows_Shell_Core_18571_0(Etw):
    pattern = Struct(
        "TaskID" / Guid,
        "QueueItemCount" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18573, version=0)
class Microsoft_Windows_Shell_Core_18573_0(Etw):
    pattern = Struct(
        "TaskID" / Guid,
        "QueueItemCount" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18579, version=0)
class Microsoft_Windows_Shell_Core_18579_0(Etw):
    pattern = Struct(
        "Mode" / Int32ul,
        "IconSize" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18580, version=0)
class Microsoft_Windows_Shell_Core_18580_0(Etw):
    pattern = Struct(
        "Mode" / Int32ul,
        "IconSize" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18581, version=0)
class Microsoft_Windows_Shell_Core_18581_0(Etw):
    pattern = Struct(
        "LoopCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18654, version=0)
class Microsoft_Windows_Shell_Core_18654_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18657, version=0)
class Microsoft_Windows_Shell_Core_18657_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18658, version=0)
class Microsoft_Windows_Shell_Core_18658_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18659, version=0)
class Microsoft_Windows_Shell_Core_18659_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18660, version=0)
class Microsoft_Windows_Shell_Core_18660_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18661, version=0)
class Microsoft_Windows_Shell_Core_18661_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18669, version=0)
class Microsoft_Windows_Shell_Core_18669_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18675, version=0)
class Microsoft_Windows_Shell_Core_18675_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18683, version=0)
class Microsoft_Windows_Shell_Core_18683_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18684, version=0)
class Microsoft_Windows_Shell_Core_18684_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18695, version=0)
class Microsoft_Windows_Shell_Core_18695_0(Etw):
    pattern = Struct(
        "LoopCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18703, version=0)
class Microsoft_Windows_Shell_Core_18703_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18705, version=0)
class Microsoft_Windows_Shell_Core_18705_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStringDatapointValue" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18739, version=0)
class Microsoft_Windows_Shell_Core_18739_0(Etw):
    pattern = Struct(
        "ExecutableName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18740, version=0)
class Microsoft_Windows_Shell_Core_18740_0(Etw):
    pattern = Struct(
        "ExecutableName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18751, version=0)
class Microsoft_Windows_Shell_Core_18751_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18766, version=0)
class Microsoft_Windows_Shell_Core_18766_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18767, version=0)
class Microsoft_Windows_Shell_Core_18767_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18768, version=0)
class Microsoft_Windows_Shell_Core_18768_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18769, version=0)
class Microsoft_Windows_Shell_Core_18769_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18770, version=0)
class Microsoft_Windows_Shell_Core_18770_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18771, version=0)
class Microsoft_Windows_Shell_Core_18771_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18773, version=0)
class Microsoft_Windows_Shell_Core_18773_0(Etw):
    pattern = Struct(
        "TaskID" / Guid,
        "QueueItemCount" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18793, version=0)
class Microsoft_Windows_Shell_Core_18793_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18794, version=0)
class Microsoft_Windows_Shell_Core_18794_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18795, version=0)
class Microsoft_Windows_Shell_Core_18795_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18796, version=0)
class Microsoft_Windows_Shell_Core_18796_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18797, version=0)
class Microsoft_Windows_Shell_Core_18797_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18798, version=0)
class Microsoft_Windows_Shell_Core_18798_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18817, version=0)
class Microsoft_Windows_Shell_Core_18817_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18820, version=0)
class Microsoft_Windows_Shell_Core_18820_0(Etw):
    pattern = Struct(
        "CompletionDelta" / Int64ul,
        "SecondTimeDelta" / Double,
        "WindowSumOfRates" / Double,
        "CalculatedRate" / Double
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18821, version=0)
class Microsoft_Windows_Shell_Core_18821_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18823, version=0)
class Microsoft_Windows_Shell_Core_18823_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18865, version=0)
class Microsoft_Windows_Shell_Core_18865_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18873, version=0)
class Microsoft_Windows_Shell_Core_18873_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18875, version=0)
class Microsoft_Windows_Shell_Core_18875_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18887, version=0)
class Microsoft_Windows_Shell_Core_18887_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18889, version=0)
class Microsoft_Windows_Shell_Core_18889_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18903, version=0)
class Microsoft_Windows_Shell_Core_18903_0(Etw):
    pattern = Struct(
        "PointsCurrent" / Int64ul,
        "PointsTotal" / Int64ul,
        "SizeCurrent" / Int64ul,
        "SizeTotal" / Int64ul,
        "ItemsCurrent" / Int64ul,
        "ItemsTotal" / Int64ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18905, version=0)
class Microsoft_Windows_Shell_Core_18905_0(Etw):
    pattern = Struct(
        "pszSource" / WString,
        "pszDest" / WString,
        "SourceType" / Int32ul,
        "DestinationType" / Int32ul,
        "FileOp" / Int32ul,
        "FileSize" / Int64ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18909, version=0)
class Microsoft_Windows_Shell_Core_18909_0(Etw):
    pattern = Struct(
        "WorkDone" / Int64ul,
        "TimeElapsed" / Int64ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18911, version=0)
class Microsoft_Windows_Shell_Core_18911_0(Etw):
    pattern = Struct(
        "NewMean" / Int64ul,
        "AverageMean" / Int64ul,
        "Estimate" / Int64ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18913, version=0)
class Microsoft_Windows_Shell_Core_18913_0(Etw):
    pattern = Struct(
        "Speed" / Int64ul,
        "IsBytesPerSecond" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18921, version=0)
class Microsoft_Windows_Shell_Core_18921_0(Etw):
    pattern = Struct(
        "DROPEFFECT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18923, version=0)
class Microsoft_Windows_Shell_Core_18923_0(Etw):
    pattern = Struct(
        "DeviceID" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18933, version=0)
class Microsoft_Windows_Shell_Core_18933_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18934, version=0)
class Microsoft_Windows_Shell_Core_18934_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18935, version=0)
class Microsoft_Windows_Shell_Core_18935_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18936, version=0)
class Microsoft_Windows_Shell_Core_18936_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18937, version=0)
class Microsoft_Windows_Shell_Core_18937_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18939, version=0)
class Microsoft_Windows_Shell_Core_18939_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18951, version=0)
class Microsoft_Windows_Shell_Core_18951_0(Etw):
    pattern = Struct(
        "ID" / Int32ul,
        "HWND" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18953, version=0)
class Microsoft_Windows_Shell_Core_18953_0(Etw):
    pattern = Struct(
        "ID" / Int32ul,
        "HWND" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18954, version=0)
class Microsoft_Windows_Shell_Core_18954_0(Etw):
    pattern = Struct(
        "ID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18956, version=0)
class Microsoft_Windows_Shell_Core_18956_0(Etw):
    pattern = Struct(
        "ID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18958, version=0)
class Microsoft_Windows_Shell_Core_18958_0(Etw):
    pattern = Struct(
        "Event" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18960, version=0)
class Microsoft_Windows_Shell_Core_18960_0(Etw):
    pattern = Struct(
        "Event" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18962, version=0)
class Microsoft_Windows_Shell_Core_18962_0(Etw):
    pattern = Struct(
        "Event" / Int32ul,
        "ID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18964, version=0)
class Microsoft_Windows_Shell_Core_18964_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18970, version=0)
class Microsoft_Windows_Shell_Core_18970_0(Etw):
    pattern = Struct(
        "pszOperationSource" / WString,
        "pszOperationDestination" / WString,
        "FileOp" / Int32ul,
        "IsOperationUndo" / Int8ul,
        "UndoFlags" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18972, version=0)
class Microsoft_Windows_Shell_Core_18972_0(Etw):
    pattern = Struct(
        "pszOperationSource" / WString,
        "pszOperationDestination" / WString,
        "FileOp" / Int32ul,
        "IsOperationUndo" / Int8ul,
        "UndoFlags" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18974, version=0)
class Microsoft_Windows_Shell_Core_18974_0(Etw):
    pattern = Struct(
        "pszOperationSource" / WString,
        "pszOperationDestination" / WString,
        "FileOp" / Int32ul,
        "IsOperationUndo" / Int8ul,
        "UndoFlags" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18976, version=0)
class Microsoft_Windows_Shell_Core_18976_0(Etw):
    pattern = Struct(
        "pszOperationSource" / WString,
        "pszOperationDestination" / WString,
        "FileOp" / Int32ul,
        "IsOperationUndo" / Int8ul,
        "UndoFlags" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=18978, version=0)
class Microsoft_Windows_Shell_Core_18978_0(Etw):
    pattern = Struct(
        "pszOperationSource" / WString,
        "pszOperationDestination" / WString,
        "FileOp" / Int32ul,
        "IsOperationUndo" / Int8ul,
        "UndoFlags" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19001, version=0)
class Microsoft_Windows_Shell_Core_19001_0(Etw):
    pattern = Struct(
        "TOID" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19002, version=0)
class Microsoft_Windows_Shell_Core_19002_0(Etw):
    pattern = Struct(
        "TOID" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19003, version=0)
class Microsoft_Windows_Shell_Core_19003_0(Etw):
    pattern = Struct(
        "TOID" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19004, version=0)
class Microsoft_Windows_Shell_Core_19004_0(Etw):
    pattern = Struct(
        "TOID" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19005, version=0)
class Microsoft_Windows_Shell_Core_19005_0(Etw):
    pattern = Struct(
        "TOID" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19006, version=0)
class Microsoft_Windows_Shell_Core_19006_0(Etw):
    pattern = Struct(
        "TOID" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19007, version=0)
class Microsoft_Windows_Shell_Core_19007_0(Etw):
    pattern = Struct(
        "TOID" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19101, version=0)
class Microsoft_Windows_Shell_Core_19101_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19201, version=0)
class Microsoft_Windows_Shell_Core_19201_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19203, version=0)
class Microsoft_Windows_Shell_Core_19203_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19205, version=0)
class Microsoft_Windows_Shell_Core_19205_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19207, version=0)
class Microsoft_Windows_Shell_Core_19207_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19209, version=0)
class Microsoft_Windows_Shell_Core_19209_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19211, version=0)
class Microsoft_Windows_Shell_Core_19211_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19441, version=0)
class Microsoft_Windows_Shell_Core_19441_0(Etw):
    pattern = Struct(
        "PathToIcon" / WString,
        "IconOffset" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19443, version=0)
class Microsoft_Windows_Shell_Core_19443_0(Etw):
    pattern = Struct(
        "PathToIcon" / WString,
        "IconOffset" / Int32sl,
        "FromIconSize" / Int32sl,
        "ToIconSize" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19501, version=0)
class Microsoft_Windows_Shell_Core_19501_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19502, version=0)
class Microsoft_Windows_Shell_Core_19502_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "HRESULT" / Int32ul,
        "PIDL_out" / Int64ul,
        "HWND" / Int32ul,
        "IBindCtx" / Int64ul,
        "cbEaten" / Int32ul,
        "dwAttributes" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19503, version=0)
class Microsoft_Windows_Shell_Core_19503_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "Depth" / Int32ul,
        "Children" / Int8sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19504, version=0)
class Microsoft_Windows_Shell_Core_19504_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "HRESULT" / Int32ul,
        "Flags" / Int32ul,
        "Name" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19613, version=0)
class Microsoft_Windows_Shell_Core_19613_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19615, version=0)
class Microsoft_Windows_Shell_Core_19615_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19617, version=0)
class Microsoft_Windows_Shell_Core_19617_0(Etw):
    pattern = Struct(
        "pszName" / WString,
        "fVal" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19619, version=0)
class Microsoft_Windows_Shell_Core_19619_0(Etw):
    pattern = Struct(
        "uMode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19621, version=0)
class Microsoft_Windows_Shell_Core_19621_0(Etw):
    pattern = Struct(
        "uAnimationType" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19623, version=0)
class Microsoft_Windows_Shell_Core_19623_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19628, version=0)
class Microsoft_Windows_Shell_Core_19628_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19801, version=0)
class Microsoft_Windows_Shell_Core_19801_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=19900, version=0)
class Microsoft_Windows_Shell_Core_19900_0(Etw):
    pattern = Struct(
        "OldState" / Int32sl,
        "NewState" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20007, version=0)
class Microsoft_Windows_Shell_Core_20007_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20009, version=0)
class Microsoft_Windows_Shell_Core_20009_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20011, version=0)
class Microsoft_Windows_Shell_Core_20011_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20013, version=0)
class Microsoft_Windows_Shell_Core_20013_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20015, version=0)
class Microsoft_Windows_Shell_Core_20015_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20017, version=0)
class Microsoft_Windows_Shell_Core_20017_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20019, version=0)
class Microsoft_Windows_Shell_Core_20019_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20021, version=0)
class Microsoft_Windows_Shell_Core_20021_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20023, version=0)
class Microsoft_Windows_Shell_Core_20023_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20025, version=0)
class Microsoft_Windows_Shell_Core_20025_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20027, version=0)
class Microsoft_Windows_Shell_Core_20027_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20029, version=0)
class Microsoft_Windows_Shell_Core_20029_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20031, version=0)
class Microsoft_Windows_Shell_Core_20031_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20033, version=0)
class Microsoft_Windows_Shell_Core_20033_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20035, version=0)
class Microsoft_Windows_Shell_Core_20035_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20037, version=0)
class Microsoft_Windows_Shell_Core_20037_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20039, version=0)
class Microsoft_Windows_Shell_Core_20039_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20041, version=0)
class Microsoft_Windows_Shell_Core_20041_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20043, version=0)
class Microsoft_Windows_Shell_Core_20043_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20045, version=0)
class Microsoft_Windows_Shell_Core_20045_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20047, version=0)
class Microsoft_Windows_Shell_Core_20047_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20049, version=0)
class Microsoft_Windows_Shell_Core_20049_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20051, version=0)
class Microsoft_Windows_Shell_Core_20051_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20053, version=0)
class Microsoft_Windows_Shell_Core_20053_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20055, version=0)
class Microsoft_Windows_Shell_Core_20055_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20057, version=0)
class Microsoft_Windows_Shell_Core_20057_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20059, version=0)
class Microsoft_Windows_Shell_Core_20059_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20061, version=0)
class Microsoft_Windows_Shell_Core_20061_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20063, version=0)
class Microsoft_Windows_Shell_Core_20063_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20071, version=0)
class Microsoft_Windows_Shell_Core_20071_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20072, version=0)
class Microsoft_Windows_Shell_Core_20072_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20073, version=0)
class Microsoft_Windows_Shell_Core_20073_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20076, version=0)
class Microsoft_Windows_Shell_Core_20076_0(Etw):
    pattern = Struct(
        "LoopCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20920, version=0)
class Microsoft_Windows_Shell_Core_20920_0(Etw):
    pattern = Struct(
        "EXTENDED_NAME_FORMAT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=20921, version=0)
class Microsoft_Windows_Shell_Core_20921_0(Etw):
    pattern = Struct(
        "EXTENDED_NAME_FORMAT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=21001, version=0)
class Microsoft_Windows_Shell_Core_21001_0(Etw):
    pattern = Struct(
        "LoopCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=21005, version=0)
class Microsoft_Windows_Shell_Core_21005_0(Etw):
    pattern = Struct(
        "nIcons" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=21007, version=0)
class Microsoft_Windows_Shell_Core_21007_0(Etw):
    pattern = Struct(
        "TrayCode" / Int32ul,
        "guid" / Guid,
        "uID" / Int32ul,
        "HWND" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=21009, version=0)
class Microsoft_Windows_Shell_Core_21009_0(Etw):
    pattern = Struct(
        "TrayCode" / Int32ul,
        "guid" / Guid,
        "uID" / Int32ul,
        "HWND" / Int32ul,
        "uReasonForDelete" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=21011, version=0)
class Microsoft_Windows_Shell_Core_21011_0(Etw):
    pattern = Struct(
        "TrayCode" / Int32ul,
        "guid" / Guid,
        "uID" / Int32ul,
        "HWND" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=21013, version=0)
class Microsoft_Windows_Shell_Core_21013_0(Etw):
    pattern = Struct(
        "guid" / Guid,
        "uID" / Int32ul,
        "HWND" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=21015, version=0)
class Microsoft_Windows_Shell_Core_21015_0(Etw):
    pattern = Struct(
        "guid" / Guid,
        "uID" / Int32ul,
        "HWND" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=21018, version=0)
class Microsoft_Windows_Shell_Core_21018_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22005, version=0)
class Microsoft_Windows_Shell_Core_22005_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22006, version=0)
class Microsoft_Windows_Shell_Core_22006_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22007, version=0)
class Microsoft_Windows_Shell_Core_22007_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22009, version=0)
class Microsoft_Windows_Shell_Core_22009_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22011, version=0)
class Microsoft_Windows_Shell_Core_22011_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22013, version=0)
class Microsoft_Windows_Shell_Core_22013_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22014, version=0)
class Microsoft_Windows_Shell_Core_22014_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22015, version=0)
class Microsoft_Windows_Shell_Core_22015_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22017, version=0)
class Microsoft_Windows_Shell_Core_22017_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22018, version=0)
class Microsoft_Windows_Shell_Core_22018_0(Etw):
    pattern = Struct(
        "HWNDSrc" / Int64ul,
        "HWNDThumbnail" / Int64ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22019, version=0)
class Microsoft_Windows_Shell_Core_22019_0(Etw):
    pattern = Struct(
        "HWNDSrc" / Int64ul,
        "HWNDThumbnail" / Int64ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22020, version=0)
class Microsoft_Windows_Shell_Core_22020_0(Etw):
    pattern = Struct(
        "iId" / Int32ul,
        "fFromGlom" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22021, version=0)
class Microsoft_Windows_Shell_Core_22021_0(Etw):
    pattern = Struct(
        "iId" / Int32ul,
        "fFromGlom" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22022, version=0)
class Microsoft_Windows_Shell_Core_22022_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22023, version=0)
class Microsoft_Windows_Shell_Core_22023_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22025, version=0)
class Microsoft_Windows_Shell_Core_22025_0(Etw):
    pattern = Struct(
        "HWND" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22026, version=0)
class Microsoft_Windows_Shell_Core_22026_0(Etw):
    pattern = Struct(
        "HWND" / Int32ul,
        "dwValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22027, version=0)
class Microsoft_Windows_Shell_Core_22027_0(Etw):
    pattern = Struct(
        "HWND" / Int32ul,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22028, version=0)
class Microsoft_Windows_Shell_Core_22028_0(Etw):
    pattern = Struct(
        "hwndTaskBand" / Int64ul,
        "pTBGroup" / Int64ul,
        "pszExePath" / WString,
        "tbgType" / Int32ul,
        "x" / Int32sl,
        "y" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22029, version=0)
class Microsoft_Windows_Shell_Core_22029_0(Etw):
    pattern = Struct(
        "hwndTaskBand" / Int64ul,
        "pTBGroup" / Int64ul,
        "pszExePath" / WString,
        "tbgType" / Int32ul,
        "x" / Int32sl,
        "y" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22030, version=0)
class Microsoft_Windows_Shell_Core_22030_0(Etw):
    pattern = Struct(
        "hwndTaskBand" / Int64ul,
        "pTBGroup" / Int64ul,
        "pszExePath" / WString,
        "tbgType" / Int32ul,
        "x" / Int32sl,
        "y" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22031, version=0)
class Microsoft_Windows_Shell_Core_22031_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "hwndTaskBand" / Int64ul,
        "pTBGroup" / Int64ul,
        "pszExePath" / WString,
        "tbgType" / Int32ul,
        "x" / Int32sl,
        "y" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22032, version=0)
class Microsoft_Windows_Shell_Core_22032_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "hwndTaskBand" / Int64ul,
        "pTBGroup" / Int64ul,
        "pszExePath" / WString,
        "tbgType" / Int32ul,
        "x" / Int32sl,
        "y" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22033, version=0)
class Microsoft_Windows_Shell_Core_22033_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "hwndTaskBand" / Int64ul,
        "pTBGroup" / Int64ul,
        "pszExePath" / WString,
        "tbgType" / Int32ul,
        "x" / Int32sl,
        "y" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22034, version=0)
class Microsoft_Windows_Shell_Core_22034_0(Etw):
    pattern = Struct(
        "fShowText" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22035, version=0)
class Microsoft_Windows_Shell_Core_22035_0(Etw):
    pattern = Struct(
        "hwndItem" / Int64ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22036, version=0)
class Microsoft_Windows_Shell_Core_22036_0(Etw):
    pattern = Struct(
        "hwndItem" / Int64ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22037, version=0)
class Microsoft_Windows_Shell_Core_22037_0(Etw):
    pattern = Struct(
        "pszGroup" / WString,
        "hwndItem" / Int64ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22038, version=0)
class Microsoft_Windows_Shell_Core_22038_0(Etw):
    pattern = Struct(
        "pszGroup" / WString,
        "hwndItem" / Int64ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22039, version=0)
class Microsoft_Windows_Shell_Core_22039_0(Etw):
    pattern = Struct(
        "pszGroup" / WString,
        "hwndItem" / Int64ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22040, version=0)
class Microsoft_Windows_Shell_Core_22040_0(Etw):
    pattern = Struct(
        "pszGroup" / WString,
        "hwndItem" / Int64ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22041, version=0)
class Microsoft_Windows_Shell_Core_22041_0(Etw):
    pattern = Struct(
        "pObj" / Int64ul,
        "nAnimType" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22042, version=0)
class Microsoft_Windows_Shell_Core_22042_0(Etw):
    pattern = Struct(
        "pObj" / Int64ul,
        "nAnimType" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22045, version=0)
class Microsoft_Windows_Shell_Core_22045_0(Etw):
    pattern = Struct(
        "nVisibleRow" / Int32ul,
        "nRequiredRow" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22046, version=0)
class Microsoft_Windows_Shell_Core_22046_0(Etw):
    pattern = Struct(
        "nTotalWidth" / Int32ul,
        "nTotalFixedWidth" / Int32ul,
        "iGroupStart" / Int32ul,
        "iItemStart" / Int32ul,
        "iGroupEnd" / Int32ul,
        "iItemEnd" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22047, version=0)
class Microsoft_Windows_Shell_Core_22047_0(Etw):
    pattern = Struct(
        "hwndTaskBand" / Int64ul,
        "pTBGroup" / Int64ul,
        "pszExePath" / WString,
        "tbgType" / Int32ul,
        "x" / Int32sl,
        "y" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22048, version=0)
class Microsoft_Windows_Shell_Core_22048_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22049, version=0)
class Microsoft_Windows_Shell_Core_22049_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22050, version=0)
class Microsoft_Windows_Shell_Core_22050_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22051, version=0)
class Microsoft_Windows_Shell_Core_22051_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22052, version=0)
class Microsoft_Windows_Shell_Core_22052_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22053, version=0)
class Microsoft_Windows_Shell_Core_22053_0(Etw):
    pattern = Struct(
        "nTotalHeight" / Int32ul,
        "nTotalFixedHeight" / Int32ul,
        "iGroupStart" / Int32ul,
        "iItemStart" / Int32ul,
        "iGroupEnd" / Int32ul,
        "iItemEnd" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22054, version=0)
class Microsoft_Windows_Shell_Core_22054_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22055, version=0)
class Microsoft_Windows_Shell_Core_22055_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22056, version=0)
class Microsoft_Windows_Shell_Core_22056_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22057, version=0)
class Microsoft_Windows_Shell_Core_22057_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22058, version=0)
class Microsoft_Windows_Shell_Core_22058_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22059, version=0)
class Microsoft_Windows_Shell_Core_22059_0(Etw):
    pattern = Struct(
        "Index" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22060, version=0)
class Microsoft_Windows_Shell_Core_22060_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22061, version=0)
class Microsoft_Windows_Shell_Core_22061_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22062, version=0)
class Microsoft_Windows_Shell_Core_22062_0(Etw):
    pattern = Struct(
        "Index" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22063, version=0)
class Microsoft_Windows_Shell_Core_22063_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22064, version=0)
class Microsoft_Windows_Shell_Core_22064_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul,
        "IsFlashed" / Int32ul,
        "SourceType" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22067, version=0)
class Microsoft_Windows_Shell_Core_22067_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22068, version=0)
class Microsoft_Windows_Shell_Core_22068_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22069, version=0)
class Microsoft_Windows_Shell_Core_22069_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22070, version=0)
class Microsoft_Windows_Shell_Core_22070_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22071, version=0)
class Microsoft_Windows_Shell_Core_22071_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22072, version=0)
class Microsoft_Windows_Shell_Core_22072_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22073, version=0)
class Microsoft_Windows_Shell_Core_22073_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22074, version=0)
class Microsoft_Windows_Shell_Core_22074_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22075, version=0)
class Microsoft_Windows_Shell_Core_22075_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22076, version=0)
class Microsoft_Windows_Shell_Core_22076_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22077, version=0)
class Microsoft_Windows_Shell_Core_22077_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=22078, version=0)
class Microsoft_Windows_Shell_Core_22078_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=23007, version=0)
class Microsoft_Windows_Shell_Core_23007_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=23008, version=0)
class Microsoft_Windows_Shell_Core_23008_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=23009, version=0)
class Microsoft_Windows_Shell_Core_23009_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=23010, version=0)
class Microsoft_Windows_Shell_Core_23010_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=23011, version=0)
class Microsoft_Windows_Shell_Core_23011_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=23012, version=0)
class Microsoft_Windows_Shell_Core_23012_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=23013, version=0)
class Microsoft_Windows_Shell_Core_23013_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=23101, version=0)
class Microsoft_Windows_Shell_Core_23101_0(Etw):
    pattern = Struct(
        "Query" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=23201, version=0)
class Microsoft_Windows_Shell_Core_23201_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=23203, version=0)
class Microsoft_Windows_Shell_Core_23203_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=23205, version=0)
class Microsoft_Windows_Shell_Core_23205_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=26001, version=0)
class Microsoft_Windows_Shell_Core_26001_0(Etw):
    pattern = Struct(
        "Operation" / WString,
        "Type" / Int32ul,
        "Event" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=26002, version=0)
class Microsoft_Windows_Shell_Core_26002_0(Etw):
    pattern = Struct(
        "Operation" / WString,
        "PendingCount" / Int32ul,
        "EventReadyState" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=26007, version=0)
class Microsoft_Windows_Shell_Core_26007_0(Etw):
    pattern = Struct(
        "Operation" / WString,
        "Type" / Int32ul,
        "Event" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=26009, version=0)
class Microsoft_Windows_Shell_Core_26009_0(Etw):
    pattern = Struct(
        "Caller" / WString,
        "IItemCollection" / Int64ul,
        "ICollectionEventSink" / Int64ul,
        "Cookie" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=26010, version=0)
class Microsoft_Windows_Shell_Core_26010_0(Etw):
    pattern = Struct(
        "Caller" / WString,
        "IItemCollection" / Int64ul,
        "ICollectionEventSink" / Int64ul,
        "Cookie" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=26011, version=0)
class Microsoft_Windows_Shell_Core_26011_0(Etw):
    pattern = Struct(
        "RetVal" / Int32ul,
        "HWND" / Int64ul,
        "Message" / Int64ul,
        "WPARAM" / Int64ul,
        "LPARAM" / Int64ul,
        "GetLastError" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27002, version=0)
class Microsoft_Windows_Shell_Core_27002_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27004, version=0)
class Microsoft_Windows_Shell_Core_27004_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27018, version=0)
class Microsoft_Windows_Shell_Core_27018_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27020, version=0)
class Microsoft_Windows_Shell_Core_27020_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27022, version=0)
class Microsoft_Windows_Shell_Core_27022_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27024, version=0)
class Microsoft_Windows_Shell_Core_27024_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27026, version=0)
class Microsoft_Windows_Shell_Core_27026_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27028, version=0)
class Microsoft_Windows_Shell_Core_27028_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27030, version=0)
class Microsoft_Windows_Shell_Core_27030_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27032, version=0)
class Microsoft_Windows_Shell_Core_27032_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27034, version=0)
class Microsoft_Windows_Shell_Core_27034_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27036, version=0)
class Microsoft_Windows_Shell_Core_27036_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27038, version=0)
class Microsoft_Windows_Shell_Core_27038_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27040, version=0)
class Microsoft_Windows_Shell_Core_27040_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27042, version=0)
class Microsoft_Windows_Shell_Core_27042_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27044, version=0)
class Microsoft_Windows_Shell_Core_27044_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27046, version=0)
class Microsoft_Windows_Shell_Core_27046_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27048, version=0)
class Microsoft_Windows_Shell_Core_27048_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27050, version=0)
class Microsoft_Windows_Shell_Core_27050_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27052, version=0)
class Microsoft_Windows_Shell_Core_27052_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27054, version=0)
class Microsoft_Windows_Shell_Core_27054_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27056, version=0)
class Microsoft_Windows_Shell_Core_27056_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27058, version=0)
class Microsoft_Windows_Shell_Core_27058_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27060, version=0)
class Microsoft_Windows_Shell_Core_27060_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27062, version=0)
class Microsoft_Windows_Shell_Core_27062_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27064, version=0)
class Microsoft_Windows_Shell_Core_27064_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27078, version=0)
class Microsoft_Windows_Shell_Core_27078_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27080, version=0)
class Microsoft_Windows_Shell_Core_27080_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27082, version=0)
class Microsoft_Windows_Shell_Core_27082_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27084, version=0)
class Microsoft_Windows_Shell_Core_27084_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27086, version=0)
class Microsoft_Windows_Shell_Core_27086_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27088, version=0)
class Microsoft_Windows_Shell_Core_27088_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27090, version=0)
class Microsoft_Windows_Shell_Core_27090_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27092, version=0)
class Microsoft_Windows_Shell_Core_27092_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27094, version=0)
class Microsoft_Windows_Shell_Core_27094_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27096, version=0)
class Microsoft_Windows_Shell_Core_27096_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27098, version=0)
class Microsoft_Windows_Shell_Core_27098_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27100, version=0)
class Microsoft_Windows_Shell_Core_27100_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27102, version=0)
class Microsoft_Windows_Shell_Core_27102_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27104, version=0)
class Microsoft_Windows_Shell_Core_27104_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27106, version=0)
class Microsoft_Windows_Shell_Core_27106_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27108, version=0)
class Microsoft_Windows_Shell_Core_27108_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27110, version=0)
class Microsoft_Windows_Shell_Core_27110_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27112, version=0)
class Microsoft_Windows_Shell_Core_27112_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27114, version=0)
class Microsoft_Windows_Shell_Core_27114_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27116, version=0)
class Microsoft_Windows_Shell_Core_27116_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27118, version=0)
class Microsoft_Windows_Shell_Core_27118_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27120, version=0)
class Microsoft_Windows_Shell_Core_27120_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27122, version=0)
class Microsoft_Windows_Shell_Core_27122_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27124, version=0)
class Microsoft_Windows_Shell_Core_27124_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27126, version=0)
class Microsoft_Windows_Shell_Core_27126_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27128, version=0)
class Microsoft_Windows_Shell_Core_27128_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27142, version=0)
class Microsoft_Windows_Shell_Core_27142_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27144, version=0)
class Microsoft_Windows_Shell_Core_27144_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27145, version=0)
class Microsoft_Windows_Shell_Core_27145_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27146, version=0)
class Microsoft_Windows_Shell_Core_27146_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27147, version=0)
class Microsoft_Windows_Shell_Core_27147_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27148, version=0)
class Microsoft_Windows_Shell_Core_27148_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27168, version=0)
class Microsoft_Windows_Shell_Core_27168_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27170, version=0)
class Microsoft_Windows_Shell_Core_27170_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27172, version=0)
class Microsoft_Windows_Shell_Core_27172_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27176, version=0)
class Microsoft_Windows_Shell_Core_27176_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27178, version=0)
class Microsoft_Windows_Shell_Core_27178_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27180, version=0)
class Microsoft_Windows_Shell_Core_27180_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27182, version=0)
class Microsoft_Windows_Shell_Core_27182_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27184, version=0)
class Microsoft_Windows_Shell_Core_27184_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27186, version=0)
class Microsoft_Windows_Shell_Core_27186_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27188, version=0)
class Microsoft_Windows_Shell_Core_27188_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27190, version=0)
class Microsoft_Windows_Shell_Core_27190_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27202, version=0)
class Microsoft_Windows_Shell_Core_27202_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27206, version=0)
class Microsoft_Windows_Shell_Core_27206_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27208, version=0)
class Microsoft_Windows_Shell_Core_27208_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27217, version=0)
class Microsoft_Windows_Shell_Core_27217_0(Etw):
    pattern = Struct(
        "PerfTrackId" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27218, version=0)
class Microsoft_Windows_Shell_Core_27218_0(Etw):
    pattern = Struct(
        "PerfTrackId" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27229, version=0)
class Microsoft_Windows_Shell_Core_27229_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27233, version=0)
class Microsoft_Windows_Shell_Core_27233_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27243, version=0)
class Microsoft_Windows_Shell_Core_27243_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27244, version=0)
class Microsoft_Windows_Shell_Core_27244_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27248, version=0)
class Microsoft_Windows_Shell_Core_27248_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27250, version=0)
class Microsoft_Windows_Shell_Core_27250_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27252, version=0)
class Microsoft_Windows_Shell_Core_27252_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27254, version=0)
class Microsoft_Windows_Shell_Core_27254_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27256, version=0)
class Microsoft_Windows_Shell_Core_27256_0(Etw):
    pattern = Struct(
        "RenderedTileCount" / Int32ul,
        "RealizedTileCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=27257, version=0)
class Microsoft_Windows_Shell_Core_27257_0(Etw):
    pattern = Struct(
        "BrowserId" / Int32ul,
        "ItemCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28025, version=0)
class Microsoft_Windows_Shell_Core_28025_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28026, version=0)
class Microsoft_Windows_Shell_Core_28026_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "Code" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28027, version=0)
class Microsoft_Windows_Shell_Core_28027_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "Event" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28028, version=0)
class Microsoft_Windows_Shell_Core_28028_0(Etw):
    pattern = Struct(
        "Identity" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28029, version=0)
class Microsoft_Windows_Shell_Core_28029_0(Etw):
    pattern = Struct(
        "InstalledVersion" / Int32sl,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28030, version=0)
class Microsoft_Windows_Shell_Core_28030_0(Etw):
    pattern = Struct(
        "StoreVersion" / Int32sl,
        "InstalledVersion" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28031, version=0)
class Microsoft_Windows_Shell_Core_28031_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "Event" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28032, version=0)
class Microsoft_Windows_Shell_Core_28032_0(Etw):
    pattern = Struct(
        "Filename" / WString,
        "SchemaType" / Int32ul,
        "ErrorCode" / Int32ul,
        "Failurereason" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28107, version=0)
class Microsoft_Windows_Shell_Core_28107_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "Code" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28109, version=0)
class Microsoft_Windows_Shell_Core_28109_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "OldState" / Int32ul,
        "NewState" / Int32ul,
        "PackageName" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28111, version=0)
class Microsoft_Windows_Shell_Core_28111_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "OldState" / Int32ul,
        "NewState" / Int32ul,
        "PackageName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28115, version=0)
class Microsoft_Windows_Shell_Core_28115_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "AppID" / WString,
        "Flags" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28116, version=0)
class Microsoft_Windows_Shell_Core_28116_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "AppID" / WString,
        "Flags" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28117, version=0)
class Microsoft_Windows_Shell_Core_28117_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "AppID" / WString,
        "Flags" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28119, version=0)
class Microsoft_Windows_Shell_Core_28119_0(Etw):
    pattern = Struct(
        "Groups" / Int32sl,
        "Tiles" / Int32sl,
        "Placeholders" / Int32sl,
        "Flags" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28123, version=0)
class Microsoft_Windows_Shell_Core_28123_0(Etw):
    pattern = Struct(
        "ItemsExisting" / Int32sl,
        "ItemsAdded" / Int32sl,
        "ItemsRemoved" / Int32sl,
        "ItemsUpdated" / Int32sl,
        "ItemsCached" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28125, version=0)
class Microsoft_Windows_Shell_Core_28125_0(Etw):
    pattern = Struct(
        "Scenario" / Int32sl,
        "Flags" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28127, version=0)
class Microsoft_Windows_Shell_Core_28127_0(Etw):
    pattern = Struct(
        "UpdateSource" / Int32sl,
        "RetryCount" / Int32sl,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28189, version=0)
class Microsoft_Windows_Shell_Core_28189_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28191, version=0)
class Microsoft_Windows_Shell_Core_28191_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28193, version=0)
class Microsoft_Windows_Shell_Core_28193_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=28195, version=0)
class Microsoft_Windows_Shell_Core_28195_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=50201, version=0)
class Microsoft_Windows_Shell_Core_50201_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=50202, version=0)
class Microsoft_Windows_Shell_Core_50202_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=50203, version=0)
class Microsoft_Windows_Shell_Core_50203_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=50204, version=0)
class Microsoft_Windows_Shell_Core_50204_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=50205, version=0)
class Microsoft_Windows_Shell_Core_50205_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=50206, version=0)
class Microsoft_Windows_Shell_Core_50206_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=50207, version=0)
class Microsoft_Windows_Shell_Core_50207_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=50208, version=0)
class Microsoft_Windows_Shell_Core_50208_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60216, version=0)
class Microsoft_Windows_Shell_Core_60216_0(Etw):
    pattern = Struct(
        "CLSIDTextService" / Guid,
        "LangId" / Int32ul,
        "LangProfile" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60217, version=0)
class Microsoft_Windows_Shell_Core_60217_0(Etw):
    pattern = Struct(
        "CLSIDTextService" / Guid,
        "LangId" / Int32ul,
        "LangProfile" / Guid,
        "HRESULT" / Int32ul,
        "QueryLen" / Int32ul,
        "AltCount" / Int32ul,
        "ReasonCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60218, version=0)
class Microsoft_Windows_Shell_Core_60218_0(Etw):
    pattern = Struct(
        "AnimId" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60219, version=0)
class Microsoft_Windows_Shell_Core_60219_0(Etw):
    pattern = Struct(
        "AnimId" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60220, version=0)
class Microsoft_Windows_Shell_Core_60220_0(Etw):
    pattern = Struct(
        "ElemId" / Int32ul,
        "IsUILess" / Int8ul,
        "IsIntegratable" / Int8ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60221, version=0)
class Microsoft_Windows_Shell_Core_60221_0(Etw):
    pattern = Struct(
        "ElemId" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60222, version=0)
class Microsoft_Windows_Shell_Core_60222_0(Etw):
    pattern = Struct(
        "ElemId" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60401, version=0)
class Microsoft_Windows_Shell_Core_60401_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60501, version=0)
class Microsoft_Windows_Shell_Core_60501_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60503, version=0)
class Microsoft_Windows_Shell_Core_60503_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60603, version=0)
class Microsoft_Windows_Shell_Core_60603_0(Etw):
    pattern = Struct(
        "Events" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60604, version=0)
class Microsoft_Windows_Shell_Core_60604_0(Etw):
    pattern = Struct(
        "Events" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60606, version=0)
class Microsoft_Windows_Shell_Core_60606_0(Etw):
    pattern = Struct(
        "Events" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60612, version=0)
class Microsoft_Windows_Shell_Core_60612_0(Etw):
    pattern = Struct(
        "Flushed" / Int32ul,
        "Skipped" / Int32ul,
        "Batched" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60631, version=0)
class Microsoft_Windows_Shell_Core_60631_0(Etw):
    pattern = Struct(
        "ANIMATIONTYPE" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60632, version=0)
class Microsoft_Windows_Shell_Core_60632_0(Etw):
    pattern = Struct(
        "ANIMATIONTYPE" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60633, version=0)
class Microsoft_Windows_Shell_Core_60633_0(Etw):
    pattern = Struct(
        "ANIMATIONTYPE" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60634, version=0)
class Microsoft_Windows_Shell_Core_60634_0(Etw):
    pattern = Struct(
        "ANIMATIONTYPE" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60636, version=0)
class Microsoft_Windows_Shell_Core_60636_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60638, version=0)
class Microsoft_Windows_Shell_Core_60638_0(Etw):
    pattern = Struct(
        "AnimationTime" / Int32ul,
        "Frames" / Int32ul,
        "Framerate" / Double,
        "BackBuffersUsed" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60641, version=0)
class Microsoft_Windows_Shell_Core_60641_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60648, version=0)
class Microsoft_Windows_Shell_Core_60648_0(Etw):
    pattern = Struct(
        "SetRedrawCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60653, version=0)
class Microsoft_Windows_Shell_Core_60653_0(Etw):
    pattern = Struct(
        "Items" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60659, version=0)
class Microsoft_Windows_Shell_Core_60659_0(Etw):
    pattern = Struct(
        "MonitorID" / Int32ul,
        "Left" / Int32sl,
        "Top" / Int32sl,
        "Right" / Int32sl,
        "Bottom" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60661, version=0)
class Microsoft_Windows_Shell_Core_60661_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60705, version=0)
class Microsoft_Windows_Shell_Core_60705_0(Etw):
    pattern = Struct(
        "WorkItem" / WString,
        "HRESULT" / Int32ul,
        "TimeToNextTick" / Int32ul,
        "Paused" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60706, version=0)
class Microsoft_Windows_Shell_Core_60706_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60707, version=0)
class Microsoft_Windows_Shell_Core_60707_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60708, version=0)
class Microsoft_Windows_Shell_Core_60708_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60709, version=0)
class Microsoft_Windows_Shell_Core_60709_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60710, version=0)
class Microsoft_Windows_Shell_Core_60710_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60711, version=0)
class Microsoft_Windows_Shell_Core_60711_0(Etw):
    pattern = Struct(
        "dwColorChosen" / Int32ul,
        "pszFilePath" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60714, version=0)
class Microsoft_Windows_Shell_Core_60714_0(Etw):
    pattern = Struct(
        "pszFilePath" / WString,
        "uImageWidth" / Int32ul,
        "uImageHeight" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60715, version=0)
class Microsoft_Windows_Shell_Core_60715_0(Etw):
    pattern = Struct(
        "fFillChosenOverFit" / Int8ul,
        "pszFilePath" / WString,
        "uImageWidth" / Int32ul,
        "uImageHeight" / Int32ul,
        "uMonitorWidth" / Int32ul,
        "uMonitorHeight" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60716, version=0)
class Microsoft_Windows_Shell_Core_60716_0(Etw):
    pattern = Struct(
        "uPicturePosition" / Int32ul,
        "pszFilePath" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60753, version=0)
class Microsoft_Windows_Shell_Core_60753_0(Etw):
    pattern = Struct(
        "pszBranchToRun" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60754, version=0)
class Microsoft_Windows_Shell_Core_60754_0(Etw):
    pattern = Struct(
        "pszBranchToRun" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60755, version=0)
class Microsoft_Windows_Shell_Core_60755_0(Etw):
    pattern = Struct(
        "pszKeyName" / WString,
        "activeSetupDisabled" / Int8ul,
        "allowTaskOverride" / Int8ul,
        "taskEnabled" / Int8ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60756, version=0)
class Microsoft_Windows_Shell_Core_60756_0(Etw):
    pattern = Struct(
        "pszKeyName" / WString,
        "activeSetupDisabled" / Int8ul,
        "allowTaskOverride" / Int8ul,
        "taskEnabled" / Int8ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60759, version=0)
class Microsoft_Windows_Shell_Core_60759_0(Etw):
    pattern = Struct(
        "pszPathName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60760, version=0)
class Microsoft_Windows_Shell_Core_60760_0(Etw):
    pattern = Struct(
        "pszPathName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60803, version=0)
class Microsoft_Windows_Shell_Core_60803_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60805, version=0)
class Microsoft_Windows_Shell_Core_60805_0(Etw):
    pattern = Struct(
        "PageIndex" / Int32sl,
        "InteractionType" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60806, version=0)
class Microsoft_Windows_Shell_Core_60806_0(Etw):
    pattern = Struct(
        "Index" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60808, version=0)
class Microsoft_Windows_Shell_Core_60808_0(Etw):
    pattern = Struct(
        "Index" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60809, version=0)
class Microsoft_Windows_Shell_Core_60809_0(Etw):
    pattern = Struct(
        "CandidateCount" / Int32sl,
        "CandidateToFocusIndex" / Int32sl,
        "PageToFocusIndex" / Int32sl,
        "InteractionType" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60811, version=0)
class Microsoft_Windows_Shell_Core_60811_0(Etw):
    pattern = Struct(
        "Index" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60812, version=0)
class Microsoft_Windows_Shell_Core_60812_0(Etw):
    pattern = Struct(
        "PageCount" / Int32sl,
        "CandidateCount" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60813, version=0)
class Microsoft_Windows_Shell_Core_60813_0(Etw):
    pattern = Struct(
        "PageCount" / Int32sl,
        "CandidateCount" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60814, version=0)
class Microsoft_Windows_Shell_Core_60814_0(Etw):
    pattern = Struct(
        "Index" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60815, version=0)
class Microsoft_Windows_Shell_Core_60815_0(Etw):
    pattern = Struct(
        "Index" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60816, version=0)
class Microsoft_Windows_Shell_Core_60816_0(Etw):
    pattern = Struct(
        "PageCount" / Int32sl,
        "CandidateCount" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60818, version=0)
class Microsoft_Windows_Shell_Core_60818_0(Etw):
    pattern = Struct(
        "PageCount" / Int32sl,
        "CandidateCount" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60819, version=0)
class Microsoft_Windows_Shell_Core_60819_0(Etw):
    pattern = Struct(
        "ButtonType" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60820, version=0)
class Microsoft_Windows_Shell_Core_60820_0(Etw):
    pattern = Struct(
        "ButtonType" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60825, version=0)
class Microsoft_Windows_Shell_Core_60825_0(Etw):
    pattern = Struct(
        "PageIndex" / Int32sl,
        "Type" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60826, version=0)
class Microsoft_Windows_Shell_Core_60826_0(Etw):
    pattern = Struct(
        "PageIndex" / Int32sl,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60901, version=0)
class Microsoft_Windows_Shell_Core_60901_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60902, version=0)
class Microsoft_Windows_Shell_Core_60902_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60903, version=0)
class Microsoft_Windows_Shell_Core_60903_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60904, version=0)
class Microsoft_Windows_Shell_Core_60904_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60905, version=0)
class Microsoft_Windows_Shell_Core_60905_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60906, version=0)
class Microsoft_Windows_Shell_Core_60906_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60907, version=0)
class Microsoft_Windows_Shell_Core_60907_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60908, version=0)
class Microsoft_Windows_Shell_Core_60908_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60909, version=0)
class Microsoft_Windows_Shell_Core_60909_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60910, version=0)
class Microsoft_Windows_Shell_Core_60910_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60911, version=0)
class Microsoft_Windows_Shell_Core_60911_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60912, version=0)
class Microsoft_Windows_Shell_Core_60912_0(Etw):
    pattern = Struct(
        "Index" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60914, version=0)
class Microsoft_Windows_Shell_Core_60914_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=60915, version=0)
class Microsoft_Windows_Shell_Core_60915_0(Etw):
    pattern = Struct(
        "EnumValue" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61004, version=0)
class Microsoft_Windows_Shell_Core_61004_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61006, version=0)
class Microsoft_Windows_Shell_Core_61006_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61204, version=0)
class Microsoft_Windows_Shell_Core_61204_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "Name" / WString,
        "Description" / WString,
        "AppliesTo" / WString,
        "State" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61205, version=0)
class Microsoft_Windows_Shell_Core_61205_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61210, version=0)
class Microsoft_Windows_Shell_Core_61210_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "State" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61211, version=0)
class Microsoft_Windows_Shell_Core_61211_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "ItemPath" / WString,
        "ScopeAffetcedItems" / Int32ul,
        "ItemSyncState" / Int32ul,
        "ItemSyncStatus" / WString,
        "ItemSyncStatusDescription" / WString,
        "ItemSyncStatusAction" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61212, version=0)
class Microsoft_Windows_Shell_Core_61212_0(Etw):
    pattern = Struct(
        "ItemPath" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61213, version=0)
class Microsoft_Windows_Shell_Core_61213_0(Etw):
    pattern = Struct(
        "ItemPath" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61214, version=0)
class Microsoft_Windows_Shell_Core_61214_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61220, version=0)
class Microsoft_Windows_Shell_Core_61220_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "State" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61221, version=0)
class Microsoft_Windows_Shell_Core_61221_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "ItemPath" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61301, version=0)
class Microsoft_Windows_Shell_Core_61301_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61340, version=0)
class Microsoft_Windows_Shell_Core_61340_0(Etw):
    pattern = Struct(
        "TileID" / Int32ul,
        "TileCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61341, version=0)
class Microsoft_Windows_Shell_Core_61341_0(Etw):
    pattern = Struct(
        "TileID" / Int32ul,
        "TileCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61342, version=0)
class Microsoft_Windows_Shell_Core_61342_0(Etw):
    pattern = Struct(
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61344, version=0)
class Microsoft_Windows_Shell_Core_61344_0(Etw):
    pattern = Struct(
        "IsEnthusiastMode" / Int8ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61345, version=0)
class Microsoft_Windows_Shell_Core_61345_0(Etw):
    pattern = Struct(
        "TileID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61346, version=0)
class Microsoft_Windows_Shell_Core_61346_0(Etw):
    pattern = Struct(
        "TileID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61347, version=0)
class Microsoft_Windows_Shell_Core_61347_0(Etw):
    pattern = Struct(
        "TileID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61348, version=0)
class Microsoft_Windows_Shell_Core_61348_0(Etw):
    pattern = Struct(
        "TileID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61349, version=0)
class Microsoft_Windows_Shell_Core_61349_0(Etw):
    pattern = Struct(
        "TileID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61350, version=0)
class Microsoft_Windows_Shell_Core_61350_0(Etw):
    pattern = Struct(
        "TileID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61351, version=0)
class Microsoft_Windows_Shell_Core_61351_0(Etw):
    pattern = Struct(
        "TileID" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61352, version=0)
class Microsoft_Windows_Shell_Core_61352_0(Etw):
    pattern = Struct(
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61353, version=0)
class Microsoft_Windows_Shell_Core_61353_0(Etw):
    pattern = Struct(
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61354, version=0)
class Microsoft_Windows_Shell_Core_61354_0(Etw):
    pattern = Struct(
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61355, version=0)
class Microsoft_Windows_Shell_Core_61355_0(Etw):
    pattern = Struct(
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61356, version=0)
class Microsoft_Windows_Shell_Core_61356_0(Etw):
    pattern = Struct(
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61357, version=0)
class Microsoft_Windows_Shell_Core_61357_0(Etw):
    pattern = Struct(
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61358, version=0)
class Microsoft_Windows_Shell_Core_61358_0(Etw):
    pattern = Struct(
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61360, version=0)
class Microsoft_Windows_Shell_Core_61360_0(Etw):
    pattern = Struct(
        "TopViewId" / Guid,
        "NumExtensionFilters" / Int32ul,
        "AppQuery" / WString,
        "UserQuery" / WString,
        "FolderDepth" / Int32ul,
        "IndexerOption" / Int32ul,
        "NumSortEntries" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61361, version=0)
class Microsoft_Windows_Shell_Core_61361_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61364, version=0)
class Microsoft_Windows_Shell_Core_61364_0(Etw):
    pattern = Struct(
        "StartIndex" / Int32ul,
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61365, version=0)
class Microsoft_Windows_Shell_Core_61365_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61367, version=0)
class Microsoft_Windows_Shell_Core_61367_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61369, version=0)
class Microsoft_Windows_Shell_Core_61369_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61371, version=0)
class Microsoft_Windows_Shell_Core_61371_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61372, version=0)
class Microsoft_Windows_Shell_Core_61372_0(Etw):
    pattern = Struct(
        "CountBytesRequested" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61373, version=0)
class Microsoft_Windows_Shell_Core_61373_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61374, version=0)
class Microsoft_Windows_Shell_Core_61374_0(Etw):
    pattern = Struct(
        "CountBytesRequested" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61375, version=0)
class Microsoft_Windows_Shell_Core_61375_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61377, version=0)
class Microsoft_Windows_Shell_Core_61377_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61381, version=0)
class Microsoft_Windows_Shell_Core_61381_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61387, version=0)
class Microsoft_Windows_Shell_Core_61387_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61391, version=0)
class Microsoft_Windows_Shell_Core_61391_0(Etw):
    pattern = Struct(
        "KnownItemRequested" / Guid,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61400, version=0)
class Microsoft_Windows_Shell_Core_61400_0(Etw):
    pattern = Struct(
        "RequestedSize" / Int32ul,
        "Options" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61401, version=0)
class Microsoft_Windows_Shell_Core_61401_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61411, version=0)
class Microsoft_Windows_Shell_Core_61411_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61413, version=0)
class Microsoft_Windows_Shell_Core_61413_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61415, version=0)
class Microsoft_Windows_Shell_Core_61415_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61421, version=0)
class Microsoft_Windows_Shell_Core_61421_0(Etw):
    pattern = Struct(
        "Token" / WString,
        "LifetimeOption" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61423, version=0)
class Microsoft_Windows_Shell_Core_61423_0(Etw):
    pattern = Struct(
        "Token" / WString,
        "LifetimeOption" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61425, version=0)
class Microsoft_Windows_Shell_Core_61425_0(Etw):
    pattern = Struct(
        "Token" / WString,
        "LifetimeOption" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61427, version=0)
class Microsoft_Windows_Shell_Core_61427_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61428, version=0)
class Microsoft_Windows_Shell_Core_61428_0(Etw):
    pattern = Struct(
        "Token" / WString,
        "LifetimeOption" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61429, version=0)
class Microsoft_Windows_Shell_Core_61429_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61431, version=0)
class Microsoft_Windows_Shell_Core_61431_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "LifetimeOption" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61433, version=0)
class Microsoft_Windows_Shell_Core_61433_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61435, version=0)
class Microsoft_Windows_Shell_Core_61435_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61437, version=0)
class Microsoft_Windows_Shell_Core_61437_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61439, version=0)
class Microsoft_Windows_Shell_Core_61439_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61441, version=0)
class Microsoft_Windows_Shell_Core_61441_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61443, version=0)
class Microsoft_Windows_Shell_Core_61443_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61449, version=0)
class Microsoft_Windows_Shell_Core_61449_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61451, version=0)
class Microsoft_Windows_Shell_Core_61451_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61453, version=0)
class Microsoft_Windows_Shell_Core_61453_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61454, version=0)
class Microsoft_Windows_Shell_Core_61454_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61455, version=0)
class Microsoft_Windows_Shell_Core_61455_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "HasAccess" / Int8ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61456, version=0)
class Microsoft_Windows_Shell_Core_61456_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61457, version=0)
class Microsoft_Windows_Shell_Core_61457_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61460, version=0)
class Microsoft_Windows_Shell_Core_61460_0(Etw):
    pattern = Struct(
        "Signature" / Int64ul,
        "szFilename" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61462, version=0)
class Microsoft_Windows_Shell_Core_61462_0(Etw):
    pattern = Struct(
        "Signature" / Int64ul,
        "szFilename" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61463, version=0)
class Microsoft_Windows_Shell_Core_61463_0(Etw):
    pattern = Struct(
        "Signature" / Int64ul,
        "szFilename" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61464, version=0)
class Microsoft_Windows_Shell_Core_61464_0(Etw):
    pattern = Struct(
        "Signature" / Int64ul,
        "szFilename" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61465, version=0)
class Microsoft_Windows_Shell_Core_61465_0(Etw):
    pattern = Struct(
        "Signature" / Int64ul,
        "szFilename" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61618, version=0)
class Microsoft_Windows_Shell_Core_61618_0(Etw):
    pattern = Struct(
        "FormatId" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61619, version=0)
class Microsoft_Windows_Shell_Core_61619_0(Etw):
    pattern = Struct(
        "FormatId" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61620, version=0)
class Microsoft_Windows_Shell_Core_61620_0(Etw):
    pattern = Struct(
        "FormatId" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61621, version=0)
class Microsoft_Windows_Shell_Core_61621_0(Etw):
    pattern = Struct(
        "FormatId" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61641, version=0)
class Microsoft_Windows_Shell_Core_61641_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=61649, version=0)
class Microsoft_Windows_Shell_Core_61649_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32sl
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62020, version=0)
class Microsoft_Windows_Shell_Core_62020_0(Etw):
    pattern = Struct(
        "psi" / Int64ul,
        "grfMode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62021, version=0)
class Microsoft_Windows_Shell_Core_62021_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62022, version=0)
class Microsoft_Windows_Shell_Core_62022_0(Etw):
    pattern = Struct(
        "Index" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62023, version=0)
class Microsoft_Windows_Shell_Core_62023_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62024, version=0)
class Microsoft_Windows_Shell_Core_62024_0(Etw):
    pattern = Struct(
        "Index" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62025, version=0)
class Microsoft_Windows_Shell_Core_62025_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62026, version=0)
class Microsoft_Windows_Shell_Core_62026_0(Etw):
    pattern = Struct(
        "Index" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62027, version=0)
class Microsoft_Windows_Shell_Core_62027_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62028, version=0)
class Microsoft_Windows_Shell_Core_62028_0(Etw):
    pattern = Struct(
        "IndexFrom" / Int32ul,
        "IndexTo" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62029, version=0)
class Microsoft_Windows_Shell_Core_62029_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62031, version=0)
class Microsoft_Windows_Shell_Core_62031_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62032, version=0)
class Microsoft_Windows_Shell_Core_62032_0(Etw):
    pattern = Struct(
        "psiFolder" / Int64ul,
        "szPlaylistName" / WString,
        "flags" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62033, version=0)
class Microsoft_Windows_Shell_Core_62033_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62072, version=0)
class Microsoft_Windows_Shell_Core_62072_0(Etw):
    pattern = Struct(
        "TileAutomationID" / Int32ul,
        "TransitionType" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62073, version=0)
class Microsoft_Windows_Shell_Core_62073_0(Etw):
    pattern = Struct(
        "TileAutomationID" / Int32ul,
        "TransitionType" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62074, version=0)
class Microsoft_Windows_Shell_Core_62074_0(Etw):
    pattern = Struct(
        "TileAutomationID" / Int32ul,
        "TransitionType" / Int32ul,
        "AnimationStatus" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62075, version=0)
class Microsoft_Windows_Shell_Core_62075_0(Etw):
    pattern = Struct(
        "Delta" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62076, version=0)
class Microsoft_Windows_Shell_Core_62076_0(Etw):
    pattern = Struct(
        "UInt32Value" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62100, version=0)
class Microsoft_Windows_Shell_Core_62100_0(Etw):
    pattern = Struct(
        "Device" / Int32ul,
        "GotRealDevice" / Int32ul,
        "VerticalResolution" / Int32ul,
        "HorizontalResolution" / Int32ul,
        "VerticalSize" / Int32ul,
        "HorizontalSize" / Int32ul,
        "ComputedScaleFactor" / Int32ul,
        "ComputedDPI" / Int32ul,
        "ChangedFlags" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62120, version=0)
class Microsoft_Windows_Shell_Core_62120_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62121, version=0)
class Microsoft_Windows_Shell_Core_62121_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62122, version=0)
class Microsoft_Windows_Shell_Core_62122_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62123, version=0)
class Microsoft_Windows_Shell_Core_62123_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62124, version=0)
class Microsoft_Windows_Shell_Core_62124_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62125, version=0)
class Microsoft_Windows_Shell_Core_62125_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62126, version=0)
class Microsoft_Windows_Shell_Core_62126_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62127, version=0)
class Microsoft_Windows_Shell_Core_62127_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62128, version=0)
class Microsoft_Windows_Shell_Core_62128_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62129, version=0)
class Microsoft_Windows_Shell_Core_62129_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62130, version=0)
class Microsoft_Windows_Shell_Core_62130_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62131, version=0)
class Microsoft_Windows_Shell_Core_62131_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62132, version=0)
class Microsoft_Windows_Shell_Core_62132_0(Etw):
    pattern = Struct(
        "ParentShortcutPath" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62133, version=0)
class Microsoft_Windows_Shell_Core_62133_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62134, version=0)
class Microsoft_Windows_Shell_Core_62134_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62135, version=0)
class Microsoft_Windows_Shell_Core_62135_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62136, version=0)
class Microsoft_Windows_Shell_Core_62136_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62137, version=0)
class Microsoft_Windows_Shell_Core_62137_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62138, version=0)
class Microsoft_Windows_Shell_Core_62138_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62139, version=0)
class Microsoft_Windows_Shell_Core_62139_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62140, version=0)
class Microsoft_Windows_Shell_Core_62140_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62141, version=0)
class Microsoft_Windows_Shell_Core_62141_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62142, version=0)
class Microsoft_Windows_Shell_Core_62142_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62143, version=0)
class Microsoft_Windows_Shell_Core_62143_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62144, version=0)
class Microsoft_Windows_Shell_Core_62144_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "InstallState" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62145, version=0)
class Microsoft_Windows_Shell_Core_62145_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62146, version=0)
class Microsoft_Windows_Shell_Core_62146_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62147, version=0)
class Microsoft_Windows_Shell_Core_62147_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62148, version=0)
class Microsoft_Windows_Shell_Core_62148_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62149, version=0)
class Microsoft_Windows_Shell_Core_62149_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62150, version=0)
class Microsoft_Windows_Shell_Core_62150_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62151, version=0)
class Microsoft_Windows_Shell_Core_62151_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62152, version=0)
class Microsoft_Windows_Shell_Core_62152_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62153, version=0)
class Microsoft_Windows_Shell_Core_62153_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62154, version=0)
class Microsoft_Windows_Shell_Core_62154_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62155, version=0)
class Microsoft_Windows_Shell_Core_62155_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62156, version=0)
class Microsoft_Windows_Shell_Core_62156_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62157, version=0)
class Microsoft_Windows_Shell_Core_62157_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62158, version=0)
class Microsoft_Windows_Shell_Core_62158_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62159, version=0)
class Microsoft_Windows_Shell_Core_62159_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62160, version=0)
class Microsoft_Windows_Shell_Core_62160_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62161, version=0)
class Microsoft_Windows_Shell_Core_62161_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62162, version=0)
class Microsoft_Windows_Shell_Core_62162_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62163, version=0)
class Microsoft_Windows_Shell_Core_62163_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Path" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62164, version=0)
class Microsoft_Windows_Shell_Core_62164_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62170, version=0)
class Microsoft_Windows_Shell_Core_62170_0(Etw):
    pattern = Struct(
        "LogonType" / Int32ul,
        "TaskName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62171, version=0)
class Microsoft_Windows_Shell_Core_62171_0(Etw):
    pattern = Struct(
        "LogonType" / Int32ul,
        "TaskName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62200, version=0)
class Microsoft_Windows_Shell_Core_62200_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62201, version=0)
class Microsoft_Windows_Shell_Core_62201_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62202, version=0)
class Microsoft_Windows_Shell_Core_62202_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62203, version=0)
class Microsoft_Windows_Shell_Core_62203_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62250, version=0)
class Microsoft_Windows_Shell_Core_62250_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62251, version=0)
class Microsoft_Windows_Shell_Core_62251_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62252, version=0)
class Microsoft_Windows_Shell_Core_62252_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62320, version=0)
class Microsoft_Windows_Shell_Core_62320_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62321, version=0)
class Microsoft_Windows_Shell_Core_62321_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62323, version=0)
class Microsoft_Windows_Shell_Core_62323_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62324, version=0)
class Microsoft_Windows_Shell_Core_62324_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "NewValues" / Int32ul,
        "ValuesToChange" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62325, version=0)
class Microsoft_Windows_Shell_Core_62325_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62326, version=0)
class Microsoft_Windows_Shell_Core_62326_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62327, version=0)
class Microsoft_Windows_Shell_Core_62327_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62328, version=0)
class Microsoft_Windows_Shell_Core_62328_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62329, version=0)
class Microsoft_Windows_Shell_Core_62329_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62330, version=0)
class Microsoft_Windows_Shell_Core_62330_0(Etw):
    pattern = Struct(
        "Position" / Int64ul,
        "Size" / Int64ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62331, version=0)
class Microsoft_Windows_Shell_Core_62331_0(Etw):
    pattern = Struct(
        "Position" / Int64ul,
        "Size" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62332, version=0)
class Microsoft_Windows_Shell_Core_62332_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62333, version=0)
class Microsoft_Windows_Shell_Core_62333_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62335, version=0)
class Microsoft_Windows_Shell_Core_62335_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "FileCompletionState" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62336, version=0)
class Microsoft_Windows_Shell_Core_62336_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "FileCompletionState" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62380, version=0)
class Microsoft_Windows_Shell_Core_62380_0(Etw):
    pattern = Struct(
        "QuestionID" / Int32sl,
        "ResponseType" / WString,
        "QuestionType" / WString,
        "Answer" / WString,
        "FollowupAnswer" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62400, version=0)
class Microsoft_Windows_Shell_Core_62400_0(Etw):
    pattern = Struct(
        "Source" / WString,
        "Experience" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62401, version=0)
class Microsoft_Windows_Shell_Core_62401_0(Etw):
    pattern = Struct(
        "Result" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62402, version=0)
class Microsoft_Windows_Shell_Core_62402_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62403, version=0)
class Microsoft_Windows_Shell_Core_62403_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62404, version=0)
class Microsoft_Windows_Shell_Core_62404_0(Etw):
    pattern = Struct(
        "CXID" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62405, version=0)
class Microsoft_Windows_Shell_Core_62405_0(Etw):
    pattern = Struct(
        "Result" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62406, version=0)
class Microsoft_Windows_Shell_Core_62406_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62407, version=0)
class Microsoft_Windows_Shell_Core_62407_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62408, version=0)
class Microsoft_Windows_Shell_Core_62408_0(Etw):
    pattern = Struct(
        "Command" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62409, version=0)
class Microsoft_Windows_Shell_Core_62409_0(Etw):
    pattern = Struct(
        "PID" / Int32ul,
        "Command" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62421, version=0)
class Microsoft_Windows_Shell_Core_62421_0(Etw):
    pattern = Struct(
        "ApplicableProfileCount" / Int32ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62422, version=0)
class Microsoft_Windows_Shell_Core_62422_0(Etw):
    pattern = Struct(
        "FormFactor" / Int32ul,
        "DeviceName" / WString,
        "OEMName" / WString,
        "HardwareId" / WString,
        "SystemDatewMonth" / Int16ul,
        "SystemDatewDay" / Int16ul,
        "SystemDatewYear" / Int16ul,
        "SystemDatewHour" / Int16ul,
        "SystemDatewMinute" / Int16ul,
        "SystemDatewSecond" / Int16ul
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62423, version=0)
class Microsoft_Windows_Shell_Core_62423_0(Etw):
    pattern = Struct(
        "HardwareId" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62440, version=0)
class Microsoft_Windows_Shell_Core_62440_0(Etw):
    pattern = Struct(
        "ExtOrUriScheme" / WString,
        "ProgId" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62441, version=0)
class Microsoft_Windows_Shell_Core_62441_0(Etw):
    pattern = Struct(
        "ProgId" / WString,
        "ExtOrUriScheme" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62442, version=0)
class Microsoft_Windows_Shell_Core_62442_0(Etw):
    pattern = Struct(
        "ProgId" / WString,
        "CurrentDefaultProgId" / WString,
        "ExtOrUriScheme" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62443, version=0)
class Microsoft_Windows_Shell_Core_62443_0(Etw):
    pattern = Struct(
        "Info" / WString
    )


@declare(guid=guid("30336ed4-e327-447c-9de0-51b652c86108"), event_id=62460, version=0)
class Microsoft_Windows_Shell_Core_62460_0(Etw):
    pattern = Struct(
        "DataVersion" / Int32sl,
        "HealthStateFlags" / Int64ul,
        "CensusFlags" / Int64ul,
        "SecondsSinceBoot" / Int64ul,
        "ImageIdentifier" / WString,
        "TrackingInfo" / WString
    )

