# -*- coding: utf-8 -*-
"""
Microsoft-Windows-NWiFi
GUID : 0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10000, version=0)
class Microsoft_Windows_NWiFi_10000_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Status" / Int32ul,
        "ResetStatus" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10001, version=0)
class Microsoft_Windows_NWiFi_10001_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Function" / Int32ul,
        "Status" / Int32ul,
        "Length" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10002, version=0)
class Microsoft_Windows_NWiFi_10002_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10003, version=0)
class Microsoft_Windows_NWiFi_10003_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10004, version=0)
class Microsoft_Windows_NWiFi_10004_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "AlgorithmId" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10005, version=0)
class Microsoft_Windows_NWiFi_10005_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "SSIDCount" / Int32ul,
        "SSIDList" / Int8ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10006, version=0)
class Microsoft_Windows_NWiFi_10006_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10007, version=0)
class Microsoft_Windows_NWiFi_10007_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "BSSType" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10008, version=0)
class Microsoft_Windows_NWiFi_10008_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "BSSIDCount" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10009, version=0)
class Microsoft_Windows_NWiFi_10009_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "AuthCount" / Int32ul,
        "AuthAlgorithm" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10010, version=0)
class Microsoft_Windows_NWiFi_10010_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Value" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10011, version=0)
class Microsoft_Windows_NWiFi_10011_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Value" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10012, version=0)
class Microsoft_Windows_NWiFi_10012_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10013, version=0)
class Microsoft_Windows_NWiFi_10013_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "ExpectedCounter" / Int64ul,
        "ReceivedCounter" / Int64ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10014, version=0)
class Microsoft_Windows_NWiFi_10014_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "ExpectedVer" / Int32ul,
        "ReceivedVer" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10015, version=0)
class Microsoft_Windows_NWiFi_10015_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "FrameSequence" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10016, version=0)
class Microsoft_Windows_NWiFi_10016_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "FrameSequence" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10017, version=0)
class Microsoft_Windows_NWiFi_10017_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "FrameSequence" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10018, version=0)
class Microsoft_Windows_NWiFi_10018_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "FrameSequence" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10019, version=0)
class Microsoft_Windows_NWiFi_10019_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10020, version=0)
class Microsoft_Windows_NWiFi_10020_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10021, version=0)
class Microsoft_Windows_NWiFi_10021_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10022, version=0)
class Microsoft_Windows_NWiFi_10022_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10023, version=0)
class Microsoft_Windows_NWiFi_10023_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10024, version=0)
class Microsoft_Windows_NWiFi_10024_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10025, version=0)
class Microsoft_Windows_NWiFi_10025_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10026, version=0)
class Microsoft_Windows_NWiFi_10026_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10027, version=0)
class Microsoft_Windows_NWiFi_10027_0(Etw):
    pattern = Struct(
        "FrameSequence" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10028, version=0)
class Microsoft_Windows_NWiFi_10028_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10029, version=0)
class Microsoft_Windows_NWiFi_10029_0(Etw):
    pattern = Struct(
        "Adapter" / Int64ul,
        "OID" / Int32ul,
        "PowerState" / Int32ul,
        "bBlockOidsDueToLowPowerState" / Int8ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10030, version=0)
class Microsoft_Windows_NWiFi_10030_0(Etw):
    pattern = Struct(
        "Adapter" / Int64ul,
        "OID" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10031, version=0)
class Microsoft_Windows_NWiFi_10031_0(Etw):
    pattern = Struct(
        "Adapter" / Int64ul,
        "OID" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10032, version=0)
class Microsoft_Windows_NWiFi_10032_0(Etw):
    pattern = Struct(
        "Adapter" / Int64ul,
        "OID" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10033, version=0)
class Microsoft_Windows_NWiFi_10033_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10034, version=0)
class Microsoft_Windows_NWiFi_10034_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "EndPointType" / Int8ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10035, version=0)
class Microsoft_Windows_NWiFi_10035_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Enabled" / Int8ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10036, version=0)
class Microsoft_Windows_NWiFi_10036_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Enabled" / Int8ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10037, version=0)
class Microsoft_Windows_NWiFi_10037_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "ResetType" / Int8ul,
        "DefaultMIB" / Int8ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10038, version=0)
class Microsoft_Windows_NWiFi_10038_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "ResetType" / Int8ul,
        "DefaultMIB" / Int8ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10039, version=0)
class Microsoft_Windows_NWiFi_10039_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10040, version=0)
class Microsoft_Windows_NWiFi_10040_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10041, version=0)
class Microsoft_Windows_NWiFi_10041_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10042, version=0)
class Microsoft_Windows_NWiFi_10042_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Reason" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10043, version=0)
class Microsoft_Windows_NWiFi_10043_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10044, version=0)
class Microsoft_Windows_NWiFi_10044_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "SessionId" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10045, version=0)
class Microsoft_Windows_NWiFi_10045_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "SessionId" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10046, version=0)
class Microsoft_Windows_NWiFi_10046_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "SessionId" / Int32ul,
        "Controlled" / Int8ul,
        "Authorized" / Int8ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10047, version=0)
class Microsoft_Windows_NWiFi_10047_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "SessionId" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10048, version=0)
class Microsoft_Windows_NWiFi_10048_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10049, version=0)
class Microsoft_Windows_NWiFi_10049_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Irp" / Int64ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10050, version=0)
class Microsoft_Windows_NWiFi_10050_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10051, version=0)
class Microsoft_Windows_NWiFi_10051_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "PowerState" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10052, version=0)
class Microsoft_Windows_NWiFi_10052_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "PowerState" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10053, version=0)
class Microsoft_Windows_NWiFi_10053_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Irp" / Int64ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10054, version=0)
class Microsoft_Windows_NWiFi_10054_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10055, version=0)
class Microsoft_Windows_NWiFi_10055_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10056, version=0)
class Microsoft_Windows_NWiFi_10056_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10057, version=0)
class Microsoft_Windows_NWiFi_10057_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "OldPowerState" / Int32ul,
        "NewPowerState" / Int32ul,
        "Halting" / Int8ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10058, version=0)
class Microsoft_Windows_NWiFi_10058_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "ConfiguredOpMode" / Int32ul,
        "IMSupportedOpModes" / Int32ul,
        "MiniPortSupportedOpModes" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10059, version=0)
class Microsoft_Windows_NWiFi_10059_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10060, version=0)
class Microsoft_Windows_NWiFi_10060_0(Etw):
    pattern = Struct(
        "CipherAlgoId" / Int32ul,
        "Direction" / Int8ul,
        "Len" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10061, version=0)
class Microsoft_Windows_NWiFi_10061_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "CipherAlgoId" / Int32ul,
        "Direction" / Int8ul,
        "Len" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10062, version=0)
class Microsoft_Windows_NWiFi_10062_0(Etw):
    pattern = Struct(
        "AdapterGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10063, version=0)
class Microsoft_Windows_NWiFi_10063_0(Etw):
    pattern = Struct(
        "AdapterGuid" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10064, version=0)
class Microsoft_Windows_NWiFi_10064_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10066, version=0)
class Microsoft_Windows_NWiFi_10066_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ContextHandle" / Int64ul,
        "MAC" / CString,
        "SSID" / CString
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10067, version=0)
class Microsoft_Windows_NWiFi_10067_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ContextHandle" / Int64ul,
        "MAC" / CString,
        "SSID" / CString
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10068, version=0)
class Microsoft_Windows_NWiFi_10068_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ErrorCode" / Int32ul,
        "ContextHandle" / Int64ul,
        "MAC" / CString,
        "SSID" / CString
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10069, version=0)
class Microsoft_Windows_NWiFi_10069_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ContextHandle" / Int64ul,
        "MAC" / CString,
        "SSID" / CString
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10070, version=0)
class Microsoft_Windows_NWiFi_10070_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ContextHandle" / Int64ul,
        "MAC" / CString,
        "SSID" / CString
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10071, version=0)
class Microsoft_Windows_NWiFi_10071_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ErrorCode" / Int32ul,
        "ContextHandle" / Int64ul,
        "MAC" / CString,
        "SSID" / CString
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10072, version=0)
class Microsoft_Windows_NWiFi_10072_0(Etw):
    pattern = Struct(
        "PowerMgmtMode" / Int32ul,
        "PowerMgmtModeSupported" / Int8ul,
        "AdapterGuid" / Guid,
        "SSID" / CString
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10073, version=0)
class Microsoft_Windows_NWiFi_10073_0(Etw):
    pattern = Struct(
        "AdapterGuid" / Guid,
        "Halted" / Int8ul,
        "NewPowerState" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10074, version=0)
class Microsoft_Windows_NWiFi_10074_0(Etw):
    pattern = Struct(
        "AdapterGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10075, version=0)
class Microsoft_Windows_NWiFi_10075_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10076, version=0)
class Microsoft_Windows_NWiFi_10076_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "AdapterGuid" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10077, version=0)
class Microsoft_Windows_NWiFi_10077_0(Etw):
    pattern = Struct(
        "AdapterGuid" / Guid,
        "TxUnicastCount" / Int32sl,
        "RxUnicastCount" / Int32sl,
        "TxBroadcastCount" / Int32sl,
        "RxBroadcastCount" / Int32sl,
        "TxMulticastCount" / Int32sl,
        "RxMulticastCount" / Int32sl,
        "TimeDiffMs" / Int64ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10078, version=0)
class Microsoft_Windows_NWiFi_10078_0(Etw):
    pattern = Struct(
        "AdapterGuid" / Guid,
        "SessionId" / Int32sl,
        "Reason" / Int32sl,
        "StatusCode" / Int32sl,
        "SecurityEndpoint" / Int32sl
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10079, version=0)
class Microsoft_Windows_NWiFi_10079_0(Etw):
    pattern = Struct(
        "AdapterGuid" / Guid,
        "DisconnectInStandby" / Int32sl,
        "EnforceDs" / Int32sl
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10080, version=0)
class Microsoft_Windows_NWiFi_10080_0(Etw):
    pattern = Struct(
        "AdapterGuid" / Guid,
        "SessionId" / Int32sl,
        "Reason" / Int32sl,
        "StatusCode" / Int32sl,
        "SecurityEndpoint" / Int32sl
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10081, version=0)
class Microsoft_Windows_NWiFi_10081_0(Etw):
    pattern = Struct(
        "AdapterGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10082, version=0)
class Microsoft_Windows_NWiFi_10082_0(Etw):
    pattern = Struct(
        "AdapterGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10083, version=0)
class Microsoft_Windows_NWiFi_10083_0(Etw):
    pattern = Struct(
        "AdapterGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10084, version=0)
class Microsoft_Windows_NWiFi_10084_0(Etw):
    pattern = Struct(
        "StatusAnnotation" / WString,
        "Status" / Int32ul,
        "Context1" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10085, version=0)
class Microsoft_Windows_NWiFi_10085_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "Initialized" / Int32ul,
        "State" / Int32ul,
        "Counter" / Int32ul,
        "LocalSendConfirm" / Int32ul,
        "PeerSendConfirm" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10086, version=0)
class Microsoft_Windows_NWiFi_10086_0(Etw):
    pattern = Struct(
        "BufferAnnotation" / WString,
        "BufferLength" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10087, version=0)
class Microsoft_Windows_NWiFi_10087_0(Etw):
    pattern = Struct(
        "LogLine" / WString
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10088, version=0)
class Microsoft_Windows_NWiFi_10088_0(Etw):
    pattern = Struct(
        "CommitFrameError" / CString,
        "CommitFrameSize" / Int32ul,
        "MinCommitFrameSize" / Int32ul,
        "AlgorithmNumber" / Int32ul,
        "ExpectedAlgorithmNumber" / Int32ul,
        "TransactionId" / Int32ul,
        "ExpectedTransactionId" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=10089, version=0)
class Microsoft_Windows_NWiFi_10089_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "Context1" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=20000, version=0)
class Microsoft_Windows_NWiFi_20000_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=20001, version=0)
class Microsoft_Windows_NWiFi_20001_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=20002, version=0)
class Microsoft_Windows_NWiFi_20002_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=20003, version=0)
class Microsoft_Windows_NWiFi_20003_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=20004, version=0)
class Microsoft_Windows_NWiFi_20004_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=20005, version=0)
class Microsoft_Windows_NWiFi_20005_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=20006, version=0)
class Microsoft_Windows_NWiFi_20006_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=20007, version=0)
class Microsoft_Windows_NWiFi_20007_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=20008, version=0)
class Microsoft_Windows_NWiFi_20008_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=20009, version=0)
class Microsoft_Windows_NWiFi_20009_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=20010, version=0)
class Microsoft_Windows_NWiFi_20010_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=20011, version=0)
class Microsoft_Windows_NWiFi_20011_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=20012, version=0)
class Microsoft_Windows_NWiFi_20012_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=20013, version=0)
class Microsoft_Windows_NWiFi_20013_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=20014, version=0)
class Microsoft_Windows_NWiFi_20014_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=20015, version=0)
class Microsoft_Windows_NWiFi_20015_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=20016, version=0)
class Microsoft_Windows_NWiFi_20016_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=20017, version=0)
class Microsoft_Windows_NWiFi_20017_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=60001, version=0)
class Microsoft_Windows_NWiFi_60001_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=60002, version=0)
class Microsoft_Windows_NWiFi_60002_0(Etw):
    pattern = Struct(
        "WarningCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=60003, version=0)
class Microsoft_Windows_NWiFi_60003_0(Etw):
    pattern = Struct(
        "NextState" / Int8ul,
        "Context" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=60004, version=0)
class Microsoft_Windows_NWiFi_60004_0(Etw):
    pattern = Struct(
        "Context" / Int32ul,
        "UpdateReasonCode" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=60101, version=0)
class Microsoft_Windows_NWiFi_60101_0(Etw):
    pattern = Struct(
        "SourceAddress" / Int32ul,
        "SourcePort" / Int32ul,
        "DestinationAddress" / Int32ul,
        "DestinationPort" / Int32ul,
        "Protocol" / Int32ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=60102, version=0)
class Microsoft_Windows_NWiFi_60102_0(Etw):
    pattern = Struct(
        "SourcePort" / Int32ul,
        "DestinationPort" / Int32ul,
        "Protocol" / Int32ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("0bd3506a-9030-4f76-9b88-3e8fe1f7cfb6"), event_id=60103, version=0)
class Microsoft_Windows_NWiFi_60103_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )

