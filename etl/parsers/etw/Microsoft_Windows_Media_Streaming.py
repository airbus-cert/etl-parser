# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Media-Streaming
GUID : 982824e5-e446-46ae-bc74-836401ffb7b6
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1001, version=0)
class Microsoft_Windows_Media_Streaming_1001_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1003, version=0)
class Microsoft_Windows_Media_Streaming_1003_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1005, version=0)
class Microsoft_Windows_Media_Streaming_1005_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1007, version=0)
class Microsoft_Windows_Media_Streaming_1007_0(Etw):
    pattern = Struct(
        "UDN" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1009, version=0)
class Microsoft_Windows_Media_Streaming_1009_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1011, version=0)
class Microsoft_Windows_Media_Streaming_1011_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1013, version=0)
class Microsoft_Windows_Media_Streaming_1013_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1015, version=0)
class Microsoft_Windows_Media_Streaming_1015_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1020, version=0)
class Microsoft_Windows_Media_Streaming_1020_0(Etw):
    pattern = Struct(
        "instanceID" / Int32ul,
        "String" / WString,
        "ui32" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1021, version=0)
class Microsoft_Windows_Media_Streaming_1021_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1022, version=0)
class Microsoft_Windows_Media_Streaming_1022_0(Etw):
    pattern = Struct(
        "instanceID" / Int32ul,
        "String" / WString,
        "ui32" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1023, version=0)
class Microsoft_Windows_Media_Streaming_1023_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1040, version=0)
class Microsoft_Windows_Media_Streaming_1040_0(Etw):
    pattern = Struct(
        "URI" / WString,
        "URIMetadata" / WString
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1041, version=0)
class Microsoft_Windows_Media_Streaming_1041_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1042, version=0)
class Microsoft_Windows_Media_Streaming_1042_0(Etw):
    pattern = Struct(
        "instanceID" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1043, version=0)
class Microsoft_Windows_Media_Streaming_1043_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1044, version=0)
class Microsoft_Windows_Media_Streaming_1044_0(Etw):
    pattern = Struct(
        "instanceID" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1045, version=0)
class Microsoft_Windows_Media_Streaming_1045_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1046, version=0)
class Microsoft_Windows_Media_Streaming_1046_0(Etw):
    pattern = Struct(
        "instanceID" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1047, version=0)
class Microsoft_Windows_Media_Streaming_1047_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1048, version=0)
class Microsoft_Windows_Media_Streaming_1048_0(Etw):
    pattern = Struct(
        "instanceID" / Int32ul,
        "String1" / WString,
        "String2" / WString
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1049, version=0)
class Microsoft_Windows_Media_Streaming_1049_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1050, version=0)
class Microsoft_Windows_Media_Streaming_1050_0(Etw):
    pattern = Struct(
        "instanceID" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1051, version=0)
class Microsoft_Windows_Media_Streaming_1051_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1052, version=0)
class Microsoft_Windows_Media_Streaming_1052_0(Etw):
    pattern = Struct(
        "instanceID" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1053, version=0)
class Microsoft_Windows_Media_Streaming_1053_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1054, version=0)
class Microsoft_Windows_Media_Streaming_1054_0(Etw):
    pattern = Struct(
        "instanceID" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1055, version=0)
class Microsoft_Windows_Media_Streaming_1055_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1057, version=0)
class Microsoft_Windows_Media_Streaming_1057_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=1058, version=0)
class Microsoft_Windows_Media_Streaming_1058_0(Etw):
    pattern = Struct(
        "dispid" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3000, version=0)
class Microsoft_Windows_Media_Streaming_3000_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3001, version=0)
class Microsoft_Windows_Media_Streaming_3001_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3002, version=0)
class Microsoft_Windows_Media_Streaming_3002_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Value" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3050, version=0)
class Microsoft_Windows_Media_Streaming_3050_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3051, version=0)
class Microsoft_Windows_Media_Streaming_3051_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3052, version=0)
class Microsoft_Windows_Media_Streaming_3052_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3053, version=0)
class Microsoft_Windows_Media_Streaming_3053_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3054, version=0)
class Microsoft_Windows_Media_Streaming_3054_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3055, version=0)
class Microsoft_Windows_Media_Streaming_3055_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3056, version=0)
class Microsoft_Windows_Media_Streaming_3056_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3057, version=0)
class Microsoft_Windows_Media_Streaming_3057_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Uri" / WString,
        "Metadata" / WString
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3058, version=0)
class Microsoft_Windows_Media_Streaming_3058_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Uri" / WString,
        "Metadata" / WString
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3100, version=0)
class Microsoft_Windows_Media_Streaming_3100_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3101, version=0)
class Microsoft_Windows_Media_Streaming_3101_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3102, version=0)
class Microsoft_Windows_Media_Streaming_3102_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3103, version=0)
class Microsoft_Windows_Media_Streaming_3103_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3104, version=0)
class Microsoft_Windows_Media_Streaming_3104_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3105, version=0)
class Microsoft_Windows_Media_Streaming_3105_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3106, version=0)
class Microsoft_Windows_Media_Streaming_3106_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3150, version=0)
class Microsoft_Windows_Media_Streaming_3150_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "String" / WString
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3151, version=0)
class Microsoft_Windows_Media_Streaming_3151_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "String" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3201, version=0)
class Microsoft_Windows_Media_Streaming_3201_0(Etw):
    pattern = Struct(
        "MenuItemCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3202, version=0)
class Microsoft_Windows_Media_Streaming_3202_0(Etw):
    pattern = Struct(
        "MenuItemCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3203, version=0)
class Microsoft_Windows_Media_Streaming_3203_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3204, version=0)
class Microsoft_Windows_Media_Streaming_3204_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3205, version=0)
class Microsoft_Windows_Media_Streaming_3205_0(Etw):
    pattern = Struct(
        "ItemCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("982824e5-e446-46ae-bc74-836401ffb7b6"), event_id=3206, version=0)
class Microsoft_Windows_Media_Streaming_3206_0(Etw):
    pattern = Struct(
        "ItemCount" / Int32ul,
        "ErrorCode" / Int32ul
    )

