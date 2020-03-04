# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DSC
GUID : 50df9e12-a8c4-4939-b281-47e1325ba63e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4097, version=0)
class Microsoft_Windows_DSC_4097_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "ComponentName" / WString,
        "ErrorId" / Int32ul,
        "ErrorDetail" / WString,
        "ResourceId" / WString,
        "SourceInfo" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4098, version=0)
class Microsoft_Windows_DSC_4098_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "WMIMessageChannel" / Int32ul,
        "ResourceId" / WString,
        "MessageBody" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4099, version=0)
class Microsoft_Windows_DSC_4099_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "MethodName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4100, version=0)
class Microsoft_Windows_DSC_4100_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "WMIMessageChannel" / Int32ul,
        "ResourceId" / WString,
        "MessageBody" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4101, version=0)
class Microsoft_Windows_DSC_4101_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "ClassName" / WString,
        "MessageBody" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4102, version=0)
class Microsoft_Windows_DSC_4102_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "Operation" / WString,
        "UserSid" / WString,
        "ComputerName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4103, version=0)
class Microsoft_Windows_DSC_4103_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "ComponentName" / WString,
        "OperationCmd" / WString,
        "ProviderName" / WString,
        "FullyQualifiedErrorId" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4104, version=0)
class Microsoft_Windows_DSC_4104_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "ComponentName" / WString,
        "DownloadManagerName" / WString,
        "ErrorId" / Int32ul,
        "ErrorDetail" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4105, version=0)
class Microsoft_Windows_DSC_4105_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "DownloadManagerName" / WString,
        "ConfigurationId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4106, version=0)
class Microsoft_Windows_DSC_4106_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "DownloadManagerName" / WString,
        "ConfigurationId" / WString,
        "Modules" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4107, version=0)
class Microsoft_Windows_DSC_4107_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "DownloadManagerName" / WString,
        "ConfigurationId" / WString,
        "Checksum" / WString,
        "Compliant" / Int8ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4108, version=0)
class Microsoft_Windows_DSC_4108_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "DownloadManagerName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4109, version=0)
class Microsoft_Windows_DSC_4109_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "DownloadManagerName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4110, version=0)
class Microsoft_Windows_DSC_4110_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "ActionStatus" / WString,
        "DownloadManagerName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4111, version=0)
class Microsoft_Windows_DSC_4111_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "Thumbprint" / WString,
        "Path" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4112, version=0)
class Microsoft_Windows_DSC_4112_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "Thumbprint" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4113, version=0)
class Microsoft_Windows_DSC_4113_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "Path" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4114, version=0)
class Microsoft_Windows_DSC_4114_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4115, version=0)
class Microsoft_Windows_DSC_4115_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4116, version=0)
class Microsoft_Windows_DSC_4116_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "ErrorId" / Int32ul,
        "ErrorDetail" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4117, version=0)
class Microsoft_Windows_DSC_4117_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "ResourceId" / WString,
        "MessageBody" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4118, version=0)
class Microsoft_Windows_DSC_4118_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "ResourceId" / WString,
        "MessageBody" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4119, version=0)
class Microsoft_Windows_DSC_4119_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "MethodName" / WString,
        "ClassName" / WString,
        "ResourceID" / WString,
        "Flags" / Int32ul,
        "ExecutionMode" / Int32ul,
        "ProviderNamespace" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4120, version=0)
class Microsoft_Windows_DSC_4120_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "MethodName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4121, version=0)
class Microsoft_Windows_DSC_4121_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "TotalSize" / Int32ul,
        "RemainingSize" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4128, version=0)
