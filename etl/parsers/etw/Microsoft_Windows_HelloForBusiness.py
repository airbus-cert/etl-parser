# -*- coding: utf-8 -*-
"""
Microsoft-Windows-HelloForBusiness
GUID : 906b8a99-63ce-58d7-86ab-10989bbd5567
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=3045, version=0)
class Microsoft_Windows_HelloForBusiness_3045_0(Etw):
    pattern = Struct(
        "HelloScenarioType" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=3060, version=0)
class Microsoft_Windows_HelloForBusiness_3060_0(Etw):
    pattern = Struct(
        "UserSid" / Sid
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=3065, version=0)
class Microsoft_Windows_HelloForBusiness_3065_0(Etw):
    pattern = Struct(
        "HelloScenarioType" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=3130, version=0)
class Microsoft_Windows_HelloForBusiness_3130_0(Etw):
    pattern = Struct(
        "PinRecoveryEntryType" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=3520, version=0)
class Microsoft_Windows_HelloForBusiness_3520_0(Etw):
    pattern = Struct(
        "DeviceUnlockProvider" / WString,
        "DeviceUnlockGroupA" / WString,
        "DeviceUnlockGroupB" / WString
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=5000, version=0)
class Microsoft_Windows_HelloForBusiness_5000_0(Etw):
    pattern = Struct(
        "Manufacturer" / WString,
        "Version" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=5001, version=0)
class Microsoft_Windows_HelloForBusiness_5001_0(Etw):
    pattern = Struct(
        "CredentialType" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=5050, version=0)
class Microsoft_Windows_HelloForBusiness_5050_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "NumberOfAvailableKeys" / Int32ul,
        "ElapsedTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=5060, version=0)
class Microsoft_Windows_HelloForBusiness_5060_0(Etw):
    pattern = Struct(
        "PinRecoveryPolicyState" / Int32ul,
        "UserSid" / Sid
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=5062, version=0)
class Microsoft_Windows_HelloForBusiness_5062_0(Etw):
    pattern = Struct(
        "UserSid" / Sid
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=5063, version=0)
class Microsoft_Windows_HelloForBusiness_5063_0(Etw):
    pattern = Struct(
        "UserSid" / Sid
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=5204, version=0)
class Microsoft_Windows_HelloForBusiness_5204_0(Etw):
    pattern = Struct(
        "CertificateEnrollmentMethod" / Int32ul,
        "CertificateRequired" / Int8ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=5225, version=0)
class Microsoft_Windows_HelloForBusiness_5225_0(Etw):
    pattern = Struct(
        "KeyProvider" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=5555, version=0)
class Microsoft_Windows_HelloForBusiness_5555_0(Etw):
    pattern = Struct(
        "TpmSupport" / Int32ul,
        "HardwarePolicy" / Int32ul,
        "IsTpm12Excluded" / Int8ul,
        "TpmVersion" / Int32ul,
        "IsTpmFIPS" / Int8ul,
        "IsTpmLockedOut" / Int8ul,
        "IsKeyPregenPoolSatisfactory" / Int8ul,
        "KeyProvider" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=6010, version=0)
class Microsoft_Windows_HelloForBusiness_6010_0(Etw):
    pattern = Struct(
        "KeyName" / WString,
        "KeyUseCredUnavailableReason" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=6045, version=0)
class Microsoft_Windows_HelloForBusiness_6045_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=6055, version=0)
class Microsoft_Windows_HelloForBusiness_6055_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=6065, version=0)
class Microsoft_Windows_HelloForBusiness_6065_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=6066, version=0)
class Microsoft_Windows_HelloForBusiness_6066_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=6525, version=0)
class Microsoft_Windows_HelloForBusiness_6525_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7002, version=0)
class Microsoft_Windows_HelloForBusiness_7002_0(Etw):
    pattern = Struct(
        "ContainerId" / Guid,
        "Error" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7025, version=0)
class Microsoft_Windows_HelloForBusiness_7025_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7030, version=0)
class Microsoft_Windows_HelloForBusiness_7030_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7031, version=0)
class Microsoft_Windows_HelloForBusiness_7031_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7032, version=0)
class Microsoft_Windows_HelloForBusiness_7032_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7045, version=0)
class Microsoft_Windows_HelloForBusiness_7045_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7052, version=0)
class Microsoft_Windows_HelloForBusiness_7052_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7053, version=0)
class Microsoft_Windows_HelloForBusiness_7053_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7054, version=0)
class Microsoft_Windows_HelloForBusiness_7054_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7055, version=0)
class Microsoft_Windows_HelloForBusiness_7055_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7060, version=0)
class Microsoft_Windows_HelloForBusiness_7060_0(Etw):
    pattern = Struct(
        "UserSid" / Sid,
        "ErrorText" / WString,
        "Error" / Int32ul,
        "CorrelationVector" / CString,
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7065, version=0)
class Microsoft_Windows_HelloForBusiness_7065_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7066, version=0)
class Microsoft_Windows_HelloForBusiness_7066_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7067, version=0)
class Microsoft_Windows_HelloForBusiness_7067_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "KeyName" / WString,
        "CertificateType" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7130, version=0)
class Microsoft_Windows_HelloForBusiness_7130_0(Etw):
    pattern = Struct(
        "ErrorText" / WString,
        "Error" / Int32ul,
        "CorrelationVector" / CString,
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7205, version=0)
class Microsoft_Windows_HelloForBusiness_7205_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7225, version=0)
class Microsoft_Windows_HelloForBusiness_7225_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7226, version=0)
class Microsoft_Windows_HelloForBusiness_7226_0(Etw):
    pattern = Struct(
        "KeyType" / Int32ul,
        "KeyName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7510, version=0)
class Microsoft_Windows_HelloForBusiness_7510_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7520, version=0)
class Microsoft_Windows_HelloForBusiness_7520_0(Etw):
    pattern = Struct(
        "ErrorText" / WString,
        "Error" / Int32ul,
        "CorrelationVector" / CString,
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7525, version=0)
class Microsoft_Windows_HelloForBusiness_7525_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7555, version=0)
class Microsoft_Windows_HelloForBusiness_7555_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7601, version=0)
class Microsoft_Windows_HelloForBusiness_7601_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7611, version=0)
class Microsoft_Windows_HelloForBusiness_7611_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7621, version=0)
class Microsoft_Windows_HelloForBusiness_7621_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=7631, version=0)
class Microsoft_Windows_HelloForBusiness_7631_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=8002, version=0)
class Microsoft_Windows_HelloForBusiness_8002_0(Etw):
    pattern = Struct(
        "ContainerId" / Guid,
        "ContainerVersion" / Int32ul,
        "KeyProvider" / Int32ul,
        "HasCachedLogonKey" / Int8ul,
        "ContainerStatus" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=8025, version=0)
class Microsoft_Windows_HelloForBusiness_8025_0(Etw):
    pattern = Struct(
        "ServiceName" / WString
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=8045, version=0)
class Microsoft_Windows_HelloForBusiness_8045_0(Etw):
    pattern = Struct(
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=8052, version=0)
class Microsoft_Windows_HelloForBusiness_8052_0(Etw):
    pattern = Struct(
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=8053, version=0)
class Microsoft_Windows_HelloForBusiness_8053_0(Etw):
    pattern = Struct(
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=8055, version=0)
class Microsoft_Windows_HelloForBusiness_8055_0(Etw):
    pattern = Struct(
        "ProcessingTime" / Int32ul,
        "UsedExistingContainer" / Int8ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=8060, version=0)
class Microsoft_Windows_HelloForBusiness_8060_0(Etw):
    pattern = Struct(
        "UserSid" / Sid,
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=8065, version=0)
class Microsoft_Windows_HelloForBusiness_8065_0(Etw):
    pattern = Struct(
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=8066, version=0)
class Microsoft_Windows_HelloForBusiness_8066_0(Etw):
    pattern = Struct(
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=8067, version=0)
class Microsoft_Windows_HelloForBusiness_8067_0(Etw):
    pattern = Struct(
        "KeyName" / WString,
        "CertificateType" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=8130, version=0)
class Microsoft_Windows_HelloForBusiness_8130_0(Etw):
    pattern = Struct(
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=8225, version=0)
class Microsoft_Windows_HelloForBusiness_8225_0(Etw):
    pattern = Struct(
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=8226, version=0)
class Microsoft_Windows_HelloForBusiness_8226_0(Etw):
    pattern = Struct(
        "KeyProvider" / Int32ul,
        "KeyType" / Int32ul,
        "KeyName" / WString
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=8520, version=0)
class Microsoft_Windows_HelloForBusiness_8520_0(Etw):
    pattern = Struct(
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=8525, version=0)
class Microsoft_Windows_HelloForBusiness_8525_0(Etw):
    pattern = Struct(
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=8555, version=0)
class Microsoft_Windows_HelloForBusiness_8555_0(Etw):
    pattern = Struct(
        "ProcessingTime" / Int32ul
    )


@declare(guid=guid("906b8a99-63ce-58d7-86ab-10989bbd5567"), event_id=8601, version=0)
class Microsoft_Windows_HelloForBusiness_8601_0(Etw):
    pattern = Struct(
        "ProcessingTime" / Int32ul
    )

