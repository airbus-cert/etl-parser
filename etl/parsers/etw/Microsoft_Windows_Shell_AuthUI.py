# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Shell-AuthUI
GUID : 63d2bb1d-e39a-41b8-9a3d-52dd06677588
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=5001, version=0)
class Microsoft_Windows_Shell_AuthUI_5001_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=5002, version=0)
class Microsoft_Windows_Shell_AuthUI_5002_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=5004, version=0)
class Microsoft_Windows_Shell_AuthUI_5004_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=5006, version=0)
class Microsoft_Windows_Shell_AuthUI_5006_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=5007, version=0)
class Microsoft_Windows_Shell_AuthUI_5007_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "DWORD1" / Int32ul,
        "DWORD2" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=5008, version=0)
class Microsoft_Windows_Shell_AuthUI_5008_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "DWORD1" / Int32ul,
        "DWORD2" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=5009, version=0)
class Microsoft_Windows_Shell_AuthUI_5009_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=5010, version=0)
class Microsoft_Windows_Shell_AuthUI_5010_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=5011, version=0)
class Microsoft_Windows_Shell_AuthUI_5011_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=5012, version=0)
class Microsoft_Windows_Shell_AuthUI_5012_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=5013, version=0)
class Microsoft_Windows_Shell_AuthUI_5013_0(Etw):
    pattern = Struct(
        "AutoLogonSettingRemovalReason" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=15016, version=0)
class Microsoft_Windows_Shell_AuthUI_15016_0(Etw):
    pattern = Struct(
        "message1" / WString
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=15018, version=0)
class Microsoft_Windows_Shell_AuthUI_15018_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=15020, version=0)
class Microsoft_Windows_Shell_AuthUI_15020_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=15023, version=0)
class Microsoft_Windows_Shell_AuthUI_15023_0(Etw):
    pattern = Struct(
        "message1" / WString,
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=15024, version=0)
class Microsoft_Windows_Shell_AuthUI_15024_0(Etw):
    pattern = Struct(
        "message1" / WString,
        "message2" / WString
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=15025, version=0)
class Microsoft_Windows_Shell_AuthUI_15025_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul,
        "DWORD2" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=15026, version=0)
class Microsoft_Windows_Shell_AuthUI_15026_0(Etw):
    pattern = Struct(
        "message1" / WString,
        "DWORD1" / Int32ul,
        "DWORD2" / Int32ul,
        "Boolean1" / Int8ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=15027, version=0)
class Microsoft_Windows_Shell_AuthUI_15027_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul,
        "DWORD2" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=15028, version=0)
class Microsoft_Windows_Shell_AuthUI_15028_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul,
        "message1" / WString,
        "message2" / WString
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=15029, version=0)
class Microsoft_Windows_Shell_AuthUI_15029_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=15030, version=0)
class Microsoft_Windows_Shell_AuthUI_15030_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=15031, version=0)
class Microsoft_Windows_Shell_AuthUI_15031_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul,
        "DWORD2" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=15032, version=0)
class Microsoft_Windows_Shell_AuthUI_15032_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul,
        "DWORD2" / Int32ul,
        "DWORD3" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=15036, version=0)
class Microsoft_Windows_Shell_AuthUI_15036_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul,
        "DWORD2" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=25052, version=0)
class Microsoft_Windows_Shell_AuthUI_25052_0(Etw):
    pattern = Struct(
        "Boolean1" / Int8ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=25058, version=0)
class Microsoft_Windows_Shell_AuthUI_25058_0(Etw):
    pattern = Struct(
        "ReadyForInputScenario" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=25062, version=0)
class Microsoft_Windows_Shell_AuthUI_25062_0(Etw):
    pattern = Struct(
        "CredProvUsageScenario" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=25066, version=0)
class Microsoft_Windows_Shell_AuthUI_25066_0(Etw):
    pattern = Struct(
        "CredProvUsageScenario" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=25068, version=0)
class Microsoft_Windows_Shell_AuthUI_25068_0(Etw):
    pattern = Struct(
        "ReadyForInputScenario" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=25073, version=0)
class Microsoft_Windows_Shell_AuthUI_25073_0(Etw):
    pattern = Struct(
        "UserType" / Int32ul,
        "CredProvCount" / Int32ul,
        "IsLogonScenario" / Int32ul,
        "IsFirstLogon" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=25074, version=0)
class Microsoft_Windows_Shell_AuthUI_25074_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=25075, version=0)
class Microsoft_Windows_Shell_AuthUI_25075_0(Etw):
    pattern = Struct(
        "Boolean1" / Int8ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=25076, version=0)
class Microsoft_Windows_Shell_AuthUI_25076_0(Etw):
    pattern = Struct(
        "message1" / WString
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=25077, version=0)
class Microsoft_Windows_Shell_AuthUI_25077_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=25078, version=0)
class Microsoft_Windows_Shell_AuthUI_25078_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=25079, version=0)
class Microsoft_Windows_Shell_AuthUI_25079_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=25080, version=0)
class Microsoft_Windows_Shell_AuthUI_25080_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=25084, version=0)
class Microsoft_Windows_Shell_AuthUI_25084_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul,
        "DWORD2" / Int32ul,
        "DWORD3" / Int32ul,
        "DWORD4" / Int32ul,
        "DWORD5" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=25090, version=0)
class Microsoft_Windows_Shell_AuthUI_25090_0(Etw):
    pattern = Struct(
        "message1" / WString,
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=25093, version=0)
class Microsoft_Windows_Shell_AuthUI_25093_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=25100, version=0)
class Microsoft_Windows_Shell_AuthUI_25100_0(Etw):
    pattern = Struct(
        "OutstandingTasks" / Int32ul,
        "TasksCancelled" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=25101, version=0)
class Microsoft_Windows_Shell_AuthUI_25101_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=25113, version=0)
class Microsoft_Windows_Shell_AuthUI_25113_0(Etw):
    pattern = Struct(
        "InvokeObject" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=25114, version=0)
class Microsoft_Windows_Shell_AuthUI_25114_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=25116, version=0)
class Microsoft_Windows_Shell_AuthUI_25116_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=45013, version=0)
class Microsoft_Windows_Shell_AuthUI_45013_0(Etw):
    pattern = Struct(
        "Boolean1" / Int8ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=55013, version=0)
class Microsoft_Windows_Shell_AuthUI_55013_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=55014, version=0)
class Microsoft_Windows_Shell_AuthUI_55014_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=55015, version=0)
class Microsoft_Windows_Shell_AuthUI_55015_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=61001, version=0)
class Microsoft_Windows_Shell_AuthUI_61001_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=61010, version=0)
class Microsoft_Windows_Shell_AuthUI_61010_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=61014, version=0)
class Microsoft_Windows_Shell_AuthUI_61014_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=61016, version=0)
class Microsoft_Windows_Shell_AuthUI_61016_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=61017, version=0)
class Microsoft_Windows_Shell_AuthUI_61017_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=61019, version=0)
class Microsoft_Windows_Shell_AuthUI_61019_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=61021, version=0)
class Microsoft_Windows_Shell_AuthUI_61021_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=61023, version=0)
class Microsoft_Windows_Shell_AuthUI_61023_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=61025, version=0)
class Microsoft_Windows_Shell_AuthUI_61025_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=61026, version=0)
class Microsoft_Windows_Shell_AuthUI_61026_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=61031, version=0)
class Microsoft_Windows_Shell_AuthUI_61031_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=61033, version=0)
class Microsoft_Windows_Shell_AuthUI_61033_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=61035, version=0)
class Microsoft_Windows_Shell_AuthUI_61035_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=61037, version=0)
class Microsoft_Windows_Shell_AuthUI_61037_0(Etw):
    pattern = Struct(
        "DWORD1" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=64001, version=0)
class Microsoft_Windows_Shell_AuthUI_64001_0(Etw):
    pattern = Struct(
        "message1" / WString,
        "message2" / WString
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=64002, version=0)
class Microsoft_Windows_Shell_AuthUI_64002_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=64003, version=0)
class Microsoft_Windows_Shell_AuthUI_64003_0(Etw):
    pattern = Struct(
        "message1" / WString,
        "message2" / WString
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=64004, version=0)
class Microsoft_Windows_Shell_AuthUI_64004_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=64005, version=0)
class Microsoft_Windows_Shell_AuthUI_64005_0(Etw):
    pattern = Struct(
        "guid" / Guid,
        "message1" / WString,
        "message2" / WString
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=64006, version=0)
class Microsoft_Windows_Shell_AuthUI_64006_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=64007, version=0)
class Microsoft_Windows_Shell_AuthUI_64007_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=64008, version=0)
class Microsoft_Windows_Shell_AuthUI_64008_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=64009, version=0)
class Microsoft_Windows_Shell_AuthUI_64009_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=64010, version=0)
class Microsoft_Windows_Shell_AuthUI_64010_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=64501, version=0)
class Microsoft_Windows_Shell_AuthUI_64501_0(Etw):
    pattern = Struct(
        "guid" / Guid,
        "message1" / WString,
        "message2" / WString
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=64502, version=0)
class Microsoft_Windows_Shell_AuthUI_64502_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=64503, version=0)
class Microsoft_Windows_Shell_AuthUI_64503_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=64504, version=0)
class Microsoft_Windows_Shell_AuthUI_64504_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=64505, version=0)
class Microsoft_Windows_Shell_AuthUI_64505_0(Etw):
    pattern = Struct(
        "message1" / WString,
        "message2" / WString
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=64506, version=0)
class Microsoft_Windows_Shell_AuthUI_64506_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=64507, version=0)
class Microsoft_Windows_Shell_AuthUI_64507_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=64508, version=0)
class Microsoft_Windows_Shell_AuthUI_64508_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=64509, version=0)
class Microsoft_Windows_Shell_AuthUI_64509_0(Etw):
    pattern = Struct(
        "guid" / Guid,
        "message" / WString
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=64510, version=0)
class Microsoft_Windows_Shell_AuthUI_64510_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=65030, version=0)
class Microsoft_Windows_Shell_AuthUI_65030_0(Etw):
    pattern = Struct(
        "NotificationType" / Int32ul,
        "Operation" / Int32ul,
        "AppId" / WString
    )


@declare(guid=guid("63d2bb1d-e39a-41b8-9a3d-52dd06677588"), event_id=65032, version=0)
class Microsoft_Windows_Shell_AuthUI_65032_0(Etw):
    pattern = Struct(
        "NotificationType" / Int32ul,
        "Operation" / Int32ul,
        "AppId" / WString
    )

