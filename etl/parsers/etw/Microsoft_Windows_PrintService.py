# -*- coding: utf-8 -*-
"""
Microsoft-Windows-PrintService
GUID : 747ef6fd-e535-4d16-b510-42c90f6873a1
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=99, version=0)
class Microsoft_Windows_PrintService_99_0(Etw):
    pattern = Struct(
        "OperationCode" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=100, version=0)
class Microsoft_Windows_PrintService_100_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "PrinterName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=101, version=0)
class Microsoft_Windows_PrintService_101_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "PrinterName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=104, version=0)
class Microsoft_Windows_PrintService_104_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "PrinterName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=105, version=0)
class Microsoft_Windows_PrintService_105_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "PrinterName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=106, version=0)
class Microsoft_Windows_PrintService_106_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "JobID" / Int32ul,
        "PrinterName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=107, version=0)
class Microsoft_Windows_PrintService_107_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "JobID" / Int32ul,
        "PrinterName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=110, version=0)
class Microsoft_Windows_PrintService_110_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "JobID" / Int32ul,
        "PrinterName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=111, version=0)
class Microsoft_Windows_PrintService_111_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "JobID" / Int32ul,
        "PrinterName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=114, version=0)
class Microsoft_Windows_PrintService_114_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "ObjectName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=115, version=0)
class Microsoft_Windows_PrintService_115_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "ObjectName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=118, version=0)
class Microsoft_Windows_PrintService_118_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "ObjectName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=119, version=0)
class Microsoft_Windows_PrintService_119_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "ObjectName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=122, version=0)
class Microsoft_Windows_PrintService_122_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "JobID" / Int32ul,
        "PrinterName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=123, version=0)
class Microsoft_Windows_PrintService_123_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "JobID" / Int32ul,
        "PrinterName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=124, version=0)
class Microsoft_Windows_PrintService_124_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "JobID" / Int32ul,
        "PrinterName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=125, version=0)
class Microsoft_Windows_PrintService_125_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "JobID" / Int32ul,
        "PrinterName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=131, version=0)
class Microsoft_Windows_PrintService_131_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "PrinterName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=200, version=0)
class Microsoft_Windows_PrintService_200_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "ObjectName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=201, version=0)
class Microsoft_Windows_PrintService_201_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "ObjectName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=204, version=0)
class Microsoft_Windows_PrintService_204_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "ObjectName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=205, version=0)
class Microsoft_Windows_PrintService_205_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "ObjectName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=207, version=0)
class Microsoft_Windows_PrintService_207_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "ObjectName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=210, version=0)
class Microsoft_Windows_PrintService_210_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "ObjectName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=211, version=0)
class Microsoft_Windows_PrintService_211_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "ObjectName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=212, version=0)
class Microsoft_Windows_PrintService_212_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "Message" / WString,
        "AdditionalInfo" / WString,
        "InfPath" / WString,
        "DriverName" / WString,
        "InstallSection" / WString,
        "ProcessorArchitecture" / WString,
        "LastError" / Int32ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=213, version=0)
class Microsoft_Windows_PrintService_213_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "Message" / WString,
        "AdditionalInfo" / WString,
        "InfPath" / WString,
        "DriverName" / WString,
        "InstallSection" / WString,
        "ProcessorArchitecture" / WString,
        "LastError" / Int32ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=214, version=0)
class Microsoft_Windows_PrintService_214_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "Message" / WString,
        "AdditionalInfo" / WString,
        "InfPath" / WString,
        "DriverName" / WString,
        "InstallSection" / WString,
        "ProcessorArchitecture" / WString,
        "PackageAware" / WString,
        "CoreDriverDependencies" / WString,
        "LastError" / Int32ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=215, version=0)
class Microsoft_Windows_PrintService_215_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "Message" / WString,
        "AdditionalInfo" / WString,
        "InfPath" / WString,
        "DriverName" / WString,
        "InstallSection" / WString,
        "ProcessorArchitecture" / WString,
        "PackageAware" / WString,
        "CoreDriverDependencies" / WString,
        "LastError" / Int32ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=216, version=0)
class Microsoft_Windows_PrintService_216_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "Message" / WString,
        "AdditionalInfo" / WString,
        "ProcessorArchitecture" / WString,
        "LastError" / Int32ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=217, version=0)
class Microsoft_Windows_PrintService_217_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "Message" / WString,
        "AdditionalInfo" / WString,
        "ProcessorArchitecture" / WString,
        "LastError" / Int32ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=218, version=0)
class Microsoft_Windows_PrintService_218_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "Message" / WString,
        "AdditionalInfo" / WString,
        "Server" / WString,
        "InfPath" / WString,
        "DestInfPath" / WString,
        "ProcessorArchitecture" / WString,
        "LastError" / Int32ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=219, version=0)
class Microsoft_Windows_PrintService_219_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "Message" / WString,
        "AdditionalInfo" / WString,
        "Server" / WString,
        "InfPath" / WString,
        "DestInfPath" / WString,
        "ProcessorArchitecture" / WString,
        "LastError" / Int32ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=220, version=0)
class Microsoft_Windows_PrintService_220_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "ObjectName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=221, version=0)
class Microsoft_Windows_PrintService_221_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "ObjectName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=222, version=0)
class Microsoft_Windows_PrintService_222_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "LastError" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=223, version=0)
class Microsoft_Windows_PrintService_223_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "LastError" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=224, version=0)
class Microsoft_Windows_PrintService_224_0(Etw):
    pattern = Struct(
        "Function" / WString,
        "Error" / Int32ul,
        "Server" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=225, version=0)
class Microsoft_Windows_PrintService_225_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "InfPath" / WString,
        "RequiredClassDriver" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=226, version=0)
class Microsoft_Windows_PrintService_226_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "InfPath" / WString,
        "DriverModelVersion" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=227, version=0)
class Microsoft_Windows_PrintService_227_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "InfPath" / WString,
        "RequiredClassDriver" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=228, version=0)
class Microsoft_Windows_PrintService_228_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "InfPath" / WString,
        "RequiredClassDriver" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=229, version=0)
class Microsoft_Windows_PrintService_229_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "InfPath" / WString,
        "RequiredClassDriver" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=230, version=0)
class Microsoft_Windows_PrintService_230_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "InfPath" / WString,
        "RequiredClassDriver" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=231, version=0)
class Microsoft_Windows_PrintService_231_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "InfPath" / WString,
        "RequiredClassDriver" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=232, version=0)
class Microsoft_Windows_PrintService_232_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "InfPath" / WString,
        "RequiredClassDriver" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=233, version=0)
class Microsoft_Windows_PrintService_233_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "InfPath" / WString,
        "RequiredClassDriver" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=234, version=0)
class Microsoft_Windows_PrintService_234_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "InfPath" / WString,
        "RequiredClassDriver" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=235, version=0)
class Microsoft_Windows_PrintService_235_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "InfPath" / WString,
        "RequiredClassDriver" / WString,
        "Directive" / WString,
        "Value" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=236, version=0)
class Microsoft_Windows_PrintService_236_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "InfPath" / WString,
        "RequiredClassDriver" / WString,
        "Directive" / WString,
        "ClassDriverOnly" / Int8ul,
        "NonClassDriverOnly" / Int8ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=237, version=0)
class Microsoft_Windows_PrintService_237_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "InfPath" / WString,
        "RequiredClassDriver" / WString,
        "Directive" / WString,
        "EmptyToken" / Int8ul,
        "IncorrectNumberOfTokens" / Int8ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=238, version=0)
class Microsoft_Windows_PrintService_238_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "InfPath" / WString,
        "RequiredClassDriver" / WString,
        "Directive" / WString,
        "Value" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=239, version=0)
class Microsoft_Windows_PrintService_239_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "InfPath" / WString,
        "RequiredClassDriver" / WString,
        "Directive" / WString,
        "Value" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=240, version=0)
class Microsoft_Windows_PrintService_240_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "InfPath" / WString,
        "MissingManifest" / Int8ul,
        "MultipleManifests" / Int8ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=241, version=0)
class Microsoft_Windows_PrintService_241_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "InfPath" / WString,
        "RequiredClassDriver" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=242, version=0)
class Microsoft_Windows_PrintService_242_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "DriverName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=300, version=0)
class Microsoft_Windows_PrintService_300_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=301, version=0)
class Microsoft_Windows_PrintService_301_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=302, version=0)
class Microsoft_Windows_PrintService_302_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=303, version=0)
class Microsoft_Windows_PrintService_303_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=304, version=0)
class Microsoft_Windows_PrintService_304_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=305, version=0)
class Microsoft_Windows_PrintService_305_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=306, version=0)
class Microsoft_Windows_PrintService_306_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=307, version=0)
class Microsoft_Windows_PrintService_307_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString,
        "param8" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=308, version=0)
class Microsoft_Windows_PrintService_308_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=309, version=0)
class Microsoft_Windows_PrintService_309_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=310, version=0)
class Microsoft_Windows_PrintService_310_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=311, version=0)
class Microsoft_Windows_PrintService_311_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=312, version=0)
class Microsoft_Windows_PrintService_312_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=313, version=0)
class Microsoft_Windows_PrintService_313_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=314, version=0)
class Microsoft_Windows_PrintService_314_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=315, version=0)
class Microsoft_Windows_PrintService_315_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=316, version=0)
class Microsoft_Windows_PrintService_316_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=317, version=0)
class Microsoft_Windows_PrintService_317_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=318, version=0)
class Microsoft_Windows_PrintService_318_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=319, version=0)
class Microsoft_Windows_PrintService_319_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=320, version=0)
class Microsoft_Windows_PrintService_320_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=321, version=0)
class Microsoft_Windows_PrintService_321_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=322, version=0)
class Microsoft_Windows_PrintService_322_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=323, version=0)
class Microsoft_Windows_PrintService_323_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=325, version=0)
class Microsoft_Windows_PrintService_325_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=326, version=0)
class Microsoft_Windows_PrintService_326_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=327, version=0)
class Microsoft_Windows_PrintService_327_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=328, version=0)
class Microsoft_Windows_PrintService_328_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=329, version=0)
class Microsoft_Windows_PrintService_329_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=331, version=0)
class Microsoft_Windows_PrintService_331_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=332, version=0)
class Microsoft_Windows_PrintService_332_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=333, version=0)
class Microsoft_Windows_PrintService_333_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=334, version=0)
class Microsoft_Windows_PrintService_334_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=335, version=0)
class Microsoft_Windows_PrintService_335_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=336, version=0)
class Microsoft_Windows_PrintService_336_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=337, version=0)
class Microsoft_Windows_PrintService_337_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=338, version=0)
class Microsoft_Windows_PrintService_338_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=342, version=0)
class Microsoft_Windows_PrintService_342_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=343, version=0)
class Microsoft_Windows_PrintService_343_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=344, version=0)
class Microsoft_Windows_PrintService_344_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=345, version=0)
class Microsoft_Windows_PrintService_345_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=346, version=0)
class Microsoft_Windows_PrintService_346_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=347, version=0)
class Microsoft_Windows_PrintService_347_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=348, version=0)
class Microsoft_Windows_PrintService_348_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=349, version=0)
class Microsoft_Windows_PrintService_349_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=350, version=0)
class Microsoft_Windows_PrintService_350_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=351, version=0)
class Microsoft_Windows_PrintService_351_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=352, version=0)
class Microsoft_Windows_PrintService_352_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=354, version=0)
class Microsoft_Windows_PrintService_354_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=356, version=0)
class Microsoft_Windows_PrintService_356_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=359, version=0)
class Microsoft_Windows_PrintService_359_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=360, version=0)
class Microsoft_Windows_PrintService_360_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=361, version=0)
class Microsoft_Windows_PrintService_361_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=362, version=0)
class Microsoft_Windows_PrintService_362_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=363, version=0)
class Microsoft_Windows_PrintService_363_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=364, version=0)
class Microsoft_Windows_PrintService_364_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=365, version=0)
class Microsoft_Windows_PrintService_365_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=366, version=0)
class Microsoft_Windows_PrintService_366_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=367, version=0)
class Microsoft_Windows_PrintService_367_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=368, version=0)
class Microsoft_Windows_PrintService_368_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=369, version=0)
class Microsoft_Windows_PrintService_369_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=370, version=0)
class Microsoft_Windows_PrintService_370_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=371, version=0)
class Microsoft_Windows_PrintService_371_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=372, version=0)
class Microsoft_Windows_PrintService_372_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString,
        "param8" / WString,
        "param9" / WString,
        "param10" / WString,
        "param11" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=502, version=0)
class Microsoft_Windows_PrintService_502_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=503, version=0)
class Microsoft_Windows_PrintService_503_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=504, version=0)
class Microsoft_Windows_PrintService_504_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=505, version=0)
class Microsoft_Windows_PrintService_505_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=507, version=0)
class Microsoft_Windows_PrintService_507_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=508, version=0)
class Microsoft_Windows_PrintService_508_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=509, version=0)
class Microsoft_Windows_PrintService_509_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=510, version=0)
class Microsoft_Windows_PrintService_510_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=511, version=0)
class Microsoft_Windows_PrintService_511_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=512, version=0)
class Microsoft_Windows_PrintService_512_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=513, version=0)
class Microsoft_Windows_PrintService_513_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=514, version=0)
class Microsoft_Windows_PrintService_514_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=515, version=0)
class Microsoft_Windows_PrintService_515_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=516, version=0)
class Microsoft_Windows_PrintService_516_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=517, version=0)
class Microsoft_Windows_PrintService_517_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=518, version=0)
class Microsoft_Windows_PrintService_518_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=519, version=0)
class Microsoft_Windows_PrintService_519_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=520, version=0)
class Microsoft_Windows_PrintService_520_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=600, version=0)
class Microsoft_Windows_PrintService_600_0(Etw):
    pattern = Struct(
        "DriverSource" / WString,
        "Driver" / WString,
        "Error" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=601, version=0)
class Microsoft_Windows_PrintService_601_0(Etw):
    pattern = Struct(
        "DriverSource" / WString,
        "Driver" / WString,
        "Error" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=602, version=0)
class Microsoft_Windows_PrintService_602_0(Etw):
    pattern = Struct(
        "RegistryKey1" / WString,
        "RegistryKey2" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=603, version=0)
class Microsoft_Windows_PrintService_603_0(Etw):
    pattern = Struct(
        "RegistryKey" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=604, version=0)
class Microsoft_Windows_PrintService_604_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=701, version=0)
class Microsoft_Windows_PrintService_701_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=702, version=0)
class Microsoft_Windows_PrintService_702_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=703, version=0)
class Microsoft_Windows_PrintService_703_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=704, version=0)
class Microsoft_Windows_PrintService_704_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=800, version=0)
class Microsoft_Windows_PrintService_800_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=801, version=0)
class Microsoft_Windows_PrintService_801_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=802, version=0)
class Microsoft_Windows_PrintService_802_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul,
        "JobSize" / Int32ul,
        "DataType" / Int32ul,
        "Pages" / Int32ul,
        "PagesPerSide" / Int32ul,
        "FilesOpened" / Int16sl,
        "JobSizeHigh" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=805, version=0)
class Microsoft_Windows_PrintService_805_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul,
        "GdiJobSize" / Int32ul,
        "ICMMethod" / Int32ul,
        "Color" / Int16sl,
        "XRes" / Int16sl,
        "YRes" / Int16sl,
        "Quality" / Int16sl,
        "Copies" / Int16sl,
        "TTOption" / Int16sl
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=806, version=0)
class Microsoft_Windows_PrintService_806_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=807, version=0)
class Microsoft_Windows_PrintService_807_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=808, version=0)
class Microsoft_Windows_PrintService_808_0(Etw):
    pattern = Struct(
        "PluginDllName" / WString,
        "ErrorCode" / Int32ul,
        "Context" / Int16sl
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=809, version=0)
class Microsoft_Windows_PrintService_809_0(Etw):
    pattern = Struct(
        "DirectoryName" / WString,
        "WaitForReboot" / Int32ul,
        "ErrorCode" / Int32ul,
        "Context" / Int16sl
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=810, version=0)
class Microsoft_Windows_PrintService_810_0(Etw):
    pattern = Struct(
        "DirectoryName" / WString,
        "WaitForReboot" / Int32ul,
        "ErrorCode" / Int32ul,
        "Context" / Int16sl
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=811, version=0)
class Microsoft_Windows_PrintService_811_0(Etw):
    pattern = Struct(
        "Source" / WString,
        "Destination" / WString,
        "Flags" / Int32ul,
        "ErrorCode" / Int32ul,
        "Context" / Int16sl
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=812, version=0)
class Microsoft_Windows_PrintService_812_0(Etw):
    pattern = Struct(
        "Source" / WString,
        "Destination" / WString,
        "Flags" / Int32ul,
        "ErrorCode" / Int32ul,
        "Context" / Int16sl
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=813, version=0)
class Microsoft_Windows_PrintService_813_0(Etw):
    pattern = Struct(
        "Source" / WString,
        "Destination" / WString,
        "Flags" / Int32ul,
        "ErrorCode" / Int32ul,
        "Context" / Int16sl
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=814, version=0)
class Microsoft_Windows_PrintService_814_0(Etw):
    pattern = Struct(
        "Processor" / WString,
        "Environment" / WString,
        "Path" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=815, version=0)
class Microsoft_Windows_PrintService_815_0(Etw):
    pattern = Struct(
        "ProtocolSequence" / WString,
        "EndPoint" / WString,
        "ErrorCode" / Int32ul,
        "Context" / Int16sl
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=816, version=0)
class Microsoft_Windows_PrintService_816_0(Etw):
    pattern = Struct(
        "ValidatedProtocolSequence" / WString,
        "ExpectedProtocolSequence" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=817, version=0)
class Microsoft_Windows_PrintService_817_0(Etw):
    pattern = Struct(
        "WindowsStarterEdition" / Int32ul,
        "SuiteStorageServer" / Int32ul,
        "SystemPrintingDisabled" / Int32ul,
        "SuiteBlade" / Int32ul,
        "SuiteEmbeddedRestricted" / Int32ul,
        "SuiteComputerServer" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=818, version=0)
class Microsoft_Windows_PrintService_818_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Context" / Int16sl
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=819, version=0)
class Microsoft_Windows_PrintService_819_0(Etw):
    pattern = Struct(
        "Policy" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=820, version=0)
class Microsoft_Windows_PrintService_820_0(Etw):
    pattern = Struct(
        "PrintProcessor" / WString,
        "Connection" / WString,
        "IsXpsPrinter" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=821, version=0)
class Microsoft_Windows_PrintService_821_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul,
        "Level" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=822, version=0)
class Microsoft_Windows_PrintService_822_0(Etw):
    pattern = Struct(
        "LocalPrintProcessor" / WString,
        "RemotePrintProcessor" / WString,
        "DefaultPrintProcessor" / WString,
        "LocalDataType" / WString,
        "RemoteDataType" / WString,
        "DefaultDataType" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=823, version=0)
class Microsoft_Windows_PrintService_823_0(Etw):
    pattern = Struct(
        "DefaultPrinterSelectedBySpooler" / Int32ul,
        "OldDefaultPrinter" / WString,
        "NewDefaultPrinter" / WString,
        "Status" / Int32ul,
        "Module" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=824, version=0)
class Microsoft_Windows_PrintService_824_0(Etw):
    pattern = Struct(
        "DocumentName" / WString,
        "JobId" / Int32ul,
        "PrintQueue" / WString,
        "ErrorInfo" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=825, version=0)
class Microsoft_Windows_PrintService_825_0(Etw):
    pattern = Struct(
        "PrintProcessor" / WString,
        "Connection" / WString,
        "IsXpsPrinter" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=826, version=0)
class Microsoft_Windows_PrintService_826_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "PrinterPath" / WString,
        "PortName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=827, version=0)
class Microsoft_Windows_PrintService_827_0(Etw):
    pattern = Struct(
        "QueueName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=828, version=0)
class Microsoft_Windows_PrintService_828_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=829, version=0)
class Microsoft_Windows_PrintService_829_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Context" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=830, version=0)
class Microsoft_Windows_PrintService_830_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Context" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=831, version=0)
class Microsoft_Windows_PrintService_831_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Context" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=832, version=0)
class Microsoft_Windows_PrintService_832_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Context" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=833, version=0)
class Microsoft_Windows_PrintService_833_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Context" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=834, version=0)
class Microsoft_Windows_PrintService_834_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Context" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=842, version=0)
class Microsoft_Windows_PrintService_842_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul,
        "Processor" / WString,
        "Printer" / WString,
        "Driver" / WString,
        "IsolationMode" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=843, version=0)
class Microsoft_Windows_PrintService_843_0(Etw):
    pattern = Struct(
        "SucceededRpcCalls" / Int32ul,
        "FailedRpcCalls" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=844, version=0)
class Microsoft_Windows_PrintService_844_0(Etw):
    pattern = Struct(
        "IsolationMode" / Int32ul,
        "Printer" / WString,
        "Driver" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=845, version=0)
class Microsoft_Windows_PrintService_845_0(Etw):
    pattern = Struct(
        "Module" / WString,
        "Printer" / WString,
        "Driver" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=846, version=0)
class Microsoft_Windows_PrintService_846_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "PrinterAge" / Int32ul,
        "ExpiryAge" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=847, version=0)
class Microsoft_Windows_PrintService_847_0(Etw):
    pattern = Struct(
        "PrinterName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=848, version=0)
class Microsoft_Windows_PrintService_848_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "ShareName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=849, version=0)
class Microsoft_Windows_PrintService_849_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "ShareName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=850, version=0)
class Microsoft_Windows_PrintService_850_0(Etw):
    pattern = Struct(
        "Driver" / WString,
        "Function" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=851, version=0)
class Microsoft_Windows_PrintService_851_0(Etw):
    pattern = Struct(
        "PrintQueue" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=852, version=0)
class Microsoft_Windows_PrintService_852_0(Etw):
    pattern = Struct(
        "OriginalDriver" / WString,
        "NewDriver" / WString,
        "PrinterName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=853, version=0)
class Microsoft_Windows_PrintService_853_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "PrinterName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=854, version=0)
class Microsoft_Windows_PrintService_854_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "PrinterName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=855, version=0)
class Microsoft_Windows_PrintService_855_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "AccessCode" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=856, version=0)
class Microsoft_Windows_PrintService_856_0(Etw):
    pattern = Struct(
        "ConnectionName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=857, version=0)
class Microsoft_Windows_PrintService_857_0(Etw):
    pattern = Struct(
        "ConnectionName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=858, version=0)
class Microsoft_Windows_PrintService_858_0(Etw):
    pattern = Struct(
        "ConnectionName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=859, version=0)
class Microsoft_Windows_PrintService_859_0(Etw):
    pattern = Struct(
        "ConnectionName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=860, version=0)
class Microsoft_Windows_PrintService_860_0(Etw):
    pattern = Struct(
        "ConnectionName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=861, version=0)
class Microsoft_Windows_PrintService_861_0(Etw):
    pattern = Struct(
        "ConnectionName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=862, version=0)
class Microsoft_Windows_PrintService_862_0(Etw):
    pattern = Struct(
        "ConnectionName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=863, version=0)
class Microsoft_Windows_PrintService_863_0(Etw):
    pattern = Struct(
        "ConnectionName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=864, version=0)
class Microsoft_Windows_PrintService_864_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=865, version=0)
class Microsoft_Windows_PrintService_865_0(Etw):
    pattern = Struct(
        "Failures" / Int32ul,
        "Jobs" / Int32ul,
        "PrinterName" / WString,
        "DriverName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=866, version=0)
class Microsoft_Windows_PrintService_866_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "DeviceObjectInstanceIdentifier" / WString,
        "HResultErrorCode" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=867, version=0)
class Microsoft_Windows_PrintService_867_0(Etw):
    pattern = Struct(
        "HResultErrorCode" / Int32ul
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=868, version=0)
class Microsoft_Windows_PrintService_868_0(Etw):
    pattern = Struct(
        "MachineName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=869, version=0)
class Microsoft_Windows_PrintService_869_0(Etw):
    pattern = Struct(
        "Label" / WString,
        "ErrorCode" / Int32ul,
        "ObjectName" / WString
    )


@declare(guid=guid("747ef6fd-e535-4d16-b510-42c90f6873a1"), event_id=870, version=0)
class Microsoft_Windows_PrintService_870_0(Etw):
    pattern = Struct(
        "Driver" / WString,
        "Error" / WString
    )

