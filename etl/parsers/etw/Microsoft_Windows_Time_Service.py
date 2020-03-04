# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Time-Service
GUID : 06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=1, version=0)
class Microsoft_Windows_Time_Service_1_0(Etw):
    pattern = Struct(
        "TimeProvider" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=2, version=0)
class Microsoft_Windows_Time_Service_2_0(Etw):
    pattern = Struct(
        "TimeProvider" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=3, version=0)
class Microsoft_Windows_Time_Service_3_0(Etw):
    pattern = Struct(
        "TimeProvider" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=4, version=0)
class Microsoft_Windows_Time_Service_4_0(Etw):
    pattern = Struct(
        "TimeProvider" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=5, version=0)
class Microsoft_Windows_Time_Service_5_0(Etw):
    pattern = Struct(
        "TimeProvider" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=6, version=0)
class Microsoft_Windows_Time_Service_6_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=7, version=0)
class Microsoft_Windows_Time_Service_7_0(Etw):
    pattern = Struct(
        "TimeProvider" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=8, version=0)
class Microsoft_Windows_Time_Service_8_0(Etw):
    pattern = Struct(
        "TimeProvider" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=9, version=0)
class Microsoft_Windows_Time_Service_9_0(Etw):
    pattern = Struct(
        "TimeProvider" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=10, version=0)
class Microsoft_Windows_Time_Service_10_0(Etw):
    pattern = Struct(
        "TimeProvider" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=14, version=0)
class Microsoft_Windows_Time_Service_14_0(Etw):
    pattern = Struct(
        "RetryMinutes" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=15, version=0)
class Microsoft_Windows_Time_Service_15_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=16, version=0)
class Microsoft_Windows_Time_Service_16_0(Etw):
    pattern = Struct(
        "ManualPeer" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=17, version=0)
class Microsoft_Windows_Time_Service_17_0(Etw):
    pattern = Struct(
        "ManualPeer" / WString,
        "ErrorMessage" / WString,
        "RetryMinutes" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=18, version=0)
class Microsoft_Windows_Time_Service_18_0(Etw):
    pattern = Struct(
        "Domain" / WString,
        "ErrorMessage" / WString,
        "RetryMinutes" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=19, version=0)
class Microsoft_Windows_Time_Service_19_0(Etw):
    pattern = Struct(
        "LogFile" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=20, version=0)
class Microsoft_Windows_Time_Service_20_0(Etw):
    pattern = Struct(
        "LogFile" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=22, version=0)
class Microsoft_Windows_Time_Service_22_0(Etw):
    pattern = Struct(
        "Peer" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=23, version=0)
class Microsoft_Windows_Time_Service_23_0(Etw):
    pattern = Struct(
        "Peer" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=24, version=0)
class Microsoft_Windows_Time_Service_24_0(Etw):
    pattern = Struct(
        "DomainPeer" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=25, version=0)
class Microsoft_Windows_Time_Service_25_0(Etw):
    pattern = Struct(
        "DomainPeer" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=26, version=0)
class Microsoft_Windows_Time_Service_26_0(Etw):
    pattern = Struct(
        "DomainPeer" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=27, version=0)
class Microsoft_Windows_Time_Service_27_0(Etw):
    pattern = Struct(
        "DomainPeer" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=29, version=0)
class Microsoft_Windows_Time_Service_29_0(Etw):
    pattern = Struct(
        "RetryMinutes" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=30, version=0)
class Microsoft_Windows_Time_Service_30_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=32, version=0)
class Microsoft_Windows_Time_Service_32_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=33, version=0)
class Microsoft_Windows_Time_Service_33_0(Etw):
    pattern = Struct(
        "SystemTimeChangeSeconds" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=34, version=0)
class Microsoft_Windows_Time_Service_34_0(Etw):
    pattern = Struct(
        "SystemTimeChangeSeconds" / Int64sl,
        "MaxSystemTimeChangeSeconds" / Int32ul,
        "TimeSource" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=35, version=0)
class Microsoft_Windows_Time_Service_35_0(Etw):
    pattern = Struct(
        "TimeSource" / WString,
        "TimeSourceRefId" / Int32ul,
        "CurrentStratumNumber" / Int32ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=36, version=0)
class Microsoft_Windows_Time_Service_36_0(Etw):
    pattern = Struct(
        "UnsynchronizedTimeSeconds" / Int32ul,
        "TimeRemainingToSetLocalClockFreeRunningSeconds" / Int32ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=37, version=0)
class Microsoft_Windows_Time_Service_37_0(Etw):
    pattern = Struct(
        "TimeSource" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=38, version=0)
class Microsoft_Windows_Time_Service_38_0(Etw):
    pattern = Struct(
        "TimeSource" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=40, version=0)
class Microsoft_Windows_Time_Service_40_0(Etw):
    pattern = Struct(
        "TimeProvider" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=43, version=0)
class Microsoft_Windows_Time_Service_43_0(Etw):
    pattern = Struct(
        "TimeProvider" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=44, version=0)
class Microsoft_Windows_Time_Service_44_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=45, version=0)
class Microsoft_Windows_Time_Service_45_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=46, version=0)
class Microsoft_Windows_Time_Service_46_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=47, version=0)
class Microsoft_Windows_Time_Service_47_0(Etw):
    pattern = Struct(
        "ManualPeer" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=48, version=0)
class Microsoft_Windows_Time_Service_48_0(Etw):
    pattern = Struct(
        "ManualPeer" / WString,
        "ErrorMessage" / WString,
        "RetryMinutes" / Int32ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=49, version=0)
class Microsoft_Windows_Time_Service_49_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=50, version=0)
class Microsoft_Windows_Time_Service_50_0(Etw):
    pattern = Struct(
        "TimeDifferenceMilliseconds" / Int32ul,
        "TimeSampleSeconds" / Int32ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=51, version=0)
class Microsoft_Windows_Time_Service_51_0(Etw):
    pattern = Struct(
        "Peer" / WString,
        "TimeDifferenceSeconds" / WString,
        "TransmissionDelayMilliseconds" / Int32ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=52, version=0)
class Microsoft_Windows_Time_Service_52_0(Etw):
    pattern = Struct(
        "TimeOffsetSeconds" / Int64sl
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=53, version=0)
class Microsoft_Windows_Time_Service_53_0(Etw):
    pattern = Struct(
        "Peer" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=54, version=0)
class Microsoft_Windows_Time_Service_54_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=129, version=0)
class Microsoft_Windows_Time_Service_129_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString,
        "RetryMinutes" / Int32ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=130, version=0)
class Microsoft_Windows_Time_Service_130_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString,
        "RetryMinutes" / Int32ul,
        "DomainPeer" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=131, version=0)
class Microsoft_Windows_Time_Service_131_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString,
        "RetryMinutes" / Int32ul,
        "DomainPeer" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=132, version=0)
class Microsoft_Windows_Time_Service_132_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString,
        "RetryMinutes" / Int32ul,
        "DomainPeer" / WString,
        "TimeSource" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=133, version=0)
class Microsoft_Windows_Time_Service_133_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString,
        "RetryMinutes" / Int32ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=134, version=0)
class Microsoft_Windows_Time_Service_134_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString,
        "RetryMinutes" / Int32ul,
        "DomainPeer" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=135, version=0)
class Microsoft_Windows_Time_Service_135_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString,
        "RetryMinutes" / Int32ul,
        "DomainPeer" / WString,
        "TimeSource" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=136, version=0)
class Microsoft_Windows_Time_Service_136_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString,
        "RetryMinutes" / Int32ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=137, version=0)
class Microsoft_Windows_Time_Service_137_0(Etw):
    pattern = Struct(
        "ManualPeer" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=138, version=0)
class Microsoft_Windows_Time_Service_138_0(Etw):
    pattern = Struct(
        "DomainPeer" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=146, version=0)
class Microsoft_Windows_Time_Service_146_0(Etw):
    pattern = Struct(
        "ChainingCountRequests" / Int32ul,
        "ChainLoggingRate" / Int32ul,
        "ChainingCountSuccess" / Int32ul,
        "ChainingCountFailure" / Int32ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=156, version=0)
class Microsoft_Windows_Time_Service_156_0(Etw):
    pattern = Struct(
        "ClientRID" / Int32ul,
        "DomainPeer" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=157, version=0)
class Microsoft_Windows_Time_Service_157_0(Etw):
    pattern = Struct(
        "ClientAddress" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=158, version=0)
class Microsoft_Windows_Time_Service_158_0(Etw):
    pattern = Struct(
        "TimeProvider" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=159, version=0)
class Microsoft_Windows_Time_Service_159_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=257, version=0)
class Microsoft_Windows_Time_Service_257_0(Etw):
    pattern = Struct(
        "CurrentTimeUTC" / WString,
        "TickCount" / Int64ul,
        "Configuration" / WString,
        "TimeProviders" / WString,
        "ClockRate" / Int64ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=258, version=0)
