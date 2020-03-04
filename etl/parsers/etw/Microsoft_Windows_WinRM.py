# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WinRM
GUID : a7975c8f-ac13-49f1-87da-5a984a4ab417
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=3, version=0)
class Microsoft_Windows_WinRM_3_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=5, version=0)
class Microsoft_Windows_WinRM_5_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=6, version=0)
class Microsoft_Windows_WinRM_6_0(Etw):
    pattern = Struct(
        "connection" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=7, version=0)
class Microsoft_Windows_WinRM_7_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=9, version=0)
class Microsoft_Windows_WinRM_9_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=10, version=0)
class Microsoft_Windows_WinRM_10_0(Etw):
    pattern = Struct(
        "optionCode" / Int32ul,
        "optionName" / WString,
        "optionValue" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=11, version=0)
class Microsoft_Windows_WinRM_11_0(Etw):
    pattern = Struct(
        "resourceUri" / WString,
        "shellId" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=12, version=0)
class Microsoft_Windows_WinRM_12_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=13, version=0)
class Microsoft_Windows_WinRM_13_0(Etw):
    pattern = Struct(
        "commandId" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=14, version=0)
class Microsoft_Windows_WinRM_14_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=28, version=0)
class Microsoft_Windows_WinRM_28_0(Etw):
    pattern = Struct(
        "apiCall" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=32, version=0)
class Microsoft_Windows_WinRM_32_0(Etw):
    pattern = Struct(
        "optionCode" / Int32ul,
        "optionName" / WString,
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=37, version=0)
class Microsoft_Windows_WinRM_37_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=38, version=0)
class Microsoft_Windows_WinRM_38_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=40, version=0)
class Microsoft_Windows_WinRM_40_0(Etw):
    pattern = Struct(
        "operationName" / WString,
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=41, version=0)
class Microsoft_Windows_WinRM_41_0(Etw):
    pattern = Struct(
        "applicationID" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=43, version=0)
class Microsoft_Windows_WinRM_43_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "errorMessage" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=44, version=0)
class Microsoft_Windows_WinRM_44_0(Etw):
    pattern = Struct(
        "destination" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=46, version=0)
class Microsoft_Windows_WinRM_46_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "errorMessage" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=47, version=0)
class Microsoft_Windows_WinRM_47_0(Etw):
    pattern = Struct(
        "operationType" / WString,
        "namespaceName" / WString,
        "className" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=49, version=0)
class Microsoft_Windows_WinRM_49_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "errorMessage" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=84, version=0)
class Microsoft_Windows_WinRM_84_0(Etw):
    pattern = Struct(
        "users" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=85, version=0)
class Microsoft_Windows_WinRM_85_0(Etw):
    pattern = Struct(
        "senderName" / WString,
        "concurrentShells" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=86, version=0)
class Microsoft_Windows_WinRM_86_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=87, version=0)
class Microsoft_Windows_WinRM_87_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=91, version=0)
class Microsoft_Windows_WinRM_91_0(Etw):
    pattern = Struct(
        "resourceUri" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=131, version=0)
class Microsoft_Windows_WinRM_131_0(Etw):
    pattern = Struct(
        "location" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=132, version=0)
class Microsoft_Windows_WinRM_132_0(Etw):
    pattern = Struct(
        "operationName" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=142, version=0)
class Microsoft_Windows_WinRM_142_0(Etw):
    pattern = Struct(
        "operationName" / WString,
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=145, version=0)
class Microsoft_Windows_WinRM_145_0(Etw):
    pattern = Struct(
        "operationName" / WString,
        "resourceUri" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=161, version=0)
class Microsoft_Windows_WinRM_161_0(Etw):
    pattern = Struct(
        "authFailureMessage" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=163, version=0)
class Microsoft_Windows_WinRM_163_0(Etw):
    pattern = Struct(
        "authClient" / WString,
        "authServer1" / WString,
        "authServer2" / WString,
        "authServer3" / WString,
        "authServer4" / WString,
        "authServer5" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=164, version=0)
class Microsoft_Windows_WinRM_164_0(Etw):
    pattern = Struct(
        "destinationMachine" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=165, version=0)
