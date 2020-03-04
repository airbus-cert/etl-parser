# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Application Server-Applications
GUID : c651f5f6-1c0d-492e-8ae1-b4efd7c9d503
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=100, version=0)
class Microsoft_Windows_Application_Server_Applications_100_0(Etw):
    pattern = Struct(
        "InstanceId" / Guid,
        "RecordNumber" / Int64sl,
        "EventTime" / Int64ul,
        "ActivityDefinitionId" / WString,
        "State" / WString,
        "Annotations" / WString,
        "ProfileName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=101, version=0)
class Microsoft_Windows_Application_Server_Applications_101_0(Etw):
    pattern = Struct(
        "InstanceId" / Guid,
        "RecordNumber" / Int64sl,
        "EventTime" / Int64ul,
        "ActivityDefinitionId" / WString,
        "SourceName" / WString,
        "SourceId" / WString,
        "SourceInstanceId" / WString,
        "SourceTypeName" / WString,
        "Exception" / WString,
        "Annotations" / WString,
        "ProfileName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=102, version=0)
class Microsoft_Windows_Application_Server_Applications_102_0(Etw):
    pattern = Struct(
        "InstanceId" / Guid,
        "RecordNumber" / Int64sl,
        "EventTime" / Int64ul,
        "ActivityDefinitionId" / WString,
        "Reason" / WString,
        "Annotations" / WString,
        "ProfileName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=103, version=0)
class Microsoft_Windows_Application_Server_Applications_103_0(Etw):
    pattern = Struct(
        "InstanceId" / Guid,
        "RecordNumber" / Int64sl,
        "EventTime" / Int64ul,
        "State" / WString,
        "Name" / WString,
        "ActivityId" / WString,
        "ActivityInstanceId" / WString,
        "ActivityTypeName" / WString,
        "Arguments" / WString,
        "Variables" / WString,
        "Annotations" / WString,
        "ProfileName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=104, version=0)
class Microsoft_Windows_Application_Server_Applications_104_0(Etw):
    pattern = Struct(
        "InstanceId" / Guid,
        "RecordNumber" / Int64sl,
        "EventTime" / Int64ul,
        "Name" / WString,
        "ActivityId" / WString,
        "ActivityInstanceId" / WString,
        "ActivityTypeName" / WString,
        "ChildActivityName" / WString,
        "ChildActivityId" / WString,
        "ChildActivityInstanceId" / WString,
        "ChildActivityTypeName" / WString,
        "Annotations" / WString,
        "ProfileName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=105, version=0)
class Microsoft_Windows_Application_Server_Applications_105_0(Etw):
    pattern = Struct(
        "InstanceId" / Guid,
        "RecordNumber" / Int64sl,
        "EventTime" / Int64ul,
        "FaultSourceActivityName" / WString,
        "FaultSourceActivityId" / WString,
        "FaultSourceActivityInstanceId" / WString,
        "FaultSourceActivityTypeName" / WString,
        "FaultHandlerActivityName" / WString,
        "FaultHandlerActivityId" / WString,
        "FaultHandlerActivityInstanceId" / WString,
        "FaultHandlerActivityTypeName" / WString,
        "Fault" / WString,
        "IsFaultSource" / Int8ul,
        "Annotations" / WString,
        "ProfileName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=106, version=0)
class Microsoft_Windows_Application_Server_Applications_106_0(Etw):
    pattern = Struct(
        "InstanceId" / Guid,
        "RecordNumber" / Int64sl,
        "EventTime" / Int64ul,
        "Name" / WString,
        "ActivityId" / WString,
        "ActivityInstanceId" / WString,
        "ActivityTypeName" / WString,
        "ChildActivityName" / WString,
        "ChildActivityId" / WString,
        "ChildActivityInstanceId" / WString,
        "ChildActivityTypeName" / WString,
        "Annotations" / WString,
        "ProfileName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=107, version=0)
class Microsoft_Windows_Application_Server_Applications_107_0(Etw):
    pattern = Struct(
        "InstanceId" / Guid,
        "RecordNumber" / Int64sl,
        "EventTime" / Int64ul,
        "Name" / WString,
        "SubInstanceID" / Guid,
        "OwnerActivityName" / WString,
        "OwnerActivityId" / WString,
        "OwnerActivityInstanceId" / WString,
        "OwnerActivityTypeName" / WString,
        "Annotations" / WString,
        "ProfileName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=108, version=0)
class Microsoft_Windows_Application_Server_Applications_108_0(Etw):
    pattern = Struct(
        "InstanceId" / Guid,
        "RecordNumber" / Int64sl,
        "EventTime" / Int64ul,
        "Name" / WString,
        "ActivityName" / WString,
        "ActivityId" / WString,
        "ActivityInstanceId" / WString,
        "ActivityTypeName" / WString,
        "Data" / WString,
        "Annotations" / WString,
        "ProfileName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=110, version=0)
class Microsoft_Windows_Application_Server_Applications_110_0(Etw):
    pattern = Struct(
        "InstanceId" / Guid,
        "RecordNumber" / Int64sl,
        "EventTime" / Int64ul,
        "Name" / WString,
        "ActivityName" / WString,
        "ActivityId" / WString,
        "ActivityInstanceId" / WString,
        "ActivityTypeName" / WString,
        "Data" / WString,
        "Annotations" / WString,
        "ProfileName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=111, version=0)
class Microsoft_Windows_Application_Server_Applications_111_0(Etw):
    pattern = Struct(
        "InstanceId" / Guid,
        "RecordNumber" / Int64sl,
        "EventTime" / Int64ul,
        "Name" / WString,
        "ActivityName" / WString,
        "ActivityId" / WString,
        "ActivityInstanceId" / WString,
        "ActivityTypeName" / WString,
        "Data" / WString,
        "Annotations" / WString,
        "ProfileName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=112, version=0)
class Microsoft_Windows_Application_Server_Applications_112_0(Etw):
    pattern = Struct(
        "InstanceId" / Guid,
        "RecordNumber" / Int64sl,
        "EventTime" / Int64ul,
        "ActivityDefinitionId" / WString,
        "Reason" / WString,
        "Annotations" / WString,
        "ProfileName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=113, version=0)
class Microsoft_Windows_Application_Server_Applications_113_0(Etw):
    pattern = Struct(
        "InstanceId" / Guid,
        "RecordNumber" / Int64sl,
        "EventTime" / Int64ul,
        "ActivityDefinitionId" / WString,
        "Reason" / WString,
        "Annotations" / WString,
        "ProfileName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=114, version=0)
class Microsoft_Windows_Application_Server_Applications_114_0(Etw):
    pattern = Struct(
        "InstanceId" / Guid,
        "RecordNumber" / Int64sl,
        "EventTime" / Int64ul,
        "ActivityDefinitionId" / WString,
        "State" / WString,
        "Annotations" / WString,
        "ProfileName" / WString,
        "WorkflowDefinitionIdentity" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=115, version=0)
class Microsoft_Windows_Application_Server_Applications_115_0(Etw):
    pattern = Struct(
        "InstanceId" / Guid,
        "RecordNumber" / Int64sl,
        "EventTime" / Int64ul,
        "ActivityDefinitionId" / WString,
        "Reason" / WString,
        "Annotations" / WString,
        "ProfileName" / WString,
        "WorkflowDefinitionIdentity" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=116, version=0)
class Microsoft_Windows_Application_Server_Applications_116_0(Etw):
    pattern = Struct(
        "InstanceId" / Guid,
        "RecordNumber" / Int64sl,
        "EventTime" / Int64ul,
        "ActivityDefinitionId" / WString,
        "Reason" / WString,
        "Annotations" / WString,
        "ProfileName" / WString,
        "WorkflowDefinitionIdentity" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=117, version=0)
class Microsoft_Windows_Application_Server_Applications_117_0(Etw):
    pattern = Struct(
        "InstanceId" / Guid,
        "RecordNumber" / Int64sl,
        "EventTime" / Int64ul,
        "ActivityDefinitionId" / WString,
        "Reason" / WString,
        "Annotations" / WString,
        "ProfileName" / WString,
        "WorkflowDefinitionIdentity" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=118, version=0)
class Microsoft_Windows_Application_Server_Applications_118_0(Etw):
    pattern = Struct(
        "InstanceId" / Guid,
        "RecordNumber" / Int64sl,
        "EventTime" / Int64ul,
        "ActivityDefinitionId" / WString,
        "SourceName" / WString,
        "SourceId" / WString,
        "SourceInstanceId" / WString,
        "SourceTypeName" / WString,
        "Exception" / WString,
        "Annotations" / WString,
        "ProfileName" / WString,
        "WorkflowDefinitionIdentity" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=119, version=0)
class Microsoft_Windows_Application_Server_Applications_119_0(Etw):
    pattern = Struct(
        "InstanceId" / Guid,
        "RecordNumber" / Int64sl,
        "EventTime" / Int64ul,
        "ActivityDefinitionId" / WString,
        "State" / WString,
        "OriginalDefinitionIdentity" / WString,
        "UpdatedDefinitionIdentity" / WString,
        "Annotations" / WString,
        "ProfileName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=131, version=0)
class Microsoft_Windows_Application_Server_Applications_131_0(Etw):
    pattern = Struct(
        "Size" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=132, version=0)
class Microsoft_Windows_Application_Server_Applications_132_0(Etw):
    pattern = Struct(
        "PoolSize" / Int32sl,
        "Delta" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=133, version=0)
class Microsoft_Windows_Application_Server_Applications_133_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=134, version=0)
class Microsoft_Windows_Application_Server_Applications_134_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=201, version=0)
class Microsoft_Windows_Application_Server_Applications_201_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=202, version=0)
class Microsoft_Windows_Application_Server_Applications_202_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=203, version=0)
class Microsoft_Windows_Application_Server_Applications_203_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=204, version=0)
class Microsoft_Windows_Application_Server_Applications_204_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=205, version=0)
class Microsoft_Windows_Application_Server_Applications_205_0(Etw):
    pattern = Struct(
        "MethodName" / WString,
        "CallerInfo" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=206, version=0)
class Microsoft_Windows_Application_Server_Applications_206_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "Handled" / Int8ul,
        "ExceptionTypeName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=207, version=0)
class Microsoft_Windows_Application_Server_Applications_207_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "ExceptionTypeName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=208, version=0)
class Microsoft_Windows_Application_Server_Applications_208_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=209, version=0)
class Microsoft_Windows_Application_Server_Applications_209_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=210, version=0)
class Microsoft_Windows_Application_Server_Applications_210_0(Etw):
    pattern = Struct(
        "ThrottleName" / WString,
        "Limit" / Int64sl,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=211, version=0)
class Microsoft_Windows_Application_Server_Applications_211_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=212, version=0)
class Microsoft_Windows_Application_Server_Applications_212_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=213, version=0)
class Microsoft_Windows_Application_Server_Applications_213_0(Etw):
    pattern = Struct(
        "ServiceTypeName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=214, version=0)
class Microsoft_Windows_Application_Server_Applications_214_0(Etw):
    pattern = Struct(
        "MethodName" / WString,
        "Duration" / Int64sl,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=215, version=0)
class Microsoft_Windows_Application_Server_Applications_215_0(Etw):
    pattern = Struct(
        "ListenAddress" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=216, version=0)
class Microsoft_Windows_Application_Server_Applications_216_0(Etw):
    pattern = Struct(
        "DestinationAddress" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=217, version=0)
class Microsoft_Windows_Application_Server_Applications_217_0(Etw):
    pattern = Struct(
        "Action" / WString,
        "ContractName" / WString,
        "Destination" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=218, version=0)
class Microsoft_Windows_Application_Server_Applications_218_0(Etw):
    pattern = Struct(
        "Action" / WString,
        "ContractName" / WString,
        "Destination" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=219, version=0)
class Microsoft_Windows_Application_Server_Applications_219_0(Etw):
    pattern = Struct(
        "ExceptionToString" / WString,
        "ExceptionTypeName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=220, version=0)
class Microsoft_Windows_Application_Server_Applications_220_0(Etw):
    pattern = Struct(
        "CorrelationId" / Guid,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=221, version=0)
class Microsoft_Windows_Application_Server_Applications_221_0(Etw):
    pattern = Struct(
        "CorrelationId" / Guid,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=222, version=0)
class Microsoft_Windows_Application_Server_Applications_222_0(Etw):
    pattern = Struct(
        "MethodName" / WString,
        "Duration" / Int64sl,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=223, version=0)
class Microsoft_Windows_Application_Server_Applications_223_0(Etw):
    pattern = Struct(
        "MethodName" / WString,
        "Duration" / Int64sl,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=224, version=0)
class Microsoft_Windows_Application_Server_Applications_224_0(Etw):
    pattern = Struct(
        "ThrottleName" / WString,
        "Limit" / Int64sl,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=225, version=0)
class Microsoft_Windows_Application_Server_Applications_225_0(Etw):
    pattern = Struct(
        "InstanceKey" / Guid,
        "Values" / WString,
        "ParentScope" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=226, version=0)
class Microsoft_Windows_Application_Server_Applications_226_0(Etw):
    pattern = Struct(
        "ClosedCount" / Int32sl,
        "TotalCount" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=301, version=0)
class Microsoft_Windows_Application_Server_Applications_301_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "HostReference" / WString,
        "Payload" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=302, version=0)
class Microsoft_Windows_Application_Server_Applications_302_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "HostReference" / WString,
        "Payload" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=303, version=0)
class Microsoft_Windows_Application_Server_Applications_303_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "HostReference" / WString,
        "Payload" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=401, version=0)
class Microsoft_Windows_Application_Server_Applications_401_0(Etw):
    pattern = Struct(
        "ExtendedData" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=402, version=0)
class Microsoft_Windows_Application_Server_Applications_402_0(Etw):
    pattern = Struct(
        "ExtendedData" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=403, version=0)
class Microsoft_Windows_Application_Server_Applications_403_0(Etw):
    pattern = Struct(
        "ExtendedData" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=404, version=0)
class Microsoft_Windows_Application_Server_Applications_404_0(Etw):
    pattern = Struct(
        "ExtendedData" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=440, version=0)
class Microsoft_Windows_Application_Server_Applications_440_0(Etw):
    pattern = Struct(
        "ExtendedData" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=441, version=0)
class Microsoft_Windows_Application_Server_Applications_441_0(Etw):
    pattern = Struct(
        "ExtendedData" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=451, version=0)
class Microsoft_Windows_Application_Server_Applications_451_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=452, version=0)
class Microsoft_Windows_Application_Server_Applications_452_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=499, version=0)
class Microsoft_Windows_Application_Server_Applications_499_0(Etw):
    pattern = Struct(
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=501, version=0)
class Microsoft_Windows_Application_Server_Applications_501_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=502, version=0)
class Microsoft_Windows_Application_Server_Applications_502_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=503, version=0)
class Microsoft_Windows_Application_Server_Applications_503_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=504, version=0)
class Microsoft_Windows_Application_Server_Applications_504_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=505, version=0)
class Microsoft_Windows_Application_Server_Applications_505_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=506, version=0)
class Microsoft_Windows_Application_Server_Applications_506_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=507, version=0)
class Microsoft_Windows_Application_Server_Applications_507_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=508, version=0)
class Microsoft_Windows_Application_Server_Applications_508_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=509, version=0)
class Microsoft_Windows_Application_Server_Applications_509_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=510, version=0)
class Microsoft_Windows_Application_Server_Applications_510_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=513, version=0)
class Microsoft_Windows_Application_Server_Applications_513_0(Etw):
    pattern = Struct(
        "AppDomainFriendlyName" / WString,
        "VirtualPath" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=514, version=0)
class Microsoft_Windows_Application_Server_Applications_514_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=601, version=0)
class Microsoft_Windows_Application_Server_Applications_601_0(Etw):
    pattern = Struct(
        "RelativeAddress" / WString,
        "NormalizedAddress" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=602, version=0)
class Microsoft_Windows_Application_Server_Applications_602_0(Etw):
    pattern = Struct(
        "IncomingAddress" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=603, version=0)
class Microsoft_Windows_Application_Server_Applications_603_0(Etw):
    pattern = Struct(
        "IncomingAddress" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=604, version=0)
class Microsoft_Windows_Application_Server_Applications_604_0(Etw):
    pattern = Struct(
        "AspNetRoutePrefix" / WString,
        "ServiceType" / WString,
        "ServiceHostFactoryType" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=605, version=0)
class Microsoft_Windows_Application_Server_Applications_605_0(Etw):
    pattern = Struct(
        "Data" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=606, version=0)
class Microsoft_Windows_Application_Server_Applications_606_0(Etw):
    pattern = Struct(
        "Data" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=701, version=0)
class Microsoft_Windows_Application_Server_Applications_701_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=702, version=0)
class Microsoft_Windows_Application_Server_Applications_702_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=703, version=0)
class Microsoft_Windows_Application_Server_Applications_703_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=704, version=0)
class Microsoft_Windows_Application_Server_Applications_704_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=706, version=0)
class Microsoft_Windows_Application_Server_Applications_706_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=707, version=0)
class Microsoft_Windows_Application_Server_Applications_707_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=708, version=0)
class Microsoft_Windows_Application_Server_Applications_708_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=709, version=0)
class Microsoft_Windows_Application_Server_Applications_709_0(Etw):
    pattern = Struct(
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=710, version=0)
class Microsoft_Windows_Application_Server_Applications_710_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=711, version=0)
class Microsoft_Windows_Application_Server_Applications_711_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=712, version=0)
class Microsoft_Windows_Application_Server_Applications_712_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=715, version=0)
class Microsoft_Windows_Application_Server_Applications_715_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=716, version=0)
class Microsoft_Windows_Application_Server_Applications_716_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=717, version=0)
class Microsoft_Windows_Application_Server_Applications_717_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1001, version=0)
class Microsoft_Windows_Application_Server_Applications_1001_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1002, version=0)
class Microsoft_Windows_Application_Server_Applications_1002_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1003, version=0)
class Microsoft_Windows_Application_Server_Applications_1003_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1004, version=0)
class Microsoft_Windows_Application_Server_Applications_1004_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1005, version=0)
class Microsoft_Windows_Application_Server_Applications_1005_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1006, version=0)
class Microsoft_Windows_Application_Server_Applications_1006_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "data4" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1007, version=0)
class Microsoft_Windows_Application_Server_Applications_1007_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1008, version=0)
class Microsoft_Windows_Application_Server_Applications_1008_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1009, version=0)
class Microsoft_Windows_Application_Server_Applications_1009_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "data4" / WString,
        "data5" / WString,
        "data6" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1010, version=0)
class Microsoft_Windows_Application_Server_Applications_1010_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "data4" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1011, version=0)
class Microsoft_Windows_Application_Server_Applications_1011_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1012, version=0)
class Microsoft_Windows_Application_Server_Applications_1012_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1013, version=0)
class Microsoft_Windows_Application_Server_Applications_1013_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1014, version=0)
class Microsoft_Windows_Application_Server_Applications_1014_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "data4" / WString,
        "data5" / WString,
        "data6" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1015, version=0)
class Microsoft_Windows_Application_Server_Applications_1015_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "data4" / WString,
        "data5" / WString,
        "data6" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1016, version=0)
class Microsoft_Windows_Application_Server_Applications_1016_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "data4" / WString,
        "data5" / WString,
        "data6" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1017, version=0)
class Microsoft_Windows_Application_Server_Applications_1017_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1018, version=0)
class Microsoft_Windows_Application_Server_Applications_1018_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1019, version=0)
class Microsoft_Windows_Application_Server_Applications_1019_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1020, version=0)
class Microsoft_Windows_Application_Server_Applications_1020_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "data4" / WString,
        "data5" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1021, version=0)
class Microsoft_Windows_Application_Server_Applications_1021_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "data4" / WString,
        "data5" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1022, version=0)
class Microsoft_Windows_Application_Server_Applications_1022_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "data4" / WString,
        "data5" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1023, version=0)
class Microsoft_Windows_Application_Server_Applications_1023_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "data4" / WString,
        "data5" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1024, version=0)
class Microsoft_Windows_Application_Server_Applications_1024_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1025, version=0)
class Microsoft_Windows_Application_Server_Applications_1025_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1026, version=0)
class Microsoft_Windows_Application_Server_Applications_1026_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1027, version=0)
class Microsoft_Windows_Application_Server_Applications_1027_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1028, version=0)
class Microsoft_Windows_Application_Server_Applications_1028_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1029, version=0)
class Microsoft_Windows_Application_Server_Applications_1029_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "data4" / WString,
        "data5" / WString,
        "data6" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1030, version=0)
class Microsoft_Windows_Application_Server_Applications_1030_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "data4" / WString,
        "data5" / WString,
        "data6" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1031, version=0)
class Microsoft_Windows_Application_Server_Applications_1031_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "data4" / WString,
        "data5" / WString,
        "data6" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1032, version=0)
class Microsoft_Windows_Application_Server_Applications_1032_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1033, version=0)
class Microsoft_Windows_Application_Server_Applications_1033_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1034, version=0)
class Microsoft_Windows_Application_Server_Applications_1034_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1035, version=0)
class Microsoft_Windows_Application_Server_Applications_1035_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "data4" / WString,
        "data5" / WString,
        "data6" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1036, version=0)
class Microsoft_Windows_Application_Server_Applications_1036_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1037, version=0)
class Microsoft_Windows_Application_Server_Applications_1037_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1038, version=0)
class Microsoft_Windows_Application_Server_Applications_1038_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1039, version=0)
class Microsoft_Windows_Application_Server_Applications_1039_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1040, version=0)
class Microsoft_Windows_Application_Server_Applications_1040_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "data4" / WString,
        "data5" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1041, version=0)
class Microsoft_Windows_Application_Server_Applications_1041_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1101, version=0)
class Microsoft_Windows_Application_Server_Applications_1101_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1102, version=0)
class Microsoft_Windows_Application_Server_Applications_1102_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1103, version=0)
class Microsoft_Windows_Application_Server_Applications_1103_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1104, version=0)
class Microsoft_Windows_Application_Server_Applications_1104_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1124, version=0)
class Microsoft_Windows_Application_Server_Applications_1124_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1125, version=0)
class Microsoft_Windows_Application_Server_Applications_1125_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1126, version=0)
class Microsoft_Windows_Application_Server_Applications_1126_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1131, version=0)
class Microsoft_Windows_Application_Server_Applications_1131_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1132, version=0)
class Microsoft_Windows_Application_Server_Applications_1132_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1140, version=0)
class Microsoft_Windows_Application_Server_Applications_1140_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1141, version=0)
class Microsoft_Windows_Application_Server_Applications_1141_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1143, version=0)
class Microsoft_Windows_Application_Server_Applications_1143_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1146, version=0)
class Microsoft_Windows_Application_Server_Applications_1146_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1147, version=0)
class Microsoft_Windows_Application_Server_Applications_1147_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1148, version=0)
class Microsoft_Windows_Application_Server_Applications_1148_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1150, version=0)
class Microsoft_Windows_Application_Server_Applications_1150_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1223, version=0)
class Microsoft_Windows_Application_Server_Applications_1223_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1400, version=0)
class Microsoft_Windows_Application_Server_Applications_1400_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1401, version=0)
class Microsoft_Windows_Application_Server_Applications_1401_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1402, version=0)
class Microsoft_Windows_Application_Server_Applications_1402_0(Etw):
    pattern = Struct(
        "msg" / WString,
        "key" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1403, version=0)
class Microsoft_Windows_Application_Server_Applications_1403_0(Etw):
    pattern = Struct(
        "msg" / WString,
        "key" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1405, version=0)
class Microsoft_Windows_Application_Server_Applications_1405_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1406, version=0)
class Microsoft_Windows_Application_Server_Applications_1406_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1407, version=0)
class Microsoft_Windows_Application_Server_Applications_1407_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1409, version=0)
class Microsoft_Windows_Application_Server_Applications_1409_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1416, version=0)
class Microsoft_Windows_Application_Server_Applications_1416_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1417, version=0)
class Microsoft_Windows_Application_Server_Applications_1417_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1418, version=0)
class Microsoft_Windows_Application_Server_Applications_1418_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1419, version=0)
class Microsoft_Windows_Application_Server_Applications_1419_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1420, version=0)
class Microsoft_Windows_Application_Server_Applications_1420_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1422, version=0)
class Microsoft_Windows_Application_Server_Applications_1422_0(Etw):
    pattern = Struct(
        "msg" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1423, version=0)
class Microsoft_Windows_Application_Server_Applications_1423_0(Etw):
    pattern = Struct(
        "cur" / Int32sl,
        "max" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1424, version=0)
class Microsoft_Windows_Application_Server_Applications_1424_0(Etw):
    pattern = Struct(
        "cur" / Int32sl,
        "max" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1430, version=0)
class Microsoft_Windows_Application_Server_Applications_1430_0(Etw):
    pattern = Struct(
        "cur" / Int32sl,
        "max" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1431, version=0)
class Microsoft_Windows_Application_Server_Applications_1431_0(Etw):
    pattern = Struct(
        "cur" / Int32sl,
        "max" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1432, version=0)
class Microsoft_Windows_Application_Server_Applications_1432_0(Etw):
    pattern = Struct(
        "cur" / Int32sl,
        "max" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1433, version=0)
class Microsoft_Windows_Application_Server_Applications_1433_0(Etw):
    pattern = Struct(
        "cur" / Int32sl,
        "max" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1436, version=0)
class Microsoft_Windows_Application_Server_Applications_1436_0(Etw):
    pattern = Struct(
        "cur" / Int32sl,
        "max" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1438, version=0)
class Microsoft_Windows_Application_Server_Applications_1438_0(Etw):
    pattern = Struct(
        "cur" / Int32sl,
        "max" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1439, version=0)
class Microsoft_Windows_Application_Server_Applications_1439_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1441, version=0)
class Microsoft_Windows_Application_Server_Applications_1441_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1442, version=0)
class Microsoft_Windows_Application_Server_Applications_1442_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1443, version=0)
class Microsoft_Windows_Application_Server_Applications_1443_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1445, version=0)
class Microsoft_Windows_Application_Server_Applications_1445_0(Etw):
    pattern = Struct(
        "itemTypeName" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1446, version=0)
class Microsoft_Windows_Application_Server_Applications_1446_0(Etw):
    pattern = Struct(
        "itemTypeName" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1449, version=0)
class Microsoft_Windows_Application_Server_Applications_1449_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1450, version=0)
class Microsoft_Windows_Application_Server_Applications_1450_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=1451, version=0)
class Microsoft_Windows_Application_Server_Applications_1451_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=2021, version=0)
class Microsoft_Windows_Application_Server_Applications_2021_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=2022, version=0)
class Microsoft_Windows_Application_Server_Applications_2022_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=2023, version=0)
class Microsoft_Windows_Application_Server_Applications_2023_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=2024, version=0)
class Microsoft_Windows_Application_Server_Applications_2024_0(Etw):
    pattern = Struct(
        "id" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=2025, version=0)
class Microsoft_Windows_Application_Server_Applications_2025_0(Etw):
    pattern = Struct(
        "id" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=2026, version=0)
class Microsoft_Windows_Application_Server_Applications_2026_0(Etw):
    pattern = Struct(
        "expr" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=2027, version=0)
class Microsoft_Windows_Application_Server_Applications_2027_0(Etw):
    pattern = Struct(
        "activityName" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=2028, version=0)
class Microsoft_Windows_Application_Server_Applications_2028_0(Etw):
    pattern = Struct(
        "activityName" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=2029, version=0)
class Microsoft_Windows_Application_Server_Applications_2029_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=2576, version=0)
class Microsoft_Windows_Application_Server_Applications_2576_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=2577, version=0)
class Microsoft_Windows_Application_Server_Applications_2577_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=2578, version=0)
class Microsoft_Windows_Application_Server_Applications_2578_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3300, version=0)
class Microsoft_Windows_Application_Server_Applications_3300_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3301, version=0)
class Microsoft_Windows_Application_Server_Applications_3301_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3302, version=0)
class Microsoft_Windows_Application_Server_Applications_3302_0(Etw):
    pattern = Struct(
        "EventSource" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3303, version=0)
class Microsoft_Windows_Application_Server_Applications_3303_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "ExceptionToString" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3305, version=0)
class Microsoft_Windows_Application_Server_Applications_3305_0(Etw):
    pattern = Struct(
        "Count" / Int32sl,
        "MaxNum" / Int32sl,
        "EventSource" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3306, version=0)
class Microsoft_Windows_Application_Server_Applications_3306_0(Etw):
    pattern = Struct(
        "Count" / Int32sl,
        "EventSource" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3307, version=0)
class Microsoft_Windows_Application_Server_Applications_3307_0(Etw):
    pattern = Struct(
        "EventSource" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3308, version=0)
class Microsoft_Windows_Application_Server_Applications_3308_0(Etw):
    pattern = Struct(
        "EventSource" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3309, version=0)
class Microsoft_Windows_Application_Server_Applications_3309_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "Uri" / WString,
        "EventSource" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3310, version=0)
class Microsoft_Windows_Application_Server_Applications_3310_0(Etw):
    pattern = Struct(
        "OperationName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3311, version=0)
class Microsoft_Windows_Application_Server_Applications_3311_0(Etw):
    pattern = Struct(
        "OperationName" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3312, version=0)
class Microsoft_Windows_Application_Server_Applications_3312_0(Etw):
    pattern = Struct(
        "Size" / Int32sl,
        "EventSource" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3313, version=0)
class Microsoft_Windows_Application_Server_Applications_3313_0(Etw):
    pattern = Struct(
        "Size" / Int32sl,
        "EventSource" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3314, version=0)
class Microsoft_Windows_Application_Server_Applications_3314_0(Etw):
    pattern = Struct(
        "RemoteAddress" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3319, version=0)
class Microsoft_Windows_Application_Server_Applications_3319_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3320, version=0)
class Microsoft_Windows_Application_Server_Applications_3320_0(Etw):
    pattern = Struct(
        "ListenerHashCode" / Int32sl,
        "SocketHashCode" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3321, version=0)
class Microsoft_Windows_Application_Server_Applications_3321_0(Etw):
    pattern = Struct(
        "PoolKey" / WString,
        "busy" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3322, version=0)
class Microsoft_Windows_Application_Server_Applications_3322_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3323, version=0)
class Microsoft_Windows_Application_Server_Applications_3323_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3324, version=0)
class Microsoft_Windows_Application_Server_Applications_3324_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3325, version=0)
class Microsoft_Windows_Application_Server_Applications_3325_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3326, version=0)
class Microsoft_Windows_Application_Server_Applications_3326_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3327, version=0)
class Microsoft_Windows_Application_Server_Applications_3327_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3328, version=0)
class Microsoft_Windows_Application_Server_Applications_3328_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3329, version=0)
class Microsoft_Windows_Application_Server_Applications_3329_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3330, version=0)
class Microsoft_Windows_Application_Server_Applications_3330_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3331, version=0)
class Microsoft_Windows_Application_Server_Applications_3331_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3332, version=0)
class Microsoft_Windows_Application_Server_Applications_3332_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3333, version=0)
class Microsoft_Windows_Application_Server_Applications_3333_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3334, version=0)
class Microsoft_Windows_Application_Server_Applications_3334_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3335, version=0)
class Microsoft_Windows_Application_Server_Applications_3335_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3336, version=0)
class Microsoft_Windows_Application_Server_Applications_3336_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3337, version=0)
class Microsoft_Windows_Application_Server_Applications_3337_0(Etw):
    pattern = Struct(
        "ChannelId" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3338, version=0)
class Microsoft_Windows_Application_Server_Applications_3338_0(Etw):
    pattern = Struct(
        "ChannelId" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3339, version=0)
class Microsoft_Windows_Application_Server_Applications_3339_0(Etw):
    pattern = Struct(
        "EventSource" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3340, version=0)
class Microsoft_Windows_Application_Server_Applications_3340_0(Etw):
    pattern = Struct(
        "uri" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3341, version=0)
class Microsoft_Windows_Application_Server_Applications_3341_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3342, version=0)
class Microsoft_Windows_Application_Server_Applications_3342_0(Etw):
    pattern = Struct(
        "Key" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3343, version=0)
class Microsoft_Windows_Application_Server_Applications_3343_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3345, version=0)
class Microsoft_Windows_Application_Server_Applications_3345_0(Etw):
    pattern = Struct(
        "Via" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3346, version=0)
class Microsoft_Windows_Application_Server_Applications_3346_0(Etw):
    pattern = Struct(
        "FaultString" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3347, version=0)
class Microsoft_Windows_Application_Server_Applications_3347_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3348, version=0)
class Microsoft_Windows_Application_Server_Applications_3348_0(Etw):
    pattern = Struct(
        "EventSource" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3349, version=0)
class Microsoft_Windows_Application_Server_Applications_3349_0(Etw):
    pattern = Struct(
        "Uri" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3350, version=0)
class Microsoft_Windows_Application_Server_Applications_3350_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3351, version=0)
class Microsoft_Windows_Application_Server_Applications_3351_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3352, version=0)
class Microsoft_Windows_Application_Server_Applications_3352_0(Etw):
    pattern = Struct(
        "SocketId" / Int32sl,
        "Uri" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3353, version=0)
class Microsoft_Windows_Application_Server_Applications_3353_0(Etw):
    pattern = Struct(
        "SocketId" / Int32sl,
        "Uri" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3354, version=0)
class Microsoft_Windows_Application_Server_Applications_3354_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3355, version=0)
class Microsoft_Windows_Application_Server_Applications_3355_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3356, version=0)
class Microsoft_Windows_Application_Server_Applications_3356_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3357, version=0)
class Microsoft_Windows_Application_Server_Applications_3357_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3358, version=0)
class Microsoft_Windows_Application_Server_Applications_3358_0(Etw):
    pattern = Struct(
        "Uri" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3359, version=0)
class Microsoft_Windows_Application_Server_Applications_3359_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3360, version=0)
class Microsoft_Windows_Application_Server_Applications_3360_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3361, version=0)
class Microsoft_Windows_Application_Server_Applications_3361_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3362, version=0)
class Microsoft_Windows_Application_Server_Applications_3362_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3363, version=0)
class Microsoft_Windows_Application_Server_Applications_3363_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3364, version=0)
class Microsoft_Windows_Application_Server_Applications_3364_0(Etw):
    pattern = Struct(
        "Uri" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3365, version=0)
class Microsoft_Windows_Application_Server_Applications_3365_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3366, version=0)
class Microsoft_Windows_Application_Server_Applications_3366_0(Etw):
    pattern = Struct(
        "Status" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3367, version=0)
class Microsoft_Windows_Application_Server_Applications_3367_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3368, version=0)
class Microsoft_Windows_Application_Server_Applications_3368_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3369, version=0)
class Microsoft_Windows_Application_Server_Applications_3369_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3370, version=0)
class Microsoft_Windows_Application_Server_Applications_3370_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3371, version=0)
class Microsoft_Windows_Application_Server_Applications_3371_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3372, version=0)
class Microsoft_Windows_Application_Server_Applications_3372_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3373, version=0)
class Microsoft_Windows_Application_Server_Applications_3373_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3374, version=0)
class Microsoft_Windows_Application_Server_Applications_3374_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3375, version=0)
class Microsoft_Windows_Application_Server_Applications_3375_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3376, version=0)
class Microsoft_Windows_Application_Server_Applications_3376_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3377, version=0)
class Microsoft_Windows_Application_Server_Applications_3377_0(Etw):
    pattern = Struct(
        "SocketId" / Int32sl,
        "Size" / Int32sl,
        "Endpoint" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3378, version=0)
class Microsoft_Windows_Application_Server_Applications_3378_0(Etw):
    pattern = Struct(
        "SocketId" / Int32sl,
        "Size" / Int32sl,
        "Endpoint" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3379, version=0)
class Microsoft_Windows_Application_Server_Applications_3379_0(Etw):
    pattern = Struct(
        "SocketId" / Int32sl,
        "Size" / Int32sl,
        "Endpoint" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3380, version=0)
class Microsoft_Windows_Application_Server_Applications_3380_0(Etw):
    pattern = Struct(
        "SocketId" / Int32sl,
        "Size" / Int32sl,
        "Endpoint" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3381, version=0)
class Microsoft_Windows_Application_Server_Applications_3381_0(Etw):
    pattern = Struct(
        "SessionId" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3382, version=0)
class Microsoft_Windows_Application_Server_Applications_3382_0(Etw):
    pattern = Struct(
        "SessionId" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3383, version=0)
class Microsoft_Windows_Application_Server_Applications_3383_0(Etw):
    pattern = Struct(
        "SessionId" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3384, version=0)
class Microsoft_Windows_Application_Server_Applications_3384_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3385, version=0)
class Microsoft_Windows_Application_Server_Applications_3385_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3386, version=0)
class Microsoft_Windows_Application_Server_Applications_3386_0(Etw):
    pattern = Struct(
        "SocketId" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3388, version=0)
class Microsoft_Windows_Application_Server_Applications_3388_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3389, version=0)
class Microsoft_Windows_Application_Server_Applications_3389_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3390, version=0)
class Microsoft_Windows_Application_Server_Applications_3390_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3391, version=0)
class Microsoft_Windows_Application_Server_Applications_3391_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3392, version=0)
class Microsoft_Windows_Application_Server_Applications_3392_0(Etw):
    pattern = Struct(
        "LocalId" / WString,
        "Distributed" / Guid,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3393, version=0)
class Microsoft_Windows_Application_Server_Applications_3393_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3394, version=0)
class Microsoft_Windows_Application_Server_Applications_3394_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3395, version=0)
class Microsoft_Windows_Application_Server_Applications_3395_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3396, version=0)
class Microsoft_Windows_Application_Server_Applications_3396_0(Etw):
    pattern = Struct(
        "BufferId" / Int32sl,
        "Size" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3397, version=0)
