# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Bits-Client
GUID : ef1cc15b-46c1-414e-bb95-e76b077bd51e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=1, version=0)
class Microsoft_Windows_Bits_Client_1_0(Etw):
    pattern = Struct(
        "JobGuid" / Guid,
        "Title" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=2, version=0)
class Microsoft_Windows_Bits_Client_2_0(Etw):
    pattern = Struct(
        "JobGuid" / Guid,
        "Title" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=3, version=0)
class Microsoft_Windows_Bits_Client_3_0(Etw):
    pattern = Struct(
        "string" / WString,
        "string2" / WString,
        "string3" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=3, version=1)
class Microsoft_Windows_Bits_Client_3_1(Etw):
    pattern = Struct(
        "jobTitle" / WString,
        "jobId" / Guid,
        "jobOwner" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=3, version=2)
class Microsoft_Windows_Bits_Client_3_2(Etw):
    pattern = Struct(
        "jobTitle" / WString,
        "jobId" / Guid,
        "jobOwner" / WString,
        "processPath" / WString,
        "processId" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=4, version=0)
class Microsoft_Windows_Bits_Client_4_0(Etw):
    pattern = Struct(
        "User" / WString,
        "jobTitle" / WString,
        "jobId" / Guid,
        "jobOwner" / WString,
        "fileCount" / Int64ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=4, version=1)
class Microsoft_Windows_Bits_Client_4_1(Etw):
    pattern = Struct(
        "User" / WString,
        "jobTitle" / WString,
        "jobId" / Guid,
        "jobOwner" / WString,
        "fileCount" / Int64ul,
        "bytesTransferred" / Int64ul,
        "bytesTransferredFromPeer" / Int64ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=5, version=0)
class Microsoft_Windows_Bits_Client_5_0(Etw):
    pattern = Struct(
        "User" / WString,
        "jobTitle" / WString,
        "jobId" / Guid,
        "jobOwner" / WString,
        "fileCount" / Int64ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=11, version=0)
class Microsoft_Windows_Bits_Client_11_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=14, version=0)
class Microsoft_Windows_Bits_Client_14_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=17, version=0)
class Microsoft_Windows_Bits_Client_17_0(Etw):
    pattern = Struct(
        "peerCacheEnabled" / Int8ul,
        "peerClientEnabled" / Int8ul,
        "peerServerEnabled" / Int8ul,
        "maxPeers" / Int32ul,
        "maxClients" / Int32ul,
        "maxContentAge" / Int32ul,
        "maxCacheSize" / Int32ul,
        "minCacheDiskSize" / Int32ul,
        "cacheDenyUrls" / WString,
        "denyUrlCount" / Int8ul,
        "denyUrls" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=18, version=0)
class Microsoft_Windows_Bits_Client_18_0(Etw):
    pattern = Struct(
        "packet" / WString,
        "hr" / Int32ul,
        "fqdn" / WString,
        "addressCount" / Int8ul,
        "addresses" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=19, version=0)
class Microsoft_Windows_Bits_Client_19_0(Etw):
    pattern = Struct(
        "fqdn" / WString,
        "authenticated" / Int8ul,
        "online" / Int8ul,
        "addressCount" / Int8ul,
        "addressLength" / Int16ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=20, version=0)
class Microsoft_Windows_Bits_Client_20_0(Etw):
    pattern = Struct(
        "fqdn" / WString,
        "authenticated" / Int8ul,
        "online" / Int8ul,
        "addressCount" / Int8ul,
        "addressLength" / Int16ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=21, version=0)
class Microsoft_Windows_Bits_Client_21_0(Etw):
    pattern = Struct(
        "fqdn" / WString,
        "authenticated" / Int8ul,
        "online" / Int8ul,
        "addressCount" / Int8ul,
        "addressLength" / Int16ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=22, version=0)
class Microsoft_Windows_Bits_Client_22_0(Etw):
    pattern = Struct(
        "fqdn" / WString,
        "authenticated" / Int8ul,
        "online" / Int8ul,
        "addressCount" / Int8ul,
        "addressLength" / Int16ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=23, version=0)
class Microsoft_Windows_Bits_Client_23_0(Etw):
    pattern = Struct(
        "user" / Sid
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=24, version=0)
class Microsoft_Windows_Bits_Client_24_0(Etw):
    pattern = Struct(

    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=25, version=0)
class Microsoft_Windows_Bits_Client_25_0(Etw):
    pattern = Struct(
        "packet" / WString,
        "hr" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=27, version=0)
class Microsoft_Windows_Bits_Client_27_0(Etw):
    pattern = Struct(
        "searchId" / Guid,
        "jobId" / Guid,
        "url" / WString,
        "timestamp" / Int64ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=28, version=0)
class Microsoft_Windows_Bits_Client_28_0(Etw):
    pattern = Struct(
        "searchId" / Guid,
        "jobId" / Guid
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=29, version=0)
class Microsoft_Windows_Bits_Client_29_0(Etw):
    pattern = Struct(
        "requestId" / Guid,
        "searchId" / Guid,
        "peer" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=30, version=0)
class Microsoft_Windows_Bits_Client_30_0(Etw):
    pattern = Struct(
        "requestId" / Guid,
        "SearchId" / Guid,
        "hr" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=31, version=0)
class Microsoft_Windows_Bits_Client_31_0(Etw):
    pattern = Struct(
        "requestId" / Guid,
        "SearchId" / Guid,
        "hr" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=32, version=0)
class Microsoft_Windows_Bits_Client_32_0(Etw):
    pattern = Struct(
        "requestId" / Guid,
        "id" / Guid,
        "url" / WString,
        "rangecount" / Int16ul,
        "Range" / Int16sl
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=33, version=0)
class Microsoft_Windows_Bits_Client_33_0(Etw):
    pattern = Struct(
        "count" / Int8ul,
        "addresses" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=34, version=0)
class Microsoft_Windows_Bits_Client_34_0(Etw):
    pattern = Struct(
        "jobName" / WString,
        "jobId" / Guid,
        "FileCount" / Int64ul,
        "jobTransferPolicy" / Int32ul,
        "globalTransferPolicy" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=37, version=0)
class Microsoft_Windows_Bits_Client_37_0(Etw):
    pattern = Struct(
        "nlmCost" / Int32ul,
        "usage" / Int32ul,
        "cap" / Int32ul,
        "isThrottled" / Int32ul,
        "isOvercap" / Int32ul,
        "isRoaming" / Int32ul,
        "globalTransferPolicy" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=59, version=0)
class Microsoft_Windows_Bits_Client_59_0(Etw):
    pattern = Struct(
        "transferId" / Guid,
        "name" / WString,
        "Id" / Guid,
        "url" / WString,
        "peer" / WString,
        "fileTime" / Int64ul,
        "fileLength" / Int64ul,
        "bytesTotal" / Int64ul,
        "bytesTransferred" / Int64ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=59, version=1)
class Microsoft_Windows_Bits_Client_59_1(Etw):
    pattern = Struct(
        "transferId" / Guid,
        "name" / WString,
        "Id" / Guid,
        "url" / WString,
        "peer" / WString,
        "fileTime" / Int64ul,
        "fileLength" / Int64ul,
        "bytesTotal" / Int64ul,
        "bytesTransferred" / Int64ul,
        "bytesTransferredFromPeer" / Int64ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=60, version=0)
class Microsoft_Windows_Bits_Client_60_0(Etw):
    pattern = Struct(
        "transferId" / Guid,
        "name" / WString,
        "Id" / Guid,
        "url" / WString,
        "peer" / WString,
        "hr" / Int32ul,
        "fileTime" / Int64ul,
        "fileLength" / Int64ul,
        "bytesTotal" / Int64ul,
        "bytesTransferred" / Int64ul,
        "proxy" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=60, version=1)
class Microsoft_Windows_Bits_Client_60_1(Etw):
    pattern = Struct(
        "transferId" / Guid,
        "name" / WString,
        "Id" / Guid,
        "url" / WString,
        "peer" / WString,
        "hr" / Int32ul,
        "fileTime" / Int64ul,
        "fileLength" / Int64ul,
        "bytesTotal" / Int64ul,
        "bytesTransferred" / Int64ul,
        "proxy" / WString,
        "peerProtocolFlags" / Int64ul,
        "bytesTransferredFromPeer" / Int64ul,
        "AdditionalInfoHr" / Int32ul,
        "PeerContextInfo" / Int32ul,
        "bandwidthLimit" / Int64ul,
        "ignoreBandwidthLimitsOnLan" / Int8ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=61, version=0)
class Microsoft_Windows_Bits_Client_61_0(Etw):
    pattern = Struct(
        "transferId" / Guid,
        "name" / WString,
        "Id" / Guid,
        "url" / WString,
        "peer" / WString,
        "hr" / Int32ul,
        "fileTime" / Int64ul,
        "fileLength" / Int64ul,
        "bytesTotal" / Int64ul,
        "bytesTransferred" / Int64ul,
        "proxy" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=61, version=1)
class Microsoft_Windows_Bits_Client_61_1(Etw):
    pattern = Struct(
        "transferId" / Guid,
        "name" / WString,
        "Id" / Guid,
        "url" / WString,
        "peer" / WString,
        "hr" / Int32ul,
        "fileTime" / Int64ul,
        "fileLength" / Int64ul,
        "bytesTotal" / Int64ul,
        "bytesTransferred" / Int64ul,
        "proxy" / WString,
        "peerProtocolFlags" / Int64ul,
        "bytesTransferredFromPeer" / Int64ul,
        "AdditionalInfoHr" / Int32ul,
        "PeerContextInfo" / Int32ul,
        "bandwidthLimit" / Int64ul,
        "ignoreBandwidthLimitsOnLan" / Int8ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=62, version=0)
class Microsoft_Windows_Bits_Client_62_0(Etw):
    pattern = Struct(
        "Title" / WString,
        "Owner" / WString,
        "Url" / WString,
        "Id" / Guid
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=63, version=0)
class Microsoft_Windows_Bits_Client_63_0(Etw):
    pattern = Struct(
        "Job" / WString,
        "Url" / WString,
        "Pgm" / WString,
        "hr" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=64, version=0)
class Microsoft_Windows_Bits_Client_64_0(Etw):
    pattern = Struct(
        "Job" / WString,
        "Url" / WString,
        "Pgm" / WString,
        "hr" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=70, version=0)
class Microsoft_Windows_Bits_Client_70_0(Etw):
    pattern = Struct(

    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=71, version=0)
class Microsoft_Windows_Bits_Client_71_0(Etw):
    pattern = Struct(
        "url" / WString,
        "timestamp" / Int64ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=72, version=0)
class Microsoft_Windows_Bits_Client_72_0(Etw):
    pattern = Struct(
        "id" / Guid,
        "url" / WString,
        "rangecount" / Int16ul,
        "Range" / Int8ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=73, version=0)
class Microsoft_Windows_Bits_Client_73_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=74, version=0)
class Microsoft_Windows_Bits_Client_74_0(Etw):
    pattern = Struct(
        "status" / Int16ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=78, version=0)
class Microsoft_Windows_Bits_Client_78_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=81, version=0)
class Microsoft_Windows_Bits_Client_81_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=82, version=0)
class Microsoft_Windows_Bits_Client_82_0(Etw):
    pattern = Struct(
        "Title" / WString,
        "PolicyValue" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=83, version=0)
class Microsoft_Windows_Bits_Client_83_0(Etw):
    pattern = Struct(
        "Title" / WString,
        "PolicyValue" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=101, version=0)
class Microsoft_Windows_Bits_Client_101_0(Etw):
    pattern = Struct(
        "requestId" / Guid,
        "responseXml" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=102, version=0)
class Microsoft_Windows_Bits_Client_102_0(Etw):
    pattern = Struct(
        "xferId" / Guid,
        "count" / Int8ul,
        "ranges" / Int8sl
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=200, version=0)
class Microsoft_Windows_Bits_Client_200_0(Etw):
    pattern = Struct(
        "url" / WString,
        "hr" / Int32ul,
        "proxy" / WString,
        "job" / WString,
        "owner" / WString,
        "jobId" / Guid,
        "xferId" / Guid,
        "proxyServerList" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=201, version=0)
class Microsoft_Windows_Bits_Client_201_0(Etw):
    pattern = Struct(
        "job" / WString,
        "jobId" / Guid,
        "jobOwner" / WString,
        "url" / WString,
        "transferId" / Guid,
        "proxyServerList" / WString,
        "proxyBypassList" / WString,
        "error" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=202, version=0)
class Microsoft_Windows_Bits_Client_202_0(Etw):
    pattern = Struct(
        "jobName" / WString,
        "jobOwner" / WString,
        "jobId" / Guid,
        "url" / WString,
        "xferId" / Guid,
        "proxy" / WString,
        "hr" / Int32ul,
        "fileLength" / Int64ul,
        "HTTPVersion" / WString,
        "URLRange" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=203, version=0)
class Microsoft_Windows_Bits_Client_203_0(Etw):
    pattern = Struct(
        "string" / WString,
        "string2" / WString,
        "string3" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=203, version=1)
class Microsoft_Windows_Bits_Client_203_1(Etw):
    pattern = Struct(
        "server" / WString,
        "job" / WString,
        "url" / WString,
        "scheme" / WString,
        "user" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=204, version=0)
class Microsoft_Windows_Bits_Client_204_0(Etw):
    pattern = Struct(
        "string" / WString,
        "string2" / WString,
        "string3" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=204, version=1)
class Microsoft_Windows_Bits_Client_204_1(Etw):
    pattern = Struct(
        "server" / WString,
        "job" / WString,
        "url" / WString,
        "scheme" / WString,
        "user" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=205, version=0)
class Microsoft_Windows_Bits_Client_205_0(Etw):
    pattern = Struct(
        "profileType" / Int8ul,
        "currSlotStartTime" / Int64ul,
        "currSlotBandwidthLimit" / Int64ul,
        "nextSlotStartTime" / Int64ul,
        "nextSlotBandwidthLimit" / Int64ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=206, version=0)
class Microsoft_Windows_Bits_Client_206_0(Etw):
    pattern = Struct(
        "jobName" / WString,
        "url" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=207, version=0)
class Microsoft_Windows_Bits_Client_207_0(Etw):
    pattern = Struct(
        "jobName" / WString,
        "url" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=208, version=0)
class Microsoft_Windows_Bits_Client_208_0(Etw):
    pattern = Struct(
        "jobName" / WString,
        "url" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=209, version=0)
class Microsoft_Windows_Bits_Client_209_0(Etw):
    pattern = Struct(
        "jobName" / WString,
        "jobId" / Guid,
        "isRoaming" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=210, version=0)
class Microsoft_Windows_Bits_Client_210_0(Etw):
    pattern = Struct(
        "jobName" / WString,
        "url" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=211, version=0)
class Microsoft_Windows_Bits_Client_211_0(Etw):
    pattern = Struct(
        "JobGuid" / Guid,
        "Title" / WString,
        "ErrorCode" / Int32ul,
        "Message" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=212, version=0)
class Microsoft_Windows_Bits_Client_212_0(Etw):
    pattern = Struct(
        "SystemEvent" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=213, version=0)
class Microsoft_Windows_Bits_Client_213_0(Etw):
    pattern = Struct(
        "jobName" / WString,
        "jobId" / Guid,
        "FileCount" / Int64ul,
        "BlockReasonErrorCode" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=307, version=0)
class Microsoft_Windows_Bits_Client_307_0(Etw):
    pattern = Struct(
        "number" / Double
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=308, version=0)
class Microsoft_Windows_Bits_Client_308_0(Etw):
    pattern = Struct(
        "number" / Double
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=310, version=0)
class Microsoft_Windows_Bits_Client_310_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=311, version=0)
class Microsoft_Windows_Bits_Client_311_0(Etw):
    pattern = Struct(
        "JobId" / Guid,
        "JobName" / WString,
        "url" / WString,
        "ErrorCode" / Int32ul,
        "ErrorContext" / Int8ul,
        "bytesTransferredFromPeer" / Int64ul,
        "PeerProtocolFlags" / Int64ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=312, version=0)
class Microsoft_Windows_Bits_Client_312_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=16384, version=0)
class Microsoft_Windows_Bits_Client_16384_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Title" / WString,
        "Owner" / WString,
        "User" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=16385, version=0)
class Microsoft_Windows_Bits_Client_16385_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Title" / WString,
        "FileList" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=16386, version=0)
class Microsoft_Windows_Bits_Client_16386_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Title" / WString,
        "FileList" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=16387, version=0)
class Microsoft_Windows_Bits_Client_16387_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Title" / WString,
        "Owner" / WString,
        "PropertyName" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=16388, version=0)
class Microsoft_Windows_Bits_Client_16388_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Title" / WString,
        "Owner" / WString,
        "User" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=16389, version=0)
class Microsoft_Windows_Bits_Client_16389_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Title" / WString,
        "Owner" / WString,
        "DayCount" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=16390, version=0)
class Microsoft_Windows_Bits_Client_16390_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Title" / WString,
        "Owner" / WString,
        "RetryWaitTime" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=16392, version=0)
class Microsoft_Windows_Bits_Client_16392_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=16393, version=0)
class Microsoft_Windows_Bits_Client_16393_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=16396, version=0)
class Microsoft_Windows_Bits_Client_16396_0(Etw):
    pattern = Struct(
        "rule" / WString,
        "enabled" / Int8ul,
        "status" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=16397, version=0)
class Microsoft_Windows_Bits_Client_16397_0(Etw):
    pattern = Struct(
        "entityName" / WString,
        "currentSize" / Int32ul,
        "currentLimit" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=16398, version=0)
class Microsoft_Windows_Bits_Client_16398_0(Etw):
    pattern = Struct(
        "entityName" / WString,
        "currentSize" / Int32ul,
        "currentLimit" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=16400, version=0)
class Microsoft_Windows_Bits_Client_16400_0(Etw):
    pattern = Struct(
        "entityName" / WString,
        "currentSize" / Int32ul,
        "currentLimit" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=16401, version=0)
class Microsoft_Windows_Bits_Client_16401_0(Etw):
    pattern = Struct(
        "entityName" / WString,
        "currentSize" / Int32ul,
        "currentLimit" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=16402, version=0)
class Microsoft_Windows_Bits_Client_16402_0(Etw):
    pattern = Struct(
        "entityName" / WString,
        "currentSize" / Int32ul,
        "currentLimit" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=16404, version=0)
class Microsoft_Windows_Bits_Client_16404_0(Etw):
    pattern = Struct(
        "function" / WString,
        "line" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=16405, version=0)
class Microsoft_Windows_Bits_Client_16405_0(Etw):
    pattern = Struct(
        "Key" / WString,
        "SubKeyOrValueName" / WString
    )


@declare(guid=guid("ef1cc15b-46c1-414e-bb95-e76b077bd51e"), event_id=17005, version=0)
class Microsoft_Windows_Bits_Client_17005_0(Etw):
    pattern = Struct(
        "string" / WString,
        "string2" / WString,
        "string3" / WString
    )

