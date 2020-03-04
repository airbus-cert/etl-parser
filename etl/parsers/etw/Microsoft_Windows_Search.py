# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Search
GUID : ca4e628d-8567-4896-ab6b-835b221f373f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=1003, version=0)
class Microsoft_Windows_Search_1003_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=1004, version=0)
class Microsoft_Windows_Search_1004_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "Reason" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=1005, version=0)
class Microsoft_Windows_Search_1005_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=1006, version=0)
class Microsoft_Windows_Search_1006_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "Phase" / WString,
        "HR" / WString,
        "DiagnosticsInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=1007, version=0)
class Microsoft_Windows_Search_1007_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=1008, version=0)
class Microsoft_Windows_Search_1008_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "Reason" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=1009, version=0)
class Microsoft_Windows_Search_1009_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "Address" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=1010, version=0)
class Microsoft_Windows_Search_1010_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=1011, version=0)
class Microsoft_Windows_Search_1011_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "Phase" / WString,
        "HR" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=1013, version=0)
class Microsoft_Windows_Search_1013_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=1014, version=0)
class Microsoft_Windows_Search_1014_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "DebugInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=1015, version=0)
class Microsoft_Windows_Search_1015_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "EventID" / WString,
        "RepeatCount" / WString,
        "ReferenceTime" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=1016, version=0)
class Microsoft_Windows_Search_1016_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "OldIndexPath" / WString,
        "NewIndexPath" / WString,
        "Phase" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=1017, version=0)
class Microsoft_Windows_Search_1017_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "OldIndexPath" / WString,
        "NewIndexPath" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=1018, version=0)
class Microsoft_Windows_Search_1018_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "OldIndexPath" / WString,
        "NewIndexPath" / WString,
        "Phase" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=1019, version=0)
class Microsoft_Windows_Search_1019_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "Phase" / WString,
        "ErrorCode" / WString,
        "Path" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=1044, version=0)
class Microsoft_Windows_Search_1044_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "FileName" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=1053, version=0)
class Microsoft_Windows_Search_1053_0(Etw):
    pattern = Struct(
        "Code" / WString,
        "StackTrace" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3003, version=0)
class Microsoft_Windows_Search_3003_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3006, version=0)
class Microsoft_Windows_Search_3006_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3007, version=0)
class Microsoft_Windows_Search_3007_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3008, version=0)
class Microsoft_Windows_Search_3008_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "Entry" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3009, version=0)
class Microsoft_Windows_Search_3009_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3010, version=0)
class Microsoft_Windows_Search_3010_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "FilePath" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3011, version=0)
class Microsoft_Windows_Search_3011_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "FilePath" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3013, version=0)
class Microsoft_Windows_Search_3013_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "Entry" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3014, version=0)
class Microsoft_Windows_Search_3014_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "ID" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3015, version=0)
class Microsoft_Windows_Search_3015_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3020, version=0)
class Microsoft_Windows_Search_3020_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3023, version=0)
class Microsoft_Windows_Search_3023_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3024, version=0)
class Microsoft_Windows_Search_3024_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3025, version=0)
class Microsoft_Windows_Search_3025_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3026, version=0)
class Microsoft_Windows_Search_3026_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3027, version=0)
class Microsoft_Windows_Search_3027_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "URL" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3028, version=0)
class Microsoft_Windows_Search_3028_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3029, version=0)
class Microsoft_Windows_Search_3029_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "Plugin" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3030, version=0)
class Microsoft_Windows_Search_3030_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3031, version=0)
class Microsoft_Windows_Search_3031_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3032, version=0)
class Microsoft_Windows_Search_3032_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3033, version=0)
class Microsoft_Windows_Search_3033_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3034, version=0)
class Microsoft_Windows_Search_3034_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "ExpectedVersion" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3036, version=0)
class Microsoft_Windows_Search_3036_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "URL" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3037, version=0)
class Microsoft_Windows_Search_3037_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "URL" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3038, version=0)
class Microsoft_Windows_Search_3038_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "RegPath" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3039, version=0)
class Microsoft_Windows_Search_3039_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3040, version=0)
class Microsoft_Windows_Search_3040_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "RequestedStatusMessage" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3041, version=0)
class Microsoft_Windows_Search_3041_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3042, version=0)
class Microsoft_Windows_Search_3042_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3044, version=0)
class Microsoft_Windows_Search_3044_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3045, version=0)
class Microsoft_Windows_Search_3045_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "OldLength" / WString,
        "NewLength" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3046, version=0)