class Microsoft_Windows_Application_Server_Applications_3397_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3398, version=0)
class Microsoft_Windows_Application_Server_Applications_3398_0(Etw):
    pattern = Struct(
        "sharedMemoryName" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3399, version=0)
class Microsoft_Windows_Application_Server_Applications_3399_0(Etw):
    pattern = Struct(
        "pipeName" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3401, version=0)
class Microsoft_Windows_Application_Server_Applications_3401_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3402, version=0)
class Microsoft_Windows_Application_Server_Applications_3402_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3403, version=0)
class Microsoft_Windows_Application_Server_Applications_3403_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3404, version=0)
class Microsoft_Windows_Application_Server_Applications_3404_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3405, version=0)
class Microsoft_Windows_Application_Server_Applications_3405_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3406, version=0)
class Microsoft_Windows_Application_Server_Applications_3406_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3407, version=0)
class Microsoft_Windows_Application_Server_Applications_3407_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3408, version=0)
class Microsoft_Windows_Application_Server_Applications_3408_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3409, version=0)
class Microsoft_Windows_Application_Server_Applications_3409_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3410, version=0)
class Microsoft_Windows_Application_Server_Applications_3410_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3411, version=0)
class Microsoft_Windows_Application_Server_Applications_3411_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3412, version=0)
class Microsoft_Windows_Application_Server_Applications_3412_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3413, version=0)
class Microsoft_Windows_Application_Server_Applications_3413_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3414, version=0)
class Microsoft_Windows_Application_Server_Applications_3414_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3415, version=0)
class Microsoft_Windows_Application_Server_Applications_3415_0(Etw):
    pattern = Struct(
        "remoteAddress" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3416, version=0)
class Microsoft_Windows_Application_Server_Applications_3416_0(Etw):
    pattern = Struct(
        "websocketId" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3417, version=0)
class Microsoft_Windows_Application_Server_Applications_3417_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3418, version=0)
class Microsoft_Windows_Application_Server_Applications_3418_0(Etw):
    pattern = Struct(
        "websocketId" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3419, version=0)
class Microsoft_Windows_Application_Server_Applications_3419_0(Etw):
    pattern = Struct(
        "errorMessage" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3420, version=0)
class Microsoft_Windows_Application_Server_Applications_3420_0(Etw):
    pattern = Struct(
        "errorMessage" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3421, version=0)
class Microsoft_Windows_Application_Server_Applications_3421_0(Etw):
    pattern = Struct(
        "websocketId" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3422, version=0)
class Microsoft_Windows_Application_Server_Applications_3422_0(Etw):
    pattern = Struct(
        "websocketId" / Int32sl,
        "byteCount" / Int32sl,
        "remoteAddress" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3423, version=0)
class Microsoft_Windows_Application_Server_Applications_3423_0(Etw):
    pattern = Struct(
        "websocketId" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3424, version=0)
class Microsoft_Windows_Application_Server_Applications_3424_0(Etw):
    pattern = Struct(
        "websocketId" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3425, version=0)
class Microsoft_Windows_Application_Server_Applications_3425_0(Etw):
    pattern = Struct(
        "websocketId" / Int32sl,
        "byteCount" / Int32sl,
        "remoteAddress" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3426, version=0)
class Microsoft_Windows_Application_Server_Applications_3426_0(Etw):
    pattern = Struct(
        "websocketId" / Int32sl,
        "remoteAddress" / WString,
        "closeStatus" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3427, version=0)
class Microsoft_Windows_Application_Server_Applications_3427_0(Etw):
    pattern = Struct(
        "websocketId" / Int32sl,
        "remoteAddress" / WString,
        "closeStatus" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3428, version=0)
class Microsoft_Windows_Application_Server_Applications_3428_0(Etw):
    pattern = Struct(
        "websocketId" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3429, version=0)
class Microsoft_Windows_Application_Server_Applications_3429_0(Etw):
    pattern = Struct(
        "websocketId" / Int32sl,
        "closeStatus" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3430, version=0)
class Microsoft_Windows_Application_Server_Applications_3430_0(Etw):
    pattern = Struct(
        "clientWebSocketFactoryType" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3431, version=0)
class Microsoft_Windows_Application_Server_Applications_3431_0(Etw):
    pattern = Struct(
        "clientWebSocketFactoryType" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3501, version=0)
class Microsoft_Windows_Application_Server_Applications_3501_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3502, version=0)
class Microsoft_Windows_Application_Server_Applications_3502_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3503, version=0)
class Microsoft_Windows_Application_Server_Applications_3503_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3507, version=0)
class Microsoft_Windows_Application_Server_Applications_3507_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3508, version=0)
class Microsoft_Windows_Application_Server_Applications_3508_0(Etw):
    pattern = Struct(
        "TrackingProfile" / WString,
        "ActivityDefinitionId" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3550, version=0)
class Microsoft_Windows_Application_Server_Applications_3550_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3551, version=0)
class Microsoft_Windows_Application_Server_Applications_3551_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3552, version=0)
class Microsoft_Windows_Application_Server_Applications_3552_0(Etw):
    pattern = Struct(
        "limit" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3553, version=0)
class Microsoft_Windows_Application_Server_Applications_3553_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3554, version=0)
class Microsoft_Windows_Application_Server_Applications_3554_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3555, version=0)
class Microsoft_Windows_Application_Server_Applications_3555_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3556, version=0)
class Microsoft_Windows_Application_Server_Applications_3556_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3557, version=0)
class Microsoft_Windows_Application_Server_Applications_3557_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3558, version=0)
class Microsoft_Windows_Application_Server_Applications_3558_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3559, version=0)
class Microsoft_Windows_Application_Server_Applications_3559_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3560, version=0)
class Microsoft_Windows_Application_Server_Applications_3560_0(Etw):
    pattern = Struct(
        "availableMemoryBytes" / Int64ul,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3561, version=0)
class Microsoft_Windows_Application_Server_Applications_3561_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3800, version=0)
class Microsoft_Windows_Application_Server_Applications_3800_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3801, version=0)
class Microsoft_Windows_Application_Server_Applications_3801_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3802, version=0)
class Microsoft_Windows_Application_Server_Applications_3802_0(Etw):
    pattern = Struct(
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3803, version=0)
class Microsoft_Windows_Application_Server_Applications_3803_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3804, version=0)
class Microsoft_Windows_Application_Server_Applications_3804_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3805, version=0)
class Microsoft_Windows_Application_Server_Applications_3805_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3807, version=0)
class Microsoft_Windows_Application_Server_Applications_3807_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3809, version=0)
class Microsoft_Windows_Application_Server_Applications_3809_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3810, version=0)
class Microsoft_Windows_Application_Server_Applications_3810_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3815, version=0)
class Microsoft_Windows_Application_Server_Applications_3815_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "data4" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3816, version=0)
class Microsoft_Windows_Application_Server_Applications_3816_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3817, version=0)
class Microsoft_Windows_Application_Server_Applications_3817_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3818, version=0)
class Microsoft_Windows_Application_Server_Applications_3818_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3819, version=0)
class Microsoft_Windows_Application_Server_Applications_3819_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3820, version=0)
class Microsoft_Windows_Application_Server_Applications_3820_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3821, version=0)
class Microsoft_Windows_Application_Server_Applications_3821_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3822, version=0)
class Microsoft_Windows_Application_Server_Applications_3822_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3823, version=0)
class Microsoft_Windows_Application_Server_Applications_3823_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3824, version=0)
class Microsoft_Windows_Application_Server_Applications_3824_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3825, version=0)
class Microsoft_Windows_Application_Server_Applications_3825_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3826, version=0)
class Microsoft_Windows_Application_Server_Applications_3826_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3827, version=0)
class Microsoft_Windows_Application_Server_Applications_3827_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3828, version=0)
class Microsoft_Windows_Application_Server_Applications_3828_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3829, version=0)
class Microsoft_Windows_Application_Server_Applications_3829_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3830, version=0)
class Microsoft_Windows_Application_Server_Applications_3830_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3831, version=0)
class Microsoft_Windows_Application_Server_Applications_3831_0(Etw):
    pattern = Struct(
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=3832, version=0)
class Microsoft_Windows_Application_Server_Applications_3832_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4001, version=0)
class Microsoft_Windows_Application_Server_Applications_4001_0(Etw):
    pattern = Struct(
        "via" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4002, version=0)
