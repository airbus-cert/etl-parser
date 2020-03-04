# -*- coding: utf-8 -*-
"""
Microsoft-Windows-StateRepository
GUID : 89592015-d996-4636-8f61-066b5d4dd739
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=100, version=0)
class Microsoft_Windows_StateRepository_100_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "SQL" / CString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=101, version=0)
class Microsoft_Windows_StateRepository_101_0(Etw):
    pattern = Struct(
        "SQL" / CString,
        "ProcessId" / Int32ul,
        "ThreadId" / Int32ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=102, version=0)
class Microsoft_Windows_StateRepository_102_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Subkey" / WString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=103, version=0)
class Microsoft_Windows_StateRepository_103_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Name" / WString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=104, version=0)
class Microsoft_Windows_StateRepository_104_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "SQL" / CString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=105, version=0)
class Microsoft_Windows_StateRepository_105_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "SQL" / CString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=106, version=0)
class Microsoft_Windows_StateRepository_106_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Name" / WString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=107, version=0)
class Microsoft_Windows_StateRepository_107_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "SQL" / CString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=108, version=0)
class Microsoft_Windows_StateRepository_108_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "SQL" / CString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=200, version=0)
class Microsoft_Windows_StateRepository_200_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Entity" / CString,
        "Method" / CString,
        "WorkId" / Int64sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=201, version=0)
class Microsoft_Windows_StateRepository_201_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Entity" / CString,
        "Method" / CString,
        "WorkId" / Int64sl,
        "Id" / Int64sl,
        "Revision" / Int64ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=202, version=0)
class Microsoft_Windows_StateRepository_202_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Entity" / CString,
        "Method" / CString,
        "WorkId" / Int64sl,
        "Id" / Int64sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=203, version=0)
class Microsoft_Windows_StateRepository_203_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Entity" / CString,
        "Method" / CString,
        "WorkId" / Int64sl,
        "Id" / Int64sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=204, version=0)
class Microsoft_Windows_StateRepository_204_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Entity" / CString,
        "Method" / CString,
        "WorkId" / Int64sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=205, version=0)
class Microsoft_Windows_StateRepository_205_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Entity" / CString,
        "Method" / CString,
        "WorkId" / Int64sl,
        "Id" / Int64sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=206, version=0)
class Microsoft_Windows_StateRepository_206_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Entity" / CString,
        "Method" / CString,
        "WorkId" / Int64sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=207, version=0)
class Microsoft_Windows_StateRepository_207_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Entity" / CString,
        "Method" / CString,
        "WorkId" / Int64sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=208, version=0)
class Microsoft_Windows_StateRepository_208_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Entity" / CString,
        "Method" / CString,
        "WorkId" / Int64sl,
        "Id" / Int64sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=209, version=0)
class Microsoft_Windows_StateRepository_209_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Entity" / CString,
        "Method" / CString,
        "WorkId" / Int64sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=210, version=0)
class Microsoft_Windows_StateRepository_210_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Entity" / CString,
        "Method" / CString,
        "WorkId" / Int64sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=211, version=0)
class Microsoft_Windows_StateRepository_211_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Entity" / CString,
        "Method" / CString,
        "WorkId" / Int64sl,
        "Id" / Int64sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=212, version=0)
class Microsoft_Windows_StateRepository_212_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Entity" / CString,
        "Method" / CString,
        "WorkId" / Int64sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=213, version=0)
class Microsoft_Windows_StateRepository_213_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Entity" / CString,
        "Method" / CString,
        "ClientId" / Int32ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=214, version=0)
class Microsoft_Windows_StateRepository_214_0(Etw):
    pattern = Struct(
        "Options" / Int32ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=215, version=0)
class Microsoft_Windows_StateRepository_215_0(Etw):
    pattern = Struct(
        "Options" / Int32ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=216, version=0)
class Microsoft_Windows_StateRepository_216_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=217, version=0)
class Microsoft_Windows_StateRepository_217_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=218, version=0)
class Microsoft_Windows_StateRepository_218_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "ThreadId" / Int32ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=219, version=0)
class Microsoft_Windows_StateRepository_219_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "ThreadId" / Int32ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=220, version=0)
class Microsoft_Windows_StateRepository_220_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Entity" / CString,
        "Method" / CString,
        "WorkId" / Int64sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=221, version=0)
class Microsoft_Windows_StateRepository_221_0(Etw):
    pattern = Struct(
        "Partition" / Int32sl,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=222, version=0)
class Microsoft_Windows_StateRepository_222_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Partition" / Int32sl,
        "Filename" / WString,
        "Disposition" / Int32sl,
        "FoundSchemaVersion" / Int32sl,
        "CreatedSchemaVersion" / Int32sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=223, version=0)
class Microsoft_Windows_StateRepository_223_0(Etw):
    pattern = Struct(
        "Partition" / Int32sl,
        "SchemaVersion" / Int32sl,
        "Filename" / WString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=224, version=0)
class Microsoft_Windows_StateRepository_224_0(Etw):
    pattern = Struct(
        "Partition" / Int32sl,
        "SchemaVersion" / Int32sl,
        "Filename" / WString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=225, version=0)
class Microsoft_Windows_StateRepository_225_0(Etw):
    pattern = Struct(
        "Partition" / Int32sl,
        "SchemaVersion" / Int32sl,
        "FoundSchemaVersion" / Int32sl,
        "Filename" / WString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=226, version=0)
class Microsoft_Windows_StateRepository_226_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ChannelName" / WString,
        "UserSid" / WString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=227, version=0)
class Microsoft_Windows_StateRepository_227_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Checkpoint" / Int32sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=228, version=0)
class Microsoft_Windows_StateRepository_228_0(Etw):
    pattern = Struct(
        "LastKnownStatus" / Int32sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=229, version=0)
class Microsoft_Windows_StateRepository_229_0(Etw):
    pattern = Struct(
        "LastKnownStatus" / Int32sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=230, version=0)
class Microsoft_Windows_StateRepository_230_0(Etw):
    pattern = Struct(
        "LastKnownStatus" / Int32sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=231, version=0)
class Microsoft_Windows_StateRepository_231_0(Etw):
    pattern = Struct(
        "Options" / Int32ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=232, version=0)
class Microsoft_Windows_StateRepository_232_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Entity" / CString,
        "Method" / CString,
        "WorkId" / Int64sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=233, version=0)
class Microsoft_Windows_StateRepository_233_0(Etw):
    pattern = Struct(
        "MachineDisposition" / Int32sl,
        "PreviousMachineVersion" / Int32sl,
        "DeploymentDisposition" / Int32sl,
        "PreviousDeploymentVersion" / Int32sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=234, version=0)
class Microsoft_Windows_StateRepository_234_0(Etw):
    pattern = Struct(
        "MachineDisposition" / Int32sl,
        "PreviousMachineVersion" / Int32sl,
        "DeploymentDisposition" / Int32sl,
        "PreviousDeploymentVersion" / Int32sl,
        "MigratorErrors" / Int32sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=235, version=0)
class Microsoft_Windows_StateRepository_235_0(Etw):
    pattern = Struct(
        "MachineDisposition" / Int32sl,
        "PreviousMachineVersion" / Int32sl,
        "DeploymentDisposition" / Int32sl,
        "PreviousDeploymentVersion" / Int32sl,
        "MigratorErrors" / Int32sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=236, version=0)
class Microsoft_Windows_StateRepository_236_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=237, version=0)
class Microsoft_Windows_StateRepository_237_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=238, version=0)
class Microsoft_Windows_StateRepository_238_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Name" / WString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=239, version=0)
class Microsoft_Windows_StateRepository_239_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Phase" / WString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=240, version=0)
class Microsoft_Windows_StateRepository_240_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Filename" / CString,
        "SQL" / CString,
        "TransactionCallerId" / Guid,
        "Priorities" / WString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=241, version=0)
class Microsoft_Windows_StateRepository_241_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Filename" / CString,
        "ProcessIndex" / Int32ul,
        "ProcessCount" / Int32ul,
        "ProcessId" / Int32ul,
        "ApplicationUserModelId" / WString,
        "PackageFullName" / WString,
        "ExecutableName" / WString,
        "UserSID" / WString,
        "UserDomain" / WString,
        "UserName" / WString,
        "SessionId" / Int32ul,
        "CommandLine" / WString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=242, version=0)
class Microsoft_Windows_StateRepository_242_0(Etw):
    pattern = Struct(
        "TimeoutMSec" / Int64ul,
        "ElapsedTimeMSec" / Int64ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=243, version=0)
class Microsoft_Windows_StateRepository_243_0(Etw):
    pattern = Struct(
        "TimeoutMSec" / Int64ul,
        "ElapsedTimeMSec" / Int64ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=244, version=0)
class Microsoft_Windows_StateRepository_244_0(Etw):
    pattern = Struct(
        "TimeoutMSec" / Int64ul,
        "ElapsedTimeMSec" / Int64ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=245, version=0)
class Microsoft_Windows_StateRepository_245_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=246, version=0)
class Microsoft_Windows_StateRepository_246_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=247, version=0)
class Microsoft_Windows_StateRepository_247_0(Etw):
    pattern = Struct(
        "Partition" / Int32sl,
        "SchemaVersion" / Int32sl,
        "Filename" / CString,
        "Issue" / WString,
        "Found" / Int32sl,
        "Id" / WString,
        "Deleted" / Int32sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=248, version=0)
class Microsoft_Windows_StateRepository_248_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Name" / WString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=249, version=0)
class Microsoft_Windows_StateRepository_249_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Name" / WString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=250, version=0)
class Microsoft_Windows_StateRepository_250_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Action" / CString,
        "Partition" / Int32sl,
        "Filename" / CString,
        "SQL" / CString,
        "Try" / Int64ul,
        "ElapsedTimeMSec" / Int64ul,
        "FirstReportedUptime" / Int64ul,
        "FirstReportedWhen" / Int64ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=251, version=0)
class Microsoft_Windows_StateRepository_251_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "UserSID" / WString,
        "PackageFamilyName" / WString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=252, version=0)
class Microsoft_Windows_StateRepository_252_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "UserSID" / WString,
        "Name" / WString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=253, version=0)
class Microsoft_Windows_StateRepository_253_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "UserSID" / WString,
        "Name" / WString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=254, version=0)
class Microsoft_Windows_StateRepository_254_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "UserSID" / WString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=255, version=0)
class Microsoft_Windows_StateRepository_255_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "UserSID" / WString,
        "Options" / Int32ul,
        "Found" / Int32ul,
        "Deleted" / Int32ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=256, version=0)
class Microsoft_Windows_StateRepository_256_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "UserSID" / WString,
        "Options" / Int32ul,
        "Found" / Int32ul,
        "Deleted" / Int32ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=257, version=0)
class Microsoft_Windows_StateRepository_257_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "UserSID" / WString,
        "Name" / WString,
        "Context" / WString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=258, version=0)
class Microsoft_Windows_StateRepository_258_0(Etw):
    pattern = Struct(
        "UserSID" / WString,
        "Name" / WString,
        "Context" / WString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=259, version=0)
class Microsoft_Windows_StateRepository_259_0(Etw):
    pattern = Struct(
        "Entity" / CString,
        "Field" / CString,
        "Filename" / CString,
        "SQL" / CString,
        "Count" / Int64ul,
        "Ids" / CString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=260, version=0)
class Microsoft_Windows_StateRepository_260_0(Etw):
    pattern = Struct(
        "Entity" / CString,
        "Field" / CString,
        "Filename" / CString,
        "SQL" / CString,
        "Count" / Int64ul,
        "Ids" / CString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=261, version=0)
class Microsoft_Windows_StateRepository_261_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Options" / Int32ul,
        "Disposition" / Int32sl,
        "ErrorCount" / Int64ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=262, version=0)
class Microsoft_Windows_StateRepository_262_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Options" / Int32ul,
        "Disposition" / Int32sl,
        "ErrorCount" / Int64ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=263, version=0)
class Microsoft_Windows_StateRepository_263_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Options" / Int32ul,
        "FixCount" / Int64ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=264, version=0)
class Microsoft_Windows_StateRepository_264_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Options" / Int32ul,
        "FixCount" / Int64ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=265, version=0)
class Microsoft_Windows_StateRepository_265_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Options" / Int32ul,
        "MachineDatabase_Pages" / Int32sl,
        "MachineDatabase_PagesCheckpointed" / Int32sl,
        "DeploymentDatabase_Pages" / Int32sl,
        "DeploymentDatabase_PagesCheckpointed" / Int32sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=266, version=0)
class Microsoft_Windows_StateRepository_266_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Options" / Int32ul,
        "MachineDatabase_Pages" / Int32sl,
        "MachineDatabase_PagesCheckpointed" / Int32sl,
        "DeploymentDatabase_Pages" / Int32sl,
        "DeploymentDatabase_PagesCheckpointed" / Int32sl
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=267, version=0)
class Microsoft_Windows_StateRepository_267_0(Etw):
    pattern = Struct(
        "Entity" / CString,
        "Field" / CString,
        "Filename" / CString,
        "SQL" / CString,
        "Count" / Int64ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=268, version=0)
class Microsoft_Windows_StateRepository_268_0(Etw):
    pattern = Struct(
        "Entity" / CString,
        "Field" / CString,
        "Filename" / CString,
        "SQL" / CString,
        "Count" / Int64ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=269, version=0)
class Microsoft_Windows_StateRepository_269_0(Etw):
    pattern = Struct(
        "Options" / Int32ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=270, version=0)
class Microsoft_Windows_StateRepository_270_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Options" / Int32ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=271, version=0)
class Microsoft_Windows_StateRepository_271_0(Etw):
    pattern = Struct(
        "Options" / Int32ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=272, version=0)
class Microsoft_Windows_StateRepository_272_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Options" / Int32ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=273, version=0)
class Microsoft_Windows_StateRepository_273_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Options" / Int32ul,
        "Disposition" / Int32sl,
        "ErrorCount" / Int64ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=274, version=0)
class Microsoft_Windows_StateRepository_274_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Options" / Int32ul,
        "Disposition" / Int32sl,
        "ErrorCount" / Int64ul
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=275, version=0)
class Microsoft_Windows_StateRepository_275_0(Etw):
    pattern = Struct(
        "Entity" / CString,
        "Count" / Int64ul,
        "Ids" / CString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=276, version=0)
class Microsoft_Windows_StateRepository_276_0(Etw):
    pattern = Struct(
        "Entity" / CString,
        "Count" / Int64ul,
        "Ids" / CString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=277, version=0)
class Microsoft_Windows_StateRepository_277_0(Etw):
    pattern = Struct(
        "Entity" / CString,
        "Id" / Int64ul,
        "Fields" / CString
    )


@declare(guid=guid("89592015-d996-4636-8f61-066b5d4dd739"), event_id=1000, version=0)
class Microsoft_Windows_StateRepository_1000_0(Etw):
    pattern = Struct(
        "ElapsedTime" / Int32ul,
        "SQL" / CString,
        "ProcessId" / Int32ul,
        "ThreadId" / Int32ul
    )

