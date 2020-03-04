# -*- coding: utf-8 -*-
"""
Microsoft-Windows-BranchCacheMonitoring
GUID : a2f55524-8ebc-45fd-88e4-a1b39f169e08
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=1, version=0)
class Microsoft_Windows_BranchCacheMonitoring_1_0(Etw):
    pattern = Struct(
        "Registrar" / WString,
        "Mode" / Int32ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=2, version=0)
class Microsoft_Windows_BranchCacheMonitoring_2_0(Etw):
    pattern = Struct(
        "Registrar" / WString,
        "Mode" / Int32ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=101, version=0)
class Microsoft_Windows_BranchCacheMonitoring_101_0(Etw):
    pattern = Struct(
        "CompletedDataDownloads" / Int64ul,
        "SuccessfulDataDownloads" / Int64ul,
        "MaxObservedSimultaneousDownloads" / Int64ul,
        "AverageDownloadByteRate" / Int64ul,
        "CompletedDataUploads" / Int64ul,
        "SuccessfulDataUploads" / Int64ul,
        "MaxObservedSimultaneousUploads" / Int64ul,
        "AverageServingLatency" / Int32ul,
        "MaxObservedServingLatency" / Int32ul,
        "CurrentAverageInboundRequestFrequency" / Double,
        "MaxObservedAverageInboundRequestFrequency" / Double,
        "AverageDiscoveryTime" / Int64ul,
        "AttemptedNetworkDiscoveries" / Int64ul,
        "AttemptedV1NetworkDiscoveries" / Int64ul,
        "AttemptedV2NetworkDiscoveries" / Int64ul,
        "SuccessfulNetworkDiscoveries" / Int64ul,
        "SuccessfulV1NetworkDiscoveries" / Int64ul,
        "SuccessfulV2NetworkDiscoveries" / Int64ul,
        "SuppressedDiscoveries" / Int64ul,
        "PreDiscoveries" / Int64ul,
        "CurrentAverageInboundDiscoveryFrequency" / Double,
        "MaxObservedAverageInboundDiscoveryFrequency" / Double,
        "TotalBytesServed" / Int64ul,
        "TotalBytesRetrieved" / Int64ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=102, version=0)
class Microsoft_Windows_BranchCacheMonitoring_102_0(Etw):
    pattern = Struct(
        "ContentIdSize" / Int32ul,
        "ContentId" / Bytes(lambda this: this.ContentIdSize),
        "StringContentId" / WString,
        "SegmentIdSize" / Int32ul,
        "SegmentId" / Bytes(lambda this: this.SegmentIdSize),
        "SegmentOffsetInContent" / Int64ul,
        "SegmentSize" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=103, version=0)
class Microsoft_Windows_BranchCacheMonitoring_103_0(Etw):
    pattern = Struct(
        "ContentIdSize" / Int32ul,
        "ContentId" / Bytes(lambda this: this.ContentIdSize),
        "StringContentId" / WString,
        "SegmentIdSize" / Int32ul,
        "SegmentId" / Bytes(lambda this: this.SegmentIdSize),
        "SegmentOffsetInContent" / Int64ul,
        "SegmentSize" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=104, version=0)
class Microsoft_Windows_BranchCacheMonitoring_104_0(Etw):
    pattern = Struct(
        "ContentIdSize" / Int32ul,
        "ContentId" / Bytes(lambda this: this.ContentIdSize),
        "StringContentId" / WString,
        "SegmentIdSize" / Int32ul,
        "SegmentId" / Bytes(lambda this: this.SegmentIdSize),
        "DataOffsetInSegment" / Int64ul,
        "DataSize" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=105, version=0)
class Microsoft_Windows_BranchCacheMonitoring_105_0(Etw):
    pattern = Struct(
        "ContentIdSize" / Int32ul,
        "ContentId" / Bytes(lambda this: this.ContentIdSize),
        "StringContentId" / WString,
        "SegmentIdSize" / Int32ul,
        "SegmentId" / Bytes(lambda this: this.SegmentIdSize),
        "ContentOffset" / Int64ul,
        "SegmentOffset" / Int64ul,
        "Bytes" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=106, version=0)
class Microsoft_Windows_BranchCacheMonitoring_106_0(Etw):
    pattern = Struct(
        "ContentIdSize" / Int32ul,
        "ContentId" / Bytes(lambda this: this.ContentIdSize),
        "StringContentId" / WString,
        "SegmentIdSize" / Int32ul,
        "SegmentId" / Bytes(lambda this: this.SegmentIdSize),
        "ContentOffset" / Int64ul,
        "SegmentOffset" / Int64ul,
        "Bytes" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=107, version=0)
class Microsoft_Windows_BranchCacheMonitoring_107_0(Etw):
    pattern = Struct(
        "SegmentIdSize" / Int32ul,
        "SegmentId" / Bytes(lambda this: this.SegmentIdSize),
        "HostName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=108, version=0)
class Microsoft_Windows_BranchCacheMonitoring_108_0(Etw):
    pattern = Struct(
        "SegmentIdSize" / Int32ul,
        "SegmentId" / Bytes(lambda this: this.SegmentIdSize),
        "HostName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=109, version=0)
class Microsoft_Windows_BranchCacheMonitoring_109_0(Etw):
    pattern = Struct(
        "SegmentIdSize" / Int32ul,
        "SegmentId" / Bytes(lambda this: this.SegmentIdSize),
        "HostName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=110, version=0)
class Microsoft_Windows_BranchCacheMonitoring_110_0(Etw):
    pattern = Struct(
        "SegmentIdSize" / Int32ul,
        "SegmentId" / Bytes(lambda this: this.SegmentIdSize),
        "HostName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=111, version=0)
class Microsoft_Windows_BranchCacheMonitoring_111_0(Etw):
    pattern = Struct(
        "SegmentIdSize" / Int32ul,
        "SegmentId" / Bytes(lambda this: this.SegmentIdSize),
        "HostName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=112, version=0)
class Microsoft_Windows_BranchCacheMonitoring_112_0(Etw):
    pattern = Struct(
        "SegmentIdSize" / Int32ul,
        "SegmentId" / Bytes(lambda this: this.SegmentIdSize),
        "HostName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=113, version=0)
class Microsoft_Windows_BranchCacheMonitoring_113_0(Etw):
    pattern = Struct(
        "SegmentIdSize" / Int32ul,
        "SegmentId" / Bytes(lambda this: this.SegmentIdSize),
        "BlockId" / Int32ul,
        "BlockSize" / Int32ul,
        "HostName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=114, version=0)
class Microsoft_Windows_BranchCacheMonitoring_114_0(Etw):
    pattern = Struct(
        "SegmentIdSize" / Int32ul,
        "SegmentId" / Bytes(lambda this: this.SegmentIdSize),
        "BlockId" / Int32ul,
        "BlockSize" / Int32ul,
        "HostName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=115, version=0)
class Microsoft_Windows_BranchCacheMonitoring_115_0(Etw):
    pattern = Struct(
        "SegmentIdSize" / Int32ul,
        "SegmentId" / Bytes(lambda this: this.SegmentIdSize),
        "BlockId" / Int32ul,
        "BlockSize" / Int32ul,
        "HostName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=116, version=0)
class Microsoft_Windows_BranchCacheMonitoring_116_0(Etw):
    pattern = Struct(
        "SegmentIdSize" / Int32ul,
        "SegmentId" / Bytes(lambda this: this.SegmentIdSize),
        "BlockId" / Int32ul,
        "BlockSize" / Int32ul,
        "HostName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=201, version=0)
class Microsoft_Windows_BranchCacheMonitoring_201_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "URL" / WString,
        "ClientIPv4Address" / Int32ul,
        "RangeRequest" / Int8ul,
        "RangeCount" / Int32ul,
        "FirstRangeOffset" / Int64ul,
        "FirstRangeLenght" / Int64ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=202, version=0)
class Microsoft_Windows_BranchCacheMonitoring_202_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "URL" / WString,
        "ClientIPv4Address" / Int32ul,
        "PeerDistMinContentInformationVersion" / Int64ul,
        "PeerDistMaxContentInformationVersion" / Int64ul,
        "PCCRTPProtocolVersion" / Int64ul,
        "RangeRequest" / Int8ul,
        "RangeCount" / Int32ul,
        "FirstRangeOffset" / Int64ul,
        "FirstRangeLenght" / Int64ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=203, version=0)
class Microsoft_Windows_BranchCacheMonitoring_203_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "URL" / WString,
        "ClientIPv4Address" / Int32ul,
        "RangeRequest" / Int8ul,
        "RangeCount" / Int32ul,
        "FirstRangeOffset" / Int64ul,
        "FirstRangeLenght" / Int64ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=204, version=0)
class Microsoft_Windows_BranchCacheMonitoring_204_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "URL" / WString,
        "ClientIPv4Address" / Int32ul,
        "PeerDistMinContentInformationVersion" / Int64ul,
        "PeerDistMaxContentInformationVersion" / Int64ul,
        "PCCRTPProtocolVersion" / Int64ul,
        "RangeRequest" / Int8ul,
        "RangeCount" / Int32ul,
        "FirstRangeOffset" / Int64ul,
        "FirstRangeLenght" / Int64ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=205, version=0)
class Microsoft_Windows_BranchCacheMonitoring_205_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "URL" / WString,
        "ClientIPv4Address" / Int32ul,
        "RangeRequest" / Int8ul,
        "RangeCount" / Int32ul,
        "FirstRangeOffset" / Int64ul,
        "FirstRangeLenght" / Int64ul,
        "HTTPProtocolMajorVersion" / Int16ul,
        "HTTPProtocolMinorVersion" / Int16ul,
        "HTTPStatusCode" / Int16ul,
        "OriginalContentLength" / Int64ul,
        "EncodedContentLength" / Int64ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=206, version=0)
class Microsoft_Windows_BranchCacheMonitoring_206_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "URL" / WString,
        "ClientIPv4Address" / Int32ul,
        "PeerDistMinContentInformationVersion" / Int64ul,
        "PeerDistMaxContentInformationVersion" / Int64ul,
        "PCCRTPProtocolVersion" / Int64ul,
        "RangeRequest" / Int8ul,
        "RangeCount" / Int32ul,
        "FirstRangeOffset" / Int64ul,
        "FirstRangeLenght" / Int64ul,
        "HTTPProtocolMajorVersion" / Int16ul,
        "HTTPProtocolMinorVersion" / Int16ul,
        "HTTPStatusCode" / Int16ul,
        "OriginalContentLength" / Int64ul,
        "EncodedContentLength" / Int64ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=207, version=0)
class Microsoft_Windows_BranchCacheMonitoring_207_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "URL" / WString,
        "ClientIPv4Address" / Int32ul,
        "PeerDistMinContentInformationVersion" / Int64ul,
        "PeerDistMaxContentInformationVersion" / Int64ul,
        "PCCRTPProtocolVersion" / Int64ul,
        "RangeRequest" / Int8ul,
        "RangeCount" / Int32ul,
        "FirstRangeOffset" / Int64ul,
        "FirstRangeLenght" / Int64ul,
        "HTTPProtocolMajorVersion" / Int16ul,
        "HTTPProtocolMinorVersion" / Int16ul,
        "HTTPStatusCode" / Int16ul,
        "OriginalContentLength" / Int64ul,
        "EncodedContentLength" / Int64ul
    )


@declare(guid=guid("a2f55524-8ebc-45fd-88e4-a1b39f169e08"), event_id=208, version=0)
class Microsoft_Windows_BranchCacheMonitoring_208_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "URL" / WString,
        "ClientIPv4Address" / Int32ul,
        "RangeRequest" / Int8ul,
        "RangeCount" / Int32ul,
        "FirstRangeOffset" / Int64ul,
        "FirstRangeLenght" / Int64ul,
        "HTTPProtocolMajorVersion" / Int16ul,
        "HTTPProtocolMinorVersion" / Int16ul,
        "HTTPStatusCode" / Int16ul,
        "OriginalContentLength" / Int64ul,
        "EncodedContentLength" / Int64ul
    )

