# -*- coding: utf-8 -*-
"""
Microsoft-Windows-PrintBRM
GUID : cf3f502e-b40d-4071-996f-00981edf938e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=3, version=0)
class Microsoft_Windows_PrintBRM_3_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "NewDriver" / WString,
        "PrinterName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=4, version=0)
class Microsoft_Windows_PrintBRM_4_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=6, version=0)
class Microsoft_Windows_PrintBRM_6_0(Etw):
    pattern = Struct(
        "PrinterName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=7, version=0)
class Microsoft_Windows_PrintBRM_7_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=8, version=0)
class Microsoft_Windows_PrintBRM_8_0(Etw):
    pattern = Struct(
        "PrinterName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=9, version=0)
class Microsoft_Windows_PrintBRM_9_0(Etw):
    pattern = Struct(
        "PrinterName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=10, version=0)
class Microsoft_Windows_PrintBRM_10_0(Etw):
    pattern = Struct(
        "PrinterName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=11, version=0)
class Microsoft_Windows_PrintBRM_11_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "PortName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=12, version=0)
class Microsoft_Windows_PrintBRM_12_0(Etw):
    pattern = Struct(
        "PrinterName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=13, version=0)
class Microsoft_Windows_PrintBRM_13_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=14, version=0)
class Microsoft_Windows_PrintBRM_14_0(Etw):
    pattern = Struct(
        "PrintProcessorName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=15, version=0)
class Microsoft_Windows_PrintBRM_15_0(Etw):
    pattern = Struct(
        "PrintProcessorName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=16, version=0)
class Microsoft_Windows_PrintBRM_16_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=17, version=0)
class Microsoft_Windows_PrintBRM_17_0(Etw):
    pattern = Struct(
        "LanguageMonitor" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=18, version=0)
class Microsoft_Windows_PrintBRM_18_0(Etw):
    pattern = Struct(
        "LanguageMonitor" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=19, version=0)
class Microsoft_Windows_PrintBRM_19_0(Etw):
    pattern = Struct(
        "SourceArchitecture" / WString,
        "TargetArchitecture" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=20, version=0)
class Microsoft_Windows_PrintBRM_20_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "TargetServerArchitecture" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=21, version=0)
class Microsoft_Windows_PrintBRM_21_0(Etw):
    pattern = Struct(
        "DriverName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=22, version=0)
class Microsoft_Windows_PrintBRM_22_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "TargetServerArchitecture" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=23, version=0)
class Microsoft_Windows_PrintBRM_23_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "Architecture" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=24, version=0)
class Microsoft_Windows_PrintBRM_24_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "Architecture" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=25, version=0)
class Microsoft_Windows_PrintBRM_25_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "Architecture" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=26, version=0)
class Microsoft_Windows_PrintBRM_26_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "Architecture" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=27, version=0)
class Microsoft_Windows_PrintBRM_27_0(Etw):
    pattern = Struct(
        "DirectoryName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=28, version=0)
class Microsoft_Windows_PrintBRM_28_0(Etw):
    pattern = Struct(
        "Source" / WString,
        "Destination" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=29, version=0)
class Microsoft_Windows_PrintBRM_29_0(Etw):
    pattern = Struct(
        "Port" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=30, version=0)
class Microsoft_Windows_PrintBRM_30_0(Etw):
    pattern = Struct(
        "PortName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=31, version=0)
class Microsoft_Windows_PrintBRM_31_0(Etw):
    pattern = Struct(
        "PortName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=32, version=0)
class Microsoft_Windows_PrintBRM_32_0(Etw):
    pattern = Struct(
        "Status" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=35, version=0)
class Microsoft_Windows_PrintBRM_35_0(Etw):
    pattern = Struct(
        "NumberOfForms" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=38, version=0)
class Microsoft_Windows_PrintBRM_38_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=39, version=0)
class Microsoft_Windows_PrintBRM_39_0(Etw):
    pattern = Struct(
        "PluginDllName" / WString,
        "ProcessorName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=40, version=0)
class Microsoft_Windows_PrintBRM_40_0(Etw):
    pattern = Struct(
        "FolderName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=41, version=0)
class Microsoft_Windows_PrintBRM_41_0(Etw):
    pattern = Struct(
        "FolderName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=42, version=0)
class Microsoft_Windows_PrintBRM_42_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=43, version=0)
class Microsoft_Windows_PrintBRM_43_0(Etw):
    pattern = Struct(
        "LogLevel" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=44, version=0)
class Microsoft_Windows_PrintBRM_44_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=45, version=0)
class Microsoft_Windows_PrintBRM_45_0(Etw):
    pattern = Struct(
        "ServerName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=46, version=0)
class Microsoft_Windows_PrintBRM_46_0(Etw):
    pattern = Struct(
        "CabFileName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=47, version=0)
class Microsoft_Windows_PrintBRM_47_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=48, version=0)
class Microsoft_Windows_PrintBRM_48_0(Etw):
    pattern = Struct(
        "PluginDllName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=49, version=0)
class Microsoft_Windows_PrintBRM_49_0(Etw):
    pattern = Struct(
        "PluginDllName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=50, version=0)
class Microsoft_Windows_PrintBRM_50_0(Etw):
    pattern = Struct(
        "PluginDllName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=51, version=0)
class Microsoft_Windows_PrintBRM_51_0(Etw):
    pattern = Struct(
        "PluginDllName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=52, version=0)
class Microsoft_Windows_PrintBRM_52_0(Etw):
    pattern = Struct(
        "ProcessorName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=53, version=0)
class Microsoft_Windows_PrintBRM_53_0(Etw):
    pattern = Struct(
        "FunctionName" / WString,
        "ComputerName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=54, version=0)
class Microsoft_Windows_PrintBRM_54_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ServerName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=55, version=0)
class Microsoft_Windows_PrintBRM_55_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ServerName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=56, version=0)
class Microsoft_Windows_PrintBRM_56_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ComputerName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=57, version=0)
class Microsoft_Windows_PrintBRM_57_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ComputerName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=58, version=0)
class Microsoft_Windows_PrintBRM_58_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=59, version=0)
class Microsoft_Windows_PrintBRM_59_0(Etw):
    pattern = Struct(
        "SourceFile" / WString,
        "DestinationFile" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=60, version=0)
class Microsoft_Windows_PrintBRM_60_0(Etw):
    pattern = Struct(
        "SourceFile" / WString,
        "DestinationFile" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=61, version=0)
class Microsoft_Windows_PrintBRM_61_0(Etw):
    pattern = Struct(
        "HostName" / WString,
        "DeviceSection" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=62, version=0)
class Microsoft_Windows_PrintBRM_62_0(Etw):
    pattern = Struct(
        "PortName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=63, version=0)
class Microsoft_Windows_PrintBRM_63_0(Etw):
    pattern = Struct(
        "Port" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=64, version=0)
class Microsoft_Windows_PrintBRM_64_0(Etw):
    pattern = Struct(
        "Port" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=65, version=0)
class Microsoft_Windows_PrintBRM_65_0(Etw):
    pattern = Struct(
        "KeyName" / WString,
        "ValueName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=66, version=0)
class Microsoft_Windows_PrintBRM_66_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "PortName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=67, version=0)
class Microsoft_Windows_PrintBRM_67_0(Etw):
    pattern = Struct(
        "KeyName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=68, version=0)
class Microsoft_Windows_PrintBRM_68_0(Etw):
    pattern = Struct(
        "PathName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=69, version=0)
class Microsoft_Windows_PrintBRM_69_0(Etw):
    pattern = Struct(
        "Address" / WString,
        "PortName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=70, version=0)
class Microsoft_Windows_PrintBRM_70_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=71, version=0)
class Microsoft_Windows_PrintBRM_71_0(Etw):
    pattern = Struct(
        "ComputerName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=72, version=0)
class Microsoft_Windows_PrintBRM_72_0(Etw):
    pattern = Struct(
        "ComputerName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=73, version=0)
class Microsoft_Windows_PrintBRM_73_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=74, version=0)
class Microsoft_Windows_PrintBRM_74_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "Architecture" / WString
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=75, version=0)
class Microsoft_Windows_PrintBRM_75_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "Architecture" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=76, version=0)
class Microsoft_Windows_PrintBRM_76_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "Architecture" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=77, version=0)
class Microsoft_Windows_PrintBRM_77_0(Etw):
    pattern = Struct(
        "PortName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=78, version=0)
class Microsoft_Windows_PrintBRM_78_0(Etw):
    pattern = Struct(
        "PrintProcessorName" / WString,
        "PrintProcessorArchitecture" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=79, version=0)
class Microsoft_Windows_PrintBRM_79_0(Etw):
    pattern = Struct(
        "PrintProcessorArchitecture" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=80, version=0)
class Microsoft_Windows_PrintBRM_80_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=81, version=0)
class Microsoft_Windows_PrintBRM_81_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=82, version=0)
class Microsoft_Windows_PrintBRM_82_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("cf3f502e-b40d-4071-996f-00981edf938e"), event_id=83, version=0)
class Microsoft_Windows_PrintBRM_83_0(Etw):
    pattern = Struct(
        "Port" / WString,
        "ErrorCode" / Int32ul
    )

