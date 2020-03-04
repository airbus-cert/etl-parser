# -*- coding: utf-8 -*-
"""
Microsoft-Office-Events
GUID : 8736922d-e8b2-47eb-8564-23e77e728cf3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=1, version=0)
class Microsoft_Office_Events_1_0(Etw):
    pattern = Struct(
        "cValue" / Int32ul,
        "Frame" / Int64ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=2, version=0)
class Microsoft_Office_Events_2_0(Etw):
    pattern = Struct(
        "BaseAddress" / Int64ul,
        "TimeDateStamp" / Int32ul,
        "Size" / Int32ul,
        "wzName" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=3, version=0)
class Microsoft_Office_Events_3_0(Etw):
    pattern = Struct(
        "dwTag" / Int32ul,
        "dwID" / Int32ul,
        "dwBudgetType" / Int32ul,
        "dwFlags" / Int32ul,
        "Limit" / Int32sl,
        "dwInterval" / Int32ul,
        "wzData" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=4, version=0)
class Microsoft_Office_Events_4_0(Etw):
    pattern = Struct(
        "dwTag" / Int32ul,
        "dwID" / Int32ul,
        "dwBudgetType" / Int32ul,
        "Update" / Int32sl,
        "dwTimeNow" / Int32ul,
        "wzData" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=5, version=0)
class Microsoft_Office_Events_5_0(Etw):
    pattern = Struct(
        "dwTag" / Int32ul,
        "dwID" / Int32ul,
        "dwBudgetType" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=6, version=0)
class Microsoft_Office_Events_6_0(Etw):
    pattern = Struct(
        "dwCodeMarker" / Int32ul,
        "dwModuleId" / Int32sl
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=7, version=0)
class Microsoft_Office_Events_7_0(Etw):
    pattern = Struct(
        "dwDatapoint" / Int32ul,
        "dwTick" / Int32ul,
        "dwValue1" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=8, version=0)
class Microsoft_Office_Events_8_0(Etw):
    pattern = Struct(
        "dwDatapoint" / Int32ul,
        "dwTick" / Int32ul,
        "dwValue1" / Int32ul,
        "dwCount" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=9, version=0)
class Microsoft_Office_Events_9_0(Etw):
    pattern = Struct(
        "dwDatapoint" / Int32ul,
        "dwTick" / Int32ul,
        "cValue" / Int32ul,
        "dwValue" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=10, version=0)
class Microsoft_Office_Events_10_0(Etw):
    pattern = Struct(
        "dwTag" / Int32ul,
        "dwID" / Int32ul,
        "dwBudgetType" / Int32ul,
        "Limit" / Int32sl,
        "dwInterval" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=11, version=0)
class Microsoft_Office_Events_11_0(Etw):
    pattern = Struct(
        "szFunction" / CString,
        "dwLine" / Int32ul,
        "dwHResult" / Int32sl,
        "wzMessage" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=12, version=0)
class Microsoft_Office_Events_12_0(Etw):
    pattern = Struct(
        "szFunction" / CString,
        "dwLine" / Int32ul,
        "dwHResult" / Int32sl,
        "wzMessage" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=13, version=0)
class Microsoft_Office_Events_13_0(Etw):
    pattern = Struct(
        "szFunction" / CString,
        "dwLine" / Int32ul,
        "dwHResult" / Int32sl,
        "wzMessage" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=14, version=0)
class Microsoft_Office_Events_14_0(Etw):
    pattern = Struct(
        "szFunction" / CString,
        "dwLine" / Int32ul,
        "dwHResult" / Int32sl,
        "wzMessage" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=15, version=0)
class Microsoft_Office_Events_15_0(Etw):
    pattern = Struct(
        "szFunction" / CString,
        "dwLine" / Int32ul,
        "szCall" / CString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=16, version=0)
class Microsoft_Office_Events_16_0(Etw):
    pattern = Struct(
        "szFunction" / CString,
        "dwLine" / Int32ul,
        "szCall" / CString,
        "dwHResult" / Int32sl
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=17, version=0)
class Microsoft_Office_Events_17_0(Etw):
    pattern = Struct(
        "szFunction" / CString,
        "szTag" / CString,
        "wzParameter" / WString,
        "pPointer" / Int64ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=18, version=0)
class Microsoft_Office_Events_18_0(Etw):
    pattern = Struct(
        "szFunction" / CString,
        "dwHResult" / Int32sl
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=19, version=0)
class Microsoft_Office_Events_19_0(Etw):
    pattern = Struct(
        "szFunction" / CString,
        "wzJob" / WString,
        "szTag" / CString,
        "wzParameter" / WString,
        "pPointer" / Int64ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=20, version=0)
class Microsoft_Office_Events_20_0(Etw):
    pattern = Struct(
        "szFunction" / CString,
        "wzJob" / WString,
        "dwHResult" / Int32sl
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=21, version=0)
class Microsoft_Office_Events_21_0(Etw):
    pattern = Struct(
        "wzFriendlyName" / WString,
        "wzAddressSMTP" / WString,
        "wzSip" / WString,
        "wzAlias" / WString,
        "wzUserInfoId" / WString,
        "wzPhoneNumber" / WString,
        "wzFlags" / WString,
        "wzEntryID" / WString,
        "wzMuid" / WString,
        "wzResID" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=22, version=0)
class Microsoft_Office_Events_22_0(Etw):
    pattern = Struct(
        "wzSigninName" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=23, version=0)
class Microsoft_Office_Events_23_0(Etw):
    pattern = Struct(
        "wzSigninName" / WString,
        "wzAltEmail" / WString,
        "dwStatus" / Int32sl,
        "dwAvail" / Int32sl
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=24, version=0)
class Microsoft_Office_Events_24_0(Etw):
    pattern = Struct(
        "szFunction" / CString,
        "szMessage" / CString,
        "pPointer" / Int64ul,
        "wzName" / WString,
        "wzSPUserId" / WString,
        "wzSPServerInfo" / WString,
        "wzDN" / WString,
        "wzManager" / WString,
        "wzEntryId" / WString,
        "wzMuid" / WString,
        "wzEmailAddress" / WString,
        "wzSignInAddress" / WString,
        "wzAlias" / WString,
        "wzHashKey" / WString,
        "wzResID" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=25, version=0)
class Microsoft_Office_Events_25_0(Etw):
    pattern = Struct(
        "szFunction" / CString,
        "szMessage" / CString,
        "wzName" / WString,
        "pPointer" / Int64ul,
        "wzContactType" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=26, version=0)
class Microsoft_Office_Events_26_0(Etw):
    pattern = Struct(
        "szFunction" / CString,
        "szMessage" / CString,
        "wzName" / WString,
        "pPointer" / Int64ul,
        "wzSigninName" / WString,
        "bSetFromDL" / Int8ul,
        "wzSMTPAddress" / WString,
        "wzFriendlyName" / WString,
        "wzTitle" / WString,
        "wzCompanyName" / WString,
        "wzDepartment" / WString,
        "wzOfficeLocation" / WString,
        "wzWorkPhone" / WString,
        "wzMobilePhone" / WString,
        "wzHomePhone" / WString,
        "wzDescription" / WString,
        "wzEntryID" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=27, version=0)
class Microsoft_Office_Events_27_0(Etw):
    pattern = Struct(
        "szFunction" / CString,
        "wzProperty" / WString,
        "wzOldValue" / WString,
        "wzNewValue" / WString,
        "wzKey" / WString,
        "pPointer" / Int64ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=28, version=0)
class Microsoft_Office_Events_28_0(Etw):
    pattern = Struct(
        "szFunction" / CString,
        "wzProperty" / WString,
        "wzOldValue" / WString,
        "wzNewValue" / WString,
        "wzKey" / WString,
        "pPointer" / Int64ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=29, version=0)
class Microsoft_Office_Events_29_0(Etw):
    pattern = Struct(
        "szString" / CString,
        "szFunction" / CString,
        "pCardHwnd" / Int64ul,
        "pPersona" / Int64ul,
        "pPersonInfo" / Int64ul,
        "wzSigninName" / WString,
        "wzContactType" / WString,
        "wzCardType" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=30, version=0)
class Microsoft_Office_Events_30_0(Etw):
    pattern = Struct(
        "szFunction" / CString,
        "szMessage" / CString,
        "wzName" / WString,
        "wzSigninName" / WString,
        "wzEmail" / WString,
        "wzWPhone" / WString,
        "wzMPhone" / WString,
        "wzHPhone" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=31, version=0)
class Microsoft_Office_Events_31_0(Etw):
    pattern = Struct(
        "szFunction" / CString,
        "wzProperty" / WString,
        "wzOldValue" / WString,
        "wzNewValue" / WString,
        "wzKey" / WString,
        "pPointer" / Int64ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=32, version=0)
class Microsoft_Office_Events_32_0(Etw):
    pattern = Struct(
        "szFunction" / CString,
        "dwRank" / Int32ul,
        "wzSIPAddress" / WString,
        "wzDataType" / WString,
        "wzEmailAddress" / WString,
        "wzDisplayName" / WString,
        "wzPhoneNumber" / WString,
        "wzTitle" / WString,
        "wzEntryId" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=33, version=0)
class Microsoft_Office_Events_33_0(Etw):
    pattern = Struct(
        "cValue" / Int32ul,
        "Frame" / Int64ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=34, version=0)
class Microsoft_Office_Events_34_0(Etw):
    pattern = Struct(
        "BaseAddress" / Int64ul,
        "TimeDateStamp" / Int32ul,
        "Size" / Int32ul,
        "wzName" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=35, version=0)
class Microsoft_Office_Events_35_0(Etw):
    pattern = Struct(
        "wzMessage" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=36, version=0)
class Microsoft_Office_Events_36_0(Etw):
    pattern = Struct(
        "cookie" / Int64ul,
        "dwID" / Int32ul,
        "wzName" / WString,
        "priority" / Int32ul,
        "scheduler" / Int32ul,
        "grfTaskFlags" / Int32ul,
        "msecRelease" / Int32ul,
        "msecDeadline" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=37, version=0)
class Microsoft_Office_Events_37_0(Etw):
    pattern = Struct(
        "cookie" / Int64ul,
        "dwID" / Int32ul,
        "wzName" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=38, version=0)
class Microsoft_Office_Events_38_0(Etw):
    pattern = Struct(
        "cookie" / Int64sl,
        "dwID" / Int32ul,
        "wzName" / WString,
        "grfModifyFlags" / Int32ul,
        "priority" / Int32ul,
        "scheduler" / Int32ul,
        "grfTaskFlags" / Int32ul,
        "msecRelease" / Int32ul,
        "msecDeadline" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=39, version=0)
class Microsoft_Office_Events_39_0(Etw):
    pattern = Struct(
        "fTimerOnly" / Int8ul,
        "fTracking" / Int8ul,
        "fResuming" / Int8ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=42, version=0)
class Microsoft_Office_Events_42_0(Etw):
    pattern = Struct(
        "cookie" / Int64ul,
        "dwID" / Int32ul,
        "wzName" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=43, version=0)
class Microsoft_Office_Events_43_0(Etw):
    pattern = Struct(
        "cookie" / Int64ul,
        "dwID" / Int32ul,
        "wzName" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=44, version=0)
class Microsoft_Office_Events_44_0(Etw):
    pattern = Struct(
        "cookie" / Int64ul,
        "dwID" / Int32ul,
        "wzName" / WString,
        "msecsRunIntervalAvg" / Int64ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=46, version=0)
class Microsoft_Office_Events_46_0(Etw):
    pattern = Struct(
        "msecDelay" / Int32ul,
        "msecsTolerableDelay" / Int32ul,
        "dwID" / Int32ul,
        "wzFirstTaskName" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=47, version=0)
class Microsoft_Office_Events_47_0(Etw):
    pattern = Struct(
        "wzC1Source" / WString,
        "wzC1EntryId" / WString,
        "wzC1PersonId" / WString,
        "wzC1StampedGalEId" / WString,
        "wzC1Email1" / WString,
        "wzC1Email2" / WString,
        "wzC1Email3" / WString,
        "wzC1DisplayName" / WString,
        "wzC2Source" / WString,
        "wzC2EntryId" / WString,
        "wzC2PersonId" / WString,
        "wzC2StampedGalEId" / WString,
        "wzC2Email1" / WString,
        "wzC2Email2" / WString,
        "wzC2Email3" / WString,
        "wzC2DisplayName" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=48, version=0)
class Microsoft_Office_Events_48_0(Etw):
    pattern = Struct(
        "dwJobSequence" / Int32ul,
        "dwJobCount" / Int32sl,
        "dwHrResult" / Int32sl,
        "dwResultCount" / Int32sl,
        "fLastBatch" / Int8ul,
        "fMoreResults" / Int8ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=49, version=0)
class Microsoft_Office_Events_49_0(Etw):
    pattern = Struct(
        "szFunction" / CString,
        "wzMessage" / WString,
        "pPointer" / Int64ul,
        "wzRootSourceType" / WString,
        "szSourceType" / CString,
        "wzKey" / WString,
        "wzName" / WString,
        "wzEntryID" / WString,
        "wzUserID" / WString,
        "wzMuid" / WString,
        "wzProviderId" / WString,
        "wzCreationDate" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=50, version=0)
class Microsoft_Office_Events_50_0(Etw):
    pattern = Struct(
        "cookie" / Int64ul,
        "grfUpdateType" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=51, version=0)
class Microsoft_Office_Events_51_0(Etw):
    pattern = Struct(
        "wzMessage" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=52, version=0)
class Microsoft_Office_Events_52_0(Etw):
    pattern = Struct(
        "wzMessageName" / WString,
        "dwValue" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=53, version=0)
class Microsoft_Office_Events_53_0(Etw):
    pattern = Struct(
        "szMessageName" / CString,
        "wzPersonID" / WString,
        "wzEntryID" / WString,
        "wzEmail1" / WString,
        "wzEmail2" / WString,
        "wzEmail3" / WString,
        "wzIM" / WString,
        "wzLastModified" / WString,
        "fLInked" / Int8ul,
        "wzGALEntryID" / WString,
        "dwGALLinkState" / Int32ul,
        "wzLinkRejectHistory" / WString,
        "wzSMTPAddressCache" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=54, version=0)
class Microsoft_Office_Events_54_0(Etw):
    pattern = Struct(
        "szMessageName" / CString,
        "wzEntryID1" / WString,
        "wzEntryID2" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=55, version=0)
class Microsoft_Office_Events_55_0(Etw):
    pattern = Struct(
        "szComment" / CString,
        "szCallingFunction" / CString,
        "wzFeedProviderName" / WString,
        "wzFeedHTML" / WString,
        "wzFeedData" / WString,
        "wzFeedPlainText" / WString,
        "wzFeedIcon" / WString,
        "wzTime" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=56, version=0)
class Microsoft_Office_Events_56_0(Etw):
    pattern = Struct(
        "szComment" / CString,
        "szFunction" / CString,
        "wzProviderXML" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=57, version=0)
class Microsoft_Office_Events_57_0(Etw):
    pattern = Struct(
        "szComment" / CString,
        "szFunction" / CString,
        "wzUnSanitizedHTML" / WString,
        "wzSanitizedHTML" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=58, version=0)
class Microsoft_Office_Events_58_0(Etw):
    pattern = Struct(
        "szComment" / CString,
        "szFunction" / CString,
        "wzFriendInfo" / WString,
        "wzRetrievalTime" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=59, version=0)
class Microsoft_Office_Events_59_0(Etw):
    pattern = Struct(
        "szComment" / CString,
        "szFunction" / CString,
        "wzCurrentTime" / WString,
        "wzTimeInMinutesForNextSync" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=60, version=0)
class Microsoft_Office_Events_60_0(Etw):
    pattern = Struct(
        "dwTag" / Int32ul,
        "dwId" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=61, version=0)
class Microsoft_Office_Events_61_0(Etw):
    pattern = Struct(
        "dwTag" / Int32ul,
        "dwId" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=62, version=0)
class Microsoft_Office_Events_62_0(Etw):
    pattern = Struct(
        "wzFunction" / WString,
        "dwLine" / Int32ul,
        "dwHResult" / Int32sl,
        "wzMessage" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=63, version=0)
class Microsoft_Office_Events_63_0(Etw):
    pattern = Struct(
        "wzFunction" / WString,
        "dwLine" / Int32ul,
        "dwHResult" / Int32sl,
        "wzMessage" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=64, version=0)
class Microsoft_Office_Events_64_0(Etw):
    pattern = Struct(
        "wzFunction" / WString,
        "dwLine" / Int32ul,
        "dwHResult" / Int32sl,
        "wzMessage" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=65, version=0)
class Microsoft_Office_Events_65_0(Etw):
    pattern = Struct(
        "wzFunction" / WString,
        "dwLine" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=66, version=0)
class Microsoft_Office_Events_66_0(Etw):
    pattern = Struct(
        "wzFunction" / WString,
        "dwLine" / Int32ul,
        "dwHResult" / Int32sl
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=67, version=0)
class Microsoft_Office_Events_67_0(Etw):
    pattern = Struct(
        "cValue" / Int32ul,
        "Frame" / Int64ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=68, version=0)
class Microsoft_Office_Events_68_0(Etw):
    pattern = Struct(
        "BaseAddress" / Int64ul,
        "TimeDateStamp" / Int32ul,
        "Size" / Int32ul,
        "wzName" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=69, version=0)
class Microsoft_Office_Events_69_0(Etw):
    pattern = Struct(
        "szFunction" / CString,
        "wzProperty" / WString,
        "wzPrevValue" / WString,
        "wzNewValue" / WString,
        "wzUniqueKey" / WString,
        "pPointer" / Int64ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=70, version=0)
class Microsoft_Office_Events_70_0(Etw):
    pattern = Struct(
        "wzLogLine" / WString
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=71, version=0)
class Microsoft_Office_Events_71_0(Etw):
    pattern = Struct(
        "dwEntrypoint" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=73, version=0)
class Microsoft_Office_Events_73_0(Etw):
    pattern = Struct(
        "dwGroupNameLength" / Int32ul,
        "dwGroupIdLength" / Int32ul,
        "dwGroupType" / Int32ul,
        "fAliasChanged" / Int8ul,
        "fAutoSubscribeChecked" / Int8ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=74, version=0)
class Microsoft_Office_Events_74_0(Etw):
    pattern = Struct(
        "fResult" / Int8ul,
        "dwErrorType" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=75, version=0)
class Microsoft_Office_Events_75_0(Etw):
    pattern = Struct(
        "dwGroupIdLength" / Int32ul,
        "fGroupIdManuallyEdited" / Int8ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=76, version=0)
class Microsoft_Office_Events_76_0(Etw):
    pattern = Struct(
        "fResult" / Int8ul,
        "dwErrorType" / Int32ul,
        "dwAvailbilityResult" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=77, version=0)
class Microsoft_Office_Events_77_0(Etw):
    pattern = Struct(
        "dwDialogType" / Int32ul,
        "dwEntrypoint" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=79, version=0)
class Microsoft_Office_Events_79_0(Etw):
    pattern = Struct(
        "dwDialogType" / Int32ul,
        "dwAddedMembersCount" / Int32ul,
        "dwRemovedMembersCount" / Int32ul,
        "dwAddedAdminsCount" / Int32ul,
        "dwRemovedAdminsCount" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=80, version=0)
class Microsoft_Office_Events_80_0(Etw):
    pattern = Struct(
        "operationType" / Int32ul,
        "fResult" / Int8ul,
        "dwErrorType" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=81, version=0)
class Microsoft_Office_Events_81_0(Etw):
    pattern = Struct(
        "fResult" / Int8ul,
        "dwErrorType" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=83, version=0)
class Microsoft_Office_Events_83_0(Etw):
    pattern = Struct(
        "fResult" / Int8ul,
        "dwErrorType" / Int32ul,
        "dwMemberCount" / Int32ul,
        "dwAdminCount" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=84, version=0)
class Microsoft_Office_Events_84_0(Etw):
    pattern = Struct(
        "fResult" / Int8ul,
        "dwErrorType" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=88, version=0)
class Microsoft_Office_Events_88_0(Etw):
    pattern = Struct(
        "fResult" / Int8ul,
        "dwErrorType" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=89, version=0)
class Microsoft_Office_Events_89_0(Etw):
    pattern = Struct(
        "dwActionType" / Int32ul,
        "dwEnvironment" / Int32ul,
        "dwHResult" / Int32ul
    )


@declare(guid=guid("8736922d-e8b2-47eb-8564-23e77e728cf3"), event_id=91, version=0)
class Microsoft_Office_Events_91_0(Etw):
    pattern = Struct(
        "fResult" / Int8ul,
        "dwErrorType" / Int32ul,
        "dwMemberCount" / Int32ul
    )