class Microsoft_Windows_DSC_4128_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4129, version=0)
class Microsoft_Windows_DSC_4129_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4130, version=0)
class Microsoft_Windows_DSC_4130_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4131, version=0)
class Microsoft_Windows_DSC_4131_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "ErrorMessage" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4132, version=0)
class Microsoft_Windows_DSC_4132_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4133, version=0)
class Microsoft_Windows_DSC_4133_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4134, version=0)
class Microsoft_Windows_DSC_4134_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4135, version=0)
class Microsoft_Windows_DSC_4135_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4136, version=0)
class Microsoft_Windows_DSC_4136_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4137, version=0)
class Microsoft_Windows_DSC_4137_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4144, version=0)
class Microsoft_Windows_DSC_4144_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4145, version=0)
class Microsoft_Windows_DSC_4145_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / Int32ul,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4146, version=0)
class Microsoft_Windows_DSC_4146_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4147, version=0)
class Microsoft_Windows_DSC_4147_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4148, version=0)
class Microsoft_Windows_DSC_4148_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4149, version=0)
class Microsoft_Windows_DSC_4149_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4150, version=0)
class Microsoft_Windows_DSC_4150_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4151, version=0)
class Microsoft_Windows_DSC_4151_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4152, version=0)
class Microsoft_Windows_DSC_4152_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4153, version=0)
class Microsoft_Windows_DSC_4153_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4160, version=0)
class Microsoft_Windows_DSC_4160_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4161, version=0)
class Microsoft_Windows_DSC_4161_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4162, version=0)
class Microsoft_Windows_DSC_4162_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4163, version=0)
class Microsoft_Windows_DSC_4163_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4164, version=0)
class Microsoft_Windows_DSC_4164_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4165, version=0)
class Microsoft_Windows_DSC_4165_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4166, version=0)
class Microsoft_Windows_DSC_4166_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4167, version=0)
class Microsoft_Windows_DSC_4167_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4168, version=0)
class Microsoft_Windows_DSC_4168_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "FunctionName" / WString,
        "ClassName" / WString,
        "MethodName" / WString,
        "Namespace" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4169, version=0)
class Microsoft_Windows_DSC_4169_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "MethodName" / WString,
        "DataSize" / Int32ul,
        "Flags" / Int32ul,
        "ExecutionMode" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4176, version=0)
class Microsoft_Windows_DSC_4176_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "paramNumber" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4177, version=0)
class Microsoft_Windows_DSC_4177_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / Int32ul,
        "param2" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4178, version=0)
class Microsoft_Windows_DSC_4178_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4179, version=0)
class Microsoft_Windows_DSC_4179_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / Int32ul,
        "param3" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4180, version=0)
class Microsoft_Windows_DSC_4180_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / Int32ul,
        "param2" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4181, version=0)
class Microsoft_Windows_DSC_4181_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4182, version=0)
class Microsoft_Windows_DSC_4182_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4183, version=0)
class Microsoft_Windows_DSC_4183_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "ParamNumber" / Int32ul,
        "ParamText" / WString,
        "ParamErrorCode" / Int32ul,
        "ParamErrorMessage" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4184, version=0)
