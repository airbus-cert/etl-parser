# -*- coding: utf-8 -*-
"""
Microsoft-Windows-PackageStateRoaming
GUID : 5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5001, version=0)
class Microsoft_Windows_PackageStateRoaming_5001_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5002, version=0)
class Microsoft_Windows_PackageStateRoaming_5002_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5003, version=0)
class Microsoft_Windows_PackageStateRoaming_5003_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5005, version=0)
class Microsoft_Windows_PackageStateRoaming_5005_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5006, version=0)
class Microsoft_Windows_PackageStateRoaming_5006_0(Etw):
    pattern = Struct(
        "OldCollectionId" / WString,
        "NewCollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5007, version=0)
class Microsoft_Windows_PackageStateRoaming_5007_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "StateType" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5008, version=0)
class Microsoft_Windows_PackageStateRoaming_5008_0(Etw):
    pattern = Struct(
        "SettingId" / WString,
        "PackageFamilyName" / WString,
        "GetModifiedTimeHRESULT" / Int32ul,
        "UnitModifiedTimestamp" / Int64ul,
        "CollectionConsistencyTimestamp" / Int64ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5009, version=0)
class Microsoft_Windows_PackageStateRoaming_5009_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5010, version=0)
class Microsoft_Windows_PackageStateRoaming_5010_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5011, version=0)
class Microsoft_Windows_PackageStateRoaming_5011_0(Etw):
    pattern = Struct(
        "FilePath" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5012, version=0)
class Microsoft_Windows_PackageStateRoaming_5012_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5013, version=0)
class Microsoft_Windows_PackageStateRoaming_5013_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5014, version=0)
class Microsoft_Windows_PackageStateRoaming_5014_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5015, version=0)
class Microsoft_Windows_PackageStateRoaming_5015_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5016, version=0)
class Microsoft_Windows_PackageStateRoaming_5016_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5017, version=0)
class Microsoft_Windows_PackageStateRoaming_5017_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5018, version=0)
class Microsoft_Windows_PackageStateRoaming_5018_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5019, version=0)
class Microsoft_Windows_PackageStateRoaming_5019_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5020, version=0)
class Microsoft_Windows_PackageStateRoaming_5020_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5021, version=0)
class Microsoft_Windows_PackageStateRoaming_5021_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5022, version=0)
class Microsoft_Windows_PackageStateRoaming_5022_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5023, version=0)
class Microsoft_Windows_PackageStateRoaming_5023_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5024, version=0)
class Microsoft_Windows_PackageStateRoaming_5024_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5025, version=0)
class Microsoft_Windows_PackageStateRoaming_5025_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5026, version=0)
class Microsoft_Windows_PackageStateRoaming_5026_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5027, version=0)
class Microsoft_Windows_PackageStateRoaming_5027_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5028, version=0)
class Microsoft_Windows_PackageStateRoaming_5028_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5029, version=0)
class Microsoft_Windows_PackageStateRoaming_5029_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5030, version=0)
class Microsoft_Windows_PackageStateRoaming_5030_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5031, version=0)
class Microsoft_Windows_PackageStateRoaming_5031_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5032, version=0)
class Microsoft_Windows_PackageStateRoaming_5032_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5033, version=0)
class Microsoft_Windows_PackageStateRoaming_5033_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5034, version=0)
class Microsoft_Windows_PackageStateRoaming_5034_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5035, version=0)
class Microsoft_Windows_PackageStateRoaming_5035_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5036, version=0)
class Microsoft_Windows_PackageStateRoaming_5036_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5037, version=0)
class Microsoft_Windows_PackageStateRoaming_5037_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5038, version=0)
class Microsoft_Windows_PackageStateRoaming_5038_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5039, version=0)
class Microsoft_Windows_PackageStateRoaming_5039_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5040, version=0)
class Microsoft_Windows_PackageStateRoaming_5040_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5041, version=0)
class Microsoft_Windows_PackageStateRoaming_5041_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5042, version=0)
class Microsoft_Windows_PackageStateRoaming_5042_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5043, version=0)
class Microsoft_Windows_PackageStateRoaming_5043_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5044, version=0)
class Microsoft_Windows_PackageStateRoaming_5044_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5045, version=0)
class Microsoft_Windows_PackageStateRoaming_5045_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5046, version=0)
class Microsoft_Windows_PackageStateRoaming_5046_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5047, version=0)
class Microsoft_Windows_PackageStateRoaming_5047_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5048, version=0)
class Microsoft_Windows_PackageStateRoaming_5048_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5049, version=0)
class Microsoft_Windows_PackageStateRoaming_5049_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5050, version=0)
class Microsoft_Windows_PackageStateRoaming_5050_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5051, version=0)
class Microsoft_Windows_PackageStateRoaming_5051_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5052, version=0)
class Microsoft_Windows_PackageStateRoaming_5052_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5053, version=0)
class Microsoft_Windows_PackageStateRoaming_5053_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5054, version=0)
class Microsoft_Windows_PackageStateRoaming_5054_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5055, version=0)
class Microsoft_Windows_PackageStateRoaming_5055_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5056, version=0)
class Microsoft_Windows_PackageStateRoaming_5056_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5057, version=0)
class Microsoft_Windows_PackageStateRoaming_5057_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=5058, version=0)
class Microsoft_Windows_PackageStateRoaming_5058_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6001, version=0)
class Microsoft_Windows_PackageStateRoaming_6001_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6002, version=0)
class Microsoft_Windows_PackageStateRoaming_6002_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6003, version=0)
class Microsoft_Windows_PackageStateRoaming_6003_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6005, version=0)
class Microsoft_Windows_PackageStateRoaming_6005_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6006, version=0)
class Microsoft_Windows_PackageStateRoaming_6006_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6008, version=0)
class Microsoft_Windows_PackageStateRoaming_6008_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6009, version=0)
class Microsoft_Windows_PackageStateRoaming_6009_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "StateType" / WString,
        "Type" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6010, version=0)
class Microsoft_Windows_PackageStateRoaming_6010_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "BackupState" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6011, version=0)
class Microsoft_Windows_PackageStateRoaming_6011_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Operation" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6012, version=0)
class Microsoft_Windows_PackageStateRoaming_6012_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6013, version=0)
class Microsoft_Windows_PackageStateRoaming_6013_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6014, version=0)
class Microsoft_Windows_PackageStateRoaming_6014_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6015, version=0)
class Microsoft_Windows_PackageStateRoaming_6015_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6016, version=0)
class Microsoft_Windows_PackageStateRoaming_6016_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6018, version=0)
class Microsoft_Windows_PackageStateRoaming_6018_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "ConsistencyHypothesis" / Int64ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6019, version=0)
class Microsoft_Windows_PackageStateRoaming_6019_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "DelayMs" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6020, version=0)
class Microsoft_Windows_PackageStateRoaming_6020_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "ConsistencyHypothesis" / Int64ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6021, version=0)
class Microsoft_Windows_PackageStateRoaming_6021_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6022, version=0)
class Microsoft_Windows_PackageStateRoaming_6022_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ConsistencyHypothesis" / Int64ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6023, version=0)
class Microsoft_Windows_PackageStateRoaming_6023_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ConsistencyHypothesis" / Int64ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6024, version=0)
class Microsoft_Windows_PackageStateRoaming_6024_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6025, version=0)
class Microsoft_Windows_PackageStateRoaming_6025_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ConsistencyHypothesis" / Int64ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6026, version=0)
class Microsoft_Windows_PackageStateRoaming_6026_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ConsistencyHypothesis" / Int64ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6027, version=0)
class Microsoft_Windows_PackageStateRoaming_6027_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6028, version=0)
class Microsoft_Windows_PackageStateRoaming_6028_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Operation" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6029, version=0)
class Microsoft_Windows_PackageStateRoaming_6029_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Locality" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6032, version=0)
class Microsoft_Windows_PackageStateRoaming_6032_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6101, version=0)
class Microsoft_Windows_PackageStateRoaming_6101_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6102, version=0)
class Microsoft_Windows_PackageStateRoaming_6102_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6103, version=0)
class Microsoft_Windows_PackageStateRoaming_6103_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6104, version=0)
class Microsoft_Windows_PackageStateRoaming_6104_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6105, version=0)
class Microsoft_Windows_PackageStateRoaming_6105_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6106, version=0)
class Microsoft_Windows_PackageStateRoaming_6106_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6107, version=0)
class Microsoft_Windows_PackageStateRoaming_6107_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6108, version=0)
class Microsoft_Windows_PackageStateRoaming_6108_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6109, version=0)
class Microsoft_Windows_PackageStateRoaming_6109_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6110, version=0)
class Microsoft_Windows_PackageStateRoaming_6110_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6111, version=0)
class Microsoft_Windows_PackageStateRoaming_6111_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6112, version=0)
class Microsoft_Windows_PackageStateRoaming_6112_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6113, version=0)
class Microsoft_Windows_PackageStateRoaming_6113_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Operation" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6114, version=0)
class Microsoft_Windows_PackageStateRoaming_6114_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6115, version=0)
class Microsoft_Windows_PackageStateRoaming_6115_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6116, version=0)
class Microsoft_Windows_PackageStateRoaming_6116_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6117, version=0)
class Microsoft_Windows_PackageStateRoaming_6117_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6118, version=0)
class Microsoft_Windows_PackageStateRoaming_6118_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6119, version=0)
class Microsoft_Windows_PackageStateRoaming_6119_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6120, version=0)
class Microsoft_Windows_PackageStateRoaming_6120_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6121, version=0)
class Microsoft_Windows_PackageStateRoaming_6121_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6122, version=0)
class Microsoft_Windows_PackageStateRoaming_6122_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6123, version=0)
class Microsoft_Windows_PackageStateRoaming_6123_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6124, version=0)
class Microsoft_Windows_PackageStateRoaming_6124_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6125, version=0)
class Microsoft_Windows_PackageStateRoaming_6125_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6126, version=0)
class Microsoft_Windows_PackageStateRoaming_6126_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6127, version=0)
class Microsoft_Windows_PackageStateRoaming_6127_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6128, version=0)
class Microsoft_Windows_PackageStateRoaming_6128_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6129, version=0)
class Microsoft_Windows_PackageStateRoaming_6129_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6130, version=0)
class Microsoft_Windows_PackageStateRoaming_6130_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6131, version=0)
class Microsoft_Windows_PackageStateRoaming_6131_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6132, version=0)
class Microsoft_Windows_PackageStateRoaming_6132_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6133, version=0)
class Microsoft_Windows_PackageStateRoaming_6133_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6134, version=0)
class Microsoft_Windows_PackageStateRoaming_6134_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6135, version=0)
class Microsoft_Windows_PackageStateRoaming_6135_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6136, version=0)
class Microsoft_Windows_PackageStateRoaming_6136_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6137, version=0)
class Microsoft_Windows_PackageStateRoaming_6137_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6138, version=0)
class Microsoft_Windows_PackageStateRoaming_6138_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6139, version=0)
class Microsoft_Windows_PackageStateRoaming_6139_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6140, version=0)
class Microsoft_Windows_PackageStateRoaming_6140_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6141, version=0)
class Microsoft_Windows_PackageStateRoaming_6141_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6142, version=0)
class Microsoft_Windows_PackageStateRoaming_6142_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6143, version=0)
class Microsoft_Windows_PackageStateRoaming_6143_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6144, version=0)
class Microsoft_Windows_PackageStateRoaming_6144_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6145, version=0)
class Microsoft_Windows_PackageStateRoaming_6145_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6146, version=0)
class Microsoft_Windows_PackageStateRoaming_6146_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6147, version=0)
class Microsoft_Windows_PackageStateRoaming_6147_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6148, version=0)
class Microsoft_Windows_PackageStateRoaming_6148_0(Etw):
    pattern = Struct(
        "EnumType" / Int32ul,
        "Items" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6149, version=0)
class Microsoft_Windows_PackageStateRoaming_6149_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6150, version=0)
class Microsoft_Windows_PackageStateRoaming_6150_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=6151, version=0)
class Microsoft_Windows_PackageStateRoaming_6151_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7001, version=0)
class Microsoft_Windows_PackageStateRoaming_7001_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7002, version=0)
class Microsoft_Windows_PackageStateRoaming_7002_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7003, version=0)
class Microsoft_Windows_PackageStateRoaming_7003_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7004, version=0)
class Microsoft_Windows_PackageStateRoaming_7004_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7005, version=0)
class Microsoft_Windows_PackageStateRoaming_7005_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7006, version=0)
class Microsoft_Windows_PackageStateRoaming_7006_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7009, version=0)
class Microsoft_Windows_PackageStateRoaming_7009_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Locality" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7010, version=0)
class Microsoft_Windows_PackageStateRoaming_7010_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7011, version=0)
class Microsoft_Windows_PackageStateRoaming_7011_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Locality" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7012, version=0)
class Microsoft_Windows_PackageStateRoaming_7012_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7013, version=0)
class Microsoft_Windows_PackageStateRoaming_7013_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Locality" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7014, version=0)
class Microsoft_Windows_PackageStateRoaming_7014_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Count" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7015, version=0)
class Microsoft_Windows_PackageStateRoaming_7015_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Locality" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7016, version=0)
class Microsoft_Windows_PackageStateRoaming_7016_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Locality" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7017, version=0)
class Microsoft_Windows_PackageStateRoaming_7017_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7018, version=0)
class Microsoft_Windows_PackageStateRoaming_7018_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7019, version=0)
class Microsoft_Windows_PackageStateRoaming_7019_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7023, version=0)
class Microsoft_Windows_PackageStateRoaming_7023_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7026, version=0)
class Microsoft_Windows_PackageStateRoaming_7026_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7027, version=0)
class Microsoft_Windows_PackageStateRoaming_7027_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Locality" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7028, version=0)
class Microsoft_Windows_PackageStateRoaming_7028_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Locality" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7029, version=0)
class Microsoft_Windows_PackageStateRoaming_7029_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Operation" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7030, version=0)
class Microsoft_Windows_PackageStateRoaming_7030_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "Operation" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7032, version=0)
class Microsoft_Windows_PackageStateRoaming_7032_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7033, version=0)
class Microsoft_Windows_PackageStateRoaming_7033_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7034, version=0)
class Microsoft_Windows_PackageStateRoaming_7034_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7035, version=0)
class Microsoft_Windows_PackageStateRoaming_7035_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0"), event_id=7036, version=0)
class Microsoft_Windows_PackageStateRoaming_7036_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )

