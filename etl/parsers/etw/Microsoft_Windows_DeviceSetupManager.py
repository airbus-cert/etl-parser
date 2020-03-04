# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DeviceSetupManager
GUID : fcbb06bb-6a2a-46e3-abaa-246cb4e508b2
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=100, version=0)
class Microsoft_Windows_DeviceSetupManager_100_0(Etw):
    pattern = Struct(
        "Prop_CoreServiceMode" / Int32ul,
        "Prop_Event_Window_Seconds" / Int64sl
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=101, version=0)
class Microsoft_Windows_DeviceSetupManager_101_0(Etw):
    pattern = Struct(
        "Prop_UpTime_Seconds" / Int64sl,
        "Prop_WorkTime_MilliSeconds" / Int64sl
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=104, version=0)
class Microsoft_Windows_DeviceSetupManager_104_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=106, version=0)
class Microsoft_Windows_DeviceSetupManager_106_0(Etw):
    pattern = Struct(
        "Prop_RetryCycleCount" / Int32ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=108, version=0)
class Microsoft_Windows_DeviceSetupManager_108_0(Etw):
    pattern = Struct(
        "Prop_CoreServiceState" / Int32ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=109, version=0)
class Microsoft_Windows_DeviceSetupManager_109_0(Etw):
    pattern = Struct(
        "Prop_CoreServiceMode" / Int32ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=110, version=0)
class Microsoft_Windows_DeviceSetupManager_110_0(Etw):
    pattern = Struct(
        "Prop_ContainerId" / Guid,
        "Prop_JobId" / Int32ul,
        "Prop_JobType" / Int32ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=111, version=0)
class Microsoft_Windows_DeviceSetupManager_111_0(Etw):
    pattern = Struct(
        "Prop_ContainerId" / Guid,
        "Prop_JobId" / Int32ul,
        "Prop_JobStatus" / Int32ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=112, version=0)
