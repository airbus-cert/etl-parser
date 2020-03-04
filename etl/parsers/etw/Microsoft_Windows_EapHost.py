# -*- coding: utf-8 -*-
"""
Microsoft-Windows-EapHost
GUID : 6eb8db94-fe96-443f-a366-5fe0cee7fb1c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1003, version=0)
class Microsoft_Windows_EapHost_1003_0(Etw):
    pattern = Struct(
        "MethodString" / WString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1021, version=0)
class Microsoft_Windows_EapHost_1021_0(Etw):
    pattern = Struct(
        "RegistryKey" / WString,
        "ErrorCode" / Int8sl
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1022, version=0)
class Microsoft_Windows_EapHost_1022_0(Etw):
    pattern = Struct(
        "RegKeyValue" / WString,
        "TypeId" / Int8ul,
        "AuthorId" / Int32ul,
        "VendorId" / Int32ul,
        "VendorType" / Int32ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1023, version=0)
class Microsoft_Windows_EapHost_1023_0(Etw):
    pattern = Struct(
        "RegKeyValue" / WString,
        "TypeId" / Int8ul,
        "AuthorId" / Int32ul,
        "VendorId" / Int32ul,
        "VendorType" / Int32ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1043, version=0)
class Microsoft_Windows_EapHost_1043_0(Etw):
    pattern = Struct(
        "ErrorString" / WString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1044, version=0)
class Microsoft_Windows_EapHost_1044_0(Etw):
    pattern = Struct(
        "Length" / Int32sl
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1046, version=0)
class Microsoft_Windows_EapHost_1046_0(Etw):
    pattern = Struct(
        "NAK" / Int8ul,
        "Accept" / Int8ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1048, version=0)
class Microsoft_Windows_EapHost_1048_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "state" / Int8sl,
        "PacketID" / Int8ul,
        "PacketLength" / Int16ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1049, version=0)
class Microsoft_Windows_EapHost_1049_0(Etw):
    pattern = Struct(
        "PacketId" / Int8ul,
        "PacketLength" / Int16ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1052, version=0)
class Microsoft_Windows_EapHost_1052_0(Etw):
    pattern = Struct(
        "TypeId" / Int8ul,
        "AuthorId" / Int32ul,
        "VendorId" / Int32ul,
        "VendorType" / Int32ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1054, version=0)
class Microsoft_Windows_EapHost_1054_0(Etw):
    pattern = Struct(
        "TypeId" / Int8ul,
        "VendorId" / Int32ul,
        "VendorType" / Int32ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1055, version=0)
class Microsoft_Windows_EapHost_1055_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1056, version=0)
class Microsoft_Windows_EapHost_1056_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1057, version=0)
class Microsoft_Windows_EapHost_1057_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1058, version=0)
class Microsoft_Windows_EapHost_1058_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1059, version=0)
class Microsoft_Windows_EapHost_1059_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1060, version=0)
class Microsoft_Windows_EapHost_1060_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1061, version=0)
class Microsoft_Windows_EapHost_1061_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1062, version=0)
class Microsoft_Windows_EapHost_1062_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1063, version=0)
class Microsoft_Windows_EapHost_1063_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1064, version=0)
class Microsoft_Windows_EapHost_1064_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1065, version=0)
class Microsoft_Windows_EapHost_1065_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1066, version=0)
class Microsoft_Windows_EapHost_1066_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1067, version=0)
class Microsoft_Windows_EapHost_1067_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1068, version=0)
class Microsoft_Windows_EapHost_1068_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1069, version=0)
class Microsoft_Windows_EapHost_1069_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1070, version=0)
class Microsoft_Windows_EapHost_1070_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1071, version=0)
class Microsoft_Windows_EapHost_1071_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1072, version=0)
class Microsoft_Windows_EapHost_1072_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1073, version=0)
class Microsoft_Windows_EapHost_1073_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1074, version=0)
class Microsoft_Windows_EapHost_1074_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1075, version=0)
class Microsoft_Windows_EapHost_1075_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1076, version=0)
class Microsoft_Windows_EapHost_1076_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1077, version=0)
class Microsoft_Windows_EapHost_1077_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1078, version=0)
class Microsoft_Windows_EapHost_1078_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1079, version=0)
class Microsoft_Windows_EapHost_1079_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1080, version=0)
class Microsoft_Windows_EapHost_1080_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1081, version=0)
class Microsoft_Windows_EapHost_1081_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1082, version=0)
class Microsoft_Windows_EapHost_1082_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1083, version=0)
class Microsoft_Windows_EapHost_1083_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1084, version=0)
class Microsoft_Windows_EapHost_1084_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1085, version=0)
class Microsoft_Windows_EapHost_1085_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1086, version=0)
class Microsoft_Windows_EapHost_1086_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1087, version=0)
class Microsoft_Windows_EapHost_1087_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1088, version=0)
class Microsoft_Windows_EapHost_1088_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1089, version=0)
class Microsoft_Windows_EapHost_1089_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1090, version=0)
class Microsoft_Windows_EapHost_1090_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1091, version=0)
class Microsoft_Windows_EapHost_1091_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=1092, version=0)
class Microsoft_Windows_EapHost_1092_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2001, version=0)
class Microsoft_Windows_EapHost_2001_0(Etw):
    pattern = Struct(
        "KeyName" / CString,
        "TypeId" / Int8ul,
        "AuthorId" / Int32ul,
        "VendorId" / Int32ul,
        "VendorType" / Int32ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2002, version=0)
class Microsoft_Windows_EapHost_2002_0(Etw):
    pattern = Struct(
        "KeyName" / CString,
        "TypeId" / Int8ul,
        "AuthorId" / Int32ul,
        "VendorId" / Int32ul,
        "VendorType" / Int32ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2005, version=0)
class Microsoft_Windows_EapHost_2005_0(Etw):
    pattern = Struct(
        "Connection" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2006, version=0)
class Microsoft_Windows_EapHost_2006_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2008, version=0)
class Microsoft_Windows_EapHost_2008_0(Etw):
    pattern = Struct(
        "ConnectionName" / WString,
        "SessionID" / Int32sl
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2009, version=0)
class Microsoft_Windows_EapHost_2009_0(Etw):
    pattern = Struct(
        "FunctionName" / CString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2014, version=0)
class Microsoft_Windows_EapHost_2014_0(Etw):
    pattern = Struct(
        "ConnectionName" / WString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2016, version=0)
class Microsoft_Windows_EapHost_2016_0(Etw):
    pattern = Struct(
        "ConnectionName" / WString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2017, version=0)
class Microsoft_Windows_EapHost_2017_0(Etw):
    pattern = Struct(
        "SessionID" / Int32sl
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2018, version=0)
class Microsoft_Windows_EapHost_2018_0(Etw):
    pattern = Struct(
        "SessionID" / Int32sl,
        "ServerOfferedMethod" / Int32sl,
        "ClientRequestedMethod" / CString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2019, version=0)
class Microsoft_Windows_EapHost_2019_0(Etw):
    pattern = Struct(
        "FunctionName" / CString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2020, version=0)
class Microsoft_Windows_EapHost_2020_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorDescription" / WString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2022, version=0)
class Microsoft_Windows_EapHost_2022_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2023, version=0)
class Microsoft_Windows_EapHost_2023_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2024, version=0)
class Microsoft_Windows_EapHost_2024_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorDescription" / WString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2026, version=0)
class Microsoft_Windows_EapHost_2026_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2027, version=0)
class Microsoft_Windows_EapHost_2027_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2028, version=0)
class Microsoft_Windows_EapHost_2028_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2029, version=0)
class Microsoft_Windows_EapHost_2029_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2030, version=0)
class Microsoft_Windows_EapHost_2030_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2031, version=0)
class Microsoft_Windows_EapHost_2031_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2032, version=0)
class Microsoft_Windows_EapHost_2032_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2033, version=0)
class Microsoft_Windows_EapHost_2033_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2034, version=0)
class Microsoft_Windows_EapHost_2034_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2035, version=0)
class Microsoft_Windows_EapHost_2035_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2036, version=0)
class Microsoft_Windows_EapHost_2036_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2037, version=0)
class Microsoft_Windows_EapHost_2037_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2038, version=0)
class Microsoft_Windows_EapHost_2038_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2039, version=0)
class Microsoft_Windows_EapHost_2039_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2040, version=0)
class Microsoft_Windows_EapHost_2040_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2041, version=0)
class Microsoft_Windows_EapHost_2041_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2042, version=0)
class Microsoft_Windows_EapHost_2042_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2043, version=0)
class Microsoft_Windows_EapHost_2043_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2044, version=0)
class Microsoft_Windows_EapHost_2044_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2045, version=0)
class Microsoft_Windows_EapHost_2045_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2046, version=0)
class Microsoft_Windows_EapHost_2046_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2047, version=0)
class Microsoft_Windows_EapHost_2047_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2048, version=0)
class Microsoft_Windows_EapHost_2048_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2049, version=0)
class Microsoft_Windows_EapHost_2049_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2050, version=0)
class Microsoft_Windows_EapHost_2050_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2051, version=0)
class Microsoft_Windows_EapHost_2051_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2052, version=0)
class Microsoft_Windows_EapHost_2052_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2053, version=0)
class Microsoft_Windows_EapHost_2053_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2054, version=0)
class Microsoft_Windows_EapHost_2054_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2055, version=0)
class Microsoft_Windows_EapHost_2055_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2056, version=0)
class Microsoft_Windows_EapHost_2056_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2057, version=0)
class Microsoft_Windows_EapHost_2057_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2058, version=0)
class Microsoft_Windows_EapHost_2058_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2059, version=0)
class Microsoft_Windows_EapHost_2059_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2060, version=0)
class Microsoft_Windows_EapHost_2060_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2061, version=0)
class Microsoft_Windows_EapHost_2061_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2062, version=0)
class Microsoft_Windows_EapHost_2062_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2063, version=0)
class Microsoft_Windows_EapHost_2063_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2064, version=0)
class Microsoft_Windows_EapHost_2064_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2065, version=0)
class Microsoft_Windows_EapHost_2065_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2066, version=0)
class Microsoft_Windows_EapHost_2066_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2067, version=0)
class Microsoft_Windows_EapHost_2067_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2068, version=0)
class Microsoft_Windows_EapHost_2068_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2069, version=0)
class Microsoft_Windows_EapHost_2069_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2070, version=0)
class Microsoft_Windows_EapHost_2070_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2071, version=0)
class Microsoft_Windows_EapHost_2071_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2072, version=0)
class Microsoft_Windows_EapHost_2072_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2073, version=0)
class Microsoft_Windows_EapHost_2073_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2074, version=0)
class Microsoft_Windows_EapHost_2074_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2075, version=0)
class Microsoft_Windows_EapHost_2075_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2076, version=0)
class Microsoft_Windows_EapHost_2076_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2077, version=0)
class Microsoft_Windows_EapHost_2077_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2078, version=0)
class Microsoft_Windows_EapHost_2078_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2079, version=0)
class Microsoft_Windows_EapHost_2079_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2080, version=0)
class Microsoft_Windows_EapHost_2080_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2081, version=0)
class Microsoft_Windows_EapHost_2081_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2082, version=0)
class Microsoft_Windows_EapHost_2082_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2083, version=0)
class Microsoft_Windows_EapHost_2083_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2084, version=0)
class Microsoft_Windows_EapHost_2084_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2085, version=0)
class Microsoft_Windows_EapHost_2085_0(Etw):
    pattern = Struct(
        "PerfId" / Int64ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=2086, version=0)
class Microsoft_Windows_EapHost_2086_0(Etw):
    pattern = Struct(
        "ReasonCode" / Int32ul,
        "EAPMethodFriendlyName" / WString,
        "EAPErrorRootCause" / WString,
        "EAPErrorRepair" / WString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=3001, version=0)
class Microsoft_Windows_EapHost_3001_0(Etw):
    pattern = Struct(
        "ModuleName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=3002, version=0)
class Microsoft_Windows_EapHost_3002_0(Etw):
    pattern = Struct(
        "TypeId" / Int8ul,
        "AuthorId" / Int32ul,
        "VendorId" / Int32ul,
        "VendorType" / Int32ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=3021, version=0)
class Microsoft_Windows_EapHost_3021_0(Etw):
    pattern = Struct(
        "RegistryKey" / WString,
        "ErrorCode" / Int8sl
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=3022, version=0)
class Microsoft_Windows_EapHost_3022_0(Etw):
    pattern = Struct(
        "TypeId" / WString,
        "AuthorId" / WString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=3023, version=0)
class Microsoft_Windows_EapHost_3023_0(Etw):
    pattern = Struct(
        "AuthorId" / WString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=3024, version=0)
class Microsoft_Windows_EapHost_3024_0(Etw):
    pattern = Struct(
        "AuthorId" / Int32ul,
        "VendorId" / WString,
        "VendorType" / WString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=3025, version=0)
class Microsoft_Windows_EapHost_3025_0(Etw):
    pattern = Struct(
        "AuthorId" / Int32ul,
        "VendorId" / WString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=3026, version=0)
class Microsoft_Windows_EapHost_3026_0(Etw):
    pattern = Struct(
        "TypeId" / Int8ul,
        "AuthorId" / Int32ul,
        "VendorId" / Int32ul,
        "VendorType" / Int32ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=3027, version=0)
class Microsoft_Windows_EapHost_3027_0(Etw):
    pattern = Struct(
        "ErrorString" / WString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=3028, version=0)
class Microsoft_Windows_EapHost_3028_0(Etw):
    pattern = Struct(
        "debugString" / CString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=3029, version=0)
class Microsoft_Windows_EapHost_3029_0(Etw):
    pattern = Struct(
        "TypeId" / Int8ul,
        "AuthorId" / Int32ul,
        "VendorId" / Int32ul,
        "VendorType" / Int32ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=3043, version=0)
class Microsoft_Windows_EapHost_3043_0(Etw):
    pattern = Struct(
        "AuthorId" / Int32ul,
        "TypeId" / Int8ul,
        "VendorId" / Int32ul,
        "VendorType" / Int32ul,
        "ErrorString" / WString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=3044, version=0)
class Microsoft_Windows_EapHost_3044_0(Etw):
    pattern = Struct(
        "AuthorId" / Int32ul,
        "TypeId" / Int8ul,
        "VendorId" / Int32ul,
        "VendorType" / Int32ul,
        "ErrorString" / WString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=3045, version=0)
class Microsoft_Windows_EapHost_3045_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int8ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=3048, version=0)
class Microsoft_Windows_EapHost_3048_0(Etw):
    pattern = Struct(
        "TypeId" / Int8ul,
        "AuthorId" / Int32ul,
        "VendorId" / Int32ul,
        "VendorType" / Int32ul
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=4001, version=0)
class Microsoft_Windows_EapHost_4001_0(Etw):
    pattern = Struct(
        "debugString" / CString
    )


@declare(guid=guid("6eb8db94-fe96-443f-a366-5fe0cee7fb1c"), event_id=4002, version=0)
class Microsoft_Windows_EapHost_4002_0(Etw):
    pattern = Struct(
        "debugString" / CString
    )