class Microsoft_Windows_WinRM_165_0(Etw):
    pattern = Struct(
        "authProxy1" / WString,
        "authProxy2" / WString,
        "authProxy3" / WString,
        "authProxy4" / WString,
        "authProxy5" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=172, version=0)
class Microsoft_Windows_WinRM_172_0(Etw):
    pattern = Struct(
        "machineName" / WString,
        "port" / WString,
        "error1" / WString,
        "error2" / WString,
        "error3" / WString,
        "error4" / WString,
        "error5" / WString,
        "error6" / WString,
        "error7" / WString,
        "error8" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=173, version=0)
class Microsoft_Windows_WinRM_173_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=192, version=0)
class Microsoft_Windows_WinRM_192_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=193, version=0)
class Microsoft_Windows_WinRM_193_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=210, version=0)
class Microsoft_Windows_WinRM_210_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=215, version=0)
class Microsoft_Windows_WinRM_215_0(Etw):
    pattern = Struct(
        "pluginName" / WString,
        "errorcode" / WString,
        "errordetail" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=216, version=0)
class Microsoft_Windows_WinRM_216_0(Etw):
    pattern = Struct(
        "errorcode" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=217, version=0)
class Microsoft_Windows_WinRM_217_0(Etw):
    pattern = Struct(
        "pluginName" / WString,
        "errorcode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=218, version=0)
class Microsoft_Windows_WinRM_218_0(Etw):
    pattern = Struct(
        "pluginName" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=219, version=0)
class Microsoft_Windows_WinRM_219_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=224, version=0)
class Microsoft_Windows_WinRM_224_0(Etw):
    pattern = Struct(
        "message" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=229, version=0)
class Microsoft_Windows_WinRM_229_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=230, version=0)
class Microsoft_Windows_WinRM_230_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=283, version=0)
class Microsoft_Windows_WinRM_283_0(Etw):
    pattern = Struct(
        "operationName" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=284, version=0)
class Microsoft_Windows_WinRM_284_0(Etw):
    pattern = Struct(
        "operationName" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=285, version=0)
class Microsoft_Windows_WinRM_285_0(Etw):
    pattern = Struct(
        "operationName" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=286, version=0)
class Microsoft_Windows_WinRM_286_0(Etw):
    pattern = Struct(
        "operationName" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=288, version=0)
class Microsoft_Windows_WinRM_288_0(Etw):
    pattern = Struct(
        "operationName" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=289, version=0)
class Microsoft_Windows_WinRM_289_0(Etw):
    pattern = Struct(
        "parameters" / Int32ul,
        "operationName" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=290, version=0)
class Microsoft_Windows_WinRM_290_0(Etw):
    pattern = Struct(
        "username" / WString,
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=291, version=0)
class Microsoft_Windows_WinRM_291_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "operation" / WString,
        "resourceUri" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=292, version=0)
class Microsoft_Windows_WinRM_292_0(Etw):
    pattern = Struct(
        "username" / WString,
        "errorCode" / Int32ul,
        "maxAllowedConcurrentShells" / Int32ul,
        "maxAllowedConcurrentOperations" / Int32ul,
        "timeslotSize" / Int32ul,
        "maxAllowedOperationsPerTimeslot" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=306, version=1)
class Microsoft_Windows_WinRM_306_1(Etw):
    pattern = Struct(
        "provider" / WString,
        "path" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=307, version=1)
class Microsoft_Windows_WinRM_307_1(Etw):
    pattern = Struct(
        "provider" / WString,
        "path" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=308, version=0)
class Microsoft_Windows_WinRM_308_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=309, version=0)
class Microsoft_Windows_WinRM_309_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=310, version=0)
class Microsoft_Windows_WinRM_310_0(Etw):
    pattern = Struct(
        "Plugin" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=311, version=0)
class Microsoft_Windows_WinRM_311_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=315, version=0)
class Microsoft_Windows_WinRM_315_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=317, version=0)
class Microsoft_Windows_WinRM_317_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=319, version=0)
class Microsoft_Windows_WinRM_319_0(Etw):
    pattern = Struct(
        "inputErrorCode" / Int32ul,
        "languageCode" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=320, version=0)
