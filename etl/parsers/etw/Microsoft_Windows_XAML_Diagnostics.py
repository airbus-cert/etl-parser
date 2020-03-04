# -*- coding: utf-8 -*-
"""
Microsoft-Windows-XAML-Diagnostics
GUID : 59e7a714-73a4-4147-b47e-0957048c75c4
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=3, version=0)
class Microsoft_Windows_XAML_Diagnostics_3_0(Etw):
    pattern = Struct(
        "RegisterdOn" / Int64ul,
        "PointerDeviceType" / Int32ul,
        "OriginalSource" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=4, version=0)
class Microsoft_Windows_XAML_Diagnostics_4_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=5, version=0)
class Microsoft_Windows_XAML_Diagnostics_5_0(Etw):
    pattern = Struct(
        "RegisterdOn" / Int64ul,
        "PointerDeviceType" / Int32ul,
        "OriginalSource" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=6, version=0)
class Microsoft_Windows_XAML_Diagnostics_6_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=7, version=0)
class Microsoft_Windows_XAML_Diagnostics_7_0(Etw):
    pattern = Struct(
        "RegisterdOn" / Int64ul,
        "PointerDeviceType" / Int32ul,
        "OriginalSource" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=8, version=0)
class Microsoft_Windows_XAML_Diagnostics_8_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=9, version=0)
class Microsoft_Windows_XAML_Diagnostics_9_0(Etw):
    pattern = Struct(
        "RegisterdOn" / Int64ul,
        "PointerDeviceType" / Int32ul,
        "OriginalSource" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=10, version=0)
class Microsoft_Windows_XAML_Diagnostics_10_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=11, version=0)
class Microsoft_Windows_XAML_Diagnostics_11_0(Etw):
    pattern = Struct(
        "RegisterdOn" / Int64ul,
        "PointerDeviceType" / Int32ul,
        "OriginalSource" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=13, version=0)
class Microsoft_Windows_XAML_Diagnostics_13_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=14, version=0)
class Microsoft_Windows_XAML_Diagnostics_14_0(Etw):
    pattern = Struct(
        "RegisterdOn" / Int64ul,
        "PointerDeviceType" / Int32ul,
        "OriginalSource" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=15, version=0)
class Microsoft_Windows_XAML_Diagnostics_15_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=16, version=0)
class Microsoft_Windows_XAML_Diagnostics_16_0(Etw):
    pattern = Struct(
        "RegisterdOn" / Int64ul,
        "PointerDeviceType" / Int32ul,
        "OriginalSource" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=17, version=0)
class Microsoft_Windows_XAML_Diagnostics_17_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=18, version=0)
class Microsoft_Windows_XAML_Diagnostics_18_0(Etw):
    pattern = Struct(
        "RegisterdOn" / Int64ul,
        "PointerDeviceType" / Int32ul,
        "OriginalSource" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=19, version=0)
class Microsoft_Windows_XAML_Diagnostics_19_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=20, version=0)
class Microsoft_Windows_XAML_Diagnostics_20_0(Etw):
    pattern = Struct(
        "RegisterdOn" / Int64ul,
        "PointerDeviceType" / Int32ul,
        "OriginalSource" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=21, version=0)
class Microsoft_Windows_XAML_Diagnostics_21_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=22, version=0)
class Microsoft_Windows_XAML_Diagnostics_22_0(Etw):
    pattern = Struct(
        "RegisterdOn" / Int64ul,
        "PointerDeviceType" / Int32ul,
        "OriginalSource" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=23, version=0)
class Microsoft_Windows_XAML_Diagnostics_23_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=24, version=0)
class Microsoft_Windows_XAML_Diagnostics_24_0(Etw):
    pattern = Struct(
        "RegisterdOn" / Int64ul,
        "PointerDeviceType" / Int32ul,
        "OriginalSource" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=25, version=0)
class Microsoft_Windows_XAML_Diagnostics_25_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=26, version=0)
class Microsoft_Windows_XAML_Diagnostics_26_0(Etw):
    pattern = Struct(
        "RegisterdOn" / Int64ul,
        "PointerDeviceType" / Int32ul,
        "OriginalSource" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=27, version=0)
class Microsoft_Windows_XAML_Diagnostics_27_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=28, version=0)
class Microsoft_Windows_XAML_Diagnostics_28_0(Etw):
    pattern = Struct(
        "RegisterdOn" / Int64ul,
        "OriginalSource" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=29, version=0)
class Microsoft_Windows_XAML_Diagnostics_29_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=30, version=0)
class Microsoft_Windows_XAML_Diagnostics_30_0(Etw):
    pattern = Struct(
        "RegisterdOn" / Int64ul,
        "OriginalSource" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=31, version=0)
class Microsoft_Windows_XAML_Diagnostics_31_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=32, version=0)
class Microsoft_Windows_XAML_Diagnostics_32_0(Etw):
    pattern = Struct(
        "RegisterdOn" / Int64ul,
        "OriginalSource" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=33, version=0)
class Microsoft_Windows_XAML_Diagnostics_33_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=34, version=0)
class Microsoft_Windows_XAML_Diagnostics_34_0(Etw):
    pattern = Struct(
        "RegisterdOn" / Int64ul,
        "OriginalSource" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=35, version=0)
class Microsoft_Windows_XAML_Diagnostics_35_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=36, version=0)
class Microsoft_Windows_XAML_Diagnostics_36_0(Etw):
    pattern = Struct(
        "RegisterdOn" / Int64ul,
        "OriginalSource" / Int64ul,
        "Container" / Int64ul,
        "Mode" / Int32ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=37, version=0)
class Microsoft_Windows_XAML_Diagnostics_37_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=38, version=0)
class Microsoft_Windows_XAML_Diagnostics_38_0(Etw):
    pattern = Struct(
        "RegisterdOn" / Int64ul,
        "OriginalSource" / Int64ul,
        "Container" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=39, version=0)
class Microsoft_Windows_XAML_Diagnostics_39_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=40, version=0)
class Microsoft_Windows_XAML_Diagnostics_40_0(Etw):
    pattern = Struct(
        "RegisterdOn" / Int64ul,
        "OriginalSource" / Int64ul,
        "Container" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=41, version=0)
class Microsoft_Windows_XAML_Diagnostics_41_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=42, version=0)
class Microsoft_Windows_XAML_Diagnostics_42_0(Etw):
    pattern = Struct(
        "RegisterdOn" / Int64ul,
        "OriginalSource" / Int64ul,
        "Container" / Int64ul,
        "IsInertial" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=43, version=0)
class Microsoft_Windows_XAML_Diagnostics_43_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=44, version=0)
class Microsoft_Windows_XAML_Diagnostics_44_0(Etw):
    pattern = Struct(
        "RegisterdOn" / Int64ul,
        "OriginalSource" / Int64ul,
        "Container" / Int64ul,
        "IsInertial" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=45, version=0)
class Microsoft_Windows_XAML_Diagnostics_45_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=54, version=0)
class Microsoft_Windows_XAML_Diagnostics_54_0(Etw):
    pattern = Struct(
        "AppBarType" / Int32ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=56, version=0)
class Microsoft_Windows_XAML_Diagnostics_56_0(Etw):
    pattern = Struct(
        "AppBarType" / Int32ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=58, version=0)
class Microsoft_Windows_XAML_Diagnostics_58_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=59, version=0)
class Microsoft_Windows_XAML_Diagnostics_59_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=60, version=0)
class Microsoft_Windows_XAML_Diagnostics_60_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=61, version=0)
class Microsoft_Windows_XAML_Diagnostics_61_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=62, version=0)
class Microsoft_Windows_XAML_Diagnostics_62_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=63, version=0)
class Microsoft_Windows_XAML_Diagnostics_63_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul,
        "PropertyName" / WString,
        "PropertyEffect" / Int32ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=63, version=1)
class Microsoft_Windows_XAML_Diagnostics_63_1(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul,
        "PropertyName" / WString,
        "PropertyEffect" / Int32ul,
        "ValueInt" / Int64ul,
        "ValueString" / WString,
        "ValueDouble" / Double
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=64, version=0)
class Microsoft_Windows_XAML_Diagnostics_64_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=65, version=0)
class Microsoft_Windows_XAML_Diagnostics_65_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=66, version=0)
class Microsoft_Windows_XAML_Diagnostics_66_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=67, version=0)
class Microsoft_Windows_XAML_Diagnostics_67_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=68, version=0)
class Microsoft_Windows_XAML_Diagnostics_68_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul,
        "PropertyName" / WString
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=69, version=0)
class Microsoft_Windows_XAML_Diagnostics_69_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul,
        "PropertyName" / WString
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=70, version=0)
class Microsoft_Windows_XAML_Diagnostics_70_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul,
        "PropertyName" / WString
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=71, version=0)
class Microsoft_Windows_XAML_Diagnostics_71_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul,
        "PropertyName" / WString
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=72, version=0)
class Microsoft_Windows_XAML_Diagnostics_72_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul,
        "PropertyName" / WString,
        "ModelTypeName" / WString,
        "ModelPropertyName" / WString
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=72, version=1)
class Microsoft_Windows_XAML_Diagnostics_72_1(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul,
        "PropertyName" / WString,
        "ModelTypeName" / WString,
        "ModelPropertyName" / WString,
        "IsPropertyTemplateBound" / Int8ul,
        "EffectiveSourceType" / Int32ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=73, version=0)
class Microsoft_Windows_XAML_Diagnostics_73_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul,
        "PropertyName" / WString
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=74, version=0)
class Microsoft_Windows_XAML_Diagnostics_74_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul,
        "PropertyName" / WString,
        "ModelTypeName" / WString,
        "ModelPropertyName" / WString
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=75, version=0)
class Microsoft_Windows_XAML_Diagnostics_75_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul,
        "PropertyName" / WString
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=76, version=0)
class Microsoft_Windows_XAML_Diagnostics_76_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul,
        "PropertyName" / WString
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=77, version=0)
class Microsoft_Windows_XAML_Diagnostics_77_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul,
        "PropertyName" / WString
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=78, version=0)
class Microsoft_Windows_XAML_Diagnostics_78_0(Etw):
    pattern = Struct(
        "PropertyName" / WString
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=83, version=0)
class Microsoft_Windows_XAML_Diagnostics_83_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "FileURI" / WString,
        "LineNumber" / Int32ul,
        "ColumnNumber" / Int32ul,
        "FileHash" / WString
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=83, version=1)
class Microsoft_Windows_XAML_Diagnostics_83_1(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ClassName" / WString,
        "FileURI" / WString,
        "LineNumber" / Int32ul,
        "ColumnNumber" / Int32ul,
        "FileHash" / WString
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=84, version=0)
class Microsoft_Windows_XAML_Diagnostics_84_0(Etw):
    pattern = Struct(
        "ResourceDictionaryId" / Int64ul,
        "ResourceId" / Int64ul,
        "FileURI" / WString,
        "LineNumber" / Int32ul,
        "ColumnNumber" / Int32ul,
        "FileHash" / WString
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=85, version=0)
class Microsoft_Windows_XAML_Diagnostics_85_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "TargetElementId" / Int64ul,
        "FileURI" / WString,
        "LineNumber" / Int32ul,
        "ColumnNumber" / Int32ul,
        "FileHash" / WString
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=88, version=0)
class Microsoft_Windows_XAML_Diagnostics_88_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul,
        "Name" / WString
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=89, version=0)
class Microsoft_Windows_XAML_Diagnostics_89_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul,
        "Name" / WString,
        "Type" / WString
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=90, version=0)
class Microsoft_Windows_XAML_Diagnostics_90_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul,
        "Name" / WString,
        "Type" / WString
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=91, version=0)
class Microsoft_Windows_XAML_Diagnostics_91_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ParentId" / Int64ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=94, version=0)
class Microsoft_Windows_XAML_Diagnostics_94_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=95, version=0)
class Microsoft_Windows_XAML_Diagnostics_95_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ViewId" / Int32ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=96, version=0)
class Microsoft_Windows_XAML_Diagnostics_96_0(Etw):
    pattern = Struct(
        "ViewId" / Int32ul,
        "Width" / Float32l,
        "Height" / Float32l
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=97, version=0)
class Microsoft_Windows_XAML_Diagnostics_97_0(Etw):
    pattern = Struct(
        "ViewId" / Int32ul,
        "State" / WString
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=99, version=0)
class Microsoft_Windows_XAML_Diagnostics_99_0(Etw):
    pattern = Struct(
        "ViewId" / Int32sl
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=100, version=0)
class Microsoft_Windows_XAML_Diagnostics_100_0(Etw):
    pattern = Struct(
        "Context" / Int32ul,
        "ViewId" / Int32ul
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=102, version=0)
class Microsoft_Windows_XAML_Diagnostics_102_0(Etw):
    pattern = Struct(
        "AppId" / WString
    )


@declare(guid=guid("59e7a714-73a4-4147-b47e-0957048c75c4"), event_id=103, version=0)
class Microsoft_Windows_XAML_Diagnostics_103_0(Etw):
    pattern = Struct(
        "Context" / Int32ul,
        "ViewId" / Int32ul
    )

