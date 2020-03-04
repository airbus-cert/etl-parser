# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ESE
GUID : 478ea8a8-00be-4ba6-8e75-8b9dc7db9f78
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=103, version=0)
class Microsoft_Windows_ESE_103_0(Etw):
    pattern = Struct(
        "ifmp" / Int32ul,
        "pgno" / Int32ul,
        "LatchFlags" / Int32ul,
        "objid" / Int32ul,
        "PageFlags" / Int32ul,
        "UserId" / Int32ul,
        "OperationId" / Int8ul,
        "OperationType" / Int8ul,
        "ClientType" / Int8ul,
        "Flags" / Int8ul,
        "CorrelationId" / Int32ul,
        "Iorp" / Int8ul,
        "Iors" / Int8ul,
        "Iort" / Int8ul,
        "Ioru" / Int8ul,
        "Iorf" / Int8ul,
        "ParentObjectClass" / Int8ul,
        "dbtimeDirtied" / Int64ul,
        "itagMicFree" / Int16ul,
        "cbFree" / Int16ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=104, version=0)
class Microsoft_Windows_ESE_104_0(Etw):
    pattern = Struct(
        "ifmp" / Int32ul,
        "pgno" / Int32ul,
        "LatchFlags" / Int32ul,
        "objid" / Int32ul,
        "PageFlags" / Int32ul,
        "UserId" / Int32ul,
        "OperationId" / Int8ul,
        "OperationType" / Int8ul,
        "ClientType" / Int8ul,
        "Flags" / Int8ul,
        "CorrelationId" / Int32ul,
        "Iorp" / Int8ul,
        "Iors" / Int8ul,
        "Iort" / Int8ul,
        "Ioru" / Int8ul,
        "Iorf" / Int8ul,
        "ParentObjectClass" / Int8ul,
        "dbtimeDirtied" / Int64ul,
        "itagMicFree" / Int16ul,
        "cbFree" / Int16ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=105, version=0)
class Microsoft_Windows_ESE_105_0(Etw):
    pattern = Struct(
        "ifmp" / Int32ul,
        "pgno" / Int32ul,
        "UserId" / Int32ul,
        "OperationId" / Int8ul,
        "OperationType" / Int8ul,
        "ClientType" / Int8ul,
        "Flags" / Int8ul,
        "CorrelationId" / Int32ul,
        "Iorp" / Int8ul,
        "Iors" / Int8ul,
        "Iort" / Int8ul,
        "Ioru" / Int8ul,
        "Iorf" / Int8ul,
        "ParentObjectClass" / Int8ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=106, version=0)
class Microsoft_Windows_ESE_106_0(Etw):
    pattern = Struct(
        "tick" / Int32ul,
        "ifmp" / Int32ul,
        "pgno" / Int32ul,
        "objid" / Int32ul,
        "PageFlags" / Int32ul,
        "DirtyLevel" / Int32ul,
        "UserId" / Int32ul,
        "OperationId" / Int8ul,
        "OperationType" / Int8ul,
        "ClientType" / Int8ul,
        "Flags" / Int8ul,
        "CorrelationId" / Int32ul,
        "Iorp" / Int8ul,
        "Iors" / Int8ul,
        "Iort" / Int8ul,
        "Ioru" / Int8ul,
        "Iorf" / Int8ul,
        "ParentObjectClass" / Int8ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=107, version=0)
class Microsoft_Windows_ESE_107_0(Etw):
    pattern = Struct(
        "tick" / Int32ul,
        "ifmp" / Int32ul,
        "pgno" / Int32ul,
        "fCurrentVersion" / Int32ul,
        "errBF" / Int32sl,
        "bfef" / Int32ul,
        "pctPriority" / Int32ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=108, version=0)
class Microsoft_Windows_ESE_108_0(Etw):
    pattern = Struct(
        "tick" / Int32ul,
        "ifmp" / Int32ul,
        "pgno" / Int32ul,
        "bflf" / Int32ul,
        "objid" / Int32ul,
        "PageFlags" / Int32ul,
        "bflt" / Int32ul,
        "pctPriority" / Int32ul,
        "bfrtf" / Int32ul,
        "ClientType" / Int8ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=110, version=0)
