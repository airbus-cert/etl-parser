# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WMI-Activity
GUID : 1418ef04-b0b4-4623-bf7e-d74ab47bbdaa
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=1, version=0)
class Microsoft_Windows_WMI_Activity_1_0(Etw):
    pattern = Struct(
        "GroupOperationId" / Int32ul,
        "OperationId" / Int32ul,
        "Operation" / WString,
        "ClientMachine" / WString,
        "User" / WString,
        "ClientProcessId" / Int32ul,
        "NamespaceName" / WString
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=2, version=0)
class Microsoft_Windows_WMI_Activity_2_0(Etw):
    pattern = Struct(
        "GroupOperationId" / Int32ul,
        "Operation" / WString,
        "ProviderName" / WString,
        "ProviderGuid" / WString,
        "Path" / WString
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=3, version=0)
class Microsoft_Windows_WMI_Activity_3_0(Etw):
    pattern = Struct(
        "OperationId" / Int32ul
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=11, version=0)
class Microsoft_Windows_WMI_Activity_11_0(Etw):
    pattern = Struct(
        "CorrelationId" / WString,
        "GroupOperationId" / Int32ul,
        "OperationId" / Int32ul,
        "Operation" / WString,
        "ClientMachine" / WString,
        "ClientMachineFQDN" / WString,
        "User" / WString,
        "ClientProcessId" / Int32ul,
        "ClientProcessCreationTime" / Int64ul,
        "NamespaceName" / WString,
        "IsLocal" / Int8ul
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=12, version=0)
class Microsoft_Windows_WMI_Activity_12_0(Etw):
    pattern = Struct(
        "GroupOperationId" / Int32ul,
        "Operation" / WString,
        "HostId" / Int32ul,
        "ProviderName" / WString,
        "ProviderGuid" / WString,
        "Path" / WString
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=13, version=0)
class Microsoft_Windows_WMI_Activity_13_0(Etw):
    pattern = Struct(
        "OperationId" / Int32ul,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=14, version=0)
class Microsoft_Windows_WMI_Activity_14_0(Etw):
    pattern = Struct(
        "OperationId" / Int32ul,
        "Operation" / WString,
        "Channel" / Int32ul,
        "Message" / WString
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=15, version=0)
class Microsoft_Windows_WMI_Activity_15_0(Etw):
    pattern = Struct(
        "OperationId" / Int32ul,
        "Operation" / WString,
        "ErrorId" / WString,
        "ErrorCategory" / Int32ul,
        "Message" / WString,
        "TargetName" / WString
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=16, version=0)
class Microsoft_Windows_WMI_Activity_16_0(Etw):
    pattern = Struct(
        "OperationId" / Int32ul,
        "Operation" / WString,
        "ErrorId" / Int32ul,
        "Message" / WString
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=17, version=0)
class Microsoft_Windows_WMI_Activity_17_0(Etw):
    pattern = Struct(
        "CorrelationId" / WString,
        "ProcessId" / Int32ul,
        "Protocol" / WString,
        "Operation" / WString,
        "User" / WString,
        "Namespace" / WString
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=18, version=0)
class Microsoft_Windows_WMI_Activity_18_0(Etw):
    pattern = Struct(
        "ConsumerType" / WString,
        "PossibleCause" / WString
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=19, version=0)
class Microsoft_Windows_WMI_Activity_19_0(Etw):
    pattern = Struct(
        "OperationID" / Int32ul,
        "Operation" / WString,
        "ClientProcessId" / Int32ul,
        "ClientMachineFQDN" / WString,
        "ClientProcessCreationTime" / Int64ul,
        "IsLocal" / Int8ul
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=20, version=0)
class Microsoft_Windows_WMI_Activity_20_0(Etw):
    pattern = Struct(
        "OperationID" / Int32ul,
        "Operation" / WString,
        "Flags" / Int32ul,
        "ClientProcessId" / Int32ul,
        "ClientMachineFQDN" / WString,
        "ClientProcessCreationTime" / Int64ul,
        "IsLocal" / Int8ul
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=21, version=0)
class Microsoft_Windows_WMI_Activity_21_0(Etw):
    pattern = Struct(
        "ConsumerType" / WString,
        "PossibleCause" / WString
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=22, version=0)
class Microsoft_Windows_WMI_Activity_22_0(Etw):
    pattern = Struct(
        "CorrelationId" / WString,
        "GroupOperationId" / Int32ul,
        "OperationId" / Int32ul,
        "ClassName" / WString,
        "MethodName" / WString,
        "ImplementationClass" / WString,
        "ClientMachine" / WString,
        "ClientMachineFQDN" / WString,
        "User" / WString,
        "ClientProcessId" / Int32ul,
        "ClientProcessCreationTime" / Int64ul,
        "NamespaceName" / WString,
        "IsLocal" / Int8ul
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=23, version=0)
class Microsoft_Windows_WMI_Activity_23_0(Etw):
    pattern = Struct(
        "CorrelationId" / WString,
        "GroupOperationId" / Int32ul,
        "OperationId" / Int32ul,
        "Commandline" / WString,
        "CreatedProcessId" / Int32ul,
        "CreatedProcessCreationTime" / Int64ul,
        "ClientMachine" / WString,
        "ClientMachineFQDN" / WString,
        "User" / WString,
        "ClientProcessId" / Int32ul,
        "ClientProcessCreationTime" / Int64ul,
        "IsLocal" / Int8ul
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=100, version=0)
class Microsoft_Windows_WMI_Activity_100_0(Etw):
    pattern = Struct(
        "ComponentName" / WString,
        "MessageDetail" / WString,
        "FileName" / WString
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=101, version=0)
class Microsoft_Windows_WMI_Activity_101_0(Etw):
    pattern = Struct(
        "ComponentName" / WString,
        "ErrorId" / Int32ul,
        "ErrorDetail" / WString,
        "FileName" / WString
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=5857, version=0)
class Microsoft_Windows_WMI_Activity_5857_0(Etw):
    pattern = Struct(
        "ProviderName" / WString,
        "Code" / Int32ul,
        "HostProcess" / WString,
        "ProcessID" / Int32ul,
        "ProviderPath" / WString
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=5858, version=0)
class Microsoft_Windows_WMI_Activity_5858_0(Etw):
    pattern = Struct(
        "Id" / WString,
        "ClientMachine" / WString,
        "User" / WString,
        "ClientProcessId" / Int32ul,
        "Component" / WString,
        "Operation" / WString,
        "ResultCode" / Int32ul,
        "PossibleCause" / WString
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=5859, version=0)
class Microsoft_Windows_WMI_Activity_5859_0(Etw):
    pattern = Struct(
        "NamespaceName" / WString,
        "Query" / WString,
        "User" / WString,
        "processid" / Int32ul,
        "providerName" / WString,
        "queryid" / Int32ul,
        "PossibleCause" / WString
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=5860, version=0)
class Microsoft_Windows_WMI_Activity_5860_0(Etw):
    pattern = Struct(
        "NamespaceName" / WString,
        "Query" / WString,
        "User" / WString,
        "processid" / Int32ul,
        "MachineName" / WString,
        "PossibleCause" / WString
    )


@declare(guid=guid("1418ef04-b0b4-4623-bf7e-d74ab47bbdaa"), event_id=5861, version=0)
class Microsoft_Windows_WMI_Activity_5861_0(Etw):
    pattern = Struct(
        "Namespace" / WString,
        "ESS" / WString,
        "CONSUMER" / WString,
        "PossibleCause" / WString
    )