class Microsoft_Windows_DSC_4184_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4185, version=0)
class Microsoft_Windows_DSC_4185_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4192, version=0)
class Microsoft_Windows_DSC_4192_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4193, version=0)
class Microsoft_Windows_DSC_4193_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4194, version=0)
class Microsoft_Windows_DSC_4194_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4195, version=0)
class Microsoft_Windows_DSC_4195_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4196, version=0)
class Microsoft_Windows_DSC_4196_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4197, version=0)
class Microsoft_Windows_DSC_4197_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4198, version=0)
class Microsoft_Windows_DSC_4198_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4199, version=0)
class Microsoft_Windows_DSC_4199_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4200, version=0)
class Microsoft_Windows_DSC_4200_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4201, version=0)
class Microsoft_Windows_DSC_4201_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4208, version=0)
class Microsoft_Windows_DSC_4208_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4209, version=0)
class Microsoft_Windows_DSC_4209_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4210, version=0)
class Microsoft_Windows_DSC_4210_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4211, version=0)
class Microsoft_Windows_DSC_4211_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4212, version=0)
class Microsoft_Windows_DSC_4212_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4213, version=0)
class Microsoft_Windows_DSC_4213_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4214, version=0)
class Microsoft_Windows_DSC_4214_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4215, version=0)
class Microsoft_Windows_DSC_4215_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4216, version=0)
class Microsoft_Windows_DSC_4216_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4217, version=0)
class Microsoft_Windows_DSC_4217_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4224, version=0)
class Microsoft_Windows_DSC_4224_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4225, version=0)
class Microsoft_Windows_DSC_4225_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4226, version=0)
class Microsoft_Windows_DSC_4226_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4227, version=0)
class Microsoft_Windows_DSC_4227_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4228, version=0)
class Microsoft_Windows_DSC_4228_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4229, version=0)
class Microsoft_Windows_DSC_4229_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4230, version=0)
class Microsoft_Windows_DSC_4230_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4231, version=0)
class Microsoft_Windows_DSC_4231_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4232, version=0)
class Microsoft_Windows_DSC_4232_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4233, version=0)
class Microsoft_Windows_DSC_4233_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4240, version=0)
class Microsoft_Windows_DSC_4240_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4241, version=0)
class Microsoft_Windows_DSC_4241_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4242, version=0)
class Microsoft_Windows_DSC_4242_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4243, version=0)
class Microsoft_Windows_DSC_4243_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4244, version=0)
class Microsoft_Windows_DSC_4244_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4245, version=0)
class Microsoft_Windows_DSC_4245_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4246, version=0)
class Microsoft_Windows_DSC_4246_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4247, version=0)
class Microsoft_Windows_DSC_4247_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4248, version=0)
class Microsoft_Windows_DSC_4248_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4249, version=0)
class Microsoft_Windows_DSC_4249_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "ClassName" / WString,
        "MessageBody" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4250, version=0)
class Microsoft_Windows_DSC_4250_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "Message" / WString,
        "HResult" / Int32sl,
        "StackTrace" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4251, version=0)
class Microsoft_Windows_DSC_4251_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "Operation" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4252, version=0)
class Microsoft_Windows_DSC_4252_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "MIResult" / Int32ul,
        "ErrorMessage" / WString,
        "MessageID" / WString,
        "ErrorCategory" / Int32ul,
        "ErrorCode" / Int32ul,
        "ErrorType" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4253, version=0)
class Microsoft_Windows_DSC_4253_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "WarningMessage" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4254, version=0)
class Microsoft_Windows_DSC_4254_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "DebugMessage" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4255, version=0)
class Microsoft_Windows_DSC_4255_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "activity" / WString,
        "currentOperation" / WString,
        "statusDescription" / WString,
        "percentComplete" / Int32ul,
        "secondsRemaining" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4256, version=0)
class Microsoft_Windows_DSC_4256_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "PromptMessage" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4257, version=0)
class Microsoft_Windows_DSC_4257_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "configurationMode" / WString,
        "configurationModeFrequencyMins" / Int32ul,
        "refreshmode" / WString,
        "refreshFrequencyMins" / Int32ul,
        "rebootNodeIfNeeded" / WString,
        "debugMode" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4258, version=0)
class Microsoft_Windows_DSC_4258_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4260, version=0)
class Microsoft_Windows_DSC_4260_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4261, version=0)
class Microsoft_Windows_DSC_4261_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4262, version=0)
class Microsoft_Windows_DSC_4262_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4263, version=0)
class Microsoft_Windows_DSC_4263_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4264, version=0)
class Microsoft_Windows_DSC_4264_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4265, version=0)
class Microsoft_Windows_DSC_4265_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "ReportManagerName" / WString,
        "ConfigurationId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4266, version=0)