class Microsoft_Windows_ESE_110_0(Etw):
    pattern = Struct(
        "tick" / Int32ul,
        "ifmp" / Int32ul,
        "pgno" / Int32ul,
        "objid" / Int32ul,
        "PageFlags" / Int32ul,
        "DirtyLevel" / Int32ul,
        "LgposModify" / Int64ul,
        "UserId" / Int32ul,
        "OperationId" / Int8ul,
        "OperationType" / Int8ul,
        "ClientType" / Int8ul,
        "Flags" / Int8ul,
        "CorrelationId" / Int32ul,
        "Iorp" / Int8ul,
        "Iors" / Int8ul,
        "Iort" / Int8ul,
        "Ioru" / Int8ul,
        "Iorf" / Int8ul,
        "ParentObjectClass" / Int8ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=111, version=0)
class Microsoft_Windows_ESE_111_0(Etw):
    pattern = Struct(
        "SessionNumber" / Int64ul,
        "TransactionNumber" / Int64ul,
        "TransactionLevel" / Int8ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=112, version=0)
class Microsoft_Windows_ESE_112_0(Etw):
    pattern = Struct(
        "SessionNumber" / Int64ul,
        "TransactionNumber" / Int64ul,
        "TransactionLevel" / Int8ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=113, version=0)
class Microsoft_Windows_ESE_113_0(Etw):
    pattern = Struct(
        "SessionNumber" / Int64ul,
        "TransactionNumber" / Int64ul,
        "TransactionLevel" / Int8ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=114, version=0)
class Microsoft_Windows_ESE_114_0(Etw):
    pattern = Struct(
        "ifmp" / Int32ul,
        "pgnoFDP" / Int32ul,
        "pgnoFirst" / Int32ul,
        "cpg" / Int32ul,
        "objidFDP" / Int32ul,
        "tce" / Int8ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=115, version=0)
class Microsoft_Windows_ESE_115_0(Etw):
    pattern = Struct(
        "ifmp" / Int32ul,
        "pgnoFDP" / Int32ul,
        "pgnoFirst" / Int32ul,
        "cpg" / Int32ul,
        "objidFDP" / Int32ul,
        "tce" / Int8ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=116, version=0)
class Microsoft_Windows_ESE_116_0(Etw):
    pattern = Struct(
        "ifmp" / Int32ul,
        "pgnoFDP" / Int32ul,
        "pgnoAlloc" / Int32ul,
        "objidFDP" / Int32ul,
        "tce" / Int8ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=117, version=0)
class Microsoft_Windows_ESE_117_0(Etw):
    pattern = Struct(
        "ifmp" / Int32ul,
        "pgnoFDP" / Int32ul,
        "pgnoFree" / Int32ul,
        "objidFDP" / Int32ul,
        "tce" / Int8ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=118, version=0)
class Microsoft_Windows_ESE_118_0(Etw):
    pattern = Struct(
        "iFile" / Int64ul,
        "ibOffset" / Int64ul,
        "cbData" / Int32ul,
        "tidAlloc" / Int32ul,
        "fHeapA" / Int32ul,
        "fWrite" / Int32ul,
        "EngineFileType" / Int32ul,
        "EngineFileId" / Int64ul,
        "cusecEnqueueLatency" / Int32ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=119, version=0)
class Microsoft_Windows_ESE_119_0(Etw):
    pattern = Struct(
        "iFile" / Int64ul,
        "ibOffset" / Int64ul,
        "cbData" / Int32ul,
        "tidAlloc" / Int32ul,
        "fHeapA" / Int32ul,
        "fWrite" / Int32ul,
        "Iorp" / Int32ul,
        "Iors" / Int32ul,
        "Ioru" / Int32ul,
        "Iorf" / Int32ul,
        "grbitQos" / Int32ul,
        "cmsecTimeInQueue" / Int64ul,
        "EngineFileType" / Int32ul,
        "EngineFileId" / Int64ul,
        "cDispatchPass" / Int64ul,
        "cIorunCombined" / Int16ul,
        "cusecDequeueLatency" / Int32ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=120, version=0)
