# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ParentalControls
GUID : 01090065-b467-4503-9b28-533766761087
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("01090065-b467-4503-9b28-533766761087"), event_id=1, version=0)
class Microsoft_Windows_ParentalControls_1_0(Etw):
    pattern = Struct(
        "Class" / WString,
        "Setting" / Int32ul,
        "AccountOwner" / WString,
        "OldValue" / WString,
        "NewValue" / WString,
        "Reason" / Int32ul,
        "Optional" / WString
    )


@declare(guid=guid("01090065-b467-4503-9b28-533766761087"), event_id=2, version=0)
class Microsoft_Windows_ParentalControls_2_0(Etw):
    pattern = Struct(
        "AppID" / Guid,
        "InstanceID" / Guid,
        "Version" / WString,
        "Path" / WString,
        "Rating" / WString,
        "RatingsSystem" / Guid,
        "Reason" / Int32ul,
        "DescriptorCount" / Int32ul,
        "Descriptor" / WString,
        "PID" / Int32ul
    )


@declare(guid=guid("01090065-b467-4503-9b28-533766761087"), event_id=3, version=0)
class Microsoft_Windows_ParentalControls_3_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "Application" / WString,
        "Version" / WString,
        "Reason" / Int32ul,
        "RatingSystemID" / Guid,
        "CategoryCount" / Int32ul,
        "Category" / WString
    )


@declare(guid=guid("01090065-b467-4503-9b28-533766761087"), event_id=4, version=0)
class Microsoft_Windows_ParentalControls_4_0(Etw):
    pattern = Struct(
        "Sender" / WString,
        "Application" / WString,
        "Version" / WString,
        "Subject" / WString,
        "Reason" / Int32ul,
        "RecipientCount" / Int32ul,
        "Recipient" / WString,
        "AttachmentCount" / Int32ul,
        "AttachmentName" / WString,
        "ReceivedTime" / SystemTime,
        "EmailAccount" / WString
    )


@declare(guid=guid("01090065-b467-4503-9b28-533766761087"), event_id=5, version=0)
class Microsoft_Windows_ParentalControls_5_0(Etw):
    pattern = Struct(
        "Sender" / WString,
        "Application" / WString,
        "Version" / WString,
        "Subject" / WString,
        "Reason" / Int32ul,
        "RecipientCount" / Int32ul,
        "Recipient" / WString,
        "AttachmentCount" / Int32ul,
        "AttachmentName" / WString,
        "EmailAccount" / WString
    )


@declare(guid=guid("01090065-b467-4503-9b28-533766761087"), event_id=6, version=0)
class Microsoft_Windows_ParentalControls_6_0(Etw):
    pattern = Struct(
        "Application" / WString,
        "Version" / WString,
        "MediaType" / Int32ul,
        "Path" / WString,
        "Title" / WString,
        "PML" / Int32ul,
        "Album" / WString,
        "ExplicitContent" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("01090065-b467-4503-9b28-533766761087"), event_id=7, version=0)
class Microsoft_Windows_ParentalControls_7_0(Etw):
    pattern = Struct(
        "Application" / WString,
        "Version" / WString,
        "AccountName" / WString,
        "ConversationID" / WString,
        "RequestingIP" / WString,
        "Sender" / WString,
        "Reason" / Int32ul,
        "RecipientCount" / Int32ul,
        "Recipient" / WString
    )


@declare(guid=guid("01090065-b467-4503-9b28-533766761087"), event_id=8, version=0)
class Microsoft_Windows_ParentalControls_8_0(Etw):
    pattern = Struct(
        "Application" / WString,
        "Version" / WString,
        "AccountName" / WString,
        "ConversationID" / WString,
        "JoiningIP" / WString,
        "JoiningUser" / WString,
        "Reason" / Int32ul,
        "MemberCount" / Int32ul,
        "Member" / WString,
        "Sender" / WString
    )


@declare(guid=guid("01090065-b467-4503-9b28-533766761087"), event_id=9, version=0)
class Microsoft_Windows_ParentalControls_9_0(Etw):
    pattern = Struct(
        "Application" / WString,
        "Version" / WString,
        "AccountName" / WString,
        "ConversationID" / WString,
        "LeavingIP" / WString,
        "LeavingUser" / WString,
        "Reason" / Int32ul,
        "MemberCount" / Int32ul,
        "Member" / WString,
        "Flags" / Int32ul
    )


