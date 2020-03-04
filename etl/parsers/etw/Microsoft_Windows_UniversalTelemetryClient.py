# -*- coding: utf-8 -*-
"""
Microsoft-Windows-UniversalTelemetryClient
GUID : 6489b27f-7c43-5886-1d00-0a61bb2a375b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=1, version=0)
class Microsoft_Windows_UniversalTelemetryClient_1_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "IKey" / WString,
        "DiskSizeInBytes" / Int32ul,
        "DailyUploadQuotaInBytes" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=2, version=0)
class Microsoft_Windows_UniversalTelemetryClient_2_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "IKey" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=3, version=0)
class Microsoft_Windows_UniversalTelemetryClient_3_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "IKey" / WString,
        "DailyUploadQuotaInBytes" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=20, version=0)
class Microsoft_Windows_UniversalTelemetryClient_20_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "Url" / WString
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=21, version=0)
class Microsoft_Windows_UniversalTelemetryClient_21_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=22, version=0)
class Microsoft_Windows_UniversalTelemetryClient_22_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "BytesUploadedSoFar" / Int64ul,
        "BytesAllowed" / Int64ul,
        "PercentageUsed" / Int32ul,
        "NewTier" / Int32ul,
        "OldTier" / Int32ul
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=23, version=0)
class Microsoft_Windows_UniversalTelemetryClient_23_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "PercentageFullInEachRingBuffer" / Int32ul
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=24, version=0)
class Microsoft_Windows_UniversalTelemetryClient_24_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "Region" / WString
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=25, version=0)
class Microsoft_Windows_UniversalTelemetryClient_25_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "UploadQuota" / Int32ul,
        "PercentageQuotaUsed" / Double
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=26, version=0)
class Microsoft_Windows_UniversalTelemetryClient_26_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "UploadQuota" / Int64ul
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=27, version=0)
class Microsoft_Windows_UniversalTelemetryClient_27_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "EventsUploaded" / Int32ul,
        "EventsDropped" / Int32ul,
        "LastEventlogWrittenTime" / Int64ul
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=28, version=0)
class Microsoft_Windows_UniversalTelemetryClient_28_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "EventsUploaded" / Int32ul,
        "EventsDropped" / Int32ul,
        "LastEventlogWrittenTime" / Int64ul,
        "SuccessfulConnections" / Int32ul,
        "FailedConnections" / Int32ul,
        "LastHttpError" / Int32ul
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=29, version=0)
class Microsoft_Windows_UniversalTelemetryClient_29_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "EventsUploaded" / Int32ul,
        "EventsDropped" / Int32ul,
        "LastEventlogWrittenTime" / Int64ul,
        "FailedConnections" / Int32ul,
        "LastHttpError" / Int32ul,
        "ProxySettingDetected" / Int8ul,
        "SslCertValidationFailures" / Int32ul,
        "LastSslCertFailure" / Int32ul
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=50, version=0)
class Microsoft_Windows_UniversalTelemetryClient_50_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=55, version=0)
class Microsoft_Windows_UniversalTelemetryClient_55_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "State" / Int8ul
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=56, version=0)
class Microsoft_Windows_UniversalTelemetryClient_56_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "State" / Int8ul
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=60, version=0)
class Microsoft_Windows_UniversalTelemetryClient_60_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "State" / Int8ul
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=61, version=0)
class Microsoft_Windows_UniversalTelemetryClient_61_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "State" / Int8ul
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=62, version=0)
class Microsoft_Windows_UniversalTelemetryClient_62_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "State" / Int8ul
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=63, version=0)
class Microsoft_Windows_UniversalTelemetryClient_63_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "State" / Int8ul
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=64, version=0)
class Microsoft_Windows_UniversalTelemetryClient_64_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "OldInfo" / Int32ul,
        "NewInfo" / Int32ul,
        "SettingAuthority" / Int32sl
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=65, version=0)
class Microsoft_Windows_UniversalTelemetryClient_65_0(Etw):
    pattern = Struct(
        "Environment" / WString,
        "AgentId" / WString,
        "IsIdle" / Int8ul,
        "IdleDurationMillis" / Int64ul
    )


@declare(guid=guid("6489b27f-7c43-5886-1d00-0a61bb2a375b"), event_id=66, version=0)
class Microsoft_Windows_UniversalTelemetryClient_66_0(Etw):
    pattern = Struct(
        "OldLevel" / Int32ul,
        "NewLevel" / Int32ul,
        "Source" / WString
    )

