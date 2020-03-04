# -*- coding: utf-8 -*-
"""
Microsoft-Office-Word2
GUID : bb00e856-a12f-4ab7-b2c8-4e80caea5b07
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30, version=2)
class Microsoft_Office_Word2_30_2(Etw):
    pattern = Struct(
        "sel" / WString,
        "pdod" / Int64ul,
        "DocKind" / WString,
        "pwwd" / Int64ul,
        "ViewType" / WString,
        "OldSelectionKind" / WString,
        "OldcpFirst" / Int32sl,
        "OldcpLim" / Int32sl,
        "OldfDiscontiguous" / Int8ul,
        "IntendedcpFirst" / Int32sl,
        "IntendedcpLim" / Int32sl,
        "grfsel" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=31, version=1)
class Microsoft_Office_Word2_31_1(Etw):
    pattern = Struct(
        "NewSelectionKind" / WString,
        "NewcpFirst" / Int32sl,
        "NewcpLim" / Int32sl,
        "NewfDiscontiguous" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=32, version=1)
class Microsoft_Office_Word2_32_1(Etw):
    pattern = Struct(
        "Type" / WString,
        "fInOptimizedPass" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=33, version=1)
class Microsoft_Office_Word2_33_1(Etw):
    pattern = Struct(
        "Type" / WString,
        "fInOptimizedPass" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=34, version=0)
class Microsoft_Office_Word2_34_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "cpFirst" / Int32sl,
        "cpLim" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=38, version=1)
class Microsoft_Office_Word2_38_1(Etw):
    pattern = Struct(
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=39, version=1)
class Microsoft_Office_Word2_39_1(Etw):
    pattern = Struct(
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=42, version=1)
class Microsoft_Office_Word2_42_1(Etw):
    pattern = Struct(
        "sel" / WString,
        "cpFirst" / Int32sl,
        "cpLim" / Int32sl,
        "rcwxp" / Int32sl,
        "rcwyp" / Int32sl,
        "rcwdxp" / Int32sl,
        "rcwdyp" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=43, version=2)
class Microsoft_Office_Word2_43_2(Etw):
    pattern = Struct(
        "sel" / WString,
        "Oldpdod" / Int64ul,
        "Newpdod" / Int64ul,
        "pwwd" / Int64ul,
        "ViewType" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=44, version=2)
class Microsoft_Office_Word2_44_2(Etw):
    pattern = Struct(
        "sel" / WString,
        "SelectionKind" / WString,
        "pdod" / Int64ul,
        "DocKind" / WString,
        "pwwd" / Int64ul,
        "ViewType" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=46, version=0)
class Microsoft_Office_Word2_46_0(Etw):
    pattern = Struct(
        "DRcpFirst" / Int32sl,
        "DRcpLim" / Int32sl,
        "OriginalxwLeft" / Int32sl,
        "OriginalxwRight" / Int32sl,
        "OriginalywTop" / Int32sl,
        "OriginalywBottom" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=47, version=0)
class Microsoft_Office_Word2_47_0(Etw):
    pattern = Struct(
        "UpdatedxwLeft" / Int32sl,
        "UpdatedxwRight" / Int32sl,
        "UpdatedywTop" / Int32sl,
        "UpdatedywBottom" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=49, version=2)
class Microsoft_Office_Word2_49_2(Etw):
    pattern = Struct(
        "CmdName" / WString,
        "FCI" / Int32ul,
        "TCID" / Int32ul,
        "grfcco" / Int64ul,
        "grfaux" / Int64ul,
        "kcm" / Int32ul,
        "kcm2" / Int32ul,
        "Chained" / Int8ul,
        "MacroActive" / Int8ul,
        "LivePreview" / Int8ul,
        "Origpdod" / Int64ul,
        "OrigDocKind" / WString,
        "Origpmwd" / Int64ul,
        "Origwwd" / Int64ul,
        "OrigViewType" / WString,
        "SELpdod" / Int64ul,
        "SELDocKind" / WString,
        "SELcpFirst" / Int32sl,
        "SELcpLim" / Int32sl,
        "SELpmwd" / Int64ul,
        "SELwwd" / Int64ul,
        "SELViewType" / WString,
        "OriginalpdodMain" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=50, version=0)
class Microsoft_Office_Word2_50_0(Etw):
    pattern = Struct(
        "CmdName" / WString,
        "CmdReturn" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=51, version=0)
class Microsoft_Office_Word2_51_0(Etw):
    pattern = Struct(
        "DlgType" / WString,
        "DlgID" / Int64ul,
        "CmdName" / WString,
        "FCI" / Int32ul,
        "TCID" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=52, version=0)
class Microsoft_Office_Word2_52_0(Etw):
    pattern = Struct(
        "DlgType" / WString,
        "DlgID" / Int64ul,
        "CmdName" / WString,
        "CmdReturn" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=53, version=0)
class Microsoft_Office_Word2_53_0(Etw):
    pattern = Struct(
        "LayoutType" / WString,
        "xScroll" / Int32sl,
        "yScroll" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=55, version=0)
class Microsoft_Office_Word2_55_0(Etw):
    pattern = Struct(
        "xScroll" / Int32sl,
        "yScroll" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=56, version=0)
class Microsoft_Office_Word2_56_0(Etw):
    pattern = Struct(
        "xScroll" / Int32sl,
        "yScroll" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=57, version=2)
class Microsoft_Office_Word2_57_2(Etw):
    pattern = Struct(
        "pdodMain" / Int64ul,
        "Wwd" / WString,
        "PctZoom" / Double
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=58, version=0)
class Microsoft_Office_Word2_58_0(Etw):
    pattern = Struct(
        "Naturalstoppage" / Int32sl,
        "xNaturalstoppoint" / Int32sl,
        "m_xeDmBegin" / Int32sl,
        "xeMid" / Int32sl,
        "Viewportleft" / Int32sl,
        "Viewportright" / Int32sl,
        "Correctedpage" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=59, version=0)
class Microsoft_Office_Word2_59_0(Etw):
    pattern = Struct(
        "dxpInertiaStrength" / Int32sl,
        "xNaturalstoppoint" / Int32sl,
        "CurrentxPos" / Int32sl,
        "Snappoint" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=60, version=0)
class Microsoft_Office_Word2_60_0(Etw):
    pattern = Struct(
        "dxpInertiaStrength" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=63, version=1)
class Microsoft_Office_Word2_63_1(Etw):
    pattern = Struct(
        "xScrollerContext" / Int32sl,
        "yScrollerContext" / Int32sl,
        "dxMoved" / Int32sl,
        "dyMoved" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=65, version=0)
class Microsoft_Office_Word2_65_0(Etw):
    pattern = Struct(
        "Currentpoint" / Int32sl,
        "LeftBounds" / Int32sl,
        "RightBounds" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=66, version=0)
class Microsoft_Office_Word2_66_0(Etw):
    pattern = Struct(
        "Correctionpoint" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=126, version=1)
class Microsoft_Office_Word2_126_1(Etw):
    pattern = Struct(
        "ETW_TrackbackTag" / Int32ul,
        "CmdName" / WString,
        "FCI" / Int32ul,
        "TCID" / Int32ul,
        "grfcco" / Int64ul,
        "grfaux" / Int64ul,
        "kcm" / Int32ul,
        "kcm2" / Int32ul,
        "FromKeyboard" / Int8ul,
        "Chained" / Int8ul,
        "Enabled" / Int8ul,
        "grfoff1" / Int64ul,
        "grfoff2" / Int64ul,
        "grfoff3" / Int64ul,
        "grfon1" / Int64ul,
        "grfon2" / Int64ul,
        "grfon3" / Int64ul,
        "CmdReturn" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=127, version=1)
class Microsoft_Office_Word2_127_1(Etw):
    pattern = Struct(
        "Dirtycallsbeforeupdate" / Int32sl,
        "pdod" / Int64ul,
        "pwwd" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=128, version=1)
class Microsoft_Office_Word2_128_1(Etw):
    pattern = Struct(
        "Updatesalreadyinprogress" / Int32sl,
        "pdod" / Int64ul,
        "pwwd" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=129, version=1)
class Microsoft_Office_Word2_129_1(Etw):
    pattern = Struct(
        "Dirtycallsduringupdate" / Int32sl,
        "Updatesscheduledduringupdate" / Int32sl,
        "Updatesstillinprogress" / Int32sl,
        "pdod" / Int64ul,
        "pwwd" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=138, version=0)
class Microsoft_Office_Word2_138_0(Etw):
    pattern = Struct(
        "idTag" / WString,
        "depth" / Int32sl,
        "cursorSaverOn" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=139, version=0)
class Microsoft_Office_Word2_139_0(Etw):
    pattern = Struct(
        "idTag" / WString,
        "fAll" / Int8ul,
        "depth" / Int32sl,
        "cursorSaverOn" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=140, version=0)
class Microsoft_Office_Word2_140_0(Etw):
    pattern = Struct(
        "UserAction" / Int32sl,
        "fViewportMovesRight" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=141, version=0)
class Microsoft_Office_Word2_141_0(Etw):
    pattern = Struct(
        "fViewportMovesRight" / Int8ul,
        "cPagesMoved" / Int32sl,
        "cPagesInViewport" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=146, version=0)
class Microsoft_Office_Word2_146_0(Etw):
    pattern = Struct(
        "Offset" / Int32sl,
        "Interval" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=147, version=0)
class Microsoft_Office_Word2_147_0(Etw):
    pattern = Struct(
        "Point1" / Int32sl,
        "Point2" / Int32sl,
        "Point3" / Int32sl,
        "Point4" / Int32sl,
        "Point5" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=160, version=1)
class Microsoft_Office_Word2_160_1(Etw):
    pattern = Struct(
        "E1oinfo" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=161, version=0)
class Microsoft_Office_Word2_161_0(Etw):
    pattern = Struct(
        "E1oinfo" / Int32ul,
        "pdod" / Int64ul,
        "DocKind" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=170, version=1)
class Microsoft_Office_Word2_170_1(Etw):
    pattern = Struct(
        "pwwd" / Int64ul,
        "SquarePixelsofMissingPage" / Int32sl,
        "SquarePixelsofMissingDRcontent" / Int32sl,
        "SquarePixelsofViewport" / Int32sl,
        "SquarePixelsScrolled" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=171, version=0)
class Microsoft_Office_Word2_171_0(Etw):
    pattern = Struct(
        "StartTimemsec" / Int64ul,
        "EndTimemsec" / Int64ul,
        "Durationmsec" / Int64ul,
        "SliverCountpixelheightorwidth1" / Int32ul,
        "TotalCount" / Int32ul,
        "Thresholdtimemsec" / Int64ul,
        "Thresholdcount" / Int32ul,
        "DxwMax" / Int32ul,
        "DywMax" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=176, version=0)
class Microsoft_Office_Word2_176_0(Etw):
    pattern = Struct(
        "PtlType" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=177, version=0)
class Microsoft_Office_Word2_177_0(Etw):
    pattern = Struct(
        "PtlType" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=180, version=1)
class Microsoft_Office_Word2_180_1(Etw):
    pattern = Struct(
        "IsNextError" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=181, version=1)
class Microsoft_Office_Word2_181_1(Etw):
    pattern = Struct(
        "IsNextError" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=182, version=0)
class Microsoft_Office_Word2_182_0(Etw):
    pattern = Struct(
        "cComments" / Int32sl,
        "cReplies" / Int32sl,
        "cArtObjs" / Int32sl,
        "cFieldChars" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=183, version=1)
class Microsoft_Office_Word2_183_1(Etw):
    pattern = Struct(
        "cParents" / Int32ul,
        "cReplies" / Int32ul,
        "cInkComments" / Int32ul,
        "cCommentsWithTables" / Int32ul,
        "cSmartArt" / Int32ul,
        "cVideos" / Int32ul,
        "cPictures" / Int32ul,
        "cCharts" / Int32ul,
        "cOtherE2Os" / Int32ul,
        "cFields" / Int32ul,
        "cOLEObjects" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=186, version=0)
class Microsoft_Office_Word2_186_0(Etw):
    pattern = Struct(
        "reason" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=188, version=0)
class Microsoft_Office_Word2_188_0(Etw):
    pattern = Struct(
        "ptX" / Int32sl,
        "ptY" / Int32sl,
        "updateCnt" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=189, version=0)
class Microsoft_Office_Word2_189_0(Etw):
    pattern = Struct(
        "ptX" / Int32sl,
        "ptY" / Int32sl,
        "updateCnt" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=190, version=0)
class Microsoft_Office_Word2_190_0(Etw):
    pattern = Struct(
        "ptX" / Int32sl,
        "ptY" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=191, version=0)
class Microsoft_Office_Word2_191_0(Etw):
    pattern = Struct(
        "ptX" / Int32sl,
        "ptY" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=193, version=2)
class Microsoft_Office_Word2_193_2(Etw):
    pattern = Struct(
        "SelcpFirst" / Int32sl,
        "SelcpLim" / Int32sl,
        "DocKind" / WString,
        "ViewType" / WString,
        "pdod" / Int64ul,
        "pwwd" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=194, version=1)
class Microsoft_Office_Word2_194_1(Etw):
    pattern = Struct(
        "cmdRet" / Int32sl,
        "UsedFmt" / WString,
        "AvailFmts" / WString,
        "AvailFmtsCount" / Int64ul,
        "Size" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=195, version=2)
class Microsoft_Office_Word2_195_2(Etw):
    pattern = Struct(
        "SelcpFirst" / Int32sl,
        "SelcpLim" / Int32sl,
        "DocKind" / WString,
        "ViewType" / WString,
        "pdod" / Int64ul,
        "pwwd" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=196, version=0)
class Microsoft_Office_Word2_196_0(Etw):
    pattern = Struct(
        "cmdRet" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=197, version=2)
class Microsoft_Office_Word2_197_2(Etw):
    pattern = Struct(
        "SelcpFirst" / Int32sl,
        "SelcpLim" / Int32sl,
        "DocKind" / WString,
        "ViewType" / WString,
        "pdod" / Int64ul,
        "pwwd" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=198, version=0)
class Microsoft_Office_Word2_198_0(Etw):
    pattern = Struct(
        "cmdRet" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=199, version=0)
class Microsoft_Office_Word2_199_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "PasteType" / Int32ul,
        "SourceUrlHash" / Guid,
        "SourceLocationType" / Int32ul,
        "SourceApp" / Int32sl,
        "ContentType" / Int32ul,
        "Size" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=201, version=0)
class Microsoft_Office_Word2_201_0(Etw):
    pattern = Struct(
        "responsivenessType" / WString,
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
        "Bucket10Count" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=202, version=1)
class Microsoft_Office_Word2_202_1(Etw):
    pattern = Struct(
        "ETW_TrackbackTag" / Int32ul,
        "responsivenessType" / WString,
        "timeoutLength" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=203, version=0)
class Microsoft_Office_Word2_203_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "IsDocDirty" / Int8ul,
        "Message" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=204, version=0)
class Microsoft_Office_Word2_204_0(Etw):
    pattern = Struct(
        "FuncName" / WString,
        "Dusec" / Int64ul,
        "fAborted" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=205, version=0)
class Microsoft_Office_Word2_205_0(Etw):
    pattern = Struct(
        "Kind" / Int32sl,
        "sti" / Int32sl,
        "stiBase" / Int32sl,
        "istd" / Int32ul,
        "istdBase" / Int32sl,
        "Linked" / Int32sl,
        "LivePreview" / Int8ul,
        "fResult" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=206, version=2)
class Microsoft_Office_Word2_206_2(Etw):
    pattern = Struct(
        "ActionType" / Int32ul,
        "E2oId" / Int32ul,
        "E2oType" / Int32ul,
        "PrevTextWrapping" / Int32ul,
        "NewTextWrapping" / Int32ul,
        "SqmDocID" / Guid
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=207, version=0)
class Microsoft_Office_Word2_207_0(Etw):
    pattern = Struct(
        "ammPrev" / Int32ul,
        "ammNew" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=208, version=0)
class Microsoft_Office_Word2_208_0(Etw):
    pattern = Struct(
        "Caller" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=209, version=0)
class Microsoft_Office_Word2_209_0(Etw):
    pattern = Struct(
        "Caller" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=210, version=0)
class Microsoft_Office_Word2_210_0(Etw):
    pattern = Struct(
        "izSource" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=211, version=0)
class Microsoft_Office_Word2_211_0(Etw):
    pattern = Struct(
        "instance" / Int32ul,
        "objectType" / WString,
        "toggleToState" / WString,
        "scale" / Int32ul,
        "zoom" / Int32ul,
        "windowWidth" / Int64ul,
        "windowHeight" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=212, version=0)
class Microsoft_Office_Word2_212_0(Etw):
    pattern = Struct(
        "instance" / Int32ul,
        "objectType" / WString,
        "scale" / Int32ul,
        "zoom" / Int32ul,
        "windowWidth" / Int64ul,
        "windowHeight" / Int64ul,
        "secondLevel" / WString,
        "objectFitKind" / WString,
        "availSpaceWidth" / Int64ul,
        "availSpaceHeight" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=213, version=0)
class Microsoft_Office_Word2_213_0(Etw):
    pattern = Struct(
        "fSinglePage" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=214, version=0)
class Microsoft_Office_Word2_214_0(Etw):
    pattern = Struct(
        "PageTurnSuccess" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=217, version=0)
class Microsoft_Office_Word2_217_0(Etw):
    pattern = Struct(
        "providerName" / WString,
        "apiName" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=218, version=0)
class Microsoft_Office_Word2_218_0(Etw):
    pattern = Struct(
        "ReadModeFontSizePCT" / Double
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=223, version=0)
class Microsoft_Office_Word2_223_0(Etw):
    pattern = Struct(
        "PtlType" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=225, version=1)
class Microsoft_Office_Word2_225_1(Etw):
    pattern = Struct(
        "pwwd" / Int64ul,
        "ViewType" / WString,
        "hwwdpdod" / Int64ul,
        "DocKind" / WString,
        "cpok" / Int32ul,
        "taxcIMac" / Int32ul,
        "rcwAnchorxp" / Int32sl,
        "rcwAnchoryp" / Int32sl,
        "rcwAnchordxp" / Int32sl,
        "rcwAnchordyp" / Int32sl,
        "SELpdod" / Int64ul,
        "SELDocKind" / WString,
        "SELcpFirst" / Int32sl,
        "SELcpLim" / Int32sl,
        "fForcefullySingleThreaded" / Int8ul,
        "cplr" / Int32ul,
        "fDocsPaneUX" / Int8ul,
        "fTrackChanges" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=226, version=0)
class Microsoft_Office_Word2_226_0(Etw):
    pattern = Struct(
        "ItemType" / Int32sl,
        "tplc" / Int64sl,
        "iCat" / Int32sl,
        "nfc" / Int32sl,
        "iApplyTo" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=227, version=0)
class Microsoft_Office_Word2_227_0(Etw):
    pattern = Struct(
        "textPatternCount" / Int64ul,
        "textRangePatternCount" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=228, version=0)
class Microsoft_Office_Word2_228_0(Etw):
    pattern = Struct(
        "PtlType" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=229, version=0)
class Microsoft_Office_Word2_229_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "fUndo" / Int32sl,
        "cActions" / Int32sl,
        "fucr" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=230, version=0)
class Microsoft_Office_Word2_230_0(Etw):
    pattern = Struct(
        "fRet" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=231, version=3)
class Microsoft_Office_Word2_231_3(Etw):
    pattern = Struct(
        "fUndo" / Int32sl,
        "Command" / Int32sl,
        "CommandArgument" / Int32sl,
        "UndoType" / Int32ul,
        "fChained" / Int8ul,
        "fChainStart" / Int8ul,
        "fInLiveDrag" / Int8ul,
        "fSwapConsidered" / Int8ul,
        "fSavedByAllowSwapStyles" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=232, version=0)
class Microsoft_Office_Word2_232_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "cUndoCmdsBlown" / Int32sl,
        "cRedoCmdsBlown" / Int32sl,
        "cCmdsUsk" / Int32sl,
        "Reason" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=233, version=0)
class Microsoft_Office_Word2_233_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "fTrackChangesNewState" / Int8ul,
        "stateToggledByFCI" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=234, version=0)
class Microsoft_Office_Word2_234_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "fTrackChangesOn" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=235, version=0)
class Microsoft_Office_Word2_235_0(Etw):
    pattern = Struct(
        "OpenInRM" / Int8ul,
        "Reason" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=236, version=1)
class Microsoft_Office_Word2_236_1(Etw):
    pattern = Struct(
        "moveDistance" / Int32sl,
        "moveTime" / Int64sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=237, version=0)
class Microsoft_Office_Word2_237_0(Etw):
    pattern = Struct(
        "maxDistance1" / Int32sl,
        "maxDistanceTime1" / Int64sl,
        "maxDistance2" / Int32sl,
        "maxDistanceTime2" / Int64sl,
        "maxDistance3" / Int32sl,
        "maxDistanceTime3" / Int64sl,
        "maxTime1" / Int64sl,
        "maxTimeDistance1" / Int32sl,
        "maxTime2" / Int64sl,
        "maxTimeDistance2" / Int32sl,
        "maxTime3" / Int64sl,
        "maxTimeDistance3" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=238, version=0)
class Microsoft_Office_Word2_238_0(Etw):
    pattern = Struct(
        "dxpApp" / Int32sl,
        "dypApp" / Int32sl,
        "rclwApp" / Int32sl,
        "pctFontApp" / Int32sl,
        "dxpPageContentApp" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=239, version=1)
class Microsoft_Office_Word2_239_1(Etw):
    pattern = Struct(
        "ETW_TrackbackTag" / Int32ul,
        "SQMDocID" / Guid,
        "dk" / Int32ul,
        "cpMac" / Int32sl,
        "cpReq" / Int32sl,
        "cpFirst" / Int32sl,
        "cpLim" / Int32sl,
        "fFoundPiece" / Int8ul,
        "fBinaryPiece" / Int8ul,
        "fInBulletProofer" / Int8ul,
        "fSafeFetch" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=241, version=1)
class Microsoft_Office_Word2_241_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "FCI" / Int32ul,
        "fCoauthEdit" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=242, version=0)
class Microsoft_Office_Word2_242_0(Etw):
    pattern = Struct(
        "fRet" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=243, version=1)
class Microsoft_Office_Word2_243_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "FCI" / Int32ul,
        "fCoauthEdit" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=244, version=0)
class Microsoft_Office_Word2_244_0(Etw):
    pattern = Struct(
        "fRet" / Int32sl,
        "cPaxuadSlots" / Int32sl,
        "cPaxuadSlotsUsed" / Int32sl,
        "cPaxuadSlotsUnused" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=245, version=0)
class Microsoft_Office_Word2_245_0(Etw):
    pattern = Struct(
        "lid" / Int32sl,
        "FCI" / Int32ul,
        "dcp" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=246, version=0)
class Microsoft_Office_Word2_246_0(Etw):
    pattern = Struct(
        "reason" / Int32ul,
        "FCI" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=250, version=1)
class Microsoft_Office_Word2_250_1(Etw):
    pattern = Struct(
        "RMRR" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=251, version=0)
class Microsoft_Office_Word2_251_0(Etw):
    pattern = Struct(
        "ZoomScrollCause" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=252, version=0)
class Microsoft_Office_Word2_252_0(Etw):
    pattern = Struct(
        "flt" / Int32sl,
        "fcr" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=253, version=0)
class Microsoft_Office_Word2_253_0(Etw):
    pattern = Struct(
        "flt" / Int32sl,
        "fcr" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=254, version=0)
class Microsoft_Office_Word2_254_0(Etw):
    pattern = Struct(
        "cTasks" / Int32sl,
        "Endpoint" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=255, version=0)
class Microsoft_Office_Word2_255_0(Etw):
    pattern = Struct(
        "cExecutedTasks" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=256, version=0)
class Microsoft_Office_Word2_256_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=257, version=0)
class Microsoft_Office_Word2_257_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "fPass" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=258, version=0)
class Microsoft_Office_Word2_258_0(Etw):
    pattern = Struct(
        "AttachmentIndex" / Int64ul,
        "HResult" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=259, version=0)
class Microsoft_Office_Word2_259_0(Etw):
    pattern = Struct(
        "CID" / WString,
        "fReuse" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=260, version=0)
class Microsoft_Office_Word2_260_0(Etw):
    pattern = Struct(
        "flt" / Int32sl,
        "fcr" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=261, version=0)
class Microsoft_Office_Word2_261_0(Etw):
    pattern = Struct(
        "pctFontApp" / Int32sl,
        "pctFontUI" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=262, version=0)
class Microsoft_Office_Word2_262_0(Etw):
    pattern = Struct(
        "pctApp" / Int32sl,
        "pctUI" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=264, version=0)
class Microsoft_Office_Word2_264_0(Etw):
    pattern = Struct(
        "vcLcidEdit" / Int32sl,
        "vfFlavourT" / Int32sl,
        "lidInstall" / Int32sl,
        "lidUITemp" / Int32sl,
        "lidOS" / Int32sl,
        "lidDefault" / Int32sl,
        "lidPolicy" / Int32sl,
        "cpgUI" / Int32sl,
        "cpgOS" / Int32sl,
        "chsOS" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=266, version=0)
class Microsoft_Office_Word2_266_0(Etw):
    pattern = Struct(
        "lidKbd" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=267, version=0)
class Microsoft_Office_Word2_267_0(Etw):
    pattern = Struct(
        "vfProfileStartup" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=268, version=0)
class Microsoft_Office_Word2_268_0(Etw):
    pattern = Struct(
        "fOsrc" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=269, version=1)
class Microsoft_Office_Word2_269_1(Etw):
    pattern = Struct(
        "pdodMain" / Int64ul,
        "autoSwitchedByFCI" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=270, version=0)
class Microsoft_Office_Word2_270_0(Etw):
    pattern = Struct(
        "LevelPrev" / Int32sl,
        "LevelCur" / Int32sl,
        "UsageCur" / Int64ul,
        "LimitCur" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=271, version=0)
class Microsoft_Office_Word2_271_0(Etw):
    pattern = Struct(
        "LimitPrev" / Int64ul,
        "LimitCur" / Int64ul,
        "UsageCur" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=272, version=0)
class Microsoft_Office_Word2_272_0(Etw):
    pattern = Struct(
        "LevelCur" / Int32sl,
        "UsageCur" / Int64ul,
        "LimitCur" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=273, version=0)
class Microsoft_Office_Word2_273_0(Etw):
    pattern = Struct(
        "LevelPrev" / Int32sl,
        "UsagePrev" / Int64ul,
        "LimitPrev" / Int64ul,
        "LevelCur" / Int32sl,
        "UsageCur" / Int64ul,
        "LimitCur" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=274, version=0)
class Microsoft_Office_Word2_274_0(Etw):
    pattern = Struct(
        "PartCount" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=275, version=0)
class Microsoft_Office_Word2_275_0(Etw):
    pattern = Struct(
        "PartCount" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=277, version=1)
class Microsoft_Office_Word2_277_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "ChromeOnly" / Int8ul,
        "ReadOnly" / Int8ul,
        "PartId" / Int32ul,
        "SdtId" / Int32ul,
        "SdtContentId" / Int32ul,
        "UseBackgroundLoad" / Int8ul,
        "ReplacePart" / Int8ul,
        "PlainText" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=278, version=0)
class Microsoft_Office_Word2_278_0(Etw):
    pattern = Struct(
        "ReadOnly" / Int8ul,
        "PartId" / Int32ul,
        "SdtId" / Int32ul,
        "PlainText" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=280, version=0)
class Microsoft_Office_Word2_280_0(Etw):
    pattern = Struct(
        "Reset" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=281, version=0)
class Microsoft_Office_Word2_281_0(Etw):
    pattern = Struct(
        "SDTType" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=282, version=0)
class Microsoft_Office_Word2_282_0(Etw):
    pattern = Struct(
        "Index" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=283, version=0)
class Microsoft_Office_Word2_283_0(Etw):
    pattern = Struct(
        "CP" / Int64sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=286, version=1)
class Microsoft_Office_Word2_286_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=288, version=0)
class Microsoft_Office_Word2_288_0(Etw):
    pattern = Struct(
        "IsPlainText" / Int8ul,
        "NumberAttachments" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=289, version=0)
class Microsoft_Office_Word2_289_0(Etw):
    pattern = Struct(
        "Succeeded" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=290, version=0)
class Microsoft_Office_Word2_290_0(Etw):
    pattern = Struct(
        "PlainText" / Int8ul,
        "StreamCount" / Int64ul,
        "AttachmentCount" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=291, version=0)
class Microsoft_Office_Word2_291_0(Etw):
    pattern = Struct(
        "Success" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=292, version=0)
class Microsoft_Office_Word2_292_0(Etw):
    pattern = Struct(
        "ParaCP" / Int64sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=294, version=0)
class Microsoft_Office_Word2_294_0(Etw):
    pattern = Struct(
        "Count" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=295, version=0)
class Microsoft_Office_Word2_295_0(Etw):
    pattern = Struct(
        "ID" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=296, version=0)
class Microsoft_Office_Word2_296_0(Etw):
    pattern = Struct(
        "ID" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=297, version=0)
class Microsoft_Office_Word2_297_0(Etw):
    pattern = Struct(
        "IsReadOnly" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=299, version=0)
class Microsoft_Office_Word2_299_0(Etw):
    pattern = Struct(
        "PartId" / Int32ul,
        "SdtId" / Int32ul,
        "IsHeader" / Int8ul,
        "HeaderXValue" / Int32ul,
        "HeaderYValue" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=300, version=0)
class Microsoft_Office_Word2_300_0(Etw):
    pattern = Struct(
        "OutputType" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=301, version=0)
class Microsoft_Office_Word2_301_0(Etw):
    pattern = Struct(
        "UseBackgroundLoading" / Int8ul,
        "IsReadOnly" / Int8ul,
        "IsPlainText" / Int8ul,
        "Encoding" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=303, version=0)
class Microsoft_Office_Word2_303_0(Etw):
    pattern = Struct(
        "IsvpdodGlobalDot" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=306, version=0)
class Microsoft_Office_Word2_306_0(Etw):
    pattern = Struct(
        "fDefaultViewWebScaling" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=307, version=1)
class Microsoft_Office_Word2_307_1(Etw):
    pattern = Struct(
        "pdodMain" / Int64ul,
        "Wwd" / WString,
        "PctZoom" / Double
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=308, version=0)
class Microsoft_Office_Word2_308_0(Etw):
    pattern = Struct(
        "MsForHitTesting" / Int64ul,
        "CountOfWindowlessNetUI" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=310, version=0)
class Microsoft_Office_Word2_310_0(Etw):
    pattern = Struct(
        "fProtected" / Int8ul,
        "fEmptyIdentity" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=311, version=0)
class Microsoft_Office_Word2_311_0(Etw):
    pattern = Struct(
        "Succeeded" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=313, version=0)
class Microsoft_Office_Word2_313_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "docKind" / Int32ul,
        "SQMDocID" / Guid,
        "DocumentId" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=314, version=0)
class Microsoft_Office_Word2_314_0(Etw):
    pattern = Struct(
        "obi" / Int32sl,
        "ioid" / Int32sl,
        "dispid" / Int32sl,
        "Invoke" / WString,
        "ClassName" / WString,
        "MethodPropName" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=315, version=0)
class Microsoft_Office_Word2_315_0(Etw):
    pattern = Struct(
        "RevokedSession" / Guid
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=317, version=0)
class Microsoft_Office_Word2_317_0(Etw):
    pattern = Struct(
        "fThinAutoCorrectArrowType" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=318, version=0)
class Microsoft_Office_Word2_318_0(Etw):
    pattern = Struct(
        "pdodMain" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=319, version=0)
class Microsoft_Office_Word2_319_0(Etw):
    pattern = Struct(
        "pdodMain" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=320, version=0)
class Microsoft_Office_Word2_320_0(Etw):
    pattern = Struct(
        "pdodMain" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=321, version=0)
class Microsoft_Office_Word2_321_0(Etw):
    pattern = Struct(
        "xScroll" / Int32sl,
        "yScroll" / Int32sl,
        "PctZoom" / Double,
        "InDM" / Int8ul,
        "InVM" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=322, version=0)
class Microsoft_Office_Word2_322_0(Etw):
    pattern = Struct(
        "xScroll" / Int32sl,
        "yScroll" / Int32sl,
        "PctZoom" / Double,
        "InDM" / Int8ul,
        "InVM" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=323, version=0)
class Microsoft_Office_Word2_323_0(Etw):
    pattern = Struct(
        "unknownUnsupported" / Int32ul,
        "cssTableBackgroundImage" / Int32ul,
        "cssASpanPaddingBottom" / Int32ul,
        "cssASpanMarginBottom" / Int32ul,
        "cssDivASpanDimensions" / Int32ul,
        "cssPosition" / Int32ul,
        "htmlTableBackgroundImage" / Int32ul,
        "htmlForm" / Int32ul,
        "tableHeaderOrFooter" / Int32ul,
        "tableWiderThan61Cols" / Int32ul,
        "tableColspan" / Int32ul,
        "tableCaption" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=324, version=0)
class Microsoft_Office_Word2_324_0(Etw):
    pattern = Struct(
        "dk" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=326, version=1)
class Microsoft_Office_Word2_326_1(Etw):
    pattern = Struct(
        "id" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=330, version=1)
class Microsoft_Office_Word2_330_1(Etw):
    pattern = Struct(
        "DismissalReason" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=331, version=0)
class Microsoft_Office_Word2_331_0(Etw):
    pattern = Struct(
        "cAtm" / Int32sl,
        "dk" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=332, version=0)
class Microsoft_Office_Word2_332_0(Etw):
    pattern = Struct(
        "cAtm" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=333, version=1)
class Microsoft_Office_Word2_333_1(Etw):
    pattern = Struct(
        "Name" / WString,
        "fPass" / Int8ul,
        "msecTimeTaken" / Int64ul,
        "tInterrupted" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=334, version=0)
class Microsoft_Office_Word2_334_0(Etw):
    pattern = Struct(
        "AllowAutoRM" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=335, version=0)
class Microsoft_Office_Word2_335_0(Etw):
    pattern = Struct(
        "OldValue" / Int8ul,
        "NewValue" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=336, version=1)
class Microsoft_Office_Word2_336_1(Etw):
    pattern = Struct(
        "pdodMain" / Int64ul,
        "OldPctZoom" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=337, version=0)
class Microsoft_Office_Word2_337_0(Etw):
    pattern = Struct(
        "tbt" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=339, version=0)
class Microsoft_Office_Word2_339_0(Etw):
    pattern = Struct(
        "leftDelta" / Int32ul,
        "rightDelta" / Int32ul,
        "topDelta" / Int32ul,
        "bottomDelta" / Int32ul,
        "widthE1o" / Int32ul,
        "widthE2o" / Int32ul,
        "heightE1o" / Int32ul,
        "heightE2o" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=340, version=0)
class Microsoft_Office_Word2_340_0(Etw):
    pattern = Struct(
        "rstyp" / Int32ul,
        "xsz" / WString,
        "timeoutLength" / Int64ul,
        "corlid" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=341, version=0)
class Microsoft_Office_Word2_341_0(Etw):
    pattern = Struct(
        "rstyp" / Int32ul,
        "xsz" / WString,
        "fActive" / Int8ul,
        "corlid" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=342, version=0)
class Microsoft_Office_Word2_342_0(Etw):
    pattern = Struct(
        "zoomScrollCorrelationId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=343, version=0)
class Microsoft_Office_Word2_343_0(Etw):
    pattern = Struct(
        "zoomScrollCorrelationId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=344, version=1)
class Microsoft_Office_Word2_344_1(Etw):
    pattern = Struct(
        "XDistanceScrolled" / Int32sl,
        "YDistanceScrolled" / Int32sl,
        "DirectManipulation" / Int8ul,
        "ThumbUsed" / Int8ul,
        "PreviewShown" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=347, version=0)
class Microsoft_Office_Word2_347_0(Etw):
    pattern = Struct(
        "ForceInlineReason" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=348, version=0)
class Microsoft_Office_Word2_348_0(Etw):
    pattern = Struct(
        "TotalNotifications" / Int32ul,
        "AddedNotifications" / Int32ul,
        "RemovedNotifications" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=349, version=0)
class Microsoft_Office_Word2_349_0(Etw):
    pattern = Struct(
        "TotalNotifications" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=350, version=0)
class Microsoft_Office_Word2_350_0(Etw):
    pattern = Struct(
        "DirtyCode" / Int16ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=352, version=0)
class Microsoft_Office_Word2_352_0(Etw):
    pattern = Struct(
        "Itap" / Int32sl,
        "HeightSpecified" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=353, version=0)
class Microsoft_Office_Word2_353_0(Etw):
    pattern = Struct(
        "Itap" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=354, version=0)
class Microsoft_Office_Word2_354_0(Etw):
    pattern = Struct(
        "TimerDurationmsec" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=356, version=0)
class Microsoft_Office_Word2_356_0(Etw):
    pattern = Struct(
        "sti" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=358, version=0)
class Microsoft_Office_Word2_358_0(Etw):
    pattern = Struct(
        "message" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=359, version=4)
class Microsoft_Office_Word2_359_4(Etw):
    pattern = Struct(
        "commandline" / WString,
        "fMainExe" / Int8ul,
        "fSafeMode" / Int8ul,
        "fOleLaunchedUs" / Int8ul,
        "fOleAutomation" / Int8ul,
        "fMacroOnCmdLine" / Int8ul,
        "fLoadAddIns" / Int8ul,
        "fOnly1DDEDcl" / Int8ul,
        "fOpenAsNew" / Int8ul,
        "fReadWriteOnSave" / Int8ul,
        "fRestore" / Int8ul,
        "fNormalDotSafe" / Int8ul,
        "fDotEvt" / Int8ul,
        "fMacroSwitch" / Int8ul,
        "fOpenedDrp" / Int8ul,
        "fDocRecoveryWorkPane" / Int8ul,
        "fShowOutspace" / Int8ul,
        "fShowAllDrps" / Int8ul,
        "fDidCrashRecoveryLastTime" / Int8ul,
        "fRestoringFromRestart" / Int8ul,
        "fFreezeDryEnabled" / Int8ul,
        "cdrpGroups" / Int32sl,
        "cdrpResolvedWithOthers" / Int32sl,
        "cdrpRepaired" / Int32sl,
        "cdrpSavedOnCrash" / Int32sl,
        "cmdLineFlagsExtended" / Int32ul,
        "fGlobalDotMatchesDefault" / Int8ul,
        "fInterrupted" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=360, version=0)
class Microsoft_Office_Word2_360_0(Etw):
    pattern = Struct(
        "cFootnoteObjects" / Int64ul,
        "cEndnoteObjects" / Int64ul,
        "cTrackedChangeObjects" / Int64ul,
        "cCommentObjects" / Int64ul,
        "cRtcPresenceObjects" / Int64ul,
        "cCoauthLockObjects" / Int64ul,
        "cAtnObjects" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=361, version=0)
class Microsoft_Office_Word2_361_0(Etw):
    pattern = Struct(
        "fReply" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=365, version=0)
class Microsoft_Office_Word2_365_0(Etw):
    pattern = Struct(
        "fComment" / Int8ul,
        "fCommentPopout" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=366, version=0)
class Microsoft_Office_Word2_366_0(Etw):
    pattern = Struct(
        "fReply" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=367, version=0)
class Microsoft_Office_Word2_367_0(Etw):
    pattern = Struct(
        "fAllComments" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=368, version=0)
class Microsoft_Office_Word2_368_0(Etw):
    pattern = Struct(
        "fBtnCe" / Int8ul,
        "fSettingToDone" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=369, version=0)
class Microsoft_Office_Word2_369_0(Etw):
    pattern = Struct(
        "flTagReplaced" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=370, version=0)
class Microsoft_Office_Word2_370_0(Etw):
    pattern = Struct(
        "fPartFound" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=371, version=0)
class Microsoft_Office_Word2_371_0(Etw):
    pattern = Struct(
        "cHsp" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=372, version=0)
class Microsoft_Office_Word2_372_0(Etw):
    pattern = Struct(
        "cE2o" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=373, version=0)
class Microsoft_Office_Word2_373_0(Etw):
    pattern = Struct(
        "SuggestionNumber" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=378, version=0)
class Microsoft_Office_Word2_378_0(Etw):
    pattern = Struct(
        "HyperlinkDestinationType" / Int32ul,
        "FromAnchorTag" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=379, version=0)
class Microsoft_Office_Word2_379_0(Etw):
    pattern = Struct(
        "HyperlinkDestinationType" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=380, version=1)
class Microsoft_Office_Word2_380_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "numberOfEntities" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=381, version=1)
class Microsoft_Office_Word2_381_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "entityId" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=382, version=0)
class Microsoft_Office_Word2_382_0(Etw):
    pattern = Struct(
        "DlgType" / WString,
        "DlgID" / Int64ul,
        "CmdName" / WString,
        "FCI" / Int32ul,
        "TCID" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=386, version=0)
class Microsoft_Office_Word2_386_0(Etw):
    pattern = Struct(
        "cPartsLoaded" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=388, version=0)
class Microsoft_Office_Word2_388_0(Etw):
    pattern = Struct(
        "HostedControl" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=389, version=0)
class Microsoft_Office_Word2_389_0(Etw):
    pattern = Struct(
        "HostedControl" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=390, version=0)
class Microsoft_Office_Word2_390_0(Etw):
    pattern = Struct(
        "fTruncationNeeded" / Int8ul,
        "fCallSucceeded" / Int8ul,
        "addtionalSpaceNeeded" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=391, version=0)
class Microsoft_Office_Word2_391_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=392, version=0)
class Microsoft_Office_Word2_392_0(Etw):
    pattern = Struct(
        "CardCount" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=393, version=0)
class Microsoft_Office_Word2_393_0(Etw):
    pattern = Struct(
        "CardCount" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=394, version=0)
class Microsoft_Office_Word2_394_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "CardId" / Int32ul,
        "dxaLeftOffset" / Int64ul,
        "dxaRightOffset" / Int64ul,
        "dyaTopOffset" / Int64ul,
        "dyaBottomOffset" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=395, version=0)
class Microsoft_Office_Word2_395_0(Etw):
    pattern = Struct(
        "PartsToRemove" / Int64ul,
        "CardId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=396, version=0)
class Microsoft_Office_Word2_396_0(Etw):
    pattern = Struct(
        "PartsToRemove" / Int64ul,
        "CardId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=397, version=0)
class Microsoft_Office_Word2_397_0(Etw):
    pattern = Struct(
        "CardIdToReplace" / Int32ul,
        "CardsToRemove" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=398, version=0)
class Microsoft_Office_Word2_398_0(Etw):
    pattern = Struct(
        "CardIdToReplace" / Int32ul,
        "CardsToRemove" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=399, version=0)
class Microsoft_Office_Word2_399_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=400, version=0)
class Microsoft_Office_Word2_400_0(Etw):
    pattern = Struct(
        "Active" / Int8ul,
        "PartId" / Int32ul,
        "PartSdtId" / Int32ul,
        "PartReadOnly" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=401, version=0)
class Microsoft_Office_Word2_401_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "CardId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=402, version=0)
class Microsoft_Office_Word2_402_0(Etw):
    pattern = Struct(
        "Succeeded" / Int8ul,
        "LoadAborted" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=403, version=0)
class Microsoft_Office_Word2_403_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "PartId" / Int32ul,
        "PartSdtId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=404, version=0)
class Microsoft_Office_Word2_404_0(Etw):
    pattern = Struct(
        "PartId" / Int32ul,
        "PartSdtId" / Int32ul,
        "DraftName" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=405, version=0)
class Microsoft_Office_Word2_405_0(Etw):
    pattern = Struct(
        "ResultSize" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=406, version=0)
class Microsoft_Office_Word2_406_0(Etw):
    pattern = Struct(
        "HyperlinkProtocol" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=407, version=1)
class Microsoft_Office_Word2_407_1(Etw):
    pattern = Struct(
        "pwwd" / Int64ul,
        "PartId" / Int32ul,
        "PartSdtId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=408, version=0)
class Microsoft_Office_Word2_408_0(Etw):
    pattern = Struct(
        "PartId" / Int32ul,
        "PartSdtId" / Int32ul,
        "Succeeded" / Int8ul,
        "DyDip" / Int32sl,
        "DxDip" / Int32sl,
        "ScaleUI" / Float32l
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=409, version=0)
class Microsoft_Office_Word2_409_0(Etw):
    pattern = Struct(
        "Succeeded" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=411, version=0)
class Microsoft_Office_Word2_411_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=412, version=0)
class Microsoft_Office_Word2_412_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=413, version=1)
class Microsoft_Office_Word2_413_1(Etw):
    pattern = Struct(
        "pwwd" / Int64ul,
        "dxdipMargin" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=415, version=0)
class Microsoft_Office_Word2_415_0(Etw):
    pattern = Struct(
        "fHeader" / Int8ul,
        "ControlHandle" / Int64ul,
        "HostParentHandle" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=416, version=0)
class Microsoft_Office_Word2_416_0(Etw):
    pattern = Struct(
        "ScaleUI" / Float32l
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=417, version=0)
class Microsoft_Office_Word2_417_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "CardId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=418, version=0)
class Microsoft_Office_Word2_418_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "CardId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=419, version=0)
class Microsoft_Office_Word2_419_0(Etw):
    pattern = Struct(
        "Pdod" / Int64ul,
        "DusecConversionTime" / Int64ul,
        "E1oCount" / Int32ul,
        "Succeeded" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=420, version=0)
class Microsoft_Office_Word2_420_0(Etw):
    pattern = Struct(
        "Success" / Int8ul,
        "icf" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=421, version=0)
class Microsoft_Office_Word2_421_0(Etw):
    pattern = Struct(
        "Success" / Int8ul,
        "icf" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=422, version=0)
class Microsoft_Office_Word2_422_0(Etw):
    pattern = Struct(
        "Success" / Int8ul,
        "icf" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=426, version=0)
class Microsoft_Office_Word2_426_0(Etw):
    pattern = Struct(
        "fSuccess" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=427, version=0)
class Microsoft_Office_Word2_427_0(Etw):
    pattern = Struct(
        "ifld" / Int32sl,
        "cpMacPdodClone" / Int32sl,
        "fCacheAllHspAtOnce" / Int8ul,
        "fInline" / Int8ul,
        "fPseudoInline" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=428, version=0)
class Microsoft_Office_Word2_428_0(Etw):
    pattern = Struct(
        "usecSystemUptime" / Int64ul,
        "usecUserCpuTime" / Int64ul,
        "usecSystemCpuTime" / Int64ul,
        "usecProcessCpuTime" / Int64ul,
        "usecMainThreadCpuTime" / Int64ul,
        "maxrss" / Int64sl,
        "ixrss" / Int64sl,
        "idrss" / Int64sl,
        "isrss" / Int64sl,
        "minflt" / Int64sl,
        "majflt" / Int64sl,
        "nswap" / Int64sl,
        "inblock" / Int64sl,
        "oublock" / Int64sl,
        "msgsnd" / Int64sl,
        "msgrcv" / Int64sl,
        "nsignals" / Int64sl,
        "nvcsw" / Int64sl,
        "nivcsw" / Int64sl,
        "fGetrusageSuccess" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=429, version=0)
class Microsoft_Office_Word2_429_0(Etw):
    pattern = Struct(
        "cpFirst" / Int32sl,
        "cpLim" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=430, version=0)
class Microsoft_Office_Word2_430_0(Etw):
    pattern = Struct(
        "cWhiteSpaces" / Int32sl,
        "cSymbols" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=431, version=1)
class Microsoft_Office_Word2_431_1(Etw):
    pattern = Struct(
        "pmwd" / Int64ul,
        "pwwd" / Int64ul,
        "hwnd" / Int64ul,
        "ViewType" / WString,
        "CountofMWDs" / Int32sl,
        "MWDPunkWindow" / Int64ul,
        "fServerObjPunkWindow" / Int8ul,
        "pdod" / Int64ul,
        "dk" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=432, version=0)
class Microsoft_Office_Word2_432_0(Etw):
    pattern = Struct(
        "FoundDocKind" / WString,
        "OriginalDocKind" / WString,
        "BookMarkClass" / Int16ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=433, version=0)
class Microsoft_Office_Word2_433_0(Etw):
    pattern = Struct(
        "dypAdjust" / Int32sl,
        "ypHostedTop" / Int32sl,
        "dypScrollable" / Int32sl,
        "ypScrollerOffset" / Int32sl,
        "dypRootHeight" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=434, version=0)
class Microsoft_Office_Word2_434_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "lCommentId" / Int64sl,
        "fBulletsAndNumbering" / Int8ul,
        "fTable" / Int8ul,
        "fWingdings" / Int8ul,
        "fMathZone" / Int8ul,
        "fSymbols" / Int8ul,
        "fExtSymbols" / Int8ul,
        "fArtObjects" / Int8ul,
        "fPictures" / Int8ul,
        "fE1oInkComments" / Int8ul,
        "fShapes" / Int8ul,
        "fFootnote" / Int8ul,
        "fMention" / Int8ul,
        "fHyperLink" / Int8ul,
        "fRevisionMarking" / Int8ul,
        "fPageField" / Int8ul,
        "fComplexField" / Int8ul,
        "fOtherFields" / Int8ul,
        "fSpecialChars" / Int8ul,
        "fUnsupportedUnderlineFormatting" / Int8ul,
        "fUnsupportedStrikethroughFormatting" / Int8ul,
        "fUnsupportedFontColorFormatting" / Int8ul,
        "fSubSuperScriptFormatting" / Int8ul,
        "fFontFamilyFormatting" / Int8ul,
        "fFontSizeFormatting" / Int8ul,
        "fOtherContentNotUnderstood" / Int8ul,
        "fUnsupportedContent" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=435, version=0)
class Microsoft_Office_Word2_435_0(Etw):
    pattern = Struct(
        "hpl" / Int64ul,
        "idpci" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=436, version=0)
class Microsoft_Office_Word2_436_0(Etw):
    pattern = Struct(
        "hpl" / Int64ul,
        "idpci" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=437, version=0)
class Microsoft_Office_Word2_437_0(Etw):
    pattern = Struct(
        "fCannotDeterminePivot" / Int8ul,
        "fNoContextAllowable" / Int8ul,
        "fContextReduced" / Int8ul,
        "fContextReducedToShort" / Int8ul,
        "fContextNaturallyTooShort" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=438, version=0)
class Microsoft_Office_Word2_438_0(Etw):
    pattern = Struct(
        "flt" / Int32sl,
        "Reason" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1000, version=0)
class Microsoft_Office_Word2_1000_0(Etw):
    pattern = Struct(
        "docKind" / Int32ul,
        "fHeader" / Int8ul,
        "ihdt" / Int32ul,
        "cpStart" / Int32sl,
        "cpLim" / Int32sl,
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl,
        "fDropCap" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1002, version=0)
class Microsoft_Office_Word2_1002_0(Etw):
    pattern = Struct(
        "LrgKind" / WString,
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1030, version=0)
class Microsoft_Office_Word2_1030_0(Etw):
    pattern = Struct(
        "docAnchorKind" / Int32ul,
        "fHeader" / Int8ul,
        "ihdt" / Int32ul,
        "cpAnchor" / Int32sl,
        "SpxKind" / WString,
        "xlLeft" / Int32sl,
        "ylTop" / Int32sl,
        "xlRight" / Int32sl,
        "ylBottom" / Int32sl,
        "xlFull" / Int32sl,
        "ylFull" / Int32sl,
        "fIgnorePositionPTS" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1040, version=0)
class Microsoft_Office_Word2_1040_0(Etw):
    pattern = Struct(
        "docKind" / Int32ul,
        "cpStart" / Int32sl,
        "cpLim" / Int32sl,
        "left" / Int32sl,
        "top" / Int32sl,
        "lstFlow" / Int8ul,
        "heightRef" / Int32sl,
        "heightPres" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1050, version=0)
class Microsoft_Office_Word2_1050_0(Etw):
    pattern = Struct(
        "docKind" / Int32ul,
        "cpStart" / Int32sl,
        "cpLim" / Int32sl,
        "left" / Int32sl,
        "top" / Int32sl,
        "lstFlow" / Int8ul,
        "heightRef" / Int32sl,
        "heightPres" / Int32sl,
        "upLimAutonumberingText" / Int32sl,
        "upLimLineProper" / Int32sl,
        "upLimLine" / Int32sl,
        "breakEndr" / Int16ul,
        "fForcedBreak" / Int8ul,
        "fTopEnable" / Int8ul,
        "fBottomEnable" / Int8ul,
        "fBetweenTop" / Int8ul,
        "fBetweenBottom" / Int8ul,
        "fVolatile" / Int8ul,
        "fPicture" / Int8ul,
        "fHandAtn" / Int8ul,
        "fFirstLineCp" / Int8ul,
        "fSplatSub" / Int8ul,
        "fSfx" / Int8ul,
        "lbrCRJ" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1051, version=0)
class Microsoft_Office_Word2_1051_0(Etw):
    pattern = Struct(
        "lstFlow" / Int8ul,
        "durReservedLeft" / Int32sl,
        "durRightIndentBreak" / Int32sl,
        "durRightIndentJustify" / Int32sl,
        "durHyphenationZone" / Int32sl,
        "lsbrj" / Int8ul,
        "lskj" / Int8ul,
        "lskal" / Int8ul,
        "durAutoDecimalTab" / Int32sl,
        "fVisiCondHyphens" / Int8ul,
        "fVisiParaMarks" / Int8ul,
        "fVisiSpaces" / Int8ul,
        "fVisiTabs" / Int8ul,
        "fVisiSplats" / Int8ul,
        "fVisiBreaks" / Int8ul,
        "fPunctStartLine" / Int8ul,
        "fHangingPunct" / Int8ul,
        "fApplyBreakingRules" / Int8ul,
        "fApplyOpticalAlignment" / Int8ul,
        "fPresSuppressWiggle" / Int8ul,
        "fAutonumber" / Int8ul,
        "fAutoDecimalTab" / Int8ul,
        "fUnderlineTrailSpacesRM" / Int8ul,
        "fSpacesInfluenceHeight" / Int8ul,
        "fAllowSplatLine" / Int8ul,
        "fForceBreakAsNext" / Int8ul,
        "fCheckTruncateBefore" / Int8ul,
        "fAllowHyphenation" / Int8ul,
        "fDrawInLogicalOrder" / Int8ul,
        "fTreatHyphenAsRegular" / Int8ul,
        "fWrapTrailingSpaces" / Int8ul,
        "fWrapAllSpaces" / Int8ul,
        "fForgetLastTabAlignment" / Int8ul,
        "fIndentChangesHyphenZone" / Int8ul,
        "fNoPunctAfterAutoNumber" / Int8ul,
        "fResolveTabsAsWord97" / Int8ul,
        "fIgnoreHeightOfEOL" / Int8ul,
        "fSpecialFirstLine" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1052, version=0)
class Microsoft_Office_Word2_1052_0(Etw):
    pattern = Struct(
        "edge" / Int8ul,
        "brcType" / Int32sl,
        "dptLineWidth" / Int32sl,
        "dptSpace" / Int32sl,
        "fShadow" / Int8ul,
        "fFrame" / Int8ul,
        "fPdvv" / Int8ul,
        "heightRef" / Int32sl,
        "heightPres" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1053, version=1)
class Microsoft_Office_Word2_1053_1(Etw):
    pattern = Struct(
        "Text" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1060, version=0)
class Microsoft_Office_Word2_1060_0(Etw):
    pattern = Struct(
        "ipgd" / Int32sl,
        "cpStart" / Int32sl,
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl,
        "VerticalAlign" / Int16ul,
        "fVertical" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1070, version=0)
class Microsoft_Office_Word2_1070_0(Etw):
    pattern = Struct(
        "docKind" / Int32ul,
        "fHeader" / Int8ul,
        "ihdt" / Int32ul,
        "cpStart" / Int32sl,
        "cpLim" / Int32sl,
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1090, version=0)
class Microsoft_Office_Word2_1090_0(Etw):
    pattern = Struct(
        "ipgdCur" / Int32sl,
        "pgnNext" / Int32sl,
        "fLandscape" / Int8ul,
        "duPageES" / Int32sl,
        "dvPageES" / Int32sl,
        "fSlicedPage" / Int8ul,
        "cpLim" / Int32sl,
        "ylTopMargin" / Int32sl,
        "ylBottomMargin" / Int32sl,
        "xlLeftMargin" / Int32sl,
        "xlRightMargin" / Int32sl,
        "fEmptyPage" / Int8ul,
        "fHasBubbles" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1148, version=0)
class Microsoft_Office_Word2_1148_0(Etw):
    pattern = Struct(
        "printer" / WString,
        "driver" / WString,
        "fUsePrinterMetrics" / Int8ul,
        "xdpi" / Int32sl,
        "ydpi" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1150, version=0)
class Microsoft_Office_Word2_1150_0(Etw):
    pattern = Struct(
        "dodKind" / Int32ul,
        "ihdt" / Int32ul,
        "cpFirst" / Int32sl,
        "cpLim" / Int32sl,
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl,
        "fDropCap" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1152, version=0)
class Microsoft_Office_Word2_1152_0(Etw):
    pattern = Struct(
        "DRK" / Int32sl,
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1160, version=0)
class Microsoft_Office_Word2_1160_0(Etw):
    pattern = Struct(
        "dodKind" / Int32ul,
        "ihdt" / Int32ul,
        "cpAnchor" / Int32sl,
        "drdoKind" / Int64ul,
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1170, version=0)
class Microsoft_Office_Word2_1170_0(Etw):
    pattern = Struct(
        "cpFirst" / Int32sl,
        "cpLim" / Int32sl,
        "left" / Int32sl,
        "top" / Int32sl,
        "dxp" / Int32sl,
        "dyp" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1180, version=0)
class Microsoft_Office_Word2_1180_0(Etw):
    pattern = Struct(
        "ipgd" / Int32sl,
        "xlLeft" / Int32sl,
        "ylTop" / Int32sl,
        "xlRight" / Int32sl,
        "ylBottom" / Int32sl,
        "fLandscape" / Int8ul,
        "fGoodClient" / Int8ul,
        "yaTopMargin" / Int32sl,
        "dyaBottomMargin" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1192, version=1)
class Microsoft_Office_Word2_1192_1(Etw):
    pattern = Struct(
        "cxpInch" / Int32sl,
        "cypInch" / Int32sl,
        "cxtInch" / Int32sl,
        "cytInch" / Int32sl,
        "fticmOut" / Int32sl,
        "fticmBase" / Int32sl,
        "pctZoom" / Int32sl,
        "ViewType" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1195, version=0)
class Microsoft_Office_Word2_1195_0(Etw):
    pattern = Struct(
        "ipgd" / Int32sl,
        "xlLeft" / Int32sl,
        "ylTop" / Int32sl,
        "xlRight" / Int32sl,
        "ylBottom" / Int32sl,
        "yaTopMargin" / Int32sl,
        "dyaBottomMargin" / Int32sl,
        "dmOrient" / Int32sl,
        "fGoodClient" / Int8ul,
        "cpFirst" / Int32sl,
        "cpLim" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1198, version=0)
class Microsoft_Office_Word2_1198_0(Etw):
    pattern = Struct(
        "xpLeft" / Int32sl,
        "ypTop" / Int32sl,
        "dxp" / Int32sl,
        "dyp" / Int32sl,
        "cpMin" / Int32sl,
        "dcp" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1201, version=0)
class Microsoft_Office_Word2_1201_0(Etw):
    pattern = Struct(
        "drk" / Int32sl,
        "dodKind" / Int32ul,
        "xl" / Int32sl,
        "yl" / Int32sl,
        "dxl" / Int32sl,
        "dyl" / Int32sl,
        "xt" / Int32sl,
        "yt" / Int32sl,
        "dxt" / Int32sl,
        "dyt" / Int32sl,
        "cpFirst" / Int32sl,
        "cpLim" / Int32sl,
        "fDropCap" / Int8ul,
        "ihdt" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1202, version=0)
class Microsoft_Office_Word2_1202_0(Etw):
    pattern = Struct(
        "drk" / Int32sl,
        "dodKind" / Int32ul,
        "xl" / Int32sl,
        "yl" / Int32sl,
        "dxl" / Int32sl,
        "dyl" / Int32sl,
        "xt" / Int32sl,
        "yt" / Int32sl,
        "dxt" / Int32sl,
        "dyt" / Int32sl,
        "cpFirst" / Int32sl,
        "cpLim" / Int32sl,
        "fDropCap" / Int8ul,
        "ihdt" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1203, version=0)
class Microsoft_Office_Word2_1203_0(Etw):
    pattern = Struct(
        "drk" / Int32sl,
        "dodKind" / Int32ul,
        "cpAnchor" / Int32sl,
        "drdoKind" / Int64ul,
        "xl" / Int32sl,
        "yl" / Int32sl,
        "dxl" / Int32sl,
        "dyl" / Int32sl,
        "fHdr" / Int8ul,
        "ihdt" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1204, version=0)
class Microsoft_Office_Word2_1204_0(Etw):
    pattern = Struct(
        "drk" / Int32sl,
        "drkx" / Int32sl,
        "xl" / Int32sl,
        "yl" / Int32sl,
        "dxl" / Int32sl,
        "dyl" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1205, version=0)
class Microsoft_Office_Word2_1205_0(Etw):
    pattern = Struct(
        "drk" / Int32sl,
        "drkx" / Int32sl,
        "xl" / Int32sl,
        "yl" / Int32sl,
        "dxl" / Int32sl,
        "dyl" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1206, version=0)
class Microsoft_Office_Word2_1206_0(Etw):
    pattern = Struct(
        "docAnchorKind" / Int32ul,
        "fHeader" / Int8ul,
        "ihdt" / Int32ul,
        "cpAnchor" / Int32sl,
        "SpxKind" / WString,
        "xlFull" / Int32sl,
        "ylFull" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1207, version=0)
class Microsoft_Office_Word2_1207_0(Etw):
    pattern = Struct(
        "dvpAscent" / Int32sl,
        "dvrAscent" / Int32sl,
        "dvpDescent" / Int32sl,
        "dvrDescent" / Int32sl,
        "dvpMultiLineHeight" / Int32sl,
        "dvrMultiLineHeight" / Int32sl,
        "dvpAscentAutoNumber" / Int32sl,
        "dvrAscentAutoNumber" / Int32sl,
        "dvpDescentAutoNumber" / Int32sl,
        "dvrDescentAutoNumber" / Int32sl,
        "durContent" / Int32sl,
        "cpLimToContinue" / Int32sl,
        "cpLimToStay" / Int32sl,
        "dcpDepend" / Int32sl,
        "endres" / Int32sl,
        "vaAdvance" / Int32sl,
        "fAdvanced" / Int8ul,
        "fFirstLineInPara" / Int8ul,
        "fTabInMarginExLine" / Int8ul,
        "fForcedBreak" / Int8ul,
        "fNoCSSInlineContent" / Int8ul,
        "fEllipsis" / Int8ul,
        "fNonTextObjectPresent" / Int8ul,
        "fAnmPresent" / Int8ul,
        "EffectsFlags" / Int32ul,
        "kysr" / Int32sl,
        "wchYsr" / Int32sl,
        "wchYsr2" / Int32sl,
        "lshq" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1208, version=0)
class Microsoft_Office_Word2_1208_0(Etw):
    pattern = Struct(
        "upStartLineOriginal" / Int64sl,
        "upStartLine" / Int64sl,
        "upLimAutonumberingText" / Int64sl,
        "upStartMainText" / Int64sl,
        "upStartLineProper" / Int64sl,
        "upLimLineProper" / Int64sl,
        "upLimLine" / Int64sl,
        "upRightMargin" / Int64sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1228, version=0)
class Microsoft_Office_Word2_1228_0(Etw):
    pattern = Struct(
        "xdpi" / Int32sl,
        "ydpi" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1300, version=0)
class Microsoft_Office_Word2_1300_0(Etw):
    pattern = Struct(
        "ppj" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1302, version=0)
class Microsoft_Office_Word2_1302_0(Etw):
    pattern = Struct(
        "ppj" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1304, version=0)
class Microsoft_Office_Word2_1304_0(Etw):
    pattern = Struct(
        "ppj" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1306, version=0)
class Microsoft_Office_Word2_1306_0(Etw):
    pattern = Struct(
        "ppj" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1308, version=0)
class Microsoft_Office_Word2_1308_0(Etw):
    pattern = Struct(
        "ppj" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1310, version=0)
class Microsoft_Office_Word2_1310_0(Etw):
    pattern = Struct(
        "ppj" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1312, version=0)
class Microsoft_Office_Word2_1312_0(Etw):
    pattern = Struct(
        "ppj" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1314, version=0)
class Microsoft_Office_Word2_1314_0(Etw):
    pattern = Struct(
        "ppj" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1316, version=0)
class Microsoft_Office_Word2_1316_0(Etw):
    pattern = Struct(
        "ppj" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1318, version=0)
class Microsoft_Office_Word2_1318_0(Etw):
    pattern = Struct(
        "ppj" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1320, version=0)
class Microsoft_Office_Word2_1320_0(Etw):
    pattern = Struct(
        "ppj" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1322, version=0)
class Microsoft_Office_Word2_1322_0(Etw):
    pattern = Struct(
        "ppj" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1324, version=0)
class Microsoft_Office_Word2_1324_0(Etw):
    pattern = Struct(
        "ppj" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1326, version=0)
class Microsoft_Office_Word2_1326_0(Etw):
    pattern = Struct(
        "ppj" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1329, version=1)
class Microsoft_Office_Word2_1329_1(Etw):
    pattern = Struct(
        "Tag" / Int32ul,
        "ppj" / Int64ul,
        "fCanceledByUser" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1330, version=1)
class Microsoft_Office_Word2_1330_1(Etw):
    pattern = Struct(
        "fMacro" / Int8ul,
        "numPages" / Int32sl,
        "rangeType" / Int32sl,
        "rangeSz" / WString,
        "jobParity" / Int32sl,
        "jobParitySz" / WString,
        "numCopies" / Int32sl,
        "fCollate" / Int8ul,
        "fDuplex" / Int8ul,
        "source" / Int32sl,
        "sourceSz" / WString,
        "fPrintToFile" / Int8ul,
        "pgsPerSheet" / Int32sl,
        "dmPaper" / Int32sl,
        "numSections" / Int32sl,
        "width" / Int64ul,
        "height" / Int64ul,
        "lMargin" / Int64ul,
        "rMargin" / Int64ul,
        "tMargin" / Int64ul,
        "bMargin" / Int64ul,
        "dmOrient" / Int32sl,
        "dmOrientSz" / WString,
        "prType" / WString,
        "szPrinterDev" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1331, version=1)
class Microsoft_Office_Word2_1331_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "grfpr" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1333, version=0)
class Microsoft_Office_Word2_1333_0(Etw):
    pattern = Struct(
        "ppj" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1335, version=0)
class Microsoft_Office_Word2_1335_0(Etw):
    pattern = Struct(
        "ppj" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1337, version=0)
class Microsoft_Office_Word2_1337_0(Etw):
    pattern = Struct(
        "ppj" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1339, version=0)
class Microsoft_Office_Word2_1339_0(Etw):
    pattern = Struct(
        "pPrintHandler" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1341, version=0)
class Microsoft_Office_Word2_1341_0(Etw):
    pattern = Struct(
        "pPrintHandler" / Int64ul,
        "desiredPage" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1343, version=0)
class Microsoft_Office_Word2_1343_0(Etw):
    pattern = Struct(
        "pPrintHandler" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1345, version=0)
class Microsoft_Office_Word2_1345_0(Etw):
    pattern = Struct(
        "pPrintHandler" / Int64ul,
        "PTCompletion" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1347, version=0)
class Microsoft_Office_Word2_1347_0(Etw):
    pattern = Struct(
        "pPrintHandler" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1348, version=0)
class Microsoft_Office_Word2_1348_0(Etw):
    pattern = Struct(
        "pPrintHandler" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1349, version=0)
class Microsoft_Office_Word2_1349_0(Etw):
    pattern = Struct(
        "pFastPrintTaskAppImpl" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1350, version=0)
class Microsoft_Office_Word2_1350_0(Etw):
    pattern = Struct(
        "pFastPrintTaskAppImpl" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1351, version=0)
class Microsoft_Office_Word2_1351_0(Etw):
    pattern = Struct(
        "pFastPrintTaskAppImpl" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1352, version=1)
class Microsoft_Office_Word2_1352_1(Etw):
    pattern = Struct(
        "pFastPrintTaskAppImpl" / Int64ul,
        "ipgd" / Int32sl,
        "dxdipPage" / Int32sl,
        "dydipPage" / Int32sl,
        "xdipContent" / Int32sl,
        "ydipContent" / Int32sl,
        "dxdipContent" / Int32sl,
        "dydipContent" / Int32sl,
        "fPrintMarkup" / Int8ul,
        "fPrintBgImages" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1354, version=1)
class Microsoft_Office_Word2_1354_1(Etw):
    pattern = Struct(
        "pFastPrintTaskAppImpl" / Int64ul,
        "ipgd" / Int32sl,
        "dxpPreview" / Int32sl,
        "dypPreview" / Int32sl,
        "xpPrintable" / Int32sl,
        "ypPrintable" / Int32sl,
        "dxpPrintable" / Int32sl,
        "dypPrintable" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1356, version=2)
class Microsoft_Office_Word2_1356_2(Etw):
    pattern = Struct(
        "pFastPrintTaskAppImpl" / Int64ul,
        "pPrintDocuemntPackageTarget" / Int64ul,
        "dxaPage" / Int32sl,
        "dyaPage" / Int32sl,
        "xdipContent" / Int32sl,
        "ydipContent" / Int32sl,
        "dxdipContent" / Int32sl,
        "dydipContent" / Int32sl,
        "printRange" / Int32sl,
        "customRange" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1358, version=0)
class Microsoft_Office_Word2_1358_0(Etw):
    pattern = Struct(
        "pFastPrintTaskAppImpl" / Int64ul,
        "completion" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1359, version=0)
class Microsoft_Office_Word2_1359_0(Etw):
    pattern = Struct(
        "ipgdMacNew" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1360, version=0)
class Microsoft_Office_Word2_1360_0(Etw):
    pattern = Struct(
        "PrintSettingUpdated" / WString,
        "InOutspace" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1361, version=0)
class Microsoft_Office_Word2_1361_0(Etw):
    pattern = Struct(
        "fFileSize" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1362, version=0)
class Microsoft_Office_Word2_1362_0(Etw):
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
        "TopUnresponsiveDuration5Msec" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1363, version=0)
class Microsoft_Office_Word2_1363_0(Etw):
    pattern = Struct(
        "CountofIntervals" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1364, version=0)
class Microsoft_Office_Word2_1364_0(Etw):
    pattern = Struct(
        "CountofIntervals" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1369, version=0)
class Microsoft_Office_Word2_1369_0(Etw):
    pattern = Struct(
        "MacPMSessionError" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1377, version=0)
class Microsoft_Office_Word2_1377_0(Etw):
    pattern = Struct(
        "E2oType" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1378, version=0)
class Microsoft_Office_Word2_1378_0(Etw):
    pattern = Struct(
        "FTransparentFill" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1401, version=0)
class Microsoft_Office_Word2_1401_0(Etw):
    pattern = Struct(
        "lid" / Int32sl,
        "Eaten" / Int8ul,
        "Succeeded" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1403, version=0)
class Microsoft_Office_Word2_1403_0(Etw):
    pattern = Struct(
        "lid" / Int32sl,
        "Eaten" / Int8ul,
        "Succeeded" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1404, version=0)
class Microsoft_Office_Word2_1404_0(Etw):
    pattern = Struct(
        "FunctionName" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1405, version=0)
class Microsoft_Office_Word2_1405_0(Etw):
    pattern = Struct(
        "FunctionName" / WString,
        "lid" / Int32sl,
        "HResult" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1407, version=0)
class Microsoft_Office_Word2_1407_0(Etw):
    pattern = Struct(
        "lid" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1409, version=0)
class Microsoft_Office_Word2_1409_0(Etw):
    pattern = Struct(
        "lid" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1410, version=0)
class Microsoft_Office_Word2_1410_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1411, version=0)
class Microsoft_Office_Word2_1411_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1412, version=0)
class Microsoft_Office_Word2_1412_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1413, version=0)
class Microsoft_Office_Word2_1413_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1414, version=0)
class Microsoft_Office_Word2_1414_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1415, version=0)
class Microsoft_Office_Word2_1415_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1416, version=0)
class Microsoft_Office_Word2_1416_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1417, version=0)
class Microsoft_Office_Word2_1417_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1420, version=1)
class Microsoft_Office_Word2_1420_1(Etw):
    pattern = Struct(
        "logId" / Int32ul,
        "corId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1421, version=1)
class Microsoft_Office_Word2_1421_1(Etw):
    pattern = Struct(
        "logId" / Int32ul,
        "corId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1422, version=1)
class Microsoft_Office_Word2_1422_1(Etw):
    pattern = Struct(
        "logId" / Int32ul,
        "corId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1423, version=0)
class Microsoft_Office_Word2_1423_0(Etw):
    pattern = Struct(
        "cBatchEdit" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1436, version=0)
class Microsoft_Office_Word2_1436_0(Etw):
    pattern = Struct(
        "logId" / Int32ul,
        "cpFirst" / Int32ul,
        "cpLim" / Int32ul,
        "grfsel" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1437, version=0)
class Microsoft_Office_Word2_1437_0(Etw):
    pattern = Struct(
        "logId" / Int32ul,
        "cpMac" / Int32ul,
        "dk" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1438, version=0)
class Microsoft_Office_Word2_1438_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1439, version=1)
class Microsoft_Office_Word2_1439_1(Etw):
    pattern = Struct(
        "logId" / Int32ul,
        "corId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1440, version=0)
class Microsoft_Office_Word2_1440_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1441, version=0)
class Microsoft_Office_Word2_1441_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1442, version=0)
class Microsoft_Office_Word2_1442_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1443, version=0)
class Microsoft_Office_Word2_1443_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1444, version=0)
class Microsoft_Office_Word2_1444_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1445, version=0)
class Microsoft_Office_Word2_1445_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1446, version=0)
class Microsoft_Office_Word2_1446_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1447, version=0)
class Microsoft_Office_Word2_1447_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1448, version=0)
class Microsoft_Office_Word2_1448_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1449, version=0)
class Microsoft_Office_Word2_1449_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1450, version=0)
class Microsoft_Office_Word2_1450_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1451, version=0)
class Microsoft_Office_Word2_1451_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1452, version=0)
class Microsoft_Office_Word2_1452_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1453, version=0)
class Microsoft_Office_Word2_1453_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1454, version=0)
class Microsoft_Office_Word2_1454_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1455, version=0)
class Microsoft_Office_Word2_1455_0(Etw):
    pattern = Struct(
        "logId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1456, version=0)
class Microsoft_Office_Word2_1456_0(Etw):
    pattern = Struct(
        "cp" / Int32ul,
        "ccp" / Int32ul,
        "cvText" / Int32ul,
        "cvBack" / Int32ul,
        "cvUl" / Int32ul,
        "kul" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1457, version=0)
class Microsoft_Office_Word2_1457_0(Etw):
    pattern = Struct(
        "lid" / Int32ul,
        "fRevMarkingPdod" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1458, version=0)
class Microsoft_Office_Word2_1458_0(Etw):
    pattern = Struct(
        "Pdod" / Int64ul,
        "DocKind" / WString,
        "Lid" / Int32ul,
        "Cicero" / Int8ul,
        "IMMForced" / Int8ul,
        "CiceroAvailable" / Int8ul,
        "UIMName" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1459, version=0)
class Microsoft_Office_Word2_1459_0(Etw):
    pattern = Struct(
        "cpFirstChange" / Int32sl,
        "cpLimChange" / Int32sl,
        "cpFirstUrb" / Int32sl,
        "cpLimUrb" / Int32sl,
        "cpFirstComp" / Int32sl,
        "cpLimComp" / Int32sl,
        "Lid" / Int32ul,
        "UIMName" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1460, version=0)
class Microsoft_Office_Word2_1460_0(Etw):
    pattern = Struct(
        "correlationId" / Int32ul,
        "messagePostDelay" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1500, version=2)
class Microsoft_Office_Word2_1500_2(Etw):
    pattern = Struct(
        "fSearchWord" / Int32ul,
        "fSearchCase" / Int32ul,
        "fSndsLike" / Int32ul,
        "fFuzzy" / Int32ul,
        "fMatchByte" / Int32ul,
        "searchStringLength" / Int32sl,
        "InReadmode" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1501, version=0)
class Microsoft_Office_Word2_1501_0(Etw):
    pattern = Struct(
        "Next" / Int8ul,
        "FindEventId" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1502, version=0)
class Microsoft_Office_Word2_1502_0(Etw):
    pattern = Struct(
        "CloseWithFindBarButton" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1503, version=0)
class Microsoft_Office_Word2_1503_0(Etw):
    pattern = Struct(
        "CSearchResults" / Int32sl,
        "fResult" / Int8ul,
        "fResultInComment" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1504, version=0)
class Microsoft_Office_Word2_1504_0(Etw):
    pattern = Struct(
        "ReplaceQueryLength" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1506, version=0)
class Microsoft_Office_Word2_1506_0(Etw):
    pattern = Struct(
        "ReplaceQueryLength" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1507, version=0)
class Microsoft_Office_Word2_1507_0(Etw):
    pattern = Struct(
        "cReplaces" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1509, version=0)
class Microsoft_Office_Word2_1509_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "fCommentsInPane" / Int8ul,
        "findReplaceMode" / Int32ul,
        "fSearchInComment" / Int8ul,
        "cHits" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=1511, version=0)
class Microsoft_Office_Word2_1511_0(Etw):
    pattern = Struct(
        "fFindInComments" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2000, version=1)
class Microsoft_Office_Word2_2000_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2001, version=1)
class Microsoft_Office_Word2_2001_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2002, version=1)
class Microsoft_Office_Word2_2002_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2003, version=1)
class Microsoft_Office_Word2_2003_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2004, version=1)
class Microsoft_Office_Word2_2004_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2005, version=1)
class Microsoft_Office_Word2_2005_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2006, version=1)
class Microsoft_Office_Word2_2006_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2007, version=1)
class Microsoft_Office_Word2_2007_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2008, version=1)
class Microsoft_Office_Word2_2008_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2009, version=1)
class Microsoft_Office_Word2_2009_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2010, version=1)
class Microsoft_Office_Word2_2010_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2011, version=1)
class Microsoft_Office_Word2_2011_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2012, version=1)
class Microsoft_Office_Word2_2012_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2013, version=1)
class Microsoft_Office_Word2_2013_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2014, version=1)
class Microsoft_Office_Word2_2014_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2015, version=1)
class Microsoft_Office_Word2_2015_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2016, version=1)
class Microsoft_Office_Word2_2016_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2017, version=1)
class Microsoft_Office_Word2_2017_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2018, version=1)
class Microsoft_Office_Word2_2018_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2019, version=1)
class Microsoft_Office_Word2_2019_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2020, version=1)
class Microsoft_Office_Word2_2020_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2021, version=1)
class Microsoft_Office_Word2_2021_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2022, version=1)
class Microsoft_Office_Word2_2022_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2023, version=1)
class Microsoft_Office_Word2_2023_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2024, version=1)
class Microsoft_Office_Word2_2024_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2025, version=1)
class Microsoft_Office_Word2_2025_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2026, version=1)
class Microsoft_Office_Word2_2026_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2027, version=1)
class Microsoft_Office_Word2_2027_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2028, version=1)
class Microsoft_Office_Word2_2028_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2029, version=1)
class Microsoft_Office_Word2_2029_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2030, version=1)
class Microsoft_Office_Word2_2030_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2031, version=1)
class Microsoft_Office_Word2_2031_1(Etw):
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


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2032, version=0)
class Microsoft_Office_Word2_2032_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2033, version=0)
class Microsoft_Office_Word2_2033_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2034, version=0)
class Microsoft_Office_Word2_2034_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2035, version=0)
class Microsoft_Office_Word2_2035_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2036, version=0)
class Microsoft_Office_Word2_2036_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2037, version=0)
class Microsoft_Office_Word2_2037_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2038, version=0)
class Microsoft_Office_Word2_2038_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2039, version=0)
class Microsoft_Office_Word2_2039_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2040, version=0)
class Microsoft_Office_Word2_2040_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2041, version=0)
class Microsoft_Office_Word2_2041_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2042, version=0)
class Microsoft_Office_Word2_2042_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2043, version=0)
class Microsoft_Office_Word2_2043_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2044, version=0)
class Microsoft_Office_Word2_2044_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2045, version=0)
class Microsoft_Office_Word2_2045_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2046, version=0)
class Microsoft_Office_Word2_2046_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2047, version=0)
class Microsoft_Office_Word2_2047_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2048, version=0)
class Microsoft_Office_Word2_2048_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2049, version=0)
class Microsoft_Office_Word2_2049_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2050, version=0)
class Microsoft_Office_Word2_2050_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2051, version=0)
class Microsoft_Office_Word2_2051_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2052, version=0)
class Microsoft_Office_Word2_2052_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2053, version=0)
class Microsoft_Office_Word2_2053_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2054, version=0)
class Microsoft_Office_Word2_2054_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2055, version=0)
class Microsoft_Office_Word2_2055_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2056, version=0)
class Microsoft_Office_Word2_2056_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2057, version=0)
class Microsoft_Office_Word2_2057_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2058, version=0)
class Microsoft_Office_Word2_2058_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2059, version=0)
class Microsoft_Office_Word2_2059_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2060, version=0)
class Microsoft_Office_Word2_2060_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2061, version=0)
class Microsoft_Office_Word2_2061_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2062, version=0)
class Microsoft_Office_Word2_2062_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2063, version=0)
class Microsoft_Office_Word2_2063_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2064, version=0)
class Microsoft_Office_Word2_2064_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2065, version=0)
class Microsoft_Office_Word2_2065_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2066, version=0)
class Microsoft_Office_Word2_2066_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2067, version=0)
class Microsoft_Office_Word2_2067_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2068, version=0)
class Microsoft_Office_Word2_2068_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2069, version=0)
class Microsoft_Office_Word2_2069_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2070, version=0)
class Microsoft_Office_Word2_2070_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2071, version=0)
class Microsoft_Office_Word2_2071_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2072, version=0)
class Microsoft_Office_Word2_2072_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2073, version=0)
class Microsoft_Office_Word2_2073_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2074, version=0)
class Microsoft_Office_Word2_2074_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2075, version=0)
class Microsoft_Office_Word2_2075_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2076, version=0)
class Microsoft_Office_Word2_2076_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2077, version=0)
class Microsoft_Office_Word2_2077_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2078, version=0)
class Microsoft_Office_Word2_2078_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2079, version=0)
class Microsoft_Office_Word2_2079_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2080, version=0)
class Microsoft_Office_Word2_2080_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2081, version=0)
class Microsoft_Office_Word2_2081_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2082, version=0)
class Microsoft_Office_Word2_2082_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2083, version=0)
class Microsoft_Office_Word2_2083_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2084, version=0)
class Microsoft_Office_Word2_2084_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2085, version=0)
class Microsoft_Office_Word2_2085_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2086, version=0)
class Microsoft_Office_Word2_2086_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2087, version=0)
class Microsoft_Office_Word2_2087_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2088, version=0)
class Microsoft_Office_Word2_2088_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2089, version=0)
class Microsoft_Office_Word2_2089_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2090, version=0)
class Microsoft_Office_Word2_2090_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2091, version=0)
class Microsoft_Office_Word2_2091_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2092, version=0)
class Microsoft_Office_Word2_2092_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2093, version=0)
class Microsoft_Office_Word2_2093_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2094, version=0)
class Microsoft_Office_Word2_2094_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2095, version=0)
class Microsoft_Office_Word2_2095_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2501, version=1)
class Microsoft_Office_Word2_2501_1(Etw):
    pattern = Struct(
        "zoomScrollCorrelationId" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2504, version=1)
class Microsoft_Office_Word2_2504_1(Etw):
    pattern = Struct(
        "MessageId" / Int32ul,
        "ClientType" / Int32sl,
        "AuthorId" / WString,
        "DocumentId" / Int64ul,
        "OpKind" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2505, version=3)
class Microsoft_Office_Word2_2505_3(Etw):
    pattern = Struct(
        "MessageId" / Int32ul,
        "ClientType" / Int32sl,
        "AuthorId" / WString,
        "OpResult" / Int32sl,
        "ParaID" / Int32ul,
        "OpKind" / Int32sl,
        "pdodMain" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2600, version=1)
class Microsoft_Office_Word2_2600_1(Etw):
    pattern = Struct(
        "Tag" / Int32ul,
        "pdod" / Int64ul,
        "ParaId" / Int32ul,
        "RtcOn" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2601, version=1)
class Microsoft_Office_Word2_2601_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "ParaId" / Int32ul,
        "AnalyzeAndDoResult" / Int32sl,
        "AnalyzeAndDoResultString" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2602, version=0)
class Microsoft_Office_Word2_2602_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2603, version=0)
class Microsoft_Office_Word2_2603_0(Etw):
    pattern = Struct(
        "cParasReverted" / Int32ul,
        "cCpTraversed" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2604, version=0)
class Microsoft_Office_Word2_2604_0(Etw):
    pattern = Struct(
        "MessageId" / Int32ul,
        "AuthorId" / WString,
        "DocumentId" / Int64ul,
        "SelType" / Int32ul,
        "ParaId" / Int32ul,
        "TextId" / Int32ul,
        "CaretPos" / Int32ul,
        "pdod" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2605, version=1)
class Microsoft_Office_Word2_2605_1(Etw):
    pattern = Struct(
        "MessageId" / Int32ul,
        "AuthorId" / WString,
        "fSetPresence" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2606, version=0)
class Microsoft_Office_Word2_2606_0(Etw):
    pattern = Struct(
        "RbodQueueSize" / Int32ul,
        "fReplay" / Int8ul,
        "fUnpause" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2607, version=0)
class Microsoft_Office_Word2_2607_0(Etw):
    pattern = Struct(
        "CountRbodProccessed" / Int32ul,
        "fRet" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2609, version=1)
class Microsoft_Office_Word2_2609_1(Etw):
    pattern = Struct(
        "GuidFileId" / Guid,
        "pdod" / Int64ul,
        "pIRtcConnection" / Int64ul,
        "pioldoc" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2610, version=1)
class Microsoft_Office_Word2_2610_1(Etw):
    pattern = Struct(
        "GuidFileId" / Guid,
        "pIRtcConnection" / Int64ul,
        "DusecEffectiveRTCSessionDuration" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2611, version=0)
class Microsoft_Office_Word2_2611_0(Etw):
    pattern = Struct(
        "MessageId" / Int32ul,
        "AuthorId" / WString,
        "DocumentId" / Int64ul,
        "OpKind" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2613, version=1)
class Microsoft_Office_Word2_2613_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "fPlayUnpausedDocument" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2615, version=0)
class Microsoft_Office_Word2_2615_0(Etw):
    pattern = Struct(
        "actt" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2616, version=0)
class Microsoft_Office_Word2_2616_0(Etw):
    pattern = Struct(
        "pdodMain" / Int64ul,
        "dusecAliveTime" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2617, version=0)
class Microsoft_Office_Word2_2617_0(Etw):
    pattern = Struct(
        "pdodMain" / Int64ul,
        "dusecDeadTime" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2618, version=0)
class Microsoft_Office_Word2_2618_0(Etw):
    pattern = Struct(
        "fSpec" / Int8ul,
        "xchSpec" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2619, version=0)
class Microsoft_Office_Word2_2619_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "ibstshort" / Int32sl,
        "fBroken" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2620, version=0)
class Microsoft_Office_Word2_2620_0(Etw):
    pattern = Struct(
        "fStart" / Int8ul,
        "fCanRtc" / Int8ul,
        "fAlwaysSaveActivated" / Int8ul,
        "HR" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2621, version=1)
class Microsoft_Office_Word2_2621_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "pcoa" / Int64ul,
        "Automatic" / Int8ul,
        "OptInSource" / Int32sl,
        "Response" / Int8ul,
        "AlwaysAsk" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2622, version=0)
class Microsoft_Office_Word2_2622_0(Etw):
    pattern = Struct(
        "Bssck" / Int32sl,
        "count" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2623, version=0)
class Microsoft_Office_Word2_2623_0(Etw):
    pattern = Struct(
        "cpIn" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2624, version=0)
class Microsoft_Office_Word2_2624_0(Etw):
    pattern = Struct(
        "cpOut" / Int32sl,
        "cFetch" / Int32sl,
        "scps" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2625, version=0)
class Microsoft_Office_Word2_2625_0(Etw):
    pattern = Struct(
        "cpIn" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2626, version=0)
class Microsoft_Office_Word2_2626_0(Etw):
    pattern = Struct(
        "cpOut" / Int32sl,
        "cFetch" / Int32sl,
        "scps" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2628, version=0)
class Microsoft_Office_Word2_2628_0(Etw):
    pattern = Struct(
        "Tag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2629, version=0)
class Microsoft_Office_Word2_2629_0(Etw):
    pattern = Struct(
        "pthis" / Int64ul,
        "pdodMain" / Int64ul,
        "pdod" / Int64ul,
        "cpFirst" / Int32sl,
        "cpLim" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2630, version=0)
class Microsoft_Office_Word2_2630_0(Etw):
    pattern = Struct(
        "pthis" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2631, version=0)
class Microsoft_Office_Word2_2631_0(Etw):
    pattern = Struct(
        "cParasDeleted" / Int64ul,
        "cParasDelMax" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2632, version=0)
class Microsoft_Office_Word2_2632_0(Etw):
    pattern = Struct(
        "FirstReason" / Int32sl,
        "GrfReasons" / Int64ul,
        "pdod" / Int64ul,
        "cpFirstOld" / Int32sl,
        "cpLimOld" / Int32sl,
        "cpFirstNew" / Int32sl,
        "cpLimNew" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2633, version=0)
class Microsoft_Office_Word2_2633_0(Etw):
    pattern = Struct(
        "GuidFileId" / Guid,
        "pdod" / Int64ul,
        "pcoa" / Int64ul,
        "pIRtcConnection" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2634, version=1)
class Microsoft_Office_Word2_2634_1(Etw):
    pattern = Struct(
        "pcoa" / Int64ul,
        "pIRtcConnection" / Int64ul,
        "DusecRTCContentHandlerDuration" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2635, version=0)
class Microsoft_Office_Word2_2635_0(Etw):
    pattern = Struct(
        "pdodMain" / Int64ul,
        "dusecAliveTime" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2636, version=0)
class Microsoft_Office_Word2_2636_0(Etw):
    pattern = Struct(
        "pdodMain" / Int64ul,
        "dusecDeadTime" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2637, version=0)
class Microsoft_Office_Word2_2637_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2638, version=0)
class Microsoft_Office_Word2_2638_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2639, version=0)
class Microsoft_Office_Word2_2639_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "ClientType" / Int32sl,
        "fPresence" / Int8ul,
        "cReceived" / Int64ul,
        "cLost" / Int64ul,
        "cUnordered" / Int64ul,
        "cDelayedStart" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2640, version=2)
class Microsoft_Office_Word2_2640_2(Etw):
    pattern = Struct(
        "fAlive" / Int8ul,
        "DeadReason" / Int32sl,
        "pdod" / Int64ul,
        "pdodMain" / Int64ul,
        "paraid" / Int32ul,
        "dusecAliveDeadTime" / Int64ul,
        "InitialOpResult" / Int32sl,
        "InitialOpKind" / Int32sl,
        "InitialClientType" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2641, version=0)
class Microsoft_Office_Word2_2641_0(Etw):
    pattern = Struct(
        "RbodIdentifier" / WString,
        "OpKind" / Int32sl,
        "MessageId" / Int32ul,
        "usecCreateTime" / Int64ul,
        "usecInsertTime" / Int64ul,
        "usecCoalesceTime" / Int64ul,
        "usecSerializeTime" / Int64ul,
        "usecBroadcastTime" / Int64ul,
        "dusecCreateToBroadcastTime" / Int64ul,
        "usecAckTime" / Int64ul,
        "dusecRoundtripTime" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2642, version=0)
class Microsoft_Office_Word2_2642_0(Etw):
    pattern = Struct(
        "RbodIdentifier" / WString,
        "OpKind" / Int32sl,
        "MessageId" / Int32ul,
        "usecCreateTime" / Int64ul,
        "usecInsertTime" / Int64ul,
        "usecProcessAllRbodsTime" / Int64ul,
        "usecRorDoIfPossibleTime" / Int64ul,
        "dusecReceiveToPlayTime" / Int64ul,
        "OpResult" / Int32sl,
        "Paused" / Int8ul,
        "UnderPauseEffect" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2643, version=0)
class Microsoft_Office_Word2_2643_0(Etw):
    pattern = Struct(
        "FeatureGateOn" / Int8ul,
        "pdodMain" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2644, version=0)
class Microsoft_Office_Word2_2644_0(Etw):
    pattern = Struct(
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2645, version=0)
class Microsoft_Office_Word2_2645_0(Etw):
    pattern = Struct(
        "PresenceTextType" / Int32ul,
        "AggregationHelper" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2646, version=0)
class Microsoft_Office_Word2_2646_0(Etw):
    pattern = Struct(
        "UnknownEditorTime" / Int32ul,
        "fNeverKnown" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2650, version=0)
class Microsoft_Office_Word2_2650_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2651, version=0)
class Microsoft_Office_Word2_2651_0(Etw):
    pattern = Struct(
        "GuidFileId" / Guid,
        "ParaId" / Int32ul,
        "cParaIds" / Int32ul,
        "cSequence" / Int32ul,
        "cUnordered" / Int32ul,
        "cLost" / Int32ul,
        "usecInBuffer" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2652, version=0)
class Microsoft_Office_Word2_2652_0(Etw):
    pattern = Struct(
        "GuidFileId" / Guid,
        "ParaId" / Int32ul,
        "cParaIds" / Int32ul,
        "cSequence" / Int32ul,
        "cUnordered" / Int32ul,
        "cLost" / Int32ul,
        "usecInBuffer" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2653, version=0)
class Microsoft_Office_Word2_2653_0(Etw):
    pattern = Struct(
        "GuidFileId" / Guid,
        "ParaId" / Int32ul,
        "cParaIds" / Int32ul,
        "cSequence" / Int32ul,
        "cUnorderedResolved" / Int32ul,
        "cLost" / Int32ul,
        "usecInBuffer" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2654, version=0)
class Microsoft_Office_Word2_2654_0(Etw):
    pattern = Struct(
        "GuidFileId" / Guid,
        "ParaId" / Int32ul,
        "drwmidss" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2900, version=0)
class Microsoft_Office_Word2_2900_0(Etw):
    pattern = Struct(
        "TagCaller" / Int32ul,
        "pdod" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2901, version=0)
class Microsoft_Office_Word2_2901_0(Etw):
    pattern = Struct(
        "NoProofRegion" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2902, version=0)
class Microsoft_Office_Word2_2902_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "lang" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2903, version=0)
class Microsoft_Office_Word2_2903_0(Etw):
    pattern = Struct(
        "Lid" / Int16ul,
        "fIsDifferentLangSelected" / Int8ul,
        "fIsNoProofChecked" / Int8ul,
        "fIsAutoDetectUnchecked" / Int8ul,
        "fIsSetDefaultPressed" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2904, version=0)
class Microsoft_Office_Word2_2904_0(Etw):
    pattern = Struct(
        "ETW_TrackbackTag" / Int32ul,
        "pdod" / Int64ul,
        "cp" / Int32sl,
        "itap" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2905, version=0)
class Microsoft_Office_Word2_2905_0(Etw):
    pattern = Struct(
        "ETW_TrackbackTag" / Int32ul,
        "pdod" / Int64ul,
        "cp" / Int32sl,
        "itap" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2906, version=0)
class Microsoft_Office_Word2_2906_0(Etw):
    pattern = Struct(
        "fVisible" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2907, version=0)
class Microsoft_Office_Word2_2907_0(Etw):
    pattern = Struct(
        "fMoving" / Int8ul,
        "xPos" / Double,
        "yPos" / Double,
        "xMaxOffset" / Double,
        "yMaxOffset" / Double,
        "xZoom" / Double,
        "yZoom" / Double
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2908, version=0)
class Microsoft_Office_Word2_2908_0(Etw):
    pattern = Struct(
        "fVisible" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2909, version=0)
class Microsoft_Office_Word2_2909_0(Etw):
    pattern = Struct(
        "XszName" / WString,
        "XszPayload" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2910, version=0)
class Microsoft_Office_Word2_2910_0(Etw):
    pattern = Struct(
        "dwTag" / Int32ul,
        "pdod" / Int64ul,
        "wkViewKind" / Int32ul,
        "fIsMotherWwd" / Int8ul,
        "fInListWwd" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2911, version=0)
class Microsoft_Office_Word2_2911_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "lTagBkmk" / Int64ul,
        "fHasAtMention" / Int8ul,
        "fCommentSelChangeFG" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=2912, version=0)
class Microsoft_Office_Word2_2912_0(Etw):
    pattern = Struct(
        "fGlobalDotMatchesDefault" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=3000, version=0)
class Microsoft_Office_Word2_3000_0(Etw):
    pattern = Struct(
        "Device" / WString,
        "Mode" / Int32ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=3001, version=0)
class Microsoft_Office_Word2_3001_0(Etw):
    pattern = Struct(
        "Devmode" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=3002, version=0)
class Microsoft_Office_Word2_3002_0(Etw):
    pattern = Struct(
        "Devmode" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=3003, version=0)
class Microsoft_Office_Word2_3003_0(Etw):
    pattern = Struct(
        "ReturnValue" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=3004, version=0)
class Microsoft_Office_Word2_3004_0(Etw):
    pattern = Struct(
        "ReturnValue" / Int32sl,
        "Index" / Int32sl,
        "DC" / Int64ul,
        "fError" / Int8ul,
        "fFaking" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=3005, version=0)
class Microsoft_Office_Word2_3005_0(Etw):
    pattern = Struct(
        "RetVal" / Int8ul,
        "Printer" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=3006, version=0)
class Microsoft_Office_Word2_3006_0(Etw):
    pattern = Struct(
        "fQuery" / Int8ul,
        "fFakePrinterNameOK" / Int8ul,
        "fHaveDefaultPrinterName" / Int8ul,
        "fEmptyPrinterName" / Int8ul,
        "RetVal" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=3008, version=0)
class Microsoft_Office_Word2_3008_0(Etw):
    pattern = Struct(
        "Driver" / WString,
        "Device" / WString,
        "Port" / WString,
        "Devmode" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=3009, version=0)
class Microsoft_Office_Word2_3009_0(Etw):
    pattern = Struct(
        "RetVal" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=3010, version=0)
class Microsoft_Office_Word2_3010_0(Etw):
    pattern = Struct(
        "DCIn" / Int64ul,
        "Devmode" / WString,
        "DCOut" / Int64ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=3011, version=0)
class Microsoft_Office_Word2_3011_0(Etw):
    pattern = Struct(
        "DC" / Int64ul,
        "RetVal" / Int8ul
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=3013, version=0)
class Microsoft_Office_Word2_3013_0(Etw):
    pattern = Struct(
        "Printer" / WString,
        "Index" / Int32ul,
        "fOutput" / Int8ul,
        "fDevmode" / Int8ul,
        "ReturnValue" / Int32sl
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=3015, version=0)
class Microsoft_Office_Word2_3015_0(Etw):
    pattern = Struct(
        "Printer" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30291, version=1)
class Microsoft_Office_Word2_30291_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30292, version=1)
class Microsoft_Office_Word2_30292_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30293, version=1)
class Microsoft_Office_Word2_30293_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30294, version=1)
class Microsoft_Office_Word2_30294_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30295, version=1)
class Microsoft_Office_Word2_30295_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30296, version=1)
class Microsoft_Office_Word2_30296_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30297, version=1)
class Microsoft_Office_Word2_30297_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30298, version=1)
class Microsoft_Office_Word2_30298_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30299, version=1)
class Microsoft_Office_Word2_30299_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30300, version=1)
class Microsoft_Office_Word2_30300_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30301, version=1)
class Microsoft_Office_Word2_30301_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30302, version=1)
class Microsoft_Office_Word2_30302_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30303, version=1)
class Microsoft_Office_Word2_30303_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30304, version=1)
class Microsoft_Office_Word2_30304_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30305, version=1)
class Microsoft_Office_Word2_30305_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30306, version=1)
class Microsoft_Office_Word2_30306_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30307, version=1)
class Microsoft_Office_Word2_30307_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30308, version=1)
class Microsoft_Office_Word2_30308_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30309, version=1)
class Microsoft_Office_Word2_30309_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30310, version=1)
class Microsoft_Office_Word2_30310_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30311, version=1)
class Microsoft_Office_Word2_30311_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30312, version=1)
class Microsoft_Office_Word2_30312_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30313, version=1)
class Microsoft_Office_Word2_30313_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30314, version=1)
class Microsoft_Office_Word2_30314_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30315, version=1)
class Microsoft_Office_Word2_30315_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30316, version=1)
class Microsoft_Office_Word2_30316_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30317, version=1)
class Microsoft_Office_Word2_30317_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30318, version=1)
class Microsoft_Office_Word2_30318_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30319, version=1)
class Microsoft_Office_Word2_30319_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30320, version=1)
class Microsoft_Office_Word2_30320_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30321, version=1)
class Microsoft_Office_Word2_30321_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30322, version=1)
class Microsoft_Office_Word2_30322_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30323, version=1)
class Microsoft_Office_Word2_30323_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30324, version=1)
class Microsoft_Office_Word2_30324_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30325, version=1)
class Microsoft_Office_Word2_30325_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30326, version=1)
class Microsoft_Office_Word2_30326_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30327, version=1)
class Microsoft_Office_Word2_30327_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30328, version=1)
class Microsoft_Office_Word2_30328_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30329, version=1)
class Microsoft_Office_Word2_30329_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30330, version=1)
class Microsoft_Office_Word2_30330_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30331, version=1)
class Microsoft_Office_Word2_30331_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30332, version=1)
class Microsoft_Office_Word2_30332_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30333, version=1)
class Microsoft_Office_Word2_30333_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30334, version=1)
class Microsoft_Office_Word2_30334_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30335, version=1)
class Microsoft_Office_Word2_30335_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30336, version=1)
class Microsoft_Office_Word2_30336_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30337, version=1)
class Microsoft_Office_Word2_30337_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30338, version=1)
class Microsoft_Office_Word2_30338_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30339, version=1)
class Microsoft_Office_Word2_30339_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30340, version=1)
class Microsoft_Office_Word2_30340_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30341, version=1)
class Microsoft_Office_Word2_30341_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30342, version=1)
class Microsoft_Office_Word2_30342_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30343, version=1)
class Microsoft_Office_Word2_30343_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30344, version=1)
class Microsoft_Office_Word2_30344_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30345, version=1)
class Microsoft_Office_Word2_30345_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30346, version=1)
class Microsoft_Office_Word2_30346_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30347, version=1)
class Microsoft_Office_Word2_30347_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30348, version=1)
class Microsoft_Office_Word2_30348_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30349, version=1)
class Microsoft_Office_Word2_30349_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30350, version=1)
class Microsoft_Office_Word2_30350_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30351, version=1)
class Microsoft_Office_Word2_30351_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30352, version=1)
class Microsoft_Office_Word2_30352_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30353, version=1)
class Microsoft_Office_Word2_30353_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30354, version=1)
class Microsoft_Office_Word2_30354_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30355, version=1)
class Microsoft_Office_Word2_30355_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30356, version=1)
class Microsoft_Office_Word2_30356_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30357, version=1)
class Microsoft_Office_Word2_30357_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30358, version=1)
class Microsoft_Office_Word2_30358_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30359, version=1)
class Microsoft_Office_Word2_30359_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30360, version=1)
class Microsoft_Office_Word2_30360_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30361, version=1)
class Microsoft_Office_Word2_30361_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30362, version=1)
class Microsoft_Office_Word2_30362_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30363, version=1)
class Microsoft_Office_Word2_30363_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30364, version=1)
class Microsoft_Office_Word2_30364_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30365, version=1)
class Microsoft_Office_Word2_30365_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30366, version=1)
class Microsoft_Office_Word2_30366_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30367, version=1)
class Microsoft_Office_Word2_30367_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30368, version=1)
class Microsoft_Office_Word2_30368_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30369, version=1)
class Microsoft_Office_Word2_30369_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30370, version=1)
class Microsoft_Office_Word2_30370_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30371, version=1)
class Microsoft_Office_Word2_30371_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30372, version=1)
class Microsoft_Office_Word2_30372_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30373, version=1)
class Microsoft_Office_Word2_30373_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30374, version=1)
class Microsoft_Office_Word2_30374_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30375, version=1)
class Microsoft_Office_Word2_30375_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30376, version=1)
class Microsoft_Office_Word2_30376_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30377, version=1)
class Microsoft_Office_Word2_30377_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30378, version=1)
class Microsoft_Office_Word2_30378_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30379, version=1)
class Microsoft_Office_Word2_30379_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30380, version=1)
class Microsoft_Office_Word2_30380_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30381, version=1)
class Microsoft_Office_Word2_30381_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30382, version=1)
class Microsoft_Office_Word2_30382_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30383, version=1)
class Microsoft_Office_Word2_30383_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30384, version=1)
class Microsoft_Office_Word2_30384_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30385, version=1)
class Microsoft_Office_Word2_30385_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30386, version=1)
class Microsoft_Office_Word2_30386_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30387, version=1)
class Microsoft_Office_Word2_30387_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30388, version=1)
class Microsoft_Office_Word2_30388_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30389, version=1)
class Microsoft_Office_Word2_30389_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30390, version=1)
class Microsoft_Office_Word2_30390_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30391, version=1)
class Microsoft_Office_Word2_30391_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30392, version=1)
class Microsoft_Office_Word2_30392_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30393, version=1)
class Microsoft_Office_Word2_30393_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30394, version=1)
class Microsoft_Office_Word2_30394_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30395, version=1)
class Microsoft_Office_Word2_30395_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30396, version=1)
class Microsoft_Office_Word2_30396_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30397, version=1)
class Microsoft_Office_Word2_30397_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30398, version=1)
class Microsoft_Office_Word2_30398_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30399, version=1)
class Microsoft_Office_Word2_30399_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30400, version=1)
class Microsoft_Office_Word2_30400_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30401, version=1)
class Microsoft_Office_Word2_30401_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30402, version=1)
class Microsoft_Office_Word2_30402_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30403, version=1)
class Microsoft_Office_Word2_30403_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30404, version=1)
class Microsoft_Office_Word2_30404_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30405, version=1)
class Microsoft_Office_Word2_30405_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30406, version=1)
class Microsoft_Office_Word2_30406_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30407, version=1)
class Microsoft_Office_Word2_30407_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30408, version=1)
class Microsoft_Office_Word2_30408_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30409, version=1)
class Microsoft_Office_Word2_30409_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30410, version=1)
class Microsoft_Office_Word2_30410_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30411, version=1)
class Microsoft_Office_Word2_30411_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30412, version=1)
class Microsoft_Office_Word2_30412_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30413, version=1)
class Microsoft_Office_Word2_30413_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30414, version=1)
class Microsoft_Office_Word2_30414_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30415, version=1)
class Microsoft_Office_Word2_30415_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30416, version=1)
class Microsoft_Office_Word2_30416_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30417, version=1)
class Microsoft_Office_Word2_30417_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30418, version=1)
class Microsoft_Office_Word2_30418_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30419, version=1)
class Microsoft_Office_Word2_30419_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30420, version=1)
class Microsoft_Office_Word2_30420_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30421, version=1)
class Microsoft_Office_Word2_30421_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30422, version=1)
class Microsoft_Office_Word2_30422_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30423, version=1)
class Microsoft_Office_Word2_30423_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30424, version=1)
class Microsoft_Office_Word2_30424_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30425, version=1)
class Microsoft_Office_Word2_30425_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30426, version=1)
class Microsoft_Office_Word2_30426_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30427, version=1)
class Microsoft_Office_Word2_30427_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30428, version=1)
class Microsoft_Office_Word2_30428_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30429, version=1)
class Microsoft_Office_Word2_30429_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30430, version=1)
class Microsoft_Office_Word2_30430_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30431, version=1)
class Microsoft_Office_Word2_30431_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30432, version=1)
class Microsoft_Office_Word2_30432_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30433, version=1)
class Microsoft_Office_Word2_30433_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30434, version=1)
class Microsoft_Office_Word2_30434_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30435, version=1)
class Microsoft_Office_Word2_30435_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30436, version=1)
class Microsoft_Office_Word2_30436_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30437, version=1)
class Microsoft_Office_Word2_30437_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30438, version=1)
class Microsoft_Office_Word2_30438_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30439, version=1)
class Microsoft_Office_Word2_30439_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30440, version=1)
class Microsoft_Office_Word2_30440_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30441, version=1)
class Microsoft_Office_Word2_30441_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30442, version=1)
class Microsoft_Office_Word2_30442_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30443, version=1)
class Microsoft_Office_Word2_30443_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30444, version=1)
class Microsoft_Office_Word2_30444_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30445, version=1)
class Microsoft_Office_Word2_30445_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30446, version=1)
class Microsoft_Office_Word2_30446_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30447, version=1)
class Microsoft_Office_Word2_30447_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30448, version=1)
class Microsoft_Office_Word2_30448_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30449, version=1)
class Microsoft_Office_Word2_30449_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30450, version=1)
class Microsoft_Office_Word2_30450_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30451, version=1)
class Microsoft_Office_Word2_30451_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30452, version=1)
class Microsoft_Office_Word2_30452_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30453, version=1)
class Microsoft_Office_Word2_30453_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30454, version=1)
class Microsoft_Office_Word2_30454_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30455, version=1)
class Microsoft_Office_Word2_30455_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30456, version=1)
class Microsoft_Office_Word2_30456_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30457, version=1)
class Microsoft_Office_Word2_30457_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30458, version=1)
class Microsoft_Office_Word2_30458_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30459, version=1)
class Microsoft_Office_Word2_30459_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30460, version=1)
class Microsoft_Office_Word2_30460_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30461, version=1)
class Microsoft_Office_Word2_30461_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30462, version=1)
class Microsoft_Office_Word2_30462_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30463, version=1)
class Microsoft_Office_Word2_30463_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30464, version=1)
class Microsoft_Office_Word2_30464_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30465, version=1)
class Microsoft_Office_Word2_30465_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30466, version=1)
class Microsoft_Office_Word2_30466_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30467, version=1)
class Microsoft_Office_Word2_30467_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30468, version=1)
class Microsoft_Office_Word2_30468_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30469, version=1)
class Microsoft_Office_Word2_30469_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30470, version=1)
class Microsoft_Office_Word2_30470_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30471, version=1)
class Microsoft_Office_Word2_30471_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30472, version=1)
class Microsoft_Office_Word2_30472_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30473, version=1)
class Microsoft_Office_Word2_30473_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30474, version=1)
class Microsoft_Office_Word2_30474_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30475, version=1)
class Microsoft_Office_Word2_30475_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30476, version=1)
class Microsoft_Office_Word2_30476_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30477, version=1)
class Microsoft_Office_Word2_30477_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30478, version=1)
class Microsoft_Office_Word2_30478_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30479, version=1)
class Microsoft_Office_Word2_30479_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30480, version=1)
class Microsoft_Office_Word2_30480_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30481, version=1)
class Microsoft_Office_Word2_30481_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30482, version=1)
class Microsoft_Office_Word2_30482_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30483, version=1)
class Microsoft_Office_Word2_30483_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30484, version=1)
class Microsoft_Office_Word2_30484_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30485, version=1)
class Microsoft_Office_Word2_30485_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30486, version=1)
class Microsoft_Office_Word2_30486_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30487, version=1)
class Microsoft_Office_Word2_30487_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30488, version=1)
class Microsoft_Office_Word2_30488_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30489, version=1)
class Microsoft_Office_Word2_30489_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30490, version=1)
class Microsoft_Office_Word2_30490_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30491, version=1)
class Microsoft_Office_Word2_30491_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30492, version=1)
class Microsoft_Office_Word2_30492_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30493, version=1)
class Microsoft_Office_Word2_30493_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30494, version=1)
class Microsoft_Office_Word2_30494_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30495, version=1)
class Microsoft_Office_Word2_30495_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30496, version=1)
class Microsoft_Office_Word2_30496_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30497, version=1)
class Microsoft_Office_Word2_30497_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30498, version=1)
class Microsoft_Office_Word2_30498_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30499, version=1)
class Microsoft_Office_Word2_30499_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30500, version=1)
class Microsoft_Office_Word2_30500_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30501, version=1)
class Microsoft_Office_Word2_30501_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30502, version=1)
class Microsoft_Office_Word2_30502_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30503, version=1)
class Microsoft_Office_Word2_30503_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30504, version=1)
class Microsoft_Office_Word2_30504_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30505, version=1)
class Microsoft_Office_Word2_30505_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30506, version=1)
class Microsoft_Office_Word2_30506_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30507, version=1)
class Microsoft_Office_Word2_30507_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30508, version=1)
class Microsoft_Office_Word2_30508_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30509, version=1)
class Microsoft_Office_Word2_30509_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30510, version=1)
class Microsoft_Office_Word2_30510_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30511, version=1)
class Microsoft_Office_Word2_30511_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30512, version=1)
class Microsoft_Office_Word2_30512_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30513, version=1)
class Microsoft_Office_Word2_30513_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30514, version=1)
class Microsoft_Office_Word2_30514_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30515, version=1)
class Microsoft_Office_Word2_30515_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30516, version=1)
class Microsoft_Office_Word2_30516_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30517, version=1)
class Microsoft_Office_Word2_30517_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30518, version=1)
class Microsoft_Office_Word2_30518_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30519, version=1)
class Microsoft_Office_Word2_30519_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30520, version=1)
class Microsoft_Office_Word2_30520_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30521, version=1)
class Microsoft_Office_Word2_30521_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30522, version=1)
class Microsoft_Office_Word2_30522_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30523, version=1)
class Microsoft_Office_Word2_30523_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30524, version=1)
class Microsoft_Office_Word2_30524_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30525, version=1)
class Microsoft_Office_Word2_30525_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30526, version=1)
class Microsoft_Office_Word2_30526_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30527, version=1)
class Microsoft_Office_Word2_30527_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30528, version=1)
class Microsoft_Office_Word2_30528_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30529, version=1)
class Microsoft_Office_Word2_30529_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30530, version=1)
class Microsoft_Office_Word2_30530_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30531, version=1)
class Microsoft_Office_Word2_30531_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30532, version=1)
class Microsoft_Office_Word2_30532_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30533, version=1)
class Microsoft_Office_Word2_30533_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30534, version=1)
class Microsoft_Office_Word2_30534_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30535, version=1)
class Microsoft_Office_Word2_30535_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30536, version=1)
class Microsoft_Office_Word2_30536_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30537, version=1)
class Microsoft_Office_Word2_30537_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30538, version=1)
class Microsoft_Office_Word2_30538_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30539, version=1)
class Microsoft_Office_Word2_30539_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30540, version=1)
class Microsoft_Office_Word2_30540_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30541, version=1)
class Microsoft_Office_Word2_30541_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30542, version=1)
class Microsoft_Office_Word2_30542_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30543, version=1)
class Microsoft_Office_Word2_30543_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30544, version=1)
class Microsoft_Office_Word2_30544_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30545, version=1)
class Microsoft_Office_Word2_30545_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30546, version=1)
class Microsoft_Office_Word2_30546_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30547, version=1)
class Microsoft_Office_Word2_30547_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30548, version=1)
class Microsoft_Office_Word2_30548_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30549, version=1)
class Microsoft_Office_Word2_30549_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30550, version=1)
class Microsoft_Office_Word2_30550_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30551, version=1)
class Microsoft_Office_Word2_30551_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30552, version=1)
class Microsoft_Office_Word2_30552_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30553, version=1)
class Microsoft_Office_Word2_30553_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30554, version=1)
class Microsoft_Office_Word2_30554_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30555, version=1)
class Microsoft_Office_Word2_30555_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30556, version=1)
class Microsoft_Office_Word2_30556_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30557, version=1)
class Microsoft_Office_Word2_30557_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30558, version=1)
class Microsoft_Office_Word2_30558_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30559, version=1)
class Microsoft_Office_Word2_30559_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30560, version=1)
class Microsoft_Office_Word2_30560_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30561, version=1)
class Microsoft_Office_Word2_30561_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30562, version=1)
class Microsoft_Office_Word2_30562_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30563, version=1)
class Microsoft_Office_Word2_30563_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30564, version=1)
class Microsoft_Office_Word2_30564_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30565, version=1)
class Microsoft_Office_Word2_30565_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30566, version=1)
class Microsoft_Office_Word2_30566_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30567, version=1)
class Microsoft_Office_Word2_30567_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30568, version=1)
class Microsoft_Office_Word2_30568_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30569, version=1)
class Microsoft_Office_Word2_30569_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30570, version=1)
class Microsoft_Office_Word2_30570_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30571, version=1)
class Microsoft_Office_Word2_30571_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30572, version=1)
class Microsoft_Office_Word2_30572_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30573, version=1)
class Microsoft_Office_Word2_30573_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30574, version=1)
class Microsoft_Office_Word2_30574_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30575, version=1)
class Microsoft_Office_Word2_30575_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30576, version=1)
class Microsoft_Office_Word2_30576_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30577, version=1)
class Microsoft_Office_Word2_30577_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("bb00e856-a12f-4ab7-b2c8-4e80caea5b07"), event_id=30578, version=1)
class Microsoft_Office_Word2_30578_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )

