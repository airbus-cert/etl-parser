# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SettingSync
GUID : 83d6e83b-900b-48a3-9835-57656b6f6474
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5001, version=0)
class Microsoft_Windows_SettingSync_5001_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5002, version=0)
class Microsoft_Windows_SettingSync_5002_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5003, version=0)
class Microsoft_Windows_SettingSync_5003_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5004, version=0)
class Microsoft_Windows_SettingSync_5004_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5005, version=0)
class Microsoft_Windows_SettingSync_5005_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5006, version=0)
class Microsoft_Windows_SettingSync_5006_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5007, version=0)
class Microsoft_Windows_SettingSync_5007_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5008, version=0)
class Microsoft_Windows_SettingSync_5008_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5009, version=0)
class Microsoft_Windows_SettingSync_5009_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString,
        "Operation" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5010, version=0)
class Microsoft_Windows_SettingSync_5010_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString,
        "Operation" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5011, version=0)
class Microsoft_Windows_SettingSync_5011_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Operation" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5012, version=0)
class Microsoft_Windows_SettingSync_5012_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5013, version=0)
class Microsoft_Windows_SettingSync_5013_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5014, version=0)
class Microsoft_Windows_SettingSync_5014_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString,
        "Operation" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5015, version=0)
class Microsoft_Windows_SettingSync_5015_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5016, version=0)
class Microsoft_Windows_SettingSync_5016_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5017, version=0)
class Microsoft_Windows_SettingSync_5017_0(Etw):
    pattern = Struct(
        "Value" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5018, version=0)
class Microsoft_Windows_SettingSync_5018_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5019, version=0)
class Microsoft_Windows_SettingSync_5019_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5020, version=0)
class Microsoft_Windows_SettingSync_5020_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5021, version=0)
class Microsoft_Windows_SettingSync_5021_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5022, version=0)
class Microsoft_Windows_SettingSync_5022_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5023, version=0)
class Microsoft_Windows_SettingSync_5023_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5024, version=0)
class Microsoft_Windows_SettingSync_5024_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5025, version=0)
class Microsoft_Windows_SettingSync_5025_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5026, version=0)
class Microsoft_Windows_SettingSync_5026_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5027, version=0)
class Microsoft_Windows_SettingSync_5027_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5028, version=0)
class Microsoft_Windows_SettingSync_5028_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5029, version=0)
class Microsoft_Windows_SettingSync_5029_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5030, version=0)
class Microsoft_Windows_SettingSync_5030_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5031, version=0)
class Microsoft_Windows_SettingSync_5031_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5032, version=0)
class Microsoft_Windows_SettingSync_5032_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5033, version=0)
class Microsoft_Windows_SettingSync_5033_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5034, version=0)
class Microsoft_Windows_SettingSync_5034_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5035, version=0)
class Microsoft_Windows_SettingSync_5035_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5036, version=0)
class Microsoft_Windows_SettingSync_5036_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5037, version=0)
class Microsoft_Windows_SettingSync_5037_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5038, version=0)
class Microsoft_Windows_SettingSync_5038_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5039, version=0)
class Microsoft_Windows_SettingSync_5039_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5040, version=0)
class Microsoft_Windows_SettingSync_5040_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5041, version=0)
class Microsoft_Windows_SettingSync_5041_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "OperationType" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5042, version=0)
class Microsoft_Windows_SettingSync_5042_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "OperationType" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5390, version=0)
class Microsoft_Windows_SettingSync_5390_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "SettingUnitId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5391, version=0)
class Microsoft_Windows_SettingSync_5391_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "SettingUnitId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5392, version=0)
class Microsoft_Windows_SettingSync_5392_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "SettingUnitId" / WString,
        "Operation" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5393, version=0)
class Microsoft_Windows_SettingSync_5393_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "SettingUnitId" / WString,
        "Operation" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5401, version=0)
class Microsoft_Windows_SettingSync_5401_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5402, version=0)
class Microsoft_Windows_SettingSync_5402_0(Etw):
    pattern = Struct(
        "message" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5403, version=0)
