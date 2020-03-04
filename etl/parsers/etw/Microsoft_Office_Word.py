# -*- coding: utf-8 -*-
"""
Microsoft-Office-Word
GUID : daf0b914-9c1c-450a-81b2-fea7244f6ffa
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=0, version=0)
class Microsoft_Office_Word_0_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "ipgd" / Int32sl,
        "GoodClient" / Int8ul,
        "PageReuse" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2, version=1)
class Microsoft_Office_Word_2_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "DocKind" / WString,
        "cpFirst" / Int32sl,
        "cpLim" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=4, version=1)
class Microsoft_Office_Word_4_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "DocKind" / WString,
        "cpFirst" / Int32sl,
        "cpLim" / Int32sl,
        "itap" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=6, version=2)
class Microsoft_Office_Word_6_2(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "DocKind" / WString,
        "cp" / Int32sl,
        "GoodClient" / Int8ul,
        "GivenCp" / Int8ul,
        "ParaClient" / Int8ul,
        "FormatLineCaller" / WString,
        "FormatLineCallerOldestAncestor" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=7, version=1)
class Microsoft_Office_Word_7_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "cp" / Int32sl,
        "cpLim" / Int32sl,
        "panic" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=8, version=0)
class Microsoft_Office_Word_8_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "ipgd" / Int32sl,
        "cpapprox" / Int32sl,
        "GoodClient" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=10, version=1)
class Microsoft_Office_Word_10_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "abdk" / WString,
        "cpFirst" / Int32sl,
        "cpLimIfAcex" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=11, version=2)
class Microsoft_Office_Word_11_2(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "DocKind" / WString,
        "pmwd" / Int64ul,
        "pwwd" / Int64ul,
        "hwnd" / Int64ul,
        "ViewType" / WString,
        "PctZoom" / Int32sl,
        "RMView" / Int8ul,
        "rcwDispxp" / Int32sl,
        "rcwDispyp" / Int32sl,
        "rcwDispdxp" / Int32sl,
        "rcwDispdyp" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=13, version=3)
class Microsoft_Office_Word_13_3(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "pwwd" / Int64ul,
        "ipgd" / Int32sl,
        "LayerHandle" / Int64sl,
        "TextureHandle" / Int64sl,
        "rcePagexe" / Int32sl,
        "rcePageye" / Int32sl,
        "rcePagedxe" / Int32sl,
        "rcePagedye" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=15, version=3)
class Microsoft_Office_Word_15_3(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "pwwd" / Int64ul,
        "ipgd" / Int32sl,
        "LayerHandle" / Int64sl,
        "TextureHandle" / Int64sl,
        "rcePagexe" / Int32sl,
        "rcePageye" / Int32sl,
        "rcePagedxe" / Int32sl,
        "rcePagedye" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=17, version=1)
class Microsoft_Office_Word_17_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=18, version=2)
class Microsoft_Office_Word_18_2(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "DocKind" / WString,
        "cpFirst" / Int32sl,
        "cpLim" / Int32sl,
        "drk" / WString,
        "Subtype" / WString,
        "drcxp" / Int32sl,
        "drcyp" / Int32sl,
        "drcdxp" / Int32sl,
        "drcdyp" / Int32sl,
        "LayerHandle" / Int64sl,
        "TextureHandle" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=20, version=3)
class Microsoft_Office_Word_20_3(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "DocKind" / WString,
        "cpFirst" / Int32sl,
        "pwwd" / Int64ul,
        "ViewType" / WString,
        "FirstLoopChar" / Int8ul,
        "SqmDocId" / Guid,
        "DocumentId" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=22, version=1)
class Microsoft_Office_Word_22_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "DocKind" / WString,
        "cpFirst" / Int32sl,
        "ccp" / Int32sl,
        "EvtMntrName" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=23, version=1)
class Microsoft_Office_Word_23_1(Etw):
    pattern = Struct(
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=26, version=2)
class Microsoft_Office_Word_26_2(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "cpFirst" / Int32sl,
        "cpLim" / Int32sl,
        "InInsertLoop" / Int8ul,
        "fEnd" / Int8ul,
        "UpdateWwd" / Int8ul,
        "Reason" / WString,
        "wm" / Int32ul,
        "hwnd" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=27, version=2)
class Microsoft_Office_Word_27_2(Etw):
    pattern = Struct(
        "pwwd" / Int64ul,
        "ViewType" / WString,
        "WwdUpdateDurationmsec" / Int64ul,
        "ChunkingUpdateThresholdmsec" / Int64ul,
        "WwdUpdateDelaymsec" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=28, version=2)
class Microsoft_Office_Word_28_2(Etw):
    pattern = Struct(
        "pwwd" / Int64ul,
        "ViewType" / WString,
        "WwdUpdateDurationmsec" / Int64ul,
        "ChunkingUpdateThresholdmsec" / Int64ul,
        "Reason" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=29, version=2)
class Microsoft_Office_Word_29_2(Etw):
    pattern = Struct(
        "pwwd" / Int64ul,
        "ViewType" / WString,
        "Timesincelastwwdupdatemsec" / Int64ul,
        "WwdUpdateDelaymsec" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=36, version=0)
class Microsoft_Office_Word_36_0(Etw):
    pattern = Struct(
        "drk" / Int32ul,
        "fDirty" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=37, version=0)
class Microsoft_Office_Word_37_0(Etw):
    pattern = Struct(
        "fInTable" / Int8ul,
        "fTxbx" / Int8ul,
        "fGEPresent" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=38, version=0)
class Microsoft_Office_Word_38_0(Etw):
    pattern = Struct(
        "drselk" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=39, version=0)
class Microsoft_Office_Word_39_0(Etw):
    pattern = Struct(
        "grfdrdo" / Int32ul,
        "cTxbx" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=40, version=0)
class Microsoft_Office_Word_40_0(Etw):
    pattern = Struct(
        "drkx" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=41, version=0)
class Microsoft_Office_Word_41_0(Etw):
    pattern = Struct(
        "DmsecInIdle" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=46, version=4)
class Microsoft_Office_Word_46_4(Etw):
    pattern = Struct(
        "filename" / WString,
        "fSuccess" / Int8ul,
        "fCancelledByUser" / Int8ul,
        "Contentinfo" / Int32ul,
        "extension" / WString,
        "size" / Int64ul,
        "fIsRetryOpenViaBcs" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=53, version=1)
class Microsoft_Office_Word_53_1(Etw):
    pattern = Struct(
        "ipgd" / Int32sl,
        "pdodMain" / Int64ul,
        "drk" / WString,
        "IdealPixelCount" / Int64ul,
        "BoundingBoxPixelCount" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=68, version=0)
class Microsoft_Office_Word_68_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=69, version=2)
class Microsoft_Office_Word_69_2(Etw):
    pattern = Struct(
        "TagCaller" / Int32ul,
        "pdodSrc0" / Int64ul,
        "pdodSrc1" / Int64ul,
        "pdodBase" / Int64ul,
        "cpMac0" / Int32sl,
        "cpMac1" / Int32sl,
        "cpMacBase" / Int32sl,
        "grfdc" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=70, version=4)
class Microsoft_Office_Word_70_4(Etw):
    pattern = Struct(
        "dwTag" / Int32ul,
        "ElapsedTimeMicroseconds" / Int64ul,
        "cmdRet" / Int32sl,
        "fConflict" / Int8ul,
        "fTwoWayMerge" / Int8ul,
        "Autofit0Microseconds" / Int64ul,
        "Autofit1Microseconds" / Int64ul,
        "AutofitBaseMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=72, version=0)
class Microsoft_Office_Word_72_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=74, version=0)
class Microsoft_Office_Word_74_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=76, version=0)
class Microsoft_Office_Word_76_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=78, version=0)
class Microsoft_Office_Word_78_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=80, version=0)
class Microsoft_Office_Word_80_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=82, version=0)
class Microsoft_Office_Word_82_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=84, version=0)
class Microsoft_Office_Word_84_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=86, version=0)
class Microsoft_Office_Word_86_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=88, version=0)
class Microsoft_Office_Word_88_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=90, version=0)
class Microsoft_Office_Word_90_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=92, version=0)
class Microsoft_Office_Word_92_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=94, version=0)
class Microsoft_Office_Word_94_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=96, version=0)
class Microsoft_Office_Word_96_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=98, version=0)
class Microsoft_Office_Word_98_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=100, version=0)
class Microsoft_Office_Word_100_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=102, version=0)
class Microsoft_Office_Word_102_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=104, version=0)
class Microsoft_Office_Word_104_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=106, version=0)
class Microsoft_Office_Word_106_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=108, version=0)
class Microsoft_Office_Word_108_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=110, version=0)
class Microsoft_Office_Word_110_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=112, version=0)
class Microsoft_Office_Word_112_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=114, version=0)
class Microsoft_Office_Word_114_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=116, version=0)
class Microsoft_Office_Word_116_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=118, version=0)
class Microsoft_Office_Word_118_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=120, version=0)
class Microsoft_Office_Word_120_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=122, version=0)
class Microsoft_Office_Word_122_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=123, version=4)
class Microsoft_Office_Word_123_4(Etw):
    pattern = Struct(
        "pdodSrc" / Int64ul,
        "pdodClone" / Int64ul,
        "fBackground" / Int8ul,
        "Format" / WString,
        "SQMDocID" / Guid,
        "recurseCount" / Int32sl,
        "SaveActionId" / Guid,
        "ftyp" / Int32sl,
        "fSaveAs" / Int8ul,
        "SqmDocLocation" / Int32sl,
        "AuthorsCount" / Int32sl,
        "fMultipleAuthors" / Int8ul,
        "fCoAuthorable" / Int8ul,
        "fMergeRequired" / Int8ul,
        "saveDwTag" / Int32ul,
        "saveInitiateKind" / Int32sl,
        "rtcEnabledState" / Int32sl,
        "alwaysSaveEnabledState" / Int32sl,
        "BkgSaveDisallowReason" / Int32ul,
        "AlwaysSaveDisableReason" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=124, version=8)
class Microsoft_Office_Word_124_8(Etw):
    pattern = Struct(
        "pdodSrc" / Int64ul,
        "pdodClone" / Int64ul,
        "fSuccess" / Int8ul,
        "eid" / Int32sl,
        "recurseCount" / Int32sl,
        "ElapsedTimeMicroseconds" / Int64ul,
        "SaveActionId" / Guid,
        "EditToSaveTimeMicroseconds" / Int64ul,
        "FirstEditId" / Guid,
        "EdpiType" / Int32ul,
        "CurrentEditId" / Guid,
        "RtcBrkEditToSaveTimeMicroseconds" / Int64ul,
        "FirstRtcBrkEditId" / Guid,
        "CurrentRtcBrkEditId" / Guid,
        "IdleDelayedAutoSaveTimeMicroseconds" / Int64ul,
        "AutoSaveIdleToSaveTimeMicroseconds" / Int64ul,
        "AutoSaveIdleDurationTimeMicroseconds" / Int64ul,
        "AutoSaveIdleCooldownTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=125, version=2)
class Microsoft_Office_Word_125_2(Etw):
    pattern = Struct(
        "SQMDocID" / Guid,
        "Source" / WString,
        "saveInitiateKind" / Int32sl,
        "Pdod" / Int64ul,
        "SqmDocLocation" / Int32sl,
        "FCoAuthorable" / Int8ul,
        "SaveActionId" / Guid,
        "DusecFirstEditToSaveInit" / Int64ul,
        "FirstEditId" / Guid,
        "DusecFirstRtcBrkEditToSaveInit" / Int64ul,
        "FirstRtcBrkEditId" / Guid,
        "CsiErrorCode" / Int32ul,
        "DynamicSaveAdjustedReason" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=132, version=2)
class Microsoft_Office_Word_132_2(Etw):
    pattern = Struct(
        "ThreadName" / WString,
        "SuspensionID" / Guid,
        "fpInitialTimeAvailableMilliseconds" / Float32l,
        "SessionID" / Guid
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=133, version=0)
class Microsoft_Office_Word_133_0(Etw):
    pattern = Struct(
        "SuspensionID" / Guid,
        "fIsDocOpen" / Int8ul,
        "SQMDocID" / Guid,
        "pdodCurrent" / Int64ul,
        "fIsDocDirty" / Int8ul,
        "fIsSaveInProgress" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=134, version=1)
class Microsoft_Office_Word_134_1(Etw):
    pattern = Struct(
        "ThreadName" / WString,
        "SuspensionID" / Guid,
        "fpTimeRemainingMilliseconds" / Float32l,
        "fpElapsedTimeMilliseconds" / Float32l,
        "HResult" / Int32sl,
        "ErrorDescription" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=135, version=1)
class Microsoft_Office_Word_135_1(Etw):
    pattern = Struct(
        "SessionID" / Guid,
        "SQMDocID" / Guid,
        "pdod" / Int64ul,
        "dataLossType" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=136, version=5)
class Microsoft_Office_Word_136_5(Etw):
    pattern = Struct(
        "ETW_TrackbackTag" / Int32ul,
        "pwwd" / Int64ul,
        "deviceid" / Int32ul,
        "layername" / WString,
        "layerid" / Int64ul,
        "airspacelayerhandle" / Int64sl,
        "bootQuitstate" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=137, version=1)
class Microsoft_Office_Word_137_1(Etw):
    pattern = Struct(
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=141, version=0)
class Microsoft_Office_Word_141_0(Etw):
    pattern = Struct(
        "SQMDocID" / Guid,
        "Reason" / WString,
        "Details1" / Int32sl,
        "Details2" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=148, version=2)
class Microsoft_Office_Word_148_2(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "SqmDocId" / Guid,
        "Format" / WString,
        "fSaveDuringSuspendOrClose" / Int8ul,
        "cIntervals" / Int32ul,
        "Bucket1MinMsec" / Int64ul,
        "Bucket2MinMsec" / Int64ul,
        "Bucket3MinMsec" / Int64ul,
        "Bucket4MinMsec" / Int64ul,
        "Bucket5MinMsec" / Int64ul,
        "Bucket6MinMsec" / Int64ul,
        "Bucket7MinMsec" / Int64ul,
        "Bucket8MinMsec" / Int64ul,
        "Bucket9MinMsec" / Int64ul,
        "Bucket10MinMsec" / Int64ul,
        "Bucket1Count" / Int64ul,
        "Bucket2Count" / Int64ul,
        "Bucket3Count" / Int64ul,
        "Bucket4Count" / Int64ul,
        "Bucket5Count" / Int64ul,
        "Bucket6Count" / Int64ul,
        "Bucket7Count" / Int64ul,
        "Bucket8Count" / Int64ul,
        "Bucket9Count" / Int64ul,
        "Bucket10Count" / Int64ul,
        "TopUnresponsiveDuration1Msec" / Int64ul,
        "TopUnresponsiveDuration2Msec" / Int64ul,
        "TopUnresponsiveDuration3Msec" / Int64ul,
        "TopUnresponsiveDuration4Msec" / Int64ul,
        "TopUnresponsiveDuration5Msec" / Int64ul,
        "SaveActionId" / Guid,
        "ftyp" / Int32sl,
        "fSaveAs" / Int8ul,
        "SqmDocLocation" / Int32sl,
        "AuthorsCount" / Int32sl,
        "fMultipleAuthors" / Int8ul,
        "fCoAuthorable" / Int8ul,
        "fMergeRequired" / Int8ul,
        "fOnBackgroundThread" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=149, version=0)
class Microsoft_Office_Word_149_0(Etw):
    pattern = Struct(
        "SuspensionID" / Guid,
        "SQMDocID" / Guid,
        "Disposition" / WString,
        "Error" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=150, version=0)
class Microsoft_Office_Word_150_0(Etw):
    pattern = Struct(
        "ThreadName" / WString,
        "MillisecondsSuspended" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=151, version=1)
class Microsoft_Office_Word_151_1(Etw):
    pattern = Struct(
        "ThreadName" / WString,
        "fpElapsedTimeMilliseconds" / Float32l
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=153, version=0)
class Microsoft_Office_Word_153_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=155, version=0)
class Microsoft_Office_Word_155_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=158, version=1)
class Microsoft_Office_Word_158_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "cmvBeforeUpgrade" / Int32sl,
        "cmvToUpgrade" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=159, version=1)
class Microsoft_Office_Word_159_1(Etw):
    pattern = Struct(
        "upgradeCmdStatus" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=162, version=1)
class Microsoft_Office_Word_162_1(Etw):
    pattern = Struct(
        "ReportID" / Int64ul,
        "IdleCoreTime" / Int64ul,
        "ActiveTime" / Int64ul,
        "DeepSleepTime" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=163, version=1)
class Microsoft_Office_Word_163_1(Etw):
    pattern = Struct(
        "ReportID" / Int64ul,
        "Bucket050Count" / Int64ul,
        "Bucket50100Count" / Int64ul,
        "Bucket100150Count" / Int64ul,
        "Bucket150200Count" / Int64ul,
        "Bucket200350Count" / Int64ul,
        "Bucket350500Count" / Int64ul,
        "Bucket5001000Count" / Int64ul,
        "Bucket10002000Count" / Int64ul,
        "Bucket20005000Count" / Int64ul,
        "Bucket5000MaxCount" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=164, version=2)
class Microsoft_Office_Word_164_2(Etw):
    pattern = Struct(
        "ReportID" / Int64ul,
        "IdleTaskName" / WString,
        "fRtcGroupIdle" / Int8ul,
        "IdleTimeForTask" / Int64ul,
        "Count" / Int64ul,
        "MsgPresentCount" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=166, version=0)
class Microsoft_Office_Word_166_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=168, version=0)
class Microsoft_Office_Word_168_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=169, version=1)
class Microsoft_Office_Word_169_1(Etw):
    pattern = Struct(
        "SessionID" / Guid
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=172, version=2)
class Microsoft_Office_Word_172_2(Etw):
    pattern = Struct(
        "fn" / Int32sl,
        "Ext" / WString,
        "ftyp" / Int32sl,
        "pioldoc" / Int64ul,
        "Caller" / WString,
        "fAutosaveDoc" / Int8ul,
        "fFnStrmWrapped" / Int8ul,
        "dof" / Int32ul,
        "dof2" / Int64ul,
        "recurseCount" / Int32sl,
        "currentScopeId" / Int32ul,
        "parentScopeId" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=173, version=6)
class Microsoft_Office_Word_173_6(Etw):
    pattern = Struct(
        "Failed" / Int8ul,
        "Canceled" / Int8ul,
        "pdod" / Int64ul,
        "diReason" / Int16ul,
        "ftyp" / Int32sl,
        "FtypExt" / WString,
        "SqmDocId" / Guid,
        "recurseCount" / Int32sl,
        "sdv" / Int32sl,
        "EdpiType" / Int32ul,
        "nFib" / Int16ul,
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=174, version=6)
class Microsoft_Office_Word_174_6(Etw):
    pattern = Struct(
        "recurseCount" / Int32sl,
        "SaveActionId" / Guid,
        "SqmDocId" / Guid,
        "ftyp" / Int32sl,
        "fSaveAs" / Int8ul,
        "SqmDocLocation" / Int32sl,
        "AuthorsCount" / Int32sl,
        "fMultipleAuthors" / Int8ul,
        "fOnBackgroundThread" / Int8ul,
        "currentScopeId" / Int32ul,
        "parentScopeId" / Int32ul,
        "pioldoc" / Int64ul,
        "saveInitiateKind" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=175, version=5)
class Microsoft_Office_Word_175_5(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul,
        "cmdRet" / Int32sl,
        "recurseCount" / Int32sl,
        "SaveActionId" / Guid,
        "fCoAuthorable" / Int8ul,
        "fMergeRequired" / Int8ul,
        "currentScopeId" / Int32ul,
        "parentScopeId" / Int32ul,
        "QueueStatus" / Int16ul,
        "fInCoherencyRetry" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=176, version=1)
class Microsoft_Office_Word_176_1(Etw):
    pattern = Struct(
        "lserr" / Int32sl,
        "dk" / Int32ul,
        "fGoodClientDoc" / Int8ul,
        "wk" / Int32ul,
        "fWwdLayout" / Int8ul,
        "fWwdVBA" / Int8ul,
        "sqmDocID" / Guid,
        "pdodMain" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=177, version=1)
class Microsoft_Office_Word_177_1(Etw):
    pattern = Struct(
        "fserr" / Int32sl,
        "ipgd" / Int32sl,
        "dk" / Int32ul,
        "fGoodClientDoc" / Int8ul,
        "wk" / Int32ul,
        "fWwdLayout" / Int8ul,
        "fWwdVBA" / Int8ul,
        "sqmDocID" / Guid,
        "pdodMain" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=178, version=2)
class Microsoft_Office_Word_178_2(Etw):
    pattern = Struct(
        "ETW_TrackbackTag" / Int32ul,
        "fInterrupt" / Int8ul,
        "sqmDocID" / Guid,
        "pdodMain" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=180, version=0)
class Microsoft_Office_Word_180_0(Etw):
    pattern = Struct(
        "SuspensionID" / Guid,
        "SQMDocID" / Guid,
        "pdod" / Int64ul,
        "fn" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=183, version=0)
class Microsoft_Office_Word_183_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=185, version=0)
class Microsoft_Office_Word_185_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=187, version=0)
class Microsoft_Office_Word_187_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=188, version=1)
class Microsoft_Office_Word_188_1(Etw):
    pattern = Struct(
        "fserr" / Int32sl,
        "ipgd" / Int32sl,
        "dk" / Int32ul,
        "fGoodClientDoc" / Int8ul,
        "wk" / Int32ul,
        "fWwdLayout" / Int8ul,
        "fWwdVBA" / Int8ul,
        "sqmDocID" / Guid,
        "pdodMain" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=189, version=2)
class Microsoft_Office_Word_189_2(Etw):
    pattern = Struct(
        "Caller" / WString,
        "pdodMain" / Int64ul,
        "pmwd" / Int64ul,
        "pwwd" / Int64ul,
        "OldViewType" / WString,
        "NewViewType" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=190, version=1)
class Microsoft_Office_Word_190_1(Etw):
    pattern = Struct(
        "Caller" / WString,
        "pmwd" / Int64ul,
        "pwwd" / Int64ul,
        "hwnd" / Int64ul,
        "ViewType" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=191, version=1)
class Microsoft_Office_Word_191_1(Etw):
    pattern = Struct(
        "Caller" / WString,
        "pmwd" / Int64ul,
        "pwwd" / Int64ul,
        "hwnd" / Int64ul,
        "ViewType" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=192, version=1)
class Microsoft_Office_Word_192_1(Etw):
    pattern = Struct(
        "Caller" / WString,
        "pmwdOld" / Int64ul,
        "pwwdOld" / Int64ul,
        "OldWwdViewType" / WString,
        "pmwdNew" / Int64ul,
        "pwwdNew" / Int64ul,
        "NewWwdViewType" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=193, version=1)
class Microsoft_Office_Word_193_1(Etw):
    pattern = Struct(
        "pwwd" / Int64ul,
        "WwdViewType" / WString,
        "xScroll" / Int32sl,
        "yScroll" / Int32sl,
        "CanvasWidth" / Int32sl,
        "CanvasHeight" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=196, version=2)
class Microsoft_Office_Word_196_2(Etw):
    pattern = Struct(
        "ReportID" / Int64ul,
        "IdleTaskName" / WString,
        "fRtcGroupIdle" / Int8ul,
        "Bucket050Count" / Int64ul,
        "Bucket50100Count" / Int64ul,
        "Bucket100150Count" / Int64ul,
        "Bucket150200Count" / Int64ul,
        "Bucket200350Count" / Int64ul,
        "Bucket350500Count" / Int64ul,
        "Bucket5001000Count" / Int64ul,
        "Bucket10002000Count" / Int64ul,
        "Bucket20005000Count" / Int64ul,
        "Bucket5000MaxCount" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=197, version=0)
class Microsoft_Office_Word_197_0(Etw):
    pattern = Struct(
        "mbit" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=198, version=0)
class Microsoft_Office_Word_198_0(Etw):
    pattern = Struct(
        "mbit" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=221, version=0)
class Microsoft_Office_Word_221_0(Etw):
    pattern = Struct(
        "HResult" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=222, version=2)
class Microsoft_Office_Word_222_2(Etw):
    pattern = Struct(
        "Tag" / Int32ul,
        "pdod" / Int64ul,
        "Allowed" / Int8ul,
        "Reason" / WString,
        "ExtraInfo" / WString,
        "ReasonInt" / Int32ul,
        "ContextTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=223, version=0)
class Microsoft_Office_Word_223_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "cp" / Int32sl,
        "E1oType" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=224, version=1)
class Microsoft_Office_Word_224_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "cp" / Int32sl,
        "E2oType" / Int32ul,
        "fAccessibilityRunning" / Int8ul,
        "wkWwd" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=225, version=0)
class Microsoft_Office_Word_225_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "cpStart" / Int32sl,
        "cpEnd" / Int32sl,
        "iTap" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=226, version=4)
class Microsoft_Office_Word_226_4(Etw):
    pattern = Struct(
        "facekind" / WString,
        "faceLeft" / Int32sl,
        "faceTop" / Int32sl,
        "faceRight" / Int32sl,
        "faceBottom" / Int32sl,
        "layerHandle" / Int32sl,
        "tE2oSelected" / Int32sl,
        "fVisible" / Int8ul,
        "cChildren" / Int32sl,
        "fHitTestChildrenOnly" / Int8ul,
        "fPinToScreen" / Int8ul,
        "fIgnoreFace" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=227, version=4)
class Microsoft_Office_Word_227_4(Etw):
    pattern = Struct(
        "facekind" / WString,
        "faceLeft" / Int32sl,
        "faceTop" / Int32sl,
        "faceRight" / Int32sl,
        "faceBottom" / Int32sl,
        "layerHandle" / Int32sl,
        "tE2oSelected" / Int32sl,
        "fVisible" / Int8ul,
        "cChildren" / Int32sl,
        "fHitTestChildrenOnly" / Int8ul,
        "fPinToScreen" / Int8ul,
        "fIgnoreFace" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=228, version=4)
class Microsoft_Office_Word_228_4(Etw):
    pattern = Struct(
        "facekind" / WString,
        "faceLeft" / Int32sl,
        "faceTop" / Int32sl,
        "faceRight" / Int32sl,
        "faceBottom" / Int32sl,
        "layerHandle" / Int32sl,
        "tE2oSelected" / Int32sl,
        "fVisible" / Int8ul,
        "cChildren" / Int32sl,
        "fHitTestChildrenOnly" / Int8ul,
        "fPinToScreen" / Int8ul,
        "fIgnoreFace" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=229, version=1)
class Microsoft_Office_Word_229_1(Etw):
    pattern = Struct(
        "ptX" / Int32sl,
        "ptY" / Int32sl,
        "fZoomMatches" / Int8ul,
        "dxeScroll" / Int32sl,
        "dyeScroll" / Int32sl,
        "tapLeft" / Int32sl,
        "tapTop" / Int32sl,
        "tapRight" / Int32sl,
        "tapBottom" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=230, version=0)
class Microsoft_Office_Word_230_0(Etw):
    pattern = Struct(
        "usec" / Int64ul,
        "iPagesTested" / Int32sl,
        "iFacesTested" / Int32sl,
        "cChildrenTree" / Int32sl,
        "cChildrenHitPage" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=231, version=0)
class Microsoft_Office_Word_231_0(Etw):
    pattern = Struct(
        "Tag" / Int32ul,
        "Interrupt" / Int8ul,
        "Reason" / WString,
        "ExtraInfo" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=232, version=0)
class Microsoft_Office_Word_232_0(Etw):
    pattern = Struct(
        "CountofIntervals" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=233, version=0)
class Microsoft_Office_Word_233_0(Etw):
    pattern = Struct(
        "CountofIntervals" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=234, version=1)
class Microsoft_Office_Word_234_1(Etw):
    pattern = Struct(
        "ReportID" / Int64ul,
        "Bucket0500Count" / Int64ul,
        "Bucket5001000Count" / Int64ul,
        "Bucket10002000Count" / Int64ul,
        "Bucket20005000Count" / Int64ul,
        "Bucket500010000Count" / Int64ul,
        "Bucket1000020000Count" / Int64ul,
        "Bucket2000050000Count" / Int64ul,
        "Bucket50000100000Count" / Int64ul,
        "Bucket100000300000Count" / Int64ul,
        "Bucket300000MaxCount" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=235, version=1)
class Microsoft_Office_Word_235_1(Etw):
    pattern = Struct(
        "MainDocCPCount" / Int32sl,
        "E2oTotalCount" / Int32sl,
        "E2oChartCount" / Int32sl,
        "E2oSmartArtCount" / Int32sl,
        "E2oPictureCount" / Int32sl,
        "E2oGroupCount" / Int32sl,
        "E2oTextBoxCount" / Int32sl,
        "E2oOLECount" / Int32sl,
        "E2oOthersCount" / Int32sl,
        "E1oTotalCount" / Int32sl,
        "E1oPictureCount" / Int32sl,
        "E1oGroupCount" / Int32sl,
        "E1oTextBoxCount" / Int32sl,
        "E1oOthersCount" / Int32sl,
        "HeaderFooterDocCPCount" / Int32sl,
        "FootNoteDocCPCount" / Int32sl,
        "FootNotesCount" / Int32sl,
        "EndNoteDocCPCount" / Int32sl,
        "EndNotesCount" / Int32sl,
        "CommentDocCPCount" / Int32sl,
        "CommentsCount" / Int32sl,
        "TxBxDocCPCount" / Int32sl,
        "pdodMain" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=236, version=1)
class Microsoft_Office_Word_236_1(Etw):
    pattern = Struct(
        "EvalFunc" / WString,
        "RuleType" / WString,
        "Rule" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=237, version=0)
class Microsoft_Office_Word_237_0(Etw):
    pattern = Struct(
        "editorsCount" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=238, version=1)
class Microsoft_Office_Word_238_1(Etw):
    pattern = Struct(
        "TagCaller" / Int32ul,
        "Issue" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=239, version=2)
class Microsoft_Office_Word_239_2(Etw):
    pattern = Struct(
        "ETW_TrackbackTag" / Int32ul,
        "CorruptionReason" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=241, version=0)
class Microsoft_Office_Word_241_0(Etw):
    pattern = Struct(
        "SQMDocID" / Guid,
        "pdod" / Int64ul,
        "pdodSrc" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=242, version=0)
class Microsoft_Office_Word_242_0(Etw):
    pattern = Struct(
        "SQMDocID" / Guid,
        "pdodSrc" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=243, version=0)
class Microsoft_Office_Word_243_0(Etw):
    pattern = Struct(
        "Issue" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=244, version=0)
class Microsoft_Office_Word_244_0(Etw):
    pattern = Struct(
        "ftyp" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=245, version=2)
class Microsoft_Office_Word_245_2(Etw):
    pattern = Struct(
        "SectionsCount" / Int32sl,
        "E2oIvyChartCount" / Int32sl,
        "pdodMain" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=246, version=0)
class Microsoft_Office_Word_246_0(Etw):
    pattern = Struct(
        "CurrentSection" / Int32sl,
        "HeaderFooterType" / Int32sl,
        "HasPAGEField" / Int8ul,
        "HasNUMPAGESField" / Int8ul,
        "HasLego" / Int8ul,
        "PNStartOn" / Int64ul,
        "PNFormat" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=249, version=0)
class Microsoft_Office_Word_249_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=250, version=0)
class Microsoft_Office_Word_250_0(Etw):
    pattern = Struct(
        "dxaLeftBefore" / Int64ul,
        "dxaRightBefore" / Int64ul,
        "dyaTopBefore" / Int64sl,
        "dyaBottomBefore" / Int64sl,
        "dzaGutterBefore" / Int64ul,
        "dxaLeftAfter" / Int64ul,
        "dxaRightAfter" / Int64ul,
        "dyaTopAfter" / Int64sl,
        "dyaBottomAfter" / Int64sl,
        "dzaGutterAfter" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=251, version=0)
class Microsoft_Office_Word_251_0(Etw):
    pattern = Struct(
        "dmPaperBefore" / Int32sl,
        "dmPaperAfter" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=252, version=0)
class Microsoft_Office_Word_252_0(Etw):
    pattern = Struct(
        "iColumnPresetBefore" / Int32sl,
        "iColumnPresetAfter" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=253, version=1)
class Microsoft_Office_Word_253_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "DocKind" / WString,
        "cp" / Int32sl,
        "GoodClient" / Int8ul,
        "FormatLineCallerStack" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=254, version=2)
class Microsoft_Office_Word_254_2(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "fStart" / Int8ul,
        "Reason" / Int32ul,
        "csiErrorCode" / Int32ul,
        "rtcState" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=255, version=2)
class Microsoft_Office_Word_255_2(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "Allowed" / Int8ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=256, version=2)
class Microsoft_Office_Word_256_2(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "fStart" / Int8ul,
        "Reason" / Int32ul,
        "csiErrorCode" / Int32ul,
        "rtcState" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=257, version=0)
class Microsoft_Office_Word_257_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "MergeAllowed" / Int8ul,
        "NoMergeReason" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=258, version=0)
class Microsoft_Office_Word_258_0(Etw):
    pattern = Struct(
        "TagCaller" / Int32ul,
        "currentScopeId" / Int32ul,
        "parentScopeId" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=259, version=0)
class Microsoft_Office_Word_259_0(Etw):
    pattern = Struct(
        "TagCaller" / Int32ul,
        "currentScopeId" / Int32ul,
        "parentScopeId" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=262, version=0)
class Microsoft_Office_Word_262_0(Etw):
    pattern = Struct(
        "reason" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=263, version=0)
class Microsoft_Office_Word_263_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "cSavesToMonitorForMovingAvg" / Int16ul,
        "MovingAvgThreshold" / Int32ul,
        "SaveSpike" / Int32ul,
        "SaveSpikeElapsedTimeThreshold" / Int32ul,
        "cGoodSavesToMonitor" / Int16ul,
        "GoodSaveTimeThreshold" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=264, version=1)
class Microsoft_Office_Word_264_1(Etw):
    pattern = Struct(
        "fDeepSleep" / Int8ul,
        "TimeSinceLastInputMsec" / Int64ul,
        "cMouse" / Int32sl,
        "cTouch" / Int32sl,
        "cKeyboard" / Int32sl,
        "cIME" / Int32sl,
        "cCommand" / Int32sl,
        "cZoom" / Int32sl,
        "cScroll" / Int32sl,
        "cDM" / Int32sl,
        "cPen" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=265, version=2)
class Microsoft_Office_Word_265_2(Etw):
    pattern = Struct(
        "ReportID" / Int64ul,
        "IdleTaskName" / WString,
        "fRtcGroupIdle" / Int8ul,
        "Bucket050Count" / Int64ul,
        "Bucket50100Count" / Int64ul,
        "Bucket100150Count" / Int64ul,
        "Bucket150200Count" / Int64ul,
        "Bucket200350Count" / Int64ul,
        "Bucket350500Count" / Int64ul,
        "Bucket5001000Count" / Int64ul,
        "Bucket10002000Count" / Int64ul,
        "Bucket20005000Count" / Int64ul,
        "Bucket5000MaxCount" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=266, version=1)
class Microsoft_Office_Word_266_1(Etw):
    pattern = Struct(
        "ETW_TrackbackTag" / Int32ul,
        "FailureType" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=267, version=1)
class Microsoft_Office_Word_267_1(Etw):
    pattern = Struct(
        "ETW_TrackbackTag" / Int32ul,
        "FailureType" / WString,
        "cChildrenTree" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=268, version=0)
class Microsoft_Office_Word_268_0(Etw):
    pattern = Struct(
        "cbGzipUncompressed" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=269, version=0)
class Microsoft_Office_Word_269_0(Etw):
    pattern = Struct(
        "OpenId" / Int32ul,
        "nFib" / Int16ul,
        "nFibCurr" / Int16ul,
        "StreamName" / WString,
        "StreamSizeBytes" / Int64sl,
        "fIsOCSB" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=270, version=1)
class Microsoft_Office_Word_270_1(Etw):
    pattern = Struct(
        "OpenId" / Int32ul,
        "IndexIntoFibshared" / Int32sl,
        "Cb" / Int64ul,
        "PercentOfTblStream" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=271, version=0)
class Microsoft_Office_Word_271_0(Etw):
    pattern = Struct(
        "SaveInitiateTag" / Int32ul,
        "SqmDocId" / Guid,
        "SaveInitiateKind" / Int32sl,
        "SaveAs" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=272, version=0)
class Microsoft_Office_Word_272_0(Etw):
    pattern = Struct(
        "SaveInitiateKind" / Int32sl,
        "SQMDocID" / Guid,
        "BkgndSaveLaunch" / Int8ul,
        "FailureRetry" / Int8ul,
        "HrCommitFileIO" / Int32sl,
        "SaveOpResult" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=273, version=0)
class Microsoft_Office_Word_273_0(Etw):
    pattern = Struct(
        "ContinueIdleReturn" / WString,
        "Count" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=274, version=0)
class Microsoft_Office_Word_274_0(Etw):
    pattern = Struct(
        "CancellationReason" / WString,
        "Count" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=275, version=0)
class Microsoft_Office_Word_275_0(Etw):
    pattern = Struct(
        "crsidBase" / Int32ul,
        "crsid0" / Int32ul,
        "crsid1" / Int32ul,
        "fBaseOver0" / Int8ul,
        "fBaseOver1" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=276, version=0)
class Microsoft_Office_Word_276_0(Etw):
    pattern = Struct(
        "Pdod" / Int64ul,
        "itcrr" / Int64ul,
        "citcrr" / Int64ul,
        "fit" / Int16ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=277, version=5)
class Microsoft_Office_Word_277_5(Etw):
    pattern = Struct(
        "ETW_TrackbackTag" / Int32ul,
        "pdod" / Int64ul,
        "pct" / Int32sl,
        "wkViewKind" / Int32ul,
        "fNoMargPgvw" / Int8ul,
        "fAlwaysSaveEnabled" / Int8ul,
        "edpiType" / Int32ul,
        "fTouch" / Int8ul,
        "fIme" / Int8ul,
        "msecUserInteractionTime" / Int64ul,
        "fTrackChanges" / Int8ul,
        "pageCount" / Int64sl,
        "fPageCountInProgress" / Int8ul,
        "wordCount" / Int64sl,
        "lineCount" / Int64sl,
        "paraCount" / Int64sl,
        "charCount" / Int64sl,
        "charWsCount" / Int64sl,
        "rsidCount" / Int32ul,
        "lidEditMru" / Int16ul,
        "szEditLids" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=278, version=0)
class Microsoft_Office_Word_278_0(Etw):
    pattern = Struct(
        "extension" / WString,
        "ftyp" / Int32sl,
        "fIsRetryOpen" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=279, version=0)
class Microsoft_Office_Word_279_0(Etw):
    pattern = Struct(
        "OriginalEncoding" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=280, version=0)
class Microsoft_Office_Word_280_0(Etw):
    pattern = Struct(
        "OriginalEncoding" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=281, version=0)
class Microsoft_Office_Word_281_0(Etw):
    pattern = Struct(
        "OriginalEncoding" / Int32sl,
        "ChangedEncoding" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=283, version=0)
class Microsoft_Office_Word_283_0(Etw):
    pattern = Struct(
        "HROptional" / Int32sl,
        "CodePage" / Int32sl,
        "Confidence" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=284, version=0)
class Microsoft_Office_Word_284_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "cp" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=285, version=0)
class Microsoft_Office_Word_285_0(Etw):
    pattern = Struct(
        "hrResult" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=287, version=0)
class Microsoft_Office_Word_287_0(Etw):
    pattern = Struct(
        "dusecInterval" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=288, version=0)
class Microsoft_Office_Word_288_0(Etw):
    pattern = Struct(
        "xszName" / WString,
        "fRtcGroupIdle" / Int8ul,
        "fResume" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=289, version=0)
class Microsoft_Office_Word_289_0(Etw):
    pattern = Struct(
        "xszName" / WString,
        "fRtcGroupIdle" / Int8ul,
        "fPause" / Int8ul,
        "dusecTaskInterval" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=290, version=0)
class Microsoft_Office_Word_290_0(Etw):
    pattern = Struct(
        "xszName" / WString,
        "fRtcGroupIdle" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=291, version=0)
class Microsoft_Office_Word_291_0(Etw):
    pattern = Struct(
        "xszName" / WString,
        "fRtcGroupIdle" / Int8ul,
        "dusecTaskInterval" / Int64ul,
        "fMsgPresent" / Int8ul,
        "dusecMsg" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=293, version=0)
class Microsoft_Office_Word_293_0(Etw):
    pattern = Struct(
        "fPause" / Int8ul,
        "dusecTaskInterval" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=294, version=1)
class Microsoft_Office_Word_294_1(Etw):
    pattern = Struct(
        "pwwd" / Int64ul,
        "m_cInBatch" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=295, version=1)
class Microsoft_Office_Word_295_1(Etw):
    pattern = Struct(
        "pwwd" / Int64ul,
        "m_cInBatch" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=298, version=1)
class Microsoft_Office_Word_298_1(Etw):
    pattern = Struct(
        "pwwd" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=299, version=1)
class Microsoft_Office_Word_299_1(Etw):
    pattern = Struct(
        "pwwd" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=301, version=1)
class Microsoft_Office_Word_301_1(Etw):
    pattern = Struct(
        "insloopID" / Int32ul,
        "pdod" / Int64ul,
        "docKind" / WString,
        "cpFirst" / Int32sl,
        "stateFrom" / Int32ul,
        "stateTo" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=302, version=0)
class Microsoft_Office_Word_302_0(Etw):
    pattern = Struct(
        "WM" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=303, version=0)
class Microsoft_Office_Word_303_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "fDefaultViewSetting" / Int8ul,
        "fViewStateSavingLogicUsed" / Int8ul,
        "UserType" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=304, version=0)
class Microsoft_Office_Word_304_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=305, version=0)
class Microsoft_Office_Word_305_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "pcoa" / Int64ul,
        "OptedIn" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=306, version=0)
class Microsoft_Office_Word_306_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "diReason" / Int16ul,
        "AutoSaveState" / Int32ul,
        "AutoCreateEventHandler" / Int32ul,
        "idReturn" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=307, version=0)
class Microsoft_Office_Word_307_0(Etw):
    pattern = Struct(
        "fStart" / Int8ul,
        "pioldoc" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=308, version=0)
class Microsoft_Office_Word_308_0(Etw):
    pattern = Struct(
        "AutorecoveryConfiguration" / Int32ul,
        "AutorecoveryInterval" / Int16ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=309, version=0)
class Microsoft_Office_Word_309_0(Etw):
    pattern = Struct(
        "fDelayUpdateWwdToEndInsert" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=311, version=1)
class Microsoft_Office_Word_311_1(Etw):
    pattern = Struct(
        "dwTag" / Int32ul,
        "fFallback" / Int8ul,
        "saveActionId" / Guid,
        "pdod" / Int64ul,
        "ftyp" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=312, version=0)
class Microsoft_Office_Word_312_0(Etw):
    pattern = Struct(
        "cmd" / Int32sl,
        "saveActionIdOrig" / Guid,
        "fSaveAsAttempted" / Int8ul,
        "fEmergencySave" / Int8ul,
        "fBsiIsFirst" / Int8ul,
        "pbsi" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=313, version=5)
class Microsoft_Office_Word_313_5(Etw):
    pattern = Struct(
        "Pdod" / Int64ul,
        "DocumentSessionId" / Int32ul,
        "AutoSaveActive" / Int8ul,
        "RtcActive" / Int8ul,
        "AutoSaveEnabled" / Int8ul,
        "RtcEnablementState" / Int32ul,
        "FlowEnabled" / Int8ul,
        "AutoSaveDisallowReason" / Int32ul,
        "AutoSaveBlockingReason" / Int32ul,
        "CsiStatusOk" / Int8ul,
        "CsiErrorCode" / Int32ul,
        "UserWantsAutoSave" / Int8ul,
        "GroupPolicyPermitsAutoSave" / Int8ul,
        "UpdateFlowDisabledReason" / Int32ul,
        "FEnableAutosaveWin32ODSP" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=314, version=0)
class Microsoft_Office_Word_314_0(Etw):
    pattern = Struct(
        "dwTag" / Int32ul,
        "message" / Int32ul,
        "TAppWndProcCloseReturn" / Int32sl,
        "fInFreezeDryClose" / Int8ul,
        "fInForceEndSession" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=315, version=0)
class Microsoft_Office_Word_315_0(Etw):
    pattern = Struct(
        "dwTag" / Int32ul,
        "ForegroundSave" / Int8ul,
        "saveActionId" / Guid,
        "pdod" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=316, version=0)
class Microsoft_Office_Word_316_0(Etw):
    pattern = Struct(
        "dmsecLastRenderedSinceEpoch" / Int64ul,
        "dmsecLastCharacterTurnAround" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=317, version=0)
class Microsoft_Office_Word_317_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "pdim" / Int64ul,
        "fEquation" / Int8ul,
        "fTable" / Int8ul,
        "selcurCpFirst" / Int64sl,
        "selcurCpLim" / Int64sl,
        "caParaCpFirst" / Int64sl,
        "caParaCpLim" / Int64sl,
        "m_cpInsert" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=318, version=0)
class Microsoft_Office_Word_318_0(Etw):
    pattern = Struct(
        "ETW_TrackbackTag" / Int32ul,
        "drk" / Int32ul,
        "drkx_drck" / Int32ul,
        "pdodDk" / Int32ul,
        "fTxbx" / Int8ul,
        "fMtxi" / Int8ul,
        "fTable" / Int8ul,
        "wkHwwd" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=319, version=0)
class Microsoft_Office_Word_319_0(Etw):
    pattern = Struct(
        "pmwd" / Int64ul,
        "dpiSys" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=320, version=0)
class Microsoft_Office_Word_320_0(Etw):
    pattern = Struct(
        "pmwd" / Int64ul,
        "dpiPerMonitor" / Int32sl,
        "fAlreadySeen" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=321, version=0)
class Microsoft_Office_Word_321_0(Etw):
    pattern = Struct(
        "pdodSrc" / Int64ul,
        "pIPersisterTrans" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=322, version=0)
class Microsoft_Office_Word_322_0(Etw):
    pattern = Struct(
        "pdodSrc" / Int64ul,
        "pIPersisterTrans" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=323, version=0)
class Microsoft_Office_Word_323_0(Etw):
    pattern = Struct(
        "pdodSrc" / Int64ul,
        "pIPersisterTrans" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=324, version=0)
class Microsoft_Office_Word_324_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "saveActionGuid" / Guid,
        "dwSrcTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=326, version=0)
class Microsoft_Office_Word_326_0(Etw):
    pattern = Struct(
        "pDod" / Int64ul,
        "runTime" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=327, version=0)
class Microsoft_Office_Word_327_0(Etw):
    pattern = Struct(
        "pDod" / Int64ul,
        "runTime" / Int64sl,
        "aggType" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=328, version=0)
class Microsoft_Office_Word_328_0(Etw):
    pattern = Struct(
        "pDod" / Int64ul,
        "runTime" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=329, version=0)
class Microsoft_Office_Word_329_0(Etw):
    pattern = Struct(
        "runTime" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=332, version=0)
class Microsoft_Office_Word_332_0(Etw):
    pattern = Struct(
        "fCompatCheckSuccess" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=334, version=0)
class Microsoft_Office_Word_334_0(Etw):
    pattern = Struct(
        "dypViewport" / Int32ul,
        "dypCard" / Int32ul,
        "pctRatioCardToViewport" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=335, version=0)
class Microsoft_Office_Word_335_0(Etw):
    pattern = Struct(
        "formatDesc" / WString,
        "fIsEjectable" / Int8ul,
        "fIsReadOnly" / Int8ul,
        "fIsEncrypted" / Int8ul,
        "fIsDirectory" / Int8ul,
        "fIsSymbolicLink" / Int8ul,
        "fileSaveType" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=336, version=1)
class Microsoft_Office_Word_336_1(Etw):
    pattern = Struct(
        "picCount" / Int64sl,
        "tocCount" / Int64sl,
        "fBibliography" / Int8ul,
        "pageNumberFieldCount" / Int64sl,
        "citationCount" / Int64sl,
        "chartCount" / Int64sl,
        "ivyChartCount" / Int64sl,
        "bkmkRefCount" / Int64sl,
        "fHeader" / Int8ul,
        "footnoteDocCount" / Int64sl,
        "endnoteDocCount" / Int64sl,
        "fUserHasEdited" / Int8ul,
        "heading1Count" / Int64sl,
        "heading2Count" / Int64sl,
        "heading3Count" / Int64sl,
        "fIsReadOnly" / Int8ul,
        "smartArtCount" / Int64sl,
        "heading1Length" / Int64sl,
        "heading2Length" / Int64sl,
        "heading3Length" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=337, version=0)
class Microsoft_Office_Word_337_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "piErrorOut" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=338, version=1)
class Microsoft_Office_Word_338_1(Etw):
    pattern = Struct(
        "ETW_TrackbackTag" / Int32ul,
        "fPidim0" / Int32ul,
        "fPidim1" / Int32ul,
        "fPidimB" / Int32ul,
        "fPidim0A" / Int32ul,
        "fPidim1A" / Int32ul,
        "fPidimBA" / Int32ul,
        "did0BEns" / Int64ul,
        "did1BEns" / Int64ul,
        "didBBEns" / Int64ul,
        "did0AEns" / Int64ul,
        "did1AEns" / Int64ul,
        "didBAEns" / Int64ul,
        "did0AAgr" / Int64ul,
        "did1AAgr" / Int64ul,
        "didBAAgr" / Int64ul,
        "fObjIn0" / Int8ul,
        "fObjIn1" / Int8ul,
        "fObjInB" / Int8ul,
        "fVclok" / Int8ul,
        "fBAncestOf0" / Int8ul,
        "fBAncestOf1" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=339, version=1)
class Microsoft_Office_Word_339_1(Etw):
    pattern = Struct(
        "ETW_TrackbackTag" / Int32ul,
        "fPidim0" / Int32ul,
        "fPidim1" / Int32ul,
        "fPidimB" / Int32ul,
        "fPidim0A" / Int32ul,
        "fPidim1A" / Int32ul,
        "fPidimBA" / Int32ul,
        "did0BEns" / Int64ul,
        "did1BEns" / Int64ul,
        "didBBEns" / Int64ul,
        "did0AEns" / Int64ul,
        "did1AEns" / Int64ul,
        "didBAEns" / Int64ul,
        "did0AAgr" / Int64ul,
        "did1AAgr" / Int64ul,
        "didBAAgr" / Int64ul,
        "fObjIn0" / Int8ul,
        "fObjIn1" / Int8ul,
        "fObjInB" / Int8ul,
        "fVclok" / Int8ul,
        "fBAncestOf0" / Int8ul,
        "fBAncestOf1" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=340, version=0)
class Microsoft_Office_Word_340_0(Etw):
    pattern = Struct(
        "dirulEval" / Int32sl,
        "lidKbd" / Int16ul,
        "lidInstall" / Int16ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=341, version=0)
class Microsoft_Office_Word_341_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "fPrintMet" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=342, version=0)
class Microsoft_Office_Word_342_0(Etw):
    pattern = Struct(
        "expectedJpnEraYear" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=343, version=0)
class Microsoft_Office_Word_343_0(Etw):
    pattern = Struct(
        "actualJpnEraYear" / Int32ul,
        "gregorianYear" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=344, version=0)
class Microsoft_Office_Word_344_0(Etw):
    pattern = Struct(
        "FRet" / Int8ul,
        "Pdod" / Int64ul,
        "CersBefore" / Int32ul,
        "CersAfter" / Int32ul,
        "Cerdr" / Int32ul,
        "Cerwr" / Int32ul,
        "Cerfr" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=345, version=0)
class Microsoft_Office_Word_345_0(Etw):
    pattern = Struct(
        "FSuccess" / Int8ul,
        "Pdod" / Int64ul,
        "ElapsedTimeMs" / Int64ul,
        "CsiErrorCode" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=346, version=0)
class Microsoft_Office_Word_346_0(Etw):
    pattern = Struct(
        "Pdod" / Int64ul,
        "CersBefore" / Int32ul,
        "CersAfter" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=347, version=0)
class Microsoft_Office_Word_347_0(Etw):
    pattern = Struct(
        "Pdod" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=348, version=0)
class Microsoft_Office_Word_348_0(Etw):
    pattern = Struct(
        "Pdod" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=349, version=0)
class Microsoft_Office_Word_349_0(Etw):
    pattern = Struct(
        "Pdod" / Int64ul,
        "fMergeExecuted" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=351, version=0)
class Microsoft_Office_Word_351_0(Etw):
    pattern = Struct(
        "fAccessibilityRunning" / Int8ul,
        "wkWwd" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=352, version=0)
class Microsoft_Office_Word_352_0(Etw):
    pattern = Struct(
        "saveActionGuid" / Guid,
        "pdod" / Int64ul,
        "fIgnore" / Int8ul,
        "fBeginBatchDone" / Int8ul,
        "fAttachKposDone" / Int8ul,
        "fRevertDone" / Int8ul,
        "fDoDestroy" / Int8ul,
        "usecExecTime" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=353, version=0)
class Microsoft_Office_Word_353_0(Etw):
    pattern = Struct(
        "saveActionGuid" / Guid,
        "pdod" / Int64ul,
        "fEndBatchDone" / Int8ul,
        "fInvokeKposDone" / Int8ul,
        "fReplayDone" / Int8ul,
        "fDoDestroy" / Int8ul,
        "fSubDocDeleted" / Int8ul,
        "usecCreateTime" / Int64sl,
        "usecDestroyTime" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=354, version=0)
class Microsoft_Office_Word_354_0(Etw):
    pattern = Struct(
        "usecNextSaveTime" / Int64ul,
        "usecMostRecentSaveEvent" / Int64ul,
        "m_dusecDynamicSaveCooldownInterval" / Int64ul,
        "usecNow" / Int64ul,
        "m_grfdysgLastAdjustedReason" / Int32sl,
        "fOcsMode" / Int8ul,
        "m_dusecDefaultSaveCooldownInterval" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1401, version=0)
class Microsoft_Office_Word_1401_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul,
        "cmdRet" / Int32sl,
        "fDidSave" / Int8ul,
        "fDidAutosave" / Int8ul,
        "fConflict" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1403, version=0)
class Microsoft_Office_Word_1403_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1405, version=0)
class Microsoft_Office_Word_1405_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1407, version=0)
class Microsoft_Office_Word_1407_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1409, version=0)
class Microsoft_Office_Word_1409_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1411, version=0)
class Microsoft_Office_Word_1411_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1412, version=1)
class Microsoft_Office_Word_1412_1(Etw):
    pattern = Struct(
        "saveActionId" / Guid,
        "sqmDocId" / Guid,
        "ftyp" / Int32sl,
        "fSaveAs" / Int8ul,
        "sqmDocLocation" / Int32sl,
        "AuthorsCount" / Int32sl,
        "fMultipleAuthors" / Int8ul,
        "fCoAuthorable" / Int8ul,
        "fOnBackgroundThread" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1413, version=1)
class Microsoft_Office_Word_1413_1(Etw):
    pattern = Struct(
        "saveActionId" / Guid,
        "sqmDocId" / Guid,
        "fMergeRequired" / Int8ul,
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1415, version=0)
class Microsoft_Office_Word_1415_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1416, version=1)
class Microsoft_Office_Word_1416_1(Etw):
    pattern = Struct(
        "HResult" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1417, version=1)
class Microsoft_Office_Word_1417_1(Etw):
    pattern = Struct(
        "HResult" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1418, version=2)
class Microsoft_Office_Word_1418_2(Etw):
    pattern = Struct(
        "HResult" / Int32sl,
        "PersisterType" / Int32ul,
        "fIsMerge" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1419, version=2)
class Microsoft_Office_Word_1419_2(Etw):
    pattern = Struct(
        "HResult" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1421, version=1)
class Microsoft_Office_Word_1421_1(Etw):
    pattern = Struct(
        "HResult" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1422, version=1)
class Microsoft_Office_Word_1422_1(Etw):
    pattern = Struct(
        "HResult" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1423, version=1)
class Microsoft_Office_Word_1423_1(Etw):
    pattern = Struct(
        "HResult" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1428, version=0)
class Microsoft_Office_Word_1428_0(Etw):
    pattern = Struct(
        "SaveActionId" / Guid,
        "Caller" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1429, version=0)
class Microsoft_Office_Word_1429_0(Etw):
    pattern = Struct(
        "SaveActionId" / Guid,
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1430, version=0)
class Microsoft_Office_Word_1430_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "sqmDocID" / Guid,
        "SqmDocLocation" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1431, version=2)
class Microsoft_Office_Word_1431_2(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "pioldoc" / Int64ul,
        "GuidFileId" / Guid,
        "sqmDocID" / Guid,
        "SqmDocLocation" / Int32sl,
        "FirstEditId" / Guid,
        "CsiErrorCode" / Int32ul,
        "EditToUploadTimeMicroseconds" / Int64ul,
        "FirstRtcBrkEditId" / Guid,
        "RtcBrkEditToUploadTimeMicroseconds" / Int64ul,
        "fRtcEnabled" / Int8ul,
        "fAutoSaveEnabled" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1432, version=0)
class Microsoft_Office_Word_1432_0(Etw):
    pattern = Struct(
        "HResult" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1433, version=0)
class Microsoft_Office_Word_1433_0(Etw):
    pattern = Struct(
        "result" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1434, version=0)
class Microsoft_Office_Word_1434_0(Etw):
    pattern = Struct(
        "PropertyType" / WString,
        "fChoose0" / Int8ul,
        "fComparedWithBase" / Int8ul,
        "Endpoint" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1435, version=0)
class Microsoft_Office_Word_1435_0(Etw):
    pattern = Struct(
        "dmsecSinceLastScheduleLoad" / Int64ul,
        "fPendingLoad" / Int8ul,
        "pdod" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1436, version=0)
class Microsoft_Office_Word_1436_0(Etw):
    pattern = Struct(
        "IsSubscribed" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1437, version=0)
class Microsoft_Office_Word_1437_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "dk" / Int32ul,
        "iCmdDoDiffTag" / Int32ul,
        "ITap" / Int32ul,
        "TMI" / Int8ul,
        "fCancelDel" / Int8ul,
        "itc" / Int32ul,
        "fMarkIns" / Int8ul,
        "fMarkDel" / Int8ul,
        "parid0CpCell" / Int32ul,
        "cpFirst" / Int32ul,
        "cpLim" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1438, version=0)
class Microsoft_Office_Word_1438_0(Etw):
    pattern = Struct(
        "dwTag" / Int32ul,
        "dk" / Int32ul,
        "cpFirst" / Int32ul,
        "cpLim" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1439, version=0)
class Microsoft_Office_Word_1439_0(Etw):
    pattern = Struct(
        "pdodSrc" / Int64ul,
        "dk" / Int32ul,
        "parid" / Int32ul,
        "cpFirst" / Int32ul,
        "cpLim" / Int32ul,
        "isGroup" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1441, version=0)
class Microsoft_Office_Word_1441_0(Etw):
    pattern = Struct(
        "ContentElement" / Int32ul,
        "CoauthUserAction" / Int32ul,
        "EditToSaveTime" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1442, version=0)
class Microsoft_Office_Word_1442_0(Etw):
    pattern = Struct(
        "iCmdDoDiffTag" / Int32ul,
        "scenarioType" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1460, version=2)
class Microsoft_Office_Word_1460_2(Etw):
    pattern = Struct(
        "fStart" / Int8ul,
        "fIsAlwaysSave" / Int8ul,
        "SqmDocId" / Guid,
        "DocumentId" / Int64ul,
        "pioldoc" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1461, version=2)
class Microsoft_Office_Word_1461_2(Etw):
    pattern = Struct(
        "saveActionId" / Guid,
        "sqmDocId" / Guid,
        "ftyp" / Int32sl,
        "fSaveAs" / Int8ul,
        "sqmDocLocation" / Int32sl,
        "AuthorsCount" / Int32sl,
        "fMultipleAuthors" / Int8ul,
        "fCoAuthorable" / Int8ul,
        "fOnBackgroundThread" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1462, version=2)
class Microsoft_Office_Word_1462_2(Etw):
    pattern = Struct(
        "saveActionId" / Guid,
        "sqmDocId" / Guid,
        "fMergeRequired" / Int8ul,
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1463, version=2)
class Microsoft_Office_Word_1463_2(Etw):
    pattern = Struct(
        "saveActionId" / Guid,
        "sqmDocId" / Guid,
        "ftyp" / Int32sl,
        "fSaveAs" / Int8ul,
        "sqmDocLocation" / Int32sl,
        "AuthorsCount" / Int32sl,
        "fMultipleAuthors" / Int8ul,
        "fCoAuthorable" / Int8ul,
        "fOnBackgroundThread" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1464, version=2)
class Microsoft_Office_Word_1464_2(Etw):
    pattern = Struct(
        "saveActionId" / Guid,
        "sqmDocId" / Guid,
        "fMergeRequired" / Int8ul,
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1466, version=0)
class Microsoft_Office_Word_1466_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1468, version=0)
class Microsoft_Office_Word_1468_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1470, version=0)
class Microsoft_Office_Word_1470_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1472, version=0)
class Microsoft_Office_Word_1472_0(Etw):
    pattern = Struct(
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1473, version=0)
class Microsoft_Office_Word_1473_0(Etw):
    pattern = Struct(
        "Tag" / Int32ul,
        "pdod" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1474, version=0)
class Microsoft_Office_Word_1474_0(Etw):
    pattern = Struct(
        "Tag" / Int32ul,
        "pdod" / Int64ul,
        "Type" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1475, version=0)
class Microsoft_Office_Word_1475_0(Etw):
    pattern = Struct(
        "Tag" / Int32ul,
        "pdod" / Int64ul,
        "Type" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1476, version=1)
class Microsoft_Office_Word_1476_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "SqmDocId" / Guid,
        "cIntervals" / Int32ul,
        "Bucket1MinMsec" / Int64ul,
        "Bucket2MinMsec" / Int64ul,
        "Bucket3MinMsec" / Int64ul,
        "Bucket4MinMsec" / Int64ul,
        "Bucket5MinMsec" / Int64ul,
        "Bucket6MinMsec" / Int64ul,
        "Bucket7MinMsec" / Int64ul,
        "Bucket8MinMsec" / Int64ul,
        "Bucket9MinMsec" / Int64ul,
        "Bucket10MinMsec" / Int64ul,
        "Bucket1Count" / Int64ul,
        "Bucket2Count" / Int64ul,
        "Bucket3Count" / Int64ul,
        "Bucket4Count" / Int64ul,
        "Bucket5Count" / Int64ul,
        "Bucket6Count" / Int64ul,
        "Bucket7Count" / Int64ul,
        "Bucket8Count" / Int64ul,
        "Bucket9Count" / Int64ul,
        "Bucket10Count" / Int64ul,
        "TopUnresponsiveDuration1Msec" / Int64ul,
        "TopUnresponsiveDuration2Msec" / Int64ul,
        "TopUnresponsiveDuration3Msec" / Int64ul,
        "TopUnresponsiveDuration4Msec" / Int64ul,
        "TopUnresponsiveDuration5Msec" / Int64ul,
        "IStm" / Int32ul,
        "SqmDocLocation" / Int32ul,
        "AuthorCount" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1477, version=0)
class Microsoft_Office_Word_1477_0(Etw):
    pattern = Struct(
        "CountofIntervals" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1478, version=0)
class Microsoft_Office_Word_1478_0(Etw):
    pattern = Struct(
        "CountofIntervals" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1479, version=1)
class Microsoft_Office_Word_1479_1(Etw):
    pattern = Struct(
        "pdodSrc" / Int64ul,
        "pIOTransaction" / Int64ul,
        "iotType" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1480, version=7)
class Microsoft_Office_Word_1480_7(Etw):
    pattern = Struct(
        "pdodSrc" / Int64ul,
        "pIOTransaction" / Int64ul,
        "iotType" / Int32ul,
        "iotFinalState" / Int32ul,
        "fMergeSucceeded" / Int8ul,
        "fConflict" / Int8ul,
        "fLoad" / Int8ul,
        "fCoroutineLoadDone" / Int8ul,
        "fCoroutineSaveDone" / Int8ul,
        "fDelayedLoadOnCoroutine" / Int8ul,
        "ElapsedTimeMicroseconds" / Int64ul,
        "persisterTransactionType" / Int32ul,
        "persisterType" / Int32ul,
        "strMeasurement" / WString,
        "fDocmCoauthEnabled" / Int8ul,
        "ftyp" / Int32ul,
        "coauthDisableReason" / Int32ul,
        "exclusiveLockReason" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1481, version=1)
class Microsoft_Office_Word_1481_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "docKind" / Int32ul,
        "pcoctxt" / Int64ul,
        "iCmdDoDiffTag" / Int32ul,
        "parid0OfCpFirst" / Int32ul,
        "parid0OfCpLast" / Int32ul,
        "parid1OfCpFirst" / Int32ul,
        "parid1OfCpLast" / Int32ul,
        "pcob" / Int64ul,
        "fChangeIn0" / Int8ul,
        "fChangeIn1" / Int8ul,
        "fInserted0" / Int8ul,
        "fInserted1" / Int8ul,
        "fDeleted0" / Int8ul,
        "fDeleted1" / Int8ul,
        "fDeletedPara0" / Int8ul,
        "fDeletedPara1" / Int8ul,
        "dcpChange0" / Int32ul,
        "dcpChange1" / Int32ul,
        "fConflictVisible" / Int8ul,
        "cpFirst" / Int32sl,
        "cpLim" / Int32sl,
        "cpFirst1" / Int32sl,
        "cpLim1" / Int32sl,
        "cpLim0ForChange0" / Int32sl,
        "cpLim0ForChange1" / Int32sl,
        "parid0ForChange0" / Int32ul,
        "parid0ForChange1" / Int32ul,
        "dcpConflict" / Int32sl,
        "cEntriesInResolvePane" / Int32ul,
        "cxchPara0" / Int32ul,
        "elapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1482, version=0)
class Microsoft_Office_Word_1482_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "docKind" / Int32ul,
        "pcoctxt" / Int64ul,
        "fChangeInLocalDoc" / Int8ul,
        "dcpChange" / Int32sl,
        "elapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1483, version=0)
class Microsoft_Office_Word_1483_0(Etw):
    pattern = Struct(
        "iotType" / Int32ul,
        "iotStatePrev" / Int32ul,
        "iotStateNext" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1484, version=0)
class Microsoft_Office_Word_1484_0(Etw):
    pattern = Struct(
        "Tag" / Int32ul,
        "pioldoc" / Int64ul,
        "fReadOnly" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1485, version=0)
class Microsoft_Office_Word_1485_0(Etw):
    pattern = Struct(
        "Tag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1486, version=1)
class Microsoft_Office_Word_1486_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "guidSqmDocId" / Guid,
        "cpMac" / Int32sl,
        "fAutoSaveOff" / Int8ul,
        "fUserRequestedSave" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1487, version=0)
class Microsoft_Office_Word_1487_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "guidSqmDocId" / Guid,
        "cpMac" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1488, version=0)
class Microsoft_Office_Word_1488_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "guidSqmDocId" / Guid,
        "cpMac" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1489, version=0)
class Microsoft_Office_Word_1489_0(Etw):
    pattern = Struct(
        "pioldoc" / Int64ul,
        "pioldocOther" / Int64ul,
        "iolcmd" / Int32ul,
        "iolcmdPrev" / Int32ul,
        "dwCallsite" / Int32ul,
        "fOnMainThread" / Int8ul,
        "fValidThread" / Int8ul,
        "hrBeginCmd" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1490, version=0)
class Microsoft_Office_Word_1490_0(Etw):
    pattern = Struct(
        "pioldoc" / Int64ul,
        "iolcmd" / Int32ul,
        "iolcmdPrev" / Int32ul,
        "dwCallsite" / Int32ul,
        "fOnMainThread" / Int8ul,
        "fValidThread" / Int8ul,
        "hrMisc" / Int32sl,
        "hrRecordEvent" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1491, version=0)
class Microsoft_Office_Word_1491_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "iotType" / Int32ul,
        "persisterTransactionType" / Int32ul,
        "persisterType" / Int32ul,
        "iotState" / Int32ul,
        "fFocusLost" / Int8ul,
        "saveInitiateKind" / Int32sl,
        "ElapsedTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1501, version=0)
class Microsoft_Office_Word_1501_0(Etw):
    pattern = Struct(
        "fSuccess" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1502, version=1)
class Microsoft_Office_Word_1502_1(Etw):
    pattern = Struct(
        "MainThread" / Int8ul,
        "NumFontsInTable" / Int32sl,
        "Reason" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1503, version=0)
class Microsoft_Office_Word_1503_0(Etw):
    pattern = Struct(
        "NumFontsInTable" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1504, version=0)
class Microsoft_Office_Word_1504_0(Etw):
    pattern = Struct(
        "FontNameRequested" / WString,
        "CharSetRequested" / Int32ul,
        "FTCResolved" / Int32sl,
        "FontNameResolved" / WString,
        "CharSetResolved" / Int32ul,
        "FTCResolvedFrom" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1505, version=0)
class Microsoft_Office_Word_1505_0(Etw):
    pattern = Struct(
        "FontName" / WString,
        "CharSet" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1506, version=0)
class Microsoft_Office_Word_1506_0(Etw):
    pattern = Struct(
        "FontName" / WString,
        "CharSet" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1507, version=1)
class Microsoft_Office_Word_1507_1(Etw):
    pattern = Struct(
        "FontName" / WString,
        "pdodMain" / Int64ul,
        "dk" / Int32ul,
        "cpStart" / Int64sl,
        "cpLim" / Int64sl,
        "CpMacPdod" / Int64sl,
        "Lid" / Int16ul,
        "Style" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1508, version=0)
class Microsoft_Office_Word_1508_0(Etw):
    pattern = Struct(
        "FontName" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1510, version=0)
class Microsoft_Office_Word_1510_0(Etw):
    pattern = Struct(
        "FontName" / WString,
        "Fticm" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1511, version=0)
class Microsoft_Office_Word_1511_0(Etw):
    pattern = Struct(
        "NameFromLogfont" / WString,
        "FaceNameLoaded" / WString,
        "Fticm" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1513, version=0)
class Microsoft_Office_Word_1513_0(Etw):
    pattern = Struct(
        "FontName" / WString,
        "FontSize" / Int32ul,
        "pdodMain" / Int64ul,
        "dk" / Int32ul,
        "cpStart" / Int64sl,
        "cpLim" / Int64sl,
        "CpMacPdod" / Int64sl,
        "Lid" / Int16ul,
        "Style" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1514, version=0)
class Microsoft_Office_Word_1514_0(Etw):
    pattern = Struct(
        "FontSize" / Float32l,
        "pdodMain" / Int64ul,
        "dk" / Int32ul,
        "cpStart" / Int64sl,
        "cpLim" / Int64sl,
        "CpMacPdod" / Int64sl,
        "Lid" / Int16ul,
        "Style" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1515, version=0)
class Microsoft_Office_Word_1515_0(Etw):
    pattern = Struct(
        "FontNameAscii" / WString,
        "FontNameFE" / WString,
        "FontNameOther" / WString,
        "FontNameBi" / WString,
        "FontSizeAscii" / Float32l,
        "FontSizeBi" / Float32l,
        "pdodMain" / Int64ul,
        "dk" / Int32ul,
        "cpStart" / Int64sl,
        "cpLim" / Int64sl,
        "CpMacPdod" / Int64sl,
        "Lid" / Int16ul,
        "Style" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1516, version=0)
class Microsoft_Office_Word_1516_0(Etw):
    pattern = Struct(
        "FontName" / WString,
        "pdodMain" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1517, version=0)
class Microsoft_Office_Word_1517_0(Etw):
    pattern = Struct(
        "FontName" / WString,
        "FontSize" / Float32l,
        "pdodMain" / Int64ul,
        "CharacterCount" / Int64sl,
        "WordCount" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1518, version=0)
class Microsoft_Office_Word_1518_0(Etw):
    pattern = Struct(
        "EmbedLicenseType" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1519, version=0)
class Microsoft_Office_Word_1519_0(Etw):
    pattern = Struct(
        "NameFromLogfont" / WString,
        "FaceNameLoaded" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1520, version=0)
class Microsoft_Office_Word_1520_0(Etw):
    pattern = Struct(
        "FontName" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1521, version=0)
class Microsoft_Office_Word_1521_0(Etw):
    pattern = Struct(
        "ErrorKind" / Int16ul,
        "GetLastError" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1600, version=1)
class Microsoft_Office_Word_1600_1(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1601, version=1)
class Microsoft_Office_Word_1601_1(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1603, version=0)
class Microsoft_Office_Word_1603_0(Etw):
    pattern = Struct(
        "lid" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1605, version=0)
class Microsoft_Office_Word_1605_0(Etw):
    pattern = Struct(
        "lid" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1606, version=1)
class Microsoft_Office_Word_1606_1(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1607, version=1)
class Microsoft_Office_Word_1607_1(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1609, version=0)
class Microsoft_Office_Word_1609_0(Etw):
    pattern = Struct(
        "lid" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1611, version=0)
class Microsoft_Office_Word_1611_0(Etw):
    pattern = Struct(
        "lid" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1612, version=1)
class Microsoft_Office_Word_1612_1(Etw):
    pattern = Struct(
        "correlationId" / Int32sl,
        "logId" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1613, version=1)
class Microsoft_Office_Word_1613_1(Etw):
    pattern = Struct(
        "lid" / Int32sl,
        "kmcHandled" / Int32sl,
        "correlationId" / Int32sl,
        "logId" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1615, version=0)
class Microsoft_Office_Word_1615_0(Etw):
    pattern = Struct(
        "lid" / Int32sl,
        "kmcHandled" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1617, version=0)
class Microsoft_Office_Word_1617_0(Etw):
    pattern = Struct(
        "lid" / Int32sl,
        "kmcHandled" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1619, version=0)
class Microsoft_Office_Word_1619_0(Etw):
    pattern = Struct(
        "lid" / Int32sl,
        "kmcHandled" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1621, version=0)
class Microsoft_Office_Word_1621_0(Etw):
    pattern = Struct(
        "lid" / Int32sl,
        "kmcHandled" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1623, version=0)
class Microsoft_Office_Word_1623_0(Etw):
    pattern = Struct(
        "lid" / Int32sl,
        "kmcHandled" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1624, version=1)
class Microsoft_Office_Word_1624_1(Etw):
    pattern = Struct(
        "Tag" / Int32ul,
        "correlationIdStart" / Int32sl,
        "correlationIdEnd" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1625, version=0)
class Microsoft_Office_Word_1625_0(Etw):
    pattern = Struct(
        "messagePostDelayMs" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1626, version=2)
class Microsoft_Office_Word_1626_2(Etw):
    pattern = Struct(
        "correlationIdStart" / Int32sl,
        "correlationIdEnd" / Int32sl,
        "fAlwaysSaveEnabledAndOn" / Int8ul,
        "fWetChangesInDocument" / Int8ul,
        "fDuringOrAfterRecentAutoSave" / Int8ul,
        "fInOcsMode" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1627, version=4)
class Microsoft_Office_Word_1627_4(Etw):
    pattern = Struct(
        "dmsecTypingTime" / Int64ul,
        "dmsecMessagePostDelay" / Int64ul,
        "dmsecTypedChar" / Int64ul,
        "dmsecAirspaceRender" / Int64ul,
        "DocumentId" / Int64ul,
        "SqmDocId" / Guid,
        "DocKind" / WString,
        "fAlwaysSaveEnabledAndOn" / Int8ul,
        "fWetChangesInDocument" / Int8ul,
        "fDuringOrAfterRecentAutoSave" / Int8ul,
        "fInOcsMode" / Int8ul,
        "fChunking" / Int8ul,
        "fUIMCharacter" / Int8ul,
        "Pdod" / Int64ul,
        "Lid" / Int16ul,
        "fShaping" / Int8ul,
        "fAcetate" / Int8ul,
        "fAbdkRMAtn" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1700, version=0)
class Microsoft_Office_Word_1700_0(Etw):
    pattern = Struct(
        "softKeyboardIsLocked" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1701, version=0)
class Microsoft_Office_Word_1701_0(Etw):
    pattern = Struct(
        "touchX" / Int32sl,
        "touchY" / Int32sl,
        "grippyX" / Int32sl,
        "grippyY" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1703, version=0)
class Microsoft_Office_Word_1703_0(Etw):
    pattern = Struct(
        "distance" / Double,
        "newTouchX" / Int32sl,
        "newTouchY" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1704, version=0)
class Microsoft_Office_Word_1704_0(Etw):
    pattern = Struct(
        "cpStart" / Int64sl,
        "cpLim" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1705, version=1)
class Microsoft_Office_Word_1705_1(Etw):
    pattern = Struct(
        "CP" / Int32sl,
        "DoubleTap" / Int8ul,
        "NestedLevelitap" / Int32sl,
        "MaxRows" / Int32sl,
        "MaxColumns" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1706, version=0)
class Microsoft_Office_Word_1706_0(Etw):
    pattern = Struct(
        "Index" / Int32sl,
        "ValidRow" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1707, version=1)
class Microsoft_Office_Word_1707_1(Etw):
    pattern = Struct(
        "CP" / Int32sl,
        "DoubleTap" / Int8ul,
        "NestedLevelitap" / Int32sl,
        "MaxRows" / Int32sl,
        "MaxColumns" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1708, version=0)
class Microsoft_Office_Word_1708_0(Etw):
    pattern = Struct(
        "Index" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1709, version=1)
class Microsoft_Office_Word_1709_1(Etw):
    pattern = Struct(
        "DoubleTap" / Int8ul,
        "MaxRows" / Int32sl,
        "MaxColumns" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1711, version=0)
class Microsoft_Office_Word_1711_0(Etw):
    pattern = Struct(
        "PointerId" / Int32ul,
        "CanDM" / Int32sl,
        "UITEH" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1712, version=0)
class Microsoft_Office_Word_1712_0(Etw):
    pattern = Struct(
        "Gesture" / Int32sl,
        "PointerId" / Int32ul,
        "InteractionState" / Int32ul,
        "PointX" / Int32sl,
        "PointY" / Int32sl,
        "DeltaX" / Int32sl,
        "DeltaY" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1713, version=1)
class Microsoft_Office_Word_1713_1(Etw):
    pattern = Struct(
        "Gesture" / Int32sl,
        "PointerId" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1714, version=0)
class Microsoft_Office_Word_1714_0(Etw):
    pattern = Struct(
        "InputType" / Int32ul,
        "PointerId" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1715, version=0)
class Microsoft_Office_Word_1715_0(Etw):
    pattern = Struct(
        "teh" / Int32ul,
        "InputType" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1716, version=0)
class Microsoft_Office_Word_1716_0(Etw):
    pattern = Struct(
        "uiteh" / Int32ul,
        "InputType" / Int32ul,
        "PointerId" / Int32ul,
        "CanDM" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1900, version=0)
class Microsoft_Office_Word_1900_0(Etw):
    pattern = Struct(
        "segid" / Int32ul,
        "iseg" / Int32ul,
        "dcpRelative" / Int64ul,
        "dcpSegmentStart" / Int64ul,
        "dcpSegmentEnd" / Int64ul,
        "dcpShift" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1901, version=0)
class Microsoft_Office_Word_1901_0(Etw):
    pattern = Struct(
        "m_ptct" / WString,
        "m_sppts" / Int8ul,
        "m_spptsbstrText" / WString,
        "m_spptcc" / Int8ul,
        "m_spptccsegid" / Int32ul,
        "m_spptcciseg" / Int32ul,
        "m_spptccdcpRelative" / Int64ul,
        "m_spptccdcpSegmentStart" / Int64ul,
        "m_spptccdcpSegmentEnd" / Int64ul,
        "m_spptccdcpShift" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1902, version=0)
class Microsoft_Office_Word_1902_0(Etw):
    pattern = Struct(
        "m_ptct" / WString,
        "m_sppts" / Int8ul,
        "m_spptsbstrText" / WString,
        "m_spptcc" / Int8ul,
        "m_spptccsegid" / Int32ul,
        "m_spptcciseg" / Int32ul,
        "m_spptccdcpRelative" / Int64ul,
        "m_spptccdcpSegmentStart" / Int64ul,
        "m_spptccdcpSegmentEnd" / Int64ul,
        "m_spptccdcpShift" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1903, version=0)
class Microsoft_Office_Word_1903_0(Etw):
    pattern = Struct(
        "segid" / Int32ul,
        "dcpShift" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1904, version=0)
class Microsoft_Office_Word_1904_0(Etw):
    pattern = Struct(
        "segid" / Int32ul,
        "dcpShift" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1905, version=0)
class Microsoft_Office_Word_1905_0(Etw):
    pattern = Struct(
        "ulRelativeOffset" / Int64ul,
        "lShift" / Int64sl,
        "ulSegmentStart" / Int64ul,
        "ulSegmentEnd" / Int64ul,
        "fClearCache" / Int8ul,
        "bstrText" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1906, version=0)
class Microsoft_Office_Word_1906_0(Etw):
    pattern = Struct(
        "segid" / Int32ul,
        "iseg" / Int32ul,
        "dcpRelative" / Int64ul,
        "dcpSegmentStart" / Int64ul,
        "dcpSegmentEnd" / Int64ul,
        "dcpShift" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1907, version=0)
class Microsoft_Office_Word_1907_0(Etw):
    pattern = Struct(
        "m_ptct" / WString,
        "m_sppts" / Int8ul,
        "m_spptsbstrText" / WString,
        "m_spptcc" / Int8ul,
        "m_spptccsegid" / Int32ul,
        "m_spptcciseg" / Int32ul,
        "m_spptccdcpRelative" / Int64ul,
        "m_spptccdcpSegmentStart" / Int64ul,
        "m_spptccdcpSegmentEnd" / Int64ul,
        "m_spptccdcpShift" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1908, version=0)
class Microsoft_Office_Word_1908_0(Etw):
    pattern = Struct(
        "iseg" / Int32ul,
        "spSegmentsegid" / Int32ul,
        "spSegmentiseg" / Int32ul,
        "spSegmentdcpRelative" / Int64ul,
        "spSegmentdcpSegmentStart" / Int64ul,
        "spSegmentdcpSegmentEnd" / Int64ul,
        "spSegmentdcpShift" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1909, version=0)
class Microsoft_Office_Word_1909_0(Etw):
    pattern = Struct(
        "iseg" / Int32ul,
        "m_vecsegmentSize" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1910, version=0)
class Microsoft_Office_Word_1910_0(Etw):
    pattern = Struct(
        "segid" / Int32ul,
        "iseg" / Int32ul,
        "dcpRelative" / Int64ul,
        "dcpSegmentStart" / Int64ul,
        "dcpSegmentEnd" / Int64ul,
        "dcpShift" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1911, version=0)
class Microsoft_Office_Word_1911_0(Etw):
    pattern = Struct(
        "iseg" / Int32ul,
        "spSegmentsegid" / Int32ul,
        "spSegmentiseg" / Int32ul,
        "spSegmentdcpRelative" / Int64ul,
        "spSegmentdcpSegmentStart" / Int64ul,
        "spSegmentdcpSegmentEnd" / Int64ul,
        "spSegmentdcpShift" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1912, version=0)
class Microsoft_Office_Word_1912_0(Etw):
    pattern = Struct(
        "iseg" / Int32ul,
        "m_vecsegmentSize" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1913, version=0)
class Microsoft_Office_Word_1913_0(Etw):
    pattern = Struct(
        "segid" / Int32ul,
        "iseg" / Int32ul,
        "dcpRelative" / Int64ul,
        "dcpSegmentStart" / Int64ul,
        "dcpSegmentEnd" / Int64ul,
        "dcpShift" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1914, version=0)
class Microsoft_Office_Word_1914_0(Etw):
    pattern = Struct(
        "iseg" / Int32ul,
        "spSegmentsegid" / Int32ul,
        "spSegmentiseg" / Int32ul,
        "spSegmentdcpRelative" / Int64ul,
        "spSegmentdcpSegmentStart" / Int64ul,
        "spSegmentdcpSegmentEnd" / Int64ul,
        "spSegmentdcpShift" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1915, version=0)
class Microsoft_Office_Word_1915_0(Etw):
    pattern = Struct(
        "segid" / Int32ul,
        "iseg" / Int32ul,
        "dcpRelative" / Int64ul,
        "dcpSegmentStart" / Int64ul,
        "dcpSegmentEnd" / Int64ul,
        "dcpShift" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1916, version=0)
class Microsoft_Office_Word_1916_0(Etw):
    pattern = Struct(
        "iseg" / Int32ul,
        "spSegmentsegid" / Int32ul,
        "spSegmentiseg" / Int32ul,
        "spSegmentdcpRelative" / Int64ul,
        "spSegmentdcpSegmentStart" / Int64ul,
        "spSegmentdcpSegmentEnd" / Int64ul,
        "spSegmentdcpShift" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1917, version=0)
class Microsoft_Office_Word_1917_0(Etw):
    pattern = Struct(
        "iseg" / Int32ul,
        "m_vecsegmentSize" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1918, version=0)
class Microsoft_Office_Word_1918_0(Etw):
    pattern = Struct(
        "segid" / Int32ul,
        "iseg" / Int32ul,
        "dcpRelative" / Int64ul,
        "dcpSegmentStart" / Int64ul,
        "dcpSegmentEnd" / Int64ul,
        "dcpShift" / Int64sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1919, version=0)
class Microsoft_Office_Word_1919_0(Etw):
    pattern = Struct(
        "iseg" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1920, version=0)
class Microsoft_Office_Word_1920_0(Etw):
    pattern = Struct(
        "iseg" / Int32ul,
        "m_vecsegmentSize" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1921, version=0)
class Microsoft_Office_Word_1921_0(Etw):
    pattern = Struct(
        "index" / Int32ul,
        "segid" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1922, version=0)
class Microsoft_Office_Word_1922_0(Etw):
    pattern = Struct(
        "iseg" / Int32ul,
        "spSegmentsegid" / Int32ul,
        "spSegmentiseg" / Int32ul,
        "spSegmentdcpRelative" / Int64ul,
        "spSegmentdcpSegmentStart" / Int64ul,
        "spSegmentdcpSegmentEnd" / Int64ul,
        "spSegmentdcpShift" / Int64sl,
        "dcpShift" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1923, version=0)
class Microsoft_Office_Word_1923_0(Etw):
    pattern = Struct(
        "ullBmkId" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1924, version=0)
class Microsoft_Office_Word_1924_0(Etw):
    pattern = Struct(
        "count" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1925, version=0)
class Microsoft_Office_Word_1925_0(Etw):
    pattern = Struct(
        "cpBmkStart" / Int32sl,
        "cpBmkEnd" / Int32sl,
        "ibkf" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1926, version=0)
class Microsoft_Office_Word_1926_0(Etw):
    pattern = Struct(
        "tempUullSegmentId" / Int64ul,
        "ullSegmentId" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1927, version=0)
class Microsoft_Office_Word_1927_0(Etw):
    pattern = Struct(
        "count" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1928, version=0)
class Microsoft_Office_Word_1928_0(Etw):
    pattern = Struct(
        "cpBmkStart" / Int32sl,
        "cpBmkEnd" / Int32sl,
        "ibkf" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1929, version=0)
class Microsoft_Office_Word_1929_0(Etw):
    pattern = Struct(
        "count" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1930, version=0)
class Microsoft_Office_Word_1930_0(Etw):
    pattern = Struct(
        "cpBmkStart" / Int32sl,
        "cpBmkEnd" / Int32sl,
        "ibkf" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1931, version=0)
class Microsoft_Office_Word_1931_0(Etw):
    pattern = Struct(
        "count" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1932, version=1)
class Microsoft_Office_Word_1932_1(Etw):
    pattern = Struct(
        "timeSpent" / Int64ul,
        "loopIterations" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1933, version=0)
class Microsoft_Office_Word_1933_0(Etw):
    pattern = Struct(
        "context" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=1934, version=0)
class Microsoft_Office_Word_1934_0(Etw):
    pattern = Struct(
        "context" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2000, version=1)
class Microsoft_Office_Word_2000_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2001, version=1)
class Microsoft_Office_Word_2001_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2002, version=1)
class Microsoft_Office_Word_2002_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2003, version=1)
class Microsoft_Office_Word_2003_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2004, version=1)
class Microsoft_Office_Word_2004_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2005, version=1)
class Microsoft_Office_Word_2005_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2006, version=1)
class Microsoft_Office_Word_2006_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2007, version=1)
class Microsoft_Office_Word_2007_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2008, version=1)
class Microsoft_Office_Word_2008_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2009, version=1)
class Microsoft_Office_Word_2009_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2010, version=1)
class Microsoft_Office_Word_2010_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2011, version=1)
class Microsoft_Office_Word_2011_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2012, version=1)
class Microsoft_Office_Word_2012_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2013, version=1)
class Microsoft_Office_Word_2013_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2014, version=1)
class Microsoft_Office_Word_2014_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2015, version=1)
class Microsoft_Office_Word_2015_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2016, version=1)
class Microsoft_Office_Word_2016_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2017, version=1)
class Microsoft_Office_Word_2017_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2018, version=1)
class Microsoft_Office_Word_2018_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2019, version=1)
class Microsoft_Office_Word_2019_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2020, version=1)
class Microsoft_Office_Word_2020_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2021, version=1)
class Microsoft_Office_Word_2021_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2022, version=1)
class Microsoft_Office_Word_2022_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2023, version=1)
class Microsoft_Office_Word_2023_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2024, version=1)
class Microsoft_Office_Word_2024_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2025, version=1)
class Microsoft_Office_Word_2025_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2026, version=1)
class Microsoft_Office_Word_2026_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2027, version=1)
class Microsoft_Office_Word_2027_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2028, version=1)
class Microsoft_Office_Word_2028_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2029, version=1)
class Microsoft_Office_Word_2029_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2030, version=1)
class Microsoft_Office_Word_2030_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2031, version=1)
class Microsoft_Office_Word_2031_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "Pdod" / Int64ul,
        "VoidPtr" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2032, version=0)
class Microsoft_Office_Word_2032_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2033, version=0)
class Microsoft_Office_Word_2033_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2034, version=0)
class Microsoft_Office_Word_2034_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2035, version=0)
class Microsoft_Office_Word_2035_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2036, version=0)
class Microsoft_Office_Word_2036_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2037, version=0)
class Microsoft_Office_Word_2037_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2038, version=0)
class Microsoft_Office_Word_2038_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2039, version=0)
class Microsoft_Office_Word_2039_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2040, version=0)
class Microsoft_Office_Word_2040_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2041, version=0)
class Microsoft_Office_Word_2041_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2042, version=0)
class Microsoft_Office_Word_2042_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2043, version=0)
class Microsoft_Office_Word_2043_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2044, version=0)
class Microsoft_Office_Word_2044_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2045, version=0)
class Microsoft_Office_Word_2045_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2046, version=0)
class Microsoft_Office_Word_2046_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2047, version=0)
class Microsoft_Office_Word_2047_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2048, version=0)
class Microsoft_Office_Word_2048_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2049, version=0)
class Microsoft_Office_Word_2049_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2050, version=0)
class Microsoft_Office_Word_2050_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2051, version=0)
class Microsoft_Office_Word_2051_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2052, version=0)
class Microsoft_Office_Word_2052_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2053, version=0)
class Microsoft_Office_Word_2053_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2054, version=0)
class Microsoft_Office_Word_2054_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2055, version=0)
class Microsoft_Office_Word_2055_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2056, version=0)
class Microsoft_Office_Word_2056_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2057, version=0)
class Microsoft_Office_Word_2057_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2058, version=0)
class Microsoft_Office_Word_2058_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2059, version=0)
class Microsoft_Office_Word_2059_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2060, version=0)
class Microsoft_Office_Word_2060_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2061, version=0)
class Microsoft_Office_Word_2061_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2062, version=0)
class Microsoft_Office_Word_2062_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2063, version=0)
class Microsoft_Office_Word_2063_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2064, version=0)
class Microsoft_Office_Word_2064_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2065, version=0)
class Microsoft_Office_Word_2065_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2066, version=0)
class Microsoft_Office_Word_2066_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2067, version=0)
class Microsoft_Office_Word_2067_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2068, version=0)
class Microsoft_Office_Word_2068_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2069, version=0)
class Microsoft_Office_Word_2069_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2070, version=0)
class Microsoft_Office_Word_2070_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2071, version=0)
class Microsoft_Office_Word_2071_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2072, version=0)
class Microsoft_Office_Word_2072_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2073, version=0)
class Microsoft_Office_Word_2073_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2074, version=0)
class Microsoft_Office_Word_2074_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2075, version=0)
class Microsoft_Office_Word_2075_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2076, version=0)
class Microsoft_Office_Word_2076_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2077, version=0)
class Microsoft_Office_Word_2077_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2078, version=0)
class Microsoft_Office_Word_2078_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2079, version=0)
class Microsoft_Office_Word_2079_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2080, version=0)
class Microsoft_Office_Word_2080_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2081, version=0)
class Microsoft_Office_Word_2081_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2082, version=0)
class Microsoft_Office_Word_2082_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2083, version=0)
class Microsoft_Office_Word_2083_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2084, version=0)
class Microsoft_Office_Word_2084_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2085, version=0)
class Microsoft_Office_Word_2085_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2086, version=0)
class Microsoft_Office_Word_2086_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2087, version=0)
class Microsoft_Office_Word_2087_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2088, version=0)
class Microsoft_Office_Word_2088_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2089, version=0)
class Microsoft_Office_Word_2089_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2090, version=0)
class Microsoft_Office_Word_2090_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2091, version=0)
class Microsoft_Office_Word_2091_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2092, version=0)
class Microsoft_Office_Word_2092_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2093, version=0)
class Microsoft_Office_Word_2093_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2094, version=0)
class Microsoft_Office_Word_2094_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2095, version=0)
class Microsoft_Office_Word_2095_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2501, version=0)
class Microsoft_Office_Word_2501_0(Etw):
    pattern = Struct(
        "ReRegisterSucceeded" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=2502, version=0)
class Microsoft_Office_Word_2502_0(Etw):
    pattern = Struct(
        "NumDocs" / Int32sl,
        "VirtualdesktopGUID" / WString,
        "Instance" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=3500, version=1)
class Microsoft_Office_Word_3500_1(Etw):
    pattern = Struct(
        "pidim" / Int64ul,
        "fMother" / Int8ul,
        "docParidsStateOpen" / Int32ul,
        "docParidsStateEnsureParids" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=3501, version=0)
class Microsoft_Office_Word_3501_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "pcaso" / Int64ul,
        "pcoa" / Int64ul,
        "fIsInCsiTransactedStreamMode" / Int8ul,
        "fIsSaveAs" / Int8ul,
        "fSourceIsServer" / Int8ul,
        "fTargetIsServer" / Int8ul,
        "fListenerRegistrationFailed" / Int8ul,
        "fDocumentContentWasNull" / Int8ul,
        "persisterTypeReplaced" / Int32ul,
        "persisterTypeConstructed" / Int32ul,
        "dwTagCaller" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=3502, version=0)
class Microsoft_Office_Word_3502_0(Etw):
    pattern = Struct(
        "Lid" / Int16ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=3503, version=0)
class Microsoft_Office_Word_3503_0(Etw):
    pattern = Struct(
        "ETW_TrackbackTag" / Int32ul,
        "pioldoc" / Int64ul,
        "previousSupportedLocations" / Int32ul,
        "newSupportedLocations" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=3504, version=0)
class Microsoft_Office_Word_3504_0(Etw):
    pattern = Struct(
        "fOnMainThread" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=3505, version=0)
class Microsoft_Office_Word_3505_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "pmwd" / Int64ul,
        "ac" / Int32sl,
        "fAutosaveActiveAfterFailure" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=3506, version=0)
class Microsoft_Office_Word_3506_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "csierrOnRetry" / Int32ul,
        "fOnFreeRunningThread" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=3507, version=0)
class Microsoft_Office_Word_3507_0(Etw):
    pattern = Struct(
        "dwtag" / Int32ul,
        "dwtagLast" / Int32ul,
        "dullDirtyToolbarsMs" / Int64ul,
        "fToolbarsDirty" / Int8ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=3508, version=0)
class Microsoft_Office_Word_3508_0(Etw):
    pattern = Struct(
        "JsonData" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=3509, version=0)
class Microsoft_Office_Word_3509_0(Etw):
    pattern = Struct(
        "ETW_TrackbackTag" / Int32ul,
        "pioldoc" / Int64ul,
        "previousDisableTempFileLocations" / Int32ul,
        "newDisableTempFileLocations" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=3550, version=0)
class Microsoft_Office_Word_3550_0(Etw):
    pattern = Struct(
        "cIntelligentPlaceholders" / Int64ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=3551, version=0)
class Microsoft_Office_Word_3551_0(Etw):
    pattern = Struct(
        "EntryPoint" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=3552, version=0)
class Microsoft_Office_Word_3552_0(Etw):
    pattern = Struct(
        "EntryPoint" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=3553, version=4)
class Microsoft_Office_Word_3553_4(Etw):
    pattern = Struct(
        "cpMac" / Int32sl,
        "cIntelligentPlaceholders" / Int64ul,
        "cDeletedIntelligentPlaceholders" / Int64ul,
        "cHitsForEsc" / Int32ul,
        "cHitsForReturn" / Int32ul,
        "cHitsForTab" / Int32ul,
        "cBucket_0_10s" / Int32ul,
        "cBucket_10_30s" / Int32ul,
        "cBucket_30_60s" / Int32ul,
        "cBucket_60_300s" / Int32ul,
        "cBucket_300_1800s" / Int32ul,
        "cBucket_1800_MAXs" / Int32ul,
        "cSavedToFile" / Int32ul,
        "cSavedToFileFromNewInsert" / Int32ul,
        "cSavedToFileFromEditOp" / Int32ul,
        "cAtmBucket_0_Atms" / Int32ul,
        "cAtmBucket_1_Atms" / Int32ul,
        "cAtmBucket_2_Atms" / Int32ul,
        "cAtmBucket_3_Atms" / Int32ul,
        "cAtmBucket_3Plus_Atms" / Int32ul,
        "cPlaceholdersWithAtm" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=3554, version=0)
class Microsoft_Office_Word_3554_0(Etw):
    pattern = Struct(
        "eventId" / Int32ul,
        "pmwd" / Int64ul,
        "placeholderCount" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=3555, version=0)
class Microsoft_Office_Word_3555_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "dcp" / Int32sl
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=3556, version=0)
class Microsoft_Office_Word_3556_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "gesture" / WString,
        "cSeenPicker" / Int32ul,
        "cSelectedPicker" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=4001, version=0)
class Microsoft_Office_Word_4001_0(Etw):
    pattern = Struct(
        "TrackbackTag" / Int32ul
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30003, version=1)
class Microsoft_Office_Word_30003_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30004, version=1)
class Microsoft_Office_Word_30004_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30005, version=1)
class Microsoft_Office_Word_30005_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30006, version=1)
class Microsoft_Office_Word_30006_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30007, version=1)
class Microsoft_Office_Word_30007_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30008, version=1)
class Microsoft_Office_Word_30008_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30009, version=1)
class Microsoft_Office_Word_30009_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30010, version=1)
class Microsoft_Office_Word_30010_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30011, version=1)
class Microsoft_Office_Word_30011_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30012, version=1)
class Microsoft_Office_Word_30012_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30013, version=1)
class Microsoft_Office_Word_30013_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30014, version=1)
class Microsoft_Office_Word_30014_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30015, version=1)
class Microsoft_Office_Word_30015_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30016, version=1)
class Microsoft_Office_Word_30016_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30017, version=1)
class Microsoft_Office_Word_30017_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30018, version=1)
class Microsoft_Office_Word_30018_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30019, version=1)
class Microsoft_Office_Word_30019_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30020, version=1)
class Microsoft_Office_Word_30020_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30021, version=1)
class Microsoft_Office_Word_30021_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30022, version=1)
class Microsoft_Office_Word_30022_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30023, version=1)
class Microsoft_Office_Word_30023_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30024, version=1)
class Microsoft_Office_Word_30024_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30025, version=1)
class Microsoft_Office_Word_30025_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30026, version=1)
class Microsoft_Office_Word_30026_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30027, version=1)
class Microsoft_Office_Word_30027_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30028, version=1)
class Microsoft_Office_Word_30028_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30029, version=1)
class Microsoft_Office_Word_30029_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30030, version=1)
class Microsoft_Office_Word_30030_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30031, version=1)
class Microsoft_Office_Word_30031_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30032, version=1)
class Microsoft_Office_Word_30032_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30033, version=1)
class Microsoft_Office_Word_30033_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30034, version=1)
class Microsoft_Office_Word_30034_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30035, version=1)
class Microsoft_Office_Word_30035_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30036, version=1)
class Microsoft_Office_Word_30036_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30037, version=1)
class Microsoft_Office_Word_30037_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30038, version=1)
class Microsoft_Office_Word_30038_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30039, version=1)
class Microsoft_Office_Word_30039_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30040, version=1)
class Microsoft_Office_Word_30040_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30041, version=1)
class Microsoft_Office_Word_30041_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30042, version=1)
class Microsoft_Office_Word_30042_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30043, version=1)
class Microsoft_Office_Word_30043_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30044, version=1)
class Microsoft_Office_Word_30044_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30045, version=1)
class Microsoft_Office_Word_30045_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30046, version=1)
class Microsoft_Office_Word_30046_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30047, version=1)
class Microsoft_Office_Word_30047_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30048, version=1)
class Microsoft_Office_Word_30048_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30049, version=1)
class Microsoft_Office_Word_30049_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30050, version=1)
class Microsoft_Office_Word_30050_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30051, version=1)
class Microsoft_Office_Word_30051_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30052, version=1)
class Microsoft_Office_Word_30052_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30053, version=1)
class Microsoft_Office_Word_30053_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30054, version=1)
class Microsoft_Office_Word_30054_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30055, version=1)
class Microsoft_Office_Word_30055_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30056, version=1)
class Microsoft_Office_Word_30056_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30057, version=1)
class Microsoft_Office_Word_30057_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30058, version=1)
class Microsoft_Office_Word_30058_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30059, version=1)
class Microsoft_Office_Word_30059_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30060, version=1)
class Microsoft_Office_Word_30060_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30061, version=1)
class Microsoft_Office_Word_30061_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30062, version=1)
class Microsoft_Office_Word_30062_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30063, version=1)
class Microsoft_Office_Word_30063_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30064, version=1)
class Microsoft_Office_Word_30064_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30065, version=1)
class Microsoft_Office_Word_30065_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30066, version=1)
class Microsoft_Office_Word_30066_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30067, version=1)
class Microsoft_Office_Word_30067_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30068, version=1)
class Microsoft_Office_Word_30068_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30069, version=1)
class Microsoft_Office_Word_30069_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30070, version=1)
class Microsoft_Office_Word_30070_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30071, version=1)
class Microsoft_Office_Word_30071_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30072, version=1)
class Microsoft_Office_Word_30072_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30073, version=1)
class Microsoft_Office_Word_30073_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30074, version=1)
class Microsoft_Office_Word_30074_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30075, version=1)
class Microsoft_Office_Word_30075_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30076, version=1)
class Microsoft_Office_Word_30076_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30077, version=1)
class Microsoft_Office_Word_30077_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30078, version=1)
class Microsoft_Office_Word_30078_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30079, version=1)
class Microsoft_Office_Word_30079_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30080, version=1)
class Microsoft_Office_Word_30080_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30081, version=1)
class Microsoft_Office_Word_30081_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30082, version=1)
class Microsoft_Office_Word_30082_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30083, version=1)
class Microsoft_Office_Word_30083_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30084, version=1)
class Microsoft_Office_Word_30084_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30085, version=1)
class Microsoft_Office_Word_30085_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30086, version=1)
class Microsoft_Office_Word_30086_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30087, version=1)
class Microsoft_Office_Word_30087_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30088, version=1)
class Microsoft_Office_Word_30088_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30089, version=1)
class Microsoft_Office_Word_30089_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30090, version=1)
class Microsoft_Office_Word_30090_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30091, version=1)
class Microsoft_Office_Word_30091_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30092, version=1)
class Microsoft_Office_Word_30092_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30093, version=1)
class Microsoft_Office_Word_30093_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30094, version=1)
class Microsoft_Office_Word_30094_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30095, version=1)
class Microsoft_Office_Word_30095_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30096, version=1)
class Microsoft_Office_Word_30096_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30097, version=1)
class Microsoft_Office_Word_30097_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30098, version=1)
class Microsoft_Office_Word_30098_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30099, version=1)
class Microsoft_Office_Word_30099_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30100, version=1)
class Microsoft_Office_Word_30100_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30101, version=1)
class Microsoft_Office_Word_30101_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30102, version=1)
class Microsoft_Office_Word_30102_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30103, version=1)
class Microsoft_Office_Word_30103_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30104, version=1)
class Microsoft_Office_Word_30104_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30105, version=1)
class Microsoft_Office_Word_30105_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30106, version=1)
class Microsoft_Office_Word_30106_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30107, version=1)
class Microsoft_Office_Word_30107_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30108, version=1)
class Microsoft_Office_Word_30108_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30109, version=1)
class Microsoft_Office_Word_30109_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30110, version=1)
class Microsoft_Office_Word_30110_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30111, version=1)
class Microsoft_Office_Word_30111_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30112, version=1)
class Microsoft_Office_Word_30112_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30113, version=1)
class Microsoft_Office_Word_30113_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30114, version=1)
class Microsoft_Office_Word_30114_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30115, version=1)
class Microsoft_Office_Word_30115_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30116, version=1)
class Microsoft_Office_Word_30116_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30117, version=1)
class Microsoft_Office_Word_30117_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30118, version=1)
class Microsoft_Office_Word_30118_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30119, version=1)
class Microsoft_Office_Word_30119_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30120, version=1)
class Microsoft_Office_Word_30120_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30121, version=1)
class Microsoft_Office_Word_30121_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30122, version=1)
class Microsoft_Office_Word_30122_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30123, version=1)
class Microsoft_Office_Word_30123_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30124, version=1)
class Microsoft_Office_Word_30124_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30125, version=1)
class Microsoft_Office_Word_30125_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30126, version=1)
class Microsoft_Office_Word_30126_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30127, version=1)
class Microsoft_Office_Word_30127_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30128, version=1)
class Microsoft_Office_Word_30128_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30129, version=1)
class Microsoft_Office_Word_30129_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30130, version=1)
class Microsoft_Office_Word_30130_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30131, version=1)
class Microsoft_Office_Word_30131_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30132, version=1)
class Microsoft_Office_Word_30132_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30133, version=1)
class Microsoft_Office_Word_30133_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30134, version=1)
class Microsoft_Office_Word_30134_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30135, version=1)
class Microsoft_Office_Word_30135_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30136, version=1)
class Microsoft_Office_Word_30136_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30137, version=1)
class Microsoft_Office_Word_30137_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30138, version=1)
class Microsoft_Office_Word_30138_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30139, version=1)
class Microsoft_Office_Word_30139_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30140, version=1)
class Microsoft_Office_Word_30140_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30141, version=1)
class Microsoft_Office_Word_30141_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30142, version=1)
class Microsoft_Office_Word_30142_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30143, version=1)
class Microsoft_Office_Word_30143_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30144, version=1)
class Microsoft_Office_Word_30144_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30145, version=1)
class Microsoft_Office_Word_30145_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30146, version=1)
class Microsoft_Office_Word_30146_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30147, version=1)
class Microsoft_Office_Word_30147_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30148, version=1)
class Microsoft_Office_Word_30148_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30149, version=1)
class Microsoft_Office_Word_30149_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30150, version=1)
class Microsoft_Office_Word_30150_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30151, version=1)
class Microsoft_Office_Word_30151_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30152, version=1)
class Microsoft_Office_Word_30152_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30153, version=1)
class Microsoft_Office_Word_30153_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30154, version=1)
class Microsoft_Office_Word_30154_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30155, version=1)
class Microsoft_Office_Word_30155_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30156, version=1)
class Microsoft_Office_Word_30156_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30157, version=1)
class Microsoft_Office_Word_30157_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30158, version=1)
class Microsoft_Office_Word_30158_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30159, version=1)
class Microsoft_Office_Word_30159_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30160, version=1)
class Microsoft_Office_Word_30160_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30161, version=1)
class Microsoft_Office_Word_30161_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30162, version=1)
class Microsoft_Office_Word_30162_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30163, version=1)
class Microsoft_Office_Word_30163_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30164, version=1)
class Microsoft_Office_Word_30164_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30165, version=1)
class Microsoft_Office_Word_30165_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30166, version=1)
class Microsoft_Office_Word_30166_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30167, version=1)
class Microsoft_Office_Word_30167_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30168, version=1)
class Microsoft_Office_Word_30168_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30169, version=1)
class Microsoft_Office_Word_30169_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30170, version=1)
class Microsoft_Office_Word_30170_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30171, version=1)
class Microsoft_Office_Word_30171_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30172, version=1)
class Microsoft_Office_Word_30172_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30173, version=1)
class Microsoft_Office_Word_30173_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30174, version=1)
class Microsoft_Office_Word_30174_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30175, version=1)
class Microsoft_Office_Word_30175_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30176, version=1)
class Microsoft_Office_Word_30176_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30177, version=1)
class Microsoft_Office_Word_30177_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30178, version=1)
class Microsoft_Office_Word_30178_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30179, version=1)
class Microsoft_Office_Word_30179_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30180, version=1)
class Microsoft_Office_Word_30180_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30181, version=1)
class Microsoft_Office_Word_30181_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30182, version=1)
class Microsoft_Office_Word_30182_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30183, version=1)
class Microsoft_Office_Word_30183_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30184, version=1)
class Microsoft_Office_Word_30184_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30185, version=1)
class Microsoft_Office_Word_30185_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30186, version=1)
class Microsoft_Office_Word_30186_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30187, version=1)
class Microsoft_Office_Word_30187_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30188, version=1)
class Microsoft_Office_Word_30188_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30189, version=1)
class Microsoft_Office_Word_30189_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30190, version=1)
class Microsoft_Office_Word_30190_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30191, version=1)
class Microsoft_Office_Word_30191_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30192, version=1)
class Microsoft_Office_Word_30192_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30193, version=1)
class Microsoft_Office_Word_30193_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30194, version=1)
class Microsoft_Office_Word_30194_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30195, version=1)
class Microsoft_Office_Word_30195_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30196, version=1)
class Microsoft_Office_Word_30196_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30197, version=1)
class Microsoft_Office_Word_30197_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30198, version=1)
class Microsoft_Office_Word_30198_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30199, version=1)
class Microsoft_Office_Word_30199_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30200, version=1)
class Microsoft_Office_Word_30200_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30201, version=1)
class Microsoft_Office_Word_30201_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30202, version=1)
class Microsoft_Office_Word_30202_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30203, version=1)
class Microsoft_Office_Word_30203_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30204, version=1)
class Microsoft_Office_Word_30204_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30205, version=1)
class Microsoft_Office_Word_30205_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30206, version=1)
class Microsoft_Office_Word_30206_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30207, version=1)
class Microsoft_Office_Word_30207_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30208, version=1)
class Microsoft_Office_Word_30208_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30209, version=1)
class Microsoft_Office_Word_30209_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30210, version=1)
class Microsoft_Office_Word_30210_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30211, version=1)
class Microsoft_Office_Word_30211_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30212, version=1)
class Microsoft_Office_Word_30212_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30213, version=1)
class Microsoft_Office_Word_30213_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30214, version=1)
class Microsoft_Office_Word_30214_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30215, version=1)
class Microsoft_Office_Word_30215_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30216, version=1)
class Microsoft_Office_Word_30216_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30217, version=1)
class Microsoft_Office_Word_30217_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30218, version=1)
class Microsoft_Office_Word_30218_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30219, version=1)
class Microsoft_Office_Word_30219_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30220, version=1)
class Microsoft_Office_Word_30220_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30221, version=1)
class Microsoft_Office_Word_30221_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30222, version=1)
class Microsoft_Office_Word_30222_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30223, version=1)
class Microsoft_Office_Word_30223_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30224, version=1)
class Microsoft_Office_Word_30224_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30225, version=1)
class Microsoft_Office_Word_30225_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30226, version=1)
class Microsoft_Office_Word_30226_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30227, version=1)
class Microsoft_Office_Word_30227_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30228, version=1)
class Microsoft_Office_Word_30228_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30229, version=1)
class Microsoft_Office_Word_30229_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30230, version=1)
class Microsoft_Office_Word_30230_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30231, version=1)
class Microsoft_Office_Word_30231_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30232, version=1)
class Microsoft_Office_Word_30232_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30233, version=1)
class Microsoft_Office_Word_30233_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30234, version=1)
class Microsoft_Office_Word_30234_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30235, version=1)
class Microsoft_Office_Word_30235_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30236, version=1)
class Microsoft_Office_Word_30236_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30237, version=1)
class Microsoft_Office_Word_30237_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30238, version=1)
class Microsoft_Office_Word_30238_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30239, version=1)
class Microsoft_Office_Word_30239_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30240, version=1)
class Microsoft_Office_Word_30240_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30241, version=1)
class Microsoft_Office_Word_30241_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30242, version=1)
class Microsoft_Office_Word_30242_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30243, version=1)
class Microsoft_Office_Word_30243_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30244, version=1)
class Microsoft_Office_Word_30244_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30245, version=1)
class Microsoft_Office_Word_30245_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30246, version=1)
class Microsoft_Office_Word_30246_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30247, version=1)
class Microsoft_Office_Word_30247_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30248, version=1)
class Microsoft_Office_Word_30248_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30249, version=1)
class Microsoft_Office_Word_30249_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30250, version=1)
class Microsoft_Office_Word_30250_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30251, version=1)
class Microsoft_Office_Word_30251_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30252, version=1)
class Microsoft_Office_Word_30252_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30253, version=1)
class Microsoft_Office_Word_30253_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30254, version=1)
class Microsoft_Office_Word_30254_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30255, version=1)
class Microsoft_Office_Word_30255_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30256, version=1)
class Microsoft_Office_Word_30256_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30257, version=1)
class Microsoft_Office_Word_30257_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30258, version=1)
class Microsoft_Office_Word_30258_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30259, version=1)
class Microsoft_Office_Word_30259_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30260, version=1)
class Microsoft_Office_Word_30260_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30261, version=1)
class Microsoft_Office_Word_30261_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30262, version=1)
class Microsoft_Office_Word_30262_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30263, version=1)
class Microsoft_Office_Word_30263_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30264, version=1)
class Microsoft_Office_Word_30264_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30265, version=1)
class Microsoft_Office_Word_30265_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30266, version=1)
class Microsoft_Office_Word_30266_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30267, version=1)
class Microsoft_Office_Word_30267_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30268, version=1)
class Microsoft_Office_Word_30268_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30269, version=1)
class Microsoft_Office_Word_30269_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30270, version=1)
class Microsoft_Office_Word_30270_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30271, version=1)
class Microsoft_Office_Word_30271_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30272, version=1)
class Microsoft_Office_Word_30272_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30273, version=1)
class Microsoft_Office_Word_30273_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30274, version=1)
class Microsoft_Office_Word_30274_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30275, version=1)
class Microsoft_Office_Word_30275_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30276, version=1)
class Microsoft_Office_Word_30276_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30277, version=1)
class Microsoft_Office_Word_30277_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30278, version=1)
class Microsoft_Office_Word_30278_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30279, version=1)
class Microsoft_Office_Word_30279_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30280, version=1)
class Microsoft_Office_Word_30280_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30281, version=1)
class Microsoft_Office_Word_30281_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30282, version=1)
class Microsoft_Office_Word_30282_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30283, version=1)
class Microsoft_Office_Word_30283_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30284, version=1)
class Microsoft_Office_Word_30284_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30285, version=1)
class Microsoft_Office_Word_30285_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30286, version=1)
class Microsoft_Office_Word_30286_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30287, version=1)
class Microsoft_Office_Word_30287_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30288, version=1)
class Microsoft_Office_Word_30288_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30289, version=1)
class Microsoft_Office_Word_30289_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("daf0b914-9c1c-450a-81b2-fea7244f6ffa"), event_id=30290, version=1)
class Microsoft_Office_Word_30290_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )

