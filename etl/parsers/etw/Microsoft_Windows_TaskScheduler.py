# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TaskScheduler
GUID : de7b24ea-73c8-4a09-985d-5bdadcfa9017
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=100, version=0)
class Microsoft_Windows_TaskScheduler_100_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "UserContext" / WString,
        "InstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=101, version=0)
class Microsoft_Windows_TaskScheduler_101_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "UserContext" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=102, version=0)
class Microsoft_Windows_TaskScheduler_102_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "UserContext" / WString,
        "InstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=103, version=0)
class Microsoft_Windows_TaskScheduler_103_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "InstanceId" / Guid,
        "UserContext" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=104, version=0)
class Microsoft_Windows_TaskScheduler_104_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "ErrorDescription" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=105, version=0)
class Microsoft_Windows_TaskScheduler_105_0(Etw):
    pattern = Struct(
        "Context" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=106, version=0)
class Microsoft_Windows_TaskScheduler_106_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "UserContext" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=107, version=0)
class Microsoft_Windows_TaskScheduler_107_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "InstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=108, version=0)
class Microsoft_Windows_TaskScheduler_108_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "InstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=109, version=0)
class Microsoft_Windows_TaskScheduler_109_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "InstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=110, version=0)
class Microsoft_Windows_TaskScheduler_110_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "InstanceId" / Guid,
        "UserContext" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=111, version=0)
class Microsoft_Windows_TaskScheduler_111_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "InstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=112, version=0)
class Microsoft_Windows_TaskScheduler_112_0(Etw):
    pattern = Struct(
        "TaskName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=113, version=0)
class Microsoft_Windows_TaskScheduler_113_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=114, version=0)
class Microsoft_Windows_TaskScheduler_114_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "InstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=115, version=0)
class Microsoft_Windows_TaskScheduler_115_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=116, version=0)
class Microsoft_Windows_TaskScheduler_116_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=117, version=0)
class Microsoft_Windows_TaskScheduler_117_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "InstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=118, version=0)
class Microsoft_Windows_TaskScheduler_118_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "InstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=119, version=0)
class Microsoft_Windows_TaskScheduler_119_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "UserName" / WString,
        "InstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=120, version=0)
class Microsoft_Windows_TaskScheduler_120_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "UserName" / WString,
        "InstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=121, version=0)
class Microsoft_Windows_TaskScheduler_121_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "UserName" / WString,
        "InstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=122, version=0)
class Microsoft_Windows_TaskScheduler_122_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "UserName" / WString,
        "InstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=123, version=0)
class Microsoft_Windows_TaskScheduler_123_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "UserName" / WString,
        "InstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=124, version=0)
class Microsoft_Windows_TaskScheduler_124_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "UserName" / WString,
        "InstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=125, version=0)
class Microsoft_Windows_TaskScheduler_125_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "UserName" / WString,
        "InstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=126, version=0)
class Microsoft_Windows_TaskScheduler_126_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=127, version=0)
class Microsoft_Windows_TaskScheduler_127_0(Etw):
    pattern = Struct(
        "TaskName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=128, version=0)
class Microsoft_Windows_TaskScheduler_128_0(Etw):
    pattern = Struct(
        "TaskName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=129, version=0)
class Microsoft_Windows_TaskScheduler_129_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "Path" / WString,
        "ProcessID" / Int32ul,
        "Priority" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=130, version=0)
class Microsoft_Windows_TaskScheduler_130_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=131, version=0)
class Microsoft_Windows_TaskScheduler_131_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "CurrentQuota" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=132, version=0)
class Microsoft_Windows_TaskScheduler_132_0(Etw):
    pattern = Struct(
        "CurrentQuota" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=133, version=0)
class Microsoft_Windows_TaskScheduler_133_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "TaskEngineName" / WString,
        "UserName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=134, version=0)
