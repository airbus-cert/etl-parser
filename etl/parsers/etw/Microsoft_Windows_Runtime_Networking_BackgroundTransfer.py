# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Runtime-Networking-BackgroundTransfer
GUID : b9d5b35d-bbb8-4625-9450-f71a5d414f4f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=1, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_1_0(Etw):
    pattern = Struct(
        "OperationId" / Guid,
        "TransferType" / Int32ul,
        "Method" / WString,
        "URI" / WString,
        "CostPolicy" / Int32ul,
        "Group" / WString,
        "CompletionGroupId" / Guid
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=2, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_2_0(Etw):
    pattern = Struct(
        "OperationId" / Guid,
        "TransferType" / Int32ul,
        "Method" / WString,
        "URI" / WString,
        "CostPolicy" / Int32ul,
        "Group" / WString,
        "CompletionGroupId" / Guid
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=3, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_3_0(Etw):
    pattern = Struct(
        "OperationId" / Guid,
        "TransferType" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=4, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_4_0(Etw):
    pattern = Struct(
        "OperationId" / Guid,
        "LocationId" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=5, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_5_0(Etw):
    pattern = Struct(
        "LocationId" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=6, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_6_0(Etw):
    pattern = Struct(
        "OperationId" / Guid,
        "LocationId" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=7, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_7_0(Etw):
    pattern = Struct(
        "LocationId" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=8, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_8_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "OperationId" / Guid,
        "LocationId" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=9, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_9_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "OperationId" / Guid,
        "LocationId" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=10, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_10_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "PowerPolicyValue" / Int32ul,
        "PromptLogicValue" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=11, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_11_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=12, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_12_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=13, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_13_0(Etw):
    pattern = Struct(
        "OperationId" / Guid,
        "CostPolicy" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=14, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_14_0(Etw):
    pattern = Struct(
        "OperationId" / Guid,
        "Priority" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=15, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_15_0(Etw):
    pattern = Struct(
        "IsInternetAvailable" / Int8ul,
        "CostType" / Int32ul,
        "IsRoaming" / Int8ul,
        "IsOverDataLimit" / Int8ul,
        "DataLimitMegabytes" / Int32ul,
        "UsedMegabytes" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=16, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_16_0(Etw):
    pattern = Struct(
        "OperationId" / Guid,
        "IsResume" / Int8ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=17, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_17_0(Etw):
    pattern = Struct(
        "GroupName" / WString,
        "LocationId" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=18, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_18_0(Etw):
    pattern = Struct(
        "GroupName" / WString,
        "Behavior" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=19, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_19_0(Etw):
    pattern = Struct(
        "NotificationId" / Guid,
        "LocationId" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=20, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_20_0(Etw):
    pattern = Struct(
        "NotificationId" / Guid,
        "LocationId" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=21, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_21_0(Etw):
    pattern = Struct(
        "OperationId" / Guid,
        "NotificationId" / Guid
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=22, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_22_0(Etw):
    pattern = Struct(
        "NotificationId" / Guid,
        "LocationId" / Int32ul,
        "NotificationType" / Int32ul,
        "NotificationInformationAvailable" / Int8ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=23, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_23_0(Etw):
    pattern = Struct(
        "OperationId" / Guid,
        "ElapsedTimeInSeconds" / Int32ul,
        "TotalBytesRemaining" / Int64ul,
        "TransferSpeedInBytesPerSeconds" / Int64ul,
        "EtaInSeconds" / Int64ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=24, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_24_0(Etw):
    pattern = Struct(
        "CompletionGroupId" / Guid,
        "LocationId" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=25, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_25_0(Etw):
    pattern = Struct(
        "CompletionGroupId" / Guid,
        "LocationId" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=26, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_26_0(Etw):
    pattern = Struct(
        "CompletionGroupId" / Guid,
        "TriggerId" / Guid,
        "Error" / Int32ul,
        "ActivationStatus" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=27, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_27_0(Etw):
    pattern = Struct(
        "CompletionGroupId" / Guid,
        "TriggerId" / Guid,
        "Error" / Int32ul,
        "ActivationStatus" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=28, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_28_0(Etw):
    pattern = Struct(
        "CompletionGroupId" / Guid,
        "TriggerId" / Guid
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=30, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_30_0(Etw):
    pattern = Struct(
        "CompletionGroupId" / Guid,
        "TriggerId" / Guid,
        "Error" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=31, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_31_0(Etw):
    pattern = Struct(
        "OldOperationId" / Guid,
        "NewOperationId" / Guid
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=32, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_32_0(Etw):
    pattern = Struct(
        "CompletionGroupId" / Guid,
        "RunningOperationsCount" / Int32ul,
        "CopiedOperationsCount" / Int32ul
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=33, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_33_0(Etw):
    pattern = Struct(
        "OperationId" / Guid,
        "LocationId" / Int32ul,
        "Path" / WString
    )


@declare(guid=guid("b9d5b35d-bbb8-4625-9450-f71a5d414f4f"), event_id=34, version=0)
class Microsoft_Windows_Runtime_Networking_BackgroundTransfer_34_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "OperationId" / Guid,
        "Progress" / Int32ul
    )

