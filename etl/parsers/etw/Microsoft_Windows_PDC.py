# -*- coding: utf-8 -*-
"""
Microsoft-Windows-PDC
GUID : a6bf0deb-3659-40ad-9f81-e25af62ce3c7
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=1, version=0)
class Microsoft_Windows_PDC_1_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "PdcId" / Int32ul,
        "Status" / Int32ul,
        "ClientNameLength" / Int32ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength)
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=2, version=0)
class Microsoft_Windows_PDC_2_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "PdcId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=3, version=0)
class Microsoft_Windows_PDC_3_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "PdcId" / Int32ul,
        "Status" / Int32ul,
        "ClientNameLength" / Int32ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength)
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=4, version=0)
class Microsoft_Windows_PDC_4_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "PdcId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=5, version=0)
class Microsoft_Windows_PDC_5_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "PdcId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=6, version=0)
class Microsoft_Windows_PDC_6_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "PdcId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=7, version=0)
class Microsoft_Windows_PDC_7_0(Etw):
    pattern = Struct(
        "Message" / Int64ul,
        "StatusActive" / Int32ul,
        "ActivityType" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=8, version=0)
class Microsoft_Windows_PDC_8_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=9, version=0)
class Microsoft_Windows_PDC_9_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "State" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=10, version=0)
class Microsoft_Windows_PDC_10_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "ClientContext" / Int64ul,
        "PdcSequence" / Int32ul,
        "Value" / Int32ul,
        "WaitTime" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=11, version=0)
class Microsoft_Windows_PDC_11_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=12, version=0)
class Microsoft_Windows_PDC_12_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "AssumedPdcSequence" / Int32ul,
        "ReceivedPdcSequence" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=13, version=0)
class Microsoft_Windows_PDC_13_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "PdcSequence" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=14, version=0)
class Microsoft_Windows_PDC_14_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=15, version=0)
class Microsoft_Windows_PDC_15_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=16, version=0)
class Microsoft_Windows_PDC_16_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "Message" / Int64ul,
        "Control" / Int32ul,
        "Status" / Int32ul,
        "PdcSequence" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=17, version=0)
class Microsoft_Windows_PDC_17_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "SendReceive" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=18, version=0)
class Microsoft_Windows_PDC_18_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "SendReceive" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=19, version=0)
class Microsoft_Windows_PDC_19_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "Port" / Int64ul,
        "ResiliencyType" / Int32ul,
        "References" / Int64ul,
        "TransactionId" / Int32ul,
        "CurrentState" / Int32ul,
        "NextState" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=20, version=0)
class Microsoft_Windows_PDC_20_0(Etw):
    pattern = Struct(
        "Message" / Int64ul,
        "TransactionId" / Int32ul,
        "ClientState" / Int32ul,
        "ClientStatus" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=21, version=0)
class Microsoft_Windows_PDC_21_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "SendReceive" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=22, version=0)
class Microsoft_Windows_PDC_22_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "SendReceive" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=23, version=0)
class Microsoft_Windows_PDC_23_0(Etw):
    pattern = Struct(
        "ActivatorToken" / Int64ul,
        "Client" / Int64ul,
        "ReferenceDereference" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=24, version=0)
class Microsoft_Windows_PDC_24_0(Etw):
    pattern = Struct(
        "ActivatorToken" / Int64ul,
        "Client" / Int64ul,
        "ReferenceDereference" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=25, version=0)
class Microsoft_Windows_PDC_25_0(Etw):
    pattern = Struct(
        "Phase" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=26, version=0)
class Microsoft_Windows_PDC_26_0(Etw):
    pattern = Struct(
        "Phase" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=27, version=0)
class Microsoft_Windows_PDC_27_0(Etw):
    pattern = Struct(
        "On" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=28, version=0)
class Microsoft_Windows_PDC_28_0(Etw):
    pattern = Struct(
        "On" / Int32ul,
        "Console" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=29, version=0)
class Microsoft_Windows_PDC_29_0(Etw):
    pattern = Struct(
        "At" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=30, version=0)
class Microsoft_Windows_PDC_30_0(Etw):
    pattern = Struct(
        "ConnectedSessionCount" / Int32ul,
        "ConsoleSessionId" / Int32ul,
        "SessionId" / Int32ul,
        "OnRequestCurrent" / Int32ul,
        "OnRequestProcessed" / Int32ul,
        "OffRequestCurrent" / Int32ul,
        "OffRequestProcessed" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=30, version=1)
class Microsoft_Windows_PDC_30_1(Etw):
    pattern = Struct(
        "ConnectedSessionCount" / Int32ul,
        "ConsoleSessionId" / Int32ul,
        "SessionId" / Int32ul,
        "OnRequestCurrent" / Int32ul,
        "OnRequestProcessed" / Int32ul,
        "OffRequestCurrent" / Int32ul,
        "OffRequestProcessed" / Int32ul,
        "BlockingActive" / Int8ul,
        "BlockingScenarioCount" / Int32ul,
        "BlockingEscapeCount" / Int32ul,
        "BlockingPowerPressCount" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=31, version=0)
class Microsoft_Windows_PDC_31_0(Etw):
    pattern = Struct(
        "At" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=36, version=0)
class Microsoft_Windows_PDC_36_0(Etw):
    pattern = Struct(
        "At" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=39, version=0)
class Microsoft_Windows_PDC_39_0(Etw):
    pattern = Struct(
        "Suspend" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=40, version=0)
class Microsoft_Windows_PDC_40_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Console" / Int32ul,
        "Connected" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=42, version=0)
class Microsoft_Windows_PDC_42_0(Etw):
    pattern = Struct(
        "AoAc" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=43, version=0)
class Microsoft_Windows_PDC_43_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Session" / Int32ul,
        "Client" / Int64ul,
        "PdcId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=44, version=0)
class Microsoft_Windows_PDC_44_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Session" / Int32ul,
        "Client" / Int64ul,
        "PdcId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=45, version=0)
class Microsoft_Windows_PDC_45_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "SendReceive" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=46, version=0)
class Microsoft_Windows_PDC_46_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "SendReceive" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=47, version=0)
class Microsoft_Windows_PDC_47_0(Etw):
    pattern = Struct(
        "Message" / Int64ul,
        "TransactionId" / Int32ul,
        "PowerEvent" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=56, version=0)
class Microsoft_Windows_PDC_56_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=57, version=0)
class Microsoft_Windows_PDC_57_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Session" / Int32ul,
        "Iteration" / Int32ul,
        "ClientContext" / Int64ul,
        "PdcSequence" / Int32ul,
        "Value" / Int32ul,
        "WaitTime" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=58, version=0)
class Microsoft_Windows_PDC_58_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "PdcSequence" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=59, version=0)
class Microsoft_Windows_PDC_59_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "AssumedPdcSequence" / Int32ul,
        "ReceivedPdcSequence" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=60, version=0)
class Microsoft_Windows_PDC_60_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=61, version=0)
class Microsoft_Windows_PDC_61_0(Etw):
    pattern = Struct(
        "Session" / Int32ul,
        "Suspend" / Int32ul,
        "AppsSvcs" / Int32ul,
        "User" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=63, version=0)
class Microsoft_Windows_PDC_63_0(Etw):
    pattern = Struct(
        "DisableInputToPLMEntry" / Int32ul,
        "DisableInputToDAMEntry" / Int32ul,
        "DisableInputToLowPowerEpochEntry" / Int32ul,
        "PhaseTimesConnection" / Int32ul,
        "PhaseTimesPresence" / Int32ul,
        "PhaseTimesPlmAndResiliencyNotification" / Int32ul,
        "PhaseTimesMaintenance" / Int32ul,
        "PhaseTimesDamAndLowPower" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=64, version=0)
class Microsoft_Windows_PDC_64_0(Etw):
    pattern = Struct(
        "ExitReason" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=65, version=0)
class Microsoft_Windows_PDC_65_0(Etw):
    pattern = Struct(
        "ResiliencyExitToLowPowerEpochEntry" / Int32ul,
        "ResiliencyExitToDAMEntry" / Int32ul,
        "ResiliencyExitToPLMEntry" / Int32ul,
        "PhaseTimesResiliencyAndResiliencyNotification" / Int32ul,
        "PhaseTimesLowPowerAndDam" / Int32ul,
        "PhaseTimesPlmAndPresence" / Int32ul,
        "PhaseTimesConnectionAndMaintenanceAndScreenOn" / Int32ul,
        "CsDuration" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=68, version=0)
class Microsoft_Windows_PDC_68_0(Etw):
    pattern = Struct(
        "NewState" / Int32ul,
        "OldState" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=69, version=0)
class Microsoft_Windows_PDC_69_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=71, version=0)
class Microsoft_Windows_PDC_71_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "PdcId" / Int32ul,
        "ResiliencyClientCount" / Int32ul,
        "ResiliencyContext" / Int16ul,
        "ClientNameLength" / Int32ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength)
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=72, version=0)
class Microsoft_Windows_PDC_72_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "PdcId" / Int32ul,
        "Type" / Int32ul,
        "ClientNameLength" / Int32ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength)
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=73, version=0)
class Microsoft_Windows_PDC_73_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "ClientReferences" / Int64ul,
        "CurrentState" / Int32ul,
        "Type" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=75, version=0)
class Microsoft_Windows_PDC_75_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "PdcId" / Int32ul,
        "Status" / Int32ul,
        "ClientNameLength" / Int32ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength)
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=76, version=0)
class Microsoft_Windows_PDC_76_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "PdcId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=77, version=0)
class Microsoft_Windows_PDC_77_0(Etw):
    pattern = Struct(
        "Message" / Int64ul,
        "StatusActive" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=78, version=0)
class Microsoft_Windows_PDC_78_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "SendReceive" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=79, version=0)
class Microsoft_Windows_PDC_79_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "SendReceive" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=80, version=0)
class Microsoft_Windows_PDC_80_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "PdcId" / Int32ul,
        "ReferenceCount" / Int32ul,
        "Status" / Int32ul,
        "ClientNameLength" / Int32ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength)
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=81, version=0)
class Microsoft_Windows_PDC_81_0(Etw):
    pattern = Struct(
        "TaskClient" / Int64ul,
        "At" / Int32ul,
        "ReferenceDereference" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=82, version=0)
class Microsoft_Windows_PDC_82_0(Etw):
    pattern = Struct(
        "TaskClient" / Int64ul,
        "At" / Int32ul,
        "ReferenceDereference" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=83, version=0)
class Microsoft_Windows_PDC_83_0(Etw):
    pattern = Struct(
        "EnterReason" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=85, version=0)
class Microsoft_Windows_PDC_85_0(Etw):
    pattern = Struct(
        "AbortReason" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=87, version=0)
class Microsoft_Windows_PDC_87_0(Etw):
    pattern = Struct(
        "TimeActivated" / Int32ul,
        "ConnectedStandbyTimeAndActivationCount" / Int32ul,
        "ClientIdAndFlags" / Int32ul,
        "MaxActivationDuration" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=88, version=0)
class Microsoft_Windows_PDC_88_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "PdcId" / Int32ul,
        "Status" / Int32ul,
        "ClientNameLength" / Int32ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength)
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=89, version=0)
class Microsoft_Windows_PDC_89_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "PdcId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=90, version=0)
class Microsoft_Windows_PDC_90_0(Etw):
    pattern = Struct(
        "PdcMessage" / Int64ul,
        "Client" / Int64ul,
        "PdcId" / Int32ul,
        "OperationStatus" / Int32ul,
        "Active" / Int8ul,
        "ReferenceCount" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=91, version=0)
class Microsoft_Windows_PDC_91_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "SendReceive" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=92, version=0)
class Microsoft_Windows_PDC_92_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "SendReceive" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=93, version=0)
class Microsoft_Windows_PDC_93_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "PdcId" / Int32ul,
        "Active" / Int8ul,
        "Status" / Int32ul,
        "ClientNameLength" / Int32ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength)
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=94, version=0)
class Microsoft_Windows_PDC_94_0(Etw):
    pattern = Struct(
        "Scenario" / Int64ul,
        "PreviousState" / Int8ul,
        "NextState" / Int8ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=95, version=0)
class Microsoft_Windows_PDC_95_0(Etw):
    pattern = Struct(
        "Scenario" / Int64ul,
        "Type" / Int8ul,
        "ClientIdCount" / Int32ul,
        "ClientIdList" / Int8ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=96, version=0)
class Microsoft_Windows_PDC_96_0(Etw):
    pattern = Struct(
        "ClientId" / Int32ul,
        "TestClient" / Int8ul,
        "ClientNameLength" / Int32ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength)
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=97, version=0)
class Microsoft_Windows_PDC_97_0(Etw):
    pattern = Struct(
        "Scenario" / Int64ul,
        "Guid" / Guid,
        "Flags" / Int32ul,
        "State" / Int8ul,
        "ScenarioNameLength" / Int32ul,
        "ScenarioName" / Bytes(lambda this: this.ScenarioNameLength)
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=97, version=1)
class Microsoft_Windows_PDC_97_1(Etw):
    pattern = Struct(
        "Scenario" / Int64ul,
        "Guid" / Guid,
        "Flags" / Int32ul,
        "State" / Int8ul,
        "ScenarioNameLength" / Int32ul,
        "ScenarioName" / Bytes(lambda this: this.ScenarioNameLength),
        "ProfileGuid" / Guid
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=98, version=0)
class Microsoft_Windows_PDC_98_0(Etw):
    pattern = Struct(
        "Scenario" / Int64ul,
        "DripsTimeInUs" / Int64ul,
        "DripsTranstions" / Int64ul,
        "PlatformIdleTimeInUs" / Int64ul,
        "PlatformIdleTranstions" / Int64ul,
        "StateCount" / Int32ul,
        "States" / Int32sl
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=99, version=0)
class Microsoft_Windows_PDC_99_0(Etw):
    pattern = Struct(
        "PdcId" / Int32ul,
        "PreviousState" / Int8ul,
        "NextState" / Int8ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=100, version=0)
class Microsoft_Windows_PDC_100_0(Etw):
    pattern = Struct(
        "PdcId" / Int32ul,
        "ReferenceCount" / Int32ul,
        "ClientNameLength" / Int32ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength)
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=101, version=0)
class Microsoft_Windows_PDC_101_0(Etw):
    pattern = Struct(
        "DataCount" / Int32ul,
        "Data" / CString
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=102, version=0)
class Microsoft_Windows_PDC_102_0(Etw):
    pattern = Struct(
        "ClientId" / Int32ul,
        "ClientFlags" / Int32ul,
        "ClientNameLength" / Int32ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength)
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=103, version=0)
class Microsoft_Windows_PDC_103_0(Etw):
    pattern = Struct(
        "TimeContinuouslyActive" / Int32ul,
        "ClientIdAndActivityTypeAndOnAc" / Int32ul,
        "UserClientProcess" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=104, version=0)
class Microsoft_Windows_PDC_104_0(Etw):
    pattern = Struct(
        "Scenario" / Int64ul,
        "DripsTimeInUs" / Int64ul,
        "DripsTranstions" / Int64ul,
        "PlatformIdleTimeInUs" / Int64ul,
        "PlatformIdleTranstions" / Int64ul,
        "StateCount" / Int32ul,
        "States" / Int32sl
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=105, version=0)
class Microsoft_Windows_PDC_105_0(Etw):
    pattern = Struct(
        "Scenario" / Int64ul,
        "ActiveCount" / Int64ul,
        "MaxActiveTime" / Int64ul,
        "MinActiveTime" / Int64ul,
        "TotalActiveTime" / Int64ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=106, version=0)
class Microsoft_Windows_PDC_106_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "PdcId" / Int32ul,
        "ProfileGuid" / Guid,
        "Status" / Int32ul,
        "ClientNameLength" / Int32ul,
        "ClientName" / Bytes(lambda this: this.ClientNameLength)
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=107, version=0)
class Microsoft_Windows_PDC_107_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "PdcId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=108, version=0)
class Microsoft_Windows_PDC_108_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "Acquire" / Int8ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=109, version=0)
class Microsoft_Windows_PDC_109_0(Etw):
    pattern = Struct(
        "Client" / Int64ul,
        "Acquire" / Int8ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=110, version=0)
class Microsoft_Windows_PDC_110_0(Etw):
    pattern = Struct(
        "ClientId" / Int32ul,
        "Status" / Int32ul,
        "PdcVersion" / Int32ul,
        "ModuleNameLength" / Int32ul,
        "ModuleName" / Bytes(lambda this: this.ModuleNameLength)
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=111, version=0)
class Microsoft_Windows_PDC_111_0(Etw):
    pattern = Struct(
        "ClientId" / Int32ul,
        "TaskNameLength" / Int32ul,
        "TaskName" / Bytes(lambda this: this.TaskNameLength),
        "SubTaskLength" / Int32ul,
        "SubTaskName" / Bytes(lambda this: this.SubTaskLength),
        "ActivationCount" / Int32ul,
        "ActivationsUpCounter" / Int32ul,
        "ExpectedMaximumDuration" / Int32ul,
        "Status" / Int32ul,
        "ActivationHandle" / Int64ul,
        "PdcVersion" / Int32ul,
        "ModuleNameLength" / Int32ul,
        "ModuleName" / Bytes(lambda this: this.ModuleNameLength)
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=112, version=0)
class Microsoft_Windows_PDC_112_0(Etw):
    pattern = Struct(
        "ClientId" / Int32ul,
        "TaskNameLength" / Int32ul,
        "TaskName" / Bytes(lambda this: this.TaskNameLength),
        "SubTaskLength" / Int32ul,
        "SubTaskName" / Bytes(lambda this: this.SubTaskLength),
        "ExpectedMaximumDuration" / Int32ul,
        "ActivationCount" / Int32ul,
        "ActivationsUpCounter" / Int32ul,
        "ActivationDuration" / Int64ul,
        "RenewalUpCounter" / Int32ul,
        "ErrorDetail" / Int32ul,
        "Status" / Int32ul,
        "ActivationHandle" / Int64ul,
        "ModuleNameLength" / Int32ul,
        "ModuleName" / Bytes(lambda this: this.ModuleNameLength),
        "BrokeredForPID" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=113, version=0)
class Microsoft_Windows_PDC_113_0(Etw):
    pattern = Struct(
        "ClientId" / Int32ul,
        "TaskNameLength" / Int32ul,
        "TaskName" / Bytes(lambda this: this.TaskNameLength),
        "SubTaskLength" / Int32ul,
        "SubTaskName" / Bytes(lambda this: this.SubTaskLength),
        "ActivationCount" / Int32ul,
        "ActivationsUpCounter" / Int32ul,
        "ActivationDuration" / Int64ul,
        "Status" / Int32ul,
        "ActivationHandle" / Int64ul,
        "PdcVersion" / Int32ul,
        "ModuleNameLength" / Int32ul,
        "ModuleName" / Bytes(lambda this: this.ModuleNameLength),
        "BrokeredForPID" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=114, version=0)
class Microsoft_Windows_PDC_114_0(Etw):
    pattern = Struct(
        "ClientId" / Int32ul,
        "Status" / Int32ul,
        "PdcVersion" / Int32ul,
        "ModuleNameLength" / Int32ul,
        "ModuleName" / Bytes(lambda this: this.ModuleNameLength)
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=115, version=0)
class Microsoft_Windows_PDC_115_0(Etw):
    pattern = Struct(
        "ClientId" / Int32ul,
        "TaskNameLength" / Int32ul,
        "TaskName" / Bytes(lambda this: this.TaskNameLength),
        "SubTaskLength" / Int32ul,
        "SubTaskName" / Bytes(lambda this: this.SubTaskLength),
        "CallbackReason" / Int32ul,
        "ActivationCount" / Int32ul,
        "ActivationsUpCounter" / Int32ul,
        "ActivationDuration" / Int64ul,
        "Status" / Int32ul,
        "ActivationHandle" / Int64ul,
        "RenewalUpCounter" / Int32ul,
        "PdcVersion" / Int32ul,
        "ModuleNameLength" / Int32ul,
        "ModuleName" / Bytes(lambda this: this.ModuleNameLength),
        "BrokeredForPID" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=116, version=0)
class Microsoft_Windows_PDC_116_0(Etw):
    pattern = Struct(
        "ClientId" / Int32ul,
        "TaskNameLength" / Int32ul,
        "TaskName" / Bytes(lambda this: this.TaskNameLength),
        "SubTaskLength" / Int32ul,
        "SubTaskName" / Bytes(lambda this: this.SubTaskLength),
        "ExpectedMaximumDuration" / Int32ul,
        "ActivationCount" / Int32ul,
        "ActivationsUpCounter" / Int32ul,
        "ActivationDuration" / Int64ul,
        "RenewalUpCounter" / Int32ul,
        "BrokeredForPID" / Int32ul,
        "Status" / Int32ul,
        "ActivationHandle" / Int64ul,
        "ModuleNameLength" / Int32ul,
        "ModuleName" / Bytes(lambda this: this.ModuleNameLength)
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=117, version=0)
class Microsoft_Windows_PDC_117_0(Etw):
    pattern = Struct(
        "ScenarioInstanceId" / Int8ul,
        "RequestType" / Int32ul,
        "Reason" / Int32ul,
        "ClassId" / Guid,
        "ProviderId" / Guid,
        "DiagStringLength" / Int32ul,
        "DiagString" / Bytes(lambda this: this.DiagStringLength)
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=118, version=0)
class Microsoft_Windows_PDC_118_0(Etw):
    pattern = Struct(
        "ScenarioInstanceId" / Int8ul,
        "RequestType" / Int32ul,
        "Reason" / Int32ul,
        "ClassId" / Guid,
        "ProviderId" / Guid,
        "DiagStringLength" / Int32ul,
        "DiagString" / Bytes(lambda this: this.DiagStringLength)
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=119, version=0)
class Microsoft_Windows_PDC_119_0(Etw):
    pattern = Struct(
        "Phase" / Int8ul,
        "CountChange" / Int32sl,
        "ReferenceCount" / Int32sl,
        "WasWorkItemQueued" / Int8ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=120, version=0)
class Microsoft_Windows_PDC_120_0(Etw):
    pattern = Struct(
        "Phase" / Int8ul,
        "CountChange" / Int32sl,
        "ReferenceCount" / Int32sl,
        "WasWorkItemQueued" / Int8ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=121, version=0)
class Microsoft_Windows_PDC_121_0(Etw):
    pattern = Struct(
        "PreviousTargetPhase" / Int8ul,
        "NewTargetPhase" / Int8ul,
        "CurrentPhase" / Int8ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=122, version=0)
class Microsoft_Windows_PDC_122_0(Etw):
    pattern = Struct(
        "Phase" / Int8ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=123, version=0)
class Microsoft_Windows_PDC_123_0(Etw):
    pattern = Struct(
        "Phase" / Int8ul,
        "PreviousState" / Int8ul,
        "NewState" / Int8ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=124, version=0)
class Microsoft_Windows_PDC_124_0(Etw):
    pattern = Struct(
        "Phase" / Int8ul,
        "ReferenceCount" / Int32sl,
        "IsHandlerEngaged" / Int8ul,
        "NotificationsState" / Int8ul,
        "NotificationsStatus" / Int32ul,
        "PdcSequenceId" / Int32ul,
        "EntryWaitTimeInSeconds" / Int32ul,
        "EntryWatchdogTimeoutInSeconds" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=125, version=0)
class Microsoft_Windows_PDC_125_0(Etw):
    pattern = Struct(
        "Phase" / Int8ul,
        "EngageCount" / Int32ul,
        "EngageHandlerTotalTime" / Int64ul,
        "EngageHandlerNotificationsTotalTime" / Int64ul,
        "DisengageCount" / Int32ul,
        "DisengageHandlerTotalTime" / Int64ul,
        "DisengageHandlerNotificationsTotalTime" / Int64ul,
        "PhaseTotalTime" / Int64ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=126, version=0)
class Microsoft_Windows_PDC_126_0(Etw):
    pattern = Struct(
        "CurrentPhase" / Int8ul,
        "CurrentPhaseNotificationsState" / Int8ul,
        "CurrentPhaseNotificationsStatus" / Int32ul,
        "CurrentPhasePdcSequence" / Int32ul,
        "CallbackStatus" / Int32ul,
        "CallbackPdcSequence" / Int32ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=127, version=0)
class Microsoft_Windows_PDC_127_0(Etw):
    pattern = Struct(
        "SystemIdle" / Int8ul
    )


@declare(guid=guid("a6bf0deb-3659-40ad-9f81-e25af62ce3c7"), event_id=128, version=0)
class Microsoft_Windows_PDC_128_0(Etw):
    pattern = Struct(
        "FunctionNameLength" / Int32ul,
        "FunctionName" / Bytes(lambda this: this.FunctionNameLength),
        "ArgumentNameLength" / Int32ul,
        "ArgumentName" / Bytes(lambda this: this.ArgumentNameLength)
    )