class Microsoft_Windows_DSC_4266_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "ReportManagerName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4267, version=0)
class Microsoft_Windows_DSC_4267_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "PartialConfigurationName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4268, version=0)
class Microsoft_Windows_DSC_4268_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4269, version=0)
class Microsoft_Windows_DSC_4269_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "FileName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4274, version=0)
class Microsoft_Windows_DSC_4274_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4275, version=0)
class Microsoft_Windows_DSC_4275_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4276, version=0)
class Microsoft_Windows_DSC_4276_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4277, version=0)
class Microsoft_Windows_DSC_4277_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4278, version=0)
class Microsoft_Windows_DSC_4278_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4279, version=0)
class Microsoft_Windows_DSC_4279_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4280, version=0)
class Microsoft_Windows_DSC_4280_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4281, version=0)
class Microsoft_Windows_DSC_4281_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4282, version=0)
class Microsoft_Windows_DSC_4282_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "partialConfigName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4283, version=0)
class Microsoft_Windows_DSC_4283_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4284, version=0)
class Microsoft_Windows_DSC_4284_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4285, version=0)
class Microsoft_Windows_DSC_4285_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "exclusiveResource" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4286, version=0)
class Microsoft_Windows_DSC_4286_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4288, version=0)
class Microsoft_Windows_DSC_4288_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4289, version=0)
class Microsoft_Windows_DSC_4289_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4290, version=0)
class Microsoft_Windows_DSC_4290_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4291, version=0)
class Microsoft_Windows_DSC_4291_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4292, version=0)
class Microsoft_Windows_DSC_4292_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4293, version=0)
class Microsoft_Windows_DSC_4293_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4294, version=0)
class Microsoft_Windows_DSC_4294_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4295, version=0)
class Microsoft_Windows_DSC_4295_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4296, version=0)
class Microsoft_Windows_DSC_4296_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4297, version=0)
class Microsoft_Windows_DSC_4297_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4298, version=0)
class Microsoft_Windows_DSC_4298_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4299, version=0)
class Microsoft_Windows_DSC_4299_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4300, version=0)
class Microsoft_Windows_DSC_4300_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4301, version=0)
class Microsoft_Windows_DSC_4301_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4302, version=0)
class Microsoft_Windows_DSC_4302_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4303, version=0)
class Microsoft_Windows_DSC_4303_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4304, version=0)
class Microsoft_Windows_DSC_4304_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4305, version=0)
class Microsoft_Windows_DSC_4305_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "Name" / WString,
        "FullyQualifiedErrorId" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4306, version=0)
class Microsoft_Windows_DSC_4306_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "Name" / WString,
        "FullyQualifiedErrorId" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4307, version=0)
class Microsoft_Windows_DSC_4307_0(Etw):
    pattern = Struct(
        "ConsistencyTimerValue" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4308, version=0)
class Microsoft_Windows_DSC_4308_0(Etw):
    pattern = Struct(
        "RefreshTimerValue" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4309, version=0)
class Microsoft_Windows_DSC_4309_0(Etw):
    pattern = Struct(
        "ConsistencyTimerValue" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4310, version=0)
class Microsoft_Windows_DSC_4310_0(Etw):
    pattern = Struct(
        "RefreshTimerValue" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4312, version=0)
class Microsoft_Windows_DSC_4312_0(Etw):
    pattern = Struct(
        "flag" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4315, version=0)
class Microsoft_Windows_DSC_4315_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4316, version=0)
class Microsoft_Windows_DSC_4316_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4317, version=0)
class Microsoft_Windows_DSC_4317_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4318, version=0)
class Microsoft_Windows_DSC_4318_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4319, version=0)
class Microsoft_Windows_DSC_4319_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "PSModulePath" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4320, version=0)
class Microsoft_Windows_DSC_4320_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4321, version=0)
class Microsoft_Windows_DSC_4321_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "UserName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4322, version=0)
class Microsoft_Windows_DSC_4322_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "UserName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4323, version=0)
class Microsoft_Windows_DSC_4323_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "UserName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4324, version=0)
class Microsoft_Windows_DSC_4324_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4325, version=0)
class Microsoft_Windows_DSC_4325_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4326, version=0)
class Microsoft_Windows_DSC_4326_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4327, version=0)
class Microsoft_Windows_DSC_4327_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4328, version=0)
class Microsoft_Windows_DSC_4328_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4329, version=0)
class Microsoft_Windows_DSC_4329_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "AgentId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4332, version=0)
class Microsoft_Windows_DSC_4332_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "ResourceSequence" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4333, version=0)
class Microsoft_Windows_DSC_4333_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "DownloadManagerName" / WString,
        "AssignedConfigurationName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4334, version=0)