class Microsoft_Windows_ESE_120_0(Etw):
    pattern = Struct(
        "iFile" / Int64ul,
        "fMultiIor" / Int32ul,
        "fWrite" / Int8ul,
        "UserId" / Int32ul,
        "OperationId" / Int8ul,
        "OperationType" / Int8ul,
        "ClientType" / Int8ul,
        "Flags" / Int8ul,
        "CorrelationId" / Int32ul,
        "Iorp" / Int8ul,
        "Iors" / Int8ul,
        "Iort" / Int8ul,
        "Ioru" / Int8ul,
        "Iorf" / Int8ul,
        "ParentObjectClass" / Int8ul,
        "ibOffset" / Int64ul,
        "cbTransfer" / Int32ul,
        "error" / Int32ul,
        "qosHighestFirst" / Int32ul,
        "cmsecIOElapsed" / Int64ul,
        "dtickCompletionDelay" / Int32ul,
        "tidAlloc" / Int32ul,
        "EngineFileType" / Int32ul,
        "EngineFileId" / Int64ul,
        "fmfFile" / Int32ul,
        "DiskNumber" / Int32ul,
        "dwEngineObjid" / Int32ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=122, version=0)
class Microsoft_Windows_ESE_122_0(Etw):
    pattern = Struct(
        "lgenData" / Int32sl,
        "ibLogData" / Int32ul,
        "cbLogData" / Int32ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=123, version=0)
class Microsoft_Windows_ESE_123_0(Etw):
    pattern = Struct(
        "szTrace" / WString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=124, version=0)
class Microsoft_Windows_ESE_124_0(Etw):
    pattern = Struct(
        "szTrace" / WString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=125, version=0)
class Microsoft_Windows_ESE_125_0(Etw):
    pattern = Struct(
        "szTrace" / WString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=126, version=0)
class Microsoft_Windows_ESE_126_0(Etw):
    pattern = Struct(
        "pfnTask" / Int64ul,
        "pvTaskContext" / Int64ul,
        "dwContext" / Int64ul,
        "dtickDelay" / Int32ul,
        "dtickPeriod" / Int32ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=127, version=0)
class Microsoft_Windows_ESE_127_0(Etw):
    pattern = Struct(
        "pfnTask" / Int64ul,
        "pvTaskContext" / Int64ul,
        "dwContext" / Int64ul,
        "cRuns" / Int64ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=128, version=0)
class Microsoft_Windows_ESE_128_0(Etw):
    pattern = Struct(
        "pfnTask" / Int64ul,
        "pvTaskContext" / Int64ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=129, version=0)
class Microsoft_Windows_ESE_129_0(Etw):
    pattern = Struct(
        "posttTimerHandle" / Int64ul,
        "pfnTask" / Int64ul,
        "pvTaskGroupContext" / Int64ul,
        "pvRuntimeContext" / Int64ul,
        "dtickMinDelay" / Int32ul,
        "dtickSlopDelay" / Int32ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=130, version=0)
class Microsoft_Windows_ESE_130_0(Etw):
    pattern = Struct(
        "posttTimerHandle" / Int64ul,
        "pfnTask" / Int64ul,
        "pvTaskGroupContext" / Int64ul,
        "pvRuntimeContext" / Int64ul,
        "cRuns" / Int64ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=131, version=0)
class Microsoft_Windows_ESE_131_0(Etw):
    pattern = Struct(
        "posttTimerHandle" / Int64ul,
        "pfnTask" / Int64ul,
        "pvTaskGroupContext" / Int64ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=132, version=0)
class Microsoft_Windows_ESE_132_0(Etw):
    pattern = Struct(
        "ptm" / Int64ul,
        "pfnCompletion" / Int64ul,
        "dwCompletionKey1" / Int32ul,
        "dwCompletionKey2" / Int64ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=133, version=0)
class Microsoft_Windows_ESE_133_0(Etw):
    pattern = Struct(
        "ptm" / Int64ul,
        "pfnCompletion" / Int64ul,
        "dwCompletionKey1" / Int32ul,
        "dwCompletionKey2" / Int64ul,
        "gle" / Int32ul,
        "dwThreadContext" / Int64ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=134, version=0)
class Microsoft_Windows_ESE_134_0(Etw):
    pattern = Struct(
        "pgptm" / Int64ul,
        "pfnCompletion" / Int64ul,
        "pvParam" / Int64ul,
        "pTaskInfo" / Int64ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=135, version=0)