class Microsoft_Windows_SettingSync_5403_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5501, version=0)
class Microsoft_Windows_SettingSync_5501_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5502, version=0)
class Microsoft_Windows_SettingSync_5502_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString,
        "Operation" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5503, version=0)
class Microsoft_Windows_SettingSync_5503_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5504, version=0)
class Microsoft_Windows_SettingSync_5504_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5505, version=0)
class Microsoft_Windows_SettingSync_5505_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5506, version=0)
class Microsoft_Windows_SettingSync_5506_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString,
        "Operation" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5507, version=0)
class Microsoft_Windows_SettingSync_5507_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString,
        "Operation" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5508, version=0)
class Microsoft_Windows_SettingSync_5508_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5510, version=0)
class Microsoft_Windows_SettingSync_5510_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5511, version=0)
class Microsoft_Windows_SettingSync_5511_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5512, version=0)
class Microsoft_Windows_SettingSync_5512_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5515, version=0)
class Microsoft_Windows_SettingSync_5515_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5516, version=0)
class Microsoft_Windows_SettingSync_5516_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5517, version=0)
class Microsoft_Windows_SettingSync_5517_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5518, version=0)
class Microsoft_Windows_SettingSync_5518_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5519, version=0)
class Microsoft_Windows_SettingSync_5519_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5520, version=0)
class Microsoft_Windows_SettingSync_5520_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5521, version=0)
class Microsoft_Windows_SettingSync_5521_0(Etw):
    pattern = Struct(
        "Response" / WString,
        "ChangesApplied" / Int32ul,
        "FailedChanges" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5522, version=0)
class Microsoft_Windows_SettingSync_5522_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5523, version=0)
class Microsoft_Windows_SettingSync_5523_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5525, version=0)
class Microsoft_Windows_SettingSync_5525_0(Etw):
    pattern = Struct(
        "ChannelName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5526, version=0)
class Microsoft_Windows_SettingSync_5526_0(Etw):
    pattern = Struct(
        "ChannelName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5530, version=0)
class Microsoft_Windows_SettingSync_5530_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5531, version=0)
class Microsoft_Windows_SettingSync_5531_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5532, version=0)
class Microsoft_Windows_SettingSync_5532_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5533, version=0)
class Microsoft_Windows_SettingSync_5533_0(Etw):
    pattern = Struct(
        "Response" / WString,
        "ChangesApplied" / Int32ul,
        "FailedChanges" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5534, version=0)
class Microsoft_Windows_SettingSync_5534_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5535, version=0)
class Microsoft_Windows_SettingSync_5535_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5536, version=0)
class Microsoft_Windows_SettingSync_5536_0(Etw):
    pattern = Struct(
        "Boolean" / Int8ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5537, version=0)
class Microsoft_Windows_SettingSync_5537_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5538, version=0)
class Microsoft_Windows_SettingSync_5538_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5539, version=0)
class Microsoft_Windows_SettingSync_5539_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5540, version=0)
class Microsoft_Windows_SettingSync_5540_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5541, version=0)
class Microsoft_Windows_SettingSync_5541_0(Etw):
    pattern = Struct(
        "Response" / WString,
        "ChangesApplied" / Int32ul,
        "FailedChanges" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5542, version=0)
class Microsoft_Windows_SettingSync_5542_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5543, version=0)
class Microsoft_Windows_SettingSync_5543_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5544, version=0)
class Microsoft_Windows_SettingSync_5544_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5545, version=0)
class Microsoft_Windows_SettingSync_5545_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5546, version=0)
class Microsoft_Windows_SettingSync_5546_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5547, version=0)
class Microsoft_Windows_SettingSync_5547_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "ProviderName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5690, version=0)
class Microsoft_Windows_SettingSync_5690_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "SettingUnitId" / WString,
        "Operation" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5691, version=0)
class Microsoft_Windows_SettingSync_5691_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "SettingUnitId" / WString,
        "Operation" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5692, version=0)
