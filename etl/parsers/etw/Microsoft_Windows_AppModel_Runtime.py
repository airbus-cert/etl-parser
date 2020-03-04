# -*- coding: utf-8 -*-
"""
Microsoft-Windows-AppModel-Runtime
GUID : f1ef270a-0d32-4352-ba52-dbab41e1d859
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=1, version=0)
class Microsoft_Windows_AppModel_Runtime_1_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "CreateTime" / Int64ul,
        "ParentProcessID" / Int32ul,
        "PackageFullName" / WString,
        "ImageName" / WString,
        "PackageRelativeApplicationId" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=2, version=0)
class Microsoft_Windows_AppModel_Runtime_2_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=3, version=0)
class Microsoft_Windows_AppModel_Runtime_3_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=4, version=0)
class Microsoft_Windows_AppModel_Runtime_4_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=5, version=0)
class Microsoft_Windows_AppModel_Runtime_5_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=6, version=0)
class Microsoft_Windows_AppModel_Runtime_6_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=7, version=0)
class Microsoft_Windows_AppModel_Runtime_7_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=8, version=0)
class Microsoft_Windows_AppModel_Runtime_8_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul,
        "FailedBinary" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=9, version=0)
class Microsoft_Windows_AppModel_Runtime_9_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul,
        "FailedBinary" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=11, version=0)
class Microsoft_Windows_AppModel_Runtime_11_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul,
        "FailedBinary" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=12, version=0)
class Microsoft_Windows_AppModel_Runtime_12_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=14, version=0)
class Microsoft_Windows_AppModel_Runtime_14_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ErrorCode" / Int32sl,
        "Size" / Int64ul,
        "Offset" / Int32ul,
        "HeaderAddr" / Int64ul,
        "Section" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=15, version=0)
class Microsoft_Windows_AppModel_Runtime_15_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ErrorCode" / Int32sl,
        "Size" / Int64ul,
        "HeaderAddr" / Int64ul,
        "Section" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=16, version=0)
class Microsoft_Windows_AppModel_Runtime_16_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ErrorCode" / Int32sl,
        "Size" / Int64ul,
        "Offset" / Int32ul,
        "HeaderAddr" / Int64ul,
        "Section" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=17, version=0)
class Microsoft_Windows_AppModel_Runtime_17_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ErrorCode" / Int32sl,
        "Size" / Int64ul,
        "Offset" / Int32ul,
        "HeaderAddr" / Int64ul,
        "Section" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=18, version=0)
class Microsoft_Windows_AppModel_Runtime_18_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ErrorCode" / Int32sl,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=19, version=0)
class Microsoft_Windows_AppModel_Runtime_19_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ExceptionCode" / Int32sl
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=20, version=0)
class Microsoft_Windows_AppModel_Runtime_20_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=21, version=0)
class Microsoft_Windows_AppModel_Runtime_21_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=22, version=0)
class Microsoft_Windows_AppModel_Runtime_22_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=23, version=0)
class Microsoft_Windows_AppModel_Runtime_23_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=24, version=0)
class Microsoft_Windows_AppModel_Runtime_24_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=25, version=0)
class Microsoft_Windows_AppModel_Runtime_25_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=26, version=0)
class Microsoft_Windows_AppModel_Runtime_26_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=27, version=0)
class Microsoft_Windows_AppModel_Runtime_27_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=28, version=0)
class Microsoft_Windows_AppModel_Runtime_28_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=29, version=0)
class Microsoft_Windows_AppModel_Runtime_29_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=30, version=0)
class Microsoft_Windows_AppModel_Runtime_30_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=31, version=0)
class Microsoft_Windows_AppModel_Runtime_31_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=32, version=0)
class Microsoft_Windows_AppModel_Runtime_32_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=33, version=0)
class Microsoft_Windows_AppModel_Runtime_33_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=34, version=0)
class Microsoft_Windows_AppModel_Runtime_34_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=35, version=0)
class Microsoft_Windows_AppModel_Runtime_35_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=36, version=0)
class Microsoft_Windows_AppModel_Runtime_36_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=37, version=0)
class Microsoft_Windows_AppModel_Runtime_37_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=38, version=0)
class Microsoft_Windows_AppModel_Runtime_38_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=39, version=0)
class Microsoft_Windows_AppModel_Runtime_39_0(Etw):
    pattern = Struct(
        "AppContainerName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=40, version=0)
class Microsoft_Windows_AppModel_Runtime_40_0(Etw):
    pattern = Struct(
        "AppContainerName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=41, version=0)
class Microsoft_Windows_AppModel_Runtime_41_0(Etw):
    pattern = Struct(
        "AppContainerName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=42, version=0)
class Microsoft_Windows_AppModel_Runtime_42_0(Etw):
    pattern = Struct(
        "AppContainerName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=43, version=0)
class Microsoft_Windows_AppModel_Runtime_43_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ErrorCode" / Int32sl,
        "Size" / Int64ul,
        "HeaderAddr" / Int64ul,
        "ApplicationUserModelId" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=44, version=0)
class Microsoft_Windows_AppModel_Runtime_44_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ErrorCode" / Int32sl,
        "Size" / Int64ul,
        "HeaderAddr" / Int64ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=45, version=0)
class Microsoft_Windows_AppModel_Runtime_45_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=46, version=0)
class Microsoft_Windows_AppModel_Runtime_46_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=47, version=0)
class Microsoft_Windows_AppModel_Runtime_47_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=48, version=0)
class Microsoft_Windows_AppModel_Runtime_48_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=49, version=0)
class Microsoft_Windows_AppModel_Runtime_49_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=50, version=0)
class Microsoft_Windows_AppModel_Runtime_50_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=51, version=0)
class Microsoft_Windows_AppModel_Runtime_51_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=52, version=0)
class Microsoft_Windows_AppModel_Runtime_52_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=53, version=0)
class Microsoft_Windows_AppModel_Runtime_53_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=54, version=0)
class Microsoft_Windows_AppModel_Runtime_54_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=55, version=0)
class Microsoft_Windows_AppModel_Runtime_55_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=56, version=0)
class Microsoft_Windows_AppModel_Runtime_56_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=57, version=0)
class Microsoft_Windows_AppModel_Runtime_57_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "PackageFullName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=58, version=0)
class Microsoft_Windows_AppModel_Runtime_58_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "PackageFullName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=59, version=0)
class Microsoft_Windows_AppModel_Runtime_59_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "PackageFullName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=60, version=0)
class Microsoft_Windows_AppModel_Runtime_60_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=61, version=0)
class Microsoft_Windows_AppModel_Runtime_61_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=62, version=0)
class Microsoft_Windows_AppModel_Runtime_62_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "PackageFullName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=63, version=0)
class Microsoft_Windows_AppModel_Runtime_63_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Resource" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=64, version=0)
class Microsoft_Windows_AppModel_Runtime_64_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Resource" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=65, version=0)
class Microsoft_Windows_AppModel_Runtime_65_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "PackageFullName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=66, version=0)
class Microsoft_Windows_AppModel_Runtime_66_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "PackageFullName" / WString,
        "User" / Sid
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=67, version=0)
class Microsoft_Windows_AppModel_Runtime_67_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "PackageFullName" / WString,
        "DesiredStatus" / Int32ul,
        "CurrentStatus" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=68, version=0)
class Microsoft_Windows_AppModel_Runtime_68_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "DesiredStatus" / Int32ul,
        "CurrentStatus" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=69, version=0)
class Microsoft_Windows_AppModel_Runtime_69_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "PackageFullName" / WString,
        "User" / Sid,
        "DesiredStatus" / Int32ul,
        "CurrentStatus" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=70, version=0)
class Microsoft_Windows_AppModel_Runtime_70_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "User" / Sid,
        "DesiredStatus" / Int32ul,
        "CurrentStatus" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=71, version=0)
class Microsoft_Windows_AppModel_Runtime_71_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=73, version=0)
class Microsoft_Windows_AppModel_Runtime_73_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=74, version=0)
class Microsoft_Windows_AppModel_Runtime_74_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ErrorCode" / Int32sl,
        "Type" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=75, version=0)
class Microsoft_Windows_AppModel_Runtime_75_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=76, version=0)
class Microsoft_Windows_AppModel_Runtime_76_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "Key" / WString,
        "Subkey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=77, version=0)
class Microsoft_Windows_AppModel_Runtime_77_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "Key" / WString,
        "Subkey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=78, version=0)
class Microsoft_Windows_AppModel_Runtime_78_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "Key" / WString,
        "Subkey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=79, version=0)
class Microsoft_Windows_AppModel_Runtime_79_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=80, version=0)
class Microsoft_Windows_AppModel_Runtime_80_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=101, version=0)
class Microsoft_Windows_AppModel_Runtime_101_0(Etw):
    pattern = Struct(
        "AppContainerName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=102, version=0)
class Microsoft_Windows_AppModel_Runtime_102_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=103, version=0)
class Microsoft_Windows_AppModel_Runtime_103_0(Etw):
    pattern = Struct(
        "AppContainerName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=104, version=0)
class Microsoft_Windows_AppModel_Runtime_104_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=105, version=0)
class Microsoft_Windows_AppModel_Runtime_105_0(Etw):
    pattern = Struct(
        "AppContainerName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=106, version=0)
class Microsoft_Windows_AppModel_Runtime_106_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=107, version=0)
class Microsoft_Windows_AppModel_Runtime_107_0(Etw):
    pattern = Struct(
        "AppContainerName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=108, version=0)
class Microsoft_Windows_AppModel_Runtime_108_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=109, version=0)
class Microsoft_Windows_AppModel_Runtime_109_0(Etw):
    pattern = Struct(
        "AppContainerName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=110, version=0)
class Microsoft_Windows_AppModel_Runtime_110_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=111, version=0)
class Microsoft_Windows_AppModel_Runtime_111_0(Etw):
    pattern = Struct(
        "AppContainerName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=112, version=0)
class Microsoft_Windows_AppModel_Runtime_112_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=113, version=0)
class Microsoft_Windows_AppModel_Runtime_113_0(Etw):
    pattern = Struct(
        "AppContainerName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=114, version=0)
class Microsoft_Windows_AppModel_Runtime_114_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=115, version=0)
class Microsoft_Windows_AppModel_Runtime_115_0(Etw):
    pattern = Struct(
        "AppContainerName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=116, version=0)
class Microsoft_Windows_AppModel_Runtime_116_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=117, version=0)
class Microsoft_Windows_AppModel_Runtime_117_0(Etw):
    pattern = Struct(
        "AppContainerName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=118, version=0)
class Microsoft_Windows_AppModel_Runtime_118_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=119, version=0)
class Microsoft_Windows_AppModel_Runtime_119_0(Etw):
    pattern = Struct(
        "AppContainerName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=120, version=0)
class Microsoft_Windows_AppModel_Runtime_120_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=121, version=0)
class Microsoft_Windows_AppModel_Runtime_121_0(Etw):
    pattern = Struct(
        "AppContainerName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=122, version=0)
class Microsoft_Windows_AppModel_Runtime_122_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=123, version=0)
class Microsoft_Windows_AppModel_Runtime_123_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=124, version=0)
class Microsoft_Windows_AppModel_Runtime_124_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "PackageFullName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=125, version=0)
class Microsoft_Windows_AppModel_Runtime_125_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=126, version=0)
class Microsoft_Windows_AppModel_Runtime_126_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "PackageFullName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=127, version=0)
class Microsoft_Windows_AppModel_Runtime_127_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=128, version=0)
class Microsoft_Windows_AppModel_Runtime_128_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "PackageFullName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=129, version=0)
class Microsoft_Windows_AppModel_Runtime_129_0(Etw):
    pattern = Struct(
        "AppContainerName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=130, version=0)
class Microsoft_Windows_AppModel_Runtime_130_0(Etw):
    pattern = Struct(
        "AppContainerName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=131, version=0)
class Microsoft_Windows_AppModel_Runtime_131_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=201, version=0)
class Microsoft_Windows_AppModel_Runtime_201_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "PackageName" / WString,
        "ImageName" / WString,
        "ApplicationName" / WString,
        "Message" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=202, version=0)
class Microsoft_Windows_AppModel_Runtime_202_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "ImageName" / WString,
        "ApplicationName" / WString,
        "ErrorCode" / Int32ul,
        "Message" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=203, version=0)
class Microsoft_Windows_AppModel_Runtime_203_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "ImageName" / WString,
        "ApplicationName" / WString,
        "ErrorCode" / Int32ul,
        "Message" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=204, version=0)
class Microsoft_Windows_AppModel_Runtime_204_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "ImageName" / WString,
        "ApplicationName" / WString,
        "ErrorCode" / Int32ul,
        "Message" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=205, version=0)
class Microsoft_Windows_AppModel_Runtime_205_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "ImageName" / WString,
        "ApplicationName" / WString,
        "ErrorCode" / Int32ul,
        "Message" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=206, version=0)
class Microsoft_Windows_AppModel_Runtime_206_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "ImageName" / WString,
        "ApplicationName" / WString,
        "ErrorCode" / Int32ul,
        "Message" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=207, version=0)
class Microsoft_Windows_AppModel_Runtime_207_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "ImageName" / WString,
        "ApplicationName" / WString,
        "ErrorCode" / Int32ul,
        "Message" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=208, version=0)
class Microsoft_Windows_AppModel_Runtime_208_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "ImageName" / WString,
        "ApplicationName" / WString,
        "ErrorCode" / Int32ul,
        "Message" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=209, version=0)
class Microsoft_Windows_AppModel_Runtime_209_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "ImageName" / WString,
        "ApplicationName" / WString,
        "ErrorCode" / Int32ul,
        "Message" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=210, version=0)
class Microsoft_Windows_AppModel_Runtime_210_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "ContainerName" / WString,
        "ContainerId" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=211, version=0)
class Microsoft_Windows_AppModel_Runtime_211_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "PackageName" / WString,
        "ContainerId" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=212, version=0)
class Microsoft_Windows_AppModel_Runtime_212_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ProcessID" / Int32ul,
        "PackageName" / WString,
        "ContainerId" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=213, version=0)
class Microsoft_Windows_AppModel_Runtime_213_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "PackageName" / WString,
        "ContainerName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=214, version=0)
class Microsoft_Windows_AppModel_Runtime_214_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "PackageName" / WString,
        "ContainerName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=215, version=0)
class Microsoft_Windows_AppModel_Runtime_215_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "PackageName" / WString,
        "ContainerName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=216, version=0)
class Microsoft_Windows_AppModel_Runtime_216_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "PackageName" / WString,
        "ContainerName" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=217, version=0)
class Microsoft_Windows_AppModel_Runtime_217_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "ContainerId" / WString
    )


@declare(guid=guid("f1ef270a-0d32-4352-ba52-dbab41e1d859"), event_id=218, version=0)
class Microsoft_Windows_AppModel_Runtime_218_0(Etw):
    pattern = Struct(
        "CleanupContainerErrorCode" / Int32ul,
        "MakeTemporaryErrorCode" / Int32ul,
        "PackageName" / WString,
        "ContainerId" / WString
    )