class Microsoft_Windows_DSC_4334_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "DownloadManagerName" / WString,
        "AgentId" / WString,
        "Modules" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4335, version=0)
class Microsoft_Windows_DSC_4335_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "clientChecksum" / WString,
        "checkSumFromServer" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4336, version=0)
class Microsoft_Windows_DSC_4336_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4337, version=0)
class Microsoft_Windows_DSC_4337_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "AgentId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4338, version=0)
class Microsoft_Windows_DSC_4338_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "requestId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4339, version=0)
class Microsoft_Windows_DSC_4339_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "header" / WString,
        "content" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4340, version=0)
class Microsoft_Windows_DSC_4340_0(Etw):
    pattern = Struct(
        "ReportingTimerValue" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4341, version=0)
class Microsoft_Windows_DSC_4341_0(Etw):
    pattern = Struct(
        "ConsistencyTimerValue" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4343, version=0)
class Microsoft_Windows_DSC_4343_0(Etw):
    pattern = Struct(
        "flag" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4344, version=0)
class Microsoft_Windows_DSC_4344_0(Etw):
    pattern = Struct(
        "flag" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4345, version=0)
class Microsoft_Windows_DSC_4345_0(Etw):
    pattern = Struct(
        "path" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4346, version=0)
class Microsoft_Windows_DSC_4346_0(Etw):
    pattern = Struct(
        "path" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4347, version=0)
class Microsoft_Windows_DSC_4347_0(Etw):
    pattern = Struct(
        "path" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4348, version=0)
class Microsoft_Windows_DSC_4348_0(Etw):
    pattern = Struct(
        "resourceName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4349, version=0)
class Microsoft_Windows_DSC_4349_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4350, version=0)
class Microsoft_Windows_DSC_4350_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4351, version=0)
class Microsoft_Windows_DSC_4351_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4352, version=0)
class Microsoft_Windows_DSC_4352_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4353, version=0)
class Microsoft_Windows_DSC_4353_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4401, version=0)
class Microsoft_Windows_DSC_4401_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "AgentId" / WString,
        "server" / WString,
        "DownloadManagerName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4402, version=0)
class Microsoft_Windows_DSC_4402_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "AgentId" / WString,
        "server" / WString,
        "DownloadManagerName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4403, version=0)
class Microsoft_Windows_DSC_4403_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "AgentId" / WString,
        "put" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4404, version=0)
class Microsoft_Windows_DSC_4404_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "AgentId" / WString,
        "error" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4405, version=0)
class Microsoft_Windows_DSC_4405_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "AgentId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4406, version=0)
class Microsoft_Windows_DSC_4406_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "AgentId" / WString,
        "CertId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4407, version=0)
class Microsoft_Windows_DSC_4407_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4408, version=0)
class Microsoft_Windows_DSC_4408_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "AgentId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4409, version=0)
class Microsoft_Windows_DSC_4409_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "AgentId" / WString,
        "Server" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4410, version=0)
class Microsoft_Windows_DSC_4410_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4411, version=0)
class Microsoft_Windows_DSC_4411_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "AgentId" / WString,
        "Server" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4412, version=0)
class Microsoft_Windows_DSC_4412_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "AgentId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4413, version=0)
class Microsoft_Windows_DSC_4413_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "AgentId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4501, version=0)
class Microsoft_Windows_DSC_4501_0(Etw):
    pattern = Struct(
        "assemblyName" / WString,
        "loadExceptionMessage" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4502, version=0)