class Microsoft_Windows_WinRM_320_0(Etw):
    pattern = Struct(
        "optionCode" / Int32ul,
        "optionName" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=322, version=0)
class Microsoft_Windows_WinRM_322_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=324, version=0)
class Microsoft_Windows_WinRM_324_0(Etw):
    pattern = Struct(
        "operationName" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=325, version=0)
class Microsoft_Windows_WinRM_325_0(Etw):
    pattern = Struct(
        "argument" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=326, version=0)
class Microsoft_Windows_WinRM_326_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=327, version=0)
class Microsoft_Windows_WinRM_327_0(Etw):
    pattern = Struct(
        "argument" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=328, version=0)
class Microsoft_Windows_WinRM_328_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=329, version=0)
class Microsoft_Windows_WinRM_329_0(Etw):
    pattern = Struct(
        "argument" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=330, version=0)
class Microsoft_Windows_WinRM_330_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=331, version=0)
class Microsoft_Windows_WinRM_331_0(Etw):
    pattern = Struct(
        "argument" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=332, version=0)
class Microsoft_Windows_WinRM_332_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=333, version=0)
class Microsoft_Windows_WinRM_333_0(Etw):
    pattern = Struct(
        "argument" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=334, version=0)
class Microsoft_Windows_WinRM_334_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=513, version=0)
class Microsoft_Windows_WinRM_513_0(Etw):
    pattern = Struct(
        "proxyList" / WString,
        "bypassList" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=514, version=0)
class Microsoft_Windows_WinRM_514_0(Etw):
    pattern = Struct(
        "proxyList" / WString,
        "bypassList" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=771, version=0)
class Microsoft_Windows_WinRM_771_0(Etw):
    pattern = Struct(
        "index" / Int32ul,
        "totalChunks" / Int32ul,
        "bytes" / Int32ul,
        "SoapDocument" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=772, version=0)
class Microsoft_Windows_WinRM_772_0(Etw):
    pattern = Struct(
        "index" / Int32ul,
        "totalChunks" / Int32ul,
        "bytes" / Int32ul,
        "SoapDocument" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=774, version=0)
class Microsoft_Windows_WinRM_774_0(Etw):
    pattern = Struct(
        "senderName" / WString,
        "concurrentOperations" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=775, version=0)
class Microsoft_Windows_WinRM_775_0(Etw):
    pattern = Struct(
        "requests" / Int32ul,
        "windowTime" / Int32ul,
        "senderName" / WString,
        "delayHint" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=776, version=0)
class Microsoft_Windows_WinRM_776_0(Etw):
    pattern = Struct(
        "requests" / Int32ul,
        "windowTime" / Int32ul,
        "senderName" / WString,
        "delayHint" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=779, version=0)
class Microsoft_Windows_WinRM_779_0(Etw):
    pattern = Struct(
        "index" / Int32ul,
        "totalChunks" / Int32ul,
        "bytes" / Int32ul,
        "SoapDocument" / CString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=780, version=0)
class Microsoft_Windows_WinRM_780_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=783, version=0)
class Microsoft_Windows_WinRM_783_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=784, version=0)
class Microsoft_Windows_WinRM_784_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=785, version=0)
class Microsoft_Windows_WinRM_785_0(Etw):
    pattern = Struct(
        "userName" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=786, version=0)
class Microsoft_Windows_WinRM_786_0(Etw):
    pattern = Struct(
        "userName" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=787, version=0)
class Microsoft_Windows_WinRM_787_0(Etw):
    pattern = Struct(
        "operationName" / WString,
        "url" / WString,
        "port" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=788, version=0)
class Microsoft_Windows_WinRM_788_0(Etw):
    pattern = Struct(
        "operationName" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=789, version=0)
class Microsoft_Windows_WinRM_789_0(Etw):
    pattern = Struct(
        "operation" / WString,
        "resourceURI" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=790, version=0)