class Microsoft_Windows_Time_Service_258_0(Etw):
    pattern = Struct(
        "CurrentTimeUTC" / WString,
        "TickCount" / Int64ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=259, version=0)
class Microsoft_Windows_Time_Service_259_0(Etw):
    pattern = Struct(
        "AllNtpServers" / WString,
        "ChosenReferenceNtpServer" / WString,
        "TickCount" / Int64ul,
        "IFTSTMP" / Int32ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=260, version=0)
class Microsoft_Windows_Time_Service_260_0(Etw):
    pattern = Struct(
        "Configuration" / WString,
        "TimeProviders" / WString,
        "LeapIndicator" / Int64ul,
        "Stratum" / Int64ul,
        "Precision" / WString,
        "RootDelay" / WString,
        "RootDispersion" / WString,
        "ReferenceId" / WString,
        "LastSuccessfulSyncTime" / WString,
        "Source" / WString,
        "PollInterval" / Int64ul,
        "PhaseOffset" / WString,
        "ClockRate" / Int64ul,
        "StateMachine" / Int64ul,
        "TimeSourceFlags" / Int64ul,
        "ServerRole" / Int64ul,
        "LastSyncError" / Int64ul,
        "TimeSinceLastGoodSync" / WString,
        "TickCount" / Int64ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=261, version=0)
class Microsoft_Windows_Time_Service_261_0(Etw):
    pattern = Struct(
        "NewTime" / WString,
        "OldTime" / WString,
        "TickCount" / Int64ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=262, version=0)
class Microsoft_Windows_Time_Service_262_0(Etw):
    pattern = Struct(
        "AdjustmentPPM" / WString,
        "NewClockRate" / Int64ul,
        "OldClockRate" / Int64ul,
        "TickCount" / Int64ul,
        "MinReportedAdjustmentPPM" / WString
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=263, version=0)
class Microsoft_Windows_Time_Service_263_0(Etw):
    pattern = Struct(
        "Configuration" / WString,
        "TimeProviders" / WString,
        "TickCount" / Int64ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=264, version=0)
class Microsoft_Windows_Time_Service_264_0(Etw):
    pattern = Struct(
        "AllNtpServers" / WString,
        "TickCount" / Int64ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=265, version=0)
class Microsoft_Windows_Time_Service_265_0(Etw):
    pattern = Struct(
        "TimeSource" / WString,
        "TimeSourceRefId" / WString,
        "LocalStratumNumber" / Int32ul,
        "TickCount" / Int64ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=266, version=0)
class Microsoft_Windows_Time_Service_266_0(Etw):
    pattern = Struct(
        "ReasonCode" / Int64ul,
        "TickCount" / Int64ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=272, version=0)
class Microsoft_Windows_Time_Service_272_0(Etw):
    pattern = Struct(
        "Enabled" / Int32ul,
        "LeapSecondCount" / Int32ul,
        "CurrentUtcOffset" / Int32sl,
        "RuntimeStateAndSettingsConsistent" / Int32ul,
        "NewestLeapSecondsList" / WString,
        "TickCount" / Int64ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=273, version=0)
class Microsoft_Windows_Time_Service_273_0(Etw):
    pattern = Struct(
        "Action" / WString,
        "UtcTime" / WString,
        "LocalTime" / WString,
        "TimeProvider" / WString,
        "TickCount" / Int64ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=274, version=0)
class Microsoft_Windows_Time_Service_274_0(Etw):
    pattern = Struct(
        "Action" / WString,
        "UtcTime" / WString,
        "LocalTime" / WString,
        "TimeProvider" / WString,
        "TickCount" / Int64ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=275, version=0)
class Microsoft_Windows_Time_Service_275_0(Etw):
    pattern = Struct(
        "UtcLeapSecondString" / WString,
        "ErrorMessage" / WString,
        "TickCount" / Int64ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=276, version=0)
class Microsoft_Windows_Time_Service_276_0(Etw):
    pattern = Struct(
        "Action" / WString,
        "UtcTime" / WString,
        "LocalTime" / WString,
        "TimeProvider" / WString,
        "TickCount" / Int64ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=279, version=0)
class Microsoft_Windows_Time_Service_279_0(Etw):
    pattern = Struct(
        "TickCount" / Int64ul
    )


@declare(guid=guid("06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb"), event_id=280, version=0)
class Microsoft_Windows_Time_Service_280_0(Etw):
    pattern = Struct(
        "RpcEndPointError" / Int32ul
    )