class Microsoft_Windows_DSC_4502_0(Etw):
    pattern = Struct(
        "typeName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4503, version=0)
class Microsoft_Windows_DSC_4503_0(Etw):
    pattern = Struct(
        "exceptionMessage" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4504, version=0)
class Microsoft_Windows_DSC_4504_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4505, version=0)
class Microsoft_Windows_DSC_4505_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4506, version=0)
class Microsoft_Windows_DSC_4506_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4507, version=0)
class Microsoft_Windows_DSC_4507_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4508, version=0)
class Microsoft_Windows_DSC_4508_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "ReportManagerName" / WString,
        "ConfigurationId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4509, version=0)
class Microsoft_Windows_DSC_4509_0(Etw):
    pattern = Struct(
        "JobId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4510, version=0)
class Microsoft_Windows_DSC_4510_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "errorno" / Int32ul,
        "logName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4511, version=0)
class Microsoft_Windows_DSC_4511_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "errorno" / Int32ul,
        "logName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4512, version=0)
class Microsoft_Windows_DSC_4512_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "logName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4513, version=0)
class Microsoft_Windows_DSC_4513_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "logName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4514, version=0)
class Microsoft_Windows_DSC_4514_0(Etw):
    pattern = Struct(
        "signatureStatus" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4515, version=0)
class Microsoft_Windows_DSC_4515_0(Etw):
    pattern = Struct(
        "message" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4516, version=0)
class Microsoft_Windows_DSC_4516_0(Etw):
    pattern = Struct(
        "message" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4517, version=0)
class Microsoft_Windows_DSC_4517_0(Etw):
    pattern = Struct(
        "message" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4518, version=0)
class Microsoft_Windows_DSC_4518_0(Etw):
    pattern = Struct(
        "storeInfo" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4521, version=0)
class Microsoft_Windows_DSC_4521_0(Etw):
    pattern = Struct(
        "signatureStatus" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4522, version=0)
class Microsoft_Windows_DSC_4522_0(Etw):
    pattern = Struct(
        "signatureStatus" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4523, version=0)
class Microsoft_Windows_DSC_4523_0(Etw):
    pattern = Struct(
        "signatureStatus" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4524, version=0)
class Microsoft_Windows_DSC_4524_0(Etw):
    pattern = Struct(
        "currentMachinSignatureVerificationPolicy" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4525, version=0)
class Microsoft_Windows_DSC_4525_0(Etw):
    pattern = Struct(
        "zipFileName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4526, version=0)
class Microsoft_Windows_DSC_4526_0(Etw):
    pattern = Struct(
        "zipFileName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4527, version=0)
class Microsoft_Windows_DSC_4527_0(Etw):
    pattern = Struct(
        "zipFileName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4528, version=0)
class Microsoft_Windows_DSC_4528_0(Etw):
    pattern = Struct(
        "moduleName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4529, version=0)
class Microsoft_Windows_DSC_4529_0(Etw):
    pattern = Struct(
        "zipFileName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4530, version=0)
class Microsoft_Windows_DSC_4530_0(Etw):
    pattern = Struct(
        "assignedConfigName" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4531, version=0)
class Microsoft_Windows_DSC_4531_0(Etw):
    pattern = Struct(
        "zipFile" / WString,
        "limit" / Int32ul
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4601, version=0)
class Microsoft_Windows_DSC_4601_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "AgentId" / WString,
        "error" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4602, version=0)
class Microsoft_Windows_DSC_4602_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "AgentId" / WString,
        "put" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4603, version=0)
class Microsoft_Windows_DSC_4603_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "AgentId" / WString,
        "HeaderValue" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4604, version=0)
class Microsoft_Windows_DSC_4604_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "AgentId" / WString
    )


@declare(guid=guid("50df9e12-a8c4-4939-b281-47e1325ba63e"), event_id=4605, version=0)
class Microsoft_Windows_DSC_4605_0(Etw):
    pattern = Struct(
        "JobId" / WString,
        "AgentId" / WString,
        "CertId" / WString
    )

