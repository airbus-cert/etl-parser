# -*- coding: utf-8 -*-
"""
Microsoft-Windows-PowerShell
GUID : a0c1853b-5c40-4b15-8766-3cf1c58f985a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=4100, version=1)
class Microsoft_Windows_PowerShell_4100_1(Etw):
    pattern = Struct(
        "ContextInfo" / WString,
        "UserData" / WString,
        "Payload" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=4101, version=1)
class Microsoft_Windows_PowerShell_4101_1(Etw):
    pattern = Struct(
        "ContextInfo" / WString,
        "UserData" / WString,
        "Payload" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=4102, version=1)
class Microsoft_Windows_PowerShell_4102_1(Etw):
    pattern = Struct(
        "ContextInfo" / WString,
        "UserData" / WString,
        "Payload" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=4103, version=1)
class Microsoft_Windows_PowerShell_4103_1(Etw):
    pattern = Struct(
        "ContextInfo" / WString,
        "UserData" / WString,
        "Payload" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=4104, version=1)
class Microsoft_Windows_PowerShell_4104_1(Etw):
    pattern = Struct(
        "MessageNumber" / Int32sl,
        "MessageTotal" / Int32sl,
        "ScriptBlockText" / WString,
        "ScriptBlockId" / WString,
        "Path" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=4105, version=1)
class Microsoft_Windows_PowerShell_4105_1(Etw):
    pattern = Struct(
        "ScriptBlockId" / WString,
        "RunspaceId" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=4106, version=1)
class Microsoft_Windows_PowerShell_4106_1(Etw):
    pattern = Struct(
        "ScriptBlockId" / WString,
        "RunspaceId" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=7937, version=1)
class Microsoft_Windows_PowerShell_7937_1(Etw):
    pattern = Struct(
        "ContextInfo" / WString,
        "UserData" / WString,
        "Payload" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=7938, version=1)
class Microsoft_Windows_PowerShell_7938_1(Etw):
    pattern = Struct(
        "ContextInfo" / WString,
        "UserData" / WString,
        "Payload" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=7939, version=1)
class Microsoft_Windows_PowerShell_7939_1(Etw):
    pattern = Struct(
        "ContextInfo" / WString,
        "UserData" / WString,
        "Payload" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=7940, version=1)
class Microsoft_Windows_PowerShell_7940_1(Etw):
    pattern = Struct(
        "ContextInfo" / WString,
        "UserData" / WString,
        "Payload" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=7941, version=1)
class Microsoft_Windows_PowerShell_7941_1(Etw):
    pattern = Struct(
        "currentActivityId" / Guid,
        "parentActivityId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=7942, version=1)
class Microsoft_Windows_PowerShell_7942_1(Etw):
    pattern = Struct(
        "ClassName" / WString,
        "MethodName" / WString,
        "WorkflowGuid" / WString,
        "Message" / WString,
        "JobData" / WString,
        "ActivityName" / WString,
        "ActivityGuid" / WString,
        "Parameters" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=8193, version=1)
class Microsoft_Windows_PowerShell_8193_1(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=8194, version=1)
class Microsoft_Windows_PowerShell_8194_1(Etw):
    pattern = Struct(
        "InstanceId" / WString,
        "MaxRunspaces" / WString,
        "MinRunspaces" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=8197, version=1)
class Microsoft_Windows_PowerShell_8197_1(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=8198, version=1)
class Microsoft_Windows_PowerShell_8198_1(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=12033, version=1)
class Microsoft_Windows_PowerShell_12033_1(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=12034, version=1)
class Microsoft_Windows_PowerShell_12034_1(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=12035, version=1)
class Microsoft_Windows_PowerShell_12035_1(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=12036, version=1)
class Microsoft_Windows_PowerShell_12036_1(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=12038, version=1)
class Microsoft_Windows_PowerShell_12038_1(Etw):
    pattern = Struct(
        "uri" / WString,
        "shell" / WString,
        "userName" / WString,
        "opentimeout" / WString,
        "idletimeout" / WString,
        "canceltimeout" / WString,
        "auth" / Int32ul,
        "thumbPrint" / WString,
        "redircount" / WString,
        "recvdDataSize" / WString,
        "recvdObjSize" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=24577, version=1)
class Microsoft_Windows_PowerShell_24577_1(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=24578, version=1)
class Microsoft_Windows_PowerShell_24578_1(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=24595, version=1)
class Microsoft_Windows_PowerShell_24595_1(Etw):
    pattern = Struct(
        "CurrentLine" / Int32sl,
        "FileName" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=24596, version=1)
class Microsoft_Windows_PowerShell_24596_1(Etw):
    pattern = Struct(
        "CurrentLine" / Int32sl,
        "FileName" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=24597, version=1)
class Microsoft_Windows_PowerShell_24597_1(Etw):
    pattern = Struct(
        "CurrentLine" / Int32sl,
        "FileName" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=24598, version=1)
class Microsoft_Windows_PowerShell_24598_1(Etw):
    pattern = Struct(
        "CurrentLine" / Int32sl,
        "FileName" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=24599, version=1)
class Microsoft_Windows_PowerShell_24599_1(Etw):
    pattern = Struct(
        "CurrentLine" / Int32sl,
        "FileName" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=28673, version=1)
class Microsoft_Windows_PowerShell_28673_1(Etw):
    pattern = Struct(
        "DeserializedType" / WString,
        "CastedToType" / WString,
        "RehydratedType" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=28674, version=1)
class Microsoft_Windows_PowerShell_28674_1(Etw):
    pattern = Struct(
        "DeserializedType" / WString,
        "CastedToType" / WString,
        "TypeCastException" / WString,
        "TypeCastInnerException" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=28675, version=1)
class Microsoft_Windows_PowerShell_28675_1(Etw):
    pattern = Struct(
        "SerializedType" / WString,
        "OriginalDepth" / Int32sl,
        "OverridenDepth" / Int32sl,
        "CurrentDepthBelowTopLevel" / Int32sl
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=28676, version=1)
class Microsoft_Windows_PowerShell_28676_1(Etw):
    pattern = Struct(
        "SerializedType" / WString,
        "OverridenMode" / Int32ul
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=28677, version=1)
class Microsoft_Windows_PowerShell_28677_1(Etw):
    pattern = Struct(
        "PropertyName" / WString,
        "PropertyOwnerType" / WString,
        "GetterScript" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=28678, version=1)
class Microsoft_Windows_PowerShell_28678_1(Etw):
    pattern = Struct(
        "PropertyName" / WString,
        "PropertyOwnerType" / WString,
        "Exception" / WString,
        "InnerException" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=28679, version=1)
class Microsoft_Windows_PowerShell_28679_1(Etw):
    pattern = Struct(
        "TypeBeingEnumerated" / WString,
        "Exception" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=28680, version=1)
class Microsoft_Windows_PowerShell_28680_1(Etw):
    pattern = Struct(
        "Type" / WString,
        "Exception" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=28682, version=1)
class Microsoft_Windows_PowerShell_28682_1(Etw):
    pattern = Struct(
        "TypeOfObjectAtMaxDepth" / WString,
        "PropertyNameAtMaxDepth" / WString,
        "Depth" / Int32sl
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=28683, version=1)
class Microsoft_Windows_PowerShell_28683_1(Etw):
    pattern = Struct(
        "LineNumber" / Int32sl,
        "LinePosition" / Int32sl,
        "Exception" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=28684, version=1)
class Microsoft_Windows_PowerShell_28684_1(Etw):
    pattern = Struct(
        "TypeOfObjectWithMissingProperty" / WString,
        "PropertyName" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32769, version=1)
class Microsoft_Windows_PowerShell_32769_1(Etw):
    pattern = Struct(
        "Runspace_InstanceId" / WString,
        "PowerShell_InstanceId" / WString,
        "Destination" / Int32ul,
        "DataType" / Int32ul,
        "TargetInterface" / Int32ul
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32775, version=1)
class Microsoft_Windows_PowerShell_32775_1(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32776, version=1)
class Microsoft_Windows_PowerShell_32776_1(Etw):
    pattern = Struct(
        "SessionId" / WString,
        "PipelineId" / WString,
        "ErrorCode" / WString,
        "ErrorMessage" / WString,
        "StackTrace" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32777, version=1)
class Microsoft_Windows_PowerShell_32777_1(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32784, version=1)
class Microsoft_Windows_PowerShell_32784_1(Etw):
    pattern = Struct(
        "SessionId" / WString,
        "PipelineId" / WString,
        "ErrorCode" / WString,
        "ErrorMessage" / WString,
        "StackTrace" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32785, version=1)
class Microsoft_Windows_PowerShell_32785_1(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32786, version=1)
class Microsoft_Windows_PowerShell_32786_1(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32787, version=1)
class Microsoft_Windows_PowerShell_32787_1(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32788, version=1)
class Microsoft_Windows_PowerShell_32788_1(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32789, version=1)
class Microsoft_Windows_PowerShell_32789_1(Etw):
    pattern = Struct(
        "SessionId" / WString,
        "PipelineId" / WString,
        "DataSize" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32790, version=1)
class Microsoft_Windows_PowerShell_32790_1(Etw):
    pattern = Struct(
        "SessionId" / WString,
        "PipelineId" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32791, version=1)
class Microsoft_Windows_PowerShell_32791_1(Etw):
    pattern = Struct(
        "SessionId" / WString,
        "PipelineId" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32792, version=1)
class Microsoft_Windows_PowerShell_32792_1(Etw):
    pattern = Struct(
        "SessionId" / WString,
        "PipelineId" / WString,
        "DataSize" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32793, version=1)
class Microsoft_Windows_PowerShell_32793_1(Etw):
    pattern = Struct(
        "SessionId" / WString,
        "PipelineId" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32800, version=1)
class Microsoft_Windows_PowerShell_32800_1(Etw):
    pattern = Struct(
        "SessionId" / WString,
        "PipelineId" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32801, version=1)
class Microsoft_Windows_PowerShell_32801_1(Etw):
    pattern = Struct(
        "SessionId" / WString,
        "PipelineId" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32802, version=1)
class Microsoft_Windows_PowerShell_32802_1(Etw):
    pattern = Struct(
        "SessionId" / WString,
        "PipelineId" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32803, version=1)
class Microsoft_Windows_PowerShell_32803_1(Etw):
    pattern = Struct(
        "SessionId" / WString,
        "PipelineId" / WString,
        "SignalCode" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32804, version=1)
class Microsoft_Windows_PowerShell_32804_1(Etw):
    pattern = Struct(
        "SessionId" / WString,
        "PipelineId" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32805, version=1)
class Microsoft_Windows_PowerShell_32805_1(Etw):
    pattern = Struct(
        "SessionId" / WString,
        "Uri" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32849, version=1)
class Microsoft_Windows_PowerShell_32849_1(Etw):
    pattern = Struct(
        "Runspace_InstanceId" / WString,
        "PowerShell_InstanceId" / WString,
        "DataSize" / WString,
        "DataType" / Int32ul,
        "TargetInterface" / Int32ul
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32850, version=1)
class Microsoft_Windows_PowerShell_32850_1(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32851, version=1)
class Microsoft_Windows_PowerShell_32851_1(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32852, version=1)
class Microsoft_Windows_PowerShell_32852_1(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32853, version=1)
class Microsoft_Windows_PowerShell_32853_1(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32854, version=1)
class Microsoft_Windows_PowerShell_32854_1(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32855, version=1)
class Microsoft_Windows_PowerShell_32855_1(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32856, version=1)
class Microsoft_Windows_PowerShell_32856_1(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32857, version=1)
class Microsoft_Windows_PowerShell_32857_1(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32865, version=1)
class Microsoft_Windows_PowerShell_32865_1(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32866, version=1)
class Microsoft_Windows_PowerShell_32866_1(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32867, version=1)
class Microsoft_Windows_PowerShell_32867_1(Etw):
    pattern = Struct(
        "ObjectId" / Int64sl,
        "FragmentId" / Int64sl,
        "sFlag" / Int32sl,
        "eFlag" / Int32sl,
        "FragmentLength" / Int32ul,
        "FragmentPayload" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=32868, version=1)
class Microsoft_Windows_PowerShell_32868_1(Etw):
    pattern = Struct(
        "ObjectId" / Int64sl,
        "FragmentId" / Int64sl,
        "sFlag" / Int32sl,
        "eFlag" / Int32sl,
        "FragmentLength" / Int32ul,
        "FragmentPayload" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45057, version=1)
class Microsoft_Windows_PowerShell_45057_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "Category" / WString,
        "Reason" / WString,
        "TargetName" / WString,
        "FullyQualifiedErrorId" / WString,
        "ExceptionMessage" / WString,
        "ExceptionStackTrace" / WString,
        "ExceptionInnerException" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45058, version=1)
class Microsoft_Windows_PowerShell_45058_1(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45060, version=1)
class Microsoft_Windows_PowerShell_45060_1(Etw):
    pattern = Struct(
        "Id" / WString,
        "InstanceId" / WString,
        "Name" / WString,
        "Location" / WString,
        "State" / WString,
        "Command" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45061, version=1)
class Microsoft_Windows_PowerShell_45061_1(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45062, version=1)
class Microsoft_Windows_PowerShell_45062_1(Etw):
    pattern = Struct(
        "uri" / WString,
        "shell" / WString,
        "userName" / WString,
        "opentimeout" / WString,
        "idletimeout" / WString,
        "canceltimeout" / WString,
        "auth" / Int32ul,
        "thumbPrint" / WString,
        "redircount" / WString,
        "recvdDataSize" / WString,
        "recvdObjSize" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45063, version=1)
class Microsoft_Windows_PowerShell_45063_1(Etw):
    pattern = Struct(
        "endpointName" / WString,
        "user" / WString,
        "hostingMode" / WString,
        "protocol" / WString,
        "configuration" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45064, version=1)
class Microsoft_Windows_PowerShell_45064_1(Etw):
    pattern = Struct(
        "workflowId" / Guid,
        "managedNodes" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45065, version=1)
class Microsoft_Windows_PowerShell_45065_1(Etw):
    pattern = Struct(
        "workflowId" / Guid,
        "newState" / WString,
        "oldState" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45072, version=1)
class Microsoft_Windows_PowerShell_45072_1(Etw):
    pattern = Struct(
        "endpointName" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45073, version=1)
class Microsoft_Windows_PowerShell_45073_1(Etw):
    pattern = Struct(
        "endpointName" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45074, version=1)
class Microsoft_Windows_PowerShell_45074_1(Etw):
    pattern = Struct(
        "workflowId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45075, version=1)
class Microsoft_Windows_PowerShell_45075_1(Etw):
    pattern = Struct(
        "endpointName" / WString,
        "configName" / WString,
        "allowedValue" / WString,
        "valueInQuestion" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45076, version=1)
class Microsoft_Windows_PowerShell_45076_1(Etw):
    pattern = Struct(
        "workflowId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45078, version=1)
class Microsoft_Windows_PowerShell_45078_1(Etw):
    pattern = Struct(
        "workflowId" / Guid,
        "managedNode" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45079, version=1)
class Microsoft_Windows_PowerShell_45079_1(Etw):
    pattern = Struct(
        "workflowId" / Guid,
        "activityName" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45080, version=1)
class Microsoft_Windows_PowerShell_45080_1(Etw):
    pattern = Struct(
        "activityName" / WString,
        "activityTypeName" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45081, version=1)
class Microsoft_Windows_PowerShell_45081_1(Etw):
    pattern = Struct(
        "workflowId" / Guid,
        "xamlFile" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45082, version=1)
class Microsoft_Windows_PowerShell_45082_1(Etw):
    pattern = Struct(
        "workflowId" / Guid,
        "xamlFile" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45083, version=1)
class Microsoft_Windows_PowerShell_45083_1(Etw):
    pattern = Struct(
        "workflowId" / Guid,
        "errorDescription" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45084, version=1)
class Microsoft_Windows_PowerShell_45084_1(Etw):
    pattern = Struct(
        "workflowId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45085, version=1)
class Microsoft_Windows_PowerShell_45085_1(Etw):
    pattern = Struct(
        "workflowId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45086, version=1)
class Microsoft_Windows_PowerShell_45086_1(Etw):
    pattern = Struct(
        "workflowId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45087, version=1)
class Microsoft_Windows_PowerShell_45087_1(Etw):
    pattern = Struct(
        "workflowId" / Guid,
        "activityDisplayName" / WString,
        "activityType" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45088, version=1)
class Microsoft_Windows_PowerShell_45088_1(Etw):
    pattern = Struct(
        "workflowId" / Guid,
        "activityDisplayName" / WString,
        "activityType" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45089, version=1)
class Microsoft_Windows_PowerShell_45089_1(Etw):
    pattern = Struct(
        "workflowId" / Guid,
        "activityName" / WString,
        "failureDescription" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45090, version=1)
class Microsoft_Windows_PowerShell_45090_1(Etw):
    pattern = Struct(
        "runspaceId" / WString,
        "availability" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45091, version=1)
class Microsoft_Windows_PowerShell_45091_1(Etw):
    pattern = Struct(
        "runspaceId" / WString,
        "newState" / WString,
        "oldState" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45092, version=1)
class Microsoft_Windows_PowerShell_45092_1(Etw):
    pattern = Struct(
        "workflowId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45093, version=1)
class Microsoft_Windows_PowerShell_45093_1(Etw):
    pattern = Struct(
        "workflowId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45094, version=1)
class Microsoft_Windows_PowerShell_45094_1(Etw):
    pattern = Struct(
        "workflowId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45095, version=1)
class Microsoft_Windows_PowerShell_45095_1(Etw):
    pattern = Struct(
        "workflowId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45096, version=1)
class Microsoft_Windows_PowerShell_45096_1(Etw):
    pattern = Struct(
        "workflowId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45097, version=1)
class Microsoft_Windows_PowerShell_45097_1(Etw):
    pattern = Struct(
        "workflowId" / Guid,
        "path" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45098, version=1)
class Microsoft_Windows_PowerShell_45098_1(Etw):
    pattern = Struct(
        "workflowId" / Guid,
        "path" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45100, version=1)
class Microsoft_Windows_PowerShell_45100_1(Etw):
    pattern = Struct(
        "jobId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45101, version=1)
class Microsoft_Windows_PowerShell_45101_1(Etw):
    pattern = Struct(
        "jobId" / Int32sl,
        "workflowId" / Guid,
        "newState" / WString,
        "oldState" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45102, version=1)
class Microsoft_Windows_PowerShell_45102_1(Etw):
    pattern = Struct(
        "jobId" / Int32sl,
        "workflowId" / Guid,
        "errorDescription" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45104, version=1)
class Microsoft_Windows_PowerShell_45104_1(Etw):
    pattern = Struct(
        "parentJobId" / Guid,
        "childJobId" / Guid,
        "childWorkflowId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45105, version=1)
class Microsoft_Windows_PowerShell_45105_1(Etw):
    pattern = Struct(
        "jobId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45106, version=1)
class Microsoft_Windows_PowerShell_45106_1(Etw):
    pattern = Struct(
        "jobId" / Guid,
        "workflowId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45107, version=1)
class Microsoft_Windows_PowerShell_45107_1(Etw):
    pattern = Struct(
        "parentJobId" / Guid,
        "childJobId" / Guid,
        "workflowId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45108, version=1)
class Microsoft_Windows_PowerShell_45108_1(Etw):
    pattern = Struct(
        "parentJobId" / Guid,
        "childJobId" / Guid,
        "workflowId" / Guid,
        "error" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45109, version=1)
class Microsoft_Windows_PowerShell_45109_1(Etw):
    pattern = Struct(
        "workflowId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45110, version=1)
class Microsoft_Windows_PowerShell_45110_1(Etw):
    pattern = Struct(
        "workflowId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45111, version=1)
class Microsoft_Windows_PowerShell_45111_1(Etw):
    pattern = Struct(
        "workflowId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45112, version=1)
class Microsoft_Windows_PowerShell_45112_1(Etw):
    pattern = Struct(
        "workflowId" / Guid,
        "reason" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45113, version=1)
class Microsoft_Windows_PowerShell_45113_1(Etw):
    pattern = Struct(
        "workflowId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45114, version=1)
class Microsoft_Windows_PowerShell_45114_1(Etw):
    pattern = Struct(
        "workflowId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45115, version=1)
class Microsoft_Windows_PowerShell_45115_1(Etw):
    pattern = Struct(
        "workflowId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45116, version=1)
class Microsoft_Windows_PowerShell_45116_1(Etw):
    pattern = Struct(
        "workflowId" / Guid,
        "errorDescription" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45117, version=1)
class Microsoft_Windows_PowerShell_45117_1(Etw):
    pattern = Struct(
        "workflowId" / Guid,
        "persistPath" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45118, version=1)
class Microsoft_Windows_PowerShell_45118_1(Etw):
    pattern = Struct(
        "workflowId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45119, version=1)
class Microsoft_Windows_PowerShell_45119_1(Etw):
    pattern = Struct(
        "activityName" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45120, version=1)
class Microsoft_Windows_PowerShell_45120_1(Etw):
    pattern = Struct(
        "workflowId" / Guid,
        "errorDescription" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45121, version=1)
class Microsoft_Windows_PowerShell_45121_1(Etw):
    pattern = Struct(
        "endpointName" / WString,
        "endpointType" / WString,
        "registeredBy" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45122, version=1)
class Microsoft_Windows_PowerShell_45122_1(Etw):
    pattern = Struct(
        "endpointName" / WString,
        "modifiedBy" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45123, version=1)
class Microsoft_Windows_PowerShell_45123_1(Etw):
    pattern = Struct(
        "endpointName" / WString,
        "unregisteredBy" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45124, version=1)
class Microsoft_Windows_PowerShell_45124_1(Etw):
    pattern = Struct(
        "endpointName" / WString,
        "disabledBy" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45125, version=1)
class Microsoft_Windows_PowerShell_45125_1(Etw):
    pattern = Struct(
        "endpointName" / WString,
        "enabledBy" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45126, version=1)
class Microsoft_Windows_PowerShell_45126_1(Etw):
    pattern = Struct(
        "command" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45127, version=1)
class Microsoft_Windows_PowerShell_45127_1(Etw):
    pattern = Struct(
        "parameters" / WString,
        "computers" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45128, version=1)
class Microsoft_Windows_PowerShell_45128_1(Etw):
    pattern = Struct(
        "endpointName" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=45129, version=1)
class Microsoft_Windows_PowerShell_45129_1(Etw):
    pattern = Struct(
        "checkpointPath" / WString,
        "configProviderId" / WString,
        "userName" / WString,
        "path" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=46337, version=1)
class Microsoft_Windows_PowerShell_46337_1(Etw):
    pattern = Struct(
        "TrackingId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=46338, version=1)
class Microsoft_Windows_PowerShell_46338_1(Etw):
    pattern = Struct(
        "TrackingId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=46339, version=1)
class Microsoft_Windows_PowerShell_46339_1(Etw):
    pattern = Struct(
        "TrackingId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=46340, version=1)
class Microsoft_Windows_PowerShell_46340_1(Etw):
    pattern = Struct(
        "TrackingId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=46341, version=1)
class Microsoft_Windows_PowerShell_46341_1(Etw):
    pattern = Struct(
        "TrackingId" / Guid,
        "ContainerParentJobInstanceId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=46342, version=1)
class Microsoft_Windows_PowerShell_46342_1(Etw):
    pattern = Struct(
        "WorkflowJobJobInstanceId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=46343, version=1)
class Microsoft_Windows_PowerShell_46343_1(Etw):
    pattern = Struct(
        "WorkflowJobJobInstanceId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=46344, version=1)
class Microsoft_Windows_PowerShell_46344_1(Etw):
    pattern = Struct(
        "WorkflowJobJobInstanceId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=46345, version=1)
class Microsoft_Windows_PowerShell_46345_1(Etw):
    pattern = Struct(
        "WorkflowJobJobInstanceId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=46346, version=1)
class Microsoft_Windows_PowerShell_46346_1(Etw):
    pattern = Struct(
        "WorkflowJobInstanceId" / Guid,
        "ContainerParentJobInstanceId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=46347, version=1)
class Microsoft_Windows_PowerShell_46347_1(Etw):
    pattern = Struct(
        "ProxyJobInstanceId" / Guid,
        "ContainerParentJobInstanceId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=46348, version=1)
class Microsoft_Windows_PowerShell_46348_1(Etw):
    pattern = Struct(
        "ContainerParentJobInstanceId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=46349, version=1)
class Microsoft_Windows_PowerShell_46349_1(Etw):
    pattern = Struct(
        "ContainerParentJobInstanceId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=46350, version=1)
class Microsoft_Windows_PowerShell_46350_1(Etw):
    pattern = Struct(
        "ProxyJobInstanceId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=46351, version=1)
class Microsoft_Windows_PowerShell_46351_1(Etw):
    pattern = Struct(
        "ProxyJobInstanceId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=46352, version=1)
class Microsoft_Windows_PowerShell_46352_1(Etw):
    pattern = Struct(
        "ProxyJobInstanceId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=46353, version=1)
class Microsoft_Windows_PowerShell_46353_1(Etw):
    pattern = Struct(
        "ProxyJobInstanceId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=46354, version=1)
class Microsoft_Windows_PowerShell_46354_1(Etw):
    pattern = Struct(
        "ProxyChildJobInstanceId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=46355, version=1)
class Microsoft_Windows_PowerShell_46355_1(Etw):
    pattern = Struct(
        "ProxyChildJobInstanceId" / Guid
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=49152, version=1)
class Microsoft_Windows_PowerShell_49152_1(Etw):
    pattern = Struct(
        "message" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=49153, version=1)
class Microsoft_Windows_PowerShell_49153_1(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=53249, version=1)
class Microsoft_Windows_PowerShell_53249_1(Etw):
    pattern = Struct(
        "ScheduledJobDefName" / WString,
        "StartTime" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=53250, version=1)
class Microsoft_Windows_PowerShell_53250_1(Etw):
    pattern = Struct(
        "ScheduledJobDefName" / WString,
        "StopTime" / WString,
        "State" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=53251, version=1)
class Microsoft_Windows_PowerShell_53251_1(Etw):
    pattern = Struct(
        "Name" / WString,
        "Message" / WString,
        "StackTrace" / WString,
        "InnerException" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=53504, version=1)
class Microsoft_Windows_PowerShell_53504_1(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=53505, version=1)
class Microsoft_Windows_PowerShell_53505_1(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=53506, version=1)
class Microsoft_Windows_PowerShell_53506_1(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=53507, version=1)
class Microsoft_Windows_PowerShell_53507_1(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("a0c1853b-5c40-4b15-8766-3cf1c58f985a"), event_id=53508, version=1)
class Microsoft_Windows_PowerShell_53508_1(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )

