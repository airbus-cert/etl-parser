# -*- coding: utf-8 -*-
"""
Microsoft-Windows-AppReadiness
GUID : f0be35f8-237b-4814-86b5-ade51192e503
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=10, version=0)
class Microsoft_Windows_AppReadiness_10_0(Etw):
    pattern = Struct(
        "User" / WString,
        "Operation" / WString,
        "PackageId" / WString,
        "Result" / Int32sl,
        "Error" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=11, version=0)
class Microsoft_Windows_AppReadiness_11_0(Etw):
    pattern = Struct(
        "Error" / Int32sl,
        "Expression" / CString,
        "Function" / CString,
        "File" / CString,
        "Line" / Int32sl
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=12, version=0)
class Microsoft_Windows_AppReadiness_12_0(Etw):
    pattern = Struct(
        "User" / WString,
        "Error" / WString,
        "Result" / Int32sl
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=104, version=0)
class Microsoft_Windows_AppReadiness_104_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "ExitCode" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=105, version=0)
class Microsoft_Windows_AppReadiness_105_0(Etw):
    pattern = Struct(
        "IsIdle" / Int8ul,
        "Reason" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=106, version=0)
class Microsoft_Windows_AppReadiness_106_0(Etw):
    pattern = Struct(
        "User" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=107, version=0)
class Microsoft_Windows_AppReadiness_107_0(Etw):
    pattern = Struct(
        "User" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=108, version=0)
class Microsoft_Windows_AppReadiness_108_0(Etw):
    pattern = Struct(
        "Source" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=109, version=0)
class Microsoft_Windows_AppReadiness_109_0(Etw):
    pattern = Struct(
        "Source" / Int32ul,
        "Result" / Int32sl
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=110, version=0)
class Microsoft_Windows_AppReadiness_110_0(Etw):
    pattern = Struct(
        "ReferencesLeaked" / Int32ul,
        "ShutdownDelayMsec" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=200, version=0)
class Microsoft_Windows_AppReadiness_200_0(Etw):
    pattern = Struct(
        "User" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=201, version=0)
class Microsoft_Windows_AppReadiness_201_0(Etw):
    pattern = Struct(
        "User" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=205, version=0)
class Microsoft_Windows_AppReadiness_205_0(Etw):
    pattern = Struct(
        "User" / WString,
        "NumPackages" / Int32ul,
        "PackageInfo" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=206, version=0)
class Microsoft_Windows_AppReadiness_206_0(Etw):
    pattern = Struct(
        "User" / WString,
        "TaskId" / WString,
        "Priority" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=207, version=0)
class Microsoft_Windows_AppReadiness_207_0(Etw):
    pattern = Struct(
        "User" / WString,
        "TaskId" / WString,
        "Result" / Int32sl
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=209, version=0)
class Microsoft_Windows_AppReadiness_209_0(Etw):
    pattern = Struct(
        "User" / WString,
        "From" / Int32ul,
        "To" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=210, version=0)
class Microsoft_Windows_AppReadiness_210_0(Etw):
    pattern = Struct(
        "User" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=211, version=0)
class Microsoft_Windows_AppReadiness_211_0(Etw):
    pattern = Struct(
        "User" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=212, version=0)
class Microsoft_Windows_AppReadiness_212_0(Etw):
    pattern = Struct(
        "SID" / WString,
        "NumPackages" / Int32ul,
        "PackageFamilyName" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=213, version=0)
class Microsoft_Windows_AppReadiness_213_0(Etw):
    pattern = Struct(
        "Username" / WString,
        "Package" / WString,
        "Operation" / Int32ul,
        "Elapsed" / Double
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=214, version=0)
class Microsoft_Windows_AppReadiness_214_0(Etw):
    pattern = Struct(
        "User" / WString,
        "Package" / WString,
        "Operation" / Int32ul,
        "Error" / Int32sl,
        "Elapsed" / Double
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=215, version=0)
class Microsoft_Windows_AppReadiness_215_0(Etw):
    pattern = Struct(
        "Username" / WString,
        "Task" / WString,
        "Error" / Int32sl,
        "Elapsed" / Double
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=216, version=0)
class Microsoft_Windows_AppReadiness_216_0(Etw):
    pattern = Struct(
        "User" / WString,
        "ResumeAt" / Int64ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=217, version=0)
class Microsoft_Windows_AppReadiness_217_0(Etw):
    pattern = Struct(
        "User" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=218, version=0)
class Microsoft_Windows_AppReadiness_218_0(Etw):
    pattern = Struct(
        "User" / WString,
        "Package" / WString,
        "Operation" / Int32ul,
        "Error" / Int32sl,
        "AttemptAfter" / Int64ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=219, version=0)
class Microsoft_Windows_AppReadiness_219_0(Etw):
    pattern = Struct(
        "SID" / WString,
        "NumPackages" / Int32ul,
        "PackageFamilyName" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=220, version=0)
class Microsoft_Windows_AppReadiness_220_0(Etw):
    pattern = Struct(
        "Username" / WString,
        "Task" / WString,
        "Elapsed" / Double
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=221, version=0)
class Microsoft_Windows_AppReadiness_221_0(Etw):
    pattern = Struct(
        "Username" / WString,
        "Task" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=222, version=0)
class Microsoft_Windows_AppReadiness_222_0(Etw):
    pattern = Struct(
        "User" / WString,
        "TaskId" / WString,
        "OpposingOperation" / Int32ul,
        "TaskCanceled" / Int8ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=223, version=0)
class Microsoft_Windows_AppReadiness_223_0(Etw):
    pattern = Struct(
        "User" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=224, version=0)
class Microsoft_Windows_AppReadiness_224_0(Etw):
    pattern = Struct(
        "User" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=225, version=0)
class Microsoft_Windows_AppReadiness_225_0(Etw):
    pattern = Struct(
        "Username" / WString,
        "Task" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=226, version=0)
class Microsoft_Windows_AppReadiness_226_0(Etw):
    pattern = Struct(
        "User" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=227, version=0)
class Microsoft_Windows_AppReadiness_227_0(Etw):
    pattern = Struct(
        "User" / WString,
        "TaskId" / WString,
        "Priority" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=228, version=0)
class Microsoft_Windows_AppReadiness_228_0(Etw):
    pattern = Struct(
        "Task" / WString,
        "Elapsed" / Double
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=229, version=0)
class Microsoft_Windows_AppReadiness_229_0(Etw):
    pattern = Struct(
        "TaskId" / WString,
        "Priority" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=232, version=0)
class Microsoft_Windows_AppReadiness_232_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=234, version=0)
class Microsoft_Windows_AppReadiness_234_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=236, version=0)
class Microsoft_Windows_AppReadiness_236_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=238, version=0)
class Microsoft_Windows_AppReadiness_238_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=239, version=0)
class Microsoft_Windows_AppReadiness_239_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=240, version=0)
class Microsoft_Windows_AppReadiness_240_0(Etw):
    pattern = Struct(
        "User" / WString,
        "TaskId" / WString,
        "TaskCount" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=241, version=0)
class Microsoft_Windows_AppReadiness_241_0(Etw):
    pattern = Struct(
        "User" / WString,
        "TaskId" / WString,
        "TaskCount" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=300, version=0)
class Microsoft_Windows_AppReadiness_300_0(Etw):
    pattern = Struct(
        "User" / WString,
        "TaskId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=301, version=0)
class Microsoft_Windows_AppReadiness_301_0(Etw):
    pattern = Struct(
        "User" / WString,
        "TaskId" / WString,
        "Result" / Int32sl,
        "Duration" / Double
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=302, version=0)
class Microsoft_Windows_AppReadiness_302_0(Etw):
    pattern = Struct(
        "User" / WString,
        "GroupId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=303, version=0)
class Microsoft_Windows_AppReadiness_303_0(Etw):
    pattern = Struct(
        "User" / WString,
        "GroupId" / WString,
        "Result" / Int32sl,
        "Duration" / Double
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=304, version=0)
class Microsoft_Windows_AppReadiness_304_0(Etw):
    pattern = Struct(
        "User" / WString,
        "GroupId" / WString,
        "TaskId" / WString,
        "Result" / Int32sl
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=305, version=0)
class Microsoft_Windows_AppReadiness_305_0(Etw):
    pattern = Struct(
        "User" / WString,
        "PackageFamilyName" / WString,
        "Reason" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=306, version=0)
class Microsoft_Windows_AppReadiness_306_0(Etw):
    pattern = Struct(
        "User" / WString,
        "TaskId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=307, version=0)
class Microsoft_Windows_AppReadiness_307_0(Etw):
    pattern = Struct(
        "User" / WString,
        "PackageFamilyName" / WString,
        "Reason" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=308, version=0)
class Microsoft_Windows_AppReadiness_308_0(Etw):
    pattern = Struct(
        "User" / WString,
        "PackageFamilyName" / WString,
        "Source" / Int32ul,
        "Result" / Int32sl
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=309, version=0)
class Microsoft_Windows_AppReadiness_309_0(Etw):
    pattern = Struct(
        "User" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=310, version=0)
class Microsoft_Windows_AppReadiness_310_0(Etw):
    pattern = Struct(
        "User" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=311, version=0)
class Microsoft_Windows_AppReadiness_311_0(Etw):
    pattern = Struct(
        "User" / WString,
        "Key" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=312, version=0)
class Microsoft_Windows_AppReadiness_312_0(Etw):
    pattern = Struct(
        "User" / WString,
        "Source" / Int32ul,
        "NumPackages" / Int32ul,
        "PackageFamilyName" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=313, version=0)
class Microsoft_Windows_AppReadiness_313_0(Etw):
    pattern = Struct(
        "User" / WString,
        "Group" / WString,
        "Task" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=314, version=0)
class Microsoft_Windows_AppReadiness_314_0(Etw):
    pattern = Struct(
        "User" / WString,
        "Group" / WString,
        "Task" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=315, version=0)
class Microsoft_Windows_AppReadiness_315_0(Etw):
    pattern = Struct(
        "User" / WString,
        "PackageFamilyName" / WString,
        "Reason" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=316, version=0)
class Microsoft_Windows_AppReadiness_316_0(Etw):
    pattern = Struct(
        "User" / WString,
        "PackageFamilyName" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=317, version=0)
class Microsoft_Windows_AppReadiness_317_0(Etw):
    pattern = Struct(
        "PackageId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=318, version=0)
class Microsoft_Windows_AppReadiness_318_0(Etw):
    pattern = Struct(
        "PackageId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=319, version=0)
class Microsoft_Windows_AppReadiness_319_0(Etw):
    pattern = Struct(
        "PackageId" / WString,
        "Result" / Int32sl
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=320, version=0)
class Microsoft_Windows_AppReadiness_320_0(Etw):
    pattern = Struct(
        "Key" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=322, version=0)
class Microsoft_Windows_AppReadiness_322_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=324, version=0)
class Microsoft_Windows_AppReadiness_324_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=325, version=0)
class Microsoft_Windows_AppReadiness_325_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=327, version=0)
class Microsoft_Windows_AppReadiness_327_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=329, version=0)
class Microsoft_Windows_AppReadiness_329_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=330, version=0)
class Microsoft_Windows_AppReadiness_330_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=1001, version=0)
class Microsoft_Windows_AppReadiness_1001_0(Etw):
    pattern = Struct(
        "User" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=1002, version=0)
class Microsoft_Windows_AppReadiness_1002_0(Etw):
    pattern = Struct(
        "User" / WString,
        "ProcessId" / Int32ul,
        "Result" / Int32sl
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=1003, version=0)
class Microsoft_Windows_AppReadiness_1003_0(Etw):
    pattern = Struct(
        "User" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=1004, version=0)
class Microsoft_Windows_AppReadiness_1004_0(Etw):
    pattern = Struct(
        "User" / WString,
        "ProcessId" / Int32ul,
        "Result" / Int32sl
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=1005, version=0)
class Microsoft_Windows_AppReadiness_1005_0(Etw):
    pattern = Struct(
        "User" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=1006, version=0)
class Microsoft_Windows_AppReadiness_1006_0(Etw):
    pattern = Struct(
        "User" / WString,
        "ProcessId" / Int32ul,
        "Result" / Int32sl
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=1009, version=0)
class Microsoft_Windows_AppReadiness_1009_0(Etw):
    pattern = Struct(
        "User" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=1010, version=0)
class Microsoft_Windows_AppReadiness_1010_0(Etw):
    pattern = Struct(
        "User" / WString,
        "ProcessId" / Int32ul,
        "Result" / Int32sl
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=1013, version=0)
class Microsoft_Windows_AppReadiness_1013_0(Etw):
    pattern = Struct(
        "User" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=1014, version=0)
class Microsoft_Windows_AppReadiness_1014_0(Etw):
    pattern = Struct(
        "User" / WString,
        "ProcessId" / Int32ul,
        "Result" / Int32sl
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=1015, version=0)
class Microsoft_Windows_AppReadiness_1015_0(Etw):
    pattern = Struct(
        "User" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=1016, version=0)
class Microsoft_Windows_AppReadiness_1016_0(Etw):
    pattern = Struct(
        "User" / WString,
        "ProcessId" / Int32ul,
        "Result" / Int32sl
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=1017, version=0)
class Microsoft_Windows_AppReadiness_1017_0(Etw):
    pattern = Struct(
        "User" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=1018, version=0)
class Microsoft_Windows_AppReadiness_1018_0(Etw):
    pattern = Struct(
        "User" / WString,
        "ProcessId" / Int32ul,
        "Result" / Int32sl
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=1019, version=0)
class Microsoft_Windows_AppReadiness_1019_0(Etw):
    pattern = Struct(
        "User" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=1020, version=0)
class Microsoft_Windows_AppReadiness_1020_0(Etw):
    pattern = Struct(
        "User" / WString,
        "ProcessId" / Int32ul,
        "Result" / Int32sl
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=1021, version=0)
class Microsoft_Windows_AppReadiness_1021_0(Etw):
    pattern = Struct(
        "IsAuditMode" / Int8ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=2000, version=0)
class Microsoft_Windows_AppReadiness_2000_0(Etw):
    pattern = Struct(
        "User" / WString,
        "PackageFamilyName" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=2001, version=0)
class Microsoft_Windows_AppReadiness_2001_0(Etw):
    pattern = Struct(
        "User" / WString,
        "PackageFamilyName" / WString,
        "Score" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=2002, version=0)
class Microsoft_Windows_AppReadiness_2002_0(Etw):
    pattern = Struct(
        "User" / WString,
        "PackageFamilyName" / WString,
        "Score" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=2003, version=0)
class Microsoft_Windows_AppReadiness_2003_0(Etw):
    pattern = Struct(
        "User" / WString,
        "PackageFamilyName" / WString,
        "Score" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=2005, version=0)
class Microsoft_Windows_AppReadiness_2005_0(Etw):
    pattern = Struct(
        "User" / WString,
        "PackageFamilyName" / WString,
        "Score" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=2006, version=0)
class Microsoft_Windows_AppReadiness_2006_0(Etw):
    pattern = Struct(
        "User" / WString,
        "PackageFamilyName" / WString,
        "Score" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=2007, version=0)
class Microsoft_Windows_AppReadiness_2007_0(Etw):
    pattern = Struct(
        "User" / WString,
        "PackageFamilyName" / WString,
        "Score" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=2008, version=0)
class Microsoft_Windows_AppReadiness_2008_0(Etw):
    pattern = Struct(
        "User" / WString,
        "PackageFamilyName" / WString,
        "Score" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=2009, version=0)
class Microsoft_Windows_AppReadiness_2009_0(Etw):
    pattern = Struct(
        "User" / WString,
        "PackageFamilyName" / WString,
        "Score" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=2500, version=0)
class Microsoft_Windows_AppReadiness_2500_0(Etw):
    pattern = Struct(
        "User" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=2501, version=0)
class Microsoft_Windows_AppReadiness_2501_0(Etw):
    pattern = Struct(
        "User" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=2502, version=0)
class Microsoft_Windows_AppReadiness_2502_0(Etw):
    pattern = Struct(
        "User" / WString,
        "Package" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=2503, version=0)
class Microsoft_Windows_AppReadiness_2503_0(Etw):
    pattern = Struct(
        "User" / WString,
        "Package" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=2504, version=0)
class Microsoft_Windows_AppReadiness_2504_0(Etw):
    pattern = Struct(
        "User" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=3000, version=0)
class Microsoft_Windows_AppReadiness_3000_0(Etw):
    pattern = Struct(
        "TaskId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=3001, version=0)
class Microsoft_Windows_AppReadiness_3001_0(Etw):
    pattern = Struct(
        "TaskId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=4000, version=0)
class Microsoft_Windows_AppReadiness_4000_0(Etw):
    pattern = Struct(
        "User" / WString,
        "Result" / Int32sl
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=4001, version=0)
class Microsoft_Windows_AppReadiness_4001_0(Etw):
    pattern = Struct(
        "User" / WString,
        "Result" / Int32sl
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5000, version=0)
class Microsoft_Windows_AppReadiness_5000_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5001, version=0)
class Microsoft_Windows_AppReadiness_5001_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5002, version=0)
class Microsoft_Windows_AppReadiness_5002_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5003, version=0)
class Microsoft_Windows_AppReadiness_5003_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5004, version=0)
class Microsoft_Windows_AppReadiness_5004_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5005, version=0)
class Microsoft_Windows_AppReadiness_5005_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5006, version=0)
class Microsoft_Windows_AppReadiness_5006_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5007, version=0)
class Microsoft_Windows_AppReadiness_5007_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5008, version=0)
class Microsoft_Windows_AppReadiness_5008_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5009, version=0)
class Microsoft_Windows_AppReadiness_5009_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5010, version=0)
class Microsoft_Windows_AppReadiness_5010_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5011, version=0)
class Microsoft_Windows_AppReadiness_5011_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5012, version=0)
class Microsoft_Windows_AppReadiness_5012_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5013, version=0)
class Microsoft_Windows_AppReadiness_5013_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5014, version=0)
class Microsoft_Windows_AppReadiness_5014_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5015, version=0)
class Microsoft_Windows_AppReadiness_5015_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5016, version=0)
class Microsoft_Windows_AppReadiness_5016_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5017, version=0)
class Microsoft_Windows_AppReadiness_5017_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5018, version=0)
class Microsoft_Windows_AppReadiness_5018_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5019, version=0)
class Microsoft_Windows_AppReadiness_5019_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5020, version=0)
class Microsoft_Windows_AppReadiness_5020_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5021, version=0)
class Microsoft_Windows_AppReadiness_5021_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5022, version=0)
class Microsoft_Windows_AppReadiness_5022_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5023, version=0)
class Microsoft_Windows_AppReadiness_5023_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5024, version=0)
class Microsoft_Windows_AppReadiness_5024_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5025, version=0)
class Microsoft_Windows_AppReadiness_5025_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5026, version=0)
class Microsoft_Windows_AppReadiness_5026_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5027, version=0)
class Microsoft_Windows_AppReadiness_5027_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5028, version=0)
class Microsoft_Windows_AppReadiness_5028_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5029, version=0)
class Microsoft_Windows_AppReadiness_5029_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5030, version=0)
class Microsoft_Windows_AppReadiness_5030_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5031, version=0)
class Microsoft_Windows_AppReadiness_5031_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5032, version=0)
class Microsoft_Windows_AppReadiness_5032_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5033, version=0)
class Microsoft_Windows_AppReadiness_5033_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5034, version=0)
class Microsoft_Windows_AppReadiness_5034_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5035, version=0)
class Microsoft_Windows_AppReadiness_5035_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5036, version=0)
class Microsoft_Windows_AppReadiness_5036_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5037, version=0)
class Microsoft_Windows_AppReadiness_5037_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5038, version=0)
class Microsoft_Windows_AppReadiness_5038_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5039, version=0)
class Microsoft_Windows_AppReadiness_5039_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5040, version=0)
class Microsoft_Windows_AppReadiness_5040_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5041, version=0)
class Microsoft_Windows_AppReadiness_5041_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5042, version=0)
class Microsoft_Windows_AppReadiness_5042_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5043, version=0)
class Microsoft_Windows_AppReadiness_5043_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5044, version=0)
class Microsoft_Windows_AppReadiness_5044_0(Etw):
    pattern = Struct(
        "User" / WString,
        "Result" / Int32sl
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5045, version=0)
class Microsoft_Windows_AppReadiness_5045_0(Etw):
    pattern = Struct(
        "User" / WString,
        "Result" / Int32sl
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5046, version=0)
class Microsoft_Windows_AppReadiness_5046_0(Etw):
    pattern = Struct(
        "User" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5047, version=0)
class Microsoft_Windows_AppReadiness_5047_0(Etw):
    pattern = Struct(
        "User" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5048, version=0)
class Microsoft_Windows_AppReadiness_5048_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("f0be35f8-237b-4814-86b5-ade51192e503"), event_id=5049, version=0)
class Microsoft_Windows_AppReadiness_5049_0(Etw):
    pattern = Struct(
        "UserId" / WString,
        "PackageFamilyName" / WString,
        "ActivityId" / WString
    )