class Microsoft_Windows_Search_3046_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3048, version=0)
class Microsoft_Windows_Search_3048_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3050, version=0)
class Microsoft_Windows_Search_3050_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3052, version=0)
class Microsoft_Windows_Search_3052_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3053, version=0)
class Microsoft_Windows_Search_3053_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3054, version=0)
class Microsoft_Windows_Search_3054_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3055, version=0)
class Microsoft_Windows_Search_3055_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3056, version=0)
class Microsoft_Windows_Search_3056_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3057, version=0)
class Microsoft_Windows_Search_3057_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "PluginManager" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3058, version=0)
class Microsoft_Windows_Search_3058_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3059, version=0)
class Microsoft_Windows_Search_3059_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3060, version=0)
class Microsoft_Windows_Search_3060_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "URL" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3061, version=0)
class Microsoft_Windows_Search_3061_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3062, version=0)
class Microsoft_Windows_Search_3062_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "Locale" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3072, version=0)
class Microsoft_Windows_Search_3072_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3073, version=0)
class Microsoft_Windows_Search_3073_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3078, version=0)
class Microsoft_Windows_Search_3078_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3079, version=0)
class Microsoft_Windows_Search_3079_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "VolumeName" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3083, version=0)
class Microsoft_Windows_Search_3083_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "ProtocolHandler" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3084, version=0)
class Microsoft_Windows_Search_3084_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "ProtocolHandler" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3085, version=0)
class Microsoft_Windows_Search_3085_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3086, version=0)
class Microsoft_Windows_Search_3086_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3087, version=0)
class Microsoft_Windows_Search_3087_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3088, version=0)
class Microsoft_Windows_Search_3088_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3089, version=0)
class Microsoft_Windows_Search_3089_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3090, version=0)
class Microsoft_Windows_Search_3090_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3091, version=0)
class Microsoft_Windows_Search_3091_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3092, version=0)
class Microsoft_Windows_Search_3092_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3093, version=0)
class Microsoft_Windows_Search_3093_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3095, version=0)
class Microsoft_Windows_Search_3095_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "Domain" / WString,
        "Account" / WString,
        "Users" / WString,
        "MaxUsers" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3096, version=0)
class Microsoft_Windows_Search_3096_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "Reason" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3097, version=0)
class Microsoft_Windows_Search_3097_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3099, version=0)
class Microsoft_Windows_Search_3099_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=3100, version=0)
class Microsoft_Windows_Search_3100_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=4103, version=0)
class Microsoft_Windows_Search_4103_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "CatalogName" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=4104, version=0)
class Microsoft_Windows_Search_4104_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "CatalogName" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=4105, version=0)
class Microsoft_Windows_Search_4105_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "CatalogName" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=4106, version=0)
class Microsoft_Windows_Search_4106_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "CatalogName" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=4121, version=0)
class Microsoft_Windows_Search_4121_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "CatalogName" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=4138, version=0)
class Microsoft_Windows_Search_4138_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "Component" / WString,
        "CatalogName" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=4163, version=0)
class Microsoft_Windows_Search_4163_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "CatalogName" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=4164, version=0)
class Microsoft_Windows_Search_4164_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "CatalogName" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=4165, version=0)
class Microsoft_Windows_Search_4165_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "CatalogName" / WString,
        "IndexesPerMergeLevel" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=4166, version=0)
class Microsoft_Windows_Search_4166_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "CatalogName" / WString,
        "ExpectedDocCount" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=4167, version=0)
class Microsoft_Windows_Search_4167_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "CatalogName" / WString,
        "MasterMergeReason" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=4168, version=0)
class Microsoft_Windows_Search_4168_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "ErrorMessage" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=4169, version=0)
class Microsoft_Windows_Search_4169_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "Phase" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=7001, version=0)
class Microsoft_Windows_Search_7001_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "SrcFile" / WString,
        "DstFile" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=7010, version=0)
class Microsoft_Windows_Search_7010_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=7011, version=0)
class Microsoft_Windows_Search_7011_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "Directory" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=7013, version=0)
class Microsoft_Windows_Search_7013_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "Directory" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=7040, version=0)
class Microsoft_Windows_Search_7040_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "CorruptionId" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=7042, version=0)
class Microsoft_Windows_Search_7042_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "Reason" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=7043, version=0)
class Microsoft_Windows_Search_7043_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=7064, version=0)
class Microsoft_Windows_Search_7064_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=7066, version=0)
class Microsoft_Windows_Search_7066_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "Directory" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=7068, version=0)
class Microsoft_Windows_Search_7068_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=7070, version=0)
class Microsoft_Windows_Search_7070_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=7071, version=0)
class Microsoft_Windows_Search_7071_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=9000, version=0)
class Microsoft_Windows_Search_9000_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=9001, version=0)
class Microsoft_Windows_Search_9001_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=9002, version=0)
class Microsoft_Windows_Search_9002_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=9003, version=0)
class Microsoft_Windows_Search_9003_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=10013, version=0)
class Microsoft_Windows_Search_10013_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=10014, version=0)
class Microsoft_Windows_Search_10014_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "OldNoiseFile" / WString,
        "NewNoiseFile" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=10020, version=0)
class Microsoft_Windows_Search_10020_0(Etw):
    pattern = Struct(
        "Driver" / WString,
        "InstanceName" / WString,
        "InstanceNum" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=10021, version=0)
class Microsoft_Windows_Search_10021_0(Etw):
    pattern = Struct(
        "Driver" / WString,
        "InstanceName" / WString,
        "InstanceNum" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=10022, version=0)
class Microsoft_Windows_Search_10022_0(Etw):
    pattern = Struct(
        "Driver" / WString,
        "InstanceName" / WString,
        "InstanceNum" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=10023, version=0)
class Microsoft_Windows_Search_10023_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "ProtocolHostProcessID" / WString,
        "FilterHostProcessID" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=10024, version=0)
class Microsoft_Windows_Search_10024_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "FilterHostProcessID" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=10025, version=0)
class Microsoft_Windows_Search_10025_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=10026, version=0)
class Microsoft_Windows_Search_10026_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=10027, version=0)
class Microsoft_Windows_Search_10027_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "SID" / WString
    )


@declare(guid=guid("ca4e628d-8567-4896-ab6b-835b221f373f"), event_id=10028, version=0)
class Microsoft_Windows_Search_10028_0(Etw):
    pattern = Struct(
        "ExtraInfo" / WString,
        "SID" / WString
    )

