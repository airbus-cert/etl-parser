# -*- coding: utf-8 -*-
"""
Microsoft-Office-Word3
GUID : a1b69d49-2195-4f59-9d33-bdf30c0fe473
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2, version=0)
class Microsoft_Office_Word3_2_0(Etw):
    pattern = Struct(
        "receivingClientVclokId" / Guid,
        "sendingClientVclokId" / Guid,
        "sendingClientVclokValue" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=4, version=1)
class Microsoft_Office_Word3_4_1(Etw):
    pattern = Struct(
        "savingClientVclokId" / Guid,
        "savingClientVclokValueMin" / Int32ul,
        "savingClientVclokValueMax" / Int32ul,
        "uploadDuration" / Int64ul,
        "editToUploadTimeMicroseconds" / Int64ul,
        "rtcBrkEditToUploadTimeMicroseconds" / Int64ul,
        "saveToUploadInitTimeMicroseconds" / Int64ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=15, version=0)
class Microsoft_Office_Word3_15_0(Etw):
    pattern = Struct(
        "DismissalReason" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=18, version=0)
class Microsoft_Office_Word3_18_0(Etw):
    pattern = Struct(
        "fDocHasFormsField" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=19, version=0)
class Microsoft_Office_Word3_19_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "diReason" / Int16ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=20, version=1)
class Microsoft_Office_Word3_20_1(Etw):
    pattern = Struct(
        "pwwd" / Int64ul,
        "pdod" / Int64ul,
        "dk" / WString,
        "cpFirst" / Int32sl,
        "cpLim" / Int32sl,
        "grftr" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=21, version=0)
class Microsoft_Office_Word3_21_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "dk" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=22, version=0)
class Microsoft_Office_Word3_22_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "dk" / WString,
        "cpFirst" / Int32sl,
        "dcp" / Int32sl,
        "grfef_low" / Int32ul,
        "grfef_high" / Int32ul,
        "grfef2_low" / Int32ul,
        "grfef2_high" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=23, version=0)
class Microsoft_Office_Word3_23_0(Etw):
    pattern = Struct(
        "drk" / WString,
        "BoundingBox" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=24, version=0)
class Microsoft_Office_Word3_24_0(Etw):
    pattern = Struct(
        "drk" / WString,
        "BoundingBox" / WString,
        "Rectangles" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=25, version=1)
class Microsoft_Office_Word3_25_1(Etw):
    pattern = Struct(
        "pwwd" / Int64ul,
        "pdod" / Int64ul,
        "dk" / WString,
        "cpFirst" / Int32sl,
        "dcp" / Int32sl,
        "fNoLayoutChange" / Int8ul,
        "fSelectionChange" / Int8ul,
        "fUpdateArtvNVersion" / Int8ul,
        "fDirtyMtxi" / Int8ul,
        "grfef_low" / Int32ul,
        "grfef_high" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=26, version=2)
class Microsoft_Office_Word3_26_2(Etw):
    pattern = Struct(
        "Tag" / Int32ul,
        "pdod" / Int64ul,
        "AutoCreateEventHandler" / Int32ul,
        "tSucceeded" / Int32sl,
        "fDocRenamed" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=27, version=2)
class Microsoft_Office_Word3_27_2(Etw):
    pattern = Struct(
        "Tag" / Int32ul,
        "pdod" / Int64ul,
        "AutoCreateEventHandler" / Int32ul,
        "tSucceeded" / Int32sl,
        "fDocRenamed" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=28, version=2)
class Microsoft_Office_Word3_28_2(Etw):
    pattern = Struct(
        "Tag" / Int32ul,
        "pdod" / Int64ul,
        "AutoCreateEventHandler" / Int32ul,
        "tSucceeded" / Int32sl,
        "fDocRenamed" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30, version=1)
class Microsoft_Office_Word3_30_1(Etw):
    pattern = Struct(
        "ReasonforConflict" / Int32ul,
        "fciUser" / Int32ul,
        "fciCoauth" / Int32ul,
        "UserCAtype" / Int32ul,
        "camoUsercp" / Int32ul,
        "camoUserdcpOld" / Int32ul,
        "camoUserdcpNew" / Int32ul,
        "camoCoauthcp" / Int32ul,
        "camoCoauthdcpOld" / Int32ul,
        "camoCoauthdcpNew" / Int32ul,
        "fUndo" / Int8ul,
        "fRepeat" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=31, version=0)
class Microsoft_Office_Word3_31_0(Etw):
    pattern = Struct(
        "ETW_TrackbackTag" / Int32ul,
        "IdomoMacUsk" / Int32ul,
        "idomoUndoLim" / Int32ul,
        "idomoRedoLim" / Int32ul,
        "idomoFirst" / Int32ul,
        "cdomo" / Int32ul,
        "UADfci" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=100, version=1)
class Microsoft_Office_Word3_100_1(Etw):
    pattern = Struct(
        "pwwd" / Int64ul,
        "fPrivateInvalRgn" / Int8ul,
        "SumofPixelCountforRects" / Int32ul,
        "BoundingBoxPixelCount" / Int32ul,
        "Rectangles" / WString,
        "BoundingBox" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=101, version=1)
class Microsoft_Office_Word3_101_1(Etw):
    pattern = Struct(
        "pwwd" / Int64ul,
        "ppr" / Int64ul,
        "grfrpu" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=102, version=1)
class Microsoft_Office_Word3_102_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "LinkedInResumeClassification" / Int32ul,
        "JobTitleMatch" / Int8ul,
        "JobCityMatch" / Int8ul,
        "JobStateMatch" / Int8ul,
        "JobZipCodeMatch" / Int8ul,
        "AuthorMatch" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=103, version=1)
class Microsoft_Office_Word3_103_1(Etw):
    pattern = Struct(
        "LinkedInUserEnabled" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=150, version=0)
class Microsoft_Office_Word3_150_0(Etw):
    pattern = Struct(
        "FlyoutType" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=151, version=0)
class Microsoft_Office_Word3_151_0(Etw):
    pattern = Struct(
        "fAppend" / Int8ul,
        "cpInsertFirst" / Int32sl,
        "cpInsertLim" / Int32sl
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=152, version=0)
class Microsoft_Office_Word3_152_0(Etw):
    pattern = Struct(
        "cpInsertFirst" / Int32sl,
        "cpInsertLim" / Int32sl
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=153, version=0)
class Microsoft_Office_Word3_153_0(Etw):
    pattern = Struct(
        "cpInsertFirst" / Int32sl,
        "cpInsertLim" / Int32sl
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=154, version=0)
class Microsoft_Office_Word3_154_0(Etw):
    pattern = Struct(
        "fRegionContainsE2O" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=200, version=1)
class Microsoft_Office_Word3_200_1(Etw):
    pattern = Struct(
        "UserInteraction" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=201, version=1)
class Microsoft_Office_Word3_201_1(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "CorrelationGuid" / Guid,
        "BlueprintsSeenJson" / WString,
        "BlueprintsTriedJson" / WString,
        "BlueprintKeptJson" / WString,
        "BlueprintsSeenCount" / Int32ul,
        "BlueprintsTriedCount" / Int32ul,
        "BlueprintWasKept" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=202, version=0)
class Microsoft_Office_Word3_202_0(Etw):
    pattern = Struct(
        "InvokeReason" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=203, version=0)
class Microsoft_Office_Word3_203_0(Etw):
    pattern = Struct(
        "BlockReason" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=250, version=0)
class Microsoft_Office_Word3_250_0(Etw):
    pattern = Struct(
        "xszText" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=351, version=0)
class Microsoft_Office_Word3_351_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "EntryType" / Int32ul,
        "ViewType" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=352, version=0)
class Microsoft_Office_Word3_352_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "ExitType" / Int32ul,
        "BackgroundColor" / Int32ul,
        "BackgroundType" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=363, version=0)
class Microsoft_Office_Word3_363_0(Etw):
    pattern = Struct(
        "NotifyUserResult" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=364, version=0)
class Microsoft_Office_Word3_364_0(Etw):
    pattern = Struct(
        "ShowNotificationResult" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=368, version=0)
class Microsoft_Office_Word3_368_0(Etw):
    pattern = Struct(
        "dwIndex" / Int32ul,
        "name" / WString,
        "dwType" / Int32ul,
        "cb" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=369, version=0)
class Microsoft_Office_Word3_369_0(Etw):
    pattern = Struct(
        "dwCValue" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=370, version=0)
class Microsoft_Office_Word3_370_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=371, version=0)
class Microsoft_Office_Word3_371_0(Etw):
    pattern = Struct(
        "GateValue" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=372, version=0)
class Microsoft_Office_Word3_372_0(Etw):
    pattern = Struct(
        "GateValue" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=373, version=0)
class Microsoft_Office_Word3_373_0(Etw):
    pattern = Struct(
        "secBootLengthThreshold" / Int32ul,
        "pctBootPercentageThreshold" / Int32ul,
        "AddinScenario" / Int32ul,
        "time" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=374, version=0)
class Microsoft_Office_Word3_374_0(Etw):
    pattern = Struct(
        "name" / WString,
        "fDisplay" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=375, version=0)
class Microsoft_Office_Word3_375_0(Etw):
    pattern = Struct(
        "name" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=377, version=1)
class Microsoft_Office_Word3_377_1(Etw):
    pattern = Struct(
        "name" / WString,
        "FIsCOMAddin" / Int8ul,
        "FIsGroupPolicyDisabled" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=378, version=0)
class Microsoft_Office_Word3_378_0(Etw):
    pattern = Struct(
        "name" / WString,
        "SelectedAction" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=379, version=0)
class Microsoft_Office_Word3_379_0(Etw):
    pattern = Struct(
        "dwConnect" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=380, version=0)
class Microsoft_Office_Word3_380_0(Etw):
    pattern = Struct(
        "dwPolicy" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=381, version=0)
class Microsoft_Office_Word3_381_0(Etw):
    pattern = Struct(
        "GateValue" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=400, version=1)
class Microsoft_Office_Word3_400_1(Etw):
    pattern = Struct(
        "cRow" / Int32sl,
        "cCol" / Int32sl,
        "fRegular" / Int8ul,
        "TableAlignmentType" / Int32sl,
        "TableDepth" / Int32sl,
        "fAutoFit" / Int8ul,
        "fBiDi" / Int8ul,
        "TableWidthType" / Int32sl,
        "TableWidthValue" / Int32sl,
        "dk" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=401, version=0)
class Microsoft_Office_Word3_401_0(Etw):
    pattern = Struct(
        "fInsEmptyTable" / Int8ul,
        "fInsTableOverWholeTable" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=402, version=1)
class Microsoft_Office_Word3_402_1(Etw):
    pattern = Struct(
        "cRowsInserted" / Int32sl,
        "fInsertedAbove" / Int8ul,
        "fInsertedBelow" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=403, version=1)
class Microsoft_Office_Word3_403_1(Etw):
    pattern = Struct(
        "cColsInserted" / Int32sl,
        "fInsertedRight" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=404, version=0)
class Microsoft_Office_Word3_404_0(Etw):
    pattern = Struct(
        "ActionPerformed" / Int32sl
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=405, version=1)
class Microsoft_Office_Word3_405_1(Etw):
    pattern = Struct(
        "fPastedIntoTable" / Int8ul,
        "msoHostID" / Int32sl,
        "pasteOptionID" / Int32sl
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=406, version=1)
class Microsoft_Office_Word3_406_1(Etw):
    pattern = Struct(
        "cRowsMerged" / Int32sl,
        "cColsMerged" / Int32sl
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=407, version=1)
class Microsoft_Office_Word3_407_1(Etw):
    pattern = Struct(
        "cRowsSplit" / Int32sl,
        "cColsSplit" / Int32sl
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=408, version=2)
class Microsoft_Office_Word3_408_2(Etw):
    pattern = Struct(
        "ibrc" / Int32sl,
        "COLORREF" / Int32sl,
        "dptLineWidth" / Int32sl,
        "brcType" / Int32sl,
        "dptSpace" / Int32sl,
        "fShadow" / Int8ul,
        "fFrame" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=409, version=2)
class Microsoft_Office_Word3_409_2(Etw):
    pattern = Struct(
        "cvFore" / Int32sl,
        "cvBack" / Int32sl,
        "ipat" / Int16ul,
        "fWholeTable" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=410, version=1)
class Microsoft_Office_Word3_410_1(Etw):
    pattern = Struct(
        "sti" / Int32sl
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=411, version=0)
class Microsoft_Office_Word3_411_0(Etw):
    pattern = Struct(
        "fHasHeaderRow" / Int8ul,
        "fHasTotalRow" / Int8ul,
        "fHasFirstColumn" / Int8ul,
        "fHasLastColumn" / Int8ul,
        "fHasBandedRows" / Int8ul,
        "fHasBandedColumns" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=413, version=1)
class Microsoft_Office_Word3_413_1(Etw):
    pattern = Struct(
        "horzAnchor" / Int32sl,
        "vertAnchor" / Int32sl,
        "dxaAbs" / Int64sl,
        "dyaAbs" / Int64sl,
        "dxaFromText" / Int64sl,
        "dyaFromText" / Int64sl,
        "dxaFromTextRight" / Int64sl,
        "dyaFromTextBottom" / Int64sl,
        "dxaIdentFromLeft" / Int64sl
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=414, version=0)
class Microsoft_Office_Word3_414_0(Etw):
    pattern = Struct(
        "fTextWrapping" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=418, version=0)
class Microsoft_Office_Word3_418_0(Etw):
    pattern = Struct(
        "fWholeTable" / Int8ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=420, version=0)
class Microsoft_Office_Word3_420_0(Etw):
    pattern = Struct(
        "identifier" / Int64ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=441, version=0)
class Microsoft_Office_Word3_441_0(Etw):
    pattern = Struct(
        "areaPoints" / Float32l
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=451, version=0)
class Microsoft_Office_Word3_451_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul,
        "fRTF" / Int8ul,
        "callType" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=461, version=0)
class Microsoft_Office_Word3_461_0(Etw):
    pattern = Struct(
        "changes" / Int64ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=462, version=0)
class Microsoft_Office_Word3_462_0(Etw):
    pattern = Struct(
        "changes" / Int64ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=463, version=0)
class Microsoft_Office_Word3_463_0(Etw):
    pattern = Struct(
        "source" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=464, version=0)
class Microsoft_Office_Word3_464_0(Etw):
    pattern = Struct(
        "property" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=472, version=0)
class Microsoft_Office_Word3_472_0(Etw):
    pattern = Struct(
        "CountOfRecipients" / Int64ul,
        "LinkPermissionType" / Int32ul,
        "CountOfRecipientsOptimizedAway" / Int64ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=481, version=0)
class Microsoft_Office_Word3_481_0(Etw):
    pattern = Struct(
        "cCsrSuccess" / Int32sl,
        "cCsrInvalidFrameCount" / Int32sl,
        "cCsrNullFunctionEntry" / Int32sl,
        "cCsrNullFunctionEntryTop" / Int32sl,
        "cCsrUnsupportedArch" / Int32sl,
        "cCsrInvalidThread" / Int32sl,
        "cCsrSampleContention" / Int32sl,
        "cCsrInvalidUnwind" / Int32sl
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=482, version=0)
class Microsoft_Office_Word3_482_0(Etw):
    pattern = Struct(
        "featureDwTag" / Int32ul,
        "ProfilerModules" / WString,
        "ProfilerSamples" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=501, version=0)
class Microsoft_Office_Word3_501_0(Etw):
    pattern = Struct(
        "pdod" / Int64ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2000, version=1)
class Microsoft_Office_Word3_2000_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2001, version=1)
class Microsoft_Office_Word3_2001_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2002, version=1)
class Microsoft_Office_Word3_2002_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2003, version=1)
class Microsoft_Office_Word3_2003_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2004, version=1)
class Microsoft_Office_Word3_2004_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2005, version=1)
class Microsoft_Office_Word3_2005_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2006, version=1)
class Microsoft_Office_Word3_2006_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2007, version=1)
class Microsoft_Office_Word3_2007_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2008, version=1)
class Microsoft_Office_Word3_2008_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2009, version=1)
class Microsoft_Office_Word3_2009_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2010, version=1)
class Microsoft_Office_Word3_2010_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2011, version=1)
class Microsoft_Office_Word3_2011_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2012, version=1)
class Microsoft_Office_Word3_2012_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2013, version=1)
class Microsoft_Office_Word3_2013_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2014, version=1)
class Microsoft_Office_Word3_2014_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2015, version=1)
class Microsoft_Office_Word3_2015_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2016, version=1)
class Microsoft_Office_Word3_2016_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2017, version=1)
class Microsoft_Office_Word3_2017_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2018, version=1)
class Microsoft_Office_Word3_2018_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2019, version=1)
class Microsoft_Office_Word3_2019_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2020, version=1)
class Microsoft_Office_Word3_2020_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2021, version=1)
class Microsoft_Office_Word3_2021_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2022, version=1)
class Microsoft_Office_Word3_2022_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2023, version=1)
class Microsoft_Office_Word3_2023_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2024, version=1)
class Microsoft_Office_Word3_2024_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2025, version=1)
class Microsoft_Office_Word3_2025_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2026, version=1)
class Microsoft_Office_Word3_2026_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2027, version=1)
class Microsoft_Office_Word3_2027_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2028, version=1)
class Microsoft_Office_Word3_2028_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2029, version=1)
class Microsoft_Office_Word3_2029_1(Etw):
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


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2032, version=0)
class Microsoft_Office_Word3_2032_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2033, version=0)
class Microsoft_Office_Word3_2033_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2034, version=0)
class Microsoft_Office_Word3_2034_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2035, version=0)
class Microsoft_Office_Word3_2035_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2036, version=0)
class Microsoft_Office_Word3_2036_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2037, version=0)
class Microsoft_Office_Word3_2037_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2038, version=0)
class Microsoft_Office_Word3_2038_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2039, version=0)
class Microsoft_Office_Word3_2039_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2040, version=0)
class Microsoft_Office_Word3_2040_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2041, version=0)
class Microsoft_Office_Word3_2041_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2042, version=0)
class Microsoft_Office_Word3_2042_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2043, version=0)
class Microsoft_Office_Word3_2043_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2044, version=0)
class Microsoft_Office_Word3_2044_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2045, version=0)
class Microsoft_Office_Word3_2045_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2046, version=0)
class Microsoft_Office_Word3_2046_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2047, version=0)
class Microsoft_Office_Word3_2047_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2048, version=0)
class Microsoft_Office_Word3_2048_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2049, version=0)
class Microsoft_Office_Word3_2049_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2050, version=0)
class Microsoft_Office_Word3_2050_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2051, version=0)
class Microsoft_Office_Word3_2051_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2052, version=0)
class Microsoft_Office_Word3_2052_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2053, version=0)
class Microsoft_Office_Word3_2053_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2054, version=0)
class Microsoft_Office_Word3_2054_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2055, version=0)
class Microsoft_Office_Word3_2055_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2056, version=0)
class Microsoft_Office_Word3_2056_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2057, version=0)
class Microsoft_Office_Word3_2057_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2058, version=0)
class Microsoft_Office_Word3_2058_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2059, version=0)
class Microsoft_Office_Word3_2059_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2060, version=0)
class Microsoft_Office_Word3_2060_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2061, version=0)
class Microsoft_Office_Word3_2061_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "InfoString" / WString,
        "ErrIdOptional" / Int32sl,
        "HROptional" / Int32sl,
        "InfoOptDeci" / Int64ul,
        "InfoOptHex" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2064, version=0)
class Microsoft_Office_Word3_2064_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2065, version=0)
class Microsoft_Office_Word3_2065_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2066, version=0)
class Microsoft_Office_Word3_2066_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2067, version=0)
class Microsoft_Office_Word3_2067_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2068, version=0)
class Microsoft_Office_Word3_2068_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2069, version=0)
class Microsoft_Office_Word3_2069_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2070, version=0)
class Microsoft_Office_Word3_2070_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2071, version=0)
class Microsoft_Office_Word3_2071_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2072, version=0)
class Microsoft_Office_Word3_2072_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2073, version=0)
class Microsoft_Office_Word3_2073_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2074, version=0)
class Microsoft_Office_Word3_2074_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2075, version=0)
class Microsoft_Office_Word3_2075_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2076, version=0)
class Microsoft_Office_Word3_2076_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2077, version=0)
class Microsoft_Office_Word3_2077_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2078, version=0)
class Microsoft_Office_Word3_2078_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2079, version=0)
class Microsoft_Office_Word3_2079_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2080, version=0)
class Microsoft_Office_Word3_2080_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2081, version=0)
class Microsoft_Office_Word3_2081_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2082, version=0)
class Microsoft_Office_Word3_2082_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2083, version=0)
class Microsoft_Office_Word3_2083_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2084, version=0)
class Microsoft_Office_Word3_2084_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2085, version=0)
class Microsoft_Office_Word3_2085_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2086, version=0)
class Microsoft_Office_Word3_2086_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2087, version=0)
class Microsoft_Office_Word3_2087_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2088, version=0)
class Microsoft_Office_Word3_2088_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2089, version=0)
class Microsoft_Office_Word3_2089_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2090, version=0)
class Microsoft_Office_Word3_2090_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2091, version=0)
class Microsoft_Office_Word3_2091_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2092, version=0)
class Microsoft_Office_Word3_2092_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=2093, version=0)
class Microsoft_Office_Word3_2093_0(Etw):
    pattern = Struct(
        "InfoOptional1" / Int64ul,
        "InfoOptional2" / Int64ul,
        "InfoOptional3" / Int64ul,
        "InfoOptional4" / Int64ul,
        "ETW_TrackbackTag" / Int32ul
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30579, version=1)
class Microsoft_Office_Word3_30579_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30580, version=1)
class Microsoft_Office_Word3_30580_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30581, version=1)
class Microsoft_Office_Word3_30581_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30582, version=1)
class Microsoft_Office_Word3_30582_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30583, version=1)
class Microsoft_Office_Word3_30583_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30584, version=1)
class Microsoft_Office_Word3_30584_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30585, version=1)
class Microsoft_Office_Word3_30585_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30586, version=1)
class Microsoft_Office_Word3_30586_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30587, version=1)
class Microsoft_Office_Word3_30587_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30588, version=1)
class Microsoft_Office_Word3_30588_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30589, version=1)
class Microsoft_Office_Word3_30589_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30590, version=1)
class Microsoft_Office_Word3_30590_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30591, version=1)
class Microsoft_Office_Word3_30591_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30592, version=1)
class Microsoft_Office_Word3_30592_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30593, version=1)
class Microsoft_Office_Word3_30593_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30594, version=1)
class Microsoft_Office_Word3_30594_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30595, version=1)
class Microsoft_Office_Word3_30595_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30596, version=1)
class Microsoft_Office_Word3_30596_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30597, version=1)
class Microsoft_Office_Word3_30597_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30598, version=1)
class Microsoft_Office_Word3_30598_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30599, version=1)
class Microsoft_Office_Word3_30599_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30600, version=1)
class Microsoft_Office_Word3_30600_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30601, version=1)
class Microsoft_Office_Word3_30601_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30602, version=1)
class Microsoft_Office_Word3_30602_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30603, version=1)
class Microsoft_Office_Word3_30603_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30604, version=1)
class Microsoft_Office_Word3_30604_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30605, version=1)
class Microsoft_Office_Word3_30605_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30606, version=1)
class Microsoft_Office_Word3_30606_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30607, version=1)
class Microsoft_Office_Word3_30607_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30608, version=1)
class Microsoft_Office_Word3_30608_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30609, version=1)
class Microsoft_Office_Word3_30609_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30610, version=1)
class Microsoft_Office_Word3_30610_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30611, version=1)
class Microsoft_Office_Word3_30611_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30612, version=1)
class Microsoft_Office_Word3_30612_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30613, version=1)
class Microsoft_Office_Word3_30613_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30614, version=1)
class Microsoft_Office_Word3_30614_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30615, version=1)
class Microsoft_Office_Word3_30615_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30616, version=1)
class Microsoft_Office_Word3_30616_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30617, version=1)
class Microsoft_Office_Word3_30617_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30618, version=1)
class Microsoft_Office_Word3_30618_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30619, version=1)
class Microsoft_Office_Word3_30619_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30620, version=1)
class Microsoft_Office_Word3_30620_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30621, version=1)
class Microsoft_Office_Word3_30621_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30622, version=1)
class Microsoft_Office_Word3_30622_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30623, version=1)
class Microsoft_Office_Word3_30623_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30624, version=1)
class Microsoft_Office_Word3_30624_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30625, version=1)
class Microsoft_Office_Word3_30625_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30626, version=1)
class Microsoft_Office_Word3_30626_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30627, version=1)
class Microsoft_Office_Word3_30627_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30628, version=1)
class Microsoft_Office_Word3_30628_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30629, version=1)
class Microsoft_Office_Word3_30629_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30630, version=1)
class Microsoft_Office_Word3_30630_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30631, version=1)
class Microsoft_Office_Word3_30631_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30632, version=1)
class Microsoft_Office_Word3_30632_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30633, version=1)
class Microsoft_Office_Word3_30633_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30634, version=1)
class Microsoft_Office_Word3_30634_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30635, version=1)
class Microsoft_Office_Word3_30635_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30636, version=1)
class Microsoft_Office_Word3_30636_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30637, version=1)
class Microsoft_Office_Word3_30637_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30638, version=1)
class Microsoft_Office_Word3_30638_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30639, version=1)
class Microsoft_Office_Word3_30639_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30640, version=1)
class Microsoft_Office_Word3_30640_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30641, version=1)
class Microsoft_Office_Word3_30641_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30642, version=1)
class Microsoft_Office_Word3_30642_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30643, version=1)
class Microsoft_Office_Word3_30643_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30644, version=1)
class Microsoft_Office_Word3_30644_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30645, version=1)
class Microsoft_Office_Word3_30645_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30646, version=1)
class Microsoft_Office_Word3_30646_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30647, version=1)
class Microsoft_Office_Word3_30647_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30648, version=1)
class Microsoft_Office_Word3_30648_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30649, version=1)
class Microsoft_Office_Word3_30649_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30650, version=1)
class Microsoft_Office_Word3_30650_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30651, version=1)
class Microsoft_Office_Word3_30651_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30652, version=1)
class Microsoft_Office_Word3_30652_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30653, version=1)
class Microsoft_Office_Word3_30653_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30654, version=1)
class Microsoft_Office_Word3_30654_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30655, version=1)
class Microsoft_Office_Word3_30655_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30656, version=1)
class Microsoft_Office_Word3_30656_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30657, version=1)
class Microsoft_Office_Word3_30657_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30658, version=1)
class Microsoft_Office_Word3_30658_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30659, version=1)
class Microsoft_Office_Word3_30659_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30660, version=1)
class Microsoft_Office_Word3_30660_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30661, version=1)
class Microsoft_Office_Word3_30661_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30662, version=1)
class Microsoft_Office_Word3_30662_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30663, version=1)
class Microsoft_Office_Word3_30663_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30664, version=1)
class Microsoft_Office_Word3_30664_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30665, version=1)
class Microsoft_Office_Word3_30665_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30666, version=1)
class Microsoft_Office_Word3_30666_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30667, version=1)
class Microsoft_Office_Word3_30667_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30668, version=1)
class Microsoft_Office_Word3_30668_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30669, version=1)
class Microsoft_Office_Word3_30669_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30670, version=1)
class Microsoft_Office_Word3_30670_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30671, version=1)
class Microsoft_Office_Word3_30671_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30672, version=1)
class Microsoft_Office_Word3_30672_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30673, version=1)
class Microsoft_Office_Word3_30673_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30674, version=1)
class Microsoft_Office_Word3_30674_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30675, version=1)
class Microsoft_Office_Word3_30675_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30676, version=1)
class Microsoft_Office_Word3_30676_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30677, version=1)
class Microsoft_Office_Word3_30677_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30678, version=1)
class Microsoft_Office_Word3_30678_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30679, version=1)
class Microsoft_Office_Word3_30679_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30680, version=1)
class Microsoft_Office_Word3_30680_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30681, version=1)
class Microsoft_Office_Word3_30681_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30682, version=1)
class Microsoft_Office_Word3_30682_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30683, version=1)
class Microsoft_Office_Word3_30683_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30684, version=1)
class Microsoft_Office_Word3_30684_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30685, version=1)
class Microsoft_Office_Word3_30685_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30686, version=1)
class Microsoft_Office_Word3_30686_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30687, version=1)
class Microsoft_Office_Word3_30687_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30688, version=1)
class Microsoft_Office_Word3_30688_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30689, version=1)
class Microsoft_Office_Word3_30689_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30690, version=1)
class Microsoft_Office_Word3_30690_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30691, version=1)
class Microsoft_Office_Word3_30691_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30692, version=1)
class Microsoft_Office_Word3_30692_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30693, version=1)
class Microsoft_Office_Word3_30693_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30694, version=1)
class Microsoft_Office_Word3_30694_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30695, version=1)
class Microsoft_Office_Word3_30695_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30696, version=1)
class Microsoft_Office_Word3_30696_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30697, version=1)
class Microsoft_Office_Word3_30697_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30698, version=1)
class Microsoft_Office_Word3_30698_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30699, version=1)
class Microsoft_Office_Word3_30699_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30700, version=1)
class Microsoft_Office_Word3_30700_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30701, version=1)
class Microsoft_Office_Word3_30701_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30702, version=1)
class Microsoft_Office_Word3_30702_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30703, version=1)
class Microsoft_Office_Word3_30703_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30704, version=1)
class Microsoft_Office_Word3_30704_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30705, version=1)
class Microsoft_Office_Word3_30705_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30706, version=1)
class Microsoft_Office_Word3_30706_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30707, version=1)
class Microsoft_Office_Word3_30707_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30708, version=1)
class Microsoft_Office_Word3_30708_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30709, version=1)
class Microsoft_Office_Word3_30709_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30710, version=1)
class Microsoft_Office_Word3_30710_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30711, version=1)
class Microsoft_Office_Word3_30711_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30712, version=1)
class Microsoft_Office_Word3_30712_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30713, version=1)
class Microsoft_Office_Word3_30713_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30714, version=1)
class Microsoft_Office_Word3_30714_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30715, version=1)
class Microsoft_Office_Word3_30715_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30716, version=1)
class Microsoft_Office_Word3_30716_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30717, version=1)
class Microsoft_Office_Word3_30717_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30718, version=1)
class Microsoft_Office_Word3_30718_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30719, version=1)
class Microsoft_Office_Word3_30719_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30720, version=1)
class Microsoft_Office_Word3_30720_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30721, version=1)
class Microsoft_Office_Word3_30721_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30722, version=1)
class Microsoft_Office_Word3_30722_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30723, version=1)
class Microsoft_Office_Word3_30723_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30724, version=1)
class Microsoft_Office_Word3_30724_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30725, version=1)
class Microsoft_Office_Word3_30725_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30726, version=1)
class Microsoft_Office_Word3_30726_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30727, version=1)
class Microsoft_Office_Word3_30727_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30728, version=1)
class Microsoft_Office_Word3_30728_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30729, version=1)
class Microsoft_Office_Word3_30729_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30730, version=1)
class Microsoft_Office_Word3_30730_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30731, version=1)
class Microsoft_Office_Word3_30731_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30732, version=1)
class Microsoft_Office_Word3_30732_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30733, version=1)
class Microsoft_Office_Word3_30733_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30734, version=1)
class Microsoft_Office_Word3_30734_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30735, version=1)
class Microsoft_Office_Word3_30735_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30736, version=1)
class Microsoft_Office_Word3_30736_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30737, version=1)
class Microsoft_Office_Word3_30737_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30738, version=1)
class Microsoft_Office_Word3_30738_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30739, version=1)
class Microsoft_Office_Word3_30739_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30740, version=1)
class Microsoft_Office_Word3_30740_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30741, version=1)
class Microsoft_Office_Word3_30741_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30742, version=1)
class Microsoft_Office_Word3_30742_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30743, version=1)
class Microsoft_Office_Word3_30743_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30744, version=1)
class Microsoft_Office_Word3_30744_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30745, version=1)
class Microsoft_Office_Word3_30745_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30746, version=1)
class Microsoft_Office_Word3_30746_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30747, version=1)
class Microsoft_Office_Word3_30747_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30748, version=1)
class Microsoft_Office_Word3_30748_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30749, version=1)
class Microsoft_Office_Word3_30749_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30750, version=1)
class Microsoft_Office_Word3_30750_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30751, version=1)
class Microsoft_Office_Word3_30751_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30752, version=1)
class Microsoft_Office_Word3_30752_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30753, version=1)
class Microsoft_Office_Word3_30753_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30754, version=1)
class Microsoft_Office_Word3_30754_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30755, version=1)
class Microsoft_Office_Word3_30755_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30756, version=1)
class Microsoft_Office_Word3_30756_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30757, version=1)
class Microsoft_Office_Word3_30757_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30758, version=1)
class Microsoft_Office_Word3_30758_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30759, version=1)
class Microsoft_Office_Word3_30759_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30760, version=1)
class Microsoft_Office_Word3_30760_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30761, version=1)
class Microsoft_Office_Word3_30761_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30762, version=1)
class Microsoft_Office_Word3_30762_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30763, version=1)
class Microsoft_Office_Word3_30763_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30764, version=1)
class Microsoft_Office_Word3_30764_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30765, version=1)
class Microsoft_Office_Word3_30765_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30766, version=1)
class Microsoft_Office_Word3_30766_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30767, version=1)
class Microsoft_Office_Word3_30767_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30768, version=1)
class Microsoft_Office_Word3_30768_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30769, version=1)
class Microsoft_Office_Word3_30769_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30770, version=1)
class Microsoft_Office_Word3_30770_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30771, version=1)
class Microsoft_Office_Word3_30771_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30772, version=1)
class Microsoft_Office_Word3_30772_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30773, version=1)
class Microsoft_Office_Word3_30773_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30774, version=1)
class Microsoft_Office_Word3_30774_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30775, version=1)
class Microsoft_Office_Word3_30775_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30776, version=1)
class Microsoft_Office_Word3_30776_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30777, version=1)
class Microsoft_Office_Word3_30777_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30778, version=1)
class Microsoft_Office_Word3_30778_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30779, version=1)
class Microsoft_Office_Word3_30779_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30780, version=1)
class Microsoft_Office_Word3_30780_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30781, version=1)
class Microsoft_Office_Word3_30781_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30782, version=1)
class Microsoft_Office_Word3_30782_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30783, version=1)
class Microsoft_Office_Word3_30783_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30784, version=1)
class Microsoft_Office_Word3_30784_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30785, version=1)
class Microsoft_Office_Word3_30785_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30786, version=1)
class Microsoft_Office_Word3_30786_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30787, version=1)
class Microsoft_Office_Word3_30787_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30788, version=1)
class Microsoft_Office_Word3_30788_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30789, version=1)
class Microsoft_Office_Word3_30789_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30790, version=1)
class Microsoft_Office_Word3_30790_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30791, version=1)
class Microsoft_Office_Word3_30791_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30792, version=1)
class Microsoft_Office_Word3_30792_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30793, version=1)
class Microsoft_Office_Word3_30793_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30794, version=1)
class Microsoft_Office_Word3_30794_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30795, version=1)
class Microsoft_Office_Word3_30795_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30796, version=1)
class Microsoft_Office_Word3_30796_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30797, version=1)
class Microsoft_Office_Word3_30797_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30798, version=1)
class Microsoft_Office_Word3_30798_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30799, version=1)
class Microsoft_Office_Word3_30799_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30800, version=1)
class Microsoft_Office_Word3_30800_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30801, version=1)
class Microsoft_Office_Word3_30801_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30802, version=1)
class Microsoft_Office_Word3_30802_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30803, version=1)
class Microsoft_Office_Word3_30803_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30804, version=1)
class Microsoft_Office_Word3_30804_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30805, version=1)
class Microsoft_Office_Word3_30805_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30806, version=1)
class Microsoft_Office_Word3_30806_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30807, version=1)
class Microsoft_Office_Word3_30807_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30808, version=1)
class Microsoft_Office_Word3_30808_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30809, version=1)
class Microsoft_Office_Word3_30809_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30810, version=1)
class Microsoft_Office_Word3_30810_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30811, version=1)
class Microsoft_Office_Word3_30811_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30812, version=1)
class Microsoft_Office_Word3_30812_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30813, version=1)
class Microsoft_Office_Word3_30813_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30814, version=1)
class Microsoft_Office_Word3_30814_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30815, version=1)
class Microsoft_Office_Word3_30815_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30816, version=1)
class Microsoft_Office_Word3_30816_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30817, version=1)
class Microsoft_Office_Word3_30817_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30818, version=1)
class Microsoft_Office_Word3_30818_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30819, version=1)
class Microsoft_Office_Word3_30819_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30820, version=1)
class Microsoft_Office_Word3_30820_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30821, version=1)
class Microsoft_Office_Word3_30821_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30822, version=1)
class Microsoft_Office_Word3_30822_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30823, version=1)
class Microsoft_Office_Word3_30823_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30824, version=1)
class Microsoft_Office_Word3_30824_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30825, version=1)
class Microsoft_Office_Word3_30825_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30826, version=1)
class Microsoft_Office_Word3_30826_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30827, version=1)
class Microsoft_Office_Word3_30827_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30828, version=1)
class Microsoft_Office_Word3_30828_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30829, version=1)
class Microsoft_Office_Word3_30829_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30830, version=1)
class Microsoft_Office_Word3_30830_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30831, version=1)
class Microsoft_Office_Word3_30831_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30832, version=1)
class Microsoft_Office_Word3_30832_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30833, version=1)
class Microsoft_Office_Word3_30833_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30834, version=1)
class Microsoft_Office_Word3_30834_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30835, version=1)
class Microsoft_Office_Word3_30835_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30836, version=1)
class Microsoft_Office_Word3_30836_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30837, version=1)
class Microsoft_Office_Word3_30837_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30838, version=1)
class Microsoft_Office_Word3_30838_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30839, version=1)
class Microsoft_Office_Word3_30839_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30840, version=1)
class Microsoft_Office_Word3_30840_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30841, version=1)
class Microsoft_Office_Word3_30841_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30842, version=1)
class Microsoft_Office_Word3_30842_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30843, version=1)
class Microsoft_Office_Word3_30843_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30844, version=1)
class Microsoft_Office_Word3_30844_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30845, version=1)
class Microsoft_Office_Word3_30845_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30846, version=1)
class Microsoft_Office_Word3_30846_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30847, version=1)
class Microsoft_Office_Word3_30847_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )


@declare(guid=guid("a1b69d49-2195-4f59-9d33-bdf30c0fe473"), event_id=30848, version=1)
class Microsoft_Office_Word3_30848_1(Etw):
    pattern = Struct(
        "tag" / WString,
        "xsz" / WString
    )

