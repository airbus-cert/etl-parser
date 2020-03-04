# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SettingSync-OneDrive
GUID : f43c3c35-22e2-53eb-f169-07594054779e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=1000, version=0)
class Microsoft_Windows_SettingSync_OneDrive_1000_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=1001, version=0)
class Microsoft_Windows_SettingSync_OneDrive_1001_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=1002, version=0)
class Microsoft_Windows_SettingSync_OneDrive_1002_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=1003, version=0)
class Microsoft_Windows_SettingSync_OneDrive_1003_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=1004, version=0)
class Microsoft_Windows_SettingSync_OneDrive_1004_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=1005, version=0)
class Microsoft_Windows_SettingSync_OneDrive_1005_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=1006, version=0)
class Microsoft_Windows_SettingSync_OneDrive_1006_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Value" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=1007, version=0)
class Microsoft_Windows_SettingSync_OneDrive_1007_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "SettingUnitId" / WString,
        "Operation" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=1008, version=0)
class Microsoft_Windows_SettingSync_OneDrive_1008_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=1012, version=0)
class Microsoft_Windows_SettingSync_OneDrive_1012_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=1013, version=0)
class Microsoft_Windows_SettingSync_OneDrive_1013_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=1014, version=0)
class Microsoft_Windows_SettingSync_OneDrive_1014_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=1015, version=0)
class Microsoft_Windows_SettingSync_OneDrive_1015_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=1016, version=0)
class Microsoft_Windows_SettingSync_OneDrive_1016_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=1017, version=0)
class Microsoft_Windows_SettingSync_OneDrive_1017_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=1018, version=0)
class Microsoft_Windows_SettingSync_OneDrive_1018_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=1019, version=0)
class Microsoft_Windows_SettingSync_OneDrive_1019_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=1020, version=0)
class Microsoft_Windows_SettingSync_OneDrive_1020_0(Etw):
    pattern = Struct(
        "ChannelName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=1021, version=0)
class Microsoft_Windows_SettingSync_OneDrive_1021_0(Etw):
    pattern = Struct(
        "ChannelName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3000, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3000_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3001, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3001_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3002, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3002_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3003, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3003_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "WriteStatus" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3004, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3004_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3005, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3005_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3006, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3006_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3007, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3007_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3008, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3008_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3009, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3009_0(Etw):
    pattern = Struct(
        "PropStoreName" / WString,
        "SettingUnitId" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3010, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3010_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "ProviderName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3011, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3011_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3012, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3012_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString,
        "Operation" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3013, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3013_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3014, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3014_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3015, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3015_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "OldValue" / Int32ul,
        "NewValue" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3017, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3017_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString,
        "Operation" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3018, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3018_0(Etw):
    pattern = Struct(
        "Response" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3020, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3020_0(Etw):
    pattern = Struct(
        "Verb" / WString,
        "Url" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3021, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3021_0(Etw):
    pattern = Struct(
        "TransactionId" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3022, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3022_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3023, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3023_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3024, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3024_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Reason" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3025, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3025_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Reason" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3026, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3026_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3027, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3027_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=3029, version=0)
class Microsoft_Windows_SettingSync_OneDrive_3029_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9000, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9000_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9001, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9001_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9002, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9002_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9004, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9004_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9008, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9008_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9012, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9012_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9022, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9022_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9026, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9026_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9030, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9030_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9032, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9032_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9034, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9034_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9036, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9036_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9038, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9038_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9040, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9040_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9042, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9042_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9045, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9045_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9047, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9047_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9049, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9049_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9051, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9051_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9053, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9053_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9055, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9055_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9057, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9057_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9059, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9059_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9061, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9061_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9063, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9063_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9065, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9065_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9067, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9067_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9071, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9071_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9073, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9073_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9075, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9075_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9076, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9076_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9077, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9077_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9079, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9079_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9083, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9083_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9085, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9085_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9087, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9087_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9089, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9089_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9093, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9093_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9095, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9095_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f43c3c35-22e2-53eb-f169-07594054779e"), event_id=9097, version=0)
class Microsoft_Windows_SettingSync_OneDrive_9097_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )

