# -*- coding: utf-8 -*-
"""
Microsoft-Windows-HttpService
GUID : dd5ef90a-6398-47a4-ad34-4dcecdef795f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=1, version=0)
class Microsoft_Windows_HttpService_1_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "ConnectionId" / Int64ul,
        "RemoteAddrLength" / Int32ul,
        "RemoteAddr" / Bytes(lambda this: this.RemoteAddrLength)
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=2, version=0)
class Microsoft_Windows_HttpService_2_0(Etw):
    pattern = Struct(
        "RequestObj" / Int64ul,
        "HttpVerb" / Int32ul,
        "Url" / WString
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=3, version=0)
class Microsoft_Windows_HttpService_3_0(Etw):
    pattern = Struct(
        "RequestObj" / Int64ul,
        "RequestId" / Int64ul,
        "SiteId" / Int32ul,
        "RequestQueueName" / WString,
        "Url" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=4, version=0)
class Microsoft_Windows_HttpService_4_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "ConnectionId" / Int64ul,
        "StatusCode" / Int16ul,
        "Verb" / CString,
        "HeaderLength" / Int32ul,
        "EntityChunkCount" / Int16ul,
        "CachePolicy" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=5, version=0)
class Microsoft_Windows_HttpService_5_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=6, version=0)
class Microsoft_Windows_HttpService_6_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "ConnectionId" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=7, version=0)
class Microsoft_Windows_HttpService_7_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=8, version=0)
class Microsoft_Windows_HttpService_8_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "ConnectionId" / Int64ul,
        "StatusCode" / Int16ul,
        "Verb" / CString,
        "HeaderLength" / Int32ul,
        "EntityChunkCount" / Int16ul,
        "CachePolicy" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=9, version=0)
class Microsoft_Windows_HttpService_9_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=10, version=0)
class Microsoft_Windows_HttpService_10_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "HttpStatus" / Int16ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=11, version=0)
class Microsoft_Windows_HttpService_11_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "HttpStatus" / Int16ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=12, version=0)
class Microsoft_Windows_HttpService_12_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "HttpStatus" / Int16ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=13, version=0)
class Microsoft_Windows_HttpService_13_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "HttpStatus" / Int16ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=14, version=0)
class Microsoft_Windows_HttpService_14_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "HttpStatus" / Int16ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=15, version=0)
class Microsoft_Windows_HttpService_15_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "Reason" / CString,
        "Status" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=16, version=0)
class Microsoft_Windows_HttpService_16_0(Etw):
    pattern = Struct(
        "RequestObj" / Int64ul,
        "SiteId" / Int32ul,
        "BytesSent" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=16, version=1)
class Microsoft_Windows_HttpService_16_1(Etw):
    pattern = Struct(
        "RequestObj" / Int64ul,
        "SiteId" / Int32ul,
        "BytesSent" / Int32ul,
        "RequestId" / Int64ul,
        "Encoding" / CString
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=17, version=0)
class Microsoft_Windows_HttpService_17_0(Etw):
    pattern = Struct(
        "RequestObj" / Int64ul,
        "SiteId" / Int32ul,
        "BytesSent" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=17, version=1)
class Microsoft_Windows_HttpService_17_1(Etw):
    pattern = Struct(
        "RequestObj" / Int64ul,
        "SiteId" / Int32ul,
        "BytesSent" / Int32ul,
        "RequestId" / Int64ul,
        "Encoding" / CString
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=18, version=0)
class Microsoft_Windows_HttpService_18_0(Etw):
    pattern = Struct(
        "Url" / WString,
        "ReserveStatus" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=19, version=0)
class Microsoft_Windows_HttpService_19_0(Etw):
    pattern = Struct(
        "IpAddrLength" / Int32ul,
        "IpAddress" / Bytes(lambda this: this.IpAddrLength)
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=20, version=0)
class Microsoft_Windows_HttpService_20_0(Etw):
    pattern = Struct(
        "EndpointConfigObj" / Int64ul,
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength),
        "CertHashLength" / Int32ul,
        "CertHash" / Bytes(lambda this: this.CertHashLength),
        "CertStoreName" / WString,
        "CertCheckMode" / Int32ul,
        "RevokeFreshnessTime" / Int32ul,
        "RevokeRetrievalTime" / Int32ul,
        "Flags" / Int32ul,
        "CtlId" / WString,
        "CtlStoreName" / WString
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=20, version=1)
class Microsoft_Windows_HttpService_20_1(Etw):
    pattern = Struct(
        "EndpointConfigObj" / Int64ul,
        "Endpoint" / WString,
        "CertHashLength" / Int32ul,
        "CertHash" / Bytes(lambda this: this.CertHashLength),
        "CertStoreName" / WString,
        "CertCheckMode" / Int32ul,
        "RevokeFreshnessTime" / Int32ul,
        "RevokeRetrievalTime" / Int32ul,
        "Flags" / Int32ul,
        "CtlId" / WString,
        "CtlStoreName" / WString,
        "CertificateLoadTimems" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=21, version=0)
class Microsoft_Windows_HttpService_21_0(Etw):
    pattern = Struct(
        "ConnectionObj" / Int64ul,
        "LocalAddrLength" / Int32ul,
        "LocalAddr" / Bytes(lambda this: this.LocalAddrLength),
        "RemoteAddrLength" / Int32ul,
        "RemoteAddr" / Bytes(lambda this: this.RemoteAddrLength)
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=22, version=0)
class Microsoft_Windows_HttpService_22_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "ConnectionId" / Int64ul,
        "ConnectionObj" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=23, version=0)
class Microsoft_Windows_HttpService_23_0(Etw):
    pattern = Struct(
        "ConnectionObj" / Int64ul,
        "Abortive" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=24, version=0)
class Microsoft_Windows_HttpService_24_0(Etw):
    pattern = Struct(
        "ConnectionObj" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=25, version=0)
class Microsoft_Windows_HttpService_25_0(Etw):
    pattern = Struct(
        "Uri" / WString,
        "StatusCode" / Int16ul,
        "Verb" / CString,
        "HeaderLength" / Int32ul,
        "ContentLength" / Int32ul,
        "ExpirationTime" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=25, version=1)
class Microsoft_Windows_HttpService_25_1(Etw):
    pattern = Struct(
        "Uri" / WString,
        "StatusCode" / Int16ul,
        "Verb" / CString,
        "HeaderLength" / Int32ul,
        "ContentLength" / Int32ul,
        "ExpirationTime" / Int64ul,
        "Encoding" / CString
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=26, version=0)
class Microsoft_Windows_HttpService_26_0(Etw):
    pattern = Struct(
        "UrlBuffer" / WString,
        "ErrorStatus" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=26, version=1)
class Microsoft_Windows_HttpService_26_1(Etw):
    pattern = Struct(
        "UrlBuffer" / WString,
        "ErrorStatus" / Int32ul,
        "Encoding" / CString
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=27, version=0)
class Microsoft_Windows_HttpService_27_0(Etw):
    pattern = Struct(
        "Uri" / WString,
        "StatusCode" / Int16ul,
        "Verb" / CString,
        "HeaderLength" / Int32ul,
        "ContentLength" / Int32ul,
        "ExpirationTime" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=28, version=0)
class Microsoft_Windows_HttpService_28_0(Etw):
    pattern = Struct(
        "Property" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=29, version=0)
class Microsoft_Windows_HttpService_29_0(Etw):
    pattern = Struct(
        "Property" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=30, version=0)
class Microsoft_Windows_HttpService_30_0(Etw):
    pattern = Struct(
        "Property" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=31, version=0)
class Microsoft_Windows_HttpService_31_0(Etw):
    pattern = Struct(
        "UrlGroupId" / Int64ul,
        "Url" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=32, version=0)
class Microsoft_Windows_HttpService_32_0(Etw):
    pattern = Struct(
        "UrlGroupId" / Int64ul,
        "Url" / WString
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=33, version=0)
class Microsoft_Windows_HttpService_33_0(Etw):
    pattern = Struct(
        "UrlGroupId" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=34, version=0)
class Microsoft_Windows_HttpService_34_0(Etw):
    pattern = Struct(
        "ConnectionObj" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=35, version=0)
class Microsoft_Windows_HttpService_35_0(Etw):
    pattern = Struct(
        "ConnectionObj" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=36, version=0)
class Microsoft_Windows_HttpService_36_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "ConnectionObj" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=37, version=0)
class Microsoft_Windows_HttpService_37_0(Etw):
    pattern = Struct(
        "ConnectionObj" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=38, version=0)
class Microsoft_Windows_HttpService_38_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "ConnectionObj" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=39, version=0)
class Microsoft_Windows_HttpService_39_0(Etw):
    pattern = Struct(
        "DataLength" / Int32ul,
        "ConnectionObj" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=40, version=0)
class Microsoft_Windows_HttpService_40_0(Etw):
    pattern = Struct(
        "DataLength" / Int32ul,
        "ConnectionObj" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=41, version=0)
class Microsoft_Windows_HttpService_41_0(Etw):
    pattern = Struct(
        "DataLength" / Int32ul,
        "ConnectionObj" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=43, version=0)
class Microsoft_Windows_HttpService_43_0(Etw):
    pattern = Struct(
        "ConnectionId" / Int64ul,
        "AuthType" / CString,
        "SecStatus" / Int32ul,
        "AuthStatus" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=43, version=1)
class Microsoft_Windows_HttpService_43_1(Etw):
    pattern = Struct(
        "ConnectionId" / Int64ul,
        "AuthType" / CString,
        "SecStatus" / Int32ul,
        "AuthStatus" / Int32ul,
        "ContextAttributes" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=44, version=0)
class Microsoft_Windows_HttpService_44_0(Etw):
    pattern = Struct(
        "ConnectionId" / Int64ul,
        "AuthCacheType" / CString,
        "AccessTokenOrHandle" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=45, version=0)
class Microsoft_Windows_HttpService_45_0(Etw):
    pattern = Struct(
        "AccessTokenOrHandle" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=46, version=0)
class Microsoft_Windows_HttpService_46_0(Etw):
    pattern = Struct(
        "ConnectionId" / Int64ul,
        "Bandwidth" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=47, version=0)
class Microsoft_Windows_HttpService_47_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "Type" / Int32ul,
        "Group" / Int32ul,
        "Directory" / WString,
        "Software" / WString,
        "SiteId" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=48, version=0)
class Microsoft_Windows_HttpService_48_0(Etw):
    pattern = Struct(
        "Present" / Int32ul,
        "Type" / Int32ul,
        "Group" / Int32ul,
        "Format" / Int32ul,
        "Directory" / WString,
        "Software" / WString,
        "SiteId" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=49, version=0)
class Microsoft_Windows_HttpService_49_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "Type" / Int32ul,
        "Group" / Int32ul,
        "Format" / Int32ul,
        "Filename" / WString,
        "SiteId" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=50, version=0)
class Microsoft_Windows_HttpService_50_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "Type" / Int32ul,
        "Group" / Int32ul,
        "Format" / Int32ul,
        "Filename" / WString,
        "SiteId" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=51, version=0)
class Microsoft_Windows_HttpService_51_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "Handle" / Int64ul,
        "Type" / Int32ul,
        "Group" / Int32ul,
        "Format" / Int32ul,
        "ResType" / CString,
        "SiteId" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=52, version=0)
class Microsoft_Windows_HttpService_52_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "RequestId" / Int64ul,
        "Reason" / CString,
        "ErrorCode" / Int32ul,
        "HintLength" / Int32ul,
        "HintData" / Bytes(lambda this: this.HintLength)
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=53, version=0)
class Microsoft_Windows_HttpService_53_0(Etw):
    pattern = Struct(
        "ConnectionId" / Int64ul,
        "ConnectionObj" / Int64ul,
        "Timer" / CString
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=56, version=0)
class Microsoft_Windows_HttpService_56_0(Etw):
    pattern = Struct(
        "EndpointConfigObj" / Int64ul,
        "SecStatus" / Int32ul,
        "Detail" / CString
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=57, version=0)
class Microsoft_Windows_HttpService_57_0(Etw):
    pattern = Struct(
        "ConnectionObj" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=58, version=0)
class Microsoft_Windows_HttpService_58_0(Etw):
    pattern = Struct(
        "ConnectionObj" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=59, version=0)
class Microsoft_Windows_HttpService_59_0(Etw):
    pattern = Struct(
        "ConnectionObj" / Int64ul,
        "SecStatus" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=60, version=0)
class Microsoft_Windows_HttpService_60_0(Etw):
    pattern = Struct(
        "ConnectionObj" / Int64ul,
        "SecStatus" / Int32ul,
        "Detail" / CString
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=61, version=0)
class Microsoft_Windows_HttpService_61_0(Etw):
    pattern = Struct(
        "ConnectionObj" / Int64ul,
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength)
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=62, version=0)
class Microsoft_Windows_HttpService_62_0(Etw):
    pattern = Struct(
        "ConnectionObj" / Int64ul,
        "SecStatus" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=63, version=0)
class Microsoft_Windows_HttpService_63_0(Etw):
    pattern = Struct(
        "ConnectionObj" / Int64ul,
        "SecStatus" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=64, version=0)
class Microsoft_Windows_HttpService_64_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "Reason" / CString,
        "RequestQueueName" / WString
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=65, version=0)
class Microsoft_Windows_HttpService_65_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "Reason" / CString,
        "RequestQueueName" / WString
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=66, version=0)
class Microsoft_Windows_HttpService_66_0(Etw):
    pattern = Struct(
        "NewProcNumber" / Int8ul,
        "ReasonString" / CString,
        "Status" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=67, version=0)
class Microsoft_Windows_HttpService_67_0(Etw):
    pattern = Struct(
        "NewProcNumber" / Int8ul,
        "Comment" / CString
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=68, version=0)
class Microsoft_Windows_HttpService_68_0(Etw):
    pattern = Struct(
        "FlowHandle" / Int64ul,
        "Bandwidth" / Int32ul,
        "PeakBandwidth" / Int32ul,
        "BurstSize" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=69, version=0)
class Microsoft_Windows_HttpService_69_0(Etw):
    pattern = Struct(
        "FlowHandle" / Int64ul,
        "Bandwidth" / Int32ul,
        "PeakBandwidth" / Int32ul,
        "BurstSize" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=70, version=0)
class Microsoft_Windows_HttpService_70_0(Etw):
    pattern = Struct(
        "Bandwidth" / Int32ul,
        "PeakBandwidth" / Int32ul,
        "BurstSize" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=71, version=0)
class Microsoft_Windows_HttpService_71_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "FlowHandle" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=72, version=0)
class Microsoft_Windows_HttpService_72_0(Etw):
    pattern = Struct(
        "FlowHandle" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=73, version=0)
class Microsoft_Windows_HttpService_73_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "FlowHandle" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=74, version=0)
class Microsoft_Windows_HttpService_74_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "ContentBytes" / Int64ul,
        "NumberOfRanges" / Int32ul,
        "Range1Start" / Int64ul,
        "Range1End" / Int64ul,
        "Range2Start" / Int64ul,
        "Range2End" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=75, version=0)
class Microsoft_Windows_HttpService_75_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "NumberOfSlices" / Int32ul,
        "SliceIndex1" / Int32ul,
        "SliceIndex2" / Int32ul,
        "NumberOfRanges" / Int32ul,
        "Range1Start" / Int64ul,
        "Range1End" / Int64ul,
        "Range2Start" / Int64ul,
        "Range2End" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=76, version=0)
class Microsoft_Windows_HttpService_76_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "CacheEntryPtr" / Int64ul,
        "NumberOfSlices" / Int32ul,
        "SliceIndex1" / Int32ul,
        "SliceIndex2" / Int32ul,
        "NumberOfRanges" / Int32ul,
        "Range1Start" / Int64ul,
        "Range1End" / Int64ul,
        "Range2Start" / Int64ul,
        "Range2End" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=77, version=0)
class Microsoft_Windows_HttpService_77_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "CacheEntryPtr" / Int64ul,
        "NumberOfSlices" / Int32ul,
        "SliceIndex1" / Int32ul,
        "SliceIndex2" / Int32ul,
        "NumberOfRanges" / Int32ul,
        "Range1Start" / Int64ul,
        "Range1End" / Int64ul,
        "Range2Start" / Int64ul,
        "Range2End" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=78, version=0)
class Microsoft_Windows_HttpService_78_0(Etw):
    pattern = Struct(
        "CacheEntryPtr" / Int64ul,
        "NofSlicesToMerge" / Int32ul,
        "NofSlicesInCache" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=79, version=0)
class Microsoft_Windows_HttpService_79_0(Etw):
    pattern = Struct(
        "CacheEntryPtr" / Int64ul,
        "Range1Start" / Int64ul,
        "Range1End" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=80, version=0)
class Microsoft_Windows_HttpService_80_0(Etw):
    pattern = Struct(
        "ConnectionId" / Int64ul,
        "NoBindBuffers" / Int32ul,
        "SecFlags" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=81, version=0)
class Microsoft_Windows_HttpService_81_0(Etw):
    pattern = Struct(
        "ConnectionId" / Int64ul,
        "SecContextL" / Int64ul,
        "SecContextH" / Int64ul,
        "SecStatus" / Int32ul,
        "Target" / WString
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=82, version=0)
class Microsoft_Windows_HttpService_82_0(Etw):
    pattern = Struct(
        "Hardening" / Int8ul,
        "Flags" / Int32ul,
        "ServiceNameCount" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=83, version=0)
class Microsoft_Windows_HttpService_83_0(Etw):
    pattern = Struct(
        "ReplaceConfigOf" / CString
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=84, version=0)
class Microsoft_Windows_HttpService_84_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "FlowHandle" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=85, version=0)
class Microsoft_Windows_HttpService_85_0(Etw):
    pattern = Struct(
        "PoolType" / CString,
        "ActivePools" / Int16ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=86, version=0)
class Microsoft_Windows_HttpService_86_0(Etw):
    pattern = Struct(
        "PoolType" / CString,
        "ActivePools" / Int16ul,
        "ThreadCount" / Int8ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=87, version=0)
class Microsoft_Windows_HttpService_87_0(Etw):
    pattern = Struct(
        "PoolType" / CString,
        "ActivePools" / Int16ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=88, version=0)
class Microsoft_Windows_HttpService_88_0(Etw):
    pattern = Struct(
        "PoolType" / CString,
        "ActivePools" / Int16ul,
        "ThreadCount" / Int8ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=89, version=0)
class Microsoft_Windows_HttpService_89_0(Etw):
    pattern = Struct(
        "ConnectionObj" / Int64ul,
        "Status" / Int32ul,
        "SniLength" / Int32ul,
        "SniHost" / Bytes(lambda this: this.SniLength),
        "NormalizedHost" / WString
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=90, version=0)
class Microsoft_Windows_HttpService_90_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=91, version=0)
class Microsoft_Windows_HttpService_91_0(Etw):
    pattern = Struct(
        "EndpointConfigObj" / Int64ul,
        "EndpointName" / WString
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=92, version=0)
class Microsoft_Windows_HttpService_92_0(Etw):
    pattern = Struct(
        "EndpointConfigObj" / Int64ul,
        "EndpointName" / WString
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=93, version=0)
class Microsoft_Windows_HttpService_93_0(Etw):
    pattern = Struct(
        "EndpointConfigObj" / Int64ul,
        "IpAddrLength" / Int32ul,
        "IpAddress" / Bytes(lambda this: this.IpAddrLength),
        "SniHostname" / WString,
        "MatchingEndpointName" / WString,
        "AutoGeneratedEndpoint" / Int8ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=94, version=0)
class Microsoft_Windows_HttpService_94_0(Etw):
    pattern = Struct(
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength)
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=95, version=0)
class Microsoft_Windows_HttpService_95_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "ResponseId" / Int64ul,
        "Reason" / CString,
        "ErrorCode" / Int32ul,
        "HintLength" / Int32ul,
        "HintData" / Bytes(lambda this: this.HintLength)
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=96, version=0)
class Microsoft_Windows_HttpService_96_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "SniHostname" / WString,
        "ThumbprintLength" / Int16ul,
        "Thumbprint" / Bytes(lambda this: this.ThumbprintLength),
        "ClientDisconnect" / Int8ul,
        "AbortiveDisconnect" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=97, version=0)
class Microsoft_Windows_HttpService_97_0(Etw):
    pattern = Struct(
        "Url" / WString,
        "Verb" / Int32ul,
        "StatusCode" / Int16ul,
        "CacheSend" / Int8ul,
        "RequestQueue" / WString,
        "ProcessId" / Int32ul,
        "ThreadId" / Int32ul,
        "ImageFileName" / CString,
        "WorkingSetSize" / Int64ul,
        "SendStatus" / Int32ul,
        "ThreadCount" / Int32ul,
        "ReasonPhrase" / CString,
        "ErrorCause" / CString,
        "Verbosity" / Int32ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=98, version=0)
class Microsoft_Windows_HttpService_98_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "SniHostname" / WString,
        "ThumbprintLength" / Int16ul,
        "Thumbprint" / Bytes(lambda this: this.ThumbprintLength),
        "ConnectionBufferFull" / Int8ul
    )


@declare(guid=guid("dd5ef90a-6398-47a4-ad34-4dcecdef795f"), event_id=99, version=0)
class Microsoft_Windows_HttpService_99_0(Etw):
    pattern = Struct(
        "Verb" / Int32ul,
        "FaultCode" / Int32ul
    )