class Microsoft_Windows_TaskScheduler_134_0(Etw):
    pattern = Struct(
        "TaskEngineName" / WString,
        "UserName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=135, version=0)
class Microsoft_Windows_TaskScheduler_135_0(Etw):
    pattern = Struct(
        "TaskName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=140, version=0)
class Microsoft_Windows_TaskScheduler_140_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "UserName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=141, version=0)
class Microsoft_Windows_TaskScheduler_141_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "UserName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=142, version=0)
class Microsoft_Windows_TaskScheduler_142_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "UserName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=146, version=0)
class Microsoft_Windows_TaskScheduler_146_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=147, version=0)
class Microsoft_Windows_TaskScheduler_147_0(Etw):
    pattern = Struct(
        "TaskName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=148, version=0)
class Microsoft_Windows_TaskScheduler_148_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=149, version=0)
class Microsoft_Windows_TaskScheduler_149_0(Etw):
    pattern = Struct(
        "TaskName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=150, version=0)
class Microsoft_Windows_TaskScheduler_150_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=151, version=0)
class Microsoft_Windows_TaskScheduler_151_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "LogPoint" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=152, version=0)
class Microsoft_Windows_TaskScheduler_152_0(Etw):
    pattern = Struct(
        "TaskName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=153, version=0)
class Microsoft_Windows_TaskScheduler_153_0(Etw):
    pattern = Struct(
        "TaskName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=155, version=0)
class Microsoft_Windows_TaskScheduler_155_0(Etw):
    pattern = Struct(
        "TaskPath" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=200, version=0)
class Microsoft_Windows_TaskScheduler_200_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "ActionName" / WString,
        "TaskInstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=200, version=1)
class Microsoft_Windows_TaskScheduler_200_1(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "ActionName" / WString,
        "TaskInstanceId" / Guid,
        "EnginePID" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=201, version=0)
class Microsoft_Windows_TaskScheduler_201_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "ActionName" / WString,
        "TaskInstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=201, version=1)
class Microsoft_Windows_TaskScheduler_201_1(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "TaskInstanceId" / Guid,
        "ActionName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=201, version=2)
class Microsoft_Windows_TaskScheduler_201_2(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "TaskInstanceId" / Guid,
        "ActionName" / WString,
        "ResultCode" / Int32ul,
        "EnginePID" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=202, version=0)
class Microsoft_Windows_TaskScheduler_202_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "TaskInstanceId" / Guid,
        "ActionName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=202, version=1)
class Microsoft_Windows_TaskScheduler_202_1(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "TaskInstanceId" / Guid,
        "ActionName" / WString,
        "ResultCode" / Int32ul,
        "EnginePID" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=203, version=0)
class Microsoft_Windows_TaskScheduler_203_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "TaskInstanceId" / Guid,
        "ActionName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=204, version=0)
class Microsoft_Windows_TaskScheduler_204_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=205, version=0)
class Microsoft_Windows_TaskScheduler_205_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=300, version=0)
class Microsoft_Windows_TaskScheduler_300_0(Etw):
    pattern = Struct(
        "TaskEngineName" / WString,
        "ProcessID" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=301, version=0)
class Microsoft_Windows_TaskScheduler_301_0(Etw):
    pattern = Struct(
        "TaskEngineName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=303, version=0)
class Microsoft_Windows_TaskScheduler_303_0(Etw):
    pattern = Struct(
        "TaskEngineName" / WString,
        "ErrorDescription" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=304, version=0)
class Microsoft_Windows_TaskScheduler_304_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "TaskEngineName" / WString,
        "TaskInstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=305, version=0)
class Microsoft_Windows_TaskScheduler_305_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "TaskEngineName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=306, version=0)
class Microsoft_Windows_TaskScheduler_306_0(Etw):
    pattern = Struct(
        "TaskEngineName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=307, version=0)
class Microsoft_Windows_TaskScheduler_307_0(Etw):
    pattern = Struct(
        "TaskEngineName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=308, version=0)
class Microsoft_Windows_TaskScheduler_308_0(Etw):
    pattern = Struct(
        "TaskEngineName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=309, version=0)
class Microsoft_Windows_TaskScheduler_309_0(Etw):
    pattern = Struct(
        "TaskCount" / Int32ul,
        "TaskEngineName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=310, version=0)
class Microsoft_Windows_TaskScheduler_310_0(Etw):
    pattern = Struct(
        "TaskEngineName" / WString,
        "Command" / WString,
        "ProcessID" / Int32ul,
        "ThreadID" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=311, version=0)
class Microsoft_Windows_TaskScheduler_311_0(Etw):
    pattern = Struct(
        "TaskEngineName" / WString,
        "Command" / WString,
        "ErrorDescription" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=312, version=0)
class Microsoft_Windows_TaskScheduler_312_0(Etw):
    pattern = Struct(
        "TaskEngineName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=313, version=0)
class Microsoft_Windows_TaskScheduler_313_0(Etw):
    pattern = Struct(
        "TaskEngineName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=314, version=0)
class Microsoft_Windows_TaskScheduler_314_0(Etw):
    pattern = Struct(
        "TaskEngineName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=315, version=0)
class Microsoft_Windows_TaskScheduler_315_0(Etw):
    pattern = Struct(
        "TaskEngineName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=316, version=0)
class Microsoft_Windows_TaskScheduler_316_0(Etw):
    pattern = Struct(
        "TaskEngineName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=317, version=0)
class Microsoft_Windows_TaskScheduler_317_0(Etw):
    pattern = Struct(
        "TaskEngineName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=318, version=0)
class Microsoft_Windows_TaskScheduler_318_0(Etw):
    pattern = Struct(
        "TaskEngineName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=319, version=0)
class Microsoft_Windows_TaskScheduler_319_0(Etw):
    pattern = Struct(
        "TaskEngineName" / WString,
        "TaskName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=320, version=0)
class Microsoft_Windows_TaskScheduler_320_0(Etw):
    pattern = Struct(
        "TaskEngineName" / WString,
        "TaskInstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=322, version=0)
class Microsoft_Windows_TaskScheduler_322_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "TaskInstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=323, version=0)
class Microsoft_Windows_TaskScheduler_323_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "StoppedTaskInstanceId" / Guid,
        "NewTaskInstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=324, version=0)
class Microsoft_Windows_TaskScheduler_324_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "QueuedTaskInstanceId" / Guid,
        "RunningTaskInstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=325, version=0)
class Microsoft_Windows_TaskScheduler_325_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "QueuedTaskInstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=326, version=0)
class Microsoft_Windows_TaskScheduler_326_0(Etw):
    pattern = Struct(
        "TaskName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=327, version=0)
class Microsoft_Windows_TaskScheduler_327_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "TaskInstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=328, version=0)
class Microsoft_Windows_TaskScheduler_328_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "TaskInstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=329, version=0)
class Microsoft_Windows_TaskScheduler_329_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "TaskInstanceId" / Guid
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=330, version=0)
class Microsoft_Windows_TaskScheduler_330_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "TaskInstanceId" / Guid,
        "UserContext" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=331, version=0)
class Microsoft_Windows_TaskScheduler_331_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "TaskInstanceId" / Guid,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=332, version=0)
class Microsoft_Windows_TaskScheduler_332_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "UserName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=333, version=0)
class Microsoft_Windows_TaskScheduler_333_0(Etw):
    pattern = Struct(
        "TaskName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=334, version=0)
class Microsoft_Windows_TaskScheduler_334_0(Etw):
    pattern = Struct(
        "TaskName" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=401, version=0)
class Microsoft_Windows_TaskScheduler_401_0(Etw):
    pattern = Struct(
        "ErrorDescription" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=403, version=0)
class Microsoft_Windows_TaskScheduler_403_0(Etw):
    pattern = Struct(
        "ErrorDescription" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=404, version=0)
class Microsoft_Windows_TaskScheduler_404_0(Etw):
    pattern = Struct(
        "ErrorDescription" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=405, version=0)
class Microsoft_Windows_TaskScheduler_405_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=406, version=0)
class Microsoft_Windows_TaskScheduler_406_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=407, version=0)
class Microsoft_Windows_TaskScheduler_407_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=408, version=0)
class Microsoft_Windows_TaskScheduler_408_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=409, version=0)
class Microsoft_Windows_TaskScheduler_409_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=410, version=0)
class Microsoft_Windows_TaskScheduler_410_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=412, version=0)
class Microsoft_Windows_TaskScheduler_412_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=413, version=0)
class Microsoft_Windows_TaskScheduler_413_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=414, version=0)
class Microsoft_Windows_TaskScheduler_414_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "Parameter" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=500, version=0)
class Microsoft_Windows_TaskScheduler_500_0(Etw):
    pattern = Struct(
        "IdleTaskId" / Int32ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=501, version=0)
class Microsoft_Windows_TaskScheduler_501_0(Etw):
    pattern = Struct(
        "IdleTaskId" / Int32ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=502, version=0)
class Microsoft_Windows_TaskScheduler_502_0(Etw):
    pattern = Struct(
        "IdleTaskId" / Int32ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=503, version=0)
class Microsoft_Windows_TaskScheduler_503_0(Etw):
    pattern = Struct(
        "IdleTaskId" / Int32ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=504, version=0)
class Microsoft_Windows_TaskScheduler_504_0(Etw):
    pattern = Struct(
        "IdleTaskId" / Int32ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=505, version=0)
class Microsoft_Windows_TaskScheduler_505_0(Etw):
    pattern = Struct(
        "IdleTaskId" / Int32ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=509, version=0)
class Microsoft_Windows_TaskScheduler_509_0(Etw):
    pattern = Struct(
        "NotificationType" / WString,
        "State" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=510, version=0)
class Microsoft_Windows_TaskScheduler_510_0(Etw):
    pattern = Struct(
        "NoIdleReason" / Int32ul,
        "DATA1" / Int32ul,
        "DATA2" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=511, version=0)
class Microsoft_Windows_TaskScheduler_511_0(Etw):
    pattern = Struct(
        "TimeSinceUserNotPresent" / Int32ul,
        "DATA" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=512, version=0)
class Microsoft_Windows_TaskScheduler_512_0(Etw):
    pattern = Struct(
        "DetectionResult" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=701, version=0)
class Microsoft_Windows_TaskScheduler_701_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=702, version=0)
class Microsoft_Windows_TaskScheduler_702_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=703, version=0)
class Microsoft_Windows_TaskScheduler_703_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=704, version=0)
class Microsoft_Windows_TaskScheduler_704_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=705, version=0)
class Microsoft_Windows_TaskScheduler_705_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=706, version=0)
class Microsoft_Windows_TaskScheduler_706_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "TaskStatus" / Int32ul,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=707, version=0)
class Microsoft_Windows_TaskScheduler_707_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=708, version=0)
class Microsoft_Windows_TaskScheduler_708_0(Etw):
    pattern = Struct(
        "SecurityDescriptor" / WString,
        "TaskName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=709, version=0)
class Microsoft_Windows_TaskScheduler_709_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=710, version=0)
class Microsoft_Windows_TaskScheduler_710_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=711, version=0)
class Microsoft_Windows_TaskScheduler_711_0(Etw):
    pattern = Struct(
        "Account" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=712, version=0)
class Microsoft_Windows_TaskScheduler_712_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=713, version=0)
class Microsoft_Windows_TaskScheduler_713_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=714, version=0)
class Microsoft_Windows_TaskScheduler_714_0(Etw):
    pattern = Struct(
        "TaskName" / WString,
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=715, version=0)
class Microsoft_Windows_TaskScheduler_715_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=716, version=0)
class Microsoft_Windows_TaskScheduler_716_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=717, version=0)
class Microsoft_Windows_TaskScheduler_717_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=718, version=0)
class Microsoft_Windows_TaskScheduler_718_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=800, version=0)
class Microsoft_Windows_TaskScheduler_800_0(Etw):
    pattern = Struct(
        "hc_stateid" / Int32ul,
        "LastRunDateTime" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=801, version=0)
class Microsoft_Windows_TaskScheduler_801_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=802, version=0)
class Microsoft_Windows_TaskScheduler_802_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=803, version=0)
class Microsoft_Windows_TaskScheduler_803_0(Etw):
    pattern = Struct(
        "Task" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=804, version=0)
class Microsoft_Windows_TaskScheduler_804_0(Etw):
    pattern = Struct(
        "Task" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=805, version=0)
class Microsoft_Windows_TaskScheduler_805_0(Etw):
    pattern = Struct(
        "Task" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=806, version=0)
class Microsoft_Windows_TaskScheduler_806_0(Etw):
    pattern = Struct(
        "Task" / WString,
        "InfoCode" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=807, version=0)
class Microsoft_Windows_TaskScheduler_807_0(Etw):
    pattern = Struct(
        "LauncherId" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=808, version=0)
class Microsoft_Windows_TaskScheduler_808_0(Etw):
    pattern = Struct(
        "Task" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=809, version=0)
class Microsoft_Windows_TaskScheduler_809_0(Etw):
    pattern = Struct(
        "FailureReason" / WString
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=998, version=0)
class Microsoft_Windows_TaskScheduler_998_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "HRESULT" / Int32ul,
        "File" / WString,
        "Line" / Int32ul
    )


@declare(guid=guid("de7b24ea-73c8-4a09-985d-5bdadcfa9017"), event_id=999, version=0)
class Microsoft_Windows_TaskScheduler_999_0(Etw):
    pattern = Struct(
        "String" / WString
    )