@declare(guid=guid("01090065-b467-4503-9b28-533766761087"), event_id=10, version=0)
class Microsoft_Windows_ParentalControls_10_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "Application" / WString,
        "Version" / WString,
        "Reason" / Int32ul,
        "Path" / WString
    )


@declare(guid=guid("01090065-b467-4503-9b28-533766761087"), event_id=11, version=0)
class Microsoft_Windows_ParentalControls_11_0(Etw):
    pattern = Struct(
        "Application" / WString,
        "Version" / WString,
        "AccountName" / WString,
        "ConversationID" / WString,
        "MediaType" / Int32ul,
        "Reason" / Int32ul,
        "RecipientCount" / Int32ul,
        "Recipient" / WString,
        "Sender" / WString,
        "SenderIP" / WString,
        "Data" / WString
    )


@declare(guid=guid("01090065-b467-4503-9b28-533766761087"), event_id=13, version=0)
class Microsoft_Windows_ParentalControls_13_0(Etw):
    pattern = Struct(
        "Publisher" / WString,
        "Application" / WString,
        "Version" / WString,
        "Event" / WString,
        "Value1" / WString,
        "Value2" / WString,
        "Value3" / WString,
        "Blocked" / Int32ul,
        "Reason" / WString
    )


@declare(guid=guid("01090065-b467-4503-9b28-533766761087"), event_id=14, version=0)
class Microsoft_Windows_ParentalControls_14_0(Etw):
    pattern = Struct(
        "Application" / WString,
        "Version" / WString,
        "OldName" / WString,
        "OldAddress" / WString,
        "NewName" / WString,
        "NewAddress" / WString,
        "Reason" / Int32ul,
        "EmailAccount" / WString
    )


@declare(guid=guid("01090065-b467-4503-9b28-533766761087"), event_id=15, version=0)
class Microsoft_Windows_ParentalControls_15_0(Etw):
    pattern = Struct(
        "Application" / WString,
        "Version" / WString,
        "AccountName" / WString,
        "OldName" / WString,
        "OldID" / WString,
        "NewName" / WString,
        "NewID" / WString,
        "Reason" / Int32ul
    )


@declare(guid=guid("01090065-b467-4503-9b28-533766761087"), event_id=16, version=0)
class Microsoft_Windows_ParentalControls_16_0(Etw):
    pattern = Struct(
        "Timestamp" / SystemTime,
        "UserID" / WString,
        "Path" / WString,
        "RuleID" / WString
    )


@declare(guid=guid("01090065-b467-4503-9b28-533766761087"), event_id=17, version=0)
class Microsoft_Windows_ParentalControls_17_0(Etw):
    pattern = Struct(
        "UserID" / WString,
        "Path" / WString,
        "Reason" / Int32ul
    )


@declare(guid=guid("01090065-b467-4503-9b28-533766761087"), event_id=18, version=0)
class Microsoft_Windows_ParentalControls_18_0(Etw):
    pattern = Struct(
        "UserID" / WString,
        "URL" / WString,
        "Reason" / Int32ul
    )


@declare(guid=guid("01090065-b467-4503-9b28-533766761087"), event_id=19, version=0)
class Microsoft_Windows_ParentalControls_19_0(Etw):
    pattern = Struct(
        "Url" / WString,
        "Decision" / Int32ul,
        "Categories" / WString,
        "BlockedCategories" / WString,
        "SerializedApplication" / WString,
        "Title" / WString,
        "ContentType" / WString,
        "Referrer" / WString,
        "Telemetry" / WString
    )


@declare(guid=guid("01090065-b467-4503-9b28-533766761087"), event_id=20, version=0)
class Microsoft_Windows_ParentalControls_20_0(Etw):
    pattern = Struct(
        "SerializedApplication" / WString,
        "State" / Int32ul,
        "ProcessId" / Int32ul,
        "CreationTime" / Int64ul,
        "TimeUsed" / Int64ul
    )


@declare(guid=guid("01090065-b467-4503-9b28-533766761087"), event_id=21, version=0)
class Microsoft_Windows_ParentalControls_21_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "TimeUsed" / Int64ul
    )


@declare(guid=guid("01090065-b467-4503-9b28-533766761087"), event_id=22, version=0)
class Microsoft_Windows_ParentalControls_22_0(Etw):
    pattern = Struct(
        "ContentProviderId" / WString,
        "ContentProviderTitle" / WString,
        "Id" / WString,
        "Title" / WString,
        "Category" / Int32ul,
        "Ratings" / WString,
        "Decision" / Int32ul
    )