class Microsoft_Windows_SettingSync_5692_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "SettingUnitId" / WString,
        "Operation" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5693, version=0)
class Microsoft_Windows_SettingSync_5693_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Value" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5706, version=0)
class Microsoft_Windows_SettingSync_5706_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5707, version=0)
class Microsoft_Windows_SettingSync_5707_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5708, version=0)
class Microsoft_Windows_SettingSync_5708_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5713, version=0)
class Microsoft_Windows_SettingSync_5713_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5714, version=0)
class Microsoft_Windows_SettingSync_5714_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5715, version=0)
class Microsoft_Windows_SettingSync_5715_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5716, version=0)
class Microsoft_Windows_SettingSync_5716_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5717, version=0)
class Microsoft_Windows_SettingSync_5717_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5718, version=0)
class Microsoft_Windows_SettingSync_5718_0(Etw):
    pattern = Struct(
        "MetadataStorePath" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5719, version=0)
class Microsoft_Windows_SettingSync_5719_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5720, version=0)
class Microsoft_Windows_SettingSync_5720_0(Etw):
    pattern = Struct(
        "UpdatedTimestamp" / Int64ul,
        "InitialTimestamp" / Int64ul,
        "CollectionId" / WString,
        "SettingUnitId" / WString,
        "Operation" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5721, version=0)
class Microsoft_Windows_SettingSync_5721_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5722, version=0)
class Microsoft_Windows_SettingSync_5722_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5723, version=0)
class Microsoft_Windows_SettingSync_5723_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5724, version=0)
class Microsoft_Windows_SettingSync_5724_0(Etw):
    pattern = Struct(
        "Collection" / WString,
        "OperationType" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5725, version=0)
class Microsoft_Windows_SettingSync_5725_0(Etw):
    pattern = Struct(
        "MetadataStorePath" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=5726, version=0)
class Microsoft_Windows_SettingSync_5726_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6001, version=0)
class Microsoft_Windows_SettingSync_6001_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6002, version=0)
class Microsoft_Windows_SettingSync_6002_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6003, version=0)
class Microsoft_Windows_SettingSync_6003_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6004, version=0)
class Microsoft_Windows_SettingSync_6004_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6005, version=0)
class Microsoft_Windows_SettingSync_6005_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6006, version=0)
class Microsoft_Windows_SettingSync_6006_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6007, version=0)
class Microsoft_Windows_SettingSync_6007_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6008, version=0)
class Microsoft_Windows_SettingSync_6008_0(Etw):
    pattern = Struct(
        "Reason" / Int8ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6009, version=0)
class Microsoft_Windows_SettingSync_6009_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6010, version=0)
class Microsoft_Windows_SettingSync_6010_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString,
        "Operation" / WString,
        "ConflictResult" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6011, version=0)
class Microsoft_Windows_SettingSync_6011_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6013, version=0)
class Microsoft_Windows_SettingSync_6013_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6014, version=0)
class Microsoft_Windows_SettingSync_6014_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6015, version=0)
class Microsoft_Windows_SettingSync_6015_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6016, version=0)
class Microsoft_Windows_SettingSync_6016_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6017, version=0)
class Microsoft_Windows_SettingSync_6017_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Operation" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6018, version=0)
class Microsoft_Windows_SettingSync_6018_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Operation" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6020, version=0)
class Microsoft_Windows_SettingSync_6020_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString,
        "Operation" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6021, version=0)
class Microsoft_Windows_SettingSync_6021_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6022, version=0)
class Microsoft_Windows_SettingSync_6022_0(Etw):
    pattern = Struct(
        "BatchComplete" / Int8ul,
        "TotalOperations" / Int32ul,
        "CompletedOperations" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6023, version=0)
