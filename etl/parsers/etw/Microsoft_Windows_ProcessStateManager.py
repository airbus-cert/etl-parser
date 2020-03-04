# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ProcessStateManager
GUID : d49918cf-9489-4bf1-9d7b-014d864cf71f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d49918cf-9489-4bf1-9d7b-014d864cf71f"), event_id=1, version=0)
class Microsoft_Windows_ProcessStateManager_1_0(Etw):
    pattern = Struct(
        "ApplicationId" / Int64ul,
        "SessionId" / Int32ul,
        "PsmKey" / WString,
        "OldState" / Int32ul,
        "NewState" / Int32ul,
        "MixedWorkItems" / Int32ul,
        "PureWorkItems" / Int32ul,
        "SystemWorkItems" / Int32ul,
        "Flags" / Int32ul,
        "CycleTime" / Int64ul,
        "NetworkTokens" / Int64ul
    )


@declare(guid=guid("d49918cf-9489-4bf1-9d7b-014d864cf71f"), event_id=2, version=0)
class Microsoft_Windows_ProcessStateManager_2_0(Etw):
    pattern = Struct(
        "ApplicationId" / Int64ul,
        "SessionId" / Int32ul,
        "PsmKey" / WString,
        "Flags" / Int32ul,
        "CycleTime" / Int64ul,
        "NetworkTokens" / Int64ul
    )


@declare(guid=guid("d49918cf-9489-4bf1-9d7b-014d864cf71f"), event_id=3, version=0)
class Microsoft_Windows_ProcessStateManager_3_0(Etw):
    pattern = Struct(
        "ApplicationId" / Int64ul,
        "SessionId" / Int32ul,
        "PsmKey" / WString,
        "Flags" / Int32ul,
        "CycleTime" / Int64ul,
        "NetworkTokens" / Int64ul
    )


@declare(guid=guid("d49918cf-9489-4bf1-9d7b-014d864cf71f"), event_id=4, version=0)
class Microsoft_Windows_ProcessStateManager_4_0(Etw):
    pattern = Struct(
        "ApplicationId" / Int64ul,
        "SessionId" / Int32ul,
        "PsmKey" / WString,
        "PlmRequestedPriority" / Int32ul,
        "EffectivePriority" / Int32ul
    )


@declare(guid=guid("d49918cf-9489-4bf1-9d7b-014d864cf71f"), event_id=100, version=0)
class Microsoft_Windows_ProcessStateManager_100_0(Etw):
    pattern = Struct(
        "ApplicationId" / Int64ul,
        "SessionId" / Int32ul,
        "PsmKey" / WString,
        "OldState" / Int32ul,
        "NewState" / Int32ul,
        "MixedWorkItems" / Int32ul,
        "PureWorkItems" / Int32ul,
        "SystemWorkItems" / Int32ul,
        "Flags" / Int32ul,
        "CycleTime" / Int64ul,
        "NetworkTokens" / Int64ul
    )


@declare(guid=guid("d49918cf-9489-4bf1-9d7b-014d864cf71f"), event_id=101, version=0)
class Microsoft_Windows_ProcessStateManager_101_0(Etw):
    pattern = Struct(
        "ApplicationId" / Int64ul,
        "SessionId" / Int32ul,
        "PsmKey" / WString,
        "PlmRequestedPriority" / Int32ul,
        "EffectivePriority" / Int32ul
    )


@declare(guid=guid("d49918cf-9489-4bf1-9d7b-014d864cf71f"), event_id=102, version=0)
class Microsoft_Windows_ProcessStateManager_102_0(Etw):
    pattern = Struct(
        "ApplicationId" / Int64ul,
        "SessionId" / Int32ul,
        "PsmKey" / WString,
        "State" / Int32ul,
        "Flags" / Int32ul,
        "PlmRequestedPriority" / Int32ul,
        "EffectivePriority" / Int32ul,
        "CycleTime" / Int64ul,
        "NetworkTokens" / Int64ul
    )


@declare(guid=guid("d49918cf-9489-4bf1-9d7b-014d864cf71f"), event_id=103, version=0)
class Microsoft_Windows_ProcessStateManager_103_0(Etw):
    pattern = Struct(
        "ApplicationId" / Int64ul,
        "SessionId" / Int32ul,
        "PsmKey" / WString,
        "ActivationFlags" / Int32ul,
        "HostId" / Int64ul
    )

