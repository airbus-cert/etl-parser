# -*- coding: utf-8 -*-
"""
Microsoft-Windows-BrokerInfrastructure
GUID : e6835967-e0d2-41fb-bcec-58387404e25a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=1, version=0)
class Microsoft_Windows_BrokerInfrastructure_1_0(Etw):
    pattern = Struct(
        "EntryPointLength" / Int16ul,
        "TaskEntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "NameLength" / Int16ul,
        "TaskName" / Bytes(lambda this: this.NameLength),
        "SessionId" / Int32ul,
        "InstanceId" / Guid,
        "ApplicationId" / Int64ul,
        "PsmActivationType" / Int32ul,
        "CriticalActivation" / Int8ul,
        "TriggerEventId" / Guid,
        "TriggerEventType" / Int32ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=1, version=1)
class Microsoft_Windows_BrokerInfrastructure_1_1(Etw):
    pattern = Struct(
        "EntryPointLength" / Int16ul,
        "TaskEntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "NameLength" / Int16ul,
        "TaskName" / Bytes(lambda this: this.NameLength),
        "UserContextId" / Int64ul,
        "InstanceId" / Guid,
        "ApplicationId" / Int64ul,
        "PsmActivationType" / Int32ul,
        "CriticalActivation" / Int8ul,
        "TriggerEventId" / Guid,
        "TriggerEventType" / Int32ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=2, version=0)
class Microsoft_Windows_BrokerInfrastructure_2_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "BrokerId" / Guid,
        "SessionId" / Int32ul,
        "TaskExecuted" / Int8ul,
        "Result" / Int32ul,
        "UserSid" / Sid,
        "PackageFullName" / WString,
        "EntryPointLength" / Int16ul,
        "EntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "ApplicationId" / Int64ul,
        "CpuThrottleCount" / Int16ul,
        "NetThrottleCount" / Int16ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=2, version=1)
class Microsoft_Windows_BrokerInfrastructure_2_1(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "BrokerId" / Guid,
        "SessionId" / Int32ul,
        "TaskExecuted" / Int8ul,
        "Result" / Int32ul,
        "UserSid" / Sid,
        "PackageFullName" / WString,
        "EntryPointLength" / Int16ul,
        "EntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "ApplicationId" / Int64ul,
        "CpuThrottleCount" / Int16ul,
        "NetThrottleCount" / Int16ul,
        "WatchdogDuration" / Int32ul,
        "WatchdogIteration" / Int32ul,
        "Flags" / Int16ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=2, version=2)
class Microsoft_Windows_BrokerInfrastructure_2_2(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "BrokerId" / Guid,
        "SessionId" / Int32ul,
        "TaskExecuted" / Int8ul,
        "Result" / Int32ul,
        "UserSid" / Sid,
        "PackageFullName" / WString,
        "EntryPointLength" / Int16ul,
        "EntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "ApplicationId" / Int64ul,
        "CpuThrottleCount" / Int16ul,
        "NetThrottleCount" / Int16ul,
        "Flags" / Int16ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=2, version=3)
class Microsoft_Windows_BrokerInfrastructure_2_3(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "BrokerId" / Guid,
        "UserContextId" / Int64ul,
        "TaskExecuted" / Int8ul,
        "Result" / Int32ul,
        "UserSid" / Sid,
        "PackageFullName" / WString,
        "EntryPointLength" / Int16ul,
        "EntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "ApplicationId" / Int64ul,
        "CpuThrottleCount" / Int16ul,
        "NetThrottleCount" / Int16ul,
        "Flags" / Int16ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=3, version=0)
class Microsoft_Windows_BrokerInfrastructure_3_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "BrokerId" / Guid,
        "StateName" / Int64ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=4, version=0)
class Microsoft_Windows_BrokerInfrastructure_4_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "EntryPointLength" / Int16ul,
        "EntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "UserSid" / Sid
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=4, version=1)
class Microsoft_Windows_BrokerInfrastructure_4_1(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "EntryPointLength" / Int16ul,
        "EntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "UserSid" / Sid
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=5, version=0)
class Microsoft_Windows_BrokerInfrastructure_5_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "EntryPointLength" / Int16ul,
        "EntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "UserSid" / Sid
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=5, version=1)
class Microsoft_Windows_BrokerInfrastructure_5_1(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "EntryPointLength" / Int16ul,
        "EntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "UserSid" / Sid
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=6, version=0)
class Microsoft_Windows_BrokerInfrastructure_6_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "EntryPointLength" / Int16ul,
        "EntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "UserSid" / Sid
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=7, version=0)
class Microsoft_Windows_BrokerInfrastructure_7_0(Etw):
    pattern = Struct(
        "EventId" / Guid,
        "EventType" / Int32ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=8, version=0)
class Microsoft_Windows_BrokerInfrastructure_8_0(Etw):
    pattern = Struct(
        "EventId" / Guid,
        "EventType" / Int32ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=9, version=0)
class Microsoft_Windows_BrokerInfrastructure_9_0(Etw):
    pattern = Struct(
        "EventId" / Guid,
        "EventType" / Int32ul,
        "OldState" / Int32ul,
        "NewState" / Int8ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=10, version=0)
class Microsoft_Windows_BrokerInfrastructure_10_0(Etw):
    pattern = Struct(
        "EventId" / Guid,
        "EventType" / Int32ul,
        "OldState" / Int32ul,
        "NewState" / Int8ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=11, version=0)
class Microsoft_Windows_BrokerInfrastructure_11_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "UserAccountName" / WString,
        "SessionId" / Int32ul,
        "PackageState" / Int32ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=11, version=1)
class Microsoft_Windows_BrokerInfrastructure_11_1(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "UserAccountName" / WString,
        "UserContextId" / Int64ul,
        "PackageState" / Int32ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=12, version=0)
class Microsoft_Windows_BrokerInfrastructure_12_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "UserAccountName" / WString,
        "SessionId" / Int32ul,
        "PackageState" / Int32ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=12, version=1)
class Microsoft_Windows_BrokerInfrastructure_12_1(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "UserAccountName" / WString,
        "UserContextId" / Int64ul,
        "PackageState" / Int32ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=13, version=0)
class Microsoft_Windows_BrokerInfrastructure_13_0(Etw):
    pattern = Struct(
        "EntryPointLength" / Int16ul,
        "TaskEntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "NameLength" / Int16ul,
        "TaskName" / Bytes(lambda this: this.NameLength),
        "ConditionType" / Int32ul,
        "ConditionValue" / Int32ul,
        "ConditionDesiredValue" / Int8ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=14, version=0)
class Microsoft_Windows_BrokerInfrastructure_14_0(Etw):
    pattern = Struct(
        "EntryPointLength" / Int16ul,
        "TaskEntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "NameLength" / Int16ul,
        "TaskName" / Bytes(lambda this: this.NameLength)
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=15, version=0)
class Microsoft_Windows_BrokerInfrastructure_15_0(Etw):
    pattern = Struct(
        "EntryPointLength" / Int16ul,
        "TaskEntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "NameLength" / Int16ul,
        "TaskName" / Bytes(lambda this: this.NameLength)
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=16, version=0)
class Microsoft_Windows_BrokerInfrastructure_16_0(Etw):
    pattern = Struct(
        "EntryPointLength" / Int16ul,
        "TaskEntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "NameLength" / Int16ul,
        "TaskName" / Bytes(lambda this: this.NameLength)
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=17, version=0)
class Microsoft_Windows_BrokerInfrastructure_17_0(Etw):
    pattern = Struct(
        "EntryPointLength" / Int16ul,
        "TaskEntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "NameLength" / Int16ul,
        "TaskName" / Bytes(lambda this: this.NameLength),
        "BufferingReason" / Int32ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=18, version=0)
class Microsoft_Windows_BrokerInfrastructure_18_0(Etw):
    pattern = Struct(
        "EntryPointLength" / Int16ul,
        "TaskEntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "NameLength" / Int16ul,
        "TaskName" / Bytes(lambda this: this.NameLength),
        "BufferingReason" / Int32ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=19, version=0)
class Microsoft_Windows_BrokerInfrastructure_19_0(Etw):
    pattern = Struct(
        "EntryPointLength" / Int16ul,
        "TaskEntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "NameLength" / Int16ul,
        "TaskName" / Bytes(lambda this: this.NameLength),
        "InstanceId" / Guid,
        "SessionId" / Int32ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=19, version=1)
class Microsoft_Windows_BrokerInfrastructure_19_1(Etw):
    pattern = Struct(
        "EntryPointLength" / Int16ul,
        "TaskEntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "NameLength" / Int16ul,
        "TaskName" / Bytes(lambda this: this.NameLength),
        "InstanceId" / Guid,
        "UserContextId" / Int64ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=20, version=0)
class Microsoft_Windows_BrokerInfrastructure_20_0(Etw):
    pattern = Struct(
        "EntryPointLength" / Int16ul,
        "TaskEntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "NameLength" / Int16ul,
        "TaskName" / Bytes(lambda this: this.NameLength),
        "DeletionReason" / Int32ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=21, version=0)
class Microsoft_Windows_BrokerInfrastructure_21_0(Etw):
    pattern = Struct(
        "EntryPointLength" / Int16ul,
        "TaskEntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "NameLength" / Int16ul,
        "TaskName" / Bytes(lambda this: this.NameLength),
        "Result" / Int32ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=22, version=0)
class Microsoft_Windows_BrokerInfrastructure_22_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "ApplicationId" / Int64ul,
        "SessionId" / Int32ul,
        "PsmActivationType" / Int32ul,
        "CpuThrottleCount" / Int16ul,
        "NetThrottleCount" / Int16ul,
        "PackageFullName" / WString
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=22, version=1)
class Microsoft_Windows_BrokerInfrastructure_22_1(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "ApplicationId" / Int64ul,
        "UserContextId" / Int64ul,
        "PsmActivationType" / Int32ul,
        "CpuThrottleCount" / Int16ul,
        "NetThrottleCount" / Int16ul,
        "PackageFullName" / WString
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=23, version=0)
class Microsoft_Windows_BrokerInfrastructure_23_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "BrokerId" / Guid,
        "TriggerEventId" / Guid,
        "TriggerEventType" / Int32ul,
        "CriticalActivation" / Int8ul,
        "EntryPointLength" / Int16ul,
        "EntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "NameLength" / Int16ul,
        "TaskName" / Bytes(lambda this: this.NameLength),
        "PackageFullName" / WString,
        "UserSid" / Sid,
        "ConditionCount" / Int16ul,
        "ConditinalEvent" / Int8ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=23, version=1)
class Microsoft_Windows_BrokerInfrastructure_23_1(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "BrokerId" / Guid,
        "TriggerEventId" / Guid,
        "TriggerEventType" / Int32ul,
        "CriticalActivation" / Int8ul,
        "EntryPointLength" / Int16ul,
        "EntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "NameLength" / Int16ul,
        "TaskName" / Bytes(lambda this: this.NameLength),
        "PackageFullName" / WString,
        "UserSid" / Sid,
        "ConditionCount" / Int16ul,
        "ConditinalEvent" / Int8ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=24, version=0)
class Microsoft_Windows_BrokerInfrastructure_24_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "StateFlags" / Int32ul,
        "ActiveTaskCount" / Int32ul,
        "LockScreen" / Int8ul,
        "PackageFullName" / WString,
        "UserSid" / Sid
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=24, version=1)
class Microsoft_Windows_BrokerInfrastructure_24_1(Etw):
    pattern = Struct(
        "UserContextId" / Int64ul,
        "StateFlags" / Int32ul,
        "ActiveTaskCount" / Int32ul,
        "LockScreen" / Int8ul,
        "PackageFullName" / WString,
        "UserSid" / Sid
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=25, version=0)
class Microsoft_Windows_BrokerInfrastructure_25_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "StateFlags" / Int32ul,
        "ActiveTaskCount" / Int32ul,
        "LockScreen" / Int8ul,
        "PackageFullName" / WString,
        "UserSid" / Sid,
        "ActiveTasks" / WString
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=26, version=0)
class Microsoft_Windows_BrokerInfrastructure_26_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul,
        "Iteration" / Int32ul,
        "ActivitySummary" / Int32ul,
        "ActivityFilter" / Int32ul,
        "HangDetected" / Int8ul,
        "EventType" / Int32ul,
        "PackageFullName" / WString,
        "EntryPoint" / WString,
        "InstanceId" / Guid,
        "CycleTime" / Int64ul,
        "NetTokens" / Int64ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=26, version=1)
class Microsoft_Windows_BrokerInfrastructure_26_1(Etw):
    pattern = Struct(
        "Duration" / Int32ul,
        "Iteration" / Int32ul,
        "ActivitySummary" / Int32ul,
        "ActivityFilter" / Int32ul,
        "HangDetected" / Int8ul,
        "EventType" / Int32ul,
        "PackageFullName" / WString,
        "EntryPoint" / WString,
        "InstanceId" / Guid,
        "CycleTime" / Int64ul,
        "NetTokens" / Int64ul,
        "PolicyVersion" / Int8ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=27, version=0)
class Microsoft_Windows_BrokerInfrastructure_27_0(Etw):
    pattern = Struct(
        "EntryPointLength" / Int16ul,
        "TaskEntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "NameLength" / Int16ul,
        "TaskName" / Bytes(lambda this: this.NameLength),
        "PackageFullName" / WString,
        "InstanceId" / Guid,
        "SessionId" / Int32ul,
        "UserSid" / Sid,
        "LockScreen" / Int8ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=27, version=1)
class Microsoft_Windows_BrokerInfrastructure_27_1(Etw):
    pattern = Struct(
        "EntryPointLength" / Int16ul,
        "TaskEntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "NameLength" / Int16ul,
        "TaskName" / Bytes(lambda this: this.NameLength),
        "PackageFullName" / WString,
        "InstanceId" / Guid,
        "SessionId" / Int32ul,
        "UserSid" / Sid,
        "LockScreen" / Int8ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=27, version=2)
class Microsoft_Windows_BrokerInfrastructure_27_2(Etw):
    pattern = Struct(
        "EntryPointLength" / Int16ul,
        "TaskEntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "NameLength" / Int16ul,
        "TaskName" / Bytes(lambda this: this.NameLength),
        "PackageFullName" / WString,
        "InstanceId" / Guid,
        "UserContextId" / Int64ul,
        "UserSid" / Sid,
        "LockScreen" / Int8ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=28, version=0)
class Microsoft_Windows_BrokerInfrastructure_28_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "TransitionId" / Int32ul,
        "Transition" / Int32ul
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=100, version=0)
class Microsoft_Windows_BrokerInfrastructure_100_0(Etw):
    pattern = Struct(
        "ElapsedTime" / Int32ul,
        "TaskThrottleCount" / Int32ul,
        "EventType" / Int32ul,
        "PackageFullName" / WString,
        "EntryPoint" / WString
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=101, version=0)
class Microsoft_Windows_BrokerInfrastructure_101_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul,
        "ActivitySummary" / Int32ul,
        "EventTypeAndBitfield" / Int32ul,
        "PackageFullName" / WString,
        "EntryPoint" / WString
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=200, version=0)
class Microsoft_Windows_BrokerInfrastructure_200_0(Etw):
    pattern = Struct(
        "ActivityType" / Int32ul,
        "PackageFullName" / WString,
        "NameLength" / Int16ul,
        "TaskName" / Bytes(lambda this: this.NameLength)
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=201, version=0)
class Microsoft_Windows_BrokerInfrastructure_201_0(Etw):
    pattern = Struct(
        "ActivityType" / Int32ul,
        "PackageFullName" / WString,
        "NameLength" / Int16ul,
        "TaskName" / Bytes(lambda this: this.NameLength)
    )


@declare(guid=guid("e6835967-e0d2-41fb-bcec-58387404e25a"), event_id=300, version=0)
class Microsoft_Windows_BrokerInfrastructure_300_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "EntryPointLength" / Int16ul,
        "EntryPoint" / Bytes(lambda this: this.EntryPointLength),
        "NameLength" / Int16ul,
        "TaskName" / Bytes(lambda this: this.NameLength),
        "PackageFullName" / WString,
        "UserSid" / Sid,
        "TriggerEventType" / Int32ul,
        "ScenarioInstanceId" / Int16ul,
        "AlwaysAllowed" / Int8ul,
        "VoipApp" / Int8ul
    )