class Microsoft_Windows_SettingSync_6023_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Reason" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6024, version=0)
class Microsoft_Windows_SettingSync_6024_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6025, version=0)
class Microsoft_Windows_SettingSync_6025_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6026, version=0)
class Microsoft_Windows_SettingSync_6026_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6027, version=0)
class Microsoft_Windows_SettingSync_6027_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6028, version=0)
class Microsoft_Windows_SettingSync_6028_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6029, version=0)
class Microsoft_Windows_SettingSync_6029_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6030, version=0)
class Microsoft_Windows_SettingSync_6030_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6031, version=0)
class Microsoft_Windows_SettingSync_6031_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "SETTINGCOLLECTIONBACKUPSTATE" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6032, version=0)
class Microsoft_Windows_SettingSync_6032_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Completed" / Int32ul,
        "Total" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6033, version=0)
class Microsoft_Windows_SettingSync_6033_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6034, version=0)
class Microsoft_Windows_SettingSync_6034_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6035, version=0)
class Microsoft_Windows_SettingSync_6035_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Timestamp" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6036, version=0)
class Microsoft_Windows_SettingSync_6036_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Timestamp" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6037, version=0)
class Microsoft_Windows_SettingSync_6037_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Timestamp" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6038, version=0)
class Microsoft_Windows_SettingSync_6038_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "SETTINGCOLLECTIONBACKUPSTATE" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6039, version=0)
class Microsoft_Windows_SettingSync_6039_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "InitialTimestamp" / Int64ul,
        "UpdatedTimestamp" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6040, version=0)
class Microsoft_Windows_SettingSync_6040_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "SettingUnitTimestamp" / Int64ul,
        "DataStreamTimestamp" / Int64ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6041, version=0)
class Microsoft_Windows_SettingSync_6041_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6044, version=0)
class Microsoft_Windows_SettingSync_6044_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6047, version=0)
class Microsoft_Windows_SettingSync_6047_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Operation" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6048, version=0)
class Microsoft_Windows_SettingSync_6048_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Operation" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6049, version=0)
class Microsoft_Windows_SettingSync_6049_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Operation" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6050, version=0)
class Microsoft_Windows_SettingSync_6050_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6052, version=0)
class Microsoft_Windows_SettingSync_6052_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6053, version=0)
class Microsoft_Windows_SettingSync_6053_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Timestamp" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6054, version=0)
class Microsoft_Windows_SettingSync_6054_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "OldValue" / Int32ul,
        "NewValue" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6055, version=0)
class Microsoft_Windows_SettingSync_6055_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6056, version=0)
class Microsoft_Windows_SettingSync_6056_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6057, version=0)
class Microsoft_Windows_SettingSync_6057_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6061, version=0)
class Microsoft_Windows_SettingSync_6061_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6062, version=0)
class Microsoft_Windows_SettingSync_6062_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6063, version=0)
class Microsoft_Windows_SettingSync_6063_0(Etw):
    pattern = Struct(
        "PropStoreName" / WString,
        "SettingUnitId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6064, version=0)
class Microsoft_Windows_SettingSync_6064_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6065, version=0)
class Microsoft_Windows_SettingSync_6065_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6066, version=0)
class Microsoft_Windows_SettingSync_6066_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6067, version=0)
class Microsoft_Windows_SettingSync_6067_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6501, version=0)
class Microsoft_Windows_SettingSync_6501_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString,
        "Operation" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6502, version=0)
class Microsoft_Windows_SettingSync_6502_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString,
        "Operation" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6503, version=0)
class Microsoft_Windows_SettingSync_6503_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6504, version=0)
class Microsoft_Windows_SettingSync_6504_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6505, version=0)
class Microsoft_Windows_SettingSync_6505_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6506, version=0)
class Microsoft_Windows_SettingSync_6506_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6507, version=0)
class Microsoft_Windows_SettingSync_6507_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6508, version=0)
class Microsoft_Windows_SettingSync_6508_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6509, version=0)
class Microsoft_Windows_SettingSync_6509_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6510, version=0)
class Microsoft_Windows_SettingSync_6510_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6511, version=0)
class Microsoft_Windows_SettingSync_6511_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6515, version=0)
class Microsoft_Windows_SettingSync_6515_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Count" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6516, version=0)
class Microsoft_Windows_SettingSync_6516_0(Etw):
    pattern = Struct(
        "SyncToken" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6517, version=0)
class Microsoft_Windows_SettingSync_6517_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Count" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6518, version=0)
class Microsoft_Windows_SettingSync_6518_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6519, version=0)
class Microsoft_Windows_SettingSync_6519_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6521, version=0)
class Microsoft_Windows_SettingSync_6521_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6522, version=0)
class Microsoft_Windows_SettingSync_6522_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6523, version=0)
class Microsoft_Windows_SettingSync_6523_0(Etw):
    pattern = Struct(
        "Response" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6527, version=0)
class Microsoft_Windows_SettingSync_6527_0(Etw):
    pattern = Struct(
        "TransactionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6528, version=0)
class Microsoft_Windows_SettingSync_6528_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6529, version=0)
class Microsoft_Windows_SettingSync_6529_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6530, version=0)
class Microsoft_Windows_SettingSync_6530_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Reason" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6531, version=0)
class Microsoft_Windows_SettingSync_6531_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Reason" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6532, version=0)
class Microsoft_Windows_SettingSync_6532_0(Etw):
    pattern = Struct(
        "Verb" / WString,
        "Url" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6533, version=0)
class Microsoft_Windows_SettingSync_6533_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6534, version=0)
class Microsoft_Windows_SettingSync_6534_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6535, version=0)
class Microsoft_Windows_SettingSync_6535_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6536, version=0)
class Microsoft_Windows_SettingSync_6536_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6538, version=0)
class Microsoft_Windows_SettingSync_6538_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString,
        "Operation" / WString,
        "ConflictResult" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6539, version=0)
class Microsoft_Windows_SettingSync_6539_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString,
        "Operation" / WString,
        "ConflictResult" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6543, version=0)
class Microsoft_Windows_SettingSync_6543_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6544, version=0)
class Microsoft_Windows_SettingSync_6544_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Count" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6545, version=0)
class Microsoft_Windows_SettingSync_6545_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6546, version=0)
class Microsoft_Windows_SettingSync_6546_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6547, version=0)
class Microsoft_Windows_SettingSync_6547_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6548, version=0)
class Microsoft_Windows_SettingSync_6548_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6549, version=0)
class Microsoft_Windows_SettingSync_6549_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6550, version=0)
class Microsoft_Windows_SettingSync_6550_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "FilterMode" / Int32ul,
        "IsApplicable" / Int8ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6551, version=0)
class Microsoft_Windows_SettingSync_6551_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6552, version=0)
class Microsoft_Windows_SettingSync_6552_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Count" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6553, version=0)
class Microsoft_Windows_SettingSync_6553_0(Etw):
    pattern = Struct(
        "Value1" / Int32ul,
        "Value2" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6554, version=0)
class Microsoft_Windows_SettingSync_6554_0(Etw):
    pattern = Struct(
        "Value1" / Int32ul,
        "Value2" / Int32ul,
        "Value3" / Int32ul,
        "Value4" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6555, version=0)
class Microsoft_Windows_SettingSync_6555_0(Etw):
    pattern = Struct(
        "Value1" / Int32ul,
        "Value2" / Int32ul,
        "Value3" / Int32ul,
        "Value4" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6556, version=0)
class Microsoft_Windows_SettingSync_6556_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6558, version=0)
class Microsoft_Windows_SettingSync_6558_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6559, version=0)
class Microsoft_Windows_SettingSync_6559_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "WriteStatus" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6560, version=0)
class Microsoft_Windows_SettingSync_6560_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString,
        "Operation" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6561, version=0)
class Microsoft_Windows_SettingSync_6561_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6567, version=0)
class Microsoft_Windows_SettingSync_6567_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6568, version=0)
class Microsoft_Windows_SettingSync_6568_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6570, version=0)
class Microsoft_Windows_SettingSync_6570_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "ProviderName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6571, version=0)
class Microsoft_Windows_SettingSync_6571_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6572, version=0)
class Microsoft_Windows_SettingSync_6572_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6573, version=0)
class Microsoft_Windows_SettingSync_6573_0(Etw):
    pattern = Struct(
        "HasInternetConnection" / Int8ul,
        "IsRoaming" / Int8ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6574, version=0)
