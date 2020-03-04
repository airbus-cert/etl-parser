# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WorkFolders
GUID : 34a3697e-0f10-4e48-af3c-f869b5babebb
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2, version=0)
class Microsoft_Windows_WorkFolders_2_0(Etw):
    pattern = Struct(
        "LocalFolder" / WString,
        "ServerURI" / WString,
        "ServerPartnershipId" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=3, version=0)
class Microsoft_Windows_WorkFolders_3_0(Etw):
    pattern = Struct(
        "LocalFolder" / WString,
        "ServerURI" / WString,
        "ServerPartnershipId" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=4, version=0)
class Microsoft_Windows_WorkFolders_4_0(Etw):
    pattern = Struct(
        "LocalFolder" / WString,
        "ServerURI" / WString,
        "ServerPartnershipId" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=5, version=0)
class Microsoft_Windows_WorkFolders_5_0(Etw):
    pattern = Struct(
        "SyncUrl" / WString,
        "AutoProvision" / Int8ul,
        "GhostingPolicy" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=6, version=0)
class Microsoft_Windows_WorkFolders_6_0(Etw):
    pattern = Struct(
        "DiscoveryUrl" / WString,
        "ServerUrl" / WString,
        "GhostingPolicy" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=7, version=0)
class Microsoft_Windows_WorkFolders_7_0(Etw):
    pattern = Struct(
        "PartnershipId" / WString,
        "PartnershipType" / WString,
        "DiscoveryUrl" / WString,
        "ServerUrl" / WString,
        "GhostingPolicy" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=9, version=0)
class Microsoft_Windows_WorkFolders_9_0(Etw):
    pattern = Struct(
        "DiscoveryUrl" / WString,
        "ServerUrl" / WString,
        "ConfiguredByPolicy" / Int8ul,
        "GhostingPolicy" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=10, version=0)
class Microsoft_Windows_WorkFolders_10_0(Etw):
    pattern = Struct(
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=11, version=0)
class Microsoft_Windows_WorkFolders_11_0(Etw):
    pattern = Struct(
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=12, version=0)
class Microsoft_Windows_WorkFolders_12_0(Etw):
    pattern = Struct(
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=13, version=0)
class Microsoft_Windows_WorkFolders_13_0(Etw):
    pattern = Struct(
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=14, version=0)
class Microsoft_Windows_WorkFolders_14_0(Etw):
    pattern = Struct(
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=15, version=0)
class Microsoft_Windows_WorkFolders_15_0(Etw):
    pattern = Struct(
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=16, version=0)
class Microsoft_Windows_WorkFolders_16_0(Etw):
    pattern = Struct(
        "DiscoveryURL" / WString,
        "ServerURL" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=17, version=0)
class Microsoft_Windows_WorkFolders_17_0(Etw):
    pattern = Struct(
        "ServerURL" / WString,
        "SyncTargetType" / WString,
        "ServerPartnershipId" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=18, version=0)
class Microsoft_Windows_WorkFolders_18_0(Etw):
    pattern = Struct(
        "UserEmail" / WString,
        "DiscoveryURL" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=19, version=0)
class Microsoft_Windows_WorkFolders_19_0(Etw):
    pattern = Struct(
        "ServerURL" / WString,
        "SyncTargetType" / WString,
        "ServerPartnershipId" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=502, version=0)
class Microsoft_Windows_WorkFolders_502_0(Etw):
    pattern = Struct(
        "LocalFolder" / WString,
        "ServerURI" / WString,
        "ServerPartnershipId" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=503, version=0)
class Microsoft_Windows_WorkFolders_503_0(Etw):
    pattern = Struct(
        "LocalFolder" / WString,
        "ServerURI" / WString,
        "ServerPartnershipId" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=516, version=0)
class Microsoft_Windows_WorkFolders_516_0(Etw):
    pattern = Struct(
        "DiscoveryURL" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=517, version=0)
class Microsoft_Windows_WorkFolders_517_0(Etw):
    pattern = Struct(
        "ServerURL" / WString,
        "SyncTargetType" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=518, version=0)
class Microsoft_Windows_WorkFolders_518_0(Etw):
    pattern = Struct(
        "UserEmail" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=1000, version=0)
class Microsoft_Windows_WorkFolders_1000_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "SizeMB" / Int64sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=1001, version=0)
class Microsoft_Windows_WorkFolders_1001_0(Etw):
    pattern = Struct(
        "User" / WString,
        "StsUri" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=1002, version=0)
class Microsoft_Windows_WorkFolders_1002_0(Etw):
    pattern = Struct(
        "User" / WString,
        "StsUri" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=1100, version=0)
class Microsoft_Windows_WorkFolders_1100_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "SyncId" / Guid,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=1101, version=0)
class Microsoft_Windows_WorkFolders_1101_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "SyncId" / Guid,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=1102, version=0)
class Microsoft_Windows_WorkFolders_1102_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "SyncId" / Guid,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=1103, version=0)
class Microsoft_Windows_WorkFolders_1103_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "SyncId" / Guid,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=1104, version=0)
class Microsoft_Windows_WorkFolders_1104_0(Etw):
    pattern = Struct(
        "SyncPartnershipId" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=1105, version=0)
class Microsoft_Windows_WorkFolders_1105_0(Etw):
    pattern = Struct(
        "SyncPartnershipId" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=1106, version=0)
class Microsoft_Windows_WorkFolders_1106_0(Etw):
    pattern = Struct(
        "SyncPartnershipId" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=1107, version=0)
class Microsoft_Windows_WorkFolders_1107_0(Etw):
    pattern = Struct(
        "SyncPartnershipId" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2000, version=0)
class Microsoft_Windows_WorkFolders_2000_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2001, version=0)
class Microsoft_Windows_WorkFolders_2001_0(Etw):
    pattern = Struct(
        "SessionUri" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2002, version=0)
class Microsoft_Windows_WorkFolders_2002_0(Etw):
    pattern = Struct(
        "SessionUri" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2003, version=0)
class Microsoft_Windows_WorkFolders_2003_0(Etw):
    pattern = Struct(
        "SuccessFileCount" / Int32sl,
        "SuccessDataSize" / Int64sl,
        "FailedFileCount" / Int32sl,
        "FailedDataSize" / Int64sl,
        "TotalBatchTime" / Int32sl,
        "Rate" / Float32l
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2004, version=0)
class Microsoft_Windows_WorkFolders_2004_0(Etw):
    pattern = Struct(
        "SuccessFileCount" / Int32sl,
        "SuccessDataSize" / Int64sl,
        "FailedFileCount" / Int32sl,
        "FailedDataSize" / Int64sl,
        "TotalBatchTime" / Int32sl,
        "Rate" / Float32l
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2005, version=0)
class Microsoft_Windows_WorkFolders_2005_0(Etw):
    pattern = Struct(
        "Uri" / WString,
        "Verb" / WString,
        "Headers" / WString,
        "BodyLength" / Int32sl,
        "HttpResponse" / Int32sl,
        "ServerCodeStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2006, version=0)
class Microsoft_Windows_WorkFolders_2006_0(Etw):
    pattern = Struct(
        "SyncId" / Guid,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2007, version=0)
class Microsoft_Windows_WorkFolders_2007_0(Etw):
    pattern = Struct(
        "Username" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2008, version=0)
class Microsoft_Windows_WorkFolders_2008_0(Etw):
    pattern = Struct(
        "Username" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2009, version=0)
class Microsoft_Windows_WorkFolders_2009_0(Etw):
    pattern = Struct(
        "ItemName" / WString,
        "SyncGID" / Guid,
        "Action" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2010, version=0)
class Microsoft_Windows_WorkFolders_2010_0(Etw):
    pattern = Struct(
        "ItemName" / WString,
        "SyncGID" / Guid,
        "Action" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2011, version=0)
class Microsoft_Windows_WorkFolders_2011_0(Etw):
    pattern = Struct(
        "ItemName" / WString,
        "SyncGID" / Guid,
        "Action" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2012, version=0)
class Microsoft_Windows_WorkFolders_2012_0(Etw):
    pattern = Struct(
        "ItemName" / WString,
        "SyncGID" / Guid,
        "Action" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2013, version=0)
class Microsoft_Windows_WorkFolders_2013_0(Etw):
    pattern = Struct(
        "ConcurrencyConflict" / Int8ul,
        "SourceItemName" / WString,
        "SourceSyncGID" / Guid,
        "DestinationItemName" / WString,
        "DestinationSyncGID" / Guid,
        "DataWinner" / WString,
        "NamespaceWinner" / WString,
        "AttributesWinner" / WString,
        "TieBreakerWinner" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2014, version=0)
class Microsoft_Windows_WorkFolders_2014_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2015, version=0)
class Microsoft_Windows_WorkFolders_2015_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2016, version=0)
class Microsoft_Windows_WorkFolders_2016_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2017, version=0)
class Microsoft_Windows_WorkFolders_2017_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2018, version=0)
class Microsoft_Windows_WorkFolders_2018_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2019, version=0)
class Microsoft_Windows_WorkFolders_2019_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2020, version=0)
class Microsoft_Windows_WorkFolders_2020_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2021, version=0)
class Microsoft_Windows_WorkFolders_2021_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2022, version=0)
class Microsoft_Windows_WorkFolders_2022_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2023, version=0)
class Microsoft_Windows_WorkFolders_2023_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2026, version=0)
class Microsoft_Windows_WorkFolders_2026_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2027, version=0)
class Microsoft_Windows_WorkFolders_2027_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2100, version=0)
class Microsoft_Windows_WorkFolders_2100_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2101, version=0)
class Microsoft_Windows_WorkFolders_2101_0(Etw):
    pattern = Struct(
        "SyncPartnershipId" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2102, version=0)
class Microsoft_Windows_WorkFolders_2102_0(Etw):
    pattern = Struct(
        "SyncPartnershipId" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2103, version=0)
class Microsoft_Windows_WorkFolders_2103_0(Etw):
    pattern = Struct(
        "SyncPartnershipId" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2104, version=0)
class Microsoft_Windows_WorkFolders_2104_0(Etw):
    pattern = Struct(
        "DatabasePath" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2105, version=0)
class Microsoft_Windows_WorkFolders_2105_0(Etw):
    pattern = Struct(
        "DatabasePath" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2106, version=0)
class Microsoft_Windows_WorkFolders_2106_0(Etw):
    pattern = Struct(
        "LocalEpoch" / Guid,
        "ServerEpoch" / Guid
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2107, version=0)
class Microsoft_Windows_WorkFolders_2107_0(Etw):
    pattern = Struct(
        "DatabasePath" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2108, version=0)
class Microsoft_Windows_WorkFolders_2108_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2109, version=0)
class Microsoft_Windows_WorkFolders_2109_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2110, version=0)
class Microsoft_Windows_WorkFolders_2110_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2111, version=0)
class Microsoft_Windows_WorkFolders_2111_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2112, version=0)
class Microsoft_Windows_WorkFolders_2112_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2113, version=0)
class Microsoft_Windows_WorkFolders_2113_0(Etw):
    pattern = Struct(
        "ItemName" / WString,
        "SyncGID" / Guid,
        "Action" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2114, version=0)
class Microsoft_Windows_WorkFolders_2114_0(Etw):
    pattern = Struct(
        "ItemName" / WString,
        "SyncGID" / Guid,
        "Action" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2115, version=0)
class Microsoft_Windows_WorkFolders_2115_0(Etw):
    pattern = Struct(
        "DatabasePath" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2116, version=0)
class Microsoft_Windows_WorkFolders_2116_0(Etw):
    pattern = Struct(
        "DatabasePath" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2117, version=0)
class Microsoft_Windows_WorkFolders_2117_0(Etw):
    pattern = Struct(
        "DatabasePath" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2118, version=0)
class Microsoft_Windows_WorkFolders_2118_0(Etw):
    pattern = Struct(
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2119, version=0)
class Microsoft_Windows_WorkFolders_2119_0(Etw):
    pattern = Struct(
        "DatabasePath" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=2120, version=0)
class Microsoft_Windows_WorkFolders_2120_0(Etw):
    pattern = Struct(
        "DatabasePath" / WString,
        "HResultStr" / WString,
        "HResult" / Int32sl
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=8000, version=0)
class Microsoft_Windows_WorkFolders_8000_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=8001, version=0)
class Microsoft_Windows_WorkFolders_8001_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=8002, version=0)
class Microsoft_Windows_WorkFolders_8002_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=8003, version=0)
class Microsoft_Windows_WorkFolders_8003_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=8004, version=0)
class Microsoft_Windows_WorkFolders_8004_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString,
        "FullEnumerationOccurred" / Int8ul
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=8005, version=0)
class Microsoft_Windows_WorkFolders_8005_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=8006, version=0)
class Microsoft_Windows_WorkFolders_8006_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=8007, version=0)
class Microsoft_Windows_WorkFolders_8007_0(Etw):
    pattern = Struct(
        "ServerPartnershipId" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=8008, version=0)
class Microsoft_Windows_WorkFolders_8008_0(Etw):
    pattern = Struct(
        "ServerPartnershipId" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=8009, version=0)
class Microsoft_Windows_WorkFolders_8009_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=8010, version=0)
class Microsoft_Windows_WorkFolders_8010_0(Etw):
    pattern = Struct(
        "ServerPartnershipId" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=8011, version=0)
class Microsoft_Windows_WorkFolders_8011_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=8012, version=0)
class Microsoft_Windows_WorkFolders_8012_0(Etw):
    pattern = Struct(
        "ServerPartnershipId" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=8015, version=0)
class Microsoft_Windows_WorkFolders_8015_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=8016, version=0)
class Microsoft_Windows_WorkFolders_8016_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=8019, version=0)
class Microsoft_Windows_WorkFolders_8019_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=8020, version=0)
class Microsoft_Windows_WorkFolders_8020_0(Etw):
    pattern = Struct(
        "LocalReplicaRoot" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=9001, version=0)
class Microsoft_Windows_WorkFolders_9001_0(Etw):
    pattern = Struct(
        "hc_stateid" / Int32ul,
        "Application" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=9002, version=0)
class Microsoft_Windows_WorkFolders_9002_0(Etw):
    pattern = Struct(
        "hc_stateid" / Int32ul,
        "Application" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=9003, version=0)
class Microsoft_Windows_WorkFolders_9003_0(Etw):
    pattern = Struct(
        "hc_stateid" / Int32ul,
        "Application" / WString
    )


@declare(guid=guid("34a3697e-0f10-4e48-af3c-f869b5babebb"), event_id=9004, version=0)
class Microsoft_Windows_WorkFolders_9004_0(Etw):
    pattern = Struct(
        "hc_stateid" / Int32ul,
        "Application" / WString
    )