class Microsoft_Windows_Application_Server_Applications_4002_0(Etw):
    pattern = Struct(
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4003, version=0)
class Microsoft_Windows_Application_Server_Applications_4003_0(Etw):
    pattern = Struct(
        "Endpoint" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4008, version=0)
class Microsoft_Windows_Application_Server_Applications_4008_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4010, version=0)
class Microsoft_Windows_Application_Server_Applications_4010_0(Etw):
    pattern = Struct(
        "Uri" / WString,
        "count" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4011, version=0)
class Microsoft_Windows_Application_Server_Applications_4011_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4012, version=0)
class Microsoft_Windows_Application_Server_Applications_4012_0(Etw):
    pattern = Struct(
        "Status" / WString,
        "Uri" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4013, version=0)
class Microsoft_Windows_Application_Server_Applications_4013_0(Etw):
    pattern = Struct(
        "Uri" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4014, version=0)
class Microsoft_Windows_Application_Server_Applications_4014_0(Etw):
    pattern = Struct(
        "Uri" / WString,
        "Status" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4015, version=0)
class Microsoft_Windows_Application_Server_Applications_4015_0(Etw):
    pattern = Struct(
        "Uri" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4016, version=0)
class Microsoft_Windows_Application_Server_Applications_4016_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4019, version=0)
class Microsoft_Windows_Application_Server_Applications_4019_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4020, version=0)
class Microsoft_Windows_Application_Server_Applications_4020_0(Etw):
    pattern = Struct(
        "Uri" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4021, version=0)
class Microsoft_Windows_Application_Server_Applications_4021_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4022, version=0)
class Microsoft_Windows_Application_Server_Applications_4022_0(Etw):
    pattern = Struct(
        "hresult" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4023, version=0)
class Microsoft_Windows_Application_Server_Applications_4023_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4024, version=0)
class Microsoft_Windows_Application_Server_Applications_4024_0(Etw):
    pattern = Struct(
        "hresult" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4025, version=0)
class Microsoft_Windows_Application_Server_Applications_4025_0(Etw):
    pattern = Struct(
        "hresult" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4026, version=0)
class Microsoft_Windows_Application_Server_Applications_4026_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4027, version=0)
class Microsoft_Windows_Application_Server_Applications_4027_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4028, version=0)
class Microsoft_Windows_Application_Server_Applications_4028_0(Etw):
    pattern = Struct(
        "Uri" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4029, version=0)
class Microsoft_Windows_Application_Server_Applications_4029_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4030, version=0)
class Microsoft_Windows_Application_Server_Applications_4030_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4031, version=0)
class Microsoft_Windows_Application_Server_Applications_4031_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4032, version=0)
class Microsoft_Windows_Application_Server_Applications_4032_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4033, version=0)
class Microsoft_Windows_Application_Server_Applications_4033_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4034, version=0)
class Microsoft_Windows_Application_Server_Applications_4034_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4035, version=0)
class Microsoft_Windows_Application_Server_Applications_4035_0(Etw):
    pattern = Struct(
        "curr" / Int32sl,
        "max" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4201, version=0)
class Microsoft_Windows_Application_Server_Applications_4201_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4202, version=0)
class Microsoft_Windows_Application_Server_Applications_4202_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4203, version=0)
class Microsoft_Windows_Application_Server_Applications_4203_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4205, version=0)
class Microsoft_Windows_Application_Server_Applications_4205_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4206, version=0)
class Microsoft_Windows_Application_Server_Applications_4206_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4207, version=0)
class Microsoft_Windows_Application_Server_Applications_4207_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4208, version=0)
class Microsoft_Windows_Application_Server_Applications_4208_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4209, version=0)
class Microsoft_Windows_Application_Server_Applications_4209_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4210, version=0)
class Microsoft_Windows_Application_Server_Applications_4210_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4211, version=0)
class Microsoft_Windows_Application_Server_Applications_4211_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4212, version=0)
class Microsoft_Windows_Application_Server_Applications_4212_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4213, version=0)
class Microsoft_Windows_Application_Server_Applications_4213_0(Etw):
    pattern = Struct(
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4214, version=0)
class Microsoft_Windows_Application_Server_Applications_4214_0(Etw):
    pattern = Struct(
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4600, version=0)
class Microsoft_Windows_Application_Server_Applications_4600_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4801, version=0)
class Microsoft_Windows_Application_Server_Applications_4801_0(Etw):
    pattern = Struct(
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4802, version=0)
class Microsoft_Windows_Application_Server_Applications_4802_0(Etw):
    pattern = Struct(
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4803, version=0)
class Microsoft_Windows_Application_Server_Applications_4803_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4804, version=0)
class Microsoft_Windows_Application_Server_Applications_4804_0(Etw):
    pattern = Struct(
        "discoveryMessageName" / WString,
        "messageId" / WString,
        "discoveryOperationName" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4805, version=0)
class Microsoft_Windows_Application_Server_Applications_4805_0(Etw):
    pattern = Struct(
        "messageType" / WString,
        "messageId" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4806, version=0)
class Microsoft_Windows_Application_Server_Applications_4806_0(Etw):
    pattern = Struct(
        "discoveryMessageName" / WString,
        "messageId" / WString,
        "relatesTo" / WString,
        "discoveryOperationName" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4807, version=0)
class Microsoft_Windows_Application_Server_Applications_4807_0(Etw):
    pattern = Struct(
        "messageId" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4808, version=0)
class Microsoft_Windows_Application_Server_Applications_4808_0(Etw):
    pattern = Struct(
        "messageType" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4809, version=0)
class Microsoft_Windows_Application_Server_Applications_4809_0(Etw):
    pattern = Struct(
        "messageType" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4810, version=0)
class Microsoft_Windows_Application_Server_Applications_4810_0(Etw):
    pattern = Struct(
        "discoveryMessageName" / WString,
        "messageId" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4811, version=0)
class Microsoft_Windows_Application_Server_Applications_4811_0(Etw):
    pattern = Struct(
        "discoveryMessageName" / WString,
        "messageId" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4812, version=0)
class Microsoft_Windows_Application_Server_Applications_4812_0(Etw):
    pattern = Struct(
        "messageId" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4813, version=0)
class Microsoft_Windows_Application_Server_Applications_4813_0(Etw):
    pattern = Struct(
        "messageType" / WString,
        "messageId" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4814, version=0)
class Microsoft_Windows_Application_Server_Applications_4814_0(Etw):
    pattern = Struct(
        "endpointAddress" / WString,
        "listenUri" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4815, version=0)
class Microsoft_Windows_Application_Server_Applications_4815_0(Etw):
    pattern = Struct(
        "endpointAddress" / WString,
        "listenUri" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4816, version=0)
class Microsoft_Windows_Application_Server_Applications_4816_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4817, version=0)
class Microsoft_Windows_Application_Server_Applications_4817_0(Etw):
    pattern = Struct(
        "endpointAddress" / WString,
        "via" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4818, version=0)
class Microsoft_Windows_Application_Server_Applications_4818_0(Etw):
    pattern = Struct(
        "endpointAddress" / WString,
        "via" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4819, version=0)
