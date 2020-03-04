# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SENSE
GUID : fae96d09-ade1-5223-0098-af7b67348531
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1, version=0)
class Microsoft_Windows_SENSE_1_0(Etw):
    pattern = Struct(
        "parameter" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=3, version=0)
class Microsoft_Windows_SENSE_3_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=4, version=0)
class Microsoft_Windows_SENSE_4_0(Etw):
    pattern = Struct(
        "UInt1" / Int64ul,
        "Message1" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=5, version=0)
class Microsoft_Windows_SENSE_5_0(Etw):
    pattern = Struct(
        "UInt1" / Int64ul,
        "Message1" / WString,
        "Int1" / Int32sl
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=7, version=0)
class Microsoft_Windows_SENSE_7_0(Etw):
    pattern = Struct(
        "parameter" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=9, version=0)
class Microsoft_Windows_SENSE_9_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=10, version=0)
class Microsoft_Windows_SENSE_10_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=12, version=0)
class Microsoft_Windows_SENSE_12_0(Etw):
    pattern = Struct(
        "parameter1" / WString,
        "parameter2" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=13, version=0)
class Microsoft_Windows_SENSE_13_0(Etw):
    pattern = Struct(
        "parameter" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=14, version=0)
class Microsoft_Windows_SENSE_14_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=15, version=0)
class Microsoft_Windows_SENSE_15_0(Etw):
    pattern = Struct(
        "parameter" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=17, version=0)
class Microsoft_Windows_SENSE_17_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=20, version=0)
class Microsoft_Windows_SENSE_20_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=25, version=0)
class Microsoft_Windows_SENSE_25_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=26, version=0)
class Microsoft_Windows_SENSE_26_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=27, version=0)
class Microsoft_Windows_SENSE_27_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=28, version=0)
class Microsoft_Windows_SENSE_28_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "diskSizeQuotaValue" / Int32sl,
        "dailyUploadQuotaValue" / Int32sl
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=29, version=0)
class Microsoft_Windows_SENSE_29_0(Etw):
    pattern = Struct(
        "errorType" / Int32sl,
        "HRESULT" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=30, version=0)
class Microsoft_Windows_SENSE_30_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=31, version=0)
class Microsoft_Windows_SENSE_31_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=32, version=0)
class Microsoft_Windows_SENSE_32_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=33, version=0)
class Microsoft_Windows_SENSE_33_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=36, version=0)
class Microsoft_Windows_SENSE_36_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "diskSizeQuotaValue" / Int32sl,
        "dailyUploadQuotaValue" / Int32sl
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=37, version=0)
class Microsoft_Windows_SENSE_37_0(Etw):
    pattern = Struct(
        "module" / WString,
        "quotaValue" / Int32sl,
        "quotaValueUnit" / WString,
        "percentageValue" / Int32sl
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=38, version=0)
class Microsoft_Windows_SENSE_38_0(Etw):
    pattern = Struct(
        "pollingInterval" / Int16ul,
        "meteredConnectionState" / Int8ul,
        "internetAvailabilityState" / Int8ul,
        "freeNetworkAvailabilityState" / Int8ul,
        "proxyDefined" / Int8ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=39, version=0)
class Microsoft_Windows_SENSE_39_0(Etw):
    pattern = Struct(
        "pollingInterval" / Int16ul,
        "meteredConnectionState" / Int8ul,
        "internetAvailabilityState" / Int8ul,
        "freeNetworkAvailabilityState" / Int8ul,
        "proxyDefined" / Int8ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=40, version=0)
class Microsoft_Windows_SENSE_40_0(Etw):
    pattern = Struct(
        "pollingInterval" / Int16ul,
        "acPowerState" / Int8ul,
        "batterySavingState" / Int8ul,
        "batteryLowState" / Int8ul,
        "batteryCriticalState" / Int8ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=41, version=0)
