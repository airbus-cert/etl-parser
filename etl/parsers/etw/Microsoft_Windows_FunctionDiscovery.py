# -*- coding: utf-8 -*-
"""
Microsoft-Windows-FunctionDiscovery
GUID : 9db0fdb5-3b21-440e-a94b-63738a4be5de
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1000, version=0)
class Microsoft_Windows_FunctionDiscovery_1000_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString,
        "IncludeSubcategories" / Int8ul
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1001, version=0)
class Microsoft_Windows_FunctionDiscovery_1001_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString,
        "IncludeSubcategories" / Int8ul
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1002, version=0)
class Microsoft_Windows_FunctionDiscovery_1002_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1003, version=0)
class Microsoft_Windows_FunctionDiscovery_1003_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1004, version=0)
class Microsoft_Windows_FunctionDiscovery_1004_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString,
        "IncludeSubcategories" / Int8ul
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1005, version=0)
class Microsoft_Windows_FunctionDiscovery_1005_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString,
        "IncludeSubcategories" / Int8ul
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1006, version=0)
class Microsoft_Windows_FunctionDiscovery_1006_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1007, version=0)
class Microsoft_Windows_FunctionDiscovery_1007_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1008, version=0)
class Microsoft_Windows_FunctionDiscovery_1008_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString,
        "ProviderInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1009, version=0)
class Microsoft_Windows_FunctionDiscovery_1009_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString,
        "ProviderInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1010, version=0)
class Microsoft_Windows_FunctionDiscovery_1010_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString,
        "ProviderInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1011, version=0)
class Microsoft_Windows_FunctionDiscovery_1011_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString,
        "ProviderInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1012, version=0)
class Microsoft_Windows_FunctionDiscovery_1012_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1013, version=0)
class Microsoft_Windows_FunctionDiscovery_1013_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1014, version=0)
class Microsoft_Windows_FunctionDiscovery_1014_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1015, version=0)
class Microsoft_Windows_FunctionDiscovery_1015_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1016, version=0)
class Microsoft_Windows_FunctionDiscovery_1016_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1017, version=0)
class Microsoft_Windows_FunctionDiscovery_1017_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1018, version=0)
class Microsoft_Windows_FunctionDiscovery_1018_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1019, version=0)
class Microsoft_Windows_FunctionDiscovery_1019_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1020, version=0)
class Microsoft_Windows_FunctionDiscovery_1020_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1021, version=0)
class Microsoft_Windows_FunctionDiscovery_1021_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1022, version=0)
class Microsoft_Windows_FunctionDiscovery_1022_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1023, version=0)
class Microsoft_Windows_FunctionDiscovery_1023_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1024, version=0)
class Microsoft_Windows_FunctionDiscovery_1024_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1025, version=0)
class Microsoft_Windows_FunctionDiscovery_1025_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1026, version=0)
class Microsoft_Windows_FunctionDiscovery_1026_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1027, version=0)
class Microsoft_Windows_FunctionDiscovery_1027_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1028, version=0)
class Microsoft_Windows_FunctionDiscovery_1028_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1029, version=0)
class Microsoft_Windows_FunctionDiscovery_1029_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1030, version=0)
class Microsoft_Windows_FunctionDiscovery_1030_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1031, version=0)
class Microsoft_Windows_FunctionDiscovery_1031_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1032, version=0)
class Microsoft_Windows_FunctionDiscovery_1032_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1033, version=0)
class Microsoft_Windows_FunctionDiscovery_1033_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1034, version=0)
class Microsoft_Windows_FunctionDiscovery_1034_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1035, version=0)
class Microsoft_Windows_FunctionDiscovery_1035_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1036, version=0)
class Microsoft_Windows_FunctionDiscovery_1036_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1037, version=0)
class Microsoft_Windows_FunctionDiscovery_1037_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1038, version=0)
class Microsoft_Windows_FunctionDiscovery_1038_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1039, version=0)
class Microsoft_Windows_FunctionDiscovery_1039_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1040, version=0)
class Microsoft_Windows_FunctionDiscovery_1040_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1041, version=0)
class Microsoft_Windows_FunctionDiscovery_1041_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1042, version=0)
class Microsoft_Windows_FunctionDiscovery_1042_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString,
        "ProviderInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1043, version=0)
class Microsoft_Windows_FunctionDiscovery_1043_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString,
        "ProviderInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1044, version=0)
class Microsoft_Windows_FunctionDiscovery_1044_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString,
        "ProviderInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1045, version=0)
class Microsoft_Windows_FunctionDiscovery_1045_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString,
        "ProviderInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1046, version=0)
class Microsoft_Windows_FunctionDiscovery_1046_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1047, version=0)
class Microsoft_Windows_FunctionDiscovery_1047_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1048, version=0)
class Microsoft_Windows_FunctionDiscovery_1048_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1049, version=0)
class Microsoft_Windows_FunctionDiscovery_1049_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1050, version=0)
class Microsoft_Windows_FunctionDiscovery_1050_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1051, version=0)
class Microsoft_Windows_FunctionDiscovery_1051_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1052, version=0)
class Microsoft_Windows_FunctionDiscovery_1052_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString,
        "fmtid" / Guid,
        "pid" / Int32ul
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1053, version=0)
class Microsoft_Windows_FunctionDiscovery_1053_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString,
        "fmtid" / Guid,
        "pid" / Int32ul
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1054, version=0)
class Microsoft_Windows_FunctionDiscovery_1054_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString,
        "fmtid" / Guid,
        "pid" / Int32ul
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1055, version=0)
class Microsoft_Windows_FunctionDiscovery_1055_0(Etw):
    pattern = Struct(
        "FunctionInstanceID" / WString,
        "fmtid" / Guid,
        "pid" / Int32ul
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1056, version=0)
class Microsoft_Windows_FunctionDiscovery_1056_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString,
        "querycookie" / Int64ul
    )


@declare(guid=guid("9db0fdb5-3b21-440e-a94b-63738a4be5de"), event_id=1057, version=0)
class Microsoft_Windows_FunctionDiscovery_1057_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Subcategory" / WString,
        "querycookie" / Int64ul
    )