class Microsoft_Windows_Application_Server_Applications_4819_0(Etw):
    pattern = Struct(
        "endpointAddress" / WString,
        "via" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4820, version=0)
class Microsoft_Windows_Application_Server_Applications_4820_0(Etw):
    pattern = Struct(
        "synchronizationContextType" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=4821, version=0)
class Microsoft_Windows_Application_Server_Applications_4821_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5001, version=0)
class Microsoft_Windows_Application_Server_Applications_5001_0(Etw):
    pattern = Struct(
        "SurrogateType" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5002, version=0)
class Microsoft_Windows_Application_Server_Applications_5002_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5003, version=0)
class Microsoft_Windows_Application_Server_Applications_5003_0(Etw):
    pattern = Struct(
        "SurrogateType" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5004, version=0)
class Microsoft_Windows_Application_Server_Applications_5004_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5005, version=0)
class Microsoft_Windows_Application_Server_Applications_5005_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5006, version=0)
class Microsoft_Windows_Application_Server_Applications_5006_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5007, version=0)
class Microsoft_Windows_Application_Server_Applications_5007_0(Etw):
    pattern = Struct(
        "TypeName" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5008, version=0)
class Microsoft_Windows_Application_Server_Applications_5008_0(Etw):
    pattern = Struct(
        "Kind" / WString,
        "TypeName" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5009, version=0)
class Microsoft_Windows_Application_Server_Applications_5009_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5010, version=0)
class Microsoft_Windows_Application_Server_Applications_5010_0(Etw):
    pattern = Struct(
        "Kind" / WString,
        "TypeName" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5011, version=0)
class Microsoft_Windows_Application_Server_Applications_5011_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5012, version=0)
class Microsoft_Windows_Application_Server_Applications_5012_0(Etw):
    pattern = Struct(
        "Kind" / WString,
        "TypeName" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5013, version=0)
class Microsoft_Windows_Application_Server_Applications_5013_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5014, version=0)
class Microsoft_Windows_Application_Server_Applications_5014_0(Etw):
    pattern = Struct(
        "Kind" / WString,
        "TypeName" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5015, version=0)
class Microsoft_Windows_Application_Server_Applications_5015_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5016, version=0)
class Microsoft_Windows_Application_Server_Applications_5016_0(Etw):
    pattern = Struct(
        "DCType" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5017, version=0)
class Microsoft_Windows_Application_Server_Applications_5017_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5203, version=0)
class Microsoft_Windows_Application_Server_Applications_5203_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5204, version=0)
class Microsoft_Windows_Application_Server_Applications_5204_0(Etw):
    pattern = Struct(
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5402, version=0)
class Microsoft_Windows_Application_Server_Applications_5402_0(Etw):
    pattern = Struct(
        "tokenType" / WString,
        "tokenID" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5403, version=0)
class Microsoft_Windows_Application_Server_Applications_5403_0(Etw):
    pattern = Struct(
        "tokenType" / WString,
        "tokenID" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5404, version=0)
class Microsoft_Windows_Application_Server_Applications_5404_0(Etw):
    pattern = Struct(
        "tokenType" / WString,
        "tokenID" / WString,
        "errorMessage" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5405, version=0)
class Microsoft_Windows_Application_Server_Applications_5405_0(Etw):
    pattern = Struct(
        "issuerName" / WString,
        "tokenID" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5406, version=0)
class Microsoft_Windows_Application_Server_Applications_5406_0(Etw):
    pattern = Struct(
        "tokenID" / WString,
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5600, version=0)
class Microsoft_Windows_Application_Server_Applications_5600_0(Etw):
    pattern = Struct(
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5601, version=0)
class Microsoft_Windows_Application_Server_Applications_5601_0(Etw):
    pattern = Struct(
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5602, version=0)
class Microsoft_Windows_Application_Server_Applications_5602_0(Etw):
    pattern = Struct(
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5603, version=0)
class Microsoft_Windows_Application_Server_Applications_5603_0(Etw):
    pattern = Struct(
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5604, version=0)
class Microsoft_Windows_Application_Server_Applications_5604_0(Etw):
    pattern = Struct(
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5605, version=0)
class Microsoft_Windows_Application_Server_Applications_5605_0(Etw):
    pattern = Struct(
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5606, version=0)
class Microsoft_Windows_Application_Server_Applications_5606_0(Etw):
    pattern = Struct(
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=5607, version=0)
class Microsoft_Windows_Application_Server_Applications_5607_0(Etw):
    pattern = Struct(
        "HostReference" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=39456, version=0)
class Microsoft_Windows_Application_Server_Applications_39456_0(Etw):
    pattern = Struct(
        "RecordNumber" / Int64sl,
        "ProviderId" / Guid,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=39457, version=0)
class Microsoft_Windows_Application_Server_Applications_39457_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=39458, version=0)
class Microsoft_Windows_Application_Server_Applications_39458_0(Etw):
    pattern = Struct(
        "RecordNumber" / Int64sl,
        "ProviderId" / Guid,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=39459, version=0)
class Microsoft_Windows_Application_Server_Applications_39459_0(Etw):
    pattern = Struct(
        "Data" / WString,
        "Activity" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=39460, version=0)
class Microsoft_Windows_Application_Server_Applications_39460_0(Etw):
    pattern = Struct(
        "name" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=57393, version=0)
class Microsoft_Windows_Application_Server_Applications_57393_0(Etw):
    pattern = Struct(
        "appdomainName" / WString,
        "processName" / WString,
        "processId" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=57394, version=0)
class Microsoft_Windows_Application_Server_Applications_57394_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=57395, version=0)
class Microsoft_Windows_Application_Server_Applications_57395_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=57396, version=0)
class Microsoft_Windows_Application_Server_Applications_57396_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=57397, version=0)
class Microsoft_Windows_Application_Server_Applications_57397_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=57398, version=0)
class Microsoft_Windows_Application_Server_Applications_57398_0(Etw):
    pattern = Struct(
        "limit" / Int32sl,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=57399, version=0)
class Microsoft_Windows_Application_Server_Applications_57399_0(Etw):
    pattern = Struct(
        "ExtendedData" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=57400, version=0)
class Microsoft_Windows_Application_Server_Applications_57400_0(Etw):
    pattern = Struct(
        "ExtendedData" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=57401, version=0)
class Microsoft_Windows_Application_Server_Applications_57401_0(Etw):
    pattern = Struct(
        "ExtendedData" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=57402, version=0)
class Microsoft_Windows_Application_Server_Applications_57402_0(Etw):
    pattern = Struct(
        "ExtendedData" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=57403, version=0)
class Microsoft_Windows_Application_Server_Applications_57403_0(Etw):
    pattern = Struct(
        "ExtendedData" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=57404, version=0)
class Microsoft_Windows_Application_Server_Applications_57404_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=57405, version=0)
class Microsoft_Windows_Application_Server_Applications_57405_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=57406, version=0)
class Microsoft_Windows_Application_Server_Applications_57406_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=57407, version=0)
class Microsoft_Windows_Application_Server_Applications_57407_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=57408, version=0)
class Microsoft_Windows_Application_Server_Applications_57408_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=57409, version=0)
class Microsoft_Windows_Application_Server_Applications_57409_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=57410, version=0)
class Microsoft_Windows_Application_Server_Applications_57410_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "SerializedException" / WString,
        "AppDomain" / WString
    )


@declare(guid=guid("c651f5f6-1c0d-492e-8ae1-b4efd7c9d503"), event_id=62326, version=0)
class Microsoft_Windows_Application_Server_Applications_62326_0(Etw):
    pattern = Struct(
        "data1" / WString,
        "data2" / WString,
        "data3" / WString,
        "AppDomain" / WString
    )