class Microsoft_Windows_SENSE_41_0(Etw):
    pattern = Struct(
        "pollingInterval" / Int16ul,
        "acPowerState" / Int8ul,
        "batterySavingState" / Int8ul,
        "batteryLowState" / Int8ul,
        "batteryCriticalState" / Int8ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=42, version=0)
class Microsoft_Windows_SENSE_42_0(Etw):
    pattern = Struct(
        "Component" / CString,
        "Operation" / WString,
        "ExceptionType" / CString,
        "ExceptionMessage" / CString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=43, version=0)
class Microsoft_Windows_SENSE_43_0(Etw):
    pattern = Struct(
        "Component" / CString,
        "Operation" / WString,
        "ExceptionType" / CString,
        "ExceptionErrorCode" / Int32ul,
        "ExceptionMessage" / CString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=45, version=0)
class Microsoft_Windows_SENSE_45_0(Etw):
    pattern = Struct(
        "TraceSessionName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=46, version=0)
class Microsoft_Windows_SENSE_46_0(Etw):
    pattern = Struct(
        "TraceSessionName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=48, version=0)
class Microsoft_Windows_SENSE_48_0(Etw):
    pattern = Struct(
        "ProviderId" / WString,
        "TraceSessionName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=49, version=0)
class Microsoft_Windows_SENSE_49_0(Etw):
    pattern = Struct(
        "Version" / WString,
        "Status" / Int16ul,
        "HRESULT" / Int64ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=50, version=0)
class Microsoft_Windows_SENSE_50_0(Etw):
    pattern = Struct(
        "parameter" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=51, version=0)
class Microsoft_Windows_SENSE_51_0(Etw):
    pattern = Struct(
        "parameter1" / WString,
        "parameter2" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=52, version=0)
class Microsoft_Windows_SENSE_52_0(Etw):
    pattern = Struct(
        "parameter1" / WString,
        "parameter2" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=53, version=0)
class Microsoft_Windows_SENSE_53_0(Etw):
    pattern = Struct(
        "parameter" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=54, version=0)
class Microsoft_Windows_SENSE_54_0(Etw):
    pattern = Struct(
        "Value1" / Int32ul,
        "Value2" / Int32ul,
        "Value3" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=55, version=0)
class Microsoft_Windows_SENSE_55_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=56, version=0)
class Microsoft_Windows_SENSE_56_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=59, version=0)
class Microsoft_Windows_SENSE_59_0(Etw):
    pattern = Struct(
        "parameter" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=60, version=0)
class Microsoft_Windows_SENSE_60_0(Etw):
    pattern = Struct(
        "CommandName" / WString,
        "HRESULT" / Int64ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=61, version=0)
class Microsoft_Windows_SENSE_61_0(Etw):
    pattern = Struct(
        "SasUri" / WString,
        "CompressionLevel" / Int16sl
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=62, version=0)
class Microsoft_Windows_SENSE_62_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=63, version=0)
class Microsoft_Windows_SENSE_63_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ActualStartType" / Int16sl,
        "ExpectedStartType" / Int16sl,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=64, version=0)
class Microsoft_Windows_SENSE_64_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=65, version=0)
class Microsoft_Windows_SENSE_65_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=66, version=0)
class Microsoft_Windows_SENSE_66_0(Etw):
    pattern = Struct(
        "parameter" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=67, version=0)
class Microsoft_Windows_SENSE_67_0(Etw):
    pattern = Struct(
        "UInt1" / Int64ul,
        "UInt2" / Int64ul,
        "UInt3" / Int64ul,
        "Message1" / WString,
        "Int1" / Int32sl
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=68, version=0)
class Microsoft_Windows_SENSE_68_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ActualStartType" / Int16sl,
        "ExpectedStartType" / Int16sl
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=69, version=0)
class Microsoft_Windows_SENSE_69_0(Etw):
    pattern = Struct(
        "parameter" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=70, version=0)
class Microsoft_Windows_SENSE_70_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=71, version=0)
class Microsoft_Windows_SENSE_71_0(Etw):
    pattern = Struct(
        "parameter" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=72, version=0)
class Microsoft_Windows_SENSE_72_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=73, version=0)
class Microsoft_Windows_SENSE_73_0(Etw):
    pattern = Struct(
        "platformBitMask" / Int64ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=74, version=0)
class Microsoft_Windows_SENSE_74_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=75, version=0)
class Microsoft_Windows_SENSE_75_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=76, version=0)
class Microsoft_Windows_SENSE_76_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=79, version=0)
class Microsoft_Windows_SENSE_79_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=80, version=0)
class Microsoft_Windows_SENSE_80_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=81, version=0)
class Microsoft_Windows_SENSE_81_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=82, version=0)
class Microsoft_Windows_SENSE_82_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=83, version=0)
class Microsoft_Windows_SENSE_83_0(Etw):
    pattern = Struct(
        "RealValue" / Int32sl,
        "quotaValue" / Int32sl
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=84, version=0)
class Microsoft_Windows_SENSE_84_0(Etw):
    pattern = Struct(
        "forcePassiveMode" / Int8ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=85, version=0)
class Microsoft_Windows_SENSE_85_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=86, version=0)
class Microsoft_Windows_SENSE_86_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=87, version=0)
class Microsoft_Windows_SENSE_87_0(Etw):
    pattern = Struct(
        "ServiceName" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=88, version=0)
class Microsoft_Windows_SENSE_88_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ActualStartType" / Int16sl,
        "ExpectedStartType" / Int16sl,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=89, version=0)
class Microsoft_Windows_SENSE_89_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ActualStartType" / Int16sl,
        "ExpectedStartType" / Int16sl
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=90, version=0)
class Microsoft_Windows_SENSE_90_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=91, version=0)
class Microsoft_Windows_SENSE_91_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=92, version=0)
class Microsoft_Windows_SENSE_92_0(Etw):
    pattern = Struct(
        "UInt2" / Int64ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=93, version=0)
class Microsoft_Windows_SENSE_93_0(Etw):
    pattern = Struct(
        "UInt2" / Int64ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=96, version=0)
class Microsoft_Windows_SENSE_96_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=99, version=0)
class Microsoft_Windows_SENSE_99_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=100, version=0)
class Microsoft_Windows_SENSE_100_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1800, version=0)
class Microsoft_Windows_SENSE_1800_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1801, version=0)
class Microsoft_Windows_SENSE_1801_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1802, version=0)
class Microsoft_Windows_SENSE_1802_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1803, version=0)
class Microsoft_Windows_SENSE_1803_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Boolean1" / Int8ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1804, version=0)
class Microsoft_Windows_SENSE_1804_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Boolean1" / Int8ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1805, version=0)
class Microsoft_Windows_SENSE_1805_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1806, version=0)
class Microsoft_Windows_SENSE_1806_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "Boolean1" / Int8ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1807, version=0)
class Microsoft_Windows_SENSE_1807_0(Etw):
    pattern = Struct(
        "onboardingBlobHash" / Int64ul,
        "isDefaultOnboardingBlob" / Int8ul,
        "onboardingState" / Int32ul,
        "isDefaultOnboardingState" / Int8ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1808, version=0)
class Microsoft_Windows_SENSE_1808_0(Etw):
    pattern = Struct(
        "offboardingBlobHash" / Int64ul,
        "isDefaultOffboardingBlob" / Int8ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1809, version=0)
class Microsoft_Windows_SENSE_1809_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "Boolean1" / Int8ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1811, version=0)
class Microsoft_Windows_SENSE_1811_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1812, version=0)
class Microsoft_Windows_SENSE_1812_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1814, version=0)
class Microsoft_Windows_SENSE_1814_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1815, version=0)
class Microsoft_Windows_SENSE_1815_0(Etw):
    pattern = Struct(
        "previousSampleCollectionValue" / Int32ul,
        "IsDefault" / Int8ul,
        "newSampleSharing" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1816, version=0)
class Microsoft_Windows_SENSE_1816_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1817, version=0)
class Microsoft_Windows_SENSE_1817_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1818, version=0)
class Microsoft_Windows_SENSE_1818_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1819, version=0)
class Microsoft_Windows_SENSE_1819_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1820, version=0)
class Microsoft_Windows_SENSE_1820_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1821, version=0)
class Microsoft_Windows_SENSE_1821_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1822, version=0)
class Microsoft_Windows_SENSE_1822_0(Etw):
    pattern = Struct(
        "previousLatencyMode" / WString,
        "IsDefault" / Int8ul,
        "newLatencyMode" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1823, version=0)
class Microsoft_Windows_SENSE_1823_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "Message1" / WString,
        "Boolean1" / Int8ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1824, version=0)
class Microsoft_Windows_SENSE_1824_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Boolean1" / Int8ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1825, version=0)
class Microsoft_Windows_SENSE_1825_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "UInt2" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1826, version=0)
class Microsoft_Windows_SENSE_1826_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1827, version=0)
class Microsoft_Windows_SENSE_1827_0(Etw):
    pattern = Struct(
        "isServiceRunningAlready" / Int8ul,
        "previousOnboardingBlobHash" / Int64ul,
        "isDefaultOnboardingBlob" / Int8ul,
        "onboardingState" / Int32ul,
        "isDefaultOnboardingState" / Int8ul,
        "newOnboardingBlobHash" / Int64ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1828, version=0)
class Microsoft_Windows_SENSE_1828_0(Etw):
    pattern = Struct(
        "isServiceRunning" / Int8ul,
        "previousOffboardingBlobHash" / Int64ul,
        "isDefaultOffboardingBlob" / Int8ul,
        "onboardingState" / Int32ul,
        "isDefaultOnboardingState" / Int8ul,
        "newOffboardingBlobHash" / Int64ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1829, version=0)
class Microsoft_Windows_SENSE_1829_0(Etw):
    pattern = Struct(
        "requestedValue" / Int32ul,
        "minimumAllowedValue" / Int32ul,
        "maximumAllowedValue" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1830, version=0)
class Microsoft_Windows_SENSE_1830_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1832, version=0)
class Microsoft_Windows_SENSE_1832_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Boolean1" / Int8ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1833, version=0)
class Microsoft_Windows_SENSE_1833_0(Etw):
    pattern = Struct(
        "registryValue" / WString,
        "IsDefault" / Int8ul,
        "conversionSucceeded" / Int8ul,
        "Result" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1834, version=0)
class Microsoft_Windows_SENSE_1834_0(Etw):
    pattern = Struct(
        "registryValue" / WString,
        "IsDefault" / Int8ul,
        "conversionSucceeded" / Int8ul,
        "Result" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1835, version=0)
class Microsoft_Windows_SENSE_1835_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1836, version=0)
class Microsoft_Windows_SENSE_1836_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "UInt2" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1837, version=0)
class Microsoft_Windows_SENSE_1837_0(Etw):
    pattern = Struct(
        "previousCriticalityValue" / WString,
        "IsDefault" / Int8ul,
        "newCriticalityValue" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1838, version=0)
class Microsoft_Windows_SENSE_1838_0(Etw):
    pattern = Struct(
        "requestedValue" / Int32ul,
        "minimumAllowedValue" / Int32ul,
        "maximumAllowedValue" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1839, version=0)
class Microsoft_Windows_SENSE_1839_0(Etw):
    pattern = Struct(
        "previousIdMethodValue" / WString,
        "IsDefault" / Int8ul,
        "newIdMethodValue" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("fae96d09-ade1-5223-0098-af7b67348531"), event_id=1840, version=0)
class Microsoft_Windows_SENSE_1840_0(Etw):
    pattern = Struct(
        "requestedValue" / Int32ul,
        "minimumAllowedValue" / Int32ul,
        "maximumAllowedValue" / Int32ul
    )

