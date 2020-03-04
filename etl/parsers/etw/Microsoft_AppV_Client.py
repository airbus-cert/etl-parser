# -*- coding: utf-8 -*-
"""
Microsoft-AppV-Client
GUID : e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=3, version=1)
class Microsoft_AppV_Client_3_1(Etw):
    pattern = Struct(
        "Item" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=4, version=1)
class Microsoft_AppV_Client_4_1(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=5, version=1)
class Microsoft_AppV_Client_5_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=6, version=1)
class Microsoft_AppV_Client_6_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=7, version=1)
class Microsoft_AppV_Client_7_1(Etw):
    pattern = Struct(
        "Error" / Int32sl
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=8, version=1)
class Microsoft_AppV_Client_8_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=9, version=1)
class Microsoft_AppV_Client_9_1(Etw):
    pattern = Struct(
        "CurrentImpersonationLevel" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=11, version=1)
class Microsoft_AppV_Client_11_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=12, version=1)
class Microsoft_AppV_Client_12_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=13, version=0)
class Microsoft_AppV_Client_13_0(Etw):
    pattern = Struct(
        "Error" / Int32sl
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=16, version=1)
class Microsoft_AppV_Client_16_1(Etw):
    pattern = Struct(
        "StringParam" / WString,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=17, version=1)
class Microsoft_AppV_Client_17_1(Etw):
    pattern = Struct(
        "StringParam1" / WString,
        "StringParam2" / WString,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=101, version=1)
class Microsoft_AppV_Client_101_1(Etw):
    pattern = Struct(
        "Item" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=102, version=1)
class Microsoft_AppV_Client_102_1(Etw):
    pattern = Struct(
        "Name" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1001, version=1)
class Microsoft_AppV_Client_1001_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1002, version=1)
class Microsoft_AppV_Client_1002_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "Folder" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1003, version=1)
class Microsoft_AppV_Client_1003_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1004, version=1)
class Microsoft_AppV_Client_1004_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1005, version=1)
class Microsoft_AppV_Client_1005_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1006, version=1)
class Microsoft_AppV_Client_1006_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1007, version=1)
class Microsoft_AppV_Client_1007_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1008, version=1)
class Microsoft_AppV_Client_1008_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "Folder" / WString,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1009, version=1)
class Microsoft_AppV_Client_1009_1(Etw):
    pattern = Struct(
        "PackageGroup" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1010, version=1)
class Microsoft_AppV_Client_1010_1(Etw):
    pattern = Struct(
        "PackageGroup" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1011, version=1)
class Microsoft_AppV_Client_1011_1(Etw):
    pattern = Struct(
        "PackageGroup" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1012, version=1)
class Microsoft_AppV_Client_1012_1(Etw):
    pattern = Struct(
        "PackageGroup" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1013, version=1)
class Microsoft_AppV_Client_1013_1(Etw):
    pattern = Struct(
        "PackageGroup" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1014, version=1)
class Microsoft_AppV_Client_1014_1(Etw):
    pattern = Struct(
        "PackageGroup" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1015, version=1)
class Microsoft_AppV_Client_1015_1(Etw):
    pattern = Struct(
        "PackageGroup" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1016, version=1)
class Microsoft_AppV_Client_1016_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1017, version=1)
class Microsoft_AppV_Client_1017_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1018, version=1)
class Microsoft_AppV_Client_1018_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ActivityID" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1019, version=1)
class Microsoft_AppV_Client_1019_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ActivityID" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1020, version=1)
class Microsoft_AppV_Client_1020_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ActivityID" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1021, version=1)
class Microsoft_AppV_Client_1021_1(Etw):
    pattern = Struct(
        "ConnectionGroup" / Guid,
        "Version" / Guid,
        "ActivityID" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1022, version=1)
class Microsoft_AppV_Client_1022_1(Etw):
    pattern = Struct(
        "ConnectionGroup" / Guid,
        "Version" / Guid,
        "ActivityID" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1023, version=1)
class Microsoft_AppV_Client_1023_1(Etw):
    pattern = Struct(
        "ConnectionGroup" / Guid,
        "Version" / Guid,
        "ActivityID" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1024, version=1)
class Microsoft_AppV_Client_1024_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1025, version=1)
class Microsoft_AppV_Client_1025_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1026, version=1)
class Microsoft_AppV_Client_1026_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1027, version=1)
class Microsoft_AppV_Client_1027_1(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Version" / Guid,
        "Path" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1028, version=1)
class Microsoft_AppV_Client_1028_1(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Version" / Guid,
        "Path" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1029, version=1)
class Microsoft_AppV_Client_1029_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1030, version=1)
class Microsoft_AppV_Client_1030_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1031, version=1)
class Microsoft_AppV_Client_1031_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1032, version=1)
class Microsoft_AppV_Client_1032_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1033, version=1)
class Microsoft_AppV_Client_1033_1(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Version" / Guid,
        "Path" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1034, version=1)
class Microsoft_AppV_Client_1034_1(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Version" / Guid,
        "Path" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1035, version=1)
class Microsoft_AppV_Client_1035_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1036, version=1)
class Microsoft_AppV_Client_1036_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1037, version=1)
class Microsoft_AppV_Client_1037_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1038, version=1)
class Microsoft_AppV_Client_1038_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1039, version=1)
class Microsoft_AppV_Client_1039_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1040, version=1)
class Microsoft_AppV_Client_1040_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1041, version=1)
class Microsoft_AppV_Client_1041_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1042, version=1)
class Microsoft_AppV_Client_1042_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1043, version=1)
class Microsoft_AppV_Client_1043_1(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Version" / Guid,
        "Path" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1044, version=1)
class Microsoft_AppV_Client_1044_1(Etw):
    pattern = Struct(
        "ConnectionGroup" / Guid,
        "GroupVersion" / Guid,
        "Package" / Guid,
        "PackageVersion" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1045, version=1)
class Microsoft_AppV_Client_1045_1(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Version" / Guid,
        "Path" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1046, version=1)
class Microsoft_AppV_Client_1046_1(Etw):
    pattern = Struct(
        "ConnectionGroup" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1047, version=1)
class Microsoft_AppV_Client_1047_1(Etw):
    pattern = Struct(
        "ConnectionGroup" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1048, version=1)
class Microsoft_AppV_Client_1048_1(Etw):
    pattern = Struct(
        "ConnectionGroup" / Guid,
        "GroupVersion" / Guid,
        "Package" / Guid,
        "PackageVersion" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1049, version=1)
class Microsoft_AppV_Client_1049_1(Etw):
    pattern = Struct(
        "ConnectionGroup" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1050, version=1)
class Microsoft_AppV_Client_1050_1(Etw):
    pattern = Struct(
        "ConnectionGroup" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1051, version=1)
class Microsoft_AppV_Client_1051_1(Etw):
    pattern = Struct(
        "ConnectionGroup" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1052, version=1)
class Microsoft_AppV_Client_1052_1(Etw):
    pattern = Struct(
        "ConnectionGroup" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1053, version=1)
class Microsoft_AppV_Client_1053_1(Etw):
    pattern = Struct(
        "ConnectionGroup" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1054, version=1)
class Microsoft_AppV_Client_1054_1(Etw):
    pattern = Struct(
        "ConnectionGroup" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1055, version=1)
class Microsoft_AppV_Client_1055_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ActivityID" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1056, version=1)
class Microsoft_AppV_Client_1056_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ActivityID" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1057, version=1)
class Microsoft_AppV_Client_1057_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1058, version=1)
class Microsoft_AppV_Client_1058_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1059, version=1)
class Microsoft_AppV_Client_1059_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1060, version=1)
class Microsoft_AppV_Client_1060_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1061, version=1)
class Microsoft_AppV_Client_1061_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ActivityID" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1062, version=1)
class Microsoft_AppV_Client_1062_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ActivityID" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1063, version=1)
class Microsoft_AppV_Client_1063_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ActivityID" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1064, version=1)
class Microsoft_AppV_Client_1064_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ActivityID" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1065, version=1)
class Microsoft_AppV_Client_1065_1(Etw):
    pattern = Struct(
        "ConnectionGroup" / Guid,
        "Version" / Guid,
        "ActivityID" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1066, version=1)
class Microsoft_AppV_Client_1066_1(Etw):
    pattern = Struct(
        "ConnectionGroup" / Guid,
        "Version" / Guid,
        "ActivityID" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1067, version=1)
class Microsoft_AppV_Client_1067_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ActivityID" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1068, version=1)
class Microsoft_AppV_Client_1068_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ActivityID" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1069, version=1)
class Microsoft_AppV_Client_1069_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ActivityID" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1070, version=1)
class Microsoft_AppV_Client_1070_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ActivityID" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1071, version=1)
class Microsoft_AppV_Client_1071_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1072, version=1)
class Microsoft_AppV_Client_1072_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1073, version=1)
class Microsoft_AppV_Client_1073_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1074, version=1)
class Microsoft_AppV_Client_1074_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ActivityID" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1075, version=1)
class Microsoft_AppV_Client_1075_1(Etw):
    pattern = Struct(
        "ConnectionGroup" / Guid,
        "Version" / Guid,
        "ActivityID" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1076, version=1)
class Microsoft_AppV_Client_1076_1(Etw):
    pattern = Struct(
        "StringParam" / WString,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1077, version=1)
class Microsoft_AppV_Client_1077_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1078, version=1)
class Microsoft_AppV_Client_1078_1(Etw):
    pattern = Struct(
        "PackageId" / Guid,
        "PackageVersion" / Guid,
        "GroupId" / Guid,
        "GroupVersion" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1079, version=1)
class Microsoft_AppV_Client_1079_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1080, version=1)
class Microsoft_AppV_Client_1080_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1082, version=1)
class Microsoft_AppV_Client_1082_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=1083, version=1)
class Microsoft_AppV_Client_1083_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=2001, version=1)
class Microsoft_AppV_Client_2001_1(Etw):
    pattern = Struct(
        "LastFolder" / WString,
        "ReqFolder" / WString,
        "Error" / Int32sl
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=2002, version=1)
class Microsoft_AppV_Client_2002_1(Etw):
    pattern = Struct(
        "LastFolder" / WString,
        "ReqFolder" / WString,
        "Error" / Int32sl
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=2003, version=1)
class Microsoft_AppV_Client_2003_1(Etw):
    pattern = Struct(
        "LastFolder" / WString,
        "ReqFolder" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=2004, version=1)
class Microsoft_AppV_Client_2004_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=2005, version=1)
class Microsoft_AppV_Client_2005_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=2006, version=1)
class Microsoft_AppV_Client_2006_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=3001, version=1)
class Microsoft_AppV_Client_3001_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=3002, version=1)
class Microsoft_AppV_Client_3002_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=4001, version=1)
class Microsoft_AppV_Client_4001_1(Etw):
    pattern = Struct(
        "ScriptScope" / Int32ul,
        "EventType" / WString,
        "CommandLine" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=4002, version=1)
class Microsoft_AppV_Client_4002_1(Etw):
    pattern = Struct(
        "Timeout" / Int64ul,
        "ScriptScope" / Int32ul,
        "EventType" / WString,
        "CommandLine" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=4004, version=1)
class Microsoft_AppV_Client_4004_1(Etw):
    pattern = Struct(
        "ScriptScope" / Int32ul,
        "Package" / Guid,
        "EventType" / WString,
        "UserSid" / WString,
        "CommandLine" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=4005, version=1)
class Microsoft_AppV_Client_4005_1(Etw):
    pattern = Struct(
        "ScriptScope" / Int32ul,
        "Package" / Guid,
        "EventType" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=4006, version=1)
class Microsoft_AppV_Client_4006_1(Etw):
    pattern = Struct(
        "tGuid" / Guid,
        "tString" / WString,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=4007, version=1)
class Microsoft_AppV_Client_4007_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=4008, version=1)
class Microsoft_AppV_Client_4008_1(Etw):
    pattern = Struct(
        "Timeout" / Int64ul,
        "ScriptScope" / Int32ul,
        "EventType" / WString,
        "CommandLine" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=4009, version=1)
class Microsoft_AppV_Client_4009_1(Etw):
    pattern = Struct(
        "ScriptScope" / Int32ul,
        "EventType" / WString,
        "CommandLine" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=4010, version=1)
class Microsoft_AppV_Client_4010_1(Etw):
    pattern = Struct(
        "ScriptScope" / Int32ul,
        "EventType" / WString,
        "CommandLine" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=5003, version=1)
class Microsoft_AppV_Client_5003_1(Etw):
    pattern = Struct(
        "Item" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=6001, version=1)
class Microsoft_AppV_Client_6001_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=6002, version=1)
class Microsoft_AppV_Client_6002_1(Etw):
    pattern = Struct(
        "Item" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=6006, version=1)
class Microsoft_AppV_Client_6006_1(Etw):
    pattern = Struct(
        "Item1" / WString,
        "Item2" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=6007, version=1)
class Microsoft_AppV_Client_6007_1(Etw):
    pattern = Struct(
        "Item1" / WString,
        "Item2" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=6008, version=1)
class Microsoft_AppV_Client_6008_1(Etw):
    pattern = Struct(
        "Item1" / WString,
        "Item2" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=6009, version=1)
class Microsoft_AppV_Client_6009_1(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=6010, version=1)
class Microsoft_AppV_Client_6010_1(Etw):
    pattern = Struct(
        "Item" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=6011, version=1)
class Microsoft_AppV_Client_6011_1(Etw):
    pattern = Struct(
        "Item" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=6012, version=1)
class Microsoft_AppV_Client_6012_1(Etw):
    pattern = Struct(
        "Item" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=6015, version=1)
class Microsoft_AppV_Client_6015_1(Etw):
    pattern = Struct(
        "Item" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=7001, version=1)
class Microsoft_AppV_Client_7001_1(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=8001, version=1)
class Microsoft_AppV_Client_8001_1(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "Reason" / WString,
        "line" / Int64sl,
        "column" / Int64sl,
        "offset" / Int64sl
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=8002, version=1)
class Microsoft_AppV_Client_8002_1(Etw):
    pattern = Struct(
        "Error" / Int32sl,
        "Reason" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=8003, version=1)
class Microsoft_AppV_Client_8003_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=8004, version=1)
class Microsoft_AppV_Client_8004_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=8005, version=1)
class Microsoft_AppV_Client_8005_1(Etw):
    pattern = Struct(
        "StringParam" / WString,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=8006, version=1)
class Microsoft_AppV_Client_8006_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=8007, version=1)
class Microsoft_AppV_Client_8007_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=8008, version=1)
class Microsoft_AppV_Client_8008_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=8009, version=1)
class Microsoft_AppV_Client_8009_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=8010, version=1)
class Microsoft_AppV_Client_8010_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=8011, version=1)
class Microsoft_AppV_Client_8011_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=8012, version=1)
class Microsoft_AppV_Client_8012_1(Etw):
    pattern = Struct(
        "ConnectionGroup" / Guid,
        "GroupVersion" / Guid,
        "Package" / Guid,
        "PackageVersion" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=8013, version=1)
class Microsoft_AppV_Client_8013_1(Etw):
    pattern = Struct(
        "ConnectionGroup" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul,
        "Sid" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=8014, version=1)
class Microsoft_AppV_Client_8014_1(Etw):
    pattern = Struct(
        "ConnectionGroup" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul,
        "Sid" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=8015, version=1)
class Microsoft_AppV_Client_8015_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=8016, version=1)
class Microsoft_AppV_Client_8016_1(Etw):
    pattern = Struct(
        "tString" / WString,
        "PackageId" / Guid,
        "PackageVersion" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=9001, version=1)
class Microsoft_AppV_Client_9001_1(Etw):
    pattern = Struct(
        "Command" / WString,
        "ErrorWarning" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=9002, version=1)
class Microsoft_AppV_Client_9002_1(Etw):
    pattern = Struct(
        "Command" / WString,
        "ErrorWarning" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=9009, version=1)
class Microsoft_AppV_Client_9009_1(Etw):
    pattern = Struct(
        "Item" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=9010, version=1)
class Microsoft_AppV_Client_9010_1(Etw):
    pattern = Struct(
        "Item" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=10001, version=1)
class Microsoft_AppV_Client_10001_1(Etw):
    pattern = Struct(
        "PID" / Int32ul,
        "Package" / Guid,
        "Version" / Guid,
        "SubsystemName" / WString,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=10002, version=1)
class Microsoft_AppV_Client_10002_1(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=11002, version=1)
class Microsoft_AppV_Client_11002_1(Etw):
    pattern = Struct(
        "Item" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=11003, version=1)
class Microsoft_AppV_Client_11003_1(Etw):
    pattern = Struct(
        "Item" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=11004, version=1)
class Microsoft_AppV_Client_11004_1(Etw):
    pattern = Struct(
        "Package" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=11005, version=1)
class Microsoft_AppV_Client_11005_1(Etw):
    pattern = Struct(
        "Item" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=11006, version=1)
class Microsoft_AppV_Client_11006_1(Etw):
    pattern = Struct(
        "Item" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=11007, version=1)
class Microsoft_AppV_Client_11007_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=11008, version=1)
class Microsoft_AppV_Client_11008_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=11009, version=1)
class Microsoft_AppV_Client_11009_1(Etw):
    pattern = Struct(
        "Item" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=11010, version=1)
class Microsoft_AppV_Client_11010_1(Etw):
    pattern = Struct(
        "Item" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=11011, version=1)
class Microsoft_AppV_Client_11011_1(Etw):
    pattern = Struct(
        "Item" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=11012, version=1)
class Microsoft_AppV_Client_11012_1(Etw):
    pattern = Struct(
        "Item" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=12001, version=1)
class Microsoft_AppV_Client_12001_1(Etw):
    pattern = Struct(
        "PackageGroup" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=13001, version=1)
class Microsoft_AppV_Client_13001_1(Etw):
    pattern = Struct(
        "Package" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=13002, version=1)
class Microsoft_AppV_Client_13002_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=13003, version=1)
class Microsoft_AppV_Client_13003_1(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "Package" / Guid,
        "Pid" / Int32ul,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=13004, version=1)
class Microsoft_AppV_Client_13004_1(Etw):
    pattern = Struct(
        "Item1" / WString,
        "Item2" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=13005, version=1)
class Microsoft_AppV_Client_13005_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=13006, version=1)
class Microsoft_AppV_Client_13006_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=13007, version=1)
class Microsoft_AppV_Client_13007_1(Etw):
    pattern = Struct(
        "Item" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=13008, version=1)
class Microsoft_AppV_Client_13008_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int64ul,
        "ErrorLow" / Int64ul,
        "ProcessID" / Int64ul,
        "PackageId" / Guid,
        "PackageVersion" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=13009, version=1)
class Microsoft_AppV_Client_13009_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=13010, version=1)
class Microsoft_AppV_Client_13010_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=13011, version=1)
class Microsoft_AppV_Client_13011_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=13012, version=1)
class Microsoft_AppV_Client_13012_1(Etw):
    pattern = Struct(
        "ConnectionGroup" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=14005, version=1)
class Microsoft_AppV_Client_14005_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int64ul,
        "ErrorLow" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=14010, version=1)
class Microsoft_AppV_Client_14010_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "Folder" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=14011, version=1)
class Microsoft_AppV_Client_14011_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=14012, version=1)
class Microsoft_AppV_Client_14012_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=14013, version=1)
class Microsoft_AppV_Client_14013_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=14014, version=1)
class Microsoft_AppV_Client_14014_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=14015, version=1)
class Microsoft_AppV_Client_14015_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "Folder" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=14016, version=1)
class Microsoft_AppV_Client_14016_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=14017, version=1)
class Microsoft_AppV_Client_14017_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "Hresult" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=14018, version=1)
class Microsoft_AppV_Client_14018_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=14019, version=1)
class Microsoft_AppV_Client_14019_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=14020, version=1)
class Microsoft_AppV_Client_14020_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=14021, version=1)
class Microsoft_AppV_Client_14021_1(Etw):
    pattern = Struct(
        "tGuid" / Guid,
        "tString" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=14022, version=1)
class Microsoft_AppV_Client_14022_1(Etw):
    pattern = Struct(
        "Error" / Int32sl
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=14023, version=1)
class Microsoft_AppV_Client_14023_1(Etw):
    pattern = Struct(
        "File" / WString,
        "Pid" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=14024, version=1)
class Microsoft_AppV_Client_14024_1(Etw):
    pattern = Struct(
        "File" / WString,
        "Pid" / Int64ul,
        "Sid" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=14029, version=1)
class Microsoft_AppV_Client_14029_1(Etw):
    pattern = Struct(
        "Item" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=15001, version=1)
class Microsoft_AppV_Client_15001_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int64ul,
        "ErrorLow" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=15002, version=1)
class Microsoft_AppV_Client_15002_1(Etw):
    pattern = Struct(
        "HResult" / Int32sl
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=15003, version=1)
class Microsoft_AppV_Client_15003_1(Etw):
    pattern = Struct(
        "VirtualEnvironmentId" / Guid,
        "VirtualEnvironmentVersion" / Guid,
        "ErrorHigh" / Int64ul,
        "ErrorLow" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=16001, version=1)
class Microsoft_AppV_Client_16001_1(Etw):
    pattern = Struct(
        "PackageGroup" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=16002, version=1)
class Microsoft_AppV_Client_16002_1(Etw):
    pattern = Struct(
        "PackageGroup" / Guid,
        "Version" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=16003, version=1)
class Microsoft_AppV_Client_16003_1(Etw):
    pattern = Struct(
        "PackageGroup" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=16004, version=1)
class Microsoft_AppV_Client_16004_1(Etw):
    pattern = Struct(
        "PackageId" / Guid,
        "PackageVersion" / Guid,
        "GroupId" / Guid,
        "GroupVersion" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=17001, version=1)
class Microsoft_AppV_Client_17001_1(Etw):
    pattern = Struct(
        "Item" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=17002, version=1)
class Microsoft_AppV_Client_17002_1(Etw):
    pattern = Struct(
        "StringParam" / WString,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=17003, version=1)
class Microsoft_AppV_Client_17003_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=17004, version=1)
class Microsoft_AppV_Client_17004_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=17006, version=1)
class Microsoft_AppV_Client_17006_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=17007, version=1)
class Microsoft_AppV_Client_17007_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=17008, version=1)
class Microsoft_AppV_Client_17008_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=17009, version=1)
class Microsoft_AppV_Client_17009_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=17010, version=1)
class Microsoft_AppV_Client_17010_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=17011, version=1)
class Microsoft_AppV_Client_17011_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=17012, version=1)
class Microsoft_AppV_Client_17012_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=18001, version=1)
class Microsoft_AppV_Client_18001_1(Etw):
    pattern = Struct(
        "Item" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=18002, version=1)
class Microsoft_AppV_Client_18002_1(Etw):
    pattern = Struct(
        "Item" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=18003, version=1)
class Microsoft_AppV_Client_18003_1(Etw):
    pattern = Struct(
        "Item" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=18004, version=1)
class Microsoft_AppV_Client_18004_1(Etw):
    pattern = Struct(
        "Item1" / WString,
        "Item2" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=18005, version=1)
class Microsoft_AppV_Client_18005_1(Etw):
    pattern = Struct(
        "StringParam1" / WString,
        "StringParam2" / WString,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=18006, version=1)
class Microsoft_AppV_Client_18006_1(Etw):
    pattern = Struct(
        "ConnectionGroup" / Guid,
        "GroupVersion" / Guid,
        "Package" / Guid,
        "PackageVersion" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19001, version=1)
class Microsoft_AppV_Client_19001_1(Etw):
    pattern = Struct(
        "String" / WString,
        "Flag" / Int8ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19002, version=1)
class Microsoft_AppV_Client_19002_1(Etw):
    pattern = Struct(
        "String" / WString,
        "Flag" / Int8ul,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19010, version=1)
class Microsoft_AppV_Client_19010_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int64ul,
        "ErrorLow" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19011, version=1)
class Microsoft_AppV_Client_19011_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int64ul,
        "ErrorLow" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19101, version=1)
class Microsoft_AppV_Client_19101_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int64ul,
        "ErrorLow" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19102, version=1)
class Microsoft_AppV_Client_19102_1(Etw):
    pattern = Struct(
        "StringParam" / WString,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19103, version=1)
class Microsoft_AppV_Client_19103_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int64ul,
        "ErrorLow" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19104, version=1)
class Microsoft_AppV_Client_19104_1(Etw):
    pattern = Struct(
        "Value1" / Int32ul,
        "Value2" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19105, version=1)
class Microsoft_AppV_Client_19105_1(Etw):
    pattern = Struct(
        "Value1" / Int32ul,
        "Value2" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19106, version=1)
class Microsoft_AppV_Client_19106_1(Etw):
    pattern = Struct(
        "Value1" / Int32ul,
        "Value2" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19107, version=1)
class Microsoft_AppV_Client_19107_1(Etw):
    pattern = Struct(
        "Value1" / Int32ul,
        "Value2" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19108, version=1)
class Microsoft_AppV_Client_19108_1(Etw):
    pattern = Struct(
        "Guid1" / Guid,
        "Guid2" / Guid,
        "Guid3" / Guid
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19201, version=1)
class Microsoft_AppV_Client_19201_1(Etw):
    pattern = Struct(
        "Item" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19202, version=1)
class Microsoft_AppV_Client_19202_1(Etw):
    pattern = Struct(
        "StringParam" / WString,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19203, version=1)
class Microsoft_AppV_Client_19203_1(Etw):
    pattern = Struct(
        "StringParam" / WString,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19204, version=1)
class Microsoft_AppV_Client_19204_1(Etw):
    pattern = Struct(
        "Item" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19205, version=1)
class Microsoft_AppV_Client_19205_1(Etw):
    pattern = Struct(
        "StringParam" / WString,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19301, version=1)
class Microsoft_AppV_Client_19301_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19302, version=1)
class Microsoft_AppV_Client_19302_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19303, version=1)
class Microsoft_AppV_Client_19303_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19304, version=1)
class Microsoft_AppV_Client_19304_1(Etw):
    pattern = Struct(
        "Package" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19401, version=1)
class Microsoft_AppV_Client_19401_1(Etw):
    pattern = Struct(
        "Value" / Int32ul,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19402, version=1)
class Microsoft_AppV_Client_19402_1(Etw):
    pattern = Struct(
        "Value" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19403, version=1)
class Microsoft_AppV_Client_19403_1(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19404, version=1)
class Microsoft_AppV_Client_19404_1(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19405, version=1)
class Microsoft_AppV_Client_19405_1(Etw):
    pattern = Struct(
        "Value1" / Int32ul,
        "Value2" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19406, version=1)
class Microsoft_AppV_Client_19406_1(Etw):
    pattern = Struct(
        "Value1" / Int32ul,
        "Value2" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19407, version=1)
class Microsoft_AppV_Client_19407_1(Etw):
    pattern = Struct(
        "Value1" / Int32ul,
        "Value2" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19408, version=1)
class Microsoft_AppV_Client_19408_1(Etw):
    pattern = Struct(
        "Item1" / WString,
        "Item2" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19501, version=1)
class Microsoft_AppV_Client_19501_1(Etw):
    pattern = Struct(
        "Item" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19502, version=1)
class Microsoft_AppV_Client_19502_1(Etw):
    pattern = Struct(
        "Item" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19801, version=1)
class Microsoft_AppV_Client_19801_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int64ul,
        "ErrorLow" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19802, version=1)
class Microsoft_AppV_Client_19802_1(Etw):
    pattern = Struct(
        "String" / WString,
        "Flag1" / Int8ul,
        "Flag2" / Int8ul,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19803, version=1)
class Microsoft_AppV_Client_19803_1(Etw):
    pattern = Struct(
        "String" / WString,
        "Flag1" / Int8ul,
        "Flag2" / Int8ul,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=19805, version=1)
class Microsoft_AppV_Client_19805_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int64ul,
        "ErrorLow" / Int64ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=20001, version=1)
class Microsoft_AppV_Client_20001_1(Etw):
    pattern = Struct(
        "PackageGroup" / Guid,
        "Version" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=20002, version=1)
class Microsoft_AppV_Client_20002_1(Etw):
    pattern = Struct(
        "PackageId" / Guid,
        "PackageVersion" / Guid,
        "GroupId" / Guid,
        "GroupVersion" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=20101, version=1)
class Microsoft_AppV_Client_20101_1(Etw):
    pattern = Struct(
        "PackageId" / Guid,
        "PackageVersion" / Guid,
        "GroupId" / Guid,
        "GroupVersion" / Guid,
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=21001, version=1)
class Microsoft_AppV_Client_21001_1(Etw):
    pattern = Struct(
        "ErrorHigh" / Int32ul,
        "ErrorLow" / Int32ul
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=22001, version=1)
class Microsoft_AppV_Client_22001_1(Etw):
    pattern = Struct(
        "Item1" / WString,
        "Item2" / WString
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=24001, version=1)
class Microsoft_AppV_Client_24001_1(Etw):
    pattern = Struct(
        "Error" / Int32sl
    )


@declare(guid=guid("e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245"), event_id=24002, version=1)
class Microsoft_AppV_Client_24002_1(Etw):
    pattern = Struct(
        "Error" / Int32sl
    )