class Microsoft_Windows_SettingSync_6574_0(Etw):
    pattern = Struct(
        "Collection" / WString,
        "OperationType" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6575, version=0)
class Microsoft_Windows_SettingSync_6575_0(Etw):
    pattern = Struct(
        "OperationType" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6576, version=0)
class Microsoft_Windows_SettingSync_6576_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6581, version=0)
class Microsoft_Windows_SettingSync_6581_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Percentage" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6582, version=0)
class Microsoft_Windows_SettingSync_6582_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6583, version=0)
class Microsoft_Windows_SettingSync_6583_0(Etw):
    pattern = Struct(
        "NumberofApps" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6589, version=0)
class Microsoft_Windows_SettingSync_6589_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "OperationType" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6590, version=0)
class Microsoft_Windows_SettingSync_6590_0(Etw):
    pattern = Struct(
        "IsRoamingEnabled" / Int8ul,
        "RoamingReasonCode" / Int32ul,
        "IsBackupEnabled" / Int8ul,
        "BackupReasonCode" / Int32ul,
        "ProviderId" / Guid
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6591, version=0)
class Microsoft_Windows_SettingSync_6591_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6592, version=0)
class Microsoft_Windows_SettingSync_6592_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Direction" / WString,
        "Priority" / WString,
        "OperationId" / Guid
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6593, version=0)
class Microsoft_Windows_SettingSync_6593_0(Etw):
    pattern = Struct(
        "OperationId" / Guid
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6594, version=0)
class Microsoft_Windows_SettingSync_6594_0(Etw):
    pattern = Struct(
        "OperationId" / Guid
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=6595, version=0)
class Microsoft_Windows_SettingSync_6595_0(Etw):
    pattern = Struct(
        "OperationId" / Guid,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7011, version=0)
class Microsoft_Windows_SettingSync_7011_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7012, version=0)
class Microsoft_Windows_SettingSync_7012_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7013, version=0)
class Microsoft_Windows_SettingSync_7013_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7014, version=0)
class Microsoft_Windows_SettingSync_7014_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7015, version=0)
class Microsoft_Windows_SettingSync_7015_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7016, version=0)
class Microsoft_Windows_SettingSync_7016_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7017, version=0)
class Microsoft_Windows_SettingSync_7017_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7018, version=0)
class Microsoft_Windows_SettingSync_7018_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7019, version=0)
class Microsoft_Windows_SettingSync_7019_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7020, version=0)
class Microsoft_Windows_SettingSync_7020_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7021, version=0)
class Microsoft_Windows_SettingSync_7021_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7022, version=0)
class Microsoft_Windows_SettingSync_7022_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7023, version=0)
class Microsoft_Windows_SettingSync_7023_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7024, version=0)
class Microsoft_Windows_SettingSync_7024_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7025, version=0)
class Microsoft_Windows_SettingSync_7025_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7026, version=0)
class Microsoft_Windows_SettingSync_7026_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7027, version=0)
class Microsoft_Windows_SettingSync_7027_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7028, version=0)
class Microsoft_Windows_SettingSync_7028_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7029, version=0)
class Microsoft_Windows_SettingSync_7029_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7030, version=0)
class Microsoft_Windows_SettingSync_7030_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7031, version=0)
class Microsoft_Windows_SettingSync_7031_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7032, version=0)
class Microsoft_Windows_SettingSync_7032_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7033, version=0)
class Microsoft_Windows_SettingSync_7033_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7034, version=0)
class Microsoft_Windows_SettingSync_7034_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7035, version=0)
class Microsoft_Windows_SettingSync_7035_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7036, version=0)
class Microsoft_Windows_SettingSync_7036_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7037, version=0)
class Microsoft_Windows_SettingSync_7037_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7038, version=0)
class Microsoft_Windows_SettingSync_7038_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7039, version=0)
class Microsoft_Windows_SettingSync_7039_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7040, version=0)
class Microsoft_Windows_SettingSync_7040_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7041, version=0)
class Microsoft_Windows_SettingSync_7041_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7042, version=0)
class Microsoft_Windows_SettingSync_7042_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7043, version=0)
class Microsoft_Windows_SettingSync_7043_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7044, version=0)
class Microsoft_Windows_SettingSync_7044_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7046, version=0)
class Microsoft_Windows_SettingSync_7046_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7050, version=0)
class Microsoft_Windows_SettingSync_7050_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7054, version=0)
class Microsoft_Windows_SettingSync_7054_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7056, version=0)
class Microsoft_Windows_SettingSync_7056_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7058, version=0)
class Microsoft_Windows_SettingSync_7058_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7062, version=0)
class Microsoft_Windows_SettingSync_7062_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7066, version=0)
class Microsoft_Windows_SettingSync_7066_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7076, version=0)
class Microsoft_Windows_SettingSync_7076_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7080, version=0)
class Microsoft_Windows_SettingSync_7080_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7089, version=0)
class Microsoft_Windows_SettingSync_7089_0(Etw):
    pattern = Struct(
        "Quality" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7091, version=0)