class Microsoft_Windows_DeviceSetupManager_112_0(Etw):
    pattern = Struct(
        "Prop_DeviceName" / WString,
        "Prop_ContainerId" / Guid,
        "Prop_TaskCount" / Int32sl,
        "Prop_PropertyCount" / Int32sl,
        "Prop_WorkTime_MilliSeconds" / Int64sl
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=120, version=0)
class Microsoft_Windows_DeviceSetupManager_120_0(Etw):
    pattern = Struct(
        "Prop_PackageId" / WString,
        "Prop_MilliSeconds" / Int64sl
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=121, version=0)
class Microsoft_Windows_DeviceSetupManager_121_0(Etw):
    pattern = Struct(
        "Prop_DevnodeId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=123, version=0)
class Microsoft_Windows_DeviceSetupManager_123_0(Etw):
    pattern = Struct(
        "Prop_Seconds" / Int32sl,
        "Prop_DeviceId" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=124, version=0)
class Microsoft_Windows_DeviceSetupManager_124_0(Etw):
    pattern = Struct(
        "Prop_PackageId" / WString,
        "Prop_DeviceInstanceId" / WString,
        "Prop_MilliSeconds" / Int64sl
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=125, version=0)
class Microsoft_Windows_DeviceSetupManager_125_0(Etw):
    pattern = Struct(
        "Prop_DevnodeId" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=126, version=0)
class Microsoft_Windows_DeviceSetupManager_126_0(Etw):
    pattern = Struct(
        "Prop_DeviceInstanceId" / WString,
        "Prop_PackageId" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=130, version=0)
class Microsoft_Windows_DeviceSetupManager_130_0(Etw):
    pattern = Struct(
        "Prop_MetadataPackageId" / WString,
        "Prop_ContainerId" / Guid,
        "Prop_StageTimeMilliSeconds" / Int64sl
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=131, version=0)
class Microsoft_Windows_DeviceSetupManager_131_0(Etw):
    pattern = Struct(
        "Prop_ContainerId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=150, version=0)
class Microsoft_Windows_DeviceSetupManager_150_0(Etw):
    pattern = Struct(
        "Prop_DeviceName" / WString,
        "Prop_ContainerId" / Guid
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=151, version=0)
class Microsoft_Windows_DeviceSetupManager_151_0(Etw):
    pattern = Struct(
        "Prop_DeviceName" / WString,
        "Prop_ContainerId" / Guid
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=152, version=0)
class Microsoft_Windows_DeviceSetupManager_152_0(Etw):
    pattern = Struct(
        "Prop_DevnodeId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=160, version=0)
class Microsoft_Windows_DeviceSetupManager_160_0(Etw):
    pattern = Struct(
        "Prop_SoftwareName" / WString,
        "Prop_DeviceInstanceId" / WString,
        "Prop_InstallTime" / Int64ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=161, version=0)
class Microsoft_Windows_DeviceSetupManager_161_0(Etw):
    pattern = Struct(
        "Prop_SoftwareName" / WString,
        "Prop_HiHighPartNew" / Int32ul,
        "Prop_LoHighPartNew" / Int32ul,
        "Prop_HiLowPartNew" / Int32ul,
        "Prop_LoLowPartNew" / Int32ul,
        "Prop_HiHighPartOld" / Int32ul,
        "Prop_LoHighPartOld" / Int32ul,
        "Prop_HiLowPartOld" / Int32ul,
        "Prop_LoLowPartOld" / Int32ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=162, version=0)
class Microsoft_Windows_DeviceSetupManager_162_0(Etw):
    pattern = Struct(
        "Prop_SoftwareName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=163, version=0)
class Microsoft_Windows_DeviceSetupManager_163_0(Etw):
    pattern = Struct(
        "Prop_SoftwareName" / WString,
        "Error" / Int32ul,
        "ExitCode" / Int32ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=164, version=0)
class Microsoft_Windows_DeviceSetupManager_164_0(Etw):
    pattern = Struct(
        "Prop_SoftwareName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=165, version=0)
class Microsoft_Windows_DeviceSetupManager_165_0(Etw):
    pattern = Struct(
        "Prop_SoftwareName" / WString,
        "Prop_CommandLine" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=166, version=0)
class Microsoft_Windows_DeviceSetupManager_166_0(Etw):
    pattern = Struct(
        "Prop_DeviceInstanceId" / WString,
        "Prop_SoftwareLinks" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=167, version=0)
class Microsoft_Windows_DeviceSetupManager_167_0(Etw):
    pattern = Struct(
        "Prop_SoftwarePfn" / WString,
        "Prop_ProductId" / WString,
        "Prop_IsFramework" / Int32ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=168, version=0)
class Microsoft_Windows_DeviceSetupManager_168_0(Etw):
    pattern = Struct(
        "Prop_SoftwarePfn" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=169, version=0)
class Microsoft_Windows_DeviceSetupManager_169_0(Etw):
    pattern = Struct(
        "Prop_ProductId" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=170, version=0)
class Microsoft_Windows_DeviceSetupManager_170_0(Etw):
    pattern = Struct(
        "Prop_ProductId" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=171, version=0)
class Microsoft_Windows_DeviceSetupManager_171_0(Etw):
    pattern = Struct(
        "Prop_ProductId" / WString,
        "Prop_InstallType" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=180, version=0)
class Microsoft_Windows_DeviceSetupManager_180_0(Etw):
    pattern = Struct(
        "Prop_ProductId" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=220, version=0)
class Microsoft_Windows_DeviceSetupManager_220_0(Etw):
    pattern = Struct(
        "Prop_ContainerId" / WString,
        "Prop_PackageId" / WString,
        "Prop_NotificationHandler" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=221, version=0)
class Microsoft_Windows_DeviceSetupManager_221_0(Etw):
    pattern = Struct(
        "Prop_ContainerId" / WString,
        "Prop_PackageId" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=222, version=0)
class Microsoft_Windows_DeviceSetupManager_222_0(Etw):
    pattern = Struct(
        "Prop_ContainerId" / WString,
        "Prop_PackageId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=223, version=0)
class Microsoft_Windows_DeviceSetupManager_223_0(Etw):
    pattern = Struct(
        "Prop_PackageId" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=224, version=0)
class Microsoft_Windows_DeviceSetupManager_224_0(Etw):
    pattern = Struct(
        "Prop_PackageId" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=230, version=0)
class Microsoft_Windows_DeviceSetupManager_230_0(Etw):
    pattern = Struct(
        "Prop_ContainerId" / WString,
        "Prop_PackageId" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=231, version=0)
class Microsoft_Windows_DeviceSetupManager_231_0(Etw):
    pattern = Struct(
        "Prop_ContainerId" / WString,
        "Prop_PackageId" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=232, version=0)
class Microsoft_Windows_DeviceSetupManager_232_0(Etw):
    pattern = Struct(
        "Prop_ContainerId" / WString,
        "Prop_PackageId" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=233, version=0)
class Microsoft_Windows_DeviceSetupManager_233_0(Etw):
    pattern = Struct(
        "Prop_ContainerId" / WString,
        "Prop_PackageId" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=234, version=0)
class Microsoft_Windows_DeviceSetupManager_234_0(Etw):
    pattern = Struct(
        "Prop_DevnodeId" / WString,
        "Prop_MilliSeconds" / Int64sl
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=300, version=0)
class Microsoft_Windows_DeviceSetupManager_300_0(Etw):
    pattern = Struct(
        "Prop_ContainerId" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=301, version=0)
class Microsoft_Windows_DeviceSetupManager_301_0(Etw):
    pattern = Struct(
        "Prop_ContainerId" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=302, version=0)
class Microsoft_Windows_DeviceSetupManager_302_0(Etw):
    pattern = Struct(
        "Prop_ContainerId" / WString,
        "Prop_ServiceInfoNamespace" / WString,
        "Prop_CultureCode" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=400, version=0)
class Microsoft_Windows_DeviceSetupManager_400_0(Etw):
    pattern = Struct(
        "Prop_ContainerId" / Guid
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=401, version=0)
class Microsoft_Windows_DeviceSetupManager_401_0(Etw):
    pattern = Struct(
        "Prop_ContainerId" / Guid
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=402, version=0)
class Microsoft_Windows_DeviceSetupManager_402_0(Etw):
    pattern = Struct(
        "Prop_DevnodeId" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=403, version=0)
class Microsoft_Windows_DeviceSetupManager_403_0(Etw):
    pattern = Struct(
        "Prop_DevnodeId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=404, version=0)
class Microsoft_Windows_DeviceSetupManager_404_0(Etw):
    pattern = Struct(
        "Prop_PackagePath" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=405, version=0)
class Microsoft_Windows_DeviceSetupManager_405_0(Etw):
    pattern = Struct(
        "Prop_PackagePath" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=406, version=0)
class Microsoft_Windows_DeviceSetupManager_406_0(Etw):
    pattern = Struct(
        "Prop_DevnodeId" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=407, version=0)
class Microsoft_Windows_DeviceSetupManager_407_0(Etw):
    pattern = Struct(
        "Prop_DevnodeId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=408, version=0)
class Microsoft_Windows_DeviceSetupManager_408_0(Etw):
    pattern = Struct(
        "Prop_ContainerId" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=409, version=0)
class Microsoft_Windows_DeviceSetupManager_409_0(Etw):
    pattern = Struct(
        "Prop_ContainerId" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=410, version=0)
class Microsoft_Windows_DeviceSetupManager_410_0(Etw):
    pattern = Struct(
        "Prop_DevnodeId" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=411, version=0)
class Microsoft_Windows_DeviceSetupManager_411_0(Etw):
    pattern = Struct(
        "Prop_DevnodeId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=412, version=0)
class Microsoft_Windows_DeviceSetupManager_412_0(Etw):
    pattern = Struct(
        "Prop_DevnodeId" / WString
    )


@declare(guid=guid("fcbb06bb-6a2a-46e3-abaa-246cb4e508b2"), event_id=413, version=0)
class Microsoft_Windows_DeviceSetupManager_413_0(Etw):
    pattern = Struct(
        "Prop_DevnodeId" / WString
    )

