# -*- coding: utf-8 -*-
"""
Microsoft-IEFRAME
GUID : 5c8bb950-959e-4309-8908-67961a1205d5
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=9, version=0)
class Microsoft_IEFRAME_9_0(Etw):
    pattern = Struct(
        "Message" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=10, version=0)
class Microsoft_IEFRAME_10_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul,
        "TabState" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=11, version=0)
class Microsoft_IEFRAME_11_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul,
        "TabState" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=12, version=0)
class Microsoft_IEFRAME_12_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul,
        "TabState" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=17, version=0)
class Microsoft_IEFRAME_17_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=18, version=0)
class Microsoft_IEFRAME_18_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=19, version=0)
class Microsoft_IEFRAME_19_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul,
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=20, version=0)
class Microsoft_IEFRAME_20_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=21, version=0)
class Microsoft_IEFRAME_21_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=22, version=0)
class Microsoft_IEFRAME_22_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=23, version=0)
class Microsoft_IEFRAME_23_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=64, version=0)
class Microsoft_IEFRAME_64_0(Etw):
    pattern = Struct(
        "Message" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=65, version=0)
class Microsoft_IEFRAME_65_0(Etw):
    pattern = Struct(
        "CLSID" / Guid
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=66, version=0)
class Microsoft_IEFRAME_66_0(Etw):
    pattern = Struct(
        "CLSID" / Guid
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=67, version=0)
class Microsoft_IEFRAME_67_0(Etw):
    pattern = Struct(
        "CLSID" / Guid
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=68, version=0)
class Microsoft_IEFRAME_68_0(Etw):
    pattern = Struct(
        "CLSID" / Guid
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=69, version=0)
class Microsoft_IEFRAME_69_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "Show" / Int8ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=70, version=0)
class Microsoft_IEFRAME_70_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "Show" / Int8ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=71, version=0)
class Microsoft_IEFRAME_71_0(Etw):
    pattern = Struct(
        "CLSID" / Guid
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=72, version=0)
class Microsoft_IEFRAME_72_0(Etw):
    pattern = Struct(
        "CLSID" / Guid
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=73, version=0)
class Microsoft_IEFRAME_73_0(Etw):
    pattern = Struct(
        "CLSID" / Guid
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=74, version=0)
class Microsoft_IEFRAME_74_0(Etw):
    pattern = Struct(
        "CLSID" / Guid
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=75, version=0)
class Microsoft_IEFRAME_75_0(Etw):
    pattern = Struct(
        "CLSID" / Guid
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=76, version=0)
class Microsoft_IEFRAME_76_0(Etw):
    pattern = Struct(
        "CLSID" / Guid
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=78, version=0)
class Microsoft_IEFRAME_78_0(Etw):
    pattern = Struct(
        "ProcessId" / Guid,
        "MessageCount" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=79, version=0)
class Microsoft_IEFRAME_79_0(Etw):
    pattern = Struct(
        "ProcessId" / Guid,
        "MessageCount" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=115, version=0)
class Microsoft_IEFRAME_115_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "QueryID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=116, version=0)
class Microsoft_IEFRAME_116_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "QueryID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=117, version=0)
class Microsoft_IEFRAME_117_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "QueryID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=118, version=0)
class Microsoft_IEFRAME_118_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "QueryID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=119, version=0)
class Microsoft_IEFRAME_119_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "QueryID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=120, version=0)
class Microsoft_IEFRAME_120_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "QueryID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=121, version=0)
class Microsoft_IEFRAME_121_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "QueryID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=122, version=0)
class Microsoft_IEFRAME_122_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "QueryID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=127, version=0)
class Microsoft_IEFRAME_127_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "Count" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=128, version=0)
class Microsoft_IEFRAME_128_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "Count" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=130, version=0)
class Microsoft_IEFRAME_130_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "QueryID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=133, version=0)
class Microsoft_IEFRAME_133_0(Etw):
    pattern = Struct(
        "QueryID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=134, version=0)
class Microsoft_IEFRAME_134_0(Etw):
    pattern = Struct(
        "QueryID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=147, version=0)
class Microsoft_IEFRAME_147_0(Etw):
    pattern = Struct(
        "PopulateOptions" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=148, version=0)
class Microsoft_IEFRAME_148_0(Etw):
    pattern = Struct(
        "PopulateOptions" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=149, version=0)
class Microsoft_IEFRAME_149_0(Etw):
    pattern = Struct(
        "LinkCount" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=150, version=0)
class Microsoft_IEFRAME_150_0(Etw):
    pattern = Struct(
        "LinkCount" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=157, version=0)
class Microsoft_IEFRAME_157_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "Count" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=173, version=0)
class Microsoft_IEFRAME_173_0(Etw):
    pattern = Struct(
        "ContextName" / CString,
        "ID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=174, version=0)
class Microsoft_IEFRAME_174_0(Etw):
    pattern = Struct(
        "ContextName" / CString,
        "ID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=183, version=0)
class Microsoft_IEFRAME_183_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul,
        "TabState" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=184, version=0)
class Microsoft_IEFRAME_184_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul,
        "TabState" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=185, version=0)
class Microsoft_IEFRAME_185_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul,
        "TabState" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=186, version=0)
class Microsoft_IEFRAME_186_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul,
        "TabState" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=187, version=0)
class Microsoft_IEFRAME_187_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul,
        "TabState" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=188, version=0)
class Microsoft_IEFRAME_188_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul,
        "TabState" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=189, version=0)
class Microsoft_IEFRAME_189_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul,
        "TabState" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=190, version=0)
class Microsoft_IEFRAME_190_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul,
        "TabState" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=191, version=0)
class Microsoft_IEFRAME_191_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul,
        "TabState" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=192, version=0)
class Microsoft_IEFRAME_192_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul,
        "TabState" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=217, version=0)
class Microsoft_IEFRAME_217_0(Etw):
    pattern = Struct(
        "OnCloseButton" / Int8ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=225, version=0)
class Microsoft_IEFRAME_225_0(Etw):
    pattern = Struct(
        "TimeElapsed" / Int64ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=232, version=0)
class Microsoft_IEFRAME_232_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "Count" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=311, version=0)
class Microsoft_IEFRAME_311_0(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "StateString" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=312, version=0)
class Microsoft_IEFRAME_312_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=313, version=0)
class Microsoft_IEFRAME_313_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=317, version=0)
class Microsoft_IEFRAME_317_0(Etw):
    pattern = Struct(
        "LayerValue" / Int32sl,
        "CommandID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=318, version=0)
class Microsoft_IEFRAME_318_0(Etw):
    pattern = Struct(
        "LayerValue" / Int32sl,
        "CommandID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=328, version=0)
class Microsoft_IEFRAME_328_0(Etw):
    pattern = Struct(
        "AnimationType" / Int32ul,
        "Flags" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=329, version=0)
class Microsoft_IEFRAME_329_0(Etw):
    pattern = Struct(
        "AnimationType" / Int32ul,
        "Flags" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=344, version=0)
class Microsoft_IEFRAME_344_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=345, version=0)
class Microsoft_IEFRAME_345_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=397, version=0)
class Microsoft_IEFRAME_397_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=398, version=0)
class Microsoft_IEFRAME_398_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=405, version=0)
class Microsoft_IEFRAME_405_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=406, version=0)
class Microsoft_IEFRAME_406_0(Etw):
    pattern = Struct(
        "Show" / Int8ul,
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=407, version=0)
class Microsoft_IEFRAME_407_0(Etw):
    pattern = Struct(
        "Disconnect" / Int8ul,
        "TabID" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=408, version=0)
class Microsoft_IEFRAME_408_0(Etw):
    pattern = Struct(
        "Disconnect" / Int8ul,
        "TabID" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=409, version=0)
class Microsoft_IEFRAME_409_0(Etw):
    pattern = Struct(
        "UserInitiated" / Int8ul,
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=410, version=0)
class Microsoft_IEFRAME_410_0(Etw):
    pattern = Struct(
        "UserInitiated" / Int8ul,
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=411, version=0)
class Microsoft_IEFRAME_411_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=412, version=0)
class Microsoft_IEFRAME_412_0(Etw):
    pattern = Struct(
        "Attach" / Int8ul,
        "TabID" / Int32ul,
        "AttachTID" / Int32ul,
        "AttachToTID" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=413, version=0)
class Microsoft_IEFRAME_413_0(Etw):
    pattern = Struct(
        "Attach" / Int8ul,
        "TabID" / Int32ul,
        "AttachTID" / Int32ul,
        "AttachToTID" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=414, version=0)
class Microsoft_IEFRAME_414_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=415, version=0)
class Microsoft_IEFRAME_415_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=416, version=0)
class Microsoft_IEFRAME_416_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=417, version=0)
class Microsoft_IEFRAME_417_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul,
        "SelfRecovered" / Int8ul,
        "PerformWhenBrowserResponds" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=418, version=0)
class Microsoft_IEFRAME_418_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul,
        "BarText" / WString,
        "ButtonText" / WString,
        "Mode" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=419, version=0)
class Microsoft_IEFRAME_419_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul,
        "BarText" / WString,
        "ButtonText" / WString,
        "Mode" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=420, version=0)
class Microsoft_IEFRAME_420_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "TabID" / Int32ul,
        "SyncTimeout" / Int32ul,
        "SetHung" / Int8ul,
        "UserAction" / Int8ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=425, version=0)
class Microsoft_IEFRAME_425_0(Etw):
    pattern = Struct(
        "PID" / Int32ul,
        "ActivityType" / WString,
        "ImageKey" / WString,
        "ImageUniqueID" / Int32ul,
        "ImageDimX" / Int32ul,
        "ImageDimY" / Int32ul,
        "ImageCleaningScheme" / Int32ul,
        "ImageLastUpdatedTime" / Int64ul,
        "ImageLastRetrievedTime" / Int64ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=426, version=0)
class Microsoft_IEFRAME_426_0(Etw):
    pattern = Struct(
        "PID" / Int32ul,
        "ActivityType" / WString,
        "ImageKey" / WString,
        "TotalNumber" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=427, version=0)
class Microsoft_IEFRAME_427_0(Etw):
    pattern = Struct(
        "PID" / Int32ul,
        "Suspending" / Int8ul,
        "ResumeReason" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=428, version=0)
class Microsoft_IEFRAME_428_0(Etw):
    pattern = Struct(
        "PID" / Int32ul,
        "Suspending" / Int8ul,
        "ResumeReason" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=429, version=0)
class Microsoft_IEFRAME_429_0(Etw):
    pattern = Struct(
        "Target" / Int32ul,
        "TargetPID" / Int32ul,
        "Dependent" / Int32ul,
        "DependentPID" / Int32ul,
        "Flags" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=430, version=0)
class Microsoft_IEFRAME_430_0(Etw):
    pattern = Struct(
        "Target" / Int32ul,
        "TargetPID" / Int32ul,
        "Dependent" / Int32ul,
        "DependentPID" / Int32ul,
        "Flags" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=431, version=0)
class Microsoft_IEFRAME_431_0(Etw):
    pattern = Struct(
        "QueryID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=432, version=0)
class Microsoft_IEFRAME_432_0(Etw):
    pattern = Struct(
        "QueryID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=433, version=0)
class Microsoft_IEFRAME_433_0(Etw):
    pattern = Struct(
        "QueryID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=434, version=0)
class Microsoft_IEFRAME_434_0(Etw):
    pattern = Struct(
        "QueryID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=435, version=0)
class Microsoft_IEFRAME_435_0(Etw):
    pattern = Struct(
        "QueryID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=436, version=0)
class Microsoft_IEFRAME_436_0(Etw):
    pattern = Struct(
        "QueryID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=456, version=0)
class Microsoft_IEFRAME_456_0(Etw):
    pattern = Struct(
        "TabId" / Guid
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=457, version=0)
class Microsoft_IEFRAME_457_0(Etw):
    pattern = Struct(
        "TabId" / Guid
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=460, version=0)
class Microsoft_IEFRAME_460_0(Etw):
    pattern = Struct(
        "TabId" / Guid
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=462, version=0)
class Microsoft_IEFRAME_462_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=463, version=0)
class Microsoft_IEFRAME_463_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=464, version=0)
class Microsoft_IEFRAME_464_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=465, version=0)
class Microsoft_IEFRAME_465_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=466, version=0)
class Microsoft_IEFRAME_466_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=467, version=0)
class Microsoft_IEFRAME_467_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=468, version=0)
class Microsoft_IEFRAME_468_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=469, version=0)
class Microsoft_IEFRAME_469_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=470, version=0)
class Microsoft_IEFRAME_470_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=471, version=0)
class Microsoft_IEFRAME_471_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=472, version=0)
class Microsoft_IEFRAME_472_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=473, version=0)
class Microsoft_IEFRAME_473_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=500, version=0)
class Microsoft_IEFRAME_500_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=501, version=0)
class Microsoft_IEFRAME_501_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=502, version=0)
class Microsoft_IEFRAME_502_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=503, version=0)
class Microsoft_IEFRAME_503_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=504, version=0)
class Microsoft_IEFRAME_504_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=505, version=0)
class Microsoft_IEFRAME_505_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=506, version=0)
class Microsoft_IEFRAME_506_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=507, version=0)
class Microsoft_IEFRAME_507_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=508, version=0)
class Microsoft_IEFRAME_508_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=509, version=0)
class Microsoft_IEFRAME_509_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=510, version=0)
class Microsoft_IEFRAME_510_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=511, version=0)
class Microsoft_IEFRAME_511_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=514, version=0)
class Microsoft_IEFRAME_514_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=515, version=0)
class Microsoft_IEFRAME_515_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=516, version=0)
class Microsoft_IEFRAME_516_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=517, version=0)
class Microsoft_IEFRAME_517_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=518, version=0)
class Microsoft_IEFRAME_518_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=525, version=0)
class Microsoft_IEFRAME_525_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=533, version=0)
class Microsoft_IEFRAME_533_0(Etw):
    pattern = Struct(
        "Uint32Val" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=534, version=0)
class Microsoft_IEFRAME_534_0(Etw):
    pattern = Struct(
        "PrerenderURL" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=535, version=0)
class Microsoft_IEFRAME_535_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "DominantImageUrl1" / WString,
        "DominantImageUrl2" / WString,
        "DominantImageUrl3" / WString,
        "DominantImageUrl4" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=550, version=0)
class Microsoft_IEFRAME_550_0(Etw):
    pattern = Struct(
        "ComponentType" / Int32ul,
        "PID" / Int32ul,
        "TID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=551, version=0)
class Microsoft_IEFRAME_551_0(Etw):
    pattern = Struct(
        "ComponentType" / Int32ul,
        "PID" / Int32ul,
        "TID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=552, version=0)
class Microsoft_IEFRAME_552_0(Etw):
    pattern = Struct(
        "ImageUrl" / WString,
        "ImageType" / Int32ul,
        "DIType" / Int32ul,
        "DIConfidence" / Int32ul,
        "TileSize" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=555, version=0)
class Microsoft_IEFRAME_555_0(Etw):
    pattern = Struct(
        "TabId" / Guid
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=556, version=0)
class Microsoft_IEFRAME_556_0(Etw):
    pattern = Struct(
        "NotifyFrame" / Int8ul,
        "Result" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=557, version=0)
class Microsoft_IEFRAME_557_0(Etw):
    pattern = Struct(
        "NotifyFrame" / Int8ul,
        "Result" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=558, version=0)
class Microsoft_IEFRAME_558_0(Etw):
    pattern = Struct(
        "TabID" / Int32sl,
        "SelectTabAsyncTabID" / Int32sl,
        "SelectTabAsyncFlags" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=559, version=0)
class Microsoft_IEFRAME_559_0(Etw):
    pattern = Struct(
        "TabID" / Int32sl,
        "SelectTabAsyncTabID" / Int32sl,
        "SelectTabAsyncFlags" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=560, version=0)
class Microsoft_IEFRAME_560_0(Etw):
    pattern = Struct(
        "SelectTabAsyncTabID" / Int32sl,
        "SelectTabAsyncFlags" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=562, version=0)
class Microsoft_IEFRAME_562_0(Etw):
    pattern = Struct(
        "SelectTabAsyncTabID" / Int32sl,
        "SelectTabAsyncFlags" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=563, version=0)
class Microsoft_IEFRAME_563_0(Etw):
    pattern = Struct(
        "TabID" / Int32sl,
        "NewVisibleState" / Int8ul,
        "CurrentVisibleState" / Int8ul,
        "IsTabSwitch" / Int8ul,
        "IsHung" / Int8ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=564, version=0)
class Microsoft_IEFRAME_564_0(Etw):
    pattern = Struct(
        "TabID" / Int32sl,
        "NewVisibleState" / Int8ul,
        "CurrentVisibleState" / Int8ul,
        "IsTabSwitch" / Int8ul,
        "IsHung" / Int8ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=565, version=0)
class Microsoft_IEFRAME_565_0(Etw):
    pattern = Struct(
        "ISO_HANDLE" / Int64ul,
        "IDLEMANAGER_TASKTYPE" / Int32ul,
        "TaskID" / Int32ul,
        "MaxWaitingTime" / Int32ul,
        "MaxBlockingTime" / Int32ul,
        "IDLETASK_PRIORITY" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=566, version=0)
class Microsoft_IEFRAME_566_0(Etw):
    pattern = Struct(
        "ISO_HANDLE" / Int64ul,
        "IDLEMANAGER_TASKTYPE" / Int32ul,
        "TaskID" / Int32ul,
        "MaxWaitingTime" / Int32ul,
        "MaxBlockingTime" / Int32ul,
        "IDLETASK_PRIORITY" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=567, version=0)
class Microsoft_IEFRAME_567_0(Etw):
    pattern = Struct(
        "ISO_HANDLE" / Int64ul,
        "IDLEMANAGER_TASKTYPE" / Int32ul,
        "TaskID" / Int32ul,
        "MaxWaitingTime" / Int32ul,
        "MaxBlockingTime" / Int32ul,
        "IDLETASK_PRIORITY" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=568, version=0)
class Microsoft_IEFRAME_568_0(Etw):
    pattern = Struct(
        "ISO_HANDLE" / Int64ul,
        "IDLEMANAGER_TASKTYPE" / Int32ul,
        "TaskID" / Int32ul,
        "MaxWaitingTime" / Int32ul,
        "MaxBlockingTime" / Int32ul,
        "IDLETASK_PRIORITY" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=569, version=0)
class Microsoft_IEFRAME_569_0(Etw):
    pattern = Struct(
        "ISO_HANDLE" / Int64ul,
        "IDLEMANAGER_TASKTYPE" / Int32ul,
        "TaskID" / Int32ul,
        "MaxWaitingTime" / Int32ul,
        "MaxBlockingTime" / Int32ul,
        "IDLETASK_PRIORITY" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=570, version=0)
class Microsoft_IEFRAME_570_0(Etw):
    pattern = Struct(
        "ISO_HANDLE" / Int64ul,
        "IDLEMANAGER_TASKTYPE" / Int32ul,
        "TaskID" / Int32ul,
        "MaxWaitingTime" / Int32ul,
        "MaxBlockingTime" / Int32ul,
        "IDLETASK_PRIORITY" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=571, version=0)
class Microsoft_IEFRAME_571_0(Etw):
    pattern = Struct(
        "WaitingTaskCount" / Int32ul,
        "RunningTaskCount" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=577, version=0)
class Microsoft_IEFRAME_577_0(Etw):
    pattern = Struct(
        "TabID" / Int32sl,
        "AllowRecovery" / Int8ul,
        "UseWER" / Int8ul,
        "HangUIShowing" / Int8ul,
        "Result" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=578, version=0)
class Microsoft_IEFRAME_578_0(Etw):
    pattern = Struct(
        "TabID" / Int32sl,
        "AllowRecovery" / Int8ul,
        "UseWER" / Int8ul,
        "HangUIShowing" / Int8ul,
        "Result" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=579, version=0)
class Microsoft_IEFRAME_579_0(Etw):
    pattern = Struct(
        "TabID" / Int32sl,
        "ProcessID" / Int32sl,
        "HWND" / Int64ul,
        "HungWindowText" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=580, version=0)
class Microsoft_IEFRAME_580_0(Etw):
    pattern = Struct(
        "TabID" / Int32sl,
        "ProcessID" / Int32sl,
        "HWND" / Int64ul,
        "HungWindowText" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=581, version=0)
class Microsoft_IEFRAME_581_0(Etw):
    pattern = Struct(
        "TabID" / Int32sl,
        "ProcessID" / Int32sl,
        "HWND" / Int64ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=582, version=0)
class Microsoft_IEFRAME_582_0(Etw):
    pattern = Struct(
        "TabID" / Int32sl,
        "TabVisibleIndex" / Int32sl
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=583, version=0)
class Microsoft_IEFRAME_583_0(Etw):
    pattern = Struct(
        "TabID" / Int32sl,
        "TabVisibleIndex" / Int32sl
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=584, version=0)
class Microsoft_IEFRAME_584_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=585, version=0)
class Microsoft_IEFRAME_585_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=589, version=0)
class Microsoft_IEFRAME_589_0(Etw):
    pattern = Struct(
        "BindContext" / Int64ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=590, version=0)
class Microsoft_IEFRAME_590_0(Etw):
    pattern = Struct(
        "BindContext" / Int64ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=592, version=0)
class Microsoft_IEFRAME_592_0(Etw):
    pattern = Struct(
        "TabID" / Int32sl,
        "IsActive" / Int8ul,
        "hwndAlternateOwner" / Int64ul,
        "fDestroyingHangUI" / Int8ul,
        "hwndNext" / Int64ul,
        "hwndPrev" / Int64ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=593, version=0)
class Microsoft_IEFRAME_593_0(Etw):
    pattern = Struct(
        "TabID" / Int32sl,
        "IsActive" / Int8ul,
        "hwndAlternateOwner" / Int64ul,
        "fDestroyingHangUI" / Int8ul,
        "hwndNext" / Int64ul,
        "hwndPrev" / Int64ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=594, version=0)
class Microsoft_IEFRAME_594_0(Etw):
    pattern = Struct(
        "TabID" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=597, version=0)
class Microsoft_IEFRAME_597_0(Etw):
    pattern = Struct(
        "TabID" / Int32sl,
        "IsActive" / Int8ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=598, version=0)
class Microsoft_IEFRAME_598_0(Etw):
    pattern = Struct(
        "TabID" / Int32sl,
        "IsActive" / Int8ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=599, version=0)
class Microsoft_IEFRAME_599_0(Etw):
    pattern = Struct(
        "TabID" / Int32sl,
        "IsActive" / Int8ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=602, version=0)
class Microsoft_IEFRAME_602_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=603, version=0)
class Microsoft_IEFRAME_603_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=606, version=0)
class Microsoft_IEFRAME_606_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=607, version=0)
class Microsoft_IEFRAME_607_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=608, version=0)
class Microsoft_IEFRAME_608_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=609, version=0)
class Microsoft_IEFRAME_609_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=610, version=0)
class Microsoft_IEFRAME_610_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=611, version=0)
class Microsoft_IEFRAME_611_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=612, version=0)
class Microsoft_IEFRAME_612_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=613, version=0)
class Microsoft_IEFRAME_613_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=614, version=0)
class Microsoft_IEFRAME_614_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=615, version=0)
class Microsoft_IEFRAME_615_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=642, version=0)
class Microsoft_IEFRAME_642_0(Etw):
    pattern = Struct(
        "SharedMemoryHandle" / Int32ul,
        "FailureReason" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=644, version=0)
class Microsoft_IEFRAME_644_0(Etw):
    pattern = Struct(
        "CommandType" / Int32sl,
        "EventType" / Int32sl
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=645, version=0)
class Microsoft_IEFRAME_645_0(Etw):
    pattern = Struct(
        "PID" / Int32ul,
        "FoundSuspendable" / Int8ul,
        "FailureReason" / Int32ul
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=648, version=0)
class Microsoft_IEFRAME_648_0(Etw):
    pattern = Struct(
        "tabID" / Int32sl
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=649, version=0)
class Microsoft_IEFRAME_649_0(Etw):
    pattern = Struct(
        "tabID" / Int32sl
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=650, version=0)
class Microsoft_IEFRAME_650_0(Etw):
    pattern = Struct(
        "tabID" / Int32sl
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=651, version=0)
class Microsoft_IEFRAME_651_0(Etw):
    pattern = Struct(
        "tabID" / Int32sl,
        "Title" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=652, version=0)
class Microsoft_IEFRAME_652_0(Etw):
    pattern = Struct(
        "HiddenTabCookie" / Int32sl
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=653, version=0)
class Microsoft_IEFRAME_653_0(Etw):
    pattern = Struct(
        "tabID" / Int32sl
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=654, version=0)
class Microsoft_IEFRAME_654_0(Etw):
    pattern = Struct(
        "tabID" / Int32sl
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=655, version=0)
class Microsoft_IEFRAME_655_0(Etw):
    pattern = Struct(
        "tabID" / Int32sl
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=656, version=0)
class Microsoft_IEFRAME_656_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=657, version=0)
class Microsoft_IEFRAME_657_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=658, version=0)
class Microsoft_IEFRAME_658_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=659, version=0)
class Microsoft_IEFRAME_659_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("5c8bb950-959e-4309-8908-67961a1205d5"), event_id=666, version=0)
class Microsoft_IEFRAME_666_0(Etw):
    pattern = Struct(
        "SharedMemoryHandle" / Int32ul,
        "FailureReason" / Int32ul
    )