class Microsoft_Windows_WinRM_790_0(Etw):
    pattern = Struct(
        "operation" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=791, version=0)
class Microsoft_Windows_WinRM_791_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=1025, version=0)
class Microsoft_Windows_WinRM_1025_0(Etw):
    pattern = Struct(
        "actionUri" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=1026, version=0)
class Microsoft_Windows_WinRM_1026_0(Etw):
    pattern = Struct(
        "index" / Int32ul,
        "totalChunks" / Int32ul,
        "bytes" / Int32ul,
        "SoapDocument" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=1027, version=0)
class Microsoft_Windows_WinRM_1027_0(Etw):
    pattern = Struct(
        "index" / Int32ul,
        "totalChunks" / Int32ul,
        "bytes" / Int32ul,
        "SoapDocument" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=1044, version=0)
class Microsoft_Windows_WinRM_1044_0(Etw):
    pattern = Struct(
        "index" / Int32ul,
        "totalChunks" / Int32ul,
        "bytes" / Int32ul,
        "SoapDocument" / CString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=1046, version=0)
class Microsoft_Windows_WinRM_1046_0(Etw):
    pattern = Struct(
        "operationName" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=1047, version=0)
class Microsoft_Windows_WinRM_1047_0(Etw):
    pattern = Struct(
        "status" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=1048, version=0)
class Microsoft_Windows_WinRM_1048_0(Etw):
    pattern = Struct(
        "httpStatus" / Int16ul,
        "errorCode" / Int32ul,
        "extraErrorInfo1" / WString,
        "extraErrorInfo2" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=1049, version=0)
class Microsoft_Windows_WinRM_1049_0(Etw):
    pattern = Struct(
        "operationName" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=1050, version=0)
class Microsoft_Windows_WinRM_1050_0(Etw):
    pattern = Struct(
        "operationName" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=1051, version=0)
class Microsoft_Windows_WinRM_1051_0(Etw):
    pattern = Struct(
        "status" / Int32ul
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=1052, version=0)
class Microsoft_Windows_WinRM_1052_0(Etw):
    pattern = Struct(
        "operationName" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=1053, version=0)
class Microsoft_Windows_WinRM_1053_0(Etw):
    pattern = Struct(
        "operationName" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=1054, version=0)
class Microsoft_Windows_WinRM_1054_0(Etw):
    pattern = Struct(
        "operationName" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=1293, version=0)
class Microsoft_Windows_WinRM_1293_0(Etw):
    pattern = Struct(
        "auth" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=1295, version=0)
class Microsoft_Windows_WinRM_1295_0(Etw):
    pattern = Struct(
        "username" / WString,
        "authenticationMechanism" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=1296, version=0)
class Microsoft_Windows_WinRM_1296_0(Etw):
    pattern = Struct(
        "subject" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=1297, version=0)
class Microsoft_Windows_WinRM_1297_0(Etw):
    pattern = Struct(
        "authentication" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=1840, version=0)
class Microsoft_Windows_WinRM_1840_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "errorString" / WString,
        "extraInformation1" / WString,
        "extraInformation2" / WString,
        "extraInformation3" / WString,
        "extraInformation4" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=1841, version=0)
class Microsoft_Windows_WinRM_1841_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "extraInformation1" / WString,
        "extraInformation2" / WString,
        "extraInformation3" / WString,
        "extraInformation4" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=1842, version=0)
class Microsoft_Windows_WinRM_1842_0(Etw):
    pattern = Struct(
        "level" / Int32ul,
        "extraInformation1" / WString,
        "extraInformation2" / WString,
        "extraInformation3" / WString,
        "extraInformation4" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=1843, version=0)
class Microsoft_Windows_WinRM_1843_0(Etw):
    pattern = Struct(
        "clientIP" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=2048, version=0)
class Microsoft_Windows_WinRM_2048_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / Int32ul,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("a7975c8f-ac13-49f1-87da-5a984a4ab417"), event_id=2049, version=0)
class Microsoft_Windows_WinRM_2049_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / Int32ul,
        "param3" / WString,
        "param4" / Int32ul,
        "param5" / WString
    )

