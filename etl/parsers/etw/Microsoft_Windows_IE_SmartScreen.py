# -*- coding: utf-8 -*-
"""
Microsoft-Windows-IE-SmartScreen
GUID : 52f82079-1974-4c67-81da-807b892778bb
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=1, version=0)
class Microsoft_Windows_IE_SmartScreen_1_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=2, version=0)
class Microsoft_Windows_IE_SmartScreen_2_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=3, version=0)
class Microsoft_Windows_IE_SmartScreen_3_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=4, version=0)
class Microsoft_Windows_IE_SmartScreen_4_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=5, version=0)
class Microsoft_Windows_IE_SmartScreen_5_0(Etw):
    pattern = Struct(
        "ReqType" / Int32ul
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=6, version=0)
class Microsoft_Windows_IE_SmartScreen_6_0(Etw):
    pattern = Struct(
        "ReqType" / Int32ul
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=7, version=0)
class Microsoft_Windows_IE_SmartScreen_7_0(Etw):
    pattern = Struct(
        "ReqType" / Int32ul
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=8, version=0)
class Microsoft_Windows_IE_SmartScreen_8_0(Etw):
    pattern = Struct(
        "ReqType" / Int32ul
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=9, version=0)
class Microsoft_Windows_IE_SmartScreen_9_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "CacheExist" / Int8ul
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=10, version=0)
class Microsoft_Windows_IE_SmartScreen_10_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "DatExist" / Int8ul
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=11, version=0)
class Microsoft_Windows_IE_SmartScreen_11_0(Etw):
    pattern = Struct(
        "numElements" / Int32ul,
        "DefaultLangId" / WString,
        "lastOverrideToken" / WString,
        "newOverrideToken" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=12, version=0)
class Microsoft_Windows_IE_SmartScreen_12_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "RawURL" / WString,
        "UrlType" / WString,
        "ReqType" / WString,
        "HostIP" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=13, version=0)
class Microsoft_Windows_IE_SmartScreen_13_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "RawURL" / WString,
        "UrlType" / WString,
        "ReqType" / WString,
        "HostIP" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=14, version=0)
class Microsoft_Windows_IE_SmartScreen_14_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "Categories" / WString,
        "HC" / Int32ul,
        "PC" / Int32ul
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=15, version=0)
class Microsoft_Windows_IE_SmartScreen_15_0(Etw):
    pattern = Struct(
        "GUID" / WString,
        "DV" / WString,
        "FV" / WString,
        "OSV" / WString,
        "BrowserLang" / WString,
        "ReportType" / WString,
        "ClientID" / WString,
        "TopURL" / WString,
        "RawTopURL" / WString,
        "TopReferURL" / WString,
        "RawTopReferURL" / WString,
        "HostIP" / WString,
        "Threats" / WString,
        "FramesCount" / Int32ul,
        "WhyString" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=16, version=0)
class Microsoft_Windows_IE_SmartScreen_16_0(Etw):
    pattern = Struct(
        "FrameURL" / WString,
        "RawFrameURL" / WString,
        "FramePCL" / WString,
        "FrameTricks" / WString,
        "Framekeywords" / WString,
        "FrameUrlType" / WString,
        "FrameIP" / WString,
        "Signature" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=17, version=0)
class Microsoft_Windows_IE_SmartScreen_17_0(Etw):
    pattern = Struct(
        "FrameURL" / WString,
        "RawFrameURL" / WString,
        "FramePCL" / WString,
        "FrameTricks" / WString,
        "Framekeywords" / WString,
        "FrameUrlType" / WString,
        "FrameIP" / WString,
        "Signature" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=18, version=0)
class Microsoft_Windows_IE_SmartScreen_18_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "Categories" / WString,
        "HC" / Int32ul,
        "PC" / Int32ul
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=19, version=0)
class Microsoft_Windows_IE_SmartScreen_19_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "PCL" / Double,
        "THREAT" / Int32ul,
        "Heuristic" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=20, version=0)
class Microsoft_Windows_IE_SmartScreen_20_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "PCL" / Double,
        "THREAT" / Int32ul,
        "Heuristic" / WString,
        "HasAnyInputFields" / Int8ul,
        "HasPasswordField" / Int8ul
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=21, version=0)
class Microsoft_Windows_IE_SmartScreen_21_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "LinksCount" / Int32ul,
        "TopTargetCount" / Int32ul
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=22, version=0)
class Microsoft_Windows_IE_SmartScreen_22_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "CanonURL" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=23, version=0)
class Microsoft_Windows_IE_SmartScreen_23_0(Etw):
    pattern = Struct(
        "Info" / WString,
        "XML" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=24, version=0)
class Microsoft_Windows_IE_SmartScreen_24_0(Etw):
    pattern = Struct(
        "Info" / WString,
        "XML" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=25, version=0)
class Microsoft_Windows_IE_SmartScreen_25_0(Etw):
    pattern = Struct(
        "Info" / WString,
        "XML" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=26, version=0)
class Microsoft_Windows_IE_SmartScreen_26_0(Etw):
    pattern = Struct(
        "Info" / WString,
        "XML" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=27, version=0)
class Microsoft_Windows_IE_SmartScreen_27_0(Etw):
    pattern = Struct(
        "Info" / WString,
        "XML" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=28, version=0)
class Microsoft_Windows_IE_SmartScreen_28_0(Etw):
    pattern = Struct(
        "Info" / WString,
        "XML" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=29, version=0)
class Microsoft_Windows_IE_SmartScreen_29_0(Etw):
    pattern = Struct(
        "Info" / WString,
        "XML" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=30, version=0)
class Microsoft_Windows_IE_SmartScreen_30_0(Etw):
    pattern = Struct(
        "Info" / WString,
        "XML" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=31, version=0)
class Microsoft_Windows_IE_SmartScreen_31_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "FinalHRESULT" / Int32ul,
        "THREAT" / Int32ul,
        "UrsStatus" / Int32ul,
        "AllUrlsFoundInDat" / Int8ul,
        "BlockedUrl" / WString,
        "IsBlockedUrlTopFrame" / Int8ul,
        "BlockedUrlCategories" / Int64ul,
        "UrlFetchState" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=32, version=0)
class Microsoft_Windows_IE_SmartScreen_32_0(Etw):
    pattern = Struct(
        "Info" / WString,
        "URL" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=33, version=0)
class Microsoft_Windows_IE_SmartScreen_33_0(Etw):
    pattern = Struct(
        "Info" / WString,
        "XML" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=34, version=0)
class Microsoft_Windows_IE_SmartScreen_34_0(Etw):
    pattern = Struct(
        "FrameURL" / WString,
        "ScriptSource" / WString
    )


@declare(guid=guid("52f82079-1974-4c67-81da-807b892778bb"), event_id=1100, version=0)
class Microsoft_Windows_IE_SmartScreen_1100_0(Etw):
    pattern = Struct(
        "Uri" / WString,
        "ReferrerUri" / WString,
        "RedirectUri" / WString,
        "CallingProcessId" / Int32ul,
        "CallingProcessCreationTime" / Int64ul,
        "RequestId" / WString,
        "FinalResult" / WString
    )