class Microsoft_Windows_ESE_135_0(Etw):
    pattern = Struct(
        "pgptm" / Int64ul,
        "pfnCompletion" / Int64ul,
        "pvParam" / Int64ul,
        "pTaskInfo" / Int64ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=136, version=0)
class Microsoft_Windows_ESE_136_0(Etw):
    pattern = Struct(
        "qwMarkerID" / Int64ul,
        "szAnnotation" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=137, version=0)
class Microsoft_Windows_ESE_137_0(Etw):
    pattern = Struct(
        "Thread" / Int64ul,
        "pfnStart" / Int64ul,
        "dwParam" / Int64ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=138, version=0)
class Microsoft_Windows_ESE_138_0(Etw):
    pattern = Struct(
        "Thread" / Int64ul,
        "pfnStart" / Int64ul,
        "dwParam" / Int64ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=139, version=0)
class Microsoft_Windows_ESE_139_0(Etw):
    pattern = Struct(
        "ifmp" / Int32ul,
        "pgno" / Int32ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=140, version=0)
class Microsoft_Windows_ESE_140_0(Etw):
    pattern = Struct(
        "ifmp" / Int32ul,
        "pgno" / Int32ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=141, version=0)
class Microsoft_Windows_ESE_141_0(Etw):
    pattern = Struct(
        "cbfCacheAddressableInitial" / Int64sl,
        "cbfCacheSizeInitial" / Int64sl,
        "cbfCacheAddressableFinal" / Int64sl,
        "cbfCacheSizeFinal" / Int64sl
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=142, version=0)
class Microsoft_Windows_ESE_142_0(Etw):
    pattern = Struct(
        "cbfCacheSizeLimitInitial" / Int64sl,
        "cbfCacheSizeLimitFinal" / Int64sl
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=143, version=0)
class Microsoft_Windows_ESE_143_0(Etw):
    pattern = Struct(
        "iRun" / Int64sl,
        "cbfVisited" / Int32sl,
        "cbfCacheSize" / Int32sl,
        "cbfCacheTarget" / Int32sl,
        "cbfCacheSizeStartShrink" / Int32sl,
        "dtickShrinkDuration" / Int32ul,
        "cbfAvail" / Int32sl,
        "cbfAvailPoolLow" / Int32sl,
        "cbfAvailPoolHigh" / Int32sl,
        "cbfFlushPending" / Int32sl,
        "cbfFlushPendingSlow" / Int32sl,
        "cbfFlushPendingHung" / Int32sl,
        "cbfOutOfMemory" / Int32sl,
        "cbfPermanentErrs" / Int32sl,
        "eStopReason" / Int32sl,
        "errRun" / Int32sl
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=144, version=0)
class Microsoft_Windows_ESE_144_0(Etw):
    pattern = Struct(
        "opApi" / Int32ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=145, version=0)
class Microsoft_Windows_ESE_145_0(Etw):
    pattern = Struct(
        "opApi" / Int32ul,
        "err" / Int32sl
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=146, version=0)
class Microsoft_Windows_ESE_146_0(Etw):
    pattern = Struct(
        "tick" / Int32ul,
        "K" / Int32sl,
        "csecCorrelatedTouch" / Double,
        "csecTimeout" / Double,
        "csecUncertainty" / Double,
        "dblHashLoadFactor" / Double,
        "dblHashUniformity" / Double,
        "dblSpeedSizeTradeoff" / Double
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=147, version=0)
class Microsoft_Windows_ESE_147_0(Etw):
    pattern = Struct(
        "tick" / Int32ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=148, version=0)
class Microsoft_Windows_ESE_148_0(Etw):
    pattern = Struct(
        "tick" / Int32ul,
        "ifmp" / Int32ul,
        "pgno" / Int32ul,
        "bflf" / Int32ul,
        "bflt" / Int32ul,
        "pctPriority" / Int32ul,
        "bfrtf" / Int32ul,
        "ClientType" / Int8ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=149, version=0)
class Microsoft_Windows_ESE_149_0(Etw):
    pattern = Struct(
        "tick" / Int32ul,
        "ifmp" / Int32ul,
        "pgno" / Int32ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=150, version=0)
class Microsoft_Windows_ESE_150_0(Etw):
    pattern = Struct(
        "ifmp" / Int32ul,
        "pgno" / Int32ul,
        "dwUserId" / Int32ul,
        "bOperationId" / Int8ul,
        "bOperationType" / Int8ul,
        "bClientType" / Int8ul,
        "bFlags" / Int8ul,
        "dwCorrelationId" / Int32ul,
        "iorp" / Int8ul,
        "iors" / Int8ul,
        "iort" / Int8ul,
        "ioru" / Int8ul,
        "iorf" / Int8ul,
        "tce" / Int8ul,
        "usecsWait" / Int64ul,
        "bftcmr" / Int8ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=151, version=0)
class Microsoft_Windows_ESE_151_0(Etw):
    pattern = Struct(
        "ifmp" / Int32ul,
        "pgno" / Int32ul,
        "dwUserId" / Int32ul,
        "bOperationId" / Int8ul,
        "bOperationType" / Int8ul,
        "bClientType" / Int8ul,
        "bFlags" / Int8ul,
        "dwCorrelationId" / Int32ul,
        "iorp" / Int8ul,
        "iors" / Int8ul,
        "iort" / Int8ul,
        "ioru" / Int8ul,
        "iorf" / Int8ul,
        "tce" / Int8ul,
        "fOpFlags" / Int8ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=152, version=0)
class Microsoft_Windows_ESE_152_0(Etw):
    pattern = Struct(
        "Disk" / Int32ul,
        "wszFileName" / WString,
        "iofr" / Int32ul,
        "cioreqFileFlushing" / Int64ul,
        "usFfb" / Int64ul,
        "error" / Int32ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=153, version=0)
class Microsoft_Windows_ESE_153_0(Etw):
    pattern = Struct(
        "dwDisk" / Int32ul,
        "hFile" / Int64ul,
        "iofr" / Int32ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=154, version=0)
class Microsoft_Windows_ESE_154_0(Etw):
    pattern = Struct(
        "tick" / Int32ul,
        "ifmp" / Int32ul,
        "pgno" / Int32ul,
        "objid" / Int32ul,
        "fFlags" / Int32ul,
        "bfdfNew" / Int32ul,
        "lgposModify" / Int64ul,
        "dwUserId" / Int32ul,
        "bOperationId" / Int8ul,
        "bOperationType" / Int8ul,
        "bClientType" / Int8ul,
        "bFlags" / Int8ul,
        "dwCorrelationId" / Int32ul,
        "iorp" / Int8ul,
        "iors" / Int8ul,
        "iort" / Int8ul,
        "ioru" / Int8ul,
        "iorf" / Int8ul,
        "tce" / Int8ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=155, version=0)
class Microsoft_Windows_ESE_155_0(Etw):
    pattern = Struct(
        "tsidr" / Int8ul,
        "dwImageVerMajor" / Int32ul,
        "dwImageVerMinor" / Int32ul,
        "dwImageBuildMajor" / Int32ul,
        "dwImageBuildMinor" / Int32ul,
        "wszDisplayName" / WString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=156, version=0)
class Microsoft_Windows_ESE_156_0(Etw):
    pattern = Struct(
        "tsidr" / Int8ul,
        "iInstance" / Int32ul,
        "perfstatusEvent" / Int8ul,
        "wszInstanceName" / WString,
        "wszDisplayName" / WString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=157, version=0)
class Microsoft_Windows_ESE_157_0(Etw):
    pattern = Struct(
        "tsidr" / Int8ul,
        "ifmp" / Int32ul,
        "iInstance" / Int32ul,
        "dbid" / Int8ul,
        "wszDatabaseName" / WString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=158, version=0)
class Microsoft_Windows_ESE_158_0(Etw):
    pattern = Struct(
        "tsidr" / Int8ul,
        "dwDiskNumber" / Int32ul,
        "wszDiskPathId" / WString,
        "szDiskModel" / CString,
        "szDiskFirmwareRev" / CString,
        "szDiskSerialNumber" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=159, version=0)
class Microsoft_Windows_ESE_159_0(Etw):
    pattern = Struct(
        "tsidr" / Int8ul,
        "hFile" / Int64ul,
        "dwDiskNumber" / Int32ul,
        "dwEngineFileType" / Int32ul,
        "qwEngineFileId" / Int64ul,
        "fmf" / Int32ul,
        "cbFileSize" / Int64ul,
        "wszAbsPath" / WString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=160, version=0)
class Microsoft_Windows_ESE_160_0(Etw):
    pattern = Struct(
        "tsidr" / Int8ul,
        "ifmp" / Int32ul,
        "filetype" / Int32ul,
        "ulMagic" / Int32ul,
        "ulChecksum" / Int32ul,
        "cbPageSize" / Int32ul,
        "ulDbFlags" / Int32ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=161, version=0)
class Microsoft_Windows_ESE_161_0(Etw):
    pattern = Struct(
        "tsidr" / Int8ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=162, version=0)
class Microsoft_Windows_ESE_162_0(Etw):
    pattern = Struct(
        "tsidr" / Int8ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=163, version=0)
class Microsoft_Windows_ESE_163_0(Etw):
    pattern = Struct(
        "tsidr" / Int8ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=165, version=0)
class Microsoft_Windows_ESE_165_0(Etw):
    pattern = Struct(
        "wszFilename" / WString,
        "fMultiIor" / Int32ul,
        "fWrite" / Int8ul,
        "dwUserId" / Int32ul,
        "bOperationId" / Int8ul,
        "bOperationType" / Int8ul,
        "bClientType" / Int8ul,
        "bFlags" / Int8ul,
        "dwCorrelationId" / Int32ul,
        "iorp" / Int8ul,
        "iors" / Int8ul,
        "iort" / Int8ul,
        "ioru" / Int8ul,
        "iorf" / Int8ul,
        "tce" / Int8ul,
        "szClientComponent" / CString,
        "szClientAction" / CString,
        "szClientActionContext" / CString,
        "guidActivityId" / Guid,
        "ibOffset" / Int64ul,
        "cbTransfer" / Int32ul,
        "dwError" / Int32ul,
        "qosHighestFirst" / Int32ul,
        "cmsecIOElapsed" / Int64ul,
        "dtickCompletionDelay" / Int32ul,
        "tidAlloc" / Int32ul,
        "dwEngineFileType" / Int32ul,
        "dwEngineFileId" / Int64ul,
        "fmfFile" / Int32ul,
        "dwDiskNumber" / Int32ul,
        "dwEngineObjid" / Int32ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=166, version=0)
class Microsoft_Windows_ESE_166_0(Etw):
    pattern = Struct(
        "iInstance" / Int32ul,
        "grbitPurgeFlags" / Int8ul,
        "fcbpfr" / Int8ul,
        "tce" / Int8ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=167, version=0)
class Microsoft_Windows_ESE_167_0(Etw):
    pattern = Struct(
        "dwDiskNumber" / Int32ul,
        "dtickSpikeLength" / Int32ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=168, version=0)