class Microsoft_Windows_SettingSync_7091_0(Etw):
    pattern = Struct(
        "OrigSizeX" / Int32ul,
        "OrigSizeY" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7093, version=0)
class Microsoft_Windows_SettingSync_7093_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7094, version=0)
class Microsoft_Windows_SettingSync_7094_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7095, version=0)
class Microsoft_Windows_SettingSync_7095_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7096, version=0)
class Microsoft_Windows_SettingSync_7096_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7097, version=0)
class Microsoft_Windows_SettingSync_7097_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7098, version=0)
class Microsoft_Windows_SettingSync_7098_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7100, version=0)
class Microsoft_Windows_SettingSync_7100_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7101, version=0)
class Microsoft_Windows_SettingSync_7101_0(Etw):
    pattern = Struct(
        "Clsid" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7102, version=0)
class Microsoft_Windows_SettingSync_7102_0(Etw):
    pattern = Struct(
        "Clsid" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7103, version=0)
class Microsoft_Windows_SettingSync_7103_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "BACKUPSETTINGDISPOSITION" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7104, version=0)
class Microsoft_Windows_SettingSync_7104_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7105, version=0)
class Microsoft_Windows_SettingSync_7105_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7106, version=0)
class Microsoft_Windows_SettingSync_7106_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7107, version=0)
class Microsoft_Windows_SettingSync_7107_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7108, version=0)
class Microsoft_Windows_SettingSync_7108_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7109, version=0)
class Microsoft_Windows_SettingSync_7109_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7110, version=0)
class Microsoft_Windows_SettingSync_7110_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7111, version=0)
class Microsoft_Windows_SettingSync_7111_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7112, version=0)
class Microsoft_Windows_SettingSync_7112_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7113, version=0)
class Microsoft_Windows_SettingSync_7113_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7114, version=0)
class Microsoft_Windows_SettingSync_7114_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7115, version=0)
class Microsoft_Windows_SettingSync_7115_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7116, version=0)
class Microsoft_Windows_SettingSync_7116_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7117, version=0)
class Microsoft_Windows_SettingSync_7117_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7118, version=0)
class Microsoft_Windows_SettingSync_7118_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7119, version=0)
class Microsoft_Windows_SettingSync_7119_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7120, version=0)
class Microsoft_Windows_SettingSync_7120_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7122, version=0)
class Microsoft_Windows_SettingSync_7122_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7124, version=0)
class Microsoft_Windows_SettingSync_7124_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7126, version=0)
class Microsoft_Windows_SettingSync_7126_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7128, version=0)
class Microsoft_Windows_SettingSync_7128_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7130, version=0)
class Microsoft_Windows_SettingSync_7130_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7132, version=0)
class Microsoft_Windows_SettingSync_7132_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7134, version=0)
class Microsoft_Windows_SettingSync_7134_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7135, version=0)
class Microsoft_Windows_SettingSync_7135_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7136, version=0)
class Microsoft_Windows_SettingSync_7136_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7138, version=0)
class Microsoft_Windows_SettingSync_7138_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7140, version=0)
class Microsoft_Windows_SettingSync_7140_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7142, version=0)
class Microsoft_Windows_SettingSync_7142_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7144, version=0)
class Microsoft_Windows_SettingSync_7144_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7146, version=0)
class Microsoft_Windows_SettingSync_7146_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7148, version=0)
class Microsoft_Windows_SettingSync_7148_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7150, version=0)
class Microsoft_Windows_SettingSync_7150_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7152, version=0)
class Microsoft_Windows_SettingSync_7152_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7154, version=0)
class Microsoft_Windows_SettingSync_7154_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7156, version=0)
class Microsoft_Windows_SettingSync_7156_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7158, version=0)
class Microsoft_Windows_SettingSync_7158_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7160, version=0)
class Microsoft_Windows_SettingSync_7160_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7162, version=0)
class Microsoft_Windows_SettingSync_7162_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7164, version=0)
class Microsoft_Windows_SettingSync_7164_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7166, version=0)
class Microsoft_Windows_SettingSync_7166_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7168, version=0)
class Microsoft_Windows_SettingSync_7168_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7170, version=0)
class Microsoft_Windows_SettingSync_7170_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7172, version=0)
class Microsoft_Windows_SettingSync_7172_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7174, version=0)
class Microsoft_Windows_SettingSync_7174_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7176, version=0)
class Microsoft_Windows_SettingSync_7176_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7178, version=0)
class Microsoft_Windows_SettingSync_7178_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7180, version=0)
class Microsoft_Windows_SettingSync_7180_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7184, version=0)
class Microsoft_Windows_SettingSync_7184_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7186, version=0)
class Microsoft_Windows_SettingSync_7186_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7188, version=0)
class Microsoft_Windows_SettingSync_7188_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7190, version=0)
class Microsoft_Windows_SettingSync_7190_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7194, version=0)
class Microsoft_Windows_SettingSync_7194_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7196, version=0)
class Microsoft_Windows_SettingSync_7196_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7198, version=0)
class Microsoft_Windows_SettingSync_7198_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7200, version=0)
class Microsoft_Windows_SettingSync_7200_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7202, version=0)
class Microsoft_Windows_SettingSync_7202_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7204, version=0)
class Microsoft_Windows_SettingSync_7204_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7206, version=0)
class Microsoft_Windows_SettingSync_7206_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7207, version=0)
class Microsoft_Windows_SettingSync_7207_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7208, version=0)
class Microsoft_Windows_SettingSync_7208_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7308, version=0)
class Microsoft_Windows_SettingSync_7308_0(Etw):
    pattern = Struct(
        "NumberOfCollections" / Int32ul,
        "TotalSize" / Int32ul,
        "hresult" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7310, version=0)
class Microsoft_Windows_SettingSync_7310_0(Etw):
    pattern = Struct(
        "CollectionSize" / Int32ul,
        "hresult" / Int32ul,
        "SecondsSinceChangeNotify" / Int32ul,
        "CollectionName" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7311, version=0)
class Microsoft_Windows_SettingSync_7311_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7312, version=0)
class Microsoft_Windows_SettingSync_7312_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7314, version=0)
class Microsoft_Windows_SettingSync_7314_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7316, version=0)
class Microsoft_Windows_SettingSync_7316_0(Etw):
    pattern = Struct(
        "Value" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7318, version=0)
class Microsoft_Windows_SettingSync_7318_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7500, version=0)
class Microsoft_Windows_SettingSync_7500_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("83d6e83b-900b-48a3-9835-57656b6f6474"), event_id=7750, version=0)
class Microsoft_Windows_SettingSync_7750_0(Etw):
    pattern = Struct(
        "Message" / WString
    )