class Microsoft_Windows_ESE_168_0(Etw):
    pattern = Struct(
        "wszFilename" / WString,
        "fMultiIor" / Int32ul,
        "fWrite" / Int8ul,
        "dwUserId" / Int32ul,
        "bOperationId" / Int8ul,
        "bOperationType" / Int8ul,
        "bClientType" / Int8ul,
        "bFlags" / Int8ul,
        "dwCorrelationId" / Int32ul,
        "iorp" / Int8ul,
        "iors" / Int8ul,
        "iort" / Int8ul,
        "ioru" / Int8ul,
        "iorf" / Int8ul,
        "tce" / Int8ul,
        "szClientComponent" / CString,
        "szClientAction" / CString,
        "szClientActionContext" / CString,
        "guidActivityId" / Guid,
        "ibOffset" / Int64ul,
        "cbTransfer" / Int32ul,
        "dwError" / Int32ul,
        "qosHighestFirst" / Int32ul,
        "cmsecIOElapsed" / Int64ul,
        "dtickCompletionDelay" / Int32ul,
        "tidAlloc" / Int32ul,
        "dwEngineFileType" / Int32ul,
        "dwEngineFileId" / Int64ul,
        "fmfFile" / Int32ul,
        "dwDiskNumber" / Int32ul,
        "dwEngineObjid" / Int32ul
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=200, version=0)
class Microsoft_Windows_ESE_200_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=201, version=0)
class Microsoft_Windows_ESE_201_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=202, version=0)
class Microsoft_Windows_ESE_202_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=203, version=0)
class Microsoft_Windows_ESE_203_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=204, version=0)
class Microsoft_Windows_ESE_204_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=205, version=0)
class Microsoft_Windows_ESE_205_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=206, version=0)
class Microsoft_Windows_ESE_206_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=207, version=0)
class Microsoft_Windows_ESE_207_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=208, version=0)
class Microsoft_Windows_ESE_208_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=209, version=0)
class Microsoft_Windows_ESE_209_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=210, version=0)
class Microsoft_Windows_ESE_210_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=211, version=0)
class Microsoft_Windows_ESE_211_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=212, version=0)
class Microsoft_Windows_ESE_212_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=213, version=0)
class Microsoft_Windows_ESE_213_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=214, version=0)
class Microsoft_Windows_ESE_214_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=215, version=0)
class Microsoft_Windows_ESE_215_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=216, version=0)
class Microsoft_Windows_ESE_216_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=217, version=0)
class Microsoft_Windows_ESE_217_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=218, version=0)
class Microsoft_Windows_ESE_218_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=219, version=0)
class Microsoft_Windows_ESE_219_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=220, version=0)
class Microsoft_Windows_ESE_220_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=221, version=0)
class Microsoft_Windows_ESE_221_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=222, version=0)
class Microsoft_Windows_ESE_222_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=223, version=0)
class Microsoft_Windows_ESE_223_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=224, version=0)
class Microsoft_Windows_ESE_224_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=225, version=0)
class Microsoft_Windows_ESE_225_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=226, version=0)
class Microsoft_Windows_ESE_226_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=227, version=0)
class Microsoft_Windows_ESE_227_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=228, version=0)
class Microsoft_Windows_ESE_228_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=229, version=0)
class Microsoft_Windows_ESE_229_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=230, version=0)
class Microsoft_Windows_ESE_230_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=231, version=0)
class Microsoft_Windows_ESE_231_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=232, version=0)
class Microsoft_Windows_ESE_232_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=233, version=0)
class Microsoft_Windows_ESE_233_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=234, version=0)
class Microsoft_Windows_ESE_234_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=235, version=0)
class Microsoft_Windows_ESE_235_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=236, version=0)
class Microsoft_Windows_ESE_236_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=237, version=0)
class Microsoft_Windows_ESE_237_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=238, version=0)
class Microsoft_Windows_ESE_238_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=239, version=0)
class Microsoft_Windows_ESE_239_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=240, version=0)
class Microsoft_Windows_ESE_240_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=241, version=0)
class Microsoft_Windows_ESE_241_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=242, version=0)
class Microsoft_Windows_ESE_242_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=243, version=0)
class Microsoft_Windows_ESE_243_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=244, version=0)
class Microsoft_Windows_ESE_244_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=245, version=0)
class Microsoft_Windows_ESE_245_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=246, version=0)
class Microsoft_Windows_ESE_246_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=247, version=0)
class Microsoft_Windows_ESE_247_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=248, version=0)
class Microsoft_Windows_ESE_248_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=249, version=0)
class Microsoft_Windows_ESE_249_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=250, version=0)
class Microsoft_Windows_ESE_250_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=251, version=0)
class Microsoft_Windows_ESE_251_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=252, version=0)
class Microsoft_Windows_ESE_252_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=253, version=0)
class Microsoft_Windows_ESE_253_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=254, version=0)
class Microsoft_Windows_ESE_254_0(Etw):
    pattern = Struct(
        "szTrace" / CString
    )


@declare(guid=guid("478ea8a8-00be-4ba6-8e75-8b9dc7db9f78"), event_id=5000, version=0)
class Microsoft_Windows_ESE_5000_0(Etw):
    pattern = Struct(
        "TableClass" / Int8ul,
        "OrigSize" / Int16ul,
        "XpressSize" / Int16ul,
        "Xpress9Size" / Int16ul,
        "usecXpressTime" / Int32ul,
        "usecXpress9Time" / Int32ul,
        "ShannonEntropy" / Double,
        "ChiSquared" / Double
    )

